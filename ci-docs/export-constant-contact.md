---
title: "Export segments to Constant Contact (preview)"
description: "Learn how to configure the connection and export to Constant Contact."
ms.date: 10/08/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to Constant Contact (preview)

Export segments of unified customer profiles to Constant Contact and use them for marketing activities.

## Prerequisites

- A [Constant Contact account](https://www.constantcontact.com/account-home) and corresponding administrator credentials.
- A [Constant Contact List ID](https://app.constantcontact.com/pages/contacts/ui#lists). Open a list in Constant Contact to find the list ID in the URL.
- [Configured segments](segments.md) in Customer Insights.
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- The maximum customer profiles per export to Constant Contact is up to 1 million, which can take up to 1 hour. The number of customer profiles that you can export to Constant Contact depends on your contract with Constant Contact.
- Exports to Constant Contact is limited to segments.

## Set up connection to Constant Contact

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Constant Contact**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection.

1. Select **Authenticate with Constant Contact** and provide your admin credentials for Constant Contact.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Constant Contact, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Constant Contact meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Constant Contact section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. Enter your **Constant Contact List ID**.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address.

1. Optionally, export First name and Last name as additional fields to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).
