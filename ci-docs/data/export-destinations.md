---
title: "Exports overview"
description: "Overview on exports in Dynamics 365 Customer Insights - Data."
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: alfergus
ms.date: 07/17/2025
ms.topic: overview
ms.custom: bap-template
---

# Exports overview

Exports let you share specific data with different applications. Exports can include customer profiles, tables, schemas, and mapping details. Each export needs a [connection set up by an admin to manage authentication and access](connections.md). The **Exports** page shows all configured exports.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=16eaf464-5b0a-4aa0-9775-df95da16e89d]

## Export types

There are two main types of exports:  

- **Segment exports** let you export segment tables from Customer Insights - Data. Segments represent a list of customer profiles. When exporting segments, you choose which data fields to include in each export. A common use case for such exports is sharing lists of your customers to advertising services like Google Ads or Meta Ads for marketing purposes.
- **Data-out exports** let you export any type of table available in Dynamics 365 Customer Insights - Data. The tables that you select for export are exported with all data fields, metadata, schemas, and mapping details. A common use case for the export of full tables, which we call a data-out export, is to share data to Azure Data Lake Gen2, from where organizations can further process these tables with their custom solutions. We recommend that for these scenarios you use Dataverse data sharing features with [Customer Insights tables in Dataverse](tables.md#view-customer-insights---data-tables-in-dataverse):
  - Use [Power BI with Dataverse data](/power-apps/maker/data-platform/use-powerbi-dataverse). It ensures you benefit from the [integration with Dataverse](integrate-d365-apps.md).
  - Get insights in Microsoft Fabric with the [Dataverse link to Fabric and Microsoft OneLake](/power-apps/maker/data-platform/azure-synapse-link-view-in-fabric).

  [!INCLUDE [data-out-azure-synapse-link](includes/data-out-azure-synapse-link.md)]

### Segment exports

Segments are built on the *unified customer profile* table. Any segment that meets the requirements of the target system (for example, an email address) can be exported. When you define a segment, you often want to export it too. To do this, use the **Manage exports** menu option.

Limits on segment exports include:

- Third-party target systems can limit the number of customer profiles you export.
- For each customer, you see the actual number of segment members when you select a segment for export. The system warns you if a segment is too large.
- Fields available for export are limited to the Customer profile table. Projected attributes from other tables aren't available for export, even if you use them when creating a segment.

## Known limitations for export connectors

Each export connector may have specific limitations. Review the following general limitations and check individual connector documentation for connector-specific details.

| Limitation | Details |
|-----------|---------|
| Maximum segment size | Third-party connectors may reject segments that exceed their API limits. Check the connector's documentation for maximum audience size. |
| Required fields | Some connectors require specific fields (for example, email address or hashed email). Exports fail if required fields are missing. |
| API rate limits | Third-party APIs impose rate limits that can affect large exports. If an export fails for a large segment, try reducing the segment size or contact the connector provider. |
| Data format requirements | Some connectors require specific data formats. For example, advertising platforms may require hashed email addresses (SHA-256). |
| Regional availability | Not all connectors are available in all regions. Check individual connector pages for regional availability. |

> [!TIP]
> If an export fails, check the export run details for the specific error returned by the connector. The error message can help you identify whether the issue is related to data format, segment size, or API limits.

## Next step

- [Set up and manage exports](export-manage.md)
- [FastTrack blog: Understanding Job Execution Flow in Customer Insights - Data Batch Runs](https://community.dynamics.com/blogs/post/?postid=84fbbaaf-262b-f011-8c4e-7c1e5218b899)

[!INCLUDE [footer-include](includes/footer-banner.md)]
