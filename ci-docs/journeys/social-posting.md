---
title: Social media posting with Dynamics 365 Customer Insights - Journeys
description: Create social media posts for immediate or scheduled publishing in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/09/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Social media posting with Dynamics 365 Customer Insights - Journeys

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

> [!WARNING]
> Social posting and LinkedIn lead generation capabilities have been removed from Customer Insights - Journeys.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=660e7570-b093-40ee-bd99-5d68165b0fa2]

Customer Insights - Journeys can schedule and post messages directly to your organization's accounts on social media sites. Customer Insights - Journeys's powerful social post designer allows you to create rich content to engage your audience. Use the **Social posts** settings to author and schedule your posts.

> [!NOTE]
> Before you can start publishing messages, your administrator must configure and authenticate each social-media account that you will publish to. More information: [Configure your social media accounts](mkt-settings-social-media.md)

## Schedule and post a message

Use the **Social posts** entity to author and schedule your posts. You can post from any social media account that your admin has set up and authenticated in Customer Insights - Journeys.

To schedule and publish a message to one of your social-media channels:

1. Go to **Outbound marketing** > **Marketing execution** > **Social posts**.
1. A calendar opens. Already published posts are greyed out. Scheduled posts have icons to quickly identify which social networks the posts are directed to. Do one of the following:
    - To schedule a social post using the calendar, choose a calendar view (month, day, or week), select a day or time slot to highlight it, and then select again (click or press enter) and choose **New item** from the context menu. More information: [Work with marketing calendars](marketing-calendar.md)
    - To schedule a message using date pickers, or to send it right away, select **New** on the command bar.

    ![The social-posts calendar.](media/social-posting-calendar-update.png "The social-posts calendar")

1. A new social post record is created. Make the following settings:
    - **Name**: Enter an internal name for the post. This name will be shown on the calendar, but won't appear in the post itself.
    - **Social channel**: Choose the social channel on which to post your message (such as Facebook, LinkedIn, or X (Twitter)). This drop-down list only shows those channels that your administrator has set up in Customer Insights - Journeys. If you don't see the channel you are looking for, contact your admin. More information: [Configure your social media accounts](mkt-settings-social-media.md)
    - **Social configuration**: Select the specific account through which to post your message. This drop-down list shows each account that your admin has set up and authenticated in Customer Insights - Journeys for the selected channel. If you don't see the account you are looking for, contact your admin. More information: [Configure your social media accounts](mkt-settings-social-media.md)
    - **Message**: Enter the text content of your post here.
        - The countdown will inform you how many characters you have left. Use the countdown to align your message length with social network requirements, such as X (Twitter).
        - You can enhance your messages with Emojis.
        - You can use hashtags to tag your messages across social media sites.
    - **Media**: If you'd like to include an image with your post, select the **Add media** button.
    - **Preview**: On the right side of the designer, you will see a rendered preview of your social post. The preview corresponds with the selected social network formatting.

    ![Social post settings and content.](media/social-posting-new-post-update.png "Social post settings and content")

1. When you are done designing your post, select one of the following buttons at the bottom of the page:
      - **Schedule**: Select this to save your post and schedule it to be published at the configured **Schedule time**. (This button only appears if you've chosen a schedule.)
        > [!IMPORTANT]
        > The dates and times for the posting schedule use the time zone configured in your personal settings. To view or edit your time zone, open the **Settings** menu ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon")
      - **Post now**: Select this to publish your post right now. Your message will be posted immediately and shown on the calendar for the current date and time. The label of this button changes based on whether you've already set a schedule or not.
      - **Change schedule**: Establish a specific date and time to post the message or edit the existing one. The label of this button changes based on whether you've already set a schedule or not.

### Edit, reschedule, or cancel a post

You can edit, reschedule, or cancel any post that hasn't been sent yet. Just find and select it on the calendar to open the record, and then edit the settings or select **Delete** on the command bar as needed.

Posts that were already sent are read-only, so you can't change or reschedule them, but you can remove them from the calendar or delete if you want. When you delete a post that has already been sent, it will be removed from the calendar and from the social-media sites.

> [!NOTE]
> Posts that were made to the Instagram channel cannot be removed by the Customer Insights - Journeys app; Instagram does not provide this functionality. To remove the post from Instagram, go to Instagram and manually remove it.

## Known issues

- X (Twitter) posting no longer works due to changes in terms and conditions by X.
- Facebook and Instagram: due to API changes, authenticated accounts can continue posting but can't re-authenticate.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
