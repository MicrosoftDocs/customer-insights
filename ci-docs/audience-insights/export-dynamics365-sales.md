---
title: "Export Customer Insights data to Dynamics 365 Sales"
description: "Learn how to configure the connection to Dynamics 365 Sales."
ms.date: 02/01/2021
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for Dynamics 365 Sales (preview)

[!INCLUDE [cc-data-platform-banner](../includes/cc-data-platform-banner.md)]

Use your customer data to create marketing lists, follow up workflows, and send out promotions with Dynamics 365 Sales.

## Prerequisite

1. Contact records must be present in Dynamics 365 Sales before you can export a segment from Customer Insights to Sales. Read more on how to ingest contacts in [Dynamics 365 Sales using Common Data Services](connect-power-query.md).

   > [!NOTE]
   > Exporting segments from audience insights to Sales will not create new contact records in the Sales instances. The contact records from Sales must be ingested in audience insights and used as a data source. They also need to be included in the unified Customer entity to map customer IDs to contact IDs before segments can be exported.

## Configure the connector for Sales

1. In audience insights, go to **Admin** > **Export destinations**.

1. Under **Dynamics 365 Sales**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

1. Enter your organization's Sales URL in the **Server address** field.

1. In the **Server admin account** section, select **Sign in** and choose a Dynamics 365 Sales account.

1. Map a customer ID field to the Dynamics 365 Contact ID.

1. Select **Next**.

1. Choose one or more segments.

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).
