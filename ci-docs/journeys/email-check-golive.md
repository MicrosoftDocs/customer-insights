---
title: Check your message for errors and prepare it for delivery
description: Learn how to finalize your email message, check it for errors, go live, and schedule it for delivery using a customer journey in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/25/2026
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Check your message for errors and prepare it for delivery

When you're done designing and previewing your email, you're ready to start sending it. First, you need to check it for errors. Once it passes the error check, you must activate it (go live) and make it available on the marketing services. Last, set up a customer journey to establish the target segment, delivery schedule, and follow-up actions.

> [!IMPORTANT]
> To build an approval process in real-time journeys, see [Journey and email approval process in Customer Insights - Journeys](https://community.dynamics.com/blogs/post/?postid=e2f9169d-eef7-ee11-a73d-000d3ae2664e).

<a name="error-check"></a>

## Required elements: How to pass the error check

Before you can go live with or test-send your message, it must pass a validation check. You can run validation check at any time by selecting **Check content** on the command bar. A validation check is also run automatically each time you select **Ready to send** or **Test send**.

All messages must include the following:

- A **Subject** entered as static text or a [dynamic expression](dynamic-email-content.md) that resolves to valid text.
- A valid **From email** entered as static text or [dynamic expressions](dynamic-email-content.md) that resolve to a valid email address. The email address domain must be one that is authenticated and registered using DKIM as belonging to your organization. You can make the message **Ready to send** with a **From email** that uses an unauthenticated domain, but you get a warning because this isn't recommended. You can't make the message **Ready to send** with a domain that is authenticated as belonging to another organization (this generates an error). For more information, see [Authenticate your domains](mkt-settings-authenticate-domains.md).
- An HTML body (your message content).
- A [plain-text version](email-properties.md#text-only) of the message. This version must exist and include any other required content. For example, commercial messages must include an unsubscribe link and company address.

If the message is marked as *Commercial purpose*, then it must also include the following additional content:
- An *Unsubscribe link* obtained from the Compliance profile.
- A *Company address* obtained from the Compliance profile.
- Both the *unsubscribe link* and *company address* are automatically included by the Email designer when an email is created. However, they can get deleted by mistake. If this happens, you can reinsert them by defining a dynamic text and including that dynamic text in the email. In this situation, perform the following instructions:
  - For the *Unsubscribe link*, create a dynamic text using **Compliance** > **Preference Center** as its data source.
  - For *Company address*, create a dynamic text using **Compliance** > **Company address** as its data source.

If the message is marked as *Transactional purpose*, then the *Unsubscribe link* and *Company address* content are not required but can be included. The validation check still looks for them and provides a warning if missing. Warnings don't block you from making these messages **Ready to send**.

For more information on compliance settings, see [Stay compliant with privacy regulations](real-time-marketing-compliance-settings.md).

The following steps also occur in the validation check:

- All [dynamic expressions](dynamic-email-content.md) and HTML code must compile and generate valid values.
- All videos and images referenced from the Dynamics 365 Customer Insights - Journeys content libraries must exist.

> [!NOTE]
> Errors that result from problems with your dynamic expressions are described in detail. A code sample is also provided that should help you locate the problem. However, the message; "Dynamic content references a static entity that's missing a record ID" can appear for two different reasons. First, it can appear because you included a [reference to a specific record](dynamic-email-content.md#personalization-expressions) but left out the ID of the record you want to show. Second, it can appear because you're referencing an entity that isn't synced with the marketing-insights service, and therefore isn't available to the error checker. To resolve this, ask your admin to confirm whether the required entity is synced and add the entity if not. For more information, see [Choose entities to sync with the marketing-insights service](mkt-settings-sync.md).

<a name="go-live-journey"></a>

## Go live and set up a customer journey to deliver your message

While you prepare a message, it stays in a draft state. This means that it's inactive and can't be sent. The message must first be published before it can be sent.

To publish a message, open it and select **Ready to send** on the command bar. Dynamics 365 Customer Insights - Journeys runs a final validation check, as described in [How to pass the error check](#required-elements-how-to-pass-the-error-check). If the validation check passes, you can publish the message. If errors occur, read the error messages, address the issues, and try again until the message is successfully published.

Once the message is published, it can be included in journeys (via the Email step) that delivers it to its audience member. Each audience member gets a personalized copy of this email when they reach Email step in the journey.

[!INCLUDE [cc-marketing-email-size](./includes/cc-marketing-email-size.md)]

For more information, see [Use customer journeys to create automated campaigns](customer-journeys-create-automated-campaigns.md) and [Go live with publishable entities and track their status](go-live.md).

## Gain insights from your email results

Once you start delivering an email message using a customer journey, Dynamics 365 Customer Insights - Journeys begins to collect information about how recipients interact with that message. The system provides a wealth of information, including analytics, KPIs, graphs, and more, to help you gain insights from your marketing results. For more information, see [Analyze results to gain insights from your marketing activities](insights.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
