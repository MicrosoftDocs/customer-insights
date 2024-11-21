---
title: "Export segments to Sendinblue (preview)"
description: "Learn how to configure the connection and export to Sendinblue."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: phkieffer
ms.author: sstabbert
---

# Export segments to Sendinblue (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to generate campaigns, provide email marketing and use specific groups of customers with Sendinblue.

## Prerequisites

- A [Sendinblue account](https://www.sendinblue.com/) and corresponding administrator credentials.
- A [SendinBlue API key](https://developers.sendinblue.com/docs/getting-started#:~:text=Get%20your%20API%20key&text=You%20can%20create%20one%20from,your%20settings%20This%20API%20key).
- Existing lists in Sendinblue and the corresponding IDs.
- [Configured segments](segments.md).
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Up to 1 million customer profiles per export to Sendinblue, which can take up to 90 minutes to complete. The number of customer profiles that you can export to Sendinblue depends on your contract with Sendinblue.
- Segments only.

## Set up connection to Sendinblue

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Sendinblue**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your **SendinBlue API key**.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Sendinblue section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Enter your **Sendinblue list ID**.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address.

1. Optionally, export **First name**, **Last name**, and **Phone**  to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
