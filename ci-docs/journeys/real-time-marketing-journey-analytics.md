---
title: Real-time tile analytics in journeys
description: Real-time journey analytics show the number of people who enter each step in a Customer Insights journey, who left each step, and why they left each step.
ms.date: 05/20/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - enduser
---

# Real-time tile analytics in journeys

It’s critical to understand exactly what happened to each customer who enters and exits your real-time journeys. The analytics provided by each journey answer questions like, "How many people started this journey?", "How many people received email from this journey?", and "What paths are people taking through this journey?". To monitor journey progress while a journey is running, you can see the progress of customers through the journey in real time. For further analysis, you can also export the list of people who take each path or action in the journey.

## Analyze customer inflow and exit at every step in a journey (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

Improved journey analytics increase confidence in the processing of every step in your journey through improved metrics and the increased ability to export data. Individual journey analytics now communicate the number of people who entered each journey step, the number of people who exit the journey at each step, and why people exit the journey.

For example, journeys that use exit or exclusion segments show why there are fewer customers who started your journey than were in your audience segment. Additionally, you can see the list of customers who entered and exited each step in the journey, and export lists of up to 50,000 people for further analysis.

> [!NOTE]
> This feature is under active development. In the future, additional analytics capabilities will be added and capabilities for each journey action. At this time, the Entry action step has been updated. The Entry step now shows which people exited the journey and why. These same capabilities will be brought to every action in the journey between now and when this feature becomes generally available.

### Enable tile entry and exit analytics preview

To use the journey copilot, an administrator needs to enable the feature switch. To enable the switch:

1. Go to **Settings** > **Overview** > **Feature switches** > **Journey**.
1. Enable the "Tile entry and drop-off analytics (preview)" feature switch toggle, then select **Save** in the upper right.

    :::image type="content" source="media/real-time-tile-analytics-feature-switch.png" alt-text="Enable entry and exit analytics feature":::

> [!NOTE]
> The tile entry and exit analytics require the May 2024 update of Customer Insights - Journeys to be installed. The preview feature will be made available to all customers before the end of May 2024.

> [!IMPORTANT]
> Journeys published after the preview feature switch is turned on will have the new journey analytics metrics enabled by this feature. Journeys published before the feature is enabled will not have the additional metrics.

## Understanding journey analytics

> [!IMPORTANT]
> This section applies to the new journey analytics enabled by the tile entry and exit analytics preview.

After a journey is published, analytics are available for each action (step or tile) of the journey. To see the analytics, open a published journey. Analytics are available for journeys that have *Live*, *Completed*, *Completing*, and *Stopped* statuses. Analytics are available for every action in the journey.

### Journey flow metrics

The following metrics are available on every tile in a journey:

* **Inflow** counts the total number of people who entered this journey step.
    * For the entry step in the journey, the **Inflow** counts the number of people who entered the journey from a segment or trigger. For a segment-based journey, it's the total size of the audience segment. For a trigger-based journey, it's the total number of people who were triggered to start this journey. **Inflow** also includes people who are later excluded from the journey due to journey configuration such as trigger filters or exit segments.
    * For all other journey steps, the **Inflow** counts the people who entered this step in the journey from the previous step.
    * **Inflow** counts a person every time they enter this journey step, including people who enter the journey step multiple times (for journeys that are configured to allow that to happen).
* **Processing** counts the number of people who entered this step in the journey but haven't yet continued to the next step in the journey or exited the journey due to processing at this step. When a journey is in the **Completed** status, all tiles should have no people in **Processing** at any step.
* **Processed** counts the number of people who were evaluated by this step and continued on to the next step in the journey.
* **Exit** counts the people who exited the journey while in this step. These people won't be evaluated by any later step in the journey. A person can exit a journey due to many reasons, such as:
    * *Exit or suppression member*: The person was one of the exit or suppression segments configured by the journey entry or exit conditions.
    * *Repeat journey entry blocked by configuration*: An ongoing journey such as a trigger-based journey was configured not to allow the same person to enter the journey more than once. Each time the same person tries to start the journey another time, they'll exit the journey immediately and be counted here.
    * *Unmet trigger condition*: For a trigger-based journey that has conditions configured, this exit reason counts the number of people who didn't meet the trigger condition.
    * *Inactive or missing audience member*: The person's entity in Dataverse can't be found or is marked as inactive.
    * *Different business unit*: If business unit scoping is enabled, the journey prevents Dataverse entities that don't have the same business unit as the journey to start the journey.

> [!TIP]
> Because journey analytics are real-time and updated as a journey is running, there are situations where the metrics may not appear consistent temporarily. You should expect that the metrics will reach a steady state, final value once the processing of the journey step has completed. When that happens, you should expect that **Inflow** = (**Processing** + **Processed** + **Exit**).

### Entry analytics

The first step in every journey is the *Entry* action, which represents the actions around processing the audience segment or triggers at the start of the customer journey.

For example, immediately after a segment based journey starts the system starts to process each member of the segment. If you view a journey while the system is working on processing the audience segment, you see the number of people in the segment (**Inflow**), the number of people who are in the segment that haven't yet moved to the next step in the journey (**Processing**), and the number of people who completed this step in the journey and sent to the next step (**Processed**).

In the screenshot below, you can see that there are 36 people in the audience segment that have entered this journey. Five of those people in the segment haven't yet moved on to the next step in the journey. Thirty-one people have been analyzed and have moved on to the next step in the journey. And nobody exited the journey due to the processing at this step in the journey.

:::image type="content" source="media/real-time-tile-analytics-entry-tile-in-progress.png" alt-text="Entry action analytics example":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]