---
title: "Troubleshooting: Segments show incorrect member count"
description: Troubleshoot issues related to segments showing an incorrect member count in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/23/2026
ms.topic: troubleshooting-general
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Troubleshooting: Segments show incorrect member count

This article provides a resolution for an issue where a segment doesn't return the expected member count. The segment may show higher or lower numbers than expected. This article can help determine if there's a discrepancy and gives steps to figure out the error's root cause.

## Incorrect member count symptoms

A segment runs and refreshes but shows a discrepancy from the expected counts. The segment shows a higher or lower number of contact IDs than expected.

## Incorrect member count examples and resolutions

The next sections in the article detail member count discrepancies you may run into and offer troubleshooting tips to resolve the issue.

### Segments show no members or fewer members than expected

To determine why a segment has fewer members than expected, try the following troubleshooting steps:

#### Step 1: Validate the basic logic for contradictory conditions or rules

Contradictory "AND" conditions or rules on the same attribute always generate empty segments. For example: `FirstName = Joe AND FirstName = Frank`.

The set operations (union, intersect, and except are used to combine two rules) are applied on the ContactId returned by each rule. So, depending on the expected outcome, verify if the expected ContactId is part (or isn't part) of the result of each rule evaluation.

#### Step 2: Break down complexity

When working with complex segments with multiple conditions or rules, reduce complexity and isolate the condition or rule responsible for the issue. This helps identify the exact case or condition where the issue occurs.

- Start from the complete segment and remove conditions and rules one by one. Run the segment after each change until it returns members.
- Build a new segment from scratch and add conditions and rules one by one from the segment that's yielding no members. Run the segment after each step of adding conditions or rules until no members are returned.
- Once the rule that filters out the members is identified, take a sample expected contact and verify if it matches all conditions added to the segment.
- Remove exclusion segments to verify if the contact shows up before adding them and check if the exclusion segment has the ContactId that might be removing it from the primary segment.

#### Step 3: Validate business units

Check if business unit scoping is enabled for the org. If enabled, real-time journeys will only return members from your business unit.

- Real-time journeys enable business units by default. In outbound marketing, business units may or may not be turned on.
- While outbound marketing allows every segment to include or not to include business units, in real-time journeys, either all segments have business units enabled or none of them have it.

#### Step 4: Validate empty tables

Validate that the tables used in the segment aren't empty. All entities used in a segment require a minimum of one record to trigger sync for that segment. If an entity is empty, the segment won't show the expected members.

#### Step 5: Validate consent

Validate if consent is enabled. Consent filters segments shown based on the chosen purpose and topic. Learn more: [Migrate consent from outbound marketing](real-time-marketing-consent-transition.md#migrate-consent-from-outbound-marketing)

#### Step 6: Allow time for data synchronization

Publishing or refreshing a segment may be delayed if the underlying data has not fully synchronized. To avoid any issues:

- Wait a short period after publishing or refreshing a segment.
- If members aren’t added immediately, allow the next scheduled refresh to run so the data can finish synchronizing.

This is especially important in certain scenarios, such as:

- Tables that are being updated via data import (for example, contacts or leads tables).
- Newly updated consent records.
- Tables that were recently enabled for Segmentation or change tracking.
- Recent uploads of static segment CSV files.

### Segments show more members than expected

To determine why a segment has more members than expected, try the following troubleshooting steps:

#### Step 1: Break down complexity

- Start from the complete segment and remove conditions and rules one by one. Run the segment after each change until it adds the expected member.
- Check if your segment has any except clauses or exclusion segments and verify if the expected contacts are a part of it and aren't getting filtered out.
- Once the rule that causes the member to get added is identified, verify if the data correlates to the output. For example if the rule says `firstname = 'Frank'`, the segment should only add contacts where `firstname = 'Frank'`.

#### Step 2: Discrepancy with outbound marketing or Advanced Find members

If you observe a discrepancy with outbound marketing or Advanced Find members, verify the following:

- Verify if the relationships used are in the same order. An "account" entity being used in a segment is a relationship between "contact" and "account". It's different from applying filters directly on the "account" entity in Advanced Find.
- Real-time journeys allow creating segments on contact and lead entities only. Verify that these are the primary entities used in outbound marketing or Advanced Find segments.

#### Step 3: Validate that virtual fields aren't being used

Currently, virtual fields created in Dataverse in tables aren't supported by the segmentation feature.

## When should you raise a support ticket?

If all the above conditions are met and if the expected contacts still don't match, you should raise a support ticket. When you open a support ticket, always include the following information:

- OrgId
- Segment ID for real-time journeys segments
- Discrepancy source: Advanced Find or outbound marketing
    - FetchXML for Advanced Find
    - Segment ID for outbound marketing
- Sample ContactIds that should or shouldn't show up in the segment.
- Attributes and the entities where the ContactId is causing the potential discrepancy.
