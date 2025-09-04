---
title: Prevent sending emails to duplicated email addresses (preview)
description: Learn how to deduplicate email addresses in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/12/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Prevent sending emails to duplicated email addresses (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

When email deduplication is enabled, the journey checks the email addresses of the contacts in the segment (once they reach the email tile) and only send one email to each unique address. For example, if three contacts have the same email address, only one of them receives the email. The other two are reported as **blocked** under the **Duplicate recipient address** category in the **Delivery and interaction details**.

When email deduplication is disabled (default), the journey sends the email to every contact in the segment, even if they share an email address.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## How to enable email deduplication

1. Go to **Settings** and select **Feature switches**.

2. Enable the **Email deduplication** feature toggle in the "Email sending" section.

> [!div class="mx-imgBorder"]
> ![Turn on the button for email deduplication.](media/enable-email-deduplication-button.png)

## How to view duplicated email addresses

You can view duplicated email addresses by going to your journey or email **Delivery and interaction details**.

When you view the insights, you see all duplicated email addresses in the **blocked** section under the **Duplicate recipient address** category.

> [!NOTE]
> When an email gets blockes due to duplication the audience member continues to the next step of journey logic. If you want to exit customers from journeys when duplication is detected, you can you use the [journey exit by triger](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/real-time-marketing-segment-based-journey#:~:text=Exit%3A%20In%20the%20Exit%20setting%20you%20can%20specify%20that%20people%20should%20exit%20the%20journey%20if%20they%20engage%20a%20trigger%20or%20belong%20to%20a%20particular%20segment) option. You can achieve that by choosing the trigger to be *Email blocked" and the Reason *Contains* the key word "Duplicate"


[!INCLUDE [footer-include](./includes/footer-banner.md)]
