---
title: "Export segments to DotDigital (preview)"
description: "Learn how to configure the connection and export to DotDigital."
ms.date: 10/10/2023
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to DotDigital (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to DotDigital address books and use them for campaigns, email marketing, and to build customer segments with DotDigital.

## Prerequisites

- A [DotDigital account](https://dotdigital.com/) and  an [API user](https://support.dotdigital.com//articles/8199489-create-an-api-user).
- A DotDigital ID from a [new](https://support.dotdigital.com/articles/8198769-create-a-contact-list) or existing address book in DotDigital. The ID can be found in the URL when you select and open an address book.
- [Configured segments](segments.md).
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Up to 1 million customer profiles per export to DotDigital, which can take up to three hours to complete because of limitations on the provider side. The number of customer profiles that you can export to DotDigital depends on your contract with DotDigital.
- Segments only.
- The connector doesn't support deleting DotDigital address books or members in the address books.

## Set up connection to DotDigital

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **DotDigital**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your credentials for the DotDigital API.

1. Enter your **DotDigital address book ID**.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the DotDigital section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address.

1. Optionally, export **First name**, **Last name**, **Full name**, **Gender**, and **Post code**.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

In DotDigital, find your segments in [DotDigital address books](https://support.dotdigital.com/articles/8198769-create-a-contact-list).

[!INCLUDE [footer-include](includes/footer-banner.md)]
