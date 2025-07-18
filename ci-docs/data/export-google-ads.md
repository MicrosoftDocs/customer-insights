---
title: "Export segments to Google Ads"
description: "Learn how to configure the connection and export to Google Ads."
ms.date: 07/17/2025
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: alfergus
---

# Export segments to Google Ads

Export segments of unified customer profiles to a Google Ads audience list. Use these segments to advertise on Google Search, Gmail, YouTube, and Google Display Network.

## Prerequisites

- A [Google Ads account](https://ads.google.com/) and corresponding admin credentials.
- A [Google Ads customer ID](https://support.google.com/google-ads/answer/1704344).
- Meet the requirements of the [Customer Match Policy](https://support.google.com/adspolicy/answer/6299717).
- Meet the requirements for [remarketing list sizes](https://support.google.com/google-ads/answer/7558048).
- The [configured segments](segments.md).
- Make sure unified customer profiles in the exported segments have fields for an email address, phone, mobile advertiser ID, third-party user ID, or address.

## Known limitations

- Export up to 1 million customer profiles per export to Google Ads. This process can take up to 30 minutes because of provider limitations.
- Only segments are supported.
- Matching in Google Ads can take up to 48 hours.

> [!NOTE]
> [Google policy](https://ads-developers.googleblog.com/2025/02/update-to-customer-match-membership.html) states that customer lists in Google Ads are deleted if they're not refreshed in 540 days. Deleting unrefreshed customer lists can affect your Google Ads campaigns and advertising strategies. Rerun the export periodically to refresh your customer lists.

## Set up connection to Google Ads

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Google Ads**.

1. Enter a recognizable name in the **Display name** field. The name and type of the connection describe the connection. Choose a name that explains the purpose and target of the connection.

1. Select who can use this connection. By default, only administrators can use it. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your Google Ads customer ID.

1. Review [data privacy and compliance](connections.md#data-privacy-and-compliance), then select **I agree**.

1. Select **Authenticate with Google Ads**, then enter your Google Ads credentials.

1. Select **Add yourself as export user**, then enter your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to finish setting up the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Google Ads section. Contact an admin if no connection is available.

1. Enter a name for the export.

1. Choose whether to use an existing audience or create a new one:
   - To update an existing Google Ads audience, enter your [Google Ads audience ID](https://support.google.com/google-ads/answer/7558048?hl=en#:~:text=Audience%20lists%20is%20a%20section,Display%20Network%20through%20remarketing%20campaigns).
   - To create a new audience, leave the Google Audience ID field blank. Customer Insights - Data automatically creates a new audience in your Google Ads account and uses the name of the exported segment.

1. In the **Data matching** section, select one or more data fields to export, and select the field that represents the corresponding data fields in Customer Insights - Data.

   > [!NOTE]
   > All personal data is sent as a hashed value to Google.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
