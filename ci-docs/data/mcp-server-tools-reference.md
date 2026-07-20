---
title: Customer Insights MCP Server tools reference (preview)
description: Explore Customer Insights MCP Server tools help agents discover data sources, unify customer profiles, and retrieve segments, measures, and predictions.
ms.date: 07/10/2026
ms.topic: reference
ms.collection: bap-ai-copilot
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Customer Insights MCP Server tools reference (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Customer Insights MCP Server exposes Microsoft Dynamics 365 **Customer Insights - Data** and **Customer Insights - Journeys** capabilities as callable tools for large language model (LLM) agents. 

Through the Model Context Protocol (MCP), an agent can:

- Discover data sources
- Resolve records to unified customer profiles
- Retrieve profile attributes, segments, measures, predictions, enrichments, and consent states
- Perform real actions against live Customer Insights data

All Customer Insights - Data tools read from **Dataverse virtual entities** which reflect live unified customer data.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

Tool names are prefixed by product area:

- **`msdynci_*`**: Customer Insights - Data (unified profiles, segments, measures, predictions, and enrichments)
- **`msdynmkt_*`**: Customer Insights - Journeys (consent and unsubscribe)

## Common tool pattern

Most workflows follow a two-step pattern:

- Resolve a unified customer ID
- Retrieve customer data by using that resolved ID

### Resolve a unified customer ID

Use one of the following tools:

   - `msdynci_findcustomerbyname`: Search for a customer by name
   - `msdynci_getcustomeridforcontact`: Resolve a Dataverse Contact ID to a unified customer ID
   - `msdynci_getcustomerbysourceid`: Resolve an ingested source record to a unified customer ID

### Resolve customer data

After you resolve the customer ID, use one of the following tools: 

   - `msdynci_getcustomerdetails`: Retrieve a complete customer profile and data provenance
   - `msdynci_getcustomersegments`: Retrieve segment memberships
   - `msdynci_getcustomermeasures`: Retrieve KPI and measure values
   - `msdynci_getpredictions`: Retrieve AI and ML prediction scores
   - `msdynci_getclusterinformation`: Retrieve cluster membership information
     
`msdynci_listsources` is a discovery helper for finding valid source entity names to use with `msdynci_getcustomerbysourceid`.

## Tool reference

Many tools require a **unified customer ID** as input. Resolve the ID by using a lookup tool before retrieving customer data. Some tool descriptions don't enumerate explicit input parameters. 

>[!NOTE]
>Confirm exact parameter names and data types against the deployed server definition before publishing.

### Discovery

#### `msdynci_listsources`

Discovers data sources by using the Dataverse virtual entity `msdynci_alternatekey` 

The tool: 

- Finds distinct `(entityName and datasourceName)` pairs.
- Cross-validates each source against `msdynci_customerprofile` columns (pattern: `msdynci_{datasource}_{entity}_{field}`)
- Reports inconsistencies as validation warnings.

Use this tool to discover source entity names (for example, `contact`, `lead`, `contosostorecustomers`) for custom source entities that can be used with `msdynci_getcustomerbysourceid`. No input is required.

### Resolving customer IDs

#### `msdynci_findcustomerbyname`

Searches unified customer profiles by name in the Dataverse virtual entity `msdynci_customerprofile`. Returns matching customers with pagination metadata.

- **Behavior**: If you don't provide a search name, it lists all customers.
- **Paging**: Use `top` to control page size. The response includes `hasMore` to indicate whether more results exist beyond the current page.
- **Returns**: Matching customers, including their unified customer IDs.

#### `msdynci_getcustomeridforcontact`

Returns the unified customer ID for a given **Dataverse Contact ID**. Looks up the `msdynci_alternatekey` entity to resolve a contact record to its unified customer.

This tool is a convenient shortcut for `msdynci_getcustomerbysourceid` with `entityName='contact'`.

#### `msdynci_getcustomerbysourceid`

Returns the unified customer ID for a given **source entity name** and **source record ID**. Looks up `msdynci_alternatekey` to resolve any ingested data source record (for example, `contact`, `lead`, or a custom table row) to its unified customer.

Use `msdynci_listsources` first to find valid source entity names.

### Reading customer data

#### `msdynci_getcustomerdetails`

Returns detailed profile information for a given unified customer ID. Queries the virtual entities `msdynci_customerprofile`, `msdynci_segmentmembership`, `msdynci_customermeasure`, and `msdynci_alternatekey`.

Includes:

- **Core profile attributes**: name, email, address (system columns excluded).
- **Segment memberships**
- **Customer measures**
- **Source records** showing data unification provenance. Each source record includes:
  - `sourceEntityAttributes`: All non-system attributes from the actual source entity such as `contact` or `lead`.
  - `attributeMapping`: How source attributes map to unified profile attributes, with source value, sanitized profile value, and an `isWinner` flag indicating which source provided the winning value.

Use this tool after resolving a customer ID to get the full profile.

#### `msdynci_getcustomersegments`

Returns all segments that a customer is a member of. 

Queries:
- `msdynci_segmentmembership`
- `mscipriv_segmentmetadata`

- **Input**: A `customerId` obtained from `msdynci_findcustomerbyname` or `msdynci_getcustomeridforcontact`.
- **Returns**: A list of segment names and IDs.

#### `msdynci_getcustomermeasures`

Returns customer measures (KPI values) for a given unified customer ID. Queries `msdynci_customermeasure`.

Use this tool to retrieve aggregated measure values like total purchases, average order value, or custom business metrics.

#### `msdynci_getpredictions`

Returns AI/ML prediction results for a given unified customer ID. Queries `msdynci_prediction`.

Includes prediction scores such as churn risk, customer lifetime value, product recommendation scores, and custom prediction model outputs.

#### `msdynci_getclusterinformation`

Returns information about cluster membership for a unified customer ID. Queries `msdynci_customerprofile`.

Clusters are a post-unification rule that matches unified customer profiles that meet select conditions. For example, a household is a common cluster of people that share a common last name and address. If the target unified customer ID is a member of a cluster, the other members of the cluster are returned.

### Customer Insights - Journeys (marketing)

Learn more in [Use consent tools in the Customer Insights MCP server (preview)](../journeys/mcp-server-consent.md).

#### `msdynmkt_checkconsent`

Checks whether consent is given for a specific **purpose**, **topic**, **channel**, and **contact point**.

#### `msdynmkt_getunsubscribelink`

Gets the unsubscribe link for the specified parameters.

## Example workflows

### Look up a customer by name and get their full profile

1. `msdynci_findcustomerbyname`: Pick the matching customer and note their unified ID.
1. `msdynci_getcustomerdetails`: Receive the full profile, segments, measures, and source provenance.

### Enrich a known Dataverse contact

1. `msdynci_getcustomeridforcontact`: Resolve the Contact ID to a unified customer ID.
1. `msdynci_getpredictions` + `msdynci_getclusterinformation`: Receive churn scores, customer lifetime value (CLV) scores, and cluster membership information.

### Resolve an arbitrary source record

1. `msdynci_listsources`: Find the valid source entity name.
1. `msdynci_getcustomerbysourceid`: Resolve the source record to a unified customer ID.
1. `msdynci_getcustomersegments` / `msdynci_getcustomermeasures`: Receive segment and KPI context.

### Check marketing consent before outreach

1. Resolve the customer by using one of the customer resolution methods.
1. `msdynmkt_checkconsent`: Verify consent for the intended purpose, topic, channel, and contact point.

## Related information

[Use tools in the Customer Insights MCP server (preview)](mcp-server-tools.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
