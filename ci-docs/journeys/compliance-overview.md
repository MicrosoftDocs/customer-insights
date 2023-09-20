---
title: Compliance overview
description: Learn how to manage compliance settings in Dynamics 365 Customer Insights - Journeys and outbound marketing.
ms.date: 09/20/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Manage user compliance settings

[!INCLUDE[consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> This article applies to Customer Insights - Journeys *and* outbound marketing.

Customer Insights - Journeys and outbound marketing have distinct but related constructs for supporting consent and regulatory compliance for communications with customers. This article provides an overview of these differences along with references to more detailed information on ways to approach compliance.

## Consent data capture and storage

In Customer Insights - Journeys, consent is captured and stored at the contact point. A contact point is the destination for a message (for example, an email address or phone number). Customer consent is stored on a per-channel basis. For example, the email `somebody@example.com` has consented to receive commercial communications about upcoming events.  

The primary benefit of contact point consent is that it allows Customer Insights - Journeys to orchestrate real-time journeys across any entity. Orchestrating across journeys means you can enforce consent for leads, Customer Insights - Data profiles, contacts, and any other entity. This approach is opposed to outbound marketing journeys, which can only orchestrate journeys for contact entities.

In outbound marketing, consent is captured and stored on the contact entity the `DoNotEmail`, `DoNotBulkEmail` and `DoNotTrack` fields that apply to the entire contact record and all its email addresses. This approach doesn't allow for different consent to be captured for a contact’s multiple email addresses, phone numbers, etc.

> [!IMPORTANT]
> Real-time journeys check the contact's `DoNotEmail`, `DoNotBulkEmail` and `DoNotTrack` fields when an email message is sent to a contact entity. This behavior matches outbound marketing's consent enforcement. For an email to be sent to a contact from a real-time journey, both the contact's fields and the contact point consent records for the email address must all allow the message to be sent. These fields are not checked for messages sent to other entities (for example, leads). These fields are also not checked for text or custom channel messages.

> [!IMPORTANT]
> Outbound marketing does not check contact point consent records to evaluate consent when sending messages. This means that outbound marketing messages will not be affected by contact point consent records.

## Compliance profiles

Compliance profiles are the hubs to manage consent and compliance in Dynamics 365 Customer Insights - Journeys. Compliance profiles govern how consent is captured and enforced. Compliance profiles store information such as company address, the preference management experience, and related configuration. Compliance profile settings vary based on the type of compliance profile you're creating or modifying.  

Learn more: [Compliance profiles](real-time-marketing-compliance-settings.md#compliance-profiles).  

## User contact preferences

There are four ways that users can manage their contact preferences: preference centers, preference pages, subscription centers, and external links.  

### Preference centers

> [!TIP]
> Preference centers are the recommended way to enable customers to manage their communication preferences with your organization.

Customer Insights - Journeys uses preference centers to enable customers to control the types of communications they wish to receive and the contact point at which they wish to receive them. They work with all supported entity types: leads, contacts, etc. Preference centers can be configured to match company branding and can include options for users to manage the consent for purposes and topics. Preference centers also support multi-brand consent, enabling you to manage consent independently for each of your lines of business.

Learn more: [Create Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)

### Preference pages

> [!IMPORTANT]
> We recommend replacing preference pages with preference centers to take full advantage of the consent features available in Customer Insights - Journeys.

Outbound marketing uses preference pages as another way to manage user consent. A preference page is a web page where your customers can change their consent settings for receiving emails and text messages and for tracking. You can't create a new preference page. Instead, you can customize the language on the page for updating contact point consent as used in outbound marketing. With the introduction of preference centers, existing preference pages will continue to support users updating their consent. However, moving forward, all new compliance profiles use the enhanced functionality of preference centers.  

Learn more: [Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)

### Subscription centers

> [!CAUTION]
> Subscription centers can only be used with contact entities. Leads and Customer Insights - Data profiles are not supported by subscription centers. If you plan to send communication to these entity types we recommend using a preference center.

Outbound marketing subscription centers are marketing pages that contacts can use to manage their communication preferences and contact details with your organization. Subscription centers must be configured in outbound marketing, but can be used by real-time journeys. Subscription centers don't work with real-time journey's purposes and topics. Only data on the contact record (such as the **DoNotBulkEmail** attribute) and Subscription Lists can be updated from a subscription center.

Learn more: [Set up a subscription center](set-up-subscription-center.md)

Customer Insights - Journeys can also use subscription centers if your journeys only target contacts. Using subscription centers from a real-time journey can enable you to start sending messages from real-time journeys before you transition to the newer preference center option.

> [!NOTE]
> When a subscription center is used in a real-time journey, updates to the `{{DoNotBulkEmail}}` field made by the user will result in a contact point consent record being created or updated for the commercial purpose of the compliance profile configured on the email message.

Learn more: [Use outbound subscription centers in Customer Insights - Journeys](real-time-marketing-outbound-subscription.md)

### External links

> [!CAUTION]
> External links are currently designed to work with externally hosted subscription centers and can only be used with contact entities. Leads and Customer Insights - Data profiles are not supported by external links. If you plan to send communication to these entity types we recommend using a preference center.

> [!TIP]
> If you want to include a link to an external preference management page and the modifications made to the URL do not work for your use case, we recommend that you configure your messages to include the preference management link directly in the message template and not use the built-in compliance `{{PreferenceCenter}}` tokens.

External links allow you to configure a website URL that points to an externally hosted subscription center. The URL configured in the compliance profile will be included in messages sent with this compliance profile. When the URL is inserted into a message, it is modified to include a query string parameter at the end to enable the receiving subscription center to identify the contact that was sent the message.

[!INCLUDE[footer-include](./includes/footer-banner.md)]
