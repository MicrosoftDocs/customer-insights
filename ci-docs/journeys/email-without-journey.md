---
title: Use "Send now" to send emails instantly
description: Learn how to send emails in Dynamics 365 Customer Insights - Journeys without building a journey.
ms.date: 08/18/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use "Send now" to send emails instantly

> [!IMPORTANT]
> The "Send now" functionality described in this article, **only** applies to Customer Insights - Journeys, not outbound marketing.

> [!TIP]
> If you don’t see this feature in your app, contact your admin who can activate it by going to **Settings** > **Overview** > **Feature switches**, scrolling to the **Email editor** area, enabling the **Send now** feature switch, and saving the setting by selecting **Save** on the top right corner.

You can now send an email directly from the email editor and be guided through a simple flow, provided your email and journey scenarios are simple. From the email editor, select the **Ready to Send** option. This directs you to select the **Send** the email option where you can select a segment, preview its contents, and then send the email. The process builds a simple journey in the background to assist you in sending your email.

Send Now is a simplified workflow which supports limited scenarios. It does not support the complete set of validations and capabilities available in the full journey editor canvas. If you are using any of these scenarios you must use the journey canvas to ensure the features in your email are supported properly: 
- Send Now only works with contact and lead, segment based journeys. We will expand to support Customer Insights Profiles in the future. 
- Outbound marketing segments which have never been used in real-time journeys.
- Send Now will not stop users from selecting an email and a segment from two different business units. If you have permissions to more than one business unit, be careful to make sure you select an email and segment from the same business unit.
- The following personalization variables DO NOT work in Send Now: 
  - Triggers, Send Now only supports Segment based journeys. It will not be able to access Trigger data used in email personalization.
  - Complex inline conditions 1:n relationships such as Contacts -> Accounts.
  - Dynamic text.
  - Lists.

If you experience a journey publish failure or email that doesn't send using Send Now, open the journey in the journey canvas and save a copy, edit the journey and email in the journey canvas and republish. 

To begin your email sending process, follow these steps:

1. Go to **Customer Insights - Journeys** > **Channels** > **Emails** and select **+ New** in the top toolbar. Select the email template that you want to use. You can either use a predesigned template or create your own custom template by selecting **Skip**.
1. From the email editor, mark your email "Ready to Send" by selecting the **Ready to Send** button.

    > [!div class="mx-imgBorder"]
    > ![Ready to send screenshot.](media/email-without-journey-ready.png "Ready to send screenshot")

1. The button changes to **Send now** or **Schedule for later** and can be selected to start the flow. If you select **Schedule for later**, you're prompted to choose a date to send the email.
1. Select a segment and select **Preview** to preview the segment. You can only select published segments.
    > [!NOTE]
    > If you have personalization in your email leveraging Contacts or Leads and you select a segment of the opposite type, you will not be allowed to move forward until the segment type matches the personalization type.
1. Select **Send** to send the mail. Your mail is queued up to be sent.
1. On the confirmation screen, select **View Customer Journey** to see the simple journey that was created to send the email. The journey name matches the name of your email. Select **View Segment** to view the segment to which the email was sent.

## Known issues

- Outbound marketing segments that have never been used in a Customer Insights - Journeys don't work with the **Send Now** functionality. Once an outbound marketing segment has been used in a Customer Insights - Journeys successfully, it's been processed and you can use it with the **Send Now** functionality.
- Sending emails without building a journey will not stop the user from selecting an email and a segment from different business units.
- Triggers, complex inline conditions, dynamic text, and lists in personalization do not work in Send Now. 

[!INCLUDE [footer-include](./includes/footer-banner.md)]
