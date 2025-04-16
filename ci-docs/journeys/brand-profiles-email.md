---
title: Use brand profiles in emails
description: Learn how to use brand profiles in email in Dynamics 365 Customer Insights - Journeys.
ms.date: 04/16/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use brand profiles in emails

Brand profiles allow you to create consistently branded content efficiently, even if your organization has multiple brands. You can create multiple brand profiles for your organization or profiles for each of your business units. To learn about creating brand profiles, see [Create consistent branding with brand profiles](brand-profiles.md).

This article describes how to use brand profiles in the Customer Insights - Journeys email designer.

## How to use brand profiles

To use brand profiles in the Customer Insights - Journeys email designer, select the desired profile from the **Brand profile** dropdown in the top right.

> [!div class="mx-imgBorder"]
> ![Select a brand profile in the Customer Insights - Journeys email designer.](media/brand-profile-email-select.png "Select a brand profile in the Customer Insights - Journeys email designer")

After you select a brand profile, the default sender for the profile will be automatically populated into the email sending settings. If you've more than one sender, you can remove the default sender, and then choose from any of the other senders in the profile by selecting the lookup icon in the **Sender** box under **Send settings**.

> [!div class="mx-imgBorder"]
> ![Select a different sender.](media/brand-profiles-email-senders.png "Select a different sender")

> [!NOTE]
> If you want to use a one-time sender for your email (and don’t want to add it to the brand profile), you can leave the sender field empty and manually insert custom sender settings.

## Use dynamic values

You can use the dynamic values from a brand profile to set social links for your social media images in the email. You can access the values by opening the brand profile category in the personalization window. This will ensure that the URLs are accurate no matter which brand profile you've selected.

Learn more about dynamic values: [Personalize content](real-time-marketing-personalization.md).

> [!div class="mx-imgBorder"]
> ![Add dynamic values.](media/brand-profiles-email-dynamic.png "Add dynamic values")

## Updating brand profiles in emails

When you update a brand profile, changes aren't automatically applied to your already-published emails. To ensure that your published emails reflect the updated brand profile, follow these steps:

1. Open the emails you want to update.
1. Temporarily change the current brand profile to another brand profile.
1. After selecting another brand profile, switch back to the original brand profile.
1. Republish the changes to ensure that the updates are reflected.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
