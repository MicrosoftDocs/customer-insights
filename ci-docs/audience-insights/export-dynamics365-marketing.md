---
title: "Export Customer Insights data to Dynamics 365 Marketing | Microsoft Docs"
description: "Learn how to configure the connection to Dynamics 365 Marketing."
ms.date: 08/21/2020
ms.reviewer: philk
ms.service: dynamics-365-ai
ms.topic: "get-started-article"
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for Dynamics 365 Marketing (preview)

Use the [segments created in Customer Insights](segments.md) to generate campaigns and contact specific groups of customers with Dynamics 365 Marketing. For more information, see [Use segments from Dynamics 365 Customer Insights with Dynamics 365 Marketing](https://docs.microsoft.com/dynamics365/marketing/customer-insights-segments)

## Prerequisite

Contact records [from Dynamics 365 Marketing ingested to Customer Insights using Common Data Service](pm-common-connectors.md#dynamics-365-apps-using-common-data-service).

## Configure the connector for Marketing

1. In Customer Insights, go to **Admin** > **Export destinations**.

1. Under **Dynamics 365 Marketing**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

1. Enter your organization's Marketing URL in the **Server address** field.

1. In the **Server admin account** section, select **Sign in** and choose a Dynamics 365 Marketing account.

1. Map a Customer Insights field to the Dynamics 365 Contact ID.

1. Select **Next**.

1. Choose one or more segments.

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).
