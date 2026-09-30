The Customer Insights [Model Context Protocol (MCP)](https://modelcontextprotocol.io) Server exposes Dynamics 365 **Customer Insights - Data** and **Customer Insights - Journeys** capabilities as callable tools for AI agents and large language model (LLM) clients.

There's a single MCP server for both apps. Instead of calling internal APIs directly, your agents work through one secure interface that applies the same rules Customer Insights enforces everywhere else, including consent rules enforced during journey execution.

Through MCP, an agent can:

- Discover the data sources ingested into Customer Insights
- Resolve a record from a source system to a unified customer profile
- Retrieve profile attributes, segments, measures, predictions, and cluster membership
- Check consent and generate compliant unsubscribe links before sending a message
- Create journeys and validate email content

## Tools at a glance

| Tool | Display title | What it does | Read-only |
|---|---|---|---|
| `find_customer` | **Find Customer** | Searches unified customer profiles by first or last name | Yes |
| `get_customer_by_source_id` | **Resolve Customer By Source Id** | Resolves a unified customer ID from a source system record ID | Yes |
| `get_customer_by_contact` | **Resolve Customer By Contact** | Resolves a unified customer ID from a Dataverse contact GUID | Yes |
| `get_customer_details` | **Get Customer Details** | Returns the full Customer 360 view for one customer | Yes |
| `get_customer_segments` | **Get Customer Segments** | Lists the segments a customer belongs to | Yes |
| `get_customer_measures` | **Get Customer Measures** | Returns calculated measures and KPIs | Yes |
| `get_customer_predictions` | **Get Customer Predictions** | Returns machine learning predictions such as churn probability | Yes |
| `get_cluster_information` | **Get Cluster Information** | Returns cluster membership, such as a household, and other members | Yes |
| `list_data_sources` | **List Data Sources** | Lists ingested data sources and their record counts | Yes |
| `check_consent` | **Check Consent** | Checks consent for a contact point, channel, purpose, and topic | Yes |
| `get_unsubscribe_link` | **Get Unsubscribe Link** | Generates a compliant unsubscribe link for a recipient | Yes |
| `create_journey` | **Create Journey** | Validates, enriches, and creates a journey | No |
| `validate_email` | **Validate Email** | Validates an existing email without changing it | Yes |

`create_journey` is the only tool that writes data. It isn't read-only, destructive, or idempotent, so calling it twice creates two journeys. Every other tool only reads.

## How the tools fit together

Most workflows follow a two-step pattern: resolve a unified customer ID, then use that ID to retrieve customer data.

### Step 1: Resolve a unified customer ID

Pick the tool that matches what you already know about the customer:

- `find_customer` when you have a person's name
- `get_customer_by_contact` when you have a Dataverse contact GUID
- `get_customer_by_source_id` when you have a record ID from an ingested source system, such as a loyalty or ERP system

If you don't know which source entity names are valid, call `list_data_sources` first.

### Step 2: Retrieve customer data

After you resolve the ID, call any of these tools:

- `get_customer_details` for the complete profile and data provenance
- `get_customer_segments` for segment memberships
- `get_customer_measures` for KPI and measure values
- `get_customer_predictions` for AI and machine learning scores
- `get_cluster_information` for cluster membership

## Customer profile tools

These tools read from **Dataverse virtual entities**, which reflect live unified customer data.

### Find Customer

**`find_customer`**

Searches unified customer profiles by first or last name and returns matching customer IDs, names, and email addresses. Use this tool first when the user gives you a person's name but not their unified customer ID.

- **Behavior**: If you don't supply a name, the tool lists profiles instead of searching.
- **Paging**: Use `top` to control the page size. The response includes `hasMore` so you can tell whether more results exist beyond the current page.

### Resolve Customer By Source Id

**`get_customer_by_source_id`**

Resolves a unified customer ID from a record identifier in an ingested source system. Use it when you have an ID from a source such as a loyalty or ERP system and need the matching Customer Insights profile.

Call `list_data_sources` first to find valid source entity names, such as `contact`, `lead`, or a custom table.

### Resolve Customer By Contact

**`get_customer_by_contact`**

Resolves a unified customer ID from a Dataverse contact GUID. Use it when a workflow starts with a contact record and needs the associated Customer Insights profile.

This tool is a shortcut for `get_customer_by_source_id` with the source entity set to `contact`.

### Get Customer Details

**`get_customer_details`**

Returns a complete Customer 360 view for one unified customer. The result includes:

- **Core profile attributes**, such as name, email, and address, with system columns excluded
- **Segment memberships**
- **Customer measures**
- **Clusters**
- **Predictions**
- **Source records** that show data unification provenance

Each source record includes the non-system attributes from the source entity, how those attributes map to unified profile attributes, and a flag that identifies which source contributed the winning value for each unified field.

Use this tool after you resolve a customer ID and you want the full picture in one call.

### Get Customer Segments

**`get_customer_segments`**

Lists the segments or audiences a unified customer belongs to. Each result includes the segment name, display name, and segment ID.

### Get Customer Measures

**`get_customer_measures`**

Returns calculated customer measures and KPIs, such as lifetime value, order counts, and engagement scores. The tool combines measures stored in the supported Customer Insights data layouts into a single result.

Use it to retrieve aggregated values like total purchases, average order value, or custom business metrics.

### Get Customer Predictions

**`get_customer_predictions`**

Returns machine learning predictions for a unified customer, such as churn probability, predicted lifetime value, propensity scores, and next-best-product suggestions. Each result includes the model and provider it came from.

### Get Cluster Information

**`get_cluster_information`**

Returns the clusters a customer belongs to, along with the other members of each cluster and their affinity scores. Cluster types are discovered dynamically from Customer Insights model metadata.

A cluster is a post-unification rule that groups unified profiles meeting a set of conditions. A household, for example, is a common cluster of people who share a last name and an address.

### List Data Sources

**`list_data_sources`**

Lists the data sources ingested into Customer Insights. For each source, the tool reports the source entity, the record count, and whether columns from that source appear in the unified profile. It also flags sources whose fields didn't resolve into profile columns, which is useful when you're troubleshooting unification.

No input is required. Use this tool to discover valid source entity names before you call `get_customer_by_source_id`.

## Consent and compliance tools

These tools delegate to the same backend consent service that Customer Insights - Journeys uses during journey execution, so an agent's decision always matches what a journey would do. The consent service can run independently of a full Customer Insights installation, so these tools are available even in environments where only Dynamics 365 Sales or Contact Center is deployed.

### Check Consent

**`check_consent`**

Checks the consent status for a contact point, communication channel, purpose, and topic. Call it before you recommend or send a communication, to confirm the recipient is eligible. The tool invokes the `msdynmkt_checkconsent` Dataverse custom API and returns the consent service's decision, including the reason a message would be blocked.

#### Typical use case

An agent preparing to send a commercial message calls `check_consent` to verify that the recipient opted in for the relevant purpose and channel.

#### Example

Check consent for contact point `+111111111`, compliance profile `7f4a6355-1811-4cde-bde3-fee8c85f56b1`, purpose `Commercial` (`10000000-0000-0000-0000-000000000003`), channel type `SMS`, business unit `c507f51d-8f0c-ee11-8f6e-6045bd6ef763`, and topic `Commercial Topic 001` (`23db4a4d-ba9f-f011-bbd3-6045bd194648`).

**Result**:

| Parameter | Value |
|---|---|
| Contact point | +111111111 |
| Channel type | SMS |
| Compliance profile ID | 7f4a6355-1811-4cde-bde3-fee8c85f56b1 |
| Purpose | Commercial (ID: 10000000-0000-0000-0000-000000000003) |
| Topic | Commercial Topic 001 (ID: 23db4a4d-ba9f-f011-bbd3-6045bd194648) |
| Business unit | c507f51d-8f0c-ee11-8f6e-6045bd6ef763 |
| **Consent** | ✅ Granted |

The contact point has the opted-in consent required for both the **Commercial** purpose and the **Commercial Topic 001** topic, so SMS messaging to this contact point is permitted under the current compliance settings.

### Get Unsubscribe Link

**`get_unsubscribe_link`**

Generates a compliant unsubscribe link for a recipient and message context. The request identifies the recipient entity, purpose, compliance settings, message template, and contact point. The tool invokes the `msdynmkt_getunsubscribelink` Dataverse custom API.

Each link is unique to the contact point and message context, so you get full traceability and auditability.

When a recipient selects the link, it opens the preference center page associated with the compliance profile. The preference center lets recipients manage their communication preferences, for example, opting out of specific purposes or topics, updating contact points, or unsubscribing from everything. That gives customers real control instead of an all-or-nothing opt-out.

You can customize the look and feel of the preference center to match your brand, including updating text, adding purposes and topics, styling the page with custom CSS, and adding custom JavaScript. Learn more in [Create branded, customized preference centers](/dynamics365/customer-insights/journeys/real-time-marketing-preference-centers).

#### Typical use case

An outreach agent generates a message and calls `get_unsubscribe_link` to embed a one-click opt-out link in the message body.

#### Example

Generate an unsubscribe link for contact point `+111111111`, entity type `Contact` (`f56302b0-875e-f111-a826-7ced8d6d1623`), message template `226abb7d-855e-f111-a826-7ced8d6d1e7c`, compliance profile `7f4a6355-1811-4cde-bde3-fee8c85f56b1`, purpose `10000000-0000-0000-0000-000000000003`, topic `23db4a4d-ba9f-f011-bbd3-6045bd194648`, and business unit `c507f51d-8f0c-ee11-8f6e-6045bd6ef763`.

**Result**:

| Parameter | Value |
|---|---|
| Contact point | +111111111 |
| Entity type | Contact |
| Entity ID | f56302b0-875e-f111-a826-7ced8d6d1623 |
| Message template ID | 226abb7d-855e-f111-a826-7ced8d6d1e7c |
| Compliance profile ID | 7f4a6355-1811-4cde-bde3-fee8c85f56b1 |
| Purpose ID | 10000000-0000-0000-0000-000000000003 |
| Topic ID | 23db4a4d-ba9f-f011-bbd3-6045bd194648 |
| Business unit ID | c507f51d-8f0c-ee11-8f6e-6045bd6ef763 |

**Generated unsubscribe link**:

```text
https://public-fra.mkt.dynamics.com/api/v2.0/orgs/7b2fdebc-d216-ee11-a66d-0022483903fc/consent/preferences?contextId=fd436906-0633-42a9-8426-c3a6edca0100
```

## Journey and email tools

### Create Journey

**`create_journey`**

Validates a complete journey JSON payload, enriches it, validates the enriched payload again, and then creates the Customer Insights - Journeys journey record. The response includes the created journey ID and the validation result.

> [!IMPORTANT]
> `create_journey` is the only tool in the Customer Insights MCP Server that creates data. It isn't idempotent, so retrying a failed call can create a duplicate journey. Have your agent confirm the outcome before it retries.

### Validate Email

**`validate_email`**

Validates an existing Customer Insights - Journeys email without modifying it. The request contains the email message ID, content parts, placeholders, and validation context. The response includes message-level and placeholder-level validation findings.

Use it to catch content problems, such as unresolved placeholders, before a journey sends the message.

## Example workflows

### Look up a customer by name and get their full profile

1. Call `find_customer`, then pick the matching customer and note their unified ID.
1. Call `get_customer_details` to get the profile, segments, measures, and source provenance.

### Enrich a known Dataverse contact

1. Call `get_customer_by_contact` to resolve the contact ID to a unified customer ID.
1. Call `get_customer_predictions` and `get_cluster_information` to get churn scores, customer lifetime value scores, and cluster membership.

### Resolve a record from another source system

1. Call `list_data_sources` to find the valid source entity name.
1. Call `get_customer_by_source_id` to resolve the source record to a unified customer ID.
1. Call `get_customer_segments` or `get_customer_measures` for segment and KPI context.

### Send a compliant message

1. Resolve the customer with one of the resolution tools.
1. Call `check_consent` to confirm the contact is opted in for the purpose, topic, channel, and contact point you intend to use.
1. Call `get_unsubscribe_link` to get a personalized opt-out link.
1. Compose and send the message with the link embedded.

### Build and check a journey

1. Call `create_journey` with the journey payload.
1. Call `validate_email` on the emails the journey uses to confirm the content resolves correctly.

## How it works

The Customer Insights MCP Server is built on the Dataverse custom API pattern. It uses two custom APIs for tool interaction:

- **List tools**: Enumerates all MCP tools registered on the server.
- **Call tool**: Runs a specific MCP tool by name, passing the arguments as JSON.

The server definition lives in the base solution (CxpClient), which ships to every Dynamics 365 organization. Tool providers from Customer Insights - Data and Customer Insights - Journeys are added as solution extensions.

### Architecture overview

The server follows a layered architecture:

1. **Protocol layer**: Custom APIs and Dataverse plugins handle MCP protocol compliance.
1. **Registry layer**: Discovers available tool providers at runtime through reflection-based autodiscovery.
1. **Tool layer**: MCP wrappers that validate inputs and delegate to services.
1. **Service layer**: Business logic that calls the underlying Customer Insights services.
1. **Data layer**: Dataverse virtual entities and Dataverse storage.

### Security

The MCP server enforces security at several layers:

| Layer | Description |
|---|---|
| **Transport security (mTLS)** | Mutual Transport Layer Security certificate-based authentication between the client and Dataverse |
| **Custom API privileges** | The platform validates user privileges before it allows tool discovery or execution |
| **Tool-level authorization** | Each tool checks entity-specific privileges, such as read access to consent purposes |
| **Data-level security** | Row-level security makes sure users only reach data they're authorized to see |

> [!NOTE]
> Authorization is enforced inside the tool logic using the caller's user context. The MCP server never escalates privileges implicitly. Tools act as facades and never do anything beyond what the calling user is permitted to do.

## Prerequisites

Before you use the tools, make sure you have:

- A Dynamics 365 Customer Insights environment. For the consent tools, a Dynamics 365 environment with Shared Consent deployed also works, for example, Dynamics 365 Sales with Shared Consent.
- Access to the Dataverse tables that back the tools you plan to call.
- For the consent tools, at least one compliance profile with purposes and topics. The default compliance profile includes a **Commercial** purpose with restrictive enforcement and a **Transactional** purpose with nonrestrictive enforcement, so you can start right away without extra configuration.
- The Dataverse security role privileges that the tools require for the user or agent identity.

## Limitations

Keep these limitations in mind:

- The consent tools cover consent checks and unsubscribe link generation. Updating consent, administrative operations such as creating or deleting purposes and topics, and consent model metadata retrieval aren't exposed through MCP.
- **Performance**: Calls through MCP can have higher latency than direct service calls during journey execution. Factor this in when you design high-throughput scenarios.
- **Single MCP server**: One server covers both Customer Insights - Journeys and Customer Insights - Data, and all tools share the same server-level scope definition. Tool-level authorization controls access to individual tools.

## Related information

- [Model Context Protocol specification](https://modelcontextprotocol.io)
- [Add tools and resources from an MCP server to your agent](/microsoft-copilot-studio/mcp-add-components-to-agent)
- [Consent management overview](/dynamics365/customer-insights/journeys/real-time-marketing-compliance-settings)
