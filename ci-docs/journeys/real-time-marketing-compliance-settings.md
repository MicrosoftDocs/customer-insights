---
title: Manage user compliance settings in Customer Insights - Journeys
description: Learn how to manage user compliance settings in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/05/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Manage user compliance settings in Customer Insights - Journeys

[!INCLUDE[consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

Managing compliance settings is key to ensuring your business processes conform with privacy laws and regulations. This article gives an overview of administrator compliance setup, preference centers, and Customer Insights - Journeys concepts. For information on outbound marketing compliance, visit [Outbound marketing compliance settings](privacy-use-features.md).

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RW137KU]

## Customer Insights - Journeys compliance overview

To configure Customer Insights - Journeys compliance, administrators can go to **Settings** > **Customer engagement** > **Compliance profiles** to define the consent model, the company address, and customize the preference center page for your end users.

### Contact point consent

A contact point is the destination for a message. For example, an email address or phone number is a contact point. Customer Insights - Journeys consent is contact point based, which means consent is stored per destination and per channel. For example, the email `somebody@example.com` has consented to receive commercial communications about upcoming events. Consent in real-time journeys stored in contact point consent records. This is different than outbound marketing's consent model that stored consent on the contact record. With Customer Insights - Journeys's contact point consent, customers have more control over where they want to receive marketing messages from your organization.

Another benefit of contact point consent is that it allows for Customer Insights - Journeys to orchestrate journeys across any entity including contacts, leads, etc.

### Compliance profiles

Compliance profiles are the containers of consent settings. In some instances, customers may want to separate consent for brands or lines-of-business (LOBs) by creating separate compliance profiles for each. Compliance profiles give marketers the ability to create specific consent settings for various LOBs. For instance, if there are headquarters in different regions whose physical address should show for recipients in that region, each compliance profile can have its own address.  

Another reason for having multiple compliance profiles would be to support different compliance requirements across regions. For example, a company that operates in the United States and France may choose to have a separate compliance profile for those two locations. Within the United States version, the commercial purpose could be set to a nonrestrictive enforcement model because the U.S. isn't subject to European regulations. Within the France version, however, they may set the commercial purpose to the restrictive enforcement model to require explicit consent before sending any commercial or promotional materials.

When you create a new compliance profile, you can **Use previously captured consent**. This option is intended to facilitate transitioning from a compliance profile with a preference page to one with a preference center. Doing so ensures that any previously captured consent applies to the new compliance profile.

### Purposes

Data use purpose consent (hereafter called “purpose”) defines the specific reason for which consent is collected. It's often associated with a specific legal basis or reason – for example, consent to be contacted for commercial marketing purposes. A purpose can be one of three types: (1) Commercial Communication, (2) Transactional Communication, and (3) Tracking Consent. When a compliance profile is created three purposes are created by default: a Commercial, Transactional, and Tracking purpose. These purposes can be customized to meet your specific needs. You can also create and add your own purposes to a compliance profile.

Purpose consent also allows customers to create line-of-business (LOB) separation without using Dataverse business units or separate compliance profiles. Each LOB has a preference center configured for each business, and each LOB has a set of purposes associated with it that's specific to each LOB. Each message (for example, email or text message) is tied to a single preference center and an associated purpose.

Each organization may need to define separate purposes for each of their LOBs individually – for example, Contoso Northwest may want to manage consent independently from Contoso East. They would create a Commercial Communication Purpose for each LOB so they could manage opt-in or opt-out of Commercial Communication independently for each LOB.

Purposes can also be shared across compliance profiles. This allows you to put purposes and topics from one compliance profile into another compliance profile's preference center and use them to control message consent. For example, a Contoso Global compliance profile may have a Commercial purpose that is shared with Contoso Northwest and Contoso East. The shared purpose could then be used to allow customers who receive email from of Contoso Northwest to opt in or out of communication from the Contoso Global brand on Contoso Northwest's preference center. Additionally, sharing consent purposes allows you to create compliance profiles that share consent data but have a different preference center design. For example, by sharing all purposes across two different compliance profiles, you could create two different preference centers in two different languages but share consent.

### Topics

Each Purpose can contain topics to add specific communications types to allow customers to refine their communications preferences. For example, Contoso Northwest may want to add topics such as "Newsletters," "Daily Deals," and "Product Announcements" to the commercial purpose to allow their customers to decide which specific topics interest them. When creating a message to send, marketers must choose a purpose and can optionally choose a topic that has been created. Recipients can then choose to opt in or out of the topics that interest them. There's a hierarchical relationship between purpose and topic. A topic can only be associated with a single purpose.

### Consent enforcement

The **Enforcement model** settings on a purposes control how consent is evaluated before an email is sent. Emails sent to a purpose use that purpose's enforcement model to evaluate if the email is or is not sent. There are three enforcement models that can be chosen depending on your regulatory needs:

- **Restrictive**: Emails are sent only to contact points that have opted-in contact point consent records for this purpose (or topic).
- **Non-restrictive**: Emails are sent to all contact points unless they have an opted-out contact point consent record for this purpose (or topic).
- **Disabled**: Emails are sent to all contact points. Contact point consent records are not checked before sending messages to this purpose (or topic).

> [!NOTE]
> Currently, the **Enforcement model** setting only applies to email messages. All SMS and custom messages are subject to the restrictive enforcement model, even if their designated purpose has a non-restrictive or disabled enforcement model set. 

Topics use the enforcement model of their parent purpose. Emails that are configured with both a purpose and a topic must have consent for both the purpose and the topic in order for the message to be sent. If a contact point doesn't have consent to send to a purpose, no messages to that purpose's topic will be delivered to the contact point. For example, if the parent purpose has a restrictive enforcement model, sending an email to a topic requires an opt-in contact point consent record for both the purpose and the topic associated with the email.

#### Considerations for contact entities
> [!NOTE]
> If you are using Customer Insights - Journeys without the outbound marketing module installed, the additional checks described in this section are not performed.

Real-time journeys make additional consent enforcement checks for emails sent to contact entities when outbound marketing is provisioned.

In order to aid in the transition from outbound marketing real-time journeys check the consent stored on contact entities in addition to the purpose and topic based consent checks. Real-time journeys look at the contact's `DoNotEmail`, `DoNotBulkEmail` and `DoNotTrack` fields when an email message is sent to a contact entity.

In outbound journeys the contact entity `DoNotEmail` and `DoNotBulkEmail` control if an email is sent. Real-time journeys also check these two fields to match outbound's consent enforcement behavior. For an email to be sent to a contact from a real-time journey, both the contact's fields and the contact point consent records for the email address must all allow the message to be sent.

Similarly, the contact's `DoNotTrack` field and tracking contact point consent records must both allow tracking in order for tracking links and pixels to be inserted into a message. These three fields are not checked for messages sent to other entities (for example, leads).

Text and custom channel messages to contacts do not use the `DoNotEmail`, `DoNotBulkEmail` or `DoNotTrack` fields when evaluating consent.

To learn more about transitioning from outbound marketing to real-time journeys here, visit [Move from outbound to Customer Insights - Journeys](real-time-marketing-move.md)




> [!IMPORTANT]
> Is the above right??? Check the link after rebase/merge with main.
#3 - Describe updates to CPC records from Subscription Centers.

### Preference centers

A preference center is a form that allows a message recipient to review and update their current consent settings. Each compliance profile has its own preference center. When you create a new compliance profile a default preference center is created that you can customize with your own branding. You can choose which purposes and topics appear on the preference center, allowing you to control what consent to show and collect on the form. The unsubscribe links in emails direct recipients to the preference center of the compliance profile chosen on the email they received.

To learn more about preference centers, visit [Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)

> [!NOTE]
> Currently, you can deactivate a compliance profile or contact point consent record. However, deactivated profiles and contact point consent records will still be used and enforced because existing journeys or messages sent may rely on them. Should you wish to update a user's consent, go to the contact point consent record itself and change the consent value.

### See also

[Manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md)
[Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)
[Outbound marketing compliance settings](privacy-use-features.md)

[!INCLUDE[footer-include](./includes/footer-banner.md)]
