---
title: "OData examples for the Dynamics 365 Customer Insights APIs"
description: "Commonly used examples of for the Open Data Protocol (OData) to query the Customer Insights APIs to review data."
ms.date: 05/10/2022
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: mhart
manager: shellyha
---

# OData query examples

The Open Data Protocol (OData) is a data access protocol built on core protocols like HTTP. It uses commonly accepted methodologies like REST for the web. There are various kinds of libraries and tools that can be used to consume OData services.

This article lists some frequently requested example queries to help you with building your own implementations based on the [Customer Insights APIs](apis.md).

You have to modify the query samples to make them work on the target environments: 

- {serviceRoot}: `https://api.ci.ai.dynamics.com/v1/instances/{instanceId}` where {instanceId} is the GUID of the Customer Insights environment you want to query. The [ListAllInstances operation](https://developer.ci.ai.dynamics.com/api-details#api=CustomerInsights&operation=Get-all-instances) lets you find the {InstanceId} you have access to.
- {CID}: GUID of a unified customer record. Example: `ce759201f786d590bf2134bff576c369`.
- {AlternateKey}: Identifier of the primary key of a customer record in a data source. Example: `CNTID_1002`
- {DSname}: String with the entity name of a data source that gets ingested to Customer Insights. Example: `Website_contacts`.
- {SegmentName}: String with the output entity name of a segment in Customer Insights. Example: `Male_under_40`.

## Customer

The following table contains a set of sample queries for the *Customer* entity.


|Query type |Example  | Note  |
|---------|---------|---------|
|Single customer ID     | `{serviceRoot}/Customer?$filter=CustomerId eq '{CID}'`          |  |
|Alternate key    | `{serviceRoot}/Customer?$filter={DSname_EntityName_PrimaryKeyColumnName} eq '{AlternateKey}' `         |  Alternate keys persist in the unified customer entity       |
|Select   | `{serviceRoot}/Customer?$select=CustomerId,FullName&$filter=customerid eq '1'`        |         |
|In    | `{serviceRoot}/Customer?$filter=CustomerId in ('{CID1}',’{CID2}’)`        |         |
|Alternate Key + In   | `Customer?$filter={DSname_EntityName_PrimaryKeyColumnName} in ('{AlternateKey}','{AlternateKey}')`         |         |
|Search  | `{serviceRoot}/Customer?$top=10&$skip=0&$search="string"`        |   Returns top 10 results for a search string      |
|Segment membership  | `{serviceRoot}/Customer?select=*&$filter=IsMemberOfSegment('{SegmentName}')&$top=10  `     | Returns a preset number of rows from the segmentation entity.      |

## Unified activity

The following table contains a set of sample queries for the *UnifiedActivity* entity.

|Query type |Example  | Note  |
|---------|---------|---------|
|Activity of CID     | `{serviceRoot}/UnifiedActivity?$filter=CustomerId eq '{CID}'`          | Lists activities of a specific customer profile |
|Activity time frame    | `{serviceRoot}/UnifiedActivity?$filter=CustomerId eq '{CID}' and ActivityTime gt 2017-01-01T00:00:00.000Z and ActivityTime lt 2020-01-01T00:00:00.000Z`     |  Activities of a customer profile in a time frame       |
|Activity type    |   `{serviceRoot}/UnifiedActivity?$filter=CustomerId eq '{CID}' and ActivityType eq '{ActivityName}'`        |         |
|Activity by display name     | `{serviceRoot}/UnifiedActivity$filter=CustomerId eq ‘{CID}’ and ActivityTypeDisplay eq ‘{ActivityDisplayName}’ `        | |
|Activity sorting    | `{serviceRoot}/UnifiedActivity?$filter=CustomerId eq ‘{CID}’ & $orderby=ActivityTime asc`     |  Sort activities ascending or descending       |
|Activity expanded from segment membership  |   `{serviceRoot}/Customer?$expand=UnifiedActivity,Customer_Measure&$filter=CustomerId eq '{CID}'`     |         |

## Other examples

The following table contains a set of sample queries for other entities.

|Query type |Example  | Note  |
|---------|---------|---------|
|Measures of CID    | `{serviceRoot}/Customer_Measure?$filter=CustomerId eq '{CID}'`          |  |
|Enriched brands of CID    | `{serviceRoot}/BrandShareOfVoiceFromMicrosoft?$filter=CustomerId eq '{CID}'`  |       |
|Enriched interests of CID    |   `{serviceRoot}/InterestShareOfVoiceFromMicrosoft?$filter=CustomerId eq '{CID}'`       |         |
|In-Clause + Expand     | `{serviceRoot}/Customer?$expand=UnifiedActivity,Customer_Measure&$filter=CustomerId in ('{CID}', '{CID}')`         | |
