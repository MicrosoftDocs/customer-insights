---
title: Conversational journeys overview
description: Learn how conversational journeys in Dynamics 365 Customer Insights combines AI agents and Contact Center to deliver seamless, automated customer interactions.
ms.date: 05/29/2025
ms.topic: article
author: vinayd-msft
ms.author: colinbirkett
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

Conversational journeys combines Dynamics 365 Customer Insights - Journeys, Dynamics 365 Contact Center, and AI agents built with Copilot Studio to deliver customer experiences at scale. Set up proactive outreach for scenarios like a canceled flight or product recall, and automate transactional calls like confirming or scheduling a delivery. Conversational journeys help organizations reduce call volume and support costs, and customers get faster resolutions without chasing down answers.

A typical conversational journeys solution has three parts:

1. A customer journey tells the AI agent who to call, when to call, and how to process choices the customer makes during the call. Set up consent management and quiet times in Customer Insights - Journeys to contact customers according to their preferences and regulatory requirements.
1. The AI agent converses with customers using natural language. Build this agent in Microsoft Copilot Studio.
1. Contact Center brings everything together. Set up customer service agent queues and phone numbers, and define behaviors like transferring a call to a human representative if the customer asks or if the AI agent can't handle the request.

You can author the entire conversational journeys solution with no code, including designing the AI agent using natural language. This no code approach allows nontechnical business users to easily define customer experiences.

In order to create conversational journeys, you will need to have both products (Journeys and Contact Center). They must be in the same environment (using the same Dataverse instance). Then, 
Use these links to learn more about different aspects of conversational journeys:
- In Contact Center, you’ll need to create a *proactive engagement*. This proactive engagement will connect to an agent (customer service representrative or a Copilot Studio Agent, or both)
- In Customer Insights - Journeys, you will need to enable the integration via [feature switch](https://learn.microsoft.com/dynamics365/customer-insights/journeys/admin-feature-switches#integrations). Then
  - [Create a journey](https://learn.microsoft.com/dynamics365/customer-insights/journeys/proactive-engagement-how-to) that uses the proactive engagement created above via *Conversational voice* step. This step initiates  voice calls for Contacts that enter the journey.
  - Conversational voice results and outcomes can be used to branch in the journey to implement different retry and other experiences.

For more details on these steps and concepts involved, please review the following:
- [Prerequisites for conversational journeys](conversational-journeys-prerequisites.md)
- [Conversational journeys concepts](proactive-engagement-concepts.md)
- [Create conversational journeys](proactive-engagement-how-to.md)

[!INCLUDE[footer-include](./includes/footer-banner.md)]
