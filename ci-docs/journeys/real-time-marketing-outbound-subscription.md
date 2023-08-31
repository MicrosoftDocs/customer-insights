---
title: Use outbound subscription centers in Customer Insights - Journeys
description: Learn how to use outbound marketing subscription centers in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/23/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use outbound subscription centers in Customer Insights - Journeys

[!INCLUDE[consolidated-sku-rtm-only](../includes/consolidated-sku-rtm-only.md)]

This article explains how to use outbound marketing subscription centers in journeys. Outbound subscription centers give you consent management flexibility, enabling you to have multiple subscription centers customized and branded to your needs.

> [!IMPORTANT]
> You can only use subscription centers in journeys that target contacts. Journeys that target leads or customer profiles will continue to use the default preference page.

> [!NOTE]
> Customer Insights - Journeys has introduced a new compliance profile type of preference center that works natively with contact point-based consent in Customer Insights - Journeys. Preference centers offer improved functionality, such as more customizable forms and the ability to update text message consent. Learn more: [Customer Insights - Journeys compliance profiles](real-time-marketing-compliance-settings.md) and [Preference centers](real-time-marketing-preference-centers.md)

## Prerequisites

To use outbound subscription centers in Customer Insights - Journeys, you must first create at least one subscription center in outbound marketing. You also need to make sure the configurable compliance settings feature switch is enabled.

### Create subscription centers in outbound marketing

If you haven’t already, [create your subscription centers](set-up-subscription-center.md) in outbound marketing.

## Set up subscription centers in Customer Insights - Journeys

In **Settings**, connect the outbound marketing subscription center to Customer Insights - Journeys compliance settings:

1. Go to **Settings** > **Customer engagement** > **Compliance**.
1. Select **+ New setting** in the top toolbar, then select **+ With subscription center** from the dropdown.

    > [!div class="mx-imgBorder"]
    > ![Screenshot of the new settings dropdown.](media/outbound-subscription-dropdown.png "Screenshot of the new settings dropdown")

1. A pane titled "Quick Create: Compliance" will appear. Fill out the following settings:
    1. **Setting name**: Select a meaningful name that will be easy to identify.
    1. **Company address**: The address that is used in the email footer.
    1. **Consent model**:
        - *Restrictive*: If consent isn't specified, assume it isn't allowed.
        - *Non-restrictive*: If consent isn't specified, assume it's allowed.
    1. **Tracking consent**: Enable this option to get tracking consent from customers.
    1. **Select a subscription center**: Select the subscription center you set up in outbound marketing.

        > [!div class="mx-imgBorder"]
        > ![Screenshot of the quick create pane.](media/outbound-subscription-quick-create.png "Screenshot of the quick create pane")

    1. Select **Save and close**.

## Use a subscription center in a Customer Insights - Journeys email

Now you can use the subscription center you've set up in a Customer Insights - Journeys email. To do so, follow the steps below.

1. Open or create a new email message in the Customer Insights - Journeys email editor.
1. Select the email header and go to **Email Settings** in the right pane.
1. Under **Compliance**, select the compliance profile with the subscription center you set up in the "Quick Create: Compliance" settings in the previous step.

    > [!div class="mx-imgBorder"]
    > ![Screenshot of selecting the subscription center under Compliance.](media/outbound-subscription-compliance-select.png "Screenshot of selecting the subscription center under Compliance")

### See also

[Outbound marketing compliance settings](privacy-use-features.md)
[Manage user compliance settings in Customer Insights - Journeys](real-time-marketing-compliance-settings.md)
[Manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
