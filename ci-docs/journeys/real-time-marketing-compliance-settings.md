---
title: Consent management overview
description: 'Consent management in Customer Insights – Journeys: Learn how to set up, manage, and enforce user consent to stay compliant with privacy regulations. Start managing consent today.'
ms.date: 06/20/2025
ms.topic: concept-article
author: petrjantac
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:06/20/2025
---

# Stay compliant with privacy regulations

Regional privacy laws like GDPR (EU), CAN-SPAM (US), CCPA (California), HIPAA (US healthcare), and others govern sending commercial communications. These regulations protect people's privacy and make sure they get only relevant and expected communications.

**Why does compliance matter?**

Following these regulations helps you avoid legal penalties, improves user experience, and increases email engagement and deliverability. If you don't comply, your messages can be blocked or sent to spam.

**How do I stay compliant?**

Use a consent management system to track and honor user preferences. You can:

- Use the built-in Consent Center in Customer Insights – Journeys, which supports real-time consent capture and enforcement.
- Integrate your existing consent management system using the extensibility features of Customer Insights – Journeys.

## Manage user compliance settings and consent data

The consent is captured and stored at the contact point level. A contact point is the destination for a message—such as an email address or phone number.

- **Channel-specific consent**: Consent is stored per channel and per destination. For example, the email address somebody@contoso.com can consent to receive commercial communications about upcoming events, while another email address or phone number might not.

- **Greater flexibility and control**: Contact point consent lets customers control where they receive communications from your organization.

- **Entity-agnostic orchestration**: One of the main benefits of contact point consent is that it lets real-time journeys orchestrate across any entity—including contacts, leads, Customer Insights - Data profiles, and more. This approach ensures consistent consent enforcement regardless of the data source.

The **consent model** uses a **flexible hierarchy** that you can tailor to meet your business and compliance requirements.

:::image type="content" source="media/real-time-marketing-consent-hierarchy.png" alt-text="Consent hierarchy" lightbox="media/real-time-marketing-consent-hierarchy.png":::

- At the top of the hierarchy are [compliance profiles](#compliance-profiles).
- Each compliance profile can include multiple purposes.
- A single purpose can be shared across multiple compliance profiles.
- Each purpose can be extended with multiple topics to provide more granular control over consent. One topic can link only to a single purpose.

> [!IMPORTANT]
> By default, real-time journeys doesn't evaluate the contact's `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. To enable these checks, go to **Settings** > **Overview** > **Feature switches** and turn on the toggle labeled "Check contact consent in real-time journeys." The preference center doesn't update the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. This means users can't change these specific consent preferences through the preference center. If you manage consent using contact point consent, don't rely on the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=51f182de-841f-41e8-85c4-49af1caaeeb0]

## Compliance profiles

Compliance profiles are the central hub for managing consent and compliance in Customer Insights - Journeys. They define how consent is captured, stored, and enforced across your marketing communications.

Each compliance profile stores essential configuration details, such as:

- Company address
- Unsubscribe link behavior
- Associated purposes and topics

**Preference center management**

The type of compliance profile (preference center or external link) affects how users manage their consent preferences. Compliance profile settings change based on the type of compliance profile you create or change.

### Why use multiple compliance profiles?

Organizations often create multiple compliance profiles to support:

- **Brand or line-of-business (LOB) separation**: For example, separate compliance profiles for different brands or business units let you tailor consent settings and messaging strategies. Each compliance profile can have its own company address.

- **Regional compliance requirements**: Different regions can require different enforcement models.
  **Example**:
  - **United States:** A commercial purpose might use a nonrestrictive model, letting messages be sent unless someone opts out.
  - **France:** The same purpose might use a restrictive model, requiring explicit opt-in because of GDPR.

- **Localized preference centers**: Each compliance profile can have its own preference center design, supporting localization and regulatory alignment.

> [!NOTE]
> **Deactivating compliance profiles and contact point consent records**
>
> You can deactivate a compliance profile or a contact point consent record at any time. But the **system continues to use the deactivated compliance profile or contact point record** because existing journeys or messages can still rely on them. To update a user's consent, change the consent value in the contact point consent record instead of relying on deactivation.

> [!IMPORTANT]
> Unsubscribe links in messages expire six months after the link is created and don't work after that.

### Set up a compliance profile

To create or set up a compliance profile, go to **Settings** > **Customer engagement** > **Compliance profiles** to define the consent model, company address, and customize the preference center page for your users.

> [!NOTE]
> When you create a new compliance profile, you can **Use previously captured consent**. This option helps you move from a legacy *compliance profile with a preference page* to one with a preference center. This way, any previously captured consent applies to the new compliance profile.

There are two types of compliance profiles:

- Compliance profile with a **preference center**: Use this option if you manage consent within Customer Insights - Journeys. It includes a built-in preference center page that lets users manage their consent preferences directly.
- Compliance profile with **external link**: Choose this option if you want to connect to an external consent management system or use a marketing form instead of the default preference center form.

#### Compliance profile with preference center

> [!IMPORTANT]
> Preference centers don't change a contact's `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields.

Customer Insights - Journeys uses preference centers to let customers control the types of communications they want to get and the contact point where they want to get them. They work with all supported entity types: leads, contacts, Customer Insights - Data profiles, and more. You can set up preference centers to match company branding and include options for users to manage consent for purposes and topics. Preference centers also support multi-brand consent, so you can manage consent independently for each line of business.

Learn more: [Create Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)

#### Compliance profile with an external link

A compliance profile with an external link lets you set a website URL that points to an external consent management page. The URL you set in the compliance profile is included in messages sent with this compliance profile.

> [!CAUTION]
> A compliance profile with an external link generates an unsubscribe link that doesn't include user identification for external consent management systems. The link can have tracking elements like `contextId` and `msdynmkt_trackingcontext`, but these are only for internal use by Customer Insights - Journeys.

If you want to include a link to an external consent management system’s preference page, create the unsubscribe link directly in your message template. Use the link personalization feature to add user identification to the link so the external system can recognize and manage the user's preferences.

## Purposes

A **data use purpose consent** (called a **purpose**) defines the specific reason for collecting consent. It's usually tied to a legal basis or justification, like getting consent to contact someone for commercial marketing.

The three standard types of purposes are:

- **Commercial communication**: Like promotional emails or newsletters
- **Transactional communication**: Like order confirmations or service updates
- **Tracking**: Like tracking user behavior for analytics, such as link clicks and message opens (using tracking pixels in messages), and identifying users for [form prefill](real-time-marketing-form-prefill.md).

When you create a new compliance profile, each type of purpose is included by default. They're fully customizable to fit your organization's needs. You can also create more purposes and assign them to one or more compliance profiles.

Purposes in the consent model are **reusable** and can be **shared across multiple compliance profiles**. This flexibility lets you do things like:

- **Unified consent management across brands or regions**: For example, a Contoso Global compliance profile might define a Commercial purpose that's also used by Contoso Northwest and Contoso East. Customers interacting with Contoso Northwest can opt in or out of communications from Contoso Global—directly from Contoso Northwest's preference center.

- **Localized preference centers with shared consent**: Sharing purposes also lets you create multiple compliance profiles with different preference center designs, like different languages or layouts, while still using the same consent data. For example, you can have two compliance profiles with identical purposes but separate preference centers in English and Czech, so customers get a consistent consent experience across regions.

Purpose consent also lets customers create line-of-business (LOB) separation without using Dataverse business units or separate compliance profiles. Each LOB has a preference center set up for each business, and each LOB has a set of purposes specific to it. Each message (email or text message) is tied to a single preference center and an associated purpose.

Each organization might need to define separate purposes for each LOB. For example, Contoso Northwest might want to manage consent separately from Contoso East. They'd create a Commercial Communication purpose for each LOB so they can manage opt-in or opt-out of Commercial Communication independently for each LOB.

### Consent enforcement models

The **enforcement model** settings on a purpose control how consent is checked before a message is sent. Messages sent to a purpose use that purpose's enforcement model to decide if the message is sent. You can choose from three enforcement models, depending on your regulatory needs:

- **Restrictive**: Messages are sent only to contact points with opted-in consent records for this purpose (or topic).
- **Non-restrictive**: Messages are sent to all contact points unless they have an opted-out consent record for this purpose (or topic).
- **Disabled**: Messages are sent to all contact points. Consent records aren't checked before sending messages to this purpose (or topic).

## Topics

Each **purpose** in the consent model can include multiple **topics**, which represent specific types of communications. Topics let customers fine-tune their consent preferences by selecting the exact types of messages they want to receive.

**Example**

For the Commercial purpose in the Contoso Northwest compliance profile, you can define topics like:

- Newsletters
- Daily deals
- Product announcements

*This setup lets customers opt in or out of individual topics based on their interests.*

When marketers create a message, they select a purpose and can optionally choose a topic associated with that purpose. Recipients then manage their preferences at the topic level, which gives them more granular control.

Purposes and topics have a hierarchical relationship:

- A topic belongs to only one purpose.
- A purpose can contain multiple topics.

Topics inherit the **enforcement model** of their parent **purpose**. When a message is configured with both a purpose and a topic, the system checks for consent at both levels before sending the message.

> [!IMPORTANT]
> **Dual consent requirement**: The system sends a message associated with a topic only if the contact point has valid consent for both the purpose and the topic. If a contact point doesn't have consent for the parent purpose, the system doesn't send any associated topics, even if the contact opted into a specific topic.

**Restrictive enforcement example**

If the parent purpose uses a restrictive enforcement model, the contact point needs an opt-in consent record for both the purpose and the topic for the system to deliver the message.

## Using `DoNotEmail`, `DoNotBulkEmail`, and `DoNotTrack` fields in real-time journeys

By default, real-time journeys in Customer Insights – Journeys don't evaluate the contact's `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields.

To enable these checks:

1. Go to **Settings** > **Overview** > **Feature switches**.
1. Turn on the toggle labeled "Check contact consent in real-time journeys."

> [!IMPORTANT]
> The preference center doesn't update the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. As a result, users can't manage these specific consent preferences through the preference center.

> [!NOTE]
> **Best Practice**: If you plan to manage consent using contact point consent, don't rely on the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. Instead, use contact point consent records as the single source of truth for consent evaluation.

### When the feature switch "Check contact consent in real-time journeys" is enabled

#### Email consent checks

- **Commercial purpose**: Both `DoNotEmail` and `DoNotBulkEmail` must be false (that is, not opted out) for the email to be sent.
- **Transactional purpose**: Only `DoNotEmail` must be false.

These checks are in addition to the contact point consent opt-in or opt-out checks for emails sent by journeys.

These field checks apply only to contacts. They're not performed for other entity types like leads or Customer Insights - Data profiles.

#### Tracking consent checks

To insert tracking links and pixels into a message:

- The contact's `DoNotTrack` field must allow tracking.
- The contact point consent record must also allow tracking.

These checks apply only to contacts. They don't apply to other entity types.

#### Text and custom channel messages

Text messages and custom channel messages don't use the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields when evaluating consent.

## See also

- [Manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md)
- [Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)
- [One-click unsubscribe support for emails](one-click-unsubscribe.md)
- [Double opt-in in real-time journeys](real-time-marketing-double-opt-in.md)
- [Migrate consent records to Customer Insights - Journeys](real-time-marketing-migrate-consent.md)
- [Consent management for business units](real-time-marketing-consent-business-units.md)
- [Create a consent record using a cloud flow](consent-record-creation.md)
- To learn more about transitioning from outbound marketing to real-time journeys, see [Consent management and double opt-in transition guidance](real-time-marketing-consent-transition.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
