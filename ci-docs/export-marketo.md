---
title: "Export segments to Marketo (preview)"
description: "Learn how to configure the connection and export to Marketo."
ms.date: 10/08/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to Marketo (preview)

Export segments of unified customer profiles to generate campaigns, provide email marketing and use specific groups of customers with Marketo.

## Prerequisites

- A [Marketo account](https://login.marketo.com/) and corresponding administrator credentials.
- A [Marketo client ID, Client secret, and REST Endpoint Hostname](https://developers.marketo.com/rest-api/authentication/).
- [Existing lists in Marketo](https://docs.marketo.com/display/public/DOCS/Understanding+Static+Lists) and the corresponding IDs.
- A [Marketo list ID](https://docs.marketo.com/display/public/DOCS/Understanding+Static+Lists).
- [Configured segments](segments.md).
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- The maximum customer profiles per export to Marketo is up to 1 million, which can take up to 3 hours. The number of customer profiles that you can export to Marketo depends on your contract with Marketo.
- Exporting to Marketo is limited to segments.

## Set up connection to Marketo

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Marketo**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your **Marketo client ID, Client secret, and REST Endpoint Hostname**. The REST Endpoint Hostname is the hostname only, without `https://`. Example: `xyz-abc-123.mktorest.com`.

1. Select **I agree** to confirm the [Data privacy and compliance](#data-privacy-and-compliance).

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Marketo, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Marketo meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Marketo section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. Enter your **Marketo list ID**. The list ID is a purely numerical value. For example, if your Marketo list ID is ST12345A7, remove the character before and after the numerals and enter `12345`.

1. In the **Data matching** section, select at least one field that represents a customer's email address or a customer's Marketo ID.

1. Optionally, export **First name**, **Last name**, **City**, **State**, and **Country/Region**  to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

In Marketo, find your segments under [Marketo lists](https://docs.marketo.com/display/public/DOCS/Understanding+Static+Lists).

[!INCLUDE [footer-include](includes/footer-banner.md)]
