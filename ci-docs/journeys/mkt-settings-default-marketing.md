---
title: Configure default settings in outbound marketing
description: Set up collections of settings that establish various defaults used throughout the app, including for email marketing, customer journey timezone, double opt-in, and email deduplication during sending in outbound marketing.
ms.date: 08/21/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Configure default settings in outbound marketing

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Use the **Settings** > **Email marketing** > **Default settings** page to set up collections of settings that establish various defaults used throughout the app. You can store as many settings sets as you want, but only the one marked as **Default** is active.

Choose an existing configuration to edit or delete it or choose **+ New** from the command bar to create a new one.

## The General tab

Make the following settings here:

- **Name**: The name of the default-settings set, as shown on the list page.
- **Owner**: The user that owns the set.
- **Default**: Set to **Yes** to activate the current default-settings set on your instance.

## The Marketing email tab

Use the **Marketing email** tab to set defaults that apply to your marketing email messages. You'll always be able to override these defaults for individual messages, but it will be more convenient for users if you set the defaults to their most-used values. You can also enable or disable Litmus integration here for all users. The following settings are available:

- **Default content settings**: Choose a default content-settings record to provide dynamic values for test sends and the preview feature of the marketing email designer. Users will be able to override this default by choosing another contact while previewing or test sending a specific message if needed. More information: [Use content settings to set up repositories of standard and required values for email messages](dynamic-email-content.md#content-settings)
- **Default sending domain**: Choose an authenticated domain to use as the sending domain in the email from-address in cases where the initial from-address uses a domain that is not yet authenticated for DKIM. This will help ensure that users don't accidentally send an email using an unauthenticated domain (which would negatively affect deliverability). More information: [Authenticate your domains](mkt-settings-authenticate-domains.md) and [Set sender and receiver options](email-properties.md#send-receive-options)
- **Default contact**: Choose a default contact record to provide dynamic values for test sends and the preview feature of the marketing email designer. Users will be able to override this default by choosing another contact while previewing or test sending a specific message if needed.
- **Enable Litmus integration**: Set this to **Yes** to enable the  [inbox preview feature](email-preview.md#inbox-preview), which provides pixel-perfect renderings of how your email messages will look on specific client and platform combinations. The feature is provided by a Microsoft partner called Litmus Software, Inc. ([litmus.com](https://litmus.com/)), and is optional.
- **Default from email**: Use this setting to define the default "From" address when you create a new email.
- **Default from name**: Choose a default sender name for new emails.

More information: [Check your work using previews and test sends](email-preview.md)

## The Customer journey tab

Use the **Customer journey** tab to choose the default time zone that you will use when starting and stopping your customer journeys.

## The Global level double opt-in tab

Use the **Global level double opt-in** tab to set up the double opt-in feature. For complete details about this feature, including how to use the settings provided here, see [Set up double opt-in for new subscriptions and consent changes](double-opt-in.md).

## The Bypass email deduplication tab

> [!IMPORTANT]
> Deduplication settings only apply to outbound marketing email functionality, not Customer Insights - Journeys. Customer Insights - Journeys, by design, allows you to send multiple emails to the same email address.

By default, Dynamics 365 Customer Insights - Journeys deduplicates outgoing outbound marketing email messages to ensure that each message is sent just once to each unique email address. Duplication detection is accomplished by storing a key value that includes a contact's email address, coupled with information about the customer journey and the email tile. This means that if more than one contact record in the target segment has the same email address, only one of those contacts will receive the message.

Duplicate email addresses usually indicates that the same person is represented by two different records in your database (for example, because they registered at different times using two different first-name variants, such as "Bob" and "Robert"), so this is the desired behavior. However, some organizations need to send separate copies of the same email messages to multiple contacts that happen to use the same email address. In this case, personalized content, such as account details, would probably be different for each recipient. If your organization requires this, set **Bypass email deduplication** to **Yes**. Set it to **No** to revert to the standard deduplication behavior.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
