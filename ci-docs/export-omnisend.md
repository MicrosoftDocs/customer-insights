---
title: "Export segments to Omnisend (preview)"
description: "Learn how to configure the connection and export to Omnisend."
ms.date: 10/08/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to Omnisend (preview)

Export segments of unified customer profiles to Omnisend and use them for marketing activities.

## Prerequisites

- An [Omnisend account](https://www.omnisend.com/) and corresponding administrator credentials.
- An [Omnisend API key](https://support.omnisend.com/en/articles/1061890-generating-api-key)
- [Configured segments](segments.md) in Customer Insights.
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- The maximum customer profiles per export to Omnisend is up to 1 million, which can take up to 4 hours. The number of customer profiles that you can export to Omnisend depends on your contract with Omnisend.
- Exports to Omnisend is limited to segments.

## Set up connection to Omnisend

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Omnisend**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your Omnisend API key.

1. Select **I agree** to confirm the [Data privacy and compliance](#data-privacy-and-compliance).

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Ommisend, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Omnisend meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights administrator can remove this export destination at any time to discontinue use of this functionality.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Omnisend section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address.

1. Optionally, export First name, Last name, Address, Country/Region, State, City, and Post Code to create more personalized emails. Select **Add attribute** to map these fields.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand). 

