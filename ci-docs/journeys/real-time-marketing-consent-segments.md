---
title: Build segments using consent‑based criteria
description: Learn how to build segments using consent‑based criteria in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/26/2026
ms.topic: how-to
author: petrjantac
ms.author: cbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Build segments using consent‑based criteria

> [!IMPORTANT]
> Existing segments continue to be evaluated using the consent rules that were in effect when they were created.  
>
> This update applies only to new segments. No changes are made to existing segments, and their behavior remains unchanged.

This article explains how to create segments using consent‑based criteria and how consent is evaluated when segment membership is calculated. Consent‑based segments help you target the right audience while respecting customer consent, purposes, topics, and enforcement models.

Consent evaluation in segments is aligned with the rules used during journey execution. This alignment ensures that contacts included in a segment are evaluated consistently when messages are sent.

## Prerequisites

Before you build a consent‑based segment, make sure that [consent](real-time-marketing-compliance-settings.md) is configured and:

- A **compliance profile** is available and active.
- **Purposes** and **topics** are defined and active in the compliance profile.

## What is a consent‑based segment

A consent‑based segment is a segment that includes or excludes contacts, leads, or profiles based on their consent preferences. Consent is evaluated using:

- **[Compliance profile](real-time-marketing-compliance-settings.md#compliance-profiles)**
- **[Purpose](real-time-marketing-compliance-settings.md#purposes)** (for example, Commercial)
- **[Topic](real-time-marketing-compliance-settings.md#topics)** (for example, Newsletter)
- **Channel** (for example, Email)
- **[Enforcement model](real-time-marketing-compliance-settings.md#consent-enforcement-models)** configured for the selected purpose and channel

> [!IMPORTANT]
> Consent‑based segments membership is evaluated based on the contact point consent. The `DoNotBulkEmail` contact attribute is NOT considered.
>
> Consent‑based segments respect the hierarchy between purposes and topics. If a contact doesn’t have consent for the parent purpose of a selected topic, the contact is excluded from the segment.

## Create a consent‑based segment

When you add a consent group to a segment, you define how consent should be evaluated for segment membership.

### Step 1: Add Compliance Profile to create a new segment group

1. Select the **Compliance profile** in the right-hand menu to create a new segment group.
1. Select **Compliance profile** in the newly created group.
  
      - If only the **default compliance profile** exists, it’s preselected.
      - If exactly one **custom compliance profile** exists in addition to the default, the custom profile is preselected.
      - If multiple compliance profiles exist, no profile is preselected and you must choose one.

:::image type="content" source="media/real-time-marketing-conset-segments-add-complianceprofile.png" alt-text="Add compliance profile to create a new segment group." lightbox="media/real-time-marketing-conset-segments-add-complianceprofile.png":::

### Step 2: Select a purpose and optionally a topic

- By default, the first purpose of type **Commercial** is preselected.
- Only **active** purposes and topics are shown.
- Purposes from different business units can be selected.

:::image type="content" source="media/real-time-marketing-consent-segments-configure.png" alt-text="Select purpose, channel, and optionally a topic." lightbox="media/real-time-marketing-consent-segments-configure.png":::

You can optionally add a **Topic** by selecting "+ Topic" button.

### Step 3: Select a channel

- By default, **Email** is selected.
- Available channels include:
  - Email
  - Text message
  - Custom channel
  - Voice channel

The selected channel, together with the purpose, determines the enforcement model.

### Step 4: Select "Will send" criteria

> [!IMPORTANT]
> The options available in the **Will send** dropdown are dynamically adjusted based on the **enforcement model** defined for the selected purpose and channel.

#### Restrictive enforcement model

- **Will send (those who opted in)**  
  The segment includes **only** contacts who have explicitly opted in for the selected purpose, topic, channel, and recipient.  
  Contacts who opted out or never provided consent are excluded.

- **Will not send (those who opted out or have not set)**  
  The segment includes contacts who explicitly opted out **and** contacts who have no consent record (consent not set).

- **Those who have opted out**  
  The segment includes only contacts who explicitly opted out. Contacts with no consent record are excluded.

#### Non‑restrictive enforcement model

- **Will send (those who opted in or have not set)**  
  The segment includes contacts who explicitly opted in **and** contacts who have no consent record.  
  Contacts who explicitly opted out are excluded.

- **Will not send (those who opted out)**  
  The segment includes only contacts who explicitly opted out.

- **Those who have opted in**  
  The segment includes only contacts who explicitly opted in. Contacts with no consent record are excluded.

#### Disabled enforcement model

- **Will send**  
  The segment includes all contacts that match the remaining segment criteria, regardless of consent state.

- **Will not send**  
  The segment includes no contacts, regardless of consent state.

### Step 5: Select a recipient field (if applicable)

If multiple recipient attributes are configured for the selected audience and channel (for example, multiple email address fields), a **Recipient** dropdown is shown.

Use this dropdown to select which attribute should be evaluated for consent.

## How consent is evaluated

Segment membership is calculated using the same consent evaluation logic as journey execution. Evaluation follows these principles:

- Consent is evaluated for the selected **purpose, topic, channel, and recipient**.
- Inactive consent records are included in evaluation.
- Purpose and topic hierarchy is enforced.
- The enforcement model determines how opted‑in, opted‑out, and unset consent states are treated.
- [More details](real-time-marketing-email-text-consent.md#how-consent-is-respected-for-emails) about consent evaluation.

> [!NOTE]
> If the enforcement model of a purpose changes after a segment is created, the segment might display a nonexisting option in the **Will send** dropdown. In this case, the option is automatically mapped to a valid value.

## Common scenarios

### Include all newsletter subscribers

**Scenario**: You want to build a segment of all contacts subscribed to a newsletter defined by **Topic A** for the **Email** channel.

**Approach**:

- Select the appropriate compliance profile.
- Select the Commercial purpose.
- Select Email as the channel.
- Choose **Will send** based on your enforcement model.
- Select Topic A.

### Target contacts who opted out of a topic

**Scenario**: You want to send an email to contacts who opted out of **Topic A** but are still opted in to the Commercial purpose.

**Approach**:

- Create two consent groups.
- In the first group, target contacts opted in to the Commercial purpose.
- In the second group, target contacts opted out of Topic A.
- Combine the groups using **AND** logic.

This allows you to explicitly include contacts who opted out of a specific topic while remaining compliant with purpose‑level consent.

## Editing existing consent‑based segments

- Existing consent segments created with the previous consent logic (V1) continue to use the old UI and evaluation logic.
- New consent segments (V2) use the new consent UI and evaluation logic automatically.
- If you edit a segment created with the previous consent rules, a warning message is shown.

## Important considerations

- Only **active compliance profiles, purposes, and topics** are shown.
- Inactive items aren’t available for selection.
- Segment counts reflect consent evaluation rules, which might differ from simple attribute‑based filters.

## Next steps

- Review your compliance profiles and enforcement models.
- Validate segment membership by comparing segment counts with expected consent behavior.
- Use consent‑based segments in journeys to ensure consistent evaluation at send time.
