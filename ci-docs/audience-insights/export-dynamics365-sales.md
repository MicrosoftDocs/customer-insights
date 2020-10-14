---
title: "Export Customer Insights data to Dynamics 365 Sales"
description: "Learn how to configure the connection to Dynamics 365 Sales."
ms.date: 08/21/2020
ms.reviewer: philk
ms.service: dynamics-365-ai
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for Dynamics 365 Sales (preview)

Use your customer data to create marketing lists, follow up workflows, and send out promotions with Dynamics 365 Sales.

## Prerequisite

Contact records [from Dynamics 365 Sales ingested using Common Data Service](connect-power-query.md).

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
