---
title: Edit a live journey in Customer Insights - Journeys
description: Learn how to edit a live journey in Customer Insights - Journeys without stopping it. Make lightweight edits or publish major changes with version control.
ms.date: 11/23/2026
ai-usage: ai-assisted
ms.topic: how-to
author: udag
ms.author: udag
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:01/21/2025
---

# Edit a live journey in Customer Insights - Journeys

You can edit a live journey in Customer Insights - Journeys without stopping it, including lightweight changes such as renaming elements or adjusting goal percentages. You can also make major changes with Customer Insights - Journeys's built-in journey version control feature. These features give you the flexibility to make edits on the fly, without concern about breaking or being unable to revert a journey.

## How to make lightweight edits to live journeys

In your journey, select the **Edit** button in the top right of the screen. Make changes such as renaming your journey or changing your goal percentage. When you're done, select the **Publish** button in the upper right. You see a confirmation that your changes published successfully.

:::image type="content" source="media/real-time-marketing-journey-edit-published.png" alt-text="Screenshot of a confirmation that live journey edits were published successfully.":::

## Edit a segment used in a live journey (preview)

If you need to change a segment's query-based definition rather than the journey itself, use live segment editing. You can update that definition without stopping the journeys using the segment or creating a new journey version. Static groups remain read-only during live editing. An administrator must first [turn on live segment editing](edit-live-segments.md#turn-on-live-segment-editing).

To change the segment's query and review the affected journeys before saving, follow the steps to [edit a segment used in a live journey](edit-live-segments.md#edit-a-segment-used-in-a-live-journey).

Changes aren't immediate. When the updated membership affects a journey depends on the segment refresh, journey type, and how the segment is used. Removing someone from an entry segment doesn't remove them from a journey they already entered. Review [when your changes take effect](edit-live-segments.md#when-your-changes-take-effect) and [what happens to people already in the journey](edit-live-segments.md#what-happens-to-people-already-in-the-journey) before saving.

## Make major changes to live journeys with version control

> [!NOTE]
> You *can only* edit the following types of live journeys: (1) trigger-based journeys, (2) long-running journeys, or (3) one-time journeys that are scheduled for a future time. You *can't* edit one-time journeys that are already running *or* are scheduled to start very soon. If a journey is scheduled to start soon, the **Edit** button isn't available in the interface.

In your journey, select the **Edit** button and make your changes. If the change impacts your customer experience, such as deleting an email in an existing journey, it creates a new version of the journey. Your existing customers complete the current version of their journey while new customers enter the new version.

The following changes create a new version:

1. Switching an email.
1. Adding or deleting a channel.
1. Adding or updating conditions in branches.

:::image type="content" source="media/real-time-marketing-journey-edit-impact-warning.png" alt-text="Screenshot of an audience impact warning while editing a live journey.":::

The change tracking and auditing capabilities help you efficiently collaborate with your marketing team.

:::image type="content" source="media/real-time-marketing-journey-edit-audit.png" alt-text="Screenshot of a change-tracking comment for an edited live journey.":::

Analytics results are kept for each version, so you can compare and optimize journey flow and goal attainment across all iterations.

:::image type="content" source="media/real-time-marketing-journey-edit-analytics.png" alt-text="Screenshot of analytics results comparing different journey versions.":::
