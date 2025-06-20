---
title: Consent management overview
description: Learn how to manage consent settings in Dynamics 365 Customer Insights - Journeys.
ms.date: 6/20/2025
ms.topic: concept-article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Stay Compliant with Privacy Regulations

The sending of commercial communications is governed by regional privacy laws such as the GDPR (EU), CAN-SPAM (US), CCPA (California), HIPAA (US healthcare), and others. These regulations are designed to protect individuals' privacy and ensure they receive only relevant and expected communications.

**Why it matters?**
Complying with these regulations not only helps you avoid legal penalties but also improves the user experience, leading to higher engagement and better deliverability of your emails. Non-compliance can result in blocked messages or reduced inbox placement.

**How to stay compliant?**
We strongly recommend using a consent management system to track and honor user preferences. You can:

- Use the built-in Consent Center in Customer Insights – Journeys, which supports real-time consent capture and enforcement.
- Integrate your existing consent management system using the extensibility features of Customer Insights – Journeys.

## Manage user compliance settings and consent data

In real-time journeys, consent is captured and stored at the contact point. A contact point is the destination for a message (for example, an email address or phone number). Customer consent is stored on a per-channel basis. For example, the email `somebody@example.com` has consented to receive commercial communications about upcoming events.

The primary benefit of contact point consent is that it allows Customer Insights - Journeys to orchestrate real-time journeys across any audience (entity). Orchestrating across journeys means you can enforce consent for leads, Customer Insights - Data profiles, contacts, and any other entity.

The consent model is designed with a flexible hierarchy that can be tailored to meet your business and compliance requirements.

:::image type="content" source="media/real-time-marketing-consent-hierarchy.png" alt-text="Consent hierarchy" lightbox="media/real-time-marketing-consent-hierarchy.png":::

- At the top of the hierarchy are [Compliance Profiles](#compliance-profiles).
- Each Compliance Profile can include multiple Purposes.
- A single Purpose can be shared across multiple Compliance Profiles.
- Each Purpose can be optionally extended with multiple Topics to provide more granular control over consent. One topic can be linked only to a single Purpose.

> [!IMPORTANT]
> By default, real-time journeys does **not** evaluate the contact's `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. To enable these checks, go to **Feature switches** and turn on the toggle labeled "Check contact consent in real-time journeys." The Preference Center does not update the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. This means users cannot change these specific consent preferences through the Preference Center. If you plan to manage consent using contact point consent, it is not recommended to rely on the DoNotEmail, DoNotBulkEmail, or DoNotTrack fields.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=51f182de-841f-41e8-85c4-49af1caaeeb0]

## Compliance profiles

Compliance profiles are the hubs to manage consent and compliance in Customer Insights - Journeys. Compliance profiles govern how consent is captured and enforced. Compliance profiles store information such as company address, the unsubscribe link management, and related configuration. Compliance profile settings vary based on the type of compliance profile you're creating or modifying.

Compliance profiles are the containers of consent settings. In some instances, customers might want to separate consent for brands or lines-of-business (LOBs) by creating separate compliance profiles for each. Compliance profiles give marketers the ability to create specific consent settings for various LOBs. For instance, if there are headquarters in different regions whose physical addresses should show for recipients in the applicable region, each compliance profile can have its own address.

Another reason for having multiple compliance profiles would be to support different compliance requirements across regions. For example, a company that operates in the United States and France might choose to have a separate compliance profile for those two locations. Within the United States version, the commercial purpose could be set to a nonrestrictive enforcement model because the U.S. isn't subject to European regulations. Within the France version, however, they might set the commercial purpose to the restrictive enforcement model to require explicit consent before sending any commercial or promotional materials.

> [!NOTE]
> Currently, you can deactivate a compliance profile or contact point consent record. However, deactivated profiles and contact point consent records will still be used and enforced because existing journeys or messages sent may rely on them. Should you wish to update a user's consent, go to the contact point consent record itself and change the consent value.

> [!IMPORTANT]
> Unsubscribe links in messages will expire six months after the link is created and will no longer work.

### Configure compliance profile

To create or configure compliance profile, administrators can go to **Settings** > **Customer engagement** > **Compliance profiles** to define the consent model, the company address, and customize the preference center page for your end users.

> [!NOTE]
> When you create a new compliance profile, you can **Use previously captured consent**. This option is intended to facilitate transitioning from a legacy *compliance profile with a preference page* to one with a preference center. Doing so ensures that any previously captured consent applies to the new compliance profile.

There are two main types of compliance profiles available:

- Compliance Profile with **Preference Center** -
Use this option if you manage consent within Customer Insights - Journeys. It includes a built-in Preference Center page that allows users to manage their consent preferences directly.
- Compliance Profile with **External Link** -
Choose this option if you need to integrate with an external consent management system or prefer to use a marketing form instead of the default Preference Center form.

#### Compliance Profile with Preference center

> [!IMPORTANT]
> Preference center does not modify a contact's `DoNotEmail`,  `DoNotBulkEmail`, or `DoNotTrack` fields.

Customer Insights - Journeys uses preference centers to enable customers to control the types of communications they wish to receive and the contact point at which they wish to receive them. They work with all supported entity types: leads, contacts, Customer Insights - Data profiles, etc. Preference centers can be configured to match company branding and can include options for users to manage the consent for purposes and topics. Preference centers also support multi-brand consent, enabling you to manage consent independently for each of your lines of business.

Learn more: [Create Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)

#### Compliance Profile with External link

Compliance profile with External link allows you to configure a website URL that points to an external consent management page. The URL configured in the compliance profile will be included in messages sent with this compliance profile.

> [!CAUTION]
> A Compliance Profile with External Link currently generates an Unsubscribe link that does not include user identification accessible for external consent management systems. Although the link can contain tracking elements such as `contextId` and `msdynmkt_trackingcontext`, these are designed solely for internal use by Customer Insights - Journeys.

If you want to include a link to an external consent management system’s preference page, we recommend creating the Unsubscribe link directly within your message template. Use the link personalization feature to embed user identification into the link, allowing the external system to recognize and manage the user's preferences accurately.

## Purposes

A **Data Use Purpose Consent** (referred to as a **purpose**) defines the specific reason for which consent is collected. It is typically tied to a legal basis or justification—such as obtaining consent to contact someone for commercial marketing.

There are three standard types of purposes:

- Commercial Communication – e.g., promotional emails or newsletters
- Transactional Communication – e.g., order confirmations or service updates
- Tracking – e.g., consent to track user behavior for analytics and identify users for [form prefill](real-time-marketing-form-prefill.md)

When you create a new Compliance Profile, there are purposes of each type included by default. However, they are fully customizable to suit your organization’s needs. You can also create additional purposes and assign them to one or more compliance profiles.

Purposes in the consent model are **reusable** and can be **shared across multiple compliance profiles**. This flexibility enables several important scenarios:

- **Unified consent management across brands or regions** -
For example, a Contoso Global compliance profile might define a Commercial purpose that is also used by Contoso Northwest and Contoso East. This allows customers interacting with Contoso Northwest to opt in or out of communications from Contoso Global—directly from Contoso Northwest’s Preference Center.

- **Localized Preference Centers with Shared Consent** -
Sharing purposes also enables you to create multiple compliance profiles with different Preference Center designs—such as different languages or layouts—while still referencing the same underlying consent data.
For instance, you could have two compliance profiles with identical purposes but separate Preference Centers in English and Czech, ensuring a consistent consent experience across regions.

Purpose consent also allows customers to create line-of-business (LOB) separation without using Dataverse business units or separate compliance profiles. Each LOB has a preference center configured for each business, and each LOB has a set of purposes associated with it that's specific to each LOB. Each message (for example, email or text message) is tied to a single preference center and an associated purpose.

Each organization might need to define separate purposes for each of their LOBs individually – for example, Contoso Northwest might want to manage consent independently from Contoso East. They would create a Commercial Communication Purpose for each LOB so they could manage opt-in or opt-out of Commercial Communication independently for each LOB.

### Consent enforcement models

The **Enforcement model** settings on a purposes control how consent is evaluated before a message is sent. Messages sent to a purpose use that purpose's enforcement model to evaluate if the message is or is not sent. There are three enforcement models that can be chosen depending on your regulatory needs:

- **Restrictive**: Messages are sent only to contact points that have opted-in contact point consent records for this purpose (or topic).
- **Non-restrictive**: Messages are sent to all contact points unless they have an opted-out contact point consent record for this purpose (or topic).
- **Disabled**: Messages are sent to all contact points. Contact point consent records aren't checked before sending messages to this purpose (or topic).

## Topics

Each **Purpose** in the consent model can include multiple **Topics**, which represent specific types of communications. Topics allow customers to fine-tune their consent preferences by selecting the exact types of messages they wish to receive.

**Example:**
For the Commercial purpose in the Contoso Northwest compliance profile, you might define topics such as:

- Newsletters
- Daily Deals
- Product Announcements

*This setup enables customers to opt in or out of individual topics based on their interests.*

When creating a message, marketers must select a Purpose and can optionally choose a Topic associated with that purpose.
Recipients can then manage their preferences at the topic level, offering more granular control.

There is a hierarchical relationship between purposes and topics:

- A Topic belongs to only one Purpose.
- A Purpose can contain multiple Topics.

Topics use the enforcement model of their parent purpose. Messages that are configured with both a purpose and a topic must have consent for both the purpose and the topic in order for the message to be sent. If a contact point doesn't have consent to send to a purpose, no messages to that purpose's topics are sent to the contact point. For example, if the parent purpose has a restrictive enforcement model, sending a message to a topic requires an opt-in contact point consent record for both the purpose and the topic associated with the contact point consent.

## Step-by-step consent configuration

START WITH DEFAULTS





#### Contact point consent

A contact point is the destination for a message. For example, an email address or phone number is a contact point. Real-time journeys consent is contact point based, which means that consent is stored per destination and per channel. For example, the email `somebody@contoso.com` has consented to receive commercial communications about upcoming events. Consent in real-time journeys is stored in contact point consent records. In comparison, outbound marketing's consent model only relies on the consent on the *contact record*. With real-time journeys's contact point consent, customers have more control over where they want to receive marketing messages from your organization.

Another benefit of contact point consent is that it allows for real-time journeys to orchestrate journeys across any entity including contacts, leads, etc.





##### Considerations for contact entities

> [!NOTE]
> If you're using Customer Insights - Journeys without the outbound marketing module installed, the additional consent enforcement checks described in this section aren't performed. If outbound marketing isn't present, only the contact point consent enforcement model is used to determine if messages are sent.

When outbound marketing is provisioned, real-time journeys make consent enforcement checks using data stored on the contact record.

To aid in the transition from outbound marketing, real-time journeys check the consent stored on contact entities in addition to the purpose and topic-based consent checks. Real-time journeys look at the contact's `DoNotEmail`, `DoNotBulkEmail`, and `DoNotTrack` fields when an email message is sent to a contact entity.

In outbound marketing journeys, the contact entities `DoNotEmail` and `DoNotBulkEmail` control if an email is sent. Real-time journeys also check these two fields to match outbound marketing's consent enforcement behavior. For emails with a **commercial** purpose type, the `DoNotEmail` and `DoNotBulkEmail` fields must both be set to allow an email to be sent to the contact. Only the `DoNotEmail` field must be set to allow emails to be sent with a **transactional** purpose type. These checks are done in addition to the Customer Insights - Journeys contact point consent opt-in/opt-out checks for emails sent by journeys. These checks are not performed for other entity types (for example, leads or Customer Insights - Data profiles).

For an email to be sent to a contact from a real-time journey, both the contact's fields and the contact point consent records for the email address must all allow the message to be sent.

Similarly, the contact's `DoNotTrack` field and tracking contact point consent records must both allow tracking in order for tracking links and pixels to be inserted into a message. These three fields aren't checked for messages sent to other entities (for example, leads).

Text and custom channel messages to contacts don't use the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields when evaluating consent.

To learn more about transitioning from outbound marketing to real-time journeys here, visit [Consent management and double opt-in transition guidance](real-time-marketing-consent-transition.md)

## See also

[Manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md)
[Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)
[Outbound marketing compliance settings](privacy-use-features.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
