---
title: "Export segments to MoEngage"
description: "Learn how to configure the connection and export to MoEngage."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to MoEngage (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to MoEngage and use them for email marketing in MoEngage.

## Prerequisites for a connection

- [MoEngage account](https://www.moengage.com/) and corresponding administrator credentials.
- MoEngage API key from Settings > API in MoEngage.
- [Configured segments](segments.md).

## Known limitations

- Up to 100'000 customer profiles per export to MoEngage, which can take up to 15 minutes. The number of customer profiles that you can export to MoEngage depends on your contract with MoEngage.
- Segments only.

## Set up connection to MoEngage

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **MoEngage** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your [MoEngage Data API ID and API key](https://developers.moengage.com/hc/articles/4404674776724-Overview#:~:text=Navigate%20to%20Settings%20%3E%20APIs%20%3E%20DATA,ID%20Password%20%2D%20DATA%20API%20KEY).

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection to MoEngage.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add export**.

1. In the **Connection for export** field, choose a connection from the MoEngage section. If you don't see this section name, there are no connections of this type available to you.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address. Repeat the same steps for other optional fields.

1. Select the segments you want to export. We'll create one or more segments with the same name as the selected segments in MoEngage under **Insights** > **Segments** > **Custom Segments**.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
