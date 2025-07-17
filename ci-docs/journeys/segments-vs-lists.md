---
title: The differences between segments and lists
description: Learn how marketing segments are different from marketing lists, and when to use each of them in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/23/2023
ms.update-cycle: 1095-days
ms.topic: concept-article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing, evergreen
---

# Marketing segments vs. marketing lists

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

Even without Dynamics 365 Customer Insights - Journeys installed, some Dynamics 365 apps provide a few basic marketing features, which include the ability to create both static and dynamic _marketing lists_ that you can use with the _quick campaigns_ feature also included with these apps. However, Customer Insights - Journeys predominantly uses a separate feature called _marketing segments_ to target its full-featured _customer journeys_, both of which are unique to Customer Insights - Journeys.

The following table summarizes a few important differences between the various types of marketing lists and segments.

| **Supported Operation** | **Static segment** | **Dynamic segment** | **Static marketing list** | **Dynamic marketing list** |
| --- | --- | --- | --- | --- |
| Use in customer journey | Yes | Yes | Subscription list only | No |
| Use in campaign / quick campaign | No | No | Yes | Yes |
| Include in a segment | Yes (compound segment) | Yes (compound segment) | Yes | No |
| Show on subscription center | No | No | Subscription list only | No |
| Query interaction records from the marketing-insights service | No | Yes | No | No |
| Go live to activate | Yes | Yes | No | No |
| Runs on the marketing-insights services | Yes | Yes | No | No |
| Add/remove a contact while viewing the contact record | Yes | No | Yes | No |
| Resulting entities | Contacts only | Contacts only | Contacts, leads, or accounts | Contacts, leads, or accounts |

## Key differences between how lists and segments are made

To create a segment, you must work directly in Customer Insights - Journeys. Marketing lists can be created using any of several different Dynamics 365 apps and add-ons.

Unlike marketing lists, marketing segments run on the marketing-insights service, which is designed to crunch large amounts of data without impacting the performance of your Dynamics 365 user interface and other functions.

You design your segments using Customer Insights - Journeys and then _go live_ with each segment to activate it. Marketing emails, customer journeys, lead-scoring models, and many other Customer Insights - Journeys features have a similar life cycle.

As you run your customer journeys, events, and more using Customer Insights - Journeys, the marketing-insights services collect huge amounts of information about how each contact interacts with your marketing initiatives. Marketing segments run directly on the marketing-insights services and therefore have access to this data so you can create a segment that, for example, finds all contacts who registered for a specific event, or opened a specific email, or visited a specific website; this information isn't available to marketing lists.

You can mix several segments and combine them with various logical operators (union, include, or exclude) to create compound segments. In this way, you can mix several simple segments to create advanced selection logic.

## How to use marketing segments with Customer Insights - Journeys

The primary role of marketing segments is to create collections of related contacts that you can target using a customer journey. You can use a dynamic segment, static segment, or subscription list to target a customer journey, but you can't use a dynamic marketing list, so the only way to target a customer journey based on a dynamic database query is to create a dynamic segment.

## How to use marketing lists with Customer Insights - Journeys

Customer Insights - Journeys makes use of static marketing lists to create _subscription lists_, which enable contacts to sign up for your various mailing lists. Subscription lists are a special type of static marketing list that can only contain contacts. Unlike most marketing lists, you can also use subscription lists to target a customer journey directly.

Another way to make use of a static marketing list in Customer Insights - Journeys is to set up a dynamic segment that queries that list. This technique is limited to static marketing lists—dynamic lists aren't supported. For contact-based static lists, you can set up a segment that queries the list and then traverses to find the list members. For static marketing lists that contain accounts or leads, your segment must select, for example, the parent contact for each lead or the primary contact for each account. For dynamic lists, you must recreate the original logic as a segmentation query because you can't query them directly like you can a static list.

## Key differences between how lists and segments are evaluated

_Evaluation_ is the process of calculating the members of a segment or list based on its membership criteria. Segments and lists evaluate their memberships quite differently.

- **Dynamic segments based on profiles and relationships** are first evaluated once they go live. The calculation occurs asynchronously, and the results of the initial query are available soon after the go-live process is complete. While you're working with a segment in Customer Insights - Journeys, you may need to refresh the page a minute or so after going live to view its members. While live, each segment is reevaluated once every hour or so to refresh its member list.
- **Dynamic segments based on interactions** are also first evaluated once they go live. While live, each behavioral segment is flagged when a new, relevant interaction arrives. Each flagged segment is then reevaluated as soon as the marketing-insights services have calculation capacity available.
- **Static segments** are populated manually and then submitted to the marketing-insights services when they go live. Static segments are reevaluated each time a user changes them in Customer Insights - Journeys.
- **Dynamic marketing lists** are evaluated on demand, such as when a user requests to see them, or when a campaign activity or quick campaign is distributing activities for the member audience.
- **Static Marketing Lists** return their lists of members on demand, such as when a user requests to see them, or when a campaign activity or quick campaign is distributing activities for the member audience.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
