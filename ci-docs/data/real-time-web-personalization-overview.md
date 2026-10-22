---
title: Web tracking and personalization overview
description: Recognize returning website visitors, personalize what they see, and turn anonymous browsing into customer profiles with Dynamics 365 Customer Insights - Data.
ms.date: 10/21/2026
ms.topic: overview
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

# Web tracking and personalization overview

Most people who visit your website never tell you who they are. They browse, compare, read a few pages, and leave. Until they fill in a form, their entire visit is invisible to you.

Web tracking and personalization in Customer Insights - Data changes that. Add a small script to your website and Customer Insights - Data starts recognizing visitors, remembering what interests them, and letting you change what they see in response. When a visitor eventually shares an email address or phone number, everything they did beforehand stays with them and becomes part of their customer profile.

Watch this brief video to learn more about real-time web personalization.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=0374bff9-f481-4324-8237-ebbaaffaed27]

## Benefits of web tracking and personalization

Web tracking and personalization in Customer Insights - Data provides many benefits.

**Recognize people before they identify themselves**: A visitor who came last week is recognized when they come back, even though you still don't know their name. You can greet them differently from a first-time visitor.

**React to what someone is actually interested in**: If a visitor spent their time on premium coffee machines, you can lead with premium coffee machines the next time they arrive, instead of the generic homepage.

**Keep the history when an anonymous visitor becomes a customer**: The moment someone gives you an email address, their previous browsing joins their profile. New customers don't start as blank records.

**Use website behavior everywhere you already work**: Web activity becomes available to the segments, measures, and profiles you already build, so "viewed the pricing page twice and never requested a demo" becomes an audience you can act on.

**See which campaigns actually drove engagement**: Tag your campaign links and Customer Insights - Data records which visits came from which campaign, so you can measure engagement rather than clicks.

## Web tracking and personalization scenarios

The following list provides some common scenarios for using web tracking and personalization. For more scenarios, see [Scenarios for web tracking and personalization](real-time-web-personalization-scenarios.md).

- **Welcome back a returning visitor**: Recognize a repeat anonymous visitor and change what the page leads with.
- **Recover an abandoned browse**: Spot someone who examined a product and left, and follow up while the interest is fresh.
- **Offer something to a specific audience**: Show an incentive only to visitors who belong to a segment such as high lifetime value.
- **Turn a browser into a known customer**: Merge an anonymous profile into a known one at the moment of signup, keeping the history.

## Two kinds of visitors

A visitor is either **unknown** or **known**, and unknown visitors can become known without losing their history.

**Unknown visitors** are people browsing your site who didn't identify themselves. Customer Insights - Data gives each one an anonymous identifier stored in a cookie, and records the pages they view and the elements they select. You can personalize for them without ever knowing who they are.

**Known customers** are people you can identify, because they signed in, downloaded something, or placed an order. When an unknown visitor becomes known, their anonymous profile merges into their known profile, and you keep everything.

 Merging sets this feature apart from traditional web analytics. For example, if a person browses from both a laptop and a phone, the two anonymous profiles merge into a single customer profile after the person signs in on either device.

## How it works

The following example shows how Customer Insights - Data connects anonymous web activity to a known customer profile for a customer named Abbie, who registers in your store in person.

1. Abbie visits your website for the first time. She receives an anonymous identifier stored in a cookie, and Customer Insights - Data begins recording her activity against it. She typically appears on the **Customers** page as an unknown profile within about 30 seconds.
1. Your website personalizes what Abbie sees, based on what she looks at.
1. Abbie signs in, or downloads something and gives her email address. Your website calls the `setUser` function with the identifier from your own customer table.
1. The profiles merge in real time. Abbie's known profile picks up every interaction from when she was anonymous, along with the cookie identifier as a new identity. Segments, measures, and APIs all refer to her known profile from that point on, and the anonymous profile expires.

Cookie identifiers use a rolling one-year expiration that refreshes on each visit, so a returning visitor stays recognizable.

To set up, go to [Set up web tracking and personalization](real-time-web-personalization.md).

## Data captured by web tracking

All data recorded by the tracking script is stored in Dataverse and available to view in Power Apps.

### Web activity tables

Web activity is split across three tables by the kind of signal that produced it:

| Table | What it holds |
|---|---|
| `msdynci_personalizationview` | **Page views**: One row each time a visitor loads a tracked page. |
| `msdynci_personalizationaction` | **Clicks and element interactions**: One row each time a visitor selects a tracked element. |
| `msdynci_personalizationuser` | **Sign-in signals**: Written when your site calls `setUser`. These identify a visitor rather than describe browsing, so they carry no page or campaign data. |

The page views and clicks tables contain the data you use most often. Segments and measures also read data from these tables.

### What each event records

Every view and action row captures:

- **Who**: The visitor's cookie identifier (`msdynci_userlocalid`), which is how anonymous activity stays connected to one person across a visit. Sign-in signals also include the authenticated identifier your site passed to `setUser` (`msdynci_userauthid`).
- **What**: The page address for a view (`msdynci_viewuri`), or the element that was selected for an action.
- **When**: The time the signal was raised (`msdynci_signaltimestamp`) and the time the row was written.
- **Which profile it belongs to**: A reference to the visitor's cookie record, which is how the row is later associated with a customer profile. You don't have to build a relationship yourself; the unified profile carries web activity references produced during unification.

Two optional fields that are available on views and actions are described in the [Capture query string and IP address (optional)](real-time-web-personalization.md#capture-query-string-and-ip-address-optional).

## Privacy and consent

The tracking script sets a cookie on your visitors' devices. Many countries and regions, including the European Union, require you to obtain consent before doing so. Knowing and following the rules that apply in your markets is your organization's responsibility. If your site offers visitors a way to opt out of cookies, ensure the tracking script honors that choice.

## How much traffic it supports

Web tracking events are written to your Dataverse environment, so sustained tracking volume consumes Dataverse capacity the way other write activity does. Before you add the script to a high-traffic site, check your expected daily event volume against your environment's capacity, and watch consumption after you go live.

## Next steps

- [Scenarios for web tracking and personalization](real-time-web-personalization-scenarios.md)
- [Set up web tracking and personalization](real-time-web-personalization.md)
- [Personalize your customers' web experience](optimizely-integration.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
