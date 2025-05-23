---
title: Edit a live journey in Customer Insights - Journeys
description: Edit live journeys in Customer Insights - Journeys without stopping them. Learn how to make lightweight edits and major changes with version control.
ms.date: 01/21/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
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

You can make lightweight edits to journeys, such as renaming elements or adjusting goal percentages, without stopping them. You can also make major changes with Customer Insights - Journeys's built-in journey version control feature. These features give you the flexibility to make edits on the fly, without concern about breaking or being unable to revert a journey.

## How to make lightweight edits to live journeys

In your journey, select the **Edit** button in the top right of the screen. Make changes such as renaming your journey or changing your goal percentage. When you're done, select the **Publish** button in the upper right. You'll see a confirmation that your changes published successfully.

> [!div class="mx-imgBorder"]
> ![Published journey edit confirmation.](media/real-time-marketing-journey-edit-published.png "Published journey edit confirmation")

## How to make changes that impact your customer experience

> [!NOTE]
> You *can only* edit the following types of live journeys: (1) trigger-based journeys, (2) long-running journeys, or (3) one-time journeys that are scheduled for a future time. You *can't* edit one-time journeys that are already running *or* are scheduled to start very soon. If a journey is scheduled to start soon, the **Edit** button isn't available in the interface.

In your journey, select the **Edit** button and make your changes. If the change impacts your customer experience, for example, deleting an email in an existing journey, it will result in a new version of the journey. Your existing customers will complete the current version of their journey while new customers will enter the new version.

The following are examples of changes that will result in a new version:

1. Switching an email.
1. Adding or deleting a channel.
1. Adding or updating conditions in branches.

> [!div class="mx-imgBorder"]
> ![Audience impact warning.](media/real-time-marketing-journey-edit-impact-warning.png "Audience impact warning")

The change tracking and auditing capabilities allow you to efficiently collaborate with your marketing team.

> [!div class="mx-imgBorder"]
> ![Change tracking comment.](media/real-time-marketing-journey-edit-audit.png "Change tracking comment")

Analytics results are kept for each version, enabling you to compare and optimize journey flow and goal attainment across all iterations.

> [!div class="mx-imgBorder"]
> ![Analytics comparison between versions.](media/real-time-marketing-journey-edit-analytics.png "Analytics comparison between versions")

[!INCLUDE [footer-include](./includes/footer-banner.md)]
