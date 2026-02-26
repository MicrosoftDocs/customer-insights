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

This article explains how to create segments using consent‑based criteria and how consent is evaluated when segment membership is calculated. Consent‑based segments help you target the right audience while respecting customer consent, purposes, topics, and enforcement models.

Consent evaluation in segments is aligned with the rules used during journey execution. This alignment ensures that contacts included in a segment are evaluated consistently when messages are sent.

## Prerequisites

Before you build a consent‑based segment, make sure that:

- A **compliance profile** is available and active.
- **Purposes** and **topics** are defined and active in the compliance profile.
- Consent records exist for your contacts (inactive consent records are also evaluated).
- Your audience configuration defines one or more recipient attributes for the selected channel (for example, email address fields).

## What is a consent‑based segment

A consent‑based segment is a segment that includes or excludes contacts based on their consent preferences. Consent is evaluated using:

- **Compliance profile**
- **Purpose** (for example, Commercial)
- **Topic** (for example, Newsletter)
- **Channel** (for example, Email)
- **Enforcement model** configured for the selected purpose and channel

Consent‑based segments respect the hierarchy between purposes and topics. If a contact doesn’t have consent for the parent purpose of a selected topic, the contact is excluded from the segment.

## Create a consent‑based segment

When you add a consent group to a segment, you define how consent should be evaluated for segment membership.

### Step 1: Select a compliance profile

- If only the **default compliance profile** exists, it’s preselected.
- If exactly one **custom compliance profile** exists in addition to the default, the custom profile is preselected.
- If multiple compliance profiles exist, no profile is preselected and you must choose one.

**Screenshot placeholder**

*Screenshot showing the consent group with the Compliance profile dropdown expanded.*

### Step 2: Select a purpose

- By default, the first purpose of type **Commercial** is preselected.
- Only **active purposes** are shown.
- Purposes from different business units can be selected.

The selected purpose determines which enforcement model is applied.

**Screenshot placeholder**

*Screenshot showing the Purpose dropdown with an active Commercial purpose selected.*

### Step 3: Select a channel

- By default, **Email** is selected.
- Available channels include:
  - Email
  - Text message
  - Custom channel
  - Voice channel

The selected channel, together with the purpose, determines the enforcement model.

**Screenshot placeholder**

*Screenshot showing the Channel dropdown with available channel options.*

### Step 4: Select "Will send" criteria

The options available in the **Will send** dropdown are dynamically adjusted based on the enforcement model defined for the selected purpose and channel.

#### Restrictive enforcement model

- **Will send (those who opted in)**
- **Will not send (those who opted out or have not set)**
- **Those who have opted out**

#### Non‑restrictive enforcement model

- **Will send (those who opted in or have not set)**
- **Will not send (those who opted out)**
- **Those who have opted in**

#### Disabled enforcement model

- **Will send**
- **Will not send**

You can explicitly choose opted‑in or opted‑out criteria, even when using **Will send** or **Will not send**, to fine‑tune segment membership.

**Screenshot placeholder**

*Screenshot showing the Will send dropdown with options reflecting the current enforcement model.*

### Step 5: Select a topic

- No topic is selected by default.
- Only **active topics** are shown.
- Topics must belong to the selected purpose.

If a contact doesn’t have consent for the parent purpose of the selected topic, the contact is excluded from the segment.

**Screenshot placeholder**

*Screenshot showing the Topic lookup filtered to active topics.*

### Step 6: Select a recipient field (if applicable)

If multiple recipient attributes are configured for the selected audience and channel (for example, multiple email address fields), a **Recipient** dropdown is shown.

Use this dropdown to select which attribute should be evaluated for consent.

**Screenshot placeholder**

*Screenshot showing the Recipient dropdown with multiple email address fields.*

## How consent is evaluated

Segment membership is calculated using the same consent evaluation logic as journey execution. Evaluation follows these principles:

- Consent is evaluated for the selected **purpose, topic, channel, and recipient**.
- Inactive consent records are included in evaluation.
- Purpose and topic hierarchy is enforced.
- The enforcement model determines how opted‑in, opted‑out, and unset consent states are treated.

> [!NOTE]
> If the enforcement model of a purpose changes after a segment is created, the segment might display a non‑existing option in the **Will send** dropdown. In this case, the option is automatically mapped to a valid value.

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

**Screenshot placeholder**

*Screenshot showing the warning message when editing a segment created with old consent rules.*

## Important considerations

- Only **active compliance profiles, purposes, and topics** are shown.
- Inactive items aren’t available for selection.
- Consent‑based segmentation respects parent‑child business unit scoping.
- Segment counts reflect consent evaluation rules, which might differ from simple attribute‑based filters.

## Next steps

- Review your compliance profiles and enforcement models.
- Validate segment membership by comparing segment counts with expected consent behavior.
- Use consent‑based segments in journeys to ensure consistent evaluation at send time.
