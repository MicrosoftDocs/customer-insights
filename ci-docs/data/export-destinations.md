---
title: "Exports (preview) overview"
description: "Overview on exports in Dynamics 365 Customer Insights - Data."
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: mhart
ms.date: 02/01/2024
ms.topic: overview
ms.custom: bap-template
---

# Exports (preview) overview

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Exports allow you to share specific data with various applications. They can include customer profiles, tables, schemas, and mapping details. Each export requires a [connection, set up by an administrator, to manage authentication and access](connections.md). The **Exports** page shows all configured exports.

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE5dsVH]

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Export types

There are two main types of exports:  

- **Segment exports** let you export segment tables from Customer Insights - Data. Segments represent a list of customer profiles. When exporting segments, you choose which data fields to include in each export. A common use case for such exports is sharing lists of your customers to advertising services like Google Ads or Meta Ads for marketing purposes.
- **Data-out exports** let you export any type of table available in Dynamics 365 Customer Insights - Data. The tables that you select for export are exported with all data fields, metadata, schemas, and mapping details. A common use case for the export of full tables, which we call a data-out export, is to share data to Azure Data Lake Gen2, from where organizations can further process these tables with their custom solutions. We recommend that for these scenarios you use Dataverse data sharing features with [Customer Insights tables in Dataverse](tables.md#customer-insights---data-tables-in-dataverse):
  - Use [Power BI with Dataverse data](/power-apps/maker/data-platform/use-powerbi-dataverse). It ensures you benefit from the [integration with Dataverse](integrate-d365-apps.md).
  - Get insights in Microsoft Fabric with the [Dataverse link to Fabric and Microsoft OneLake](/power-apps/maker/data-platform/azure-synapse-link-view-in-fabric).

  [!INCLUDE [data-out-azure-synapse-link](includes/data-out-azure-synapse-link.md)]

### Segment exports

Segments are built on the *unified customer profile* table. Every segment that meets the requirements of the target systems (for example, an email address) can get exported. When defining a segment you often want to ensure it's exported as well, to do so you can use the **Manage exports** menu option.

Limits on segment exports include:

- Third-party target systems can limit the number of customer profiles that you can export.
- For individual customers, you see the actual number of segment members when you select a segment for export. The system warns you if a segment is too large.
- Fields available for export are limited to the Customer profile table. Projected attributes from other tables aren't available for export, regardless if you use them when creating a segment.

## Next step

- [Set up and manage exports](export-manage.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
