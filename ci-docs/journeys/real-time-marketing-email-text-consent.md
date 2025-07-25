---
title: Manage consent for email, SMS (text), and custom channel messages
description: Manage consent for email, SMS, and custom channel messages in Customer Insights - Journeys. Learn how to set up, update, and audit consent records for compliance.
ms.date: 07/24/2025
ms.topic: reference
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:06/02/2025
  - sfi-image-nochange
---

# Manage consent for email, SMS (text), voice, and custom channel messages

> [!NOTE]
> Customer Insights - Journeys consent is contact point-based and works for messages you send to contacts, leads, and Customer Insights - Data profiles. The system stores customer consent for each email address or phone number, not for each contact record.

## How consent is respected for emails

When you create a new email message, choose a **Compliance Profile**, a **Purpose**, and, optionally, a **Topic** from that profile in the **Compliance** section of the **Email header** settings. To set up message designation, select the gear icon ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") in the email header. This action opens the **Email header** settings pane. Go to the **Email settings** section.

> [!div class="mx-imgBorder"]
> ![Compliance profile and purpose screenshot.](media/real-time-marketing-email-compliance-settings.png " Compliance profile and purpose screenshot ")

Customer Insights - Journeys sends an email message only if it passes the consent checks set by the **Purpose** and optional **Topic**. The app decides to send or block a message right before sending. This approach makes sure the app doesn't mistakenly send a message to someone who opted out, even if they're included in a journey segment by mistake.

The **Enforcement model** setting on the purpose controls the consent rules. If the purpose uses a "Restrictive" enforcement model, the app sends the email only if the email address explicitly opts in. If the purpose uses a "Nonrestrictive" enforcement model, the app sends the email as long as the email address hasn't opted out. The "Disabled" enforcement model turns off consent checks and lets all messages be delivered. The default "Commercial" purpose uses a "Nonrestrictive" enforcement model for email sending. The default "Transactional" purpose uses a "Disabled" enforcement model. You can change the enforcement models of the purposes in the compliance profile. To learn more about the **Purpose**, **Topic**, and **Enforcement model** concepts, see [Manage user compliance settings in Customer Insights - Journeys](real-time-marketing-compliance-settings.md).

As required for commercial email, the app automatically adds a **Company Address** placeholder and a **Preference Center** placeholder link to the email footer. The company address shows the value set on the **Compliance profile**, and you can edit it directly from the email editor if needed. The **Preference center** link goes to the preference management page set by the **Compliance Profile**, where customers can review and change communication preferences.

The app checks for a company address and unsubscribe link when you select **Ready to send**. The app warns you if either is missing when you send a message to a commercial consent purpose.

> [!NOTE]
> The app shows warnings if, for example, you accidentally delete the company address or the link to the preference center, but it doesn't block you from sending the email. You can replace the company address field with another one or add a link to a custom preference center if you want.

## How consent is respected for SMS (text) and custom channel messages by default

Customer Insights - Journeys rules for sending SMS and custom channel messages differ slightly from the rules for sending email by default. Users always need to opt in to get commercial SMS or commercial custom channel messages.

## How consent is respected for voice channel by default

By default, users need to opt in to voice consent to get commercial voice channel calls. The enforcement model for voice channel is restrictive.

## Consent to track user behavior

Each compliance profile has a specific purpose for tracking user interactions, like message opens and link clicks. Like commercial and transactional purposes, the enforcement model for tracking consent can be restrictive, nonrestrictive, or disabled. If the tracking purpose uses a disabled enforcement model, the system doesn't check tracking consent for messages sent as part of that compliance profile, so it tracks all interactions.

To collect tracking consent, add the tracking purpose to forms and preference centers.

Tracking consent is also considered for the form prefill feature.

> [!NOTE]
> Customer Insights - Journeys can check the **Allow Tracking** field in contact records to see if it can track the contact's interactions. This check is in addition to the Customer Insights - Journeys contact-point consent opt-in or opt-out check for tracking. The system doesn't perform these checks for other entity types, like leads or Customer Insights - Data profiles. This additional check is managed by the [Check contact consent for real-time journeys](#disable-contact-level-consent-checks) feature switch.

> [!IMPORTANT]
> With the July 2023 release, customer consent data uses the new multi-brand consent features. For some Customer Insights - Journeys users, the migration changes the settings that control whether tracking links are included in messages. The changes can prevent tracking in messages if customers haven't given explicit consent. After the migration, to let tracking links be included in messages for customers who haven't provided consent, update the tracking purpose enforcement model of your compliance profile to "Nonrestrictive." This lets tracking links be substituted in emails, as long as the receiver hasn't explicitly opted out of tracking.

## Consent enforcement diagrams

The following tables show how consent is checked by default when you run journeys in Customer Insights - Journeys.

### Restrictive enforcement model

|                      | **Opted out** | **None/not-set** | **Opted in** |
|----------------------|---------------|------------------|--------------|
| **All channels**     | Blocked       | Blocked          | Sent         |
| **Tracking purpose** | Not tracked   | Not tracked      | Tracked      |

For example, in the *restrictive enforcement model*, a customer who hasn't set consent preferences is *blocked* from all communication channels in a journey and isn't tracked.

### Nonrestrictive enforcement model

|                      | **Opted out** | **None/not-set** | **Opted in** |
|----------------------|---------------|------------------|--------------|
| **All channels**     | Blocked       | Sent             | Sent         |
| **Tracking purpose** | Not tracked   | Tracked          | Tracked      |

For example, in the *nonrestrictive enforcement model*, a customer who hasn't set consent preferences is *sent* messages from all communication channels in a journey and is *tracked*.

### Disabled enforcement model

|                      | **Opted out** | **None/not-set** | **Opted in** |
|----------------------|---------------|------------------|--------------|
| **All channels**     | Sent          | Sent             | Sent         |
| **Tracking purpose** | Tracked       | Tracked          | Tracked      |

In the *disabled enforcement model*, *all customers* are *sent* messages from all communication channels in a journey and are *tracked*.

> [!NOTE]
> All channels include email, text, and custom channels.

> [!IMPORTANT]
> If your environment has real-time journeys and outbound marketing installed, the app can check the **Allow email** and **Allow bulk email** fields in contact records to see if email can be sent to a contact's email address. Both fields must be set to **Allow** for a commercial email to be sent. Only the **Allow email** field must be set to allow transactional emails. These checks are in addition to the Customer Insights - Journeys contact-point consent opt-in or opt-out checks for emails sent by journeys. This additional check is managed by the [Check contact consent for real-time journeys](#disable-contact-level-consent-checks) feature switch. These checks aren't done for other entity types, like leads or Customer Insights - Data profiles.

## Disable contact-level consent checks

Starting February 2024, a new feature switch lets you set the system to consider or bypass contact-level consent checks. You can separate consent by contact point for emails, so each entity has consent captured and enforced by contact point, and the system ignores consent on the contact record for journeys that target contacts.

Disable contact-level consent checks when outbound journeys aren't in use. To disable contact-level consent checks:

1. Go to **Settings** > **Other settings** > **Feature switches**.
1. Set the **Check contact consent for real-time journeys** toggle to **Off**.
1. Select **Save** in the upper-right corner.

The system enforces consent only based on contact point consent records.

## How is consent populated on different unsubscribe experiences

Customer Insights - Journeys offers [different options for providing an unsubscribe experience to your customers](real-time-marketing-compliance-settings.md#compliance-profiles). The system computes the exact consent status for different scenarios and always shows the user visiting the unsubscribe experience an accurate view of consent.

The consent status shown on an unsubscribe experience depends on several factors:

1. Whether the [check contact consent for real-time journeys feature switch](real-time-marketing-email-text-consent.md#disable-contact-level-consent-checks) is on or off.
1. The enforcement model of the purpose.
1. The channel for which consent is shown.
1. The contact point's consent status.

Review these important definitions before you start.

#### Will send, will not send

- **Will send** means the contact point consent record and its purpose enforcement model let the app send an email for that purpose to that address. For example, if the purpose is nonrestrictive and no contact point consent record exists, the app evaluates that as **Will send**.
- **Will not send** means the app evaluates that email address’s contact point consent record and purpose and decides not to send an email.  

#### Will track, will not track  

- Similarly, **Will track** means the tracking contact point consent record and its purpose enforcement model let the app include tracking links in messages sent to that address. For example, if the purpose is nonrestrictive and no contact point consent record exists, the app evaluates that as **Will track**.
- **Will not track** means the app evaluates that email address’s contact point consent record and purpose and decides not to track links in the email.

### Subscription centers used in real-time journeys

> [!IMPORTANT]
> Subscription centers will be removed along with outbound marketing. Consider using a preference center instead.

The **DoNotBulkEmail**, **DoNotEmail**, and **DoNotTrack** fields on a subscription center prefill for the contact based on contact data and contact point consent records for all the contact's email addresses.

1. **DoNotBulkEmail** prefills to block sending if the attribute is currently set to block or if any commercial purpose on the compliance profile from any email address on the contact evaluates to **will not send**.
1. **DoNotEmail** prefills to block sending if the attribute is currently set to block or if any transactional purpose on the compliance profile from any email address on the contact evaluates to **will not send**.
1. **DoNotTrack** prefills to block tracking if the attribute is currently set to block or if the tracking purpose on the compliance profile from any email address on the contact evaluates to **will not track**.  

When a user submits changes through a subscription center, the states of **DoNotBulkEmail**, **DoNotEmail**, and **DoNotTrack** update the contact and the contact point consent records for all the contact's email addresses, as set in the [audience configuration](real-time-marketing-audience-data.md#select-the-audience-source-for-journeys).

1. If both **DoNotBulkEmail** and **DoNotEmail** are set to allow emails, all commercial purposes on the compliance profile for every email address on the contact record have an opted-in contact point consent record. If either is set to don't allow, all contact point consent records update to opted-out.
1. The **DoNotEmail** state is written to all transactional purposes on the compliance profile for every email address on the contact record.
1. The **DoNotTrack** state is written to the tracking purpose on the compliance profile for every email address on the contact record.

### Preference page and preference center  

For journeys **targeting contacts**, each email address consent prefills if it's contactable (**will send**) or traceable (**will track**) based on the specific purpose's enforcement model and its contact point consent record, combined with the contact-level consent fields (only if the [check contact consent](real-time-marketing-email-text-consent.md#disable-contact-level-consent-checks) for real-time journeys feature switch is on).

1. **Commercial purposes/topics** prefill to opt in only if the contact point consent record evaluates to **will send** and both **DoNotBulkEmail** and **DoNotEmail** are set to allow emails.
1. **Transactional purposes/topics** prefill to opt in only if the contact point consent record evaluates to **will send** and **DoNotEmail** is set to allow emails.
1. **Tracking purpose** prefill to opt in only if the contact point consent record evaluates to **will send** and the contact's **DoNotTrack** is set to allow tracking.

For journeys **targeting leads or Customer Insights - Data profiles**, each email address consent prefills if it's contactable (**will send**) or traceable (**will track**) based on the specific purpose's enforcement model and its contact point consent record. The preference page and preference center experiences prefill email address consent to opt in if the contact point consent record for the email evaluates to **will send**.

When a user submits consent changes through a preference page or preference center, the system updates only the relevant contact point consent records. The system doesn't modify any contact-level consent attribute in these cases.  

## View and manage consent records

In the consent center, you see a list of all contact point consents and their related attributes (type, status, source of consent data, and date modified). To see a compact view for a single consent record or change it, select the contact-point name from the list of records.

The contact and lead forms let you quickly see and update a customer's consent, so you can easily manage what types of messages you send to your customers. You find this comprehensive view under the **Communication** tab. It gives you one place to manage consent across every channel and line of business in your organization.

The **Communication** tab lets you:

1. Get a summary view of the consent each contact or lead provides, so you can see if the customer is contactable at a glance.
1. Easily change the consent for the email addresses, phone numbers, and custom channels of a contact or lead directly from the contact or lead forms. This gives you control over the type of messages you send to the customer on each channel. The grid view shows you both the consent record and its evaluated contactability. This helps answer the question: "Why did my journey get blocked because there's no consent?"
1. Drill down into consent for each compliance profile set up in your organization, so you can understand customer consent for each line of business.

You see the consent records for each purpose and topic (if present) of the selected compliance profile here, and you can update them directly. You can also choose a different contact point from the drop-down and select the compliance profile you want to manage consent records for.

When you change a consent record, the contactability column and the communication and tracking status cards update immediately. However, sometimes updates to a consent record don't affect its contactability. For example, if you update the consent status for a topic record to opt in while the parent purpose stays opted out, the contactability of the topic record doesn't change.  

## Audit consent records

Track all consent-related changes for each contact record, including who made the changes and when. The **Audit history** is available under a consent record's **Related** tab.

### See also

[Grow your business with multi-brand, custom preference centers](real-time-marketing-compliance-settings.md)
[Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)
[Outbound marketing compliance settings](privacy-use-features.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
