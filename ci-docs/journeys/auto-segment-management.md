---
title: Understand automated segment refresh and data freshness
description: Learn how automated segment management, refresh intervals, and data sync affect audience freshness, and optimize results in Customer Insights - Journeys.
ms.date: 08/31/2026
ms.topic: article
author: udag
ms.author: udag
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-seo-date:02/18/2025
  - ai-gen-description
---

# Understand automated segment refresh and data freshness

Automated segment management in Dynamics 365 Customer Insights – Journeys adjusts segment refresh intervals based on usage to keep active campaign audiences accurate while improving processing speed. This article explains the intervals introduced on February 17, 2025, how data sync affects audience freshness, and how to get fresher results.

## Refresh intervals

- **Newly created unused segments**: Segments that you don't actively use in a journey now refresh every 30 minutes for the first 24 hours to ensure initial accuracy. After this period, they transition to a 24-hour refresh cycle unless they become actively used.
- **Segments in active journeys that don't use behavioral data**: Segments that you actively use in a journey or reference by another segment or email continue refreshing every 30 minutes, ensuring that they stay updated with the latest audience data.
- **Segments in active journeys that use behavioral data**: Segments that you actively use in a journey or reference by another segment or email continue refreshing every 60 minutes, ensuring that they stay updated with the latest audience data.
- **Segments no longer used in any active journey**: Segments move to a 24‑hour refresh cycle. If they remain unused for 120 days, they transition to the Expired state, where they're no longer evaluated and don't count toward segment limits, helping optimize performance. You must republish the segment before using it in a journey.

Behavioral data covers what customers did - opening an email, visiting a form, registering for an event - and you add it from the **Behavioral** tab in the segment builder. Learn more: [Improve targeting using interaction data in segments](real-time-marketing-redesigned-segment-builder.md)

## Benefits of automated segment management

These updates ensure that marketers can rely on automated segment management to:  

- Maintain timely and relevant audience updates for active campaigns.
- Optimize system performance by reducing unnecessary refreshes for inactive segments.
- Streamline audience management, allowing teams to focus on strategy while the system ensures data freshness.

## What happens during a refresh

A refresh isn't a single step. Two things have to happen before an update you make shows up in your segment:

1. **Data sync**: Recent changes to your data - a new contact, an updated job title, a fresh event registration - become available to segmentation. This process runs continuously in the background, independently of your segments.
1. **Segment execution**: Customer Insights - Journeys evaluates your segment definition and works out who belongs in the segment.

Both parts affect how fresh your segment is. A segment can run right on schedule and still miss a change you just made, because the change didn't finish syncing yet.

## Where your segment is calculated

Most segments don't calculate directly on your Dataverse data. They run against a separate store that's built for the large, repeated queries segmentation needs. Data has to be copied into that store first, which is why speed and freshness can differ between runs.

Running straight on Dataverse is faster and uses your latest data, so Customer Insights - Journeys does that wherever it can. There's a limit to how much querying Dataverse can absorb, though, so not every segment can use it. In practice, environments with only a handful of segments run nearly all of them on Dataverse, while environments with hundreds run far fewer that way. A segment also falls back to the separate store if running it on Dataverse doesn't succeed, and a segment can move between the two over time.

This design is deliberate. Sending every segment to Dataverse would slow down the rest of your environment.

When a segment runs against the separate store:

- Its results reflect the last data sync rather than the newest change in Dataverse.
- It's more likely to fall behind its schedule.

> [!NOTE]
> You don't choose where a segment runs. Customer Insights - Journeys decides automatically, balancing freshness against the performance of your environment.

## How data sync affects freshness

Customer Insights - Journeys doesn't manage data sync. The wider Dataverse data platform handles it, copying changes continuously as they happen rather than in a single scheduled batch. Only records that actually changed get copied. A segment refresh doesn't start a sync and can't speed one up - it uses whatever is synced by the time it runs. For background on how Dataverse replicates data and what affects the timing, see [Plan your latency for Link to Fabric](/power-apps/maker/data-platform/fabric-link-plan-latency).

As a planning figure, allow about an hour - sometimes longer - for a change to a record to become available to segmentation. Changes to the shape of your data, like adding a column to a table, take longer.

How close you get to that figure depends on how much your data changes. Environments with a steady stream of updates usually stay well inside the hour. Environments where data changes rarely can sit further behind, though that matter less, because there's little new to pick up.

The key point is that **a refresh interval is a schedule, not a freshness guarantee**. It controls how often your segment is evaluated, not how recent the data behind it is. A run can finish successfully and still leave membership unchanged, because the data it needed didn't sync yet.

**Example**: You change a contact's job title, then wait for the next refresh. The segment refreshes on schedule, but the contact is still evaluated against the old job title until that change syncs. A later refresh picks up the new value.

## Expected segment refresh timing

Segments used in an active journey are the freshest, because they're on the shortest interval and are the most likely to run on Dataverse. Even so:

- Most update within roughly half an hour, in line with their interval.
- A sizable share take longer than their interval suggests.
- A small number sit several hours behind, usually in environments with many segments or when a data sync is delayed.

Plan for that variation when timing matters. If a campaign depends on a change you just made, don't assume the next scheduled refresh includes it. When the timing is critical, check the segment's membership itself rather than assuming the interval was met.

## When refresh frequency matters

How much the refresh interval matters depends on how your journey uses the segment.

- **One time**: The journey runs against a fixed audience. Once it starts, later refreshes don't change who goes through it. Ensure the segment is up to date *before* you start the journey.
- **One time with a dynamic audience**: People who join the segment after the journey starts still enter it, so the refresh interval keeps mattering for as long as the journey runs.
- **Repeating**: Each occurrence uses the audience as it stands when that occurrence begins. People added in between wait for the next occurrence.

Learn more: [Start a journey](journey-start.md)

If you want an audience that deliberately doesn't change, set the segment's refresh rate to **Static snapshot** instead of relying on timing. Learn more: [Create a static snapshot of a segment](real-time-marketing-static-snapshot.md)

## How long a refresh takes

Execution time is different from the refresh interval. The interval is how often a segment is scheduled to run. Execution time is how long that run takes once it starts.

Most segments finish quickly. A typical run takes a couple of minutes, and the large majority complete within about five minutes.

Segment size matters less than you'd expect. A segment with millions of members usually takes about as long as a small one, because most of the time is fixed overhead rather than working through your data. Runs that take dramatically longer are rare, and they usually point to a temporary problem reaching your data rather than to the size or shape of your segment.

This means execution time is rarely why a segment looks out of date. If membership seems stale, the wait is almost always in the data sync or in the queue before the run starts - not in the run itself.

## Get fresher results

- **Keep the number of segments down**: This is the single biggest thing you control. The fewer segments your environment has, the more of them run on Dataverse with fresher data. Delete or unpublish segments you no longer need.
- **Keep definitions lean**: Fewer groups, subgroups, and related tables make a segment easier to run. Learn more: [Build segments in Customer Insights - Journeys](real-time-marketing-build-segments.md)
- **Allow time after a data change**: If you update records and need the segment to reflect them, allow around an hour for the sync on top of the next scheduled refresh.
- **Set a custom interval when you need one**: You can change the refresh interval, or turn automatic refresh off, for an individual segment. Learn more: [Create a Customer Insights - Journeys segment using the Web API](real-time-marketing-api-segment.md)
- **Line up journeys with data refreshes**: If you also use Customer Insights - Data, use quiet times so journeys don't run while data is still being updated. Learn more: [Align quiet times with Customer Insights - Data refresh](coordinate-ci-data-refresh-with-quiet-times.md)

## Related information

- [Segmentation overview](real-time-marketing-segments.md)
- [Build segments in Customer Insights - Journeys](real-time-marketing-build-segments.md)
- [Improve targeting using interaction data in segments](real-time-marketing-redesigned-segment-builder.md)
- [Start a journey](journey-start.md)
- [Create a static snapshot of a segment](real-time-marketing-static-snapshot.md)
- [Align quiet times with Customer Insights - Data refresh](coordinate-ci-data-refresh-with-quiet-times.md)
- [Plan your latency for Link to Fabric](/power-apps/maker/data-platform/fabric-link-plan-latency)

