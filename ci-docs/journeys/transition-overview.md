---
title: Transition overview
description: Overview of the transition process from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/12/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition overview

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

In July 2023, Microsoft announced significant changes to the former Dynamics 365 Marketing application. The following changes were released to market in September 2023: 
-	The Dynamics 365 Marketing application was renamed to Customer Insights - Journeys.
-	The former Customer Insights application was renamed to Customer Insights - Data.
-	Both applications are now sold together under a single product SKU called Customer Insights.

The real-time journeys module covers most of the functionalities of the outbound module while exceeding its capabilities in many areas. To mitigate uncertainty and confusion, the articles in the "Transition from outbound marketing" section of the documentation walk through how to successfully transition to the real-time journeys module and answer frequently asked questions about this topic.

The following diagram shows how the changes affect new and existing customers:

> [!div class="mx-imgBorder"]
> ![Customer Insights - Journeys transition comparison.](media/real-time-marketing-transition-graphic.png "Customer Insights - Journeys transition comparison")

## Guidance for trials

New trials can only be created with real-time journeys.

## Guidance for new customers

New customers who install Customer Insights - Journeys no longer see the outbound marketing module and can't install it. Because outbound marketing doesn't offer the performance, scale, user experience, and AI copilot capabilities of Customer Insights - Journeys and is no longer being invested in from an engineering perspective, we strongly encourage customers to not adopt outbound marketing.

Here are some recommendations depending on your situation:

| Situation                                                                        | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I purchased before September 1, 2023 and planned to implement outbound marketing | We strongly recommend using real-time journeys. See [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys)                                                                                                                                                                                                                                                                                                     |
| I evaluated the real-time journeys module and determined that I can't use it    | Review the [transition functional areas](transition-walkthrough-functional.md) guide and the other [transition resources](transition-resources.md). After review, if you still have concerns that prevent you from using real-time journeys, create a support ticket with the required details as described in [Creating a support ticket requesting outbound marketing](transition-overview.md#create-a-support-ticket-requesting-outbound-marketing) |

## Guidance for existing customers

Existing customers are encouraged to transition from outbound marketing to the real-time journeys engine for optimal performance, scale, and to take advantage of ongoing product investments and AI Copilot features. Learn more: [Customer Insights - Journeys transition FAQs](transition-faqs.md)

> [!NOTE]
> Existing customers who complete new installations can add outbound features through a self-serve interface. To add outbound marketing features, go to **Settings** > **Versions** and select the **Enable** link.

Here's some recommendation actions for existing customers depending on your needs:

| Situation                                                                                                          | Action                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New org**: I provisioned a new org and don't see outbound marketing                                             | This is expected; outbound marketing is no longer included in new orgs. We strongly recommend using real-time journeys. See [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys) |
| **New org**: I'm unable to transition to real-time journeys                                                        | Review the [transition functional areas](transition-walkthrough-functional.md) guide and the other [transition resources](transition-resources.md). We strongly recommend using real-time journeys. After review, if you still have concerns that prevent you from using real-time journeys, you can add outbound marketing back using the **Enable** link available on the **Settings** > **Versions** page. If you don't see the link, create a support ticket with the required details as described in [Creating a support ticket requesting outbound marketing](transition-overview.md#create-a-support-ticket-requesting-outbound-marketing)                                                                                                                                                                                                                                                           |
| **Existing org**: I updated an existing org that had outbound marketing, but after the update I don't see outbound | Do you need outbound marketing? Review the [transition functional areas](transition-walkthrough-functional.md) guide and the other [transition resources](transition-resources.md). We strongly recommend using real-time journeys. After review, if you still want to enable outbound marketing, use the **Enable** link available on the **Settings** > **Versions** page. If you don't see the link, create a support ticket with the required details as described in [Creating a support ticket requesting outbound marketing](transition-overview.md#create-a-support-ticket-requesting-outbound-marketing)                                                                                                                                                                                                                                                           |
## Create a support ticket requesting outbound marketing

Do you see the **Enable** link on the **Settings** > **Versions** page? If yes, don't create a ticket. Use that link to provision outbound marketing.

If you create a support ticket, you must include the following information:

- What is the TenantID? (TenantID)
-	What is the OrgID of the org that needs outbound marketing? (OrgID)
-	Is this a new org or an existing org that was updated? (New or existing)
-	Is this org a “solutions only” org? (Yes or no)
-	Is this the only org in this tenant? (Yes or no)
    -	If no, include the OrgIDs of other orgs. (OrgIDs)
-	Why do you need outbound marketing? Select the reason(s) from the list below and include the requested details.
    1. There are features in outbound marketing that I can’t live without. (Include a list of the features)
    1. I'm not ready to transition to real-time journeys yet, I plan to transition later. (Include the planned timeline)
    1. I have customization that I can't move to real-time journeys. (Include details)
    1. I've tried tje real-time journeys module and had issues with it. (Include details)
    1. Other reasons. (Include details)

[!INCLUDE [footer-include](./includes/footer-banner.md)]