---
title: "LiveRamp connector"
description: "Learn how to export data to LiveRamp."
ms.date: 12/02/2020
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: kishorem-ms
ms.author: kishorem
manager: shellyha
---

# LiveRamp&reg; connector (preview)

Activate your data in LiveRamp to connect with over 500 platforms across digital, social, and TV ecosystems. Work with your data in LiveRamp to target, suppress, and personalize ad campaigns.

## Prerequisites

- You need a LiveRamp subscription to use this connector.
- To get a subscription, [contact LiveRamp](https://liveramp.com/contact/) directly. [Learn more about LiveRamp Onboarding](https://liveramp.com/our-platform/data-onboarding/).

## Connect to LiveRamp

1. In audience insights, go to **Admin** > **Export destinations**.

1. In the **LiveRamp** tile, select **Set up**.

1. Give your destination a recognizable name in the **Display name** field.

1. Provide a **Username** and **Password** for your LiveRamp Secure FTP (SFTP) account.
These credentials may be different from your LiveRamp Onboarding credentials.

1. Select **Verify** to test the connection to LiveRamp.

1. After successful verification, provide your consent for **Data privacy and compliance** by selecting the **I agree** checkbox.

1. Select **Next** to set up the LiveRamp connector.

## Configure the connector

1. In the **Choose your key identifier** field, select **Email**,  **Name and address**, or **Phone** to send to LiveRamp for identity resolution.

1. Map the corresponding attributes from your unified customer entity for the selected key identifier.

1. Select **Add attribute** to map additional attributes to send to LiveRamp.

   > [!TIP]
   > Sending more key identifier attributes to LiveRamp is likely to get you a higher match rate.

1. Select the segments you want to export to LiveRamp.

1. Select **Save**.

> [!div class="mx-imgBorder"]
> ![LiveRamp connector with attribute mapping](media/export-liveramp-segments.png "LiveRamp connector with attribute mapping")

## Export the data

The export will start shortly if all prerequisites for export have been completed. The export will also run with every [scheduled refresh](system.md#schedule-tab).
Once the export is successfully completed, you can sign in to LiveRamp Onboarding to activate and distribute your data.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Liveramp, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Liveramp meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.

[!INCLUDE[footer-include](../includes/footer-banner.md)]