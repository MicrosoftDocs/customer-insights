---
title: Use brand profiles in emails
description: Discover how to select and manage brand profiles in the Customer Insights - Journeys email designer for seamless branding.
ms.date: 04/16/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:04/16/2025
  - sfi-image-nochange
---

# Use brand profiles in emails

Brand profiles let you create consistently branded content efficiently, even if your organization has multiple brands. You can create multiple brand profiles for your organization or profiles for each of your business units. To learn about creating brand profiles, see [Create consistent branding with brand profiles](brand-profiles.md).

This article explains how to use brand profiles in the Customer Insights - Journeys email designer.

## How to use brand profiles

To use brand profiles in the Customer Insights - Journeys email designer, select the desired profile from the **Brand profile** dropdown in the upper-right corner.

> [!div class="mx-imgBorder"]
> ![Select a brand profile in the Customer Insights - Journeys email designer.](media/brand-profile-email-select.png "Select a brand profile in the Customer Insights - Journeys email designer")

After you select a brand profile, the default sender for the profile is automatically populated into the email sending settings. If you have more than one sender, you can remove the default sender, and then choose from any of the other senders in the profile by selecting the lookup icon in the **Sender** box under **Send settings**.

> [!div class="mx-imgBorder"]
> ![Select a different sender.](media/brand-profiles-email-senders.png "Select a different sender")

> [!NOTE]
> To use a one-time sender for your email (and avoid adding it to the brand profile), leave the sender field empty and manually insert custom sender settings.

## Use dynamic values

You can use the dynamic values from a brand profile to set social links for your social media images in the email. You can access the values by opening the brand profile category in the personalization window. This ensures that the URLs are accurate no matter which brand profile you've selected.

Learn more about dynamic values in [Personalize content](real-time-marketing-personalization.md).

> [!div class="mx-imgBorder"]
> ![Screenshot of adding dynamic values.](media/brand-profiles-email-dynamic.png "Add dynamic values")

## Updating brand profiles in emails

When you update a brand profile, changes aren't automatically applied to your already-published emails. To ensure that your published emails reflect the updated brand profile, follow these steps:

1. Open the email you want to update.
1. Temporarily switch the current brand profile to another brand profile.
1. After you select another brand profile, switch back to the original brand profile.
1. Republish the changes to ensure the updates are reflected.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
