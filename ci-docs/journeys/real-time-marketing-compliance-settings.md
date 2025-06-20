---
title: Consent management overview
description: Learn how to manage consent settings in Dynamics 365 Customer Insights - Journeys.
ms.date: 6/20/2025
ms.topic: concept-article
author: petrjantac
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

The consent is captured and stored at the contact point level. A contact point is the destination for a message—such as an email address or phone number.

- **Channel-specific consent**:
Consent is stored per channel and per destination. For example, the email address somebody@example.com may have consented to receive commercial communications about upcoming events, while another email or phone number may not.

- **Greater flexibility and control:**
Contact point consent gives customers more control over where they want to receive communications from your organization.

- **Entity-Agnostic Orchestration:**
One of the major benefits of contact point consent is that it enables real-time journeys to orchestrate across any entity—including contacts, leads, Customer Insights - Data profiles, and more. This ensures consistent consent enforcement regardless of the data source.

The **consent model** is designed with a **flexible hierarchy** that can be tailored to meet your business and compliance requirements.

:::image type="content" source="media/real-time-marketing-consent-hierarchy.png" alt-text="Consent hierarchy" lightbox="media/real-time-marketing-consent-hierarchy.png":::

- At the top of the hierarchy are [Compliance Profiles](#compliance-profiles).
- Each Compliance Profile can include multiple Purposes.
- A single Purpose can be shared across multiple Compliance Profiles.
- Each Purpose can be optionally extended with multiple Topics to provide more granular control over consent. One topic can be linked only to a single Purpose.

> [!IMPORTANT]
> By default, real-time journeys does **not** evaluate the contact's `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. To enable these checks, go to **Feature switches** and turn on the toggle labeled "Check contact consent in real-time journeys." The Preference Center does not update the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. This means users cannot change these specific consent preferences through the Preference Center. If you plan to manage consent using contact point consent, it is not recommended to rely on the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=51f182de-841f-41e8-85c4-49af1caaeeb0]

## Compliance profiles

Compliance profiles are the central hubs for managing consent and compliance in Customer Insights - Journeys. They define how consent is captured, stored, and enforced across your marketing communications.

Each compliance profile stores essential configuration details such as:

- Company address
- Unsubscribe link behavior
- Associated purposes and topics

**Preference Center Management:**
The type of compliance profile (e.g., with Preference Center or External Link) influences how users manage their consent preferences. Compliance profile settings vary based on the type of compliance profile you're creating or modifying.

### Why use multiple compliance profiles?

Organizations often create multiple compliance profiles to support:

- **Brand or Line-of-Business (LOB) Separation:**
For example, separate compliance profiles for different brands or business units allow tailored consent settings and messaging strategies. Each compliance profile can have its own company address.

- **Regional Compliance Requirements:**
Different regions may require different enforcement models.
  **Example:**
  - **United States:** A commercial purpose might use a nonrestrictive model, allowing messages unless opted out.
  - **France:** The same purpose might use a restrictive model, requiring explicit opt-in due to GDPR.

- **Localized Preference Centers:**
Each compliance profile can have its own Preference Center design, supporting localization and regulatory alignment.

> [!NOTE]
> **Deactivating compliance profiles and contact point consent records**
>
> You can deactivate a compliance profile or a contact point consent record at any time. However, the **system continues to use the deactivated compliance profile or contact point record**. This is because existing journeys or messages may still rely on them. If you need to update a user's consent, you should directly modify the consent value within the contact point consent record itself, rather than relying on deactivation.

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
- Tracking – e.g., consent to track user behavior for analytics such as link click and message open tracking (via tracking pixels embedded in messages), and identify users for [form prefill](real-time-marketing-form-prefill.md)

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

Topics inherit the **enforcement model** of their parent **Purpose**. This means that when a message is configured with both a Purpose and a Topic, the system checks for consent at both levels before sending the message.

> [!IMPORTANT]
> **Dual consent requirement**
>
> - A message associated with a topic will only be sent if the contact point has valid consent for both the Purpose and the Topic.
> - If a contact point does not have consent for the parent Purpose, none of the associated Topics will be sent—even if the contact has opted into a specific topic.

**Restrictive Enforcement Example:**
If the parent Purpose uses a restrictive enforcement model, then an opt-in consent record is required for both the Purpose and the Topic at the contact point level in order for the message to be delivered.

## Using DoNotEmail, DoNotBulkEmail, and DoNotTrack Fields in Real-Time Journeys

By default, real-time journeys in Customer Insights – Journeys do **not** evaluate the contact's `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields.

To enable these checks:

1. Navigate to Feature switches.
1. Turn on the toggle labeled "Check contact consent in real-time journeys."

> [!IMPORTANT]
> The Preference Center does not update the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. As a result, users cannot manage these specific consent preferences through the Preference Center.

> [!NOTE]
> **Best Practice**
>
> If you plan to manage consent using contact point consent, it is **not recommended to rely** on the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields. Instead, use contact point consent records as the single source of truth for consent evaluation.

### When the feature switch "Check contact consent in real-time journeys" is Enabled

#### Email Consent Checks

- **Commercial Purpose:**
Both `DoNotEmail` and `DoNotBulkEmail` must be false (i.e., not opted out) for the email to be sent.
- **Transactional Purpose:**
Only `DoNotEmail` must be false.

These checks are performed in addition to the contact point consent opt-in/opt-out checks for emails sent by journeys.

These field checks apply only to contacts. They are not performed for other entity types such as leads or Customer Insights - Data profiles.

#### Tracking consent checks

To insert tracking links and pixels into a message:

- The contact’s `DoNotTrack` field must allow tracking.
- The contact point consent record must also allow tracking.

These checks apply only to contacts, not to other entity types.

#### Text and custom channel messages

Text messages and custom channel messages do not use the `DoNotEmail`, `DoNotBulkEmail`, or `DoNotTrack` fields when evaluating consent.

## See also

- [Manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md)
- [Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)
- [One-click unsubscribe support for emails](one-click-unsubscribe.md)
- [Double opt-in in real-time journeys](real-time-marketing-double-opt-in.md)
- [Migrate consent records to Customer Insights - Journeys](real-time-marketing-migrate-consent.md)
- [Consent management for business units](real-time-marketing-consent-business-units.md)
- [Create a consent record using a cloud flow](consent-record-creation.md)
- To learn more about transitioning from outbound marketing to real-time journeys here, visit [Consent management and double opt-in transition guidance](real-time-marketing-consent-transition.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
