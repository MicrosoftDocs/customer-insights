---
title: Visualize results from your scoring model
description: Visualize lead scoring model results in Dynamics 365 Customer Insights - Journeys to evaluate scores and identify promising leads. Explore the steps.
ms.date: 11/09/2026
ms.topic: how-to
ai-usage: ai-assisted
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Visualize lead scoring model results

After you publish a lead scoring model in Dynamics 365 Customer Insights - Journeys, use its insights and individual lead scores to evaluate the results. Review the score distribution to identify high-potential leads, refine your scoring criteria, and inform your qualification thresholds.

## Prerequisites

- Ensure you have the **Lead Score Viewer** or **Lead Score Modeler** security role. Learn more in [Security roles for lead scoring and qualification](real-time-marketing-security-roles-lead-scoring.md).
- If **Scoring models** isn't available in the navigation, ask an administrator to check that the **Lead Management** feature switch is enabled. Learn more in [Enable lead scoring](real-time-marketing-create-lead-scoring-model.md#enable-the-feature).
- [Create and publish a lead scoring model](real-time-marketing-create-lead-scoring-model.md), and allow time for scores to calculate. Initial calculation time depends on the number of leads and the complexity of the model.

> [!NOTE]
> Scoring models refresh every two hours. Changes to lead data or interactions might not appear in scores immediately.

## Review model insights

1. Go to **Lead management** > **Scoring models**.
1. Open the published model you want to review.
1. Select the **Insights** tab.

Review the following metrics:

- Total number of leads scored.
- Score for the top 10% of leads.
- Score distribution among all leads.
- Number of leads per grade, if you configured grades.

Use the score distribution to assess whether your scoring criteria distinguish high-potential leads from those that need more engagement. Grades are optional, so a model can calculate scores without assigning grades.

## Review individual lead scores

1. In the scoring model, select the **Scores** tab.
1. Review the leads scored by the model, along with their scores and any configured grades.
1. Open a lead record to review its calculated scores and compare the results with your model's criteria.

## Use results for nurturing and qualification

Use scores to inform the next action for a lead. For example, you can create a segment for leads with scores between 13 and 19 points and use that segment in a nurturing journey. This range is illustrative: choose a range that fits your model and business goals. For segment creation guidance, see [Build segments in Customer Insights - Journeys](real-time-marketing-build-segments.md).

> [!NOTE]
> Scoring model refresh and segment refresh are separate processes. An updated score doesn't guarantee an immediate change in segment membership. Data sync and segment evaluation also affect when a lead enters a segment. Learn more in [Understand automated segment refresh and data freshness](auto-segment-management.md).

A high score or a position in the top 10% doesn't automatically mark a lead as sales-ready. Configure and publish qualification criteria and actions to update **Status Reason** to **Marketing Qualified** or **Sales-Ready** to **Yes**. Only leads with an open status can be marketing-qualified.

If a marketing-qualified lead's score later falls below the qualification threshold, the lead remains marketing-qualified. Review qualification status separately from the current score when you assess sales readiness. Learn more in [Qualify the best leads](real-time-marketing-qualify-leads.md).

## Troubleshoot unexpected results

If scores are missing or differ from what you expect, check the following items:

- **Calculation timing:** Allow time for the initial calculation or the next two-hour refresh.
- **Audience conditions:** Confirm that the lead meets the model's audience conditions.
- **Business-unit scope:** If the model operates within a business unit, confirm that the lead belongs to that business unit.
- **Interaction timeframes:** Check that the interactions fall within the timeframes defined in the scoring conditions.
- **Parent-contact interactions:** Check whether **Count parent contact interactions** is enabled in the model settings. If it isn't enabled, the model considers only the lead's interactions.
- **Merged leads:** If you merged duplicate leads, the model might not score the primary record. Review the recovery options, which include republishing the model, in [Publish a lead scoring model and start calculating scores](real-time-marketing-create-lead-scoring-model.md#publish-a-lead-scoring-model-and-start-calculating-scores).
- **Grades:** Confirm that grades are configured if you expect them to appear.

For details about these settings, see [Create lead scoring models](real-time-marketing-create-lead-scoring-model.md).
