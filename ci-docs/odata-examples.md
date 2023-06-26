---
title: "OData query examples for Customer Insights APIs"
description: "Commonly used examples of for the Open Data Protocol (OData) to query the Customer Insights APIs to review data."
ms.date: 06/26/2023
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: mhart
ms.custom: bap-template
---

# OData query examples for Customer Insights APIs

> [!NOTE]
> Customer Insights APIs will be deprecated on January 31st, 2024. You're recommended to use Dataverse APIs to query Customer Insights data. For more information, see [Dataverse APIs for Customer Insights](dv-odata.md).

The Open Data Protocol (OData) is a data access protocol built on core protocols like HTTP. It uses commonly accepted methodologies like REST for the web. There are various kinds of libraries and tools that can be used to consume OData services.

To help you build your own implementations based on the [Customer Insights APIs](apis.md), review some frequently requested example queries.

Modify the query samples to make them work on the target environments:

- {serviceRoot}: `https://api.ci.ai.dynamics.com/v1/instances/{instanceId}/data` where {instanceId} is the GUID of the Customer Insights environment you want to query. The [ListAllInstances operation](https://developer.ci.ai.dynamics.com/api-details#api=CustomerInsights&operation=Get-all-instances) lets you find the {InstanceId} you have access to.
- {CID}: GUID of a unified customer record. Example: `ce759201f786d590bf2134bff576c369`.
- {AlternateKey}: Identifier of the primary key of a customer record in a data source. Example: `CNTID_1002`
- {DSname}: String with the table name of a data source that gets ingested to Customer Insights. Example: `Website_contacts`.
- {SegmentName}: String with the output table name of a segment in Customer Insights. Example: `Male_under_40`.

## Customer

Sample queries for the *Customer* table.

|Query type |Example  | Note  |
|---------|---------|---------|
|Single customer ID     | `{serviceRoot}/Customer?$filter=CustomerId eq '{CID}'`          |  |
|Alternate key    | `{serviceRoot}/Customer?$filter={DSname_TableName_PrimaryKeyColumnName} eq '{AlternateKey}'`         |  Alternate keys persist in the unified customer table       |
|Select   | `{serviceRoot}/Customer?$select=CustomerId,FullName&$filter=customerid eq '1'`        |         |
|In    | `{serviceRoot}/Customer?$filter=CustomerId in ('{CID1}',’{CID2}’)`        |         |
|Alternate Key + In   | `{serviceRoot}/Customer?$filter={DSname_TableName_PrimaryKeyColumnName} in ('{AlternateKey}','{AlternateKey}')`         |         |
|Search  | `{serviceRoot}/Customer?$top=10&$skip=0&$search="string"`        |   Returns top 10 results for a search string      |
|Segment membership  | `{serviceRoot}/Customer?select=*&$filter=IsMemberOfSegment('{SegmentName}')&$top=10`     | Returns a preset number of rows from the segmentation table.      |
|Segment membership for a customer | `{serviceRoot}/Customer?$filter=CustomerId eq '{CID}'&IsMemberOfSegment('{SegmentName}')`     | Returns the customer profile if they're a member of the given segment     |

## Unified activity

Sample queries for the *UnifiedActivity* table.

|Query type |Example  | Note  |
|---------|---------|---------|
|Activity of CID     | `{serviceRoot}/UnifiedActivity?$filter=CustomerId eq '{CID}'`          | Lists activities of a specific customer profile |
|Activity time frame    | `{serviceRoot}/UnifiedActivity?$filter=CustomerId eq '{CID}' and ActivityTime gt 2017-01-01T00:00:00.000Z and ActivityTime lt 2020-01-01T00:00:00.000Z`     |  Activities of a customer profile in a time frame       |
|Activity type    |   `{serviceRoot}/UnifiedActivity?$filter=CustomerId eq '{CID}' and ActivityType eq '{ActivityName}'`        |         |
|Activity by display name     | `{serviceRoot}/UnifiedActivity$filter=CustomerId eq ‘{CID}’ and ActivityTypeDisplay eq ‘{ActivityDisplayName}’`        | |
|Activity sorting    | `{serviceRoot}/UnifiedActivity?$filter=CustomerId eq ‘{CID}’ & $orderby=ActivityTime asc`     |  Sort activities ascending or descending       |
|All activities and measures for a customer  |   `{serviceRoot}/Customer?$expand=UnifiedActivity,Customer_Measure&$filter=CustomerId eq '{CID}'`     | Activities and measures are additional key/value pairs on the returned customer profile       |

## Other examples

Sample queries for other tables.

|Query type |Example  | Note  |
|---------|---------|---------|
|Measures of CID    | `{serviceRoot}/Customer_Measure?$filter=CustomerId eq '{CID}'`          |  |
|Enriched brands of CID    | `{serviceRoot}/BrandShareOfVoiceFromMicrosoft?$filter=CustomerId eq '{CID}'`  |       |
|Enriched interests of CID    |   `{serviceRoot}/InterestShareOfVoiceFromMicrosoft?$filter=CustomerId eq '{CID}'`       |         |
|In-Clause + Expand     | `{serviceRoot}/Customer?$expand=UnifiedActivity,Customer_Measure&$filter=CustomerId in ('{CID}', '{CID}')`         | |

## Limitations

- Customer Insights API returns a maximum of 100 objects by default. You can parse through more than the 100 returned objects by using standard pagination techniques. Alternatively, you can [export your data](export-destinations.md).

- The following queries aren't supported by Customer Insights:
  - `$filter` on ingested source tables. You can only run $filter queries on system tables that Customer Insights creates.
  - `$expand` from a `$search` query. For example: `Customer?$expand=UnifiedActivity$top=10&$skip=0&$search="corey"`.
  - `$expand` from `$select` if only a subset of attributes is selected. For example: `Customer?$select=CustomerId,FullName&$expand=UnifiedActivity&$filter=CustomerId eq '{CID}'`.
  - `$expand` enriched brand or interest affinities for a given customer. For example: `Customer?$expand=BrandShareOfVoiceFromMicrosoft&$filter=CustomerId eq '518291faaa12f6d853c417835d40eb10'`.
  - Query prediction model output tables through alternate key. For example: `OOBModelOutputTable?$filter=HotelCustomerID eq '{AK}'`.

[!INCLUDE [footer-include](includes/footer-banner.md)]
