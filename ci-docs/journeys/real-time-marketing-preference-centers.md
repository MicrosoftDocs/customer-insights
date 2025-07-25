---
title: Create branded, customized preference centers to manage customer consent
description: Learn how to set up preference centers to collect and manage consent from your customers.
ms.date: 09/10/2024
ms.topic: reference
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: sfi-image-nochange
---

# Create branded, customized preference centers to manage customer consent

> [!IMPORTANT]
> Starting on October 10, 2024, unsubscribe links will expire six months after the link is created and will no longer work.

Preference centers in Customer Insights - Journeys allow you to provide customers with branded experiences to sign up for communications and fine-tune their preferences to ensure they receive the right communications.

## Creating preference centers

In Customer Insights - Journeys, each compliance profile starts with a default preference center that you can configure. To setup the preference center, go to **Settings** > **Customer engagement** > **Compliance profiles** and select the compliance profile with the preference center to update. Follow the link to the preference center to make updates.

> [!div class="mx-imgBorder"]
> ![Compliance profile screenshot.](media/real-time-marketing-compliance-profile.png "Compliance profile screenshot")

> [!NOTE]
> Customers who have used Customer Insights - Journeys preference pages prior to the introduction of the preference center will have a compliance profile already created with the previously configured preference page in place of a preference center. It is recommended that customers replace preference pages with preference centers.

The default preference center includes options for users to opt in or opt out of the **Commercial** and **Tracking** purposes, along with the default contact point of the user’s email address. You can update how the purposes capture consent in various ways to ensure you capture consent appropriately:

- Update the contact point(s) for which consent is captured
- Update the page directly to change the text displayed for each purpose to make it clear to the user
- Change whether checking the box opts the user in or out of communications
- Add or remove a purpose so the preference center collects the right information
- Add topics to the form to capture more granular preferences

:::image type="content" source="media/real-time-marketing-preference-center.png" alt-text="Preference center screenshot." lightbox="media/real-time-marketing-preference-center.png":::

In addition, you can add content and update the branding and styling of the page to make the experience seamless for your users.

> [!NOTE]
> Customer Insights - Journeys preference centers will update the contact point consent record for the email and phone number channels. It will not make updates to the **DoNotEmail** and **DoNotBulkEmail** fields on the contact or lead record. This is because there is no mapping between Customer Insights - Journeys purposes and topics to the fields on the contact or lead.

## Advanced preference center customization

Preference center forms are built on top of Customer Insights - Journeys forms which enable you to customize the forms by applying your own CSS and add custom JavaScript.

Learn more: [Manage Customer Insights - Journeys forms](real-time-marketing-manage-forms.md#advanced-form-customization)

## Replacing a preference page with a preference center

> [!IMPORTANT]
> We recommend replacing preference pages with preference centers to take full advantage of the consent features available in Customer Insights - Journeys.

To replace your preference page with a preference center, first create a new compliance profile of type preference center and use the **Use previously captured consent** option to use the consent already gathered by your preference page compliance profile. Doing so will result in the new preference center sharing the same commercial, transactional, and tracking purposes from the preference page. The result is shared consent between the two profiles, which avoids the need to create new contact point consent records for your new compliance profile.

Once configured, you can start using the new preference center compliance profile in messages. All existing and future messages should update their **Compliance profile** to reference the new preference center compliance profile.

### See also

[Manage user compliance settings in Customer Insights - Journeys](real-time-marketing-compliance-settings.md)
[Manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md)
[Outbound marketing compliance settings](privacy-use-features.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
