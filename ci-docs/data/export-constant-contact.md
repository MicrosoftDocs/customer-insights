---
title: "Export segments to Constant Contact (preview)"
description: "Learn how to configure the connection and export to Constant Contact."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: conceptual
author: pkieffer
ms.author: philk
---

# Export segments to Constant Contact (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to Constant Contact and use them for marketing activities.

## Prerequisites

- A [Constant Contact account](https://www.constantcontact.com/account-home) and corresponding administrator credentials.
- A [Constant Contact List ID](https://app.constantcontact.com/pages/contacts/ui#lists). Open a list in Constant Contact to find the list ID in the URL.
- [Configured segments](segments.md).
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Bring your own Azure storage account behind a firewall isn't supported.
- Up to 1 million customer profiles per export to Constant Contact, which can take up to one hour to complete. The number of customer profiles that you can export to Constant Contact depends on your contract with Constant Contact.
- Segments only.

## Set up connection to Constant Contact

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Constant Contact**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Authenticate with Constant Contact** and provide your admin credentials for Constant Contact.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Constant Contact section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Enter your **Constant Contact List ID**.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address.

1. Optionally, export **First name** and **Last name** as additional fields to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
