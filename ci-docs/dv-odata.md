---
title: "Dataverse APIs for Customer Insights"
description: "Overview and examples of Dataverse Open Data Protocol (OData) APIs to query Customer Insights data."
ms.date: 07/06/2023
ms.topic: conceptual
author: srivas15
ms.author: shsri
ms.reviewer: mhart
ms.custom: bap-template
---

# Dataverse APIs for Customer Insights

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

[!INCLUDE [api-deprecate](./includes/api-deprecate.md)]

If you're already using Customer Insights APIs to query data, such as query a Customer Profile or get segment memberships, we recommend you migrate your APIs to Dataverse APIs instead. Support for querying metadata, such as get segment definition and workflow management, is coming soon to Dataverse APIs.

If you're getting started with querying data using APIs, we recommend using Dataverse APIs instead.

> [!IMPORTANT]
> It's recommended to use Dataverse APIs only to read data (GET) and not to write data (POST/PATCH/PUT) as it can cause issues with Customer Insights processing.

Dataverse APIs have the following advantages over Customer Insights APIs:

- Extended capabilities for filtering and sorting

- Improved scale and performance

- Consistent API experience across Dynamics 365 and Power Platform apps

## Sample queries

To get started using Dataverse APIs, [create an application registration in Azure and request permissions for Dataverse](/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory) and [grant your Azure Active Directory app Viewer permissions](permissions.md) on Customer Insights.

Modify the query samples to make them work on the target environments:

- {serviceRoot}: `{Organization URI}/api/data/v9.2/` where {Organization URI} is the URI of the [Dataverse org](customer-insights-dataverse.md) associated to your Customer Insights environment. For example: `https://{mydvorg}.crm.dynamics.com`

- {CID}: GUID of a unified customer record. For example: `ce759201f786d590bf2134bff576c369`.

- {AlternateKey}: Identifier of the primary key of a customer record in a data source. For example: `CNTID_1002`.

- {DSname}: String with the table name of a data source that gets ingested to Customer Insights. For example: `Website_contacts`.

- {SegmentName}: String with the output table name of a segment in Customer Insights. For example: `Male_under_40`.

### Customer

Sample queries for the *CustomerProfile* table and segment memberships.

|Query type |Example  | Note  |
|---------|---------|---------|
|Get all customers | ` {serviceRoot}/msdynci_customerprofiles`  |          |  
|Get a customer by ID | ` {serviceRoot}/msdynci_customerprofiles?$filter=msdynci_customerid eq '{CID}'`  |          |
|Get a customer by Alternate Key | ` {serviceRoot}/msdynci_customerprofiles?$filter={msdynci_alternate_column} eq '{AK}'`  |  Alternate keys persist in the unified customer table in the format msdynci_DSname_TableName_PrimaryKeyColumnName  |
|Get selected attributes for a customer | ` {serviceRoot}/msdynci_customerprofiles?$select=msdynci_fullname&$filter=msdynci_customerid eq '{CID}'`  |    |
|Get customers by IDs (In) | `{serviceRoot}/msdynci_customerprofiles?$filter=msdynci_customerid eq '{CID1}' or msdynci_customerid eq '{CID2}'`  |          |
|Get customers by Alternate Keys (In) | `{serviceRoot}/msdynci_customerprofiles?$filter={msdynci_alternate_column} eq '{AK1}' or {msdynci_alternate_column} eq '{AK2}'`  |          |
|Search for customers| `{serviceRoot}/msdynci_customerprofiles?$filter=contains(msdynci_lastname,'string')&$top=10`  |          |
|Get all customers that are members of a segment| `{serviceRoot}/msdynci_segmentmemberships?$filter=contains(msdynci_segments,'\"{SegmentName}\"')&$select=msdynci_customerid`  |          |
|Get a customer if they're a member of a segment| `{serviceRoot}/msdynci_segmentmemberships?$filter=contains(msdynci_segments,'\"{SegmentName}\"') and msdynci_customerid eq '{CID}'&$select=msdynci_customerid `  |   |
|Get all segment memberships of a customer| `{serviceRoot}/msdynci_segmentmemberships?$filter=msdynci_customerid eq '{CID}'&$select=msdynci_segments`  |      |

### Unified activity

Sample queries for the *UnifiedActivity* table.

|Query type |Example  | Note  |
|---------|---------|---------|
|Get all activities of a customer| `{serviceRoot}/msdynci_unifiedactivities?$filter=msdynci_customerid eq '{CID}'`  |      |
|Get all activities of a customer within a time period| `{serviceRoot}/msdynci_unifiedactivities?$filter=msdynci_customerid eq '{CID}' and msdynci_activitytime gt 2017-01-01T00:00:00Z and msdynci_activitytime lt 2017-01-01T00:00:00Z`  |      |
|Get all activities of an activityType of a customer | `{serviceRoot}/msdynci_unifiedactivities?$filter=msdynci_customerid eq '{CID}' and msdynci_activitytype eq '{ActivityType}'`  |      |
|Get all activities of activityDisplayName of a customer | `{serviceRoot}/msdynci_unifiedactivities?$filter=msdynci_customerid eq '{CID}' and msdynci_activitytypedisplay eq '{ActivityDisplayName}'`  |      |
|Get all activities of a customer and sort them| `{serviceRoot}/msdynci_unifiedactivities?$filter=msdynci_customerid eq '{CID}'&$orderby=msdynci_activitytime asc`  |      |

### Other examples

Sample queries for other tables.

|Query type |Example  | Note  |
|---------|---------|---------|
|Get all measures of a customer| `{serviceRoot}/msdynci_customermeasures?$filter=msdynci_customerid eq '{CID}'`  |      |
|Get enriched brands of a customer| `{serviceRoot}/msdynci_enrichments?$filter=msdynci_customerid eq '{CID}' and msdynci_enrichmentprovider eq 'BrandShareOfVoiceFromMicrosoft'`  |      |  
|Get enriched interests of a customer| `{serviceRoot}/msdynci_enrichments?$filter=msdynci_customerid eq '{CID}' and msdynci_enrichmentprovider eq 'InterestShareOfVoiceFromMicrosoft'`  |      |
|Get AI model results of a customer| `{serviceRoot}/msdynci_predictions?$filter=msdynci_customerid eq '{CID}' and msdynci_modelprovider eq 'ChurnModel'`  |      |

## Next steps

- Most Customer Insights tables are available in Dataverse. For more information, see [Customer Insights tables in Dataverse](tables.md#customer-insights-tables-in-dataverse).

- Dataverse offers extensive support for testing their APIs, for example via Postman. For more information see [Set up a Postman environment](/power-apps/developer/data-platform/webapi/setup-postman-environment).

- For more information on Dataverse API service limits, see [Microsoft Dataverse API limits overview](/power-apps/maker/data-platform/api-limits-overview).

- For more information on how to use Dataverse APIs, see [Query data using the Web API](/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results).

[!INCLUDE [footer-include](includes/footer-banner.md)]
