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
- **Segment exports** let you export segment tables from Customer Insights. For individual consumers (B-to-C), segments represent a list of customer profiles. For businesses (B-to-B), [segments can represent a list of accounts or contacts](segment-builder.md#create-a-new-segment-with-segment-builder). When configuring the export, you select the included data fields, depending on the target system you are exporting data to.

### Segment exports

**Exporting segments in environments for business accounts (B-to-B) or individual consumers (B-to-C)**  
Most export options support both types of environments. Exporting segments to various target systems have specific requirements. 

**Segment exports in environments for individual consumers (B-to-C)**  
- Segments in the context of environments for individual customers are built on the *unified customer profile* table. Every segment that meets the requirements of the target systems (for example, an email address) can get exported.

**Segment exports in environments for business accounts (B-to-B)**  
- Segments in the context of environments for business accounts are built on the *account* table or the *contact* table. To export account segments as is, the target system needs to support pure account segments. This is the case for [LinkedIn](export-linkedin-ads.md) when you choose the **company** option while defining the export.
- All other target systems require fields from the contact table.
- With two segment types (contacts and accounts), Customer Insights automatically identifies which type of segments are eligible for export based on the target system. For example, for a contact-focused target system like Mailchimp, Customer Insights only allows you to choose contact segments to export.

**Limits on segment exports**  
- Third-party target systems may limit the number of customer profiles that you can export. 
- For individual customers, you'll see the actual number of segment members when you select a segment for export. You will get a warning if a segment is too large. 
- For business accounts, you'll see the number of accounts or contacts depending on the segment. You will get a warning if the segment is too large. Exceeding the limits of the target systems results will skip the export.

## Next steps

- [Set up and manage exports](export-manage.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
