---
title: "Export Customer Insights data to Dynamics 365 Marketing"
description: "Learn how to configure the connection to Dynamics 365 Marketing."
ms.date: 08/21/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for Dynamics 365 Marketing (preview)

[!INCLUDE [cc-data-platform-banner](../includes/cc-data-platform-banner.md)]

Use [segments](segments.md) to generate campaigns and contact specific groups of customers with Dynamics 365 Marketing. For more information, see [Use segments from Dynamics 365 Customer Insights with Dynamics 365 Marketing](https://docs.microsoft.com/dynamics365/marketing/customer-insights-segments)

## Prerequisite

Contact records [from Dynamics 365 Marketing ingested Common Data Service](connect-power-query.md).

## Configure the connector for Marketing

1. In audience insights, go to **Admin** > **Export destinations**.

1. Under **Dynamics 365 Marketing**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

1. Enter your organization's Marketing URL in the **Server address** field.

1. In the **Server admin account** section, select **Sign in** and choose a Dynamics 365 Marketing account.

1. Map a customer ID field to the Dynamics 365 Contact ID.

1. Select **Next**.

1. Choose one or more segments.

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).
