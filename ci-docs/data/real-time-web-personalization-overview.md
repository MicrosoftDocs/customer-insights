---
title: Web tracking and personalization overview
description: Recognize returning website visitors, personalize their experience, and turn anonymous browsing activity into customer profiles with Dynamics 365 Customer Insights - Data.
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

Most people who visit your website never tell you who they are. They browse, compare, read a few pages, and leave. Until they submit a form, their entire visit is invisible to you.

Web tracking and personalization in Customer Insights - Data changes that. Add a small script to your website, and Customer Insights - Data starts recognizing visitors, remembering what interests them, and personalizing their experience based on their activity. When a visitor eventually shares an email address or phone number, their previous browsing activity becomes part of their customer profile.

Watch this brief video to learn more about real-time web personalization.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=0374bff9-f481-4324-8237-ebbaaffaed27]

## Benefits of web tracking and personalization

Web tracking and personalization in Customer Insights - Data provides the following benefits.

**Recognize people before they identify themselves**: A visitor who came last week is recognized when they return, even though you still don't know their name. You can greet them differently from a first-time visitor.

**React to what someone is actually interested in**: If a visitor spent time viewing premium coffee machines, you can feature those products the next time they arrive instead of showing the generic homepage.

**Keep the history when an anonymous visitor becomes a customer**: When someone gives you an email address, their previous browsing activity becomes part of their profile. New customers don't start as blank records.

**Use website behavior everywhere you already work**: Web activity becomes available to the segments, measures, and profiles you already build. For example, you can create an audience of visitors who viewed the pricing page twice but never requested a demo.

**See which campaigns actually drove engagement**: Tag your campaign links and Customer Insights - Data records which visits came from which campaign, so you can measure engagement rather than clicks.

## Web tracking and personalization scenarios

The following list provides some common scenarios for using web tracking and personalization. For more scenarios, see [Scenarios for web tracking and personalization](real-time-web-personalization-scenarios.md).

- **Welcome back a returning visitor**: Recognize a repeat anonymous visitor and change the content they see.
- **Recover an abandoned browse**: Identify a visitor who viewed a product and left, and follow up while their interest is fresh.
- **Offer something to a specific audience**: Show an incentive only to visitors who belong to a segment such as high lifetime value.
- **Turn a browser into a known customer**: Merge an anonymous profile into a known profile when the visitor signs up, while retaining their browsing history.

## Unknown and known visitors

A visitor is either **unknown** or **known**, and unknown visitors can become known without losing their history.

**Unknown visitors** are people browsing your site who don't identify themselves. Customer Insights - Data gives each visitor an anonymous identifier stored in a cookie and records the pages they view and the elements they select. You can personalize for them without ever knowing who they are.

**Known customers** are people you can identify because they sign in, download something, or place an order. When an unknown visitor becomes known, their anonymous profile merges into their known profile, and you keep everything.

This profile merging sets the feature apart from traditional web analytics. For example, if a person browses from both a laptop and a phone, the two anonymous profiles merge into a single customer profile after the person signs in on either device.

## How it works

The following example shows how Customer Insights - Data connects anonymous web activity to a known customer profile. In this example, Abbie registers in your store in person.

1. Abbie visits your website for the first time. They receive an anonymous identifier stored in a cookie, and Customer Insights - Data begins associating their activity with that identifier. They typically appear on the **Customers** page as an unknown profile within about 30 seconds.
1. Your website personalizes what Abbie sees based on their browsing activity.
1. Abbie signs in or provides their email address when downloading content. Your website calls the `setUser` function with the identifier from your own customer table.
1. The profiles merge in real time. Abbie's known profile includes the interactions recorded while they were anonymous and the cookie identifier as a new identity. From that point on, segments, measures, and APIs refer to their known profile, and the anonymous profile expires.

Cookie identifiers expire after one year, with the expiration period resetting after each visit, so a returning visitor stays recognizable.

To set up web tracking and personalization, see [Set up web tracking and personalization](real-time-web-personalization.md).

## Data captured by web tracking

All data recorded by the tracking script is stored in Dataverse and can be viewed in Power Apps.

### Web activity tables

Web activity is stored in three tables based on the type of signal:

| Table | What it holds |
|---|---|
| `msdynci_personalizationview` | **Page views**: One row is created each time a visitor loads a tracked page. |
| `msdynci_personalizationaction` | **Clicks and element interactions**: One row is created each time a visitor selects a tracked element. |
| `msdynci_personalizationuser` | **Sign-in signals**: Written when your site calls `setUser`. These signals identify a visitor rather than describe browsing, so they carry no page or campaign data. |

The page views and clicks tables contain the data you use most often. Segments and measures also read data from these tables.

### What each event records

Every view and action row captures:

- **Who**: The visitor's cookie identifier (`msdynci_userlocalid`), which connects anonymous activity to the same visitor across a visit. Sign-in signals also include the authenticated identifier that your site passes to `setUser` (`msdynci_userauthid`).
- **What**: The page address for a view (`msdynci_viewuri`) or the element that you selected for an action.
- **When**: The time the signal was raised (`msdynci_signaltimestamp`) and the time the row was written.
- **Which profile it belongs to**: A reference to the visitor's cookie record, which is how the row is later associated with a customer profile. You don't have to create this relationship yourself. The unified profile contains the web activity references created during unification.

For information about two optional fields available for views and actions, see [Capture query string and IP address (optional)](real-time-web-personalization.md#capture-query-string-and-ip-address-optional).

## Privacy and consent

The tracking script sets a cookie on your visitors' devices. Depending on applicable laws and regulations, you might need to obtain consent before setting cookies on visitors' devices. Knowing and following the rules that apply in your markets is your organization's responsibility. If your site allows visitors to opt out of cookies, ensure the tracking script respects their choice.

## Web tracking capacity

Web tracking events are written to your Dataverse environment. Sustained tracking volume therefore consumes Dataverse capacity like other write activity. Before you add the script to a high-traffic site, check your expected daily event volume against your environment's capacity. Monitor capacity consumption after you go live.

## Next steps

- [Scenarios for web tracking and personalization](real-time-web-personalization-scenarios.md)
- [Set up web tracking and personalization](real-time-web-personalization.md)
- [Personalize your customers' web experience](optimizely-integration.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
