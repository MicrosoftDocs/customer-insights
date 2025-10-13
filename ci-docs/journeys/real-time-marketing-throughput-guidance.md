---
title: Throughput guidance
description: Learn about throughput based on your monthly interactions quota in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/04/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Throughput guidance

In Dynamics 365 Customer Insights - Journeys, the [Service limits and fair use policy](fair-use-policy.md) article provides guidance on the scale that the service can support. The interaction limits in the article provide a maximum number of monthly interactions supported by the service today.

Your maximum number of interactions per month may differ from the service limit. Your interactions are governed by the total number of contact packs you purchase. Details on purchasing of contacts packs can be found on the [pricing page](https://dynamics.microsoft.com/marketing/pricing/). Contact license pack purchases determine the maximum number of Marketing contact records and monthly outbound interactions that you can send in a month (Learn more: [Quota limits](quota-management.md)). If your service needs are beyond the maximum capabilities of the service, contact your sales team and we can work with you to meet your needs.

## What is throughput?

The license purchased also determines the number of resources that are dedicated to you, which in turn determines your throughput. Throughput is defined as the total number of interactions that you can send per unit of time (second/minute/hour).

The following tables provide directional guidance on the throughput you should expect based on the number of monthly interactions quota while your consumption is within that monthly quota. You can increase your monthly interaction quota by upgrading your license with additional contact packs or interaction packs.

Expected throughput in standalone Dynamics 365 Marketing (old SKU):

| Monthly contact quota     | Throughput (interactions/hr) |
|---------------------------|------------------------------|
| Up to 10,000,000 contacts | 140,000                      |
| 10,000,000+ contacts      | 500,000*                     |

**Available in preview. Contact your Microsoft representative if you have or are going to purchase a quota of more than 10,000,000 contacts.*

Expected throughput in Dynamics 365 Customer Insights (new SKU):

| Interacted people quota         | Throughput (interactions/hr) |
|---------------------------------|------------------------------|
| Up to 500,000 interacted people | 140,000                      |
| 500,000+ interacted people      | 500,000*                     |

> [!NOTE]
> The above throughput guidance varies depending on a few factors such as the complexity of your journey, the number of concurrent journeys that you run, the consumption patterns from other applications that you use, and the resource intensive workloads that are being carried out.

## Throughput examples

Let’s look at a throughput example: On January 1, Contoso (a coffee maker) purchases 3,000,000 marketing contacts and 30,000,000 monthly interactions quota. This gives them a throughput of 140,000 interactions/hr. On January 5, they send an email newsletter to a segment of 280,000 customers. Because the maximum throughput for their interaction quota is 140,000 interactions/hr, the newsletter takes about 2 hours to send.

On January 10, they run two separate customer journeys targeting 280,000 customers each; one starting 8:00 AM and the other at 9:00 AM. Because they’re able to send 140,000 messages per hour, only half the customers in the first journey receive emails by 9:00 AM. Between 9:00 AM and 11:00 AM, both journeys start sending emails simultaneously, so each is only able to send roughly 70,000 messages per hour (the total throughput gets divided between the two journeys). By 11:00 AM, the first journey has completed and the second journey has 140,000 customers left to email. The second journey can now be completed by around 12:00 PM.

## Frequently asked questions

### What are the differences between "service limits," "monthly interactions for a customer," and "throughput"?

**Service Limits**: This is the absolute high-end limit on what Customer Insights - Journeys can support. This defines the limits of the product today. Any requirement that you have above these limits would require additional work from our end to enable you.

**Monthly interactions for a customer**: This is the total number of monthly interactions that you can purchase by buying contacts packs through the pricing page on the website. This may not be the same as the service limits for Customer Insights - Journeys.

Let’s think about this with an example: Contoso (a coffee maker) purchases 1,000,000 marketing contacts. This entitles them to 10,000,000 monthly interactions. While the product supports 100,000,000 contacts and 300,000,000 interactions, their purchase limits them to the 10,000,000 interaction quota. However, they can buy additional quantities of contacts and interactions to increase their quota. They can keep doing so until they hit the service limit. At this point, their purchase entitles them to the service limit of the product. Any further purchases won’t give them additional contacts or interactions.

**Throughput**: As mentioned above, this is defined as the total number of interactions that you can send per unit of time (second/minute/hour). The throughput is determined by your monthly contact quota.

Let’s think about this with an example: Contoso has 1,000,000 contacts, which, in standalone Dynamics 365 Marketing (outbound marketing), entitles them to a monthly interaction quota of 10,000,000 interactions and a throughput of 140,000 interactions/hr (as per above table). Contoso is preparing a campaign with a single newsletter email targeting 280,000 customers. They can complete this campaign in 2 hours, assuming no other campaign is executing simultaneously, because their throughput is 140,000 interactions/hr.

### I don't think that I'm getting the throughput that is promised in the tables above. What do I do in that case?

If you believe that your throughput doesn't meet expectations per these guidelines, contact support or [create a ticket](/power-platform/admin/get-help-support).

### I have no requirement to purchase additional contacts/interacted people, but I'd like to increase the throughput on my journeys. Is that possible?

In the standalone Dynamics 365 Marketing (outbound marketing) SKU, throughput can be increased only with the purchase of additional contacts that provide better throughput based on the tiers mentioned in the above table. Reach out to your Microsoft representative to get more help on this.
