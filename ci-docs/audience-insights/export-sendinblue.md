---
title: "Export Customer Insights data to Sendinblue"
description: "Learn how to configure the connection and export to Sendinblue."
ms.date: 08/27/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: phkieffer
ms.author: philk
manager: shellyha
---

# Export segments to Sendinblue (preview)

Export segments of unified customer profiles to generate campaigns, provide email marketing and use specific groups of customers with Sendinblue.

## Prerequisites for connection

-	You have a [Sendinblue account](https://www.sendinblue.com/) and corresponding administrator credentials.
-	There are existing lists in Sendinblue and the corresponding IDs.
-	You have [configured segments](segments.md).
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Up to 1 million customer profiles per export to Sendinblue.
- Exporting to Sendinblue is limited to segments.
- Exporting segments with a total of 1 million customer profiles can take up to 90 minutes. 
- The number of customer profiles that you can export to Sendinblue is dependent and limited on your contract with Sendinblue.

## Set up connection to Sendinblue

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Sendinblue** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your **[SendinBlue API key](https://developers.sendinblue.com/docs/getting-started#:~:text=Get%20your%20API%20key&text=You%20can%20create%20one%20from,your%20settings%20This%20API%20key)**.

1. Select **I agree** to confirm the **Data privacy and compliance** and select **Connect** to initialize the connection to Sendinblue.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the Sendinblue section. If you don't see this section name, there are no connections of this type available to you.

1. Enter your **Sendinblue list ID** 

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address. 

1. Optionally, you can export **First name**, **Last name**, and **Phone**  to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export. 

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Sendinblue, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Sendinblue meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights administrator can remove this export destination at any time to discontinue use of this functionality.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
