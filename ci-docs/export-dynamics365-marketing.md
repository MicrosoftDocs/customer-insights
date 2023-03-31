---
title: "Export segments to Dynamics 365 Marketing (preview)"
description: "Learn how to configure the connection and export to Dynamics 365 Marketing."
ms.date: 03/31/2023
ms.reviewer: mhart

ms.topic: how-to
author: pkieffer
ms.author: philk
searchScope: 
  - ci-export
  - customerInsights
---

# Export segments to Dynamics 365 Marketing (preview)

Use [segments](segments.md) to generate campaigns and contact specific groups of customers with [Dynamics 365 Marketing](/dynamics365/marketing/customer-insights-segments).

Customer Insights recommends using the capabilities of Dynamics 365 Marketing for real-time customer journey orchestration because you don't need to create exports to Dynamics 365 Marketing. Contacts and segments from Customer Insights are available directly in Dynamics 365 Marketing after connecting Marketing and Customer Insights. Before you delete existing exports, review the documentation on [how to connect Customer Insights and Dynamics 365 Marketing customer journey orchestration](/dynamics365/marketing/real-time-marketing-ci-profile). If you are using Marketing outbound, [learn more about the transition to Marketing real time](https://community.dynamics.com/365/dynamics-365-fasttrack/b/dynamics-365-fasttrack-blog/posts/transition-from-outbound-to-real-time-marketing-playbook).

## Prerequisite

Contact records must be present in Dynamics 365 Marketing before you can export a segment from Customer Insights to Marketing. Read more on how to ingest contacts in [Dynamics 365 Marketing using Microsoft Dataverse](connect-dataverse-managed-lake.md).

> [!NOTE]
> Exporting segments from Customer Insights to Marketing will not create new contact records in the Marketing instances. The contact records from Marketing must be ingested in Customer Insights and used as a data source. They also need to be included in the unified Customer table to map customer IDs to contact IDs before segments can be exported.

## Recommendations
Consider the following restrictions before exporting to Dynamics 365 Marketing outbound:
- In Dynamics 365 Marketing outbound, you can send a limited number of interactions per month and per day. Your segments for Marketing should have no more than one million members. [Check the service limits of Dynamics 365 Marketing outbound for more details](/dynamics365/marketing/fair-use-policy).
- Exports to Dynamics 365 Marketing outbound takes longer when you update multiple segments to the same environment. For better performance and stability, set up only one export that includes all the segments you need.

## Set up connection to Marketing

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Dynamics 365 Marketing**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your organization's Marketing URL in the **Server address** field.

1. In the **Server admin account** section, select **Sign in** and choose a Dynamics 365 Marketing account.

1. Map the Contact ID field in the Customer table to the Dynamics 365 Contact ID.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Dynamics 365 Marketing section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Select the Contact ID field in the Customer table that matches the Dynamics 365 Contact ID.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
