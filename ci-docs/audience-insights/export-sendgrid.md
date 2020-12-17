---
title: "Export Customer Insights data to SendGrid"
description: "Learn how to configure the connection to SendGrid."
ms.date: 12/08/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for SendGrid (preview)

Export segments of unified customer profiles to SendGrid contact lists and use them for campaigns and email marketing in SendGrid. 

## Prerequisites

-	You have a [SendGrid account](https://sendgrid.com/) and corresponding administrator credentials.
-	There are existing contact lists in SendGrid and the corresponding IDs. For more information, see [SendGrid - Manage contacts](https://sendgrid.com/docs/ui/managing-contacts/create-and-manage-contacts/#manage-contacts).
-	You have [configured segments](segments.md) in audience insights.
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Connect to SendGrid

1. Go to **Admin** > **Export destinations**.

1. Under **SendGrid**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

   :::image type="content" source="media/export-sendgrid.PNG" alt-text="SendGrid export configuration pane.":::

1. Enter your **SendGrid API key** [SendGrid API key](https://sendgrid.com/docs/ui/account-and-settings/api-keys/).

1. Enter your **[SendGrid list ID](https://sendgrid.com/docs/ui/managing-contacts/create-and-manage-contacts/#manage-contacts)**.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to SendGrid.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Next** to configure the export.

## Configure the connector

1. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. Repeat the same steps for other optional fields such as **First name**, **Last name**, **Country/Region**, **State**, **City**, and **Post code**.

1. Select the segments you want to export. We strongly **recommend to not export more than 100'000 customer profiles in total** to SendGrid. 

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).

## Known limitations

- Up to 100'000 profiles in total to SendGrid.
- Exporting to SendGrid is limited to segments.
- Exporting up to 100'000 profiles to SendGrid can take up to a few hours to complete. 
- The number of profiles that you can export to SendGrid is dependent and limited on your contract with SendGrid.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to SendGrid, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that SendGrid meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
