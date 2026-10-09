---
title: Exclude bot interactions for reliable analytics
description: Exclude bot interactions in Dynamics 365 Customer Insights - Journeys to filter nonhuman clicks. Learn how bot protection improves analytics reliability.
ms.date: 10/09/2026
ms.topic: how-to
author: Joni-M
ms.author: udag
ms.reviewer: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Exclude bot interactions for reliable analytics

Exclude bot interactions from channel analytics by using bot protection in Customer Insights - Journeys. The feature filters nonhuman clicks on emails, text messages, push notifications, and custom channels to provide more reliable analytics and prevent inflated metrics, incorrect journeys, and fraudulent double opt-ins.

## How automated activity affects email metrics

Every email platform that reports opens and clicks deals with the same problem: email security services and mailbox privacy features open messages and follow links automatically, before the recipient does anything. Customer Insights - Journeys applies bot protection to tracked links. It checks each click against a range of signals and records clicks it classifies as automated as separate bot interactions, so they're kept rather than deleted. Email opens get simpler checks, because an open is recorded when an image loads and there's no step in between where the request can be assessed.

As with any classification of this kind, the judgment is probabilistic: a genuine click can be classified as automated, and some automated activity can still be counted as human. Opens and clicks are therefore best used to compare similar sends over time, not as exact counts. Where a decision depends on precise numbers, measuring the outcome the email is meant to drive, such as site visits or conversions tracked with [UTM parameters](real-time-marketing-utm.md), gives a more reliable and auditable result. To learn more, see [Beyond open rate: Rethinking email marketing metrics](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/10/16/rethinking-email-metrics-the-evolving-landscape-of-open-rates/).

## Impact of bot protection

Bot protection filters out suspected bot clicks. It doesn't impact any historical data. Because bot protection filters out nonhuman link clicks, it might affect some journey triggers and branching conditions that use "email clicked." Protection for email opens is limited to simpler checks, so automated activity can still raise email open counts and open rates. Bot protection doesn't impact push notification open rates.

## How bots are detected

Any time a link is selected, it goes through an intermediate page. Customer Insights - Journeys runs checks on the intermediate page to determine if the click was made by a bot or a human.

## Frequently asked questions

| Question                      | Answer               |
|:-----------------------------------|:------------------------------|
| Why do I see multiple email open interactions for the same contact with the exact same timestamp? | Protection for email opens is limited to simpler checks, because an open is recorded when the email's images load. This condition could be due to bot-related activity, such as email security services or mailbox privacy features loading the images, resulting in multiple open interactions. |
| I noticed an inflated email open rate recently. What's happening? | Because protection for email opens is limited to simpler checks, nonhuman traffic can increase the open rate. To learn more about improving engagement measurement, see [Beyond open rate: Rethinking email marketing metrics](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/10/16/rethinking-email-metrics-the-evolving-landscape-of-open-rates/).|
| Why are no or limited email opens being recorded? | Many modern email clients block image loading by default to protect user privacy. Because email open tracking relies on images being loaded, this condition might limit the app's ability to accurately capture email open interactions. To learn more, see [Beyond open rate: Rethinking email marketing metrics](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/10/16/rethinking-email-metrics-the-evolving-landscape-of-open-rates/). |
| Why are there no email opens or clicks recorded? | Ensure compliance profiles are correctly configured, and tracking is allowed for the contacts, leads, or Customer Insights - Data profiles that received the email. To learn more, see [Consent management overview](real-time-marketing-compliance-settings.md). | 

