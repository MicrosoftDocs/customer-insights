---
title: "Export segments to Braze (preview)"
description: "Learn how to configure the connection and export to Braze."
ms.date: 07/25/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to Braze (preview)

Export segments of unified customer profiles to Braze and use them for marketing activities.

## Prerequisites

- A [Braze account](https://www.braze.com/) and corresponding administrator credentials.
- A [Braze API key](https://www.braze.com/docs/api/basics/)
- [Configured segments](segments.md) in Customer Insights.
- Unified customer profiles in the exported segments contain a field representing an email address and a Braze customer ID.

## Known limitations

- Up 1 million customer profiles to Braze, which can take up to 40 minutes to complete. The number of customer profiles that you can export to Braze depends on your contract with Braze.
- Segments only.

## Set up connection to Braze

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Braze**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your Braze API key to continue to sign in.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Braze section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address. In the **Customer ID** field, select the field that represents the customer's Braze ID. The segments in Braze will be created with the same name of the segment as in Dynamics 365 Customer Insights. You can choose more, optional fields for matching data.

1. Select the entities or segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
