---
title: "Export segments to HubSpot (preview)"
description: "Learn how to configure the connection and export to HubSpot."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to HubSpot (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to HubSpot and use them for email marketing.

## Prerequisites for a connection

- A [HubSpot account](https://www.hubspot.com/) and corresponding administrator credentials.
- [API key](https://knowledge.hubspot.com/Integrations/How-do-I-get-my-HubSpot-API-key) from HubSpot.
- [Configured segments](segments.md).

## Known limitations

- Up to 100'000 customer profiles per export to HubSpot, which can take up to 15 minutes to complete. The number of customer profiles that you can export to HubSpot is dependent and limited on your contract with HubSpot.
- Segments only.

## Set up connection to HubSpot

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **HubSpot** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your HubSpot credentials when prompted.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection to HubSpot.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add export**.

1. In the **Connection for export** field, choose a connection from the HubSpot section. If you don't see this section name, there are no connections of this type available to you.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address. Repeat the same steps for other optional fields.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
