---
title: Prerequisites for conversational journeys
description: 'Prerequisites for conversational journeys: Discover the required products and steps to use Dynamics 365 Customer Insights - Journeys and Contact Center.'
ms.date: 05/13/2026
ms.topic: article
author: Joni-M
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

# Prerequisites for conversational journeys

To use conversational journeys, you need Dynamics 365 Customer Insights - Journeys and Dynamics 365 Contact Center. If you want to use AI agents, you also need Microsoft Copilot Studio.

## Licensing information

1. [Purchase Dynamics 365 Customer Insights](purchase.md) (**required**)
1. [Buy Dynamics 365 Contact Center](https://www.microsoft.com/dynamics-365/products/contact-center/pricing) (**required**)
1. To purchase the appropriate [Customer Insights - Journeys license](purchase.md), you need to estimate how many "Interacted persons" and "Interactions" you require monthly and yearly.
    - Each contact that has a conversational voice call or text message (SMS) request sent from Customer Insights - Journeys to Contact Center counts as an "Interacted person."
        > [!NOTE]
        > Currently, conversational journeys only support interactions with contacts.
    - Each conversation request sent from Customer Insights - Journeys to Contact Center counts as one interaction.
    - Conversations occur over channels managed by Contact Center, and therefore usage is metered by Contact Center based on call minutes or text message volume. Even though Customer Insights – Journeys can include a text messaging (SMS) channel, conversational text messaging is handled through Contact Center channels, not through the Customer Insights – Journeys SMS channel.

## Get started with Customer Insights - Journeys

To get started with Customer Insights - Journey, see [Get started with Customer Insights - Journeys app setup](get-started.md).

## Get started with Contact Center

To get started with Contact Center, see [Use Copilot Service admin center](/dynamics365/contact-center/administer/cc-admin-center).

## Communication channels

Conversational journeys require communication channels such as voice or text messaging (SMS). You must configure these channels in Contact Center using supported providers.

> [!NOTE]
> Although Customer Insights - Journeys supports a text messaging (SMS) channel, conversational journeys don't use that channel. Instead, they rely on the text messaging (SMS) channel configured in Contact Center.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
