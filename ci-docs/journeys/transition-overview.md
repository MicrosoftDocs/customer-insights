---
title: Transition overview
description: Overview of the transition process from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/07/2023
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
| I evaluated the real-time journeys module and determined that I can't use it    | Review the [transition functional areas](transition-walkthrough-functional.md) guide and the other [transition resources](transition-resources.md). After review, if you still have concerns that prevent you from using real-time journeys, follow the guidance for [requesting outbound marketing to be added](transition-overview.md#requesting-an-exception-for-enabling-outbound-marketing) |

## Guidance for existing customers

Existing customers are encouraged to transition from outbound marketing to the real-time journeys engine for optimal performance, scale, and to take advantage of ongoing product investments and AI Copilot features. Learn more: [Customer Insights - Journeys transition FAQs](transition-faqs.md)

> [!NOTE]
> Existing customers who complete new installations can add outbound features through a self-serve interface. To add outbound marketing features, go to **Settings** > **Versions** and select the **Enable** link.

Here's some recommendation actions for existing customers depending on your needs:

| Situation                                                                                                          | Action                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New org**: I provisioned a new org and don't see outbound marketing                                             | This is expected; outbound marketing is no longer included in new orgs. We strongly recommend using real-time journeys. See [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys) |
| **New org**: I'm unable to transition to real-time journeys                                                        | Review the [transition functional areas](transition-walkthrough-functional.md) guide and the other [transition resources](transition-resources.md). We strongly recommend using real-time journeys. After review, if you still have concerns that prevent you from using real-time journeys, you can add outbound marketing back using the **Enable** link available on the **Settings** > **Versions** page. If you don't see the link, follow the guidance for [requesting outbound marketing to be added](transition-overview.md#requesting-an-exception-for-enabling-outbound-marketing)                                                                                                                                                                                                                                                           |
| **Existing org**: I updated an existing org that had outbound marketing, but after the update I don't see outbound | Do you need outbound marketing? Review the [transition functional areas](transition-walkthrough-functional.md) guide and the other [transition resources](transition-resources.md). We strongly recommend using real-time journeys. After review, if you still want to enable outbound marketing, use the **Enable** link available on the **Settings** > **Versions** page. If you don't see the link, follow the guidance for [requesting outbound marketing to be added](transition-overview.md#requesting-an-exception-for-enabling-outbound-marketing)                                                                                                                                                                                                                                                           |
## Requesting an exception for enabling outbound marketing

If you have valid business reasons that require outbound marketing to be enabled in your environment, you can request an exception by filling out [the outbound marketing request form](https://go.microsoft.com/fwlink/?linkid=2251742).

Note the following parameters:
- Don't create support tickets or use other channels for the same requests, you'll be redirected to this form.
- This form requires an email address. The email address is used to communicate receipt of the request, confirming when the request has been processed, and if needed, ask for additional information.
- Most requests are processed in about three business days once all needed information is available.

[!INCLUDE [footer-include](./includes/footer-banner.md)]