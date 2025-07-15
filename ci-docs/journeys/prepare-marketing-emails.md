---
title: Email marketing overview
description: Get an overview for how to create and send marketing email messages in Dynamics 365 Customer Insights - Journeys.
ms.date: 07/14/2025
ms.topic: overview
author: alfergus
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Email marketing overview

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=640e5cfb-a60b-4982-9aa1-66da88d7a50a]

The process for creating marketing emails in Dynamics 365 Customer Insights - Journeys begins with understanding what makes them such a powerful tool for your marketing campaigns. After you create a good design aimed at a specific segment of your audience, you preview it and check for errors before going live. You can fine-tune the reach and effectiveness of your message through advanced operations like merging database values, adding dynamic content, and introduce programming logic.

## How marketing email works in Customer Insights - Journeys

Marketing email works differently from person-to-person messaging. Here are some key differences:

- **Marketing email messages target entire market segments, but each message is individual**  
    Marketing email messages aren't just standard messages with large "To" or "BCC" fields. Long recipient lists are hard to manage and analyze. Messages with long recipient lists often get caught by spam filters and aren't delivered. In Customer Insights - Journeys, you send a single marketing email design to a segment, but each message is personalized for each recipient. These messages are delivered one at a time from your organization to each recipient.
- **Mail-merge features enable personalized and dynamic content**  
    Design messages to include information personalized for each recipient. For example, each message might include the recipient's name or other content that changes based on gender, location, preferred-customer status, or other contact data. Personalization can improve open and response rates.
- **Marketing email messages are hosted by the marketing services, so you must "go live" rather than just send messages.**  
    Live messages are hosted by a marketing service linked to your Customer Insights - Journeys instance. They're ready to be personalized and sent to individual recipients as needed. A live marketing email message acts as a master document on your server and includes logic to generate and send individual messages when triggered by a customer journey.
- **Required content and automated error-checking help improve deliverability and ensure compliance**  
    When you go live with a message, the system checks for common technical errors and required content. Required content helps maintain your organization's email reputation and meets most email-marketing regulations (like CAN-SPAM in the United States). Required features include a subscription center link (so contacts can manage their email subscriptions), your organization's physical address, a message subject, and a valid return address.
- **Set up a customer journey to deliver messages to a target segment**  
    When your email message is live, it's ready for use in a *customer journey*. The customer journey sets a target segment (a selected list of contacts) and includes logic for that segment. For example, the journey might target contacts in New York City and start by sending an event announcement. The journey then uses a trigger to separate contacts who sign up from those who don't. Contacts who sign up get an automatic thank-you email, while those who don't sign up within a week get a reminder. This journey needs three live email messages (invite, thank you, and reminder) before you start.
- **You can use a single marketing email message in several marketing contexts**  
    Each marketing email message can adapt to different marketing contexts defined by the content settings in each customer journey. Examples include supporting page links (like subscription center and forward pages), your postal address, social media links, and more. This feature lets you use a single live email message in several customer journeys or campaigns.
- **View and analyze message results**  
    Customer Insights - Journeys tracks what happens to each marketing message and records when a contact opens, clicks, or forwards it. The system tracks opens by including a unique [web beacon](https://en.wikipedia.org/wiki/Web_beacon) in each message (recipients must load images for this to work). For each link in your message, Customer Insights - Journeys creates a unique redirect link for each recipient. All clicks go through Customer Insights - Journeys, which logs the message and contact IDs and forwards the contact to the correct URL. Review results and analytics by customer journey, email message, email template, and more. More information: [Analyze results to gain insights from your marketing activities](insights.md).
- **You should provide a forwarding form rather than allow contacts to forward messages directly from their email client**  
    Customer Insights - Journeys provides a forward-to-a-friend feature for sharing messages. The system tracks when contacts use this form to forward messages. It doesn't track messages forwarded with a standard email client. Messages forwarded with an email client still have the web beacon and personalized links of the original recipient, so your email results show all interactions as being done by the original recipient. When a contact uses the forward-to-a-friend form, Customer Insights - Journeys generates a new web beacon and personalized redirect links for each forwarded message.

## Process overview: How to create and go live with a marketing email

Below is an overview of the general process for creating and sending a marketing email. Complete details are provided later in related topics.

1. Go to **Customer Insights - Journeys** > **Channels** > **Emails** to open the marketing email list view.

1. Select **New** to [create a new message](email-design.md).

1. Choose a template to set the basic format of your message.

1. Design your message using the [drag-and-drop designer or HTML editor](real-time-marketing-email.md).

1. Add a compelling **Subject** to your message.

1. [Preview](email-preview.md) your message by using the **Preview** tab and by sending [test messages](email-preview.md).

1. Save your work as often as you want. The message stays in draft status until you go live with it.

1. Run an [error check](email-check-golive.md) on your message. This step checks that you've included all required elements and haven't added any invalid code. If there are errors, you see messages with advice on how to fix them. Fix the errors as suggested, and keep rechecking until the message passes.

1. Select **[Go Live](email-check-golive.md)**. The system runs a final error check automatically, so you can't go live unless your message passes.

1. The message is now live and ready on your server, but it isn't addressed or sent yet. To send it, add it to a [customer journey](customer-journeys-create-automated-campaigns.md).

1. Check your email results to [gain insights](insights.md) about how contacts interact with your messages.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
