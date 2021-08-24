---
title: "Export Customer Insights data to Dynamics 365 Marketing"
description: "Learn how to configure the connection and export to Dynamics 365 Marketing."
ms.date: 03/03/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: pkieffer
ms.author: philk
manager: shellyha
---

# Use segments in Dynamics 365 Marketing (preview)

 > [!IMPORTANT]
  > If you are using the new capabilities of Dynamics 365 Marketing regarding real time customer journey orchestration, then you do not need to create a standard export to Dynamics 365 Marketing through audience insights, as the contacts and segments available in audience insights are also available directly in D365 Marketing. Before you delete any existing exports, please refer to the extensive documentation on [how to connect audience insights and Dynamics 365 Marketing customer journey orchestration] (https://docs.microsoft.com/en-us/dynamics365/marketing/real-time-marketing-ci-profile)

[!INCLUDE [cc-data-platform-banner](../includes/cc-data-platform-banner.md)]

Use [segments](segments.md) to generate campaigns and contact specific groups of customers with Dynamics 365 Marketing. For more information, see [Use segments from Dynamics 365 Customer Insights with Dynamics 365 Marketing](/dynamics365/marketing/customer-insights-segments)

## Prerequisite for a connection

- Contact records must be present in Dynamics 365 Marketing before you can export a segment from Customer Insights to Marketing. Read more on how to ingest contacts in [Dynamics 365 Marketing using Microsoft Dataverse](connect-power-query.md).

  > [!NOTE]
  > Exporting segments from audience insights to Marketing will not create new contact records in the Marketing instances. The contact records from Marketing must be ingested in audience insights and used as a data source. They also need to be included in the unified Customer entity to map customer IDs to contact IDs before segments can be exported.

## Set up connection to Marketing

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Dynamics 365 Marketing** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your organization's Marketing URL in the **Server address** field.

1. In the **Server admin account** section, select **Sign in** and choose a Dynamics 365 Marketing account.

1. Map a customer ID field to the Dynamics 365 Contact ID.

1. Select **Save** to complete the connection. 

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the Dynamics 365 Marketing section. If you don't see this section name, there are no connections of this type available to you.

1. Choose one or more segments.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 

[!INCLUDE[footer-include](../includes/footer-banner.md)]
