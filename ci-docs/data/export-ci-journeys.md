---
title: Export segments to Customer Insights - Journeys outbound marketing (preview)
description: "Learn how to configure the connection and export to Dynamics 365 Customer Insights - Journeys."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: pkieffer
ms.author: philk
---

# Export segments to Customer Insights - Journeys outbound marketing (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Use [segments](segments.md) to generate campaigns and contact specific groups of customers with [Dynamics 365 Customer Insights - Journeys outbound marketing](/dynamics365/marketing/customer-insights-segments). If you are using Customer Insights - Journeys outbound, [learn more about the transition to real time](https://community.dynamics.com/blogs/post/?postid=1b4394d5-7764-4484-aba9-c7f972292c10).

We recommend using real-time customer journey orchestration because you don't need to create exports to Customer Insights - Journeys. Contacts and segments are available directly through Dataverse after connecting the two apps. Review the documentation on [how to connect Customer Insights and Customer Insights - Journeys customer journey orchestration](/dynamics365/marketing/real-time-marketing-ci-profile).

## Prerequisite

Contact records must be present in Customer Insights - Journeys before you can export a segment from Customer Insights - Data to Customer Insights - Journeys. Read more on how to ingest contacts from [Microsoft Dataverse](connect-dataverse.md).

> [!NOTE]
> Exporting segments won't create new contact records. The contact records must be ingested in Customer Insights - Data and used as a data source. They also need to be included in the unified Customer table to map customer IDs to contact IDs before segments can be exported.

## Recommendations

Consider the following restrictions before exporting to Customer Insights - Journeys outbound:

- In Customer Insights - Journeys outbound, you can send a limited number of interactions per month and per day. Your segments for Customer Insights - Journeys should have no more than one million members. [Check the service limits of Customer Insights - Journeys outbound for more details](/dynamics365/marketing/fair-use-policy).
- Exports to Customer Insights - Journeys outbound takes longer when you update multiple segments to the same environment. For better performance and stability, set up only one export that includes all the segments you need.

## Set up connection to Customer Insights - Journeys

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Customer Insights - Journeys**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your organization's Customer Insights - Journeys URL in the **Server address** field.

1. In the **Server admin account** section, select **Sign in** and choose a Customer Insights - Journeys account.

1. Map the Contact ID field in the Customer table to the Dynamics 365 Contact ID.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Customer Insights - Journeys section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Select the Contact ID field in the Customer table that matches the Dynamics 365 Contact ID.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
