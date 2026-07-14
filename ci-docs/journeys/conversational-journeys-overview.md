---
title: Conversational journeys overview
description: Learn how conversational journeys in Dynamics 365 Customer Insights combines AI agents and Contact Center to deliver seamless, automated customer interactions.
ms.date: 05/07/2026
ms.topic: article
author: vinayd-msft
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:05/27/2025
---

# Conversational journeys overview

Conversational journeys combines Dynamics 365 Customer Insights - Journeys, Dynamics 365 Contact Center, and AI agents built with Copilot Studio to deliver natural language conversational experiences at scale. Set up proactive outreach for scenarios like a canceled flight or product recall, and automate transactional communications like confirming or scheduling a delivery. Conversational journeys help organizations reduce call volume and support costs, and customers get faster resolutions without chasing down answers.

Conversational journeys support the following channels:

1. **Voice call**: A voice phone call is placed to the recipient. When the call is answered, an AI agent handles the conversation with the recipient.
1. **Text messaging (SMS)**: An initial text message is sent to the recipient. When the recipient responds, an AI agent handles the conversation over the SMS channel.

A typical conversational journeys solution has three parts:

1. **Customer journey**: A customer journey that controls who to contact, when to contact, and how to process choices the customer makes during the conversation.
    - Set up consent management and quiet times in Customer Insights - Journeys to contact customers according to their preferences and regulatory requirements.
1. **AI agent**: An AI agent that converses with customers using natural language.
    - Build this agent in Microsoft Copilot Studio.
1. **Dynamics 365 Contact Center**: Contact Center brings everything together.
    - Set up customer service agent queues and phone numbers, and define behaviors like transferring a call to a human representative if the customer asks or if the AI agent can't handle the request.

You can author the entire conversational journeys solution with no code, including designing the AI agent using natural language. This no-code approach allows nontechnical business users to easily define customer experiences.

To create conversational journeys, you need both products (Customer Insights - Journeys and Contact Center). The apps must be in the same environment (using the same Dataverse instance). Use these links to learn more about different aspects of conversational journeys:

- In Contact Center, create a *proactive engagement*. This proactive engagement connects to an agent (customer service representative, a Copilot Studio agent, or both).
- In Customer Insights - Journeys, enable the integration [feature switch](admin-feature-switches.md#integration-feature-switches).
    - Next, [create a journey](proactive-engagement-how-to.md) that uses the proactive engagement created above using the *Conversational voice* step. This step starts voice calls for contacts that enter the journey.
    - Use conversational voice results and outcomes to branch the journey and implement different retry and other experiences.

For more details on these steps and concepts, review the following articles:

- [Prerequisites for conversational journeys](conversational-journeys-prerequisites.md)
- [Conversational journeys concepts](proactive-engagement-concepts.md)
- [Create conversational journeys](proactive-engagement-how-to.md)

[!INCLUDE[footer-include](./includes/footer-banner.md)]
