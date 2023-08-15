---
title: "Exports (preview) overview"
description: "Overview on exports in Customer Insights"
author: pkieffer
ms.author: philk
ms.reviewer: mhart
ms.date: 03/20/2023
ms.topic: overview
ms.custom: bap-template
searchScope: 
  - ci-export
  - ci-connections
  - customerInsights
---

# Exports (preview) overview

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

 Exports allow you to share specific data with various applications. They can include customer profiles, tables, schemas, and mapping details. Each export requires a [connection, set up by an administrator, to manage authentication and access](connections.md). The **Exports** page shows you all configured exports.

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE5dsVH]

## Export types

There are two main types of exports:  

- **Data-out exports** let you export any type of table available in Customer Insights. The tables that you select for export are exported with all data fields, metadata, schemas, and mapping details.
- **Segment exports** let you export segment tables from Customer Insights. Segments represent a list of customer profiles.

### Segment exports

Segments are built on the *unified customer profile* table. Every segment that meets the requirements of the target systems (for example, an email address) can get exported.

Limits on segment exports include:

- Third-party target systems may limit the number of customer profiles that you can export.
- For individual customers, you'll see the actual number of segment members when you select a segment for export. You will get a warning if a segment is too large.

## Next steps

- [Set up and manage exports](export-manage.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
