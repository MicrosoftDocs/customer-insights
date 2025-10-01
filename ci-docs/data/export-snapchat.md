---
title: "Export segments to Snapchat"
description: "Learn how to configure the connection and export to Snapchat."
ms.date: 09/29/2025
ms.reviewer: alfergus
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to Snapchat

Export segments of unified customer profiles to Snapchat to use them for advertising.

## Prerequisites

- A [Snapchat Business account](https://business.snapchat.com/), a [Snapchat Ads account](https://ads.snapchat.com/), and admin credentials. You need to be a member of an Organization Account and a Data Manager of a specific Ad Account.
- At least one audience in Snapchat Audience Manager of the type SAM (Snap Audience Match).
- The [Snapchat Segment/Audience ID](https://businesshelp.snapchat.com/s/article/custom-audiences). You can find the audience ID in the URL after you select the audience in Snapchat Audience Manager.
- [Configured segments](segments.md).
- Unified customer profiles in the exported segments have a field for an email address.

## Known limitations

- Supports up to 1 million customer profiles. Processing can take up to 15 minutes.
- Only segments are supported.

## Set up connection to Snapchat

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection**, and choose **Snapchat**.

1. Enter a recognizable name in the **Display name** field. The name and type describe the connection. Choose a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, only admins can use it. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) information, and select **I agree**.

1. Select **Connect** to start the connection.

1. Select **Authenticate with Snapchat**, and enter your admin credentials for Snapchat.

1. Select **Add yourself as export user**, and enter your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to finish the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Snapchat section. Contact your admin if no connection is available.

1. Enter a name for the export.

1. Enter the **Snapchat Segment/Audience ID**.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address.

      > [!NOTE]
   > All personal data goes to Snapchat as a hashed value.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
