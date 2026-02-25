---
title: Check your message for errors and prepare it for delivery
description: Learn how to finalize your email message, check it for errors, go live, and schedule it for delivery using a customer journey in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/18/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Check your message for errors and prepare it for delivery

When you're done designing and previewing your email, you're ready to start sending it. First, you need to check it for errors. Then, once it passes the error check, you must go live to activate it and make it available on the marketing services. Finally, set up a customer journey to establish the target segment, delivery schedule, and follow-up actions.

> [!IMPORTANT]
> To build an approval process in real-time journeys, see [Journey and email approval process in Customer Insights - Journeys](https://community.dynamics.com/blogs/post/?postid=e2f9169d-eef7-ee11-a73d-000d3ae2664e)

<a name="error-check"></a>

## Required elements: How to pass the error check

Before you can go-live with or test-send your message, it must pass a validation check. You can run validation check at any time by selecting **Check content** on the command bar. A validation check is also run automatically each time you select **Ready to send** or **Test Send**.

All messages must include the following:

- A **Subject** entered as static text or a [dynamic expression](dynamic-email-content.md) that resolves to valid text.
- A valid **From email** entered as static text or [dynamic expressions](dynamic-email-content.md) that resolve to a valid email address. The email address domain must be one that is authenticated and registered using DKIM as belonging to your organization. You canmake the message **Ready to send** with a **From email** that uses an unauthenticated domain, but you'll get a warning because this isn't recommended. You can't make the message **Ready to send** with a domain that is authenticated as belonging to another organization (this generates an error). More information: [Authenticate your domains](mkt-settings-authenticate-domains.md)
- An HTML body (your message content).
- A [plain-text version](email-properties.md#text-only) of the message. This version must exist and must also include any other required content (For example, Commercial messages must include unsubscribe link and company address, see below).

If the message is marked as “Commercial purpose” (this setting is found in the Email settings under Compliance section) then it must also include the following additional content:
- An unsubscribe link obtained from the Compliance profile.
- Company address obtained from the Compliance profile.
- Both are automatically included by the Email designer when an email is created but they can be deleted by mistake. If that happens, you can re-insert them by defining a dynamic text and including that dynamic text in the email as explained below:
  - For **Unsubscribe link**, create a dynamic text using Compliance > Preference Center as its data source
  - For **Company address**, create a dynamic text using Compliance > Company address as its data source

If the message is marked as “Transactional purpose”, then unsubscribe link and company address content is NOT required but can be included. The validation check will still look for them and give a warning if they are missing (warnings will not block you from making these messages **ready to send**).

For more details on Compliance Settings, see [Compliance Settings](real-time-marketing-compliance-settings.md)

The following are also confirmed by the check:

- All [dynamic expressions](dynamic-email-content.md) and HTML code must compile and generate valid values.
- All videos and images referenced from the Dynamics 365 Customer Insights - Journeys content libraries must exist.


> [!NOTE]
> Errors that result from problems with your dynamic expressions are described in detail and provide a code sample that should help you locate the problem. However, one message, which shows the text "Dynamic content references a static entity that's missing a record ID", can appear for two different reasons. The first reason is the one implied by the text, which means you included a [reference to a specific record](dynamic-email-content.md#personalization-expressions), but left out the ID of the record you want to show. The second reason (which is only loosely related to the displayed text) is that you are referencing an entity that isn't yet synced with the marketing-insights service and therefore isn't available to the error checker; to fix this, ask your admin to confirm whether the required entity is synced, and to add it if it isn't. More information: [Choose entities to sync with the marketing-insights service](mkt-settings-sync.md) 

<a name="go-live-journey"></a>

## Go live and set up a customer journey to deliver your message

While you prepare a message, it stays in a draft state, which means that it's inactive and can't be sent.The message must first be published before it can be sent.

To publish a message, open it and select **Ready to send** on the command bar. Dynamics 365 Customer Insights - Journeys will run a final validation check, as described in the previous section, and&mdash;if it passes&mdash;publish the message. If errors are returned, read the error messages, address the issues, and try again until the message is successfully published.

Once the message is published, it can be included in journeys (via the Email step) that will deliver it to its audience member (each audience member will get a personalized copy of this email when they reach Email step in the journey).

[!INCLUDE [cc-marketing-email-size](./includes/cc-marketing-email-size.md)]

More information: [Use customer journeys to create automated campaigns](customer-journeys-create-automated-campaigns.md) and [Go live with publishable entities and track their status](go-live.md)

## Gain insights from your email results

Once you start delivering an email message using a customer journey, Dynamics 365 Customer Insights - Journeys will begin to collect information about how recipients interact with that message.  The system provides a wealth of information, including analytics, KPIs, graphs, and more, to help you gain insights from your marketing results. More information: [Analyze results to gain insights from your marketing activities](insights.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
