---
title: "Export segments to ActiveCampaign"
description: "Learn how to configure the connection and export to ActiveCampaign."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: conceptual
author: pkieffer
ms.author: philk
---

# Export segments to ActiveCampaign (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to ActiveCampaign and use them for marketing activities.

## Prerequisites

- An [ActiveCampaign account](https://www.activecampaign.com/) and corresponding administrator credentials.
- An [ActiveCampaign List ID](https://help.activecampaign.com/hc/articles/360000030559-How-to-create-a-list-in-ActiveCampaign).
- An [ActiveCampaign API Key](https://help.activecampaign.com/hc/articles/207317590-Getting-started-with-the-API#how-to-obtain-your-activecampaign-api-url-and-key) and REST Endpoint Hostname.
- [Configured segments](segments.md).
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Bring your own Azure storage account behind a firewall isn't supported.
- Up to 1 million customer profiles per export to ActiveCampaign, which can take up to 90 minutes to complete. The number of customer profiles that you can export to ActiveCampaign depends on your contract with ActiveCampaign.
- Segments only.

## Set up connection to ActiveCampaign

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **ActiveCampaign**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your ActiveCampaign API Key and REST Endpoint Hostname. The REST Endpoint Hostname is the hostname only, without https://.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the ActiveCampaign section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Enter your **ActiveCampaign List ID**.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address.

1. Optionally, export **First name**, **Last name**, and **Phone** to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
