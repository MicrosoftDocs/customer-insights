---
title: Add email carbon copy recipients to journeys
description: Enable and use the CC feature in Dynamics 365 Customer Insights - Journeys. Follow our guide to add up to five CC recipients to your emails.
ms.date: 11/22/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Add email carbon copy recipients to journeys

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RW10sVQ]

You can add carbon copy (CC) recipients to your journeys when sending emails. When designing your journey, select up to five recipients for your emails from the email tile. Dynamically choose your CC recipients by mapping them to your marketable contacts.

> [!IMPORTANT]
>
>- When you add CC recipients to your emails, the sent email will be identical for both primary and CC contacts. The interactions from CC recipients with sent emails (open, forward, clicks, unsubscribe) will be counted as a primary recipient interactions and will have direct impact on your insights and analytics.
>- Email interactions (sent, delivered, bounced, etc.) are not shown for CC.
>- If a CC recipient clicks on the unsubscribe button for marketing emails, they will unsubscribe the primary contact.
>- The CC recipient interaction will trigger the next step in the journey if you are utilizing the **Respond to an action** element in your journey based on the customer interaction.
>- CC contacts are counted for marketable contact quota.
>- CC contacts interactions are counted for interaction quota.
>- Only the communication consent of the primary recipient is verified. The communication consent of CC recipients is not verified.
>
> CC recipients will receive the same amount of emails as the overall emails sent to primary recipients, meaning, if you send 1,000 emails to primary recipients with two people in CC, your overall sent emails will be 3,000. It's recommended that you select people in the CC field who are aware of how this feature functions.  
>

## Enabling the CC feature

The CC feature is disabled by default. To enable the feature:

1. Go to **Settings** and select **Feature Switches**.
    > [!div class="mx-imgBorder"]
    > ![Select feature switches from settings.](media/real-time-email-cc-settings-feature-switches.png "Select feature switches from settings")

2. Enable the feature in the Customer Journey section.
    > [!div class="mx-imgBorder"]
    > ![Screenshot of enabling the feature switch.](media/real-time-email-cc-enable-feature.png "Screenshot of enabling the feature switch")

## How to use the CC feature in customer journeys

1. In your journey, select the **Send an email** action.

    > [!div class="mx-imgBorder"]
    > ![Screenshot choosing the Send an email action.](media/real-time-email-cc-send-email.png "Screenshot choosing the Send an email action")

1. Select the **Select a recipient** to dynamically select the CC recipient. You have to select the relation to your target audience (contact or lead).

    > [!div class="mx-imgBorder"]
    > ![Screenshot showing the recipient selection.](media/real-time-email-cc-select-recipient.png "Screenshot showing the recipient selection")

1. Select up to five recipients. Make sure you're selecting entities that contain email addresses. If you select an entity that doesn't contain an email, it's ignored when sending the email.

    > [!div class="mx-imgBorder"]
    > ![Screenshot showing five recipients selected.](media/real-time-email-cc-select-recipient-up-to-5.png "Screenshot showing five recipients selected")

[!INCLUDE [footer-include](./includes/footer-banner.md)]
