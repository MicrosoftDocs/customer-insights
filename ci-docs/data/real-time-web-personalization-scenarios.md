---
title: Top scenarios for web tracking and personalization
description: Web tracking and personalization in Customer Insights helps teams turn visitor behavior into segments, offers, service actions, and insights.
ms.date: 10/21/2026
ms.topic: concept-article
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: tozahalk
ms.custom:
  - bap-template
  - ci-data-web-tracking
  - ai-gen-docs-bap
  - ai-seo-date: 09/16/2026
ai-usage: ai-assisted
---

# Scenarios for web tracking and personalization

When you use web tracking, the stream of visitor activity helps you acquire new customers, convert active visitors, retain existing customers, and support the people who serve them.

Customers often adopt the following scenarios first to realize value quickly. Each scenario is a starting point rather than a limit. Most organizations begin with one, see how it works, and expand from there.

## Acquisition and campaign scenarios

### Attribute web activity to a paid campaign

Tag the destination links in your paid and social campaigns with a campaign parameter. Customer Insights - Data captures that parameter on every tracked view and action. You can then identify which campaigns drove engagement on your site, not just clicks, and build segments of people who responded to a specific campaign.

### Close the loop between an exported segment and the visit it produced

Export a segment to an advertising platform, and then recognize the visitors who arrive from that campaign when they land on your site. The round trip from segment to ad to tracked visit to follow-up segment happens without any manual list reconciliation.

### Measure landing page performance by audience

Compare how different segments behave on the same landing page by using the pages they viewed and the elements they selected rather than aggregate page counts. The result shows which audiences convert and which audiences leave the page.

## Conversion scenarios

### Welcome back a returning anonymous visitor

Recognize an unknown visitor who has been to your site before and change what they see on arrival, without asking them to identify themselves. Returning visitors can see the category they browsed last time, a continuation of an unfinished task, or an offer that recognizes their repeat interest.

### Recommend based on what the visitor already browsed

Use the specific products, plans, or content a visitor viewed to determine what you show them next. Someone who looked at three premium coffee machines sees premium machines, accessories, and a comparison guide rather than the generic homepage merchandising.

### Convert an anonymous visitor into a known customer

When a visitor supplies an email address or phone number, merge their anonymous profile into a known customer profile and keep the entire browsing history that preceded it. Known customer profiles then include the visitor's previous browsing history instead of starting with a blank record.

### Recover an abandoned browse or cart

Detect when a visitor views a product or starts a purchase and then leaves, and follow up while their interest is still recent. Because the activity is available within seconds, you can follow up during the same session rather than waiting until the next day.

## Personalization scenarios

### Offer an incentive to a high-value segment

Show a discount, upgrade path, or loyalty benefit only to visitors who belong to a segment such as high lifetime value. Define the segment once in Customer Insights - Data and apply it on your website, in journeys, and in exports.

### Suppress offers for customers who already converted

Stop promoting a product to visitors who already own it or already responded to the campaign. Suppression can reduce irrelevant messaging by preventing customers from seeing offers that no longer apply to them.

### Personalize pricing, plan, and renewal pages by tier

Adapt the page a customer sees based on their plan, tier, or contract so that pricing and renewal options reflect their current subscription. This approach is useful for self-service upgrade and renewal paths.

### Test personalization variants without code

Use the Optimizely integration to use your Customer Insights - Data segments as Optimizely audiences and test different experiences for each audience. Marketers can change and measure the experience without requiring a development cycle.

## Segmentation and insight scenarios

### Build intent-based segments from browsing behavior

Create segments based on what people did on your site. For example, create a segment of people who viewed a pricing page twice in the last 30 days without requesting a demo. Behavioral segments capture intent that never appears in transactional data.

### Enrich lead scoring with real-time web signals

Feed web interaction data into your lead scoring model so scores reflect current browsing behavior alongside firmographic and transactional attributes. Sales teams can see a score that changes as the buyer's behavior changes.

### Reunite activity across devices and browsers

A single person visiting from a laptop and a phone starts as two anonymous profiles. After they sign in on either device, the activity from both devices is consolidated into one known profile, which helps prevent double-counting in engagement metrics.

### Surface web activity on the customer timeline

Show sellers and service agents a customer's recent web activity directly on the profile timeline. They can use this information to understand the customer's recent interests instead of relying only on the last recorded transaction.

## Retention and service scenarios

### Detect churn-risk signals from support and cancellation pages

Treat repeated visits to support, troubleshooting, or cancellation pages as an early churn signal, and act on it while the customer is still on the site. A proactive offer or service follow-up can help address the issue before the customer leaves.

### Trigger a real-time service follow-up

Use a tracked action, such as a failed form submission or repeated visits to the same help article, to trigger a journey or service task within seconds. You can contact the customer while they're still experiencing the problem.

### Prioritize outreach with live buying signals

Prioritize accounts and contacts based on their current activity on your site rather than a score that's refreshed nightly. Sellers can then reach out while customer interest is high.

## Related information

- [Web tracking and personalization overview](real-time-web-personalization-overview.md)
- [Set up web tracking and personalization](real-time-web-personalization.md)
- [Personalize your customers' web experience](optimizely-integration.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
