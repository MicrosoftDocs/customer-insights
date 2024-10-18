---
title: "Export segments to Marketo (preview)"
description: "Learn how to configure the connection and export to Marketo."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: pkieffer
ms.author: philk
---

# Export segments to Marketo (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to generate campaigns, provide email marketing and use specific groups of customers with Marketo.

## Prerequisites

- A [Marketo account](https://login.marketo.com/) and corresponding administrator credentials.
- A [Marketo client ID, Client secret, and REST Endpoint Hostname](https://developers.marketo.com/rest-api/authentication/).
- [Existing lists in Marketo](https://docs.marketo.com/display/public/DOCS/Understanding+Static+Lists) and the corresponding IDs.
- [Configured segments](segments.md).
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Up to 1 million customer profiles per export to Marketo, which can take up to 3 hours. The number of customer profiles that you can export to Marketo depends on your contract with Marketo.
- Segments only.

## Set up connection to Marketo

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Marketo**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your **Marketo client ID, Client secret, and REST Endpoint Hostname**. The REST Endpoint Hostname is the hostname only, without https://. Example: xyz-abc-123.mktorest.com.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Marketo section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Enter your **Marketo list ID**. The list ID is a purely numerical value. For example, if your Marketo list ID is ST12345A7, remove the character before and after the numerals and enter *12345*.

1. In the **Data matching** section, select at least one field that represents a customer's email address or a customer's Marketo ID.

1. Optionally, export **First name**, **Last name**, **City**, **State**, and **Country/Region**  to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

In Marketo, find your segments under [Marketo lists](https://docs.marketo.com/display/public/DOCS/Understanding+Static+Lists).

[!INCLUDE [footer-include](includes/footer-banner.md)]
