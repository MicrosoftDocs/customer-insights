---
title: "Export Customer Insights data to DotDigital"
description: "Learn how to configure the connection to DotDigital."
ms.date: 11/18/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for DotDigital (preview)

Export segments of unified customer profiles to DotDigital address books and use generate campaigns, provide email marketing and leverage specific customer groups with DotDigital. 

## Prerequisites

-	You have a [DotDigital account](https://dotdigital.com/) and corresponding administrator credentials.
-	There are existing address books in DotDigital and the corresponding IDs. The ID can be found in the URL when you selected and opened an address book. For more information, see [DotDigital address books](https://support.dotdigital.com/hc/en-gb/articles/212211968-Creating-an-address-book).
-	You have [configured segments](segments.md)
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Connect to DotDigital

1. Go to **Admin** > **Export destinations**.

1. Under **DotDigital**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

1. Enter your **DotDigital username and password**.

1. Enter your **[DotDigital address book ID ](https://support.dotdigital.com/hc/en-gb/articles/212211968-Creating-an-address-book)**.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to DotDigital.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Next** to configure the export.

## Configure the connector

1. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. Repeat the same steps for other non-mandatory fields such as First name, Last name, Full name, Gender, and Post code.

1. Select the segments you want to export. You can export up to 1 million customer profiles in total to DotDigital.

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab). In DotDigital, you can now find your segments under [DotDigital address books](https://support.dotdigital.com/hc/en-gb/articles/212211968-Creating-an-address-book).

## Known limitations

- Up to 1 million profiles per export to DotDigital.
- Exporting to DotDigital is limited to segments.
- Exporting segments with a total of 1 million profiles can take up to 3 hours because of limitations on the provider side. 
- The number of profiles that you can export to DotDigital is dependent and limited on your contract with DotDigital.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to DotDigital, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that DotDigital meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
