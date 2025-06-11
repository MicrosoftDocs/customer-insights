---
title: Transition emails, content settings, and assets
description: Transition your emails and assets to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/04/2025
ms.topic: concept-article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition emails, content settings, and assets

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

## Emails

It's not possible to use outbound marketing emails directly in real-time journeys. However, you can use the **Import emails** button in the real-time journeys email editor to select and transfer any outbound marketing emails you want to use.

> [!div class="mx-imgBorder"]
> ![Select emails screenshot.](media/transition-select-emails.png "Select emails screenshot")

Importing outbound marketing emails not only saves time but also protects your investment in expensive designs and layouts. During the import, most of the functionality, like personalization and content blocks is also transitioned. After the import, make sure to check to see if all settings and personalizations are correct. Also, you need to choose the right compliance settings for the email before you can go live and use the email in a journey.

While reviewing the imported emails, it's worth considering whether you should start using [brand profiles](brand-profiles.md). Brand profiles provide the ability to standardize content, like links to your company’s LinkedIn, in a similar manner that content settings do for outbound marketing.

You can use the same tool to import email templates. To import templates, go to the email templates area in the real-time journeys email editor and select the **Import template** option.

**Known limitations when importing emails with content blocks**: When you import emails with the *Import content blocks used in the selected emails* option selected, each email re-imports the associated content block(s), overriding any existing version. This results in the loss of any modifications made to the imported content blocks in Real-time marketing (RTM).

> [!TIP]
> To avoid unintended overwrites, import the content block first, along with all related emails, before making any modifications. The content block dependency from outbound marketing is stored in the `msdynmkt_obmmigrationinfo` column within the `msdynmkt_fragment` table. Clearing this value prevents automatic overwriting during imports.

## Content settings

Most of the **content settings** from outbound marketing (for example, social links or sender addresses) can be configured under **brand profiles** in real-time marketing. You can define multiple brand profiles and also set a default brand profile to apply automatically when no specific profile is selected. Just like content settings, brand profile can also be customized (additional columns added) that can then be used for personalization. 
 
<img width="407" alt="image" src="https://github.com/user-attachments/assets/293d707a-a4d7-4504-9da9-e71684dd17bd" />

> [!NOTE]
> The token `{{msdyncrm_contentsettings.ccf_businessname}}` used in outbound marketing doesn't work in real-time marketing. In real-time marketing, personalization must reference the brand profile fields or use the default settings if no brand profile is explicitly associated.

## Asset library

No migration of the asset library should be needed. If you're using the outbound marketing asset library, the same asset library is used by real-time journeys, so you can continue to use all previously uploaded assets. If you're using an external asset library, the process remains the same (get the URL of the asset from the external library and insert it in your messages).

## Relevant upcoming features or workarounds in real-time journeys

The features listed below may be of interest as you transition from outbound marketing to real-time journeys. These features provide parity, equivalent, or better functionality than what was available in outbound marketing.

### Email

- **Email A/B testing and multivariant**: Compare and test variations of your emails on different subsets of your recipients and analyze how they interact with each to determine which variation performs better. 
  - *Guidance:* We don't have a published roadmap. You can create emails for each variation and [use A/B tests at the journey level](real-time-marketing-ab-tests-in-marketing-journeys.md).
- **Email address can only be from Contact/Lead**: Emails can only be sent to email addresses in contacts and leads.
  - *Guidance:* We don't plan to support sending to other email addresses. [Use the CC (carbon copy) field](real-time-marketing-add-cc-recipients.md), where you can use personalization to select an email address from any table related to contacts or leads.

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
