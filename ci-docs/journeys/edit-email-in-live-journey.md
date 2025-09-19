---
title: Edit email components in a live journey
description: Learn how to edit email components in live journey in Dynamics 365 Customer Insights - Journeys
ms.date: 03/10/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Edit email components in a live journey

The email editor in Dynamics 365 Customer Insights – Journeys allows you to create and design engaging email messages for your customers. You can use various components such as text, images, buttons, links, and dynamic content to customize your email layout and content.

Once you activate a customer journey, the email messages that are part of it are sent to the recipients according to the schedule and conditions that you set. However, you may need to make changes to your email messages after the journey is live, for example, to correct a typo, update an offer, or add a new link.

In this article, you'll learn about the email components that can be edited in a live journey and the ones that can't. You'll also learn how to edit your email messages in a live journey and the limitations and best practices that you should consider.

## How to edit your email messages in a live journey

To edit your email messages in a live journey, follow these steps:

1. In your journey, select the email tile, then go to **Properties** and select the email title.
1. Select the edit button in the email editor, then select continue.
1. Make the changes that you want to the email components that [can be edited](edit-email-in-live-journey.md#email-components-that-can-be-edited-in-a-live-journey) in a live journey.
1. Select finish editing.

> [!NOTE]
> - Editing email messages in a live journey does not affect the email messages that have already been sent or are in the process of being sent. The changes only apply to email messages that are scheduled to be sent after the publication of the changes.
> - Editing email messages in a live journey may affect the performance and reporting of your customer journey. For example, if you change the link of a button or an image, the click-through rate and the conversion rate of your email message may change.

## Email components that can be edited in a live journey

The email editor components that can be edited in a live journey are:

| **Components** | **Editable** | **Note** |
|---:|---|---|
| Text layout/formatting | Yes | You can add or edit the text content, font, size, color, alignment, and formatting of any text component in your email message. |
| Image | Yes | You can add or edit the image source, alt text, size, alignment, and link of any image component in your email message. |
| Content blocks      (without links/personalization) | Yes | You can add or edit the link text, font, size, color, alignment. |
| Compliance profile and consent related settings | Yes | You can update the settings. |
| Subject and preheader | Yes | You can add or edit the text content. |
| QR code | Yes | You can add or edit the QR code without any   personalization. |
| Survey links | Yes | You can add or edit the survey links without any personalization. |
| Personalization | Yes | You can add or edit the personalization and rules. |
| Conditional content | Yes | You can only edit the existing condition. |

> [!NOTE]
> - Link insights displays data for emails (with links) that have this feature enabled and were created after September 2024. 
> - To easily track and identify links in analytics, we incorporate editable "link aliases" into the URL. 

[!INCLUDE [footer-include](./includes/footer-banner.md)]
