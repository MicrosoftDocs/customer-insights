---
title: Outreach Optimization Agent in Customer Insights - Journeys (preview)
description: Outreach Optimization Agent in Dynamics 365 Customer Insights – Journeys uses AI to send marketing emails at peak engagement times. Learn how to set it up.
ms.date: 05/04/2026
ms.topic: how-to
ms.collection: bap-ai-copilot
author: Joni-M
ms.author: alfergus
ms.reviewer: alfergus
---

# Outreach Optimization Agent in Customer Insights - Journeys (preview)

Outreach Optimization Agent is an AI-powered journey step in Dynamics 365 Customer Insights – Journeys that optimizes *when* your marketing emails are sent. Determining the best time to reach your audience is difficult to do manually at scale — the agent addresses this by analyzing historical engagement data and automatically selecting high-engagement send times for your emails.

The agent uses *aggregated* historical interaction patterns to calculate a baseline best send time. You add it to a customer journey like any other step, and the agent handles scheduling from there.

## What the Outreach Optimization Agent does

- **Analyzes aggregated engagement patterns.** It accesses your organization's historical interaction data— such as when past emails were opened or clicked — to identify general patterns of peak engagement across your audience.
- **Determines an optimal send time.** Based on those patterns, the agent selects the time (or times, for multi-email sequences) when your audience is most likely to engage with your messages.
- **Falls back gracefully for new environments.** If historical engagement data is not yet available (for example, for a first-time user), the agent uses a generic fallback strategy so your emails are still sent at a reasonable time.
- **Honors quiet-time settings.** The agent respects your organization's configured quiet times. Even if historical data suggests a high-engagement window outside permitted hours (for example, late at night), the agent will not schedule emails during quiet-time periods.
- **Honors contact point consent.** The agent respects the communication preferences set for each contact or lead. If a contact has opted out of email communication on a specific address, no email is sent to that address.

## Key benefits

- **Maximize engagement without manual effort**: Automatically sends emails at the times your audience is most likely to open and interact, eliminating the need to manually analyze send-time performance.
- **Turn historical data into immediate value**: Uses your organization’s aggregated engagement patterns to continuously inform better send-time decisions—no complex setup or data science expertise required.
- **Scale personalization across every journey**: Optimizes timing across single emails and multi-email sequences, ensuring each communication is delivered when it has the highest chance of impact.
- **Accelerate time-to-value for new deployments**: Provides intelligent fallback scheduling when historical data is limited, so you can start optimizing from day one.
- **Stay compliant by design**: Automatically respects quiet-time policies and customer consent preferences, ensuring all communications align with organizational and regulatory requirements.
- **Reduce operational complexity**: Removes guesswork and ongoing optimization overhead from campaign execution, allowing teams to focus on content and strategy instead of scheduling.

## Prerequisites

To be able to use Outreach Optimization Agent in journeys, you have to:

- Enable Outreach Optimization Agent via AI Hub

## Using the Outreach Optimization Agent in a journey

At a high level, using the agent involves adding it to a journey, selecting the emails to send, defining when they should be sent, and—when using multiple emails—choosing a goal.

### 1. Add the agent to a journey

In the journey designer, add Outreach Optimization Agent as a step. The agent behaves like other journey steps and can be placed anywhere in the flow where you want email timing to be optimized.

### 2. Choose the emails to send

When configuring the step, select one or more email messages.

#### Single email

Select one email. The agent calculates the best send time and delivers the email at that time. Because there is only one message, the goal is immediately considered met once the email is sent, and the contact moves to the next step in the journey. This is useful when you want a single communication — such as a newsletter or announcement — to arrive when recipients are most likely to engage, without manually selecting a send time.

#### Multiple emails

Select two or more emails. The agent schedules each email at its own optimal send time, spacing them out based on the engagement data. When configuring multiple emails, you must select a goal that defines the desired outcome of the sequence (see the section below for available options).

The agent sends the first email at the best available time, then sends each subsequent email at the next optimal time. Throughout the sequence, the agent tracks whether the goal condition has been satisfied.

If the goal is met before all emails have been sent, the agent continues to send the remaining emails in the sequence. It does not cancel queued messages. However, it records the goal as achieved at the point the condition was satisfied, and once all emails have been sent, the contact moves to the next step in the journey with a Goal met status.

### 3. Goal options for multi-email sequences

When using multiple emails, choose one of three goal criteria:

- **All emails are sent.** The goal is met when the agent has delivered every email in the sequence. Use this when your objective is to ensure each contact receives all planned touchpoints, regardless of interaction. *Example:* A 3-email educational series where the journey should continue only after all 3 emails have been delivered.

- **Any link in any email is clicked.** The goal is met as soon as the contact clicks **any link** in **any of the emails** in the sequence. This treats any click as a positive engagement signal. *Example:* You send up to 4 reminder emails. If the contact clicks a link in the second email, the goal is recorded as achieved at that point. The remaining emails are still sent, and the contact proceeds with a **Goal met** status after the sequence completes.

- **Selected links are clicked.** The goal is met when the contact clicks one of the **specific links you designate** across the emails. This lets you target a particular call-to-action rather than any link. *Example:* Your email contains a "Register Now" button. You set that link as the goal trigger. If the contact clicks "Register Now", the goal is achieved.

After the full sequence completes, the journey can branch on the **Goal met** or **Goal not met** outcome. If the goal was not met by the end date (for example, no link was clicked before the specified cutoff), the agent outputs **Goal not met**, and the contact proceeds to the next journey step.

### 4. Define the end date

The end date defines the latest point in time by which the agent can send emails. The agent schedules all selected emails at optimal times, but ensures that all sends occur **before this date**.

The end date also defines when the goal evaluation completes:

- If the goal condition (for example, a link click) is satisfied before the end date, the goal is recorded as met.
- If the end date is reached and the goal condition has not occurred, the agent outputs **Goal not met**.

[!INCLUDE [footer-include](./includes/footer-banner.md)]