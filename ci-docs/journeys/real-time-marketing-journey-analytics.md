---
title: Real-time tile analytics in journeys
description: Real-time journey analytics help you track customer movement at every step, showing who enters, exits, and why. Start analyzing your journeys now.
ms.date: 07/11/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:07/11/2025
---

# Real-time tile analytics in journeys

It’s critical to understand exactly what happened to each customer who enters and exits your real-time journeys. The analytics provided by each journey answer questions like, "How many people started this journey?", "How many people received email from this journey?", and "What paths are people taking through this journey?". To monitor journey progress while a journey is running, you can see the progress of customers through the journey in real time. For further analysis, you can also export the list of people who take each path or action in the journey.

## Analyze customer inflow and exit at every step in a journey

Improved journey analytics help you track every step in your journey with better metrics and more ways to export data. Individual journey analytics show how many people enter each step, how many exit at each step, and why they exit.

For example, journeys that use exit or exclusion segments show why fewer customers start your journey than are in your audience segment. You also see the list of customers who enter and exit each step, and you can export lists of up to 50,000 people for further analysis.

> [!NOTE]
> This feature is under active development. In the future, additional analytics capabilities will be added and capabilities for each journey action. At this time, the Entry action step has been updated. The Entry step now shows which people exited the journey and why. These same capabilities will be brought to every action in the journey between now and when this feature becomes generally available.

### Enable tile entry and exit analytics

To use the journey copilot, an admin needs to turn on the feature switch. To turn on the switch:

1. Go to **Settings** > **Overview** > **Feature switches** > **Journey**.
1. Turn on the "Tile entry and drop-off analytics" feature switch toggle, then select **Save** in the upper right.

    :::image type="content" source="media/real-time-tile-analytics-feature-switch.png" alt-text="Screenshot of the feature switch to enable entry and exit analytics in the settings menu.":::

> [!IMPORTANT]
> Journeys published after the feature goes live have the new journey analytics metrics. Journeys published before the feature is turned on don't have the additional metrics.

## Understanding journey analytics

> [!IMPORTANT]
> This section applies to the new journey analytics enabled by the tile entry and exit analytics.

After you publish a journey, analytics are available for each action (step or tile) in the journey. To see the analytics, open a published journey. Analytics are available for journeys with *Live*, *Completed*, *Completing*, and *Stopped* statuses. Analytics are available for every action in the journey.

### Journey flow metrics

Each tile in a journey shows the following metrics:

* **Inflow** counts the total number of people who enter this journey step.
    * For the entry step in the journey, **Inflow** counts the number of people who enter the journey from a segment or trigger. For a segment-based journey, it's the total size of the audience segment. For a trigger-based journey, it's the total number of people who are triggered to start this journey. **Inflow** also includes people who are later excluded from the journey because of journey configuration such as trigger filters or exit segments.
    * For all other journey steps, **Inflow** counts the people who enter this step in the journey from the previous step.
    * **Inflow** counts a person every time they enter this journey step, including people who enter the journey step multiple times (for journeys that are set up to allow that to happen).
* **Processing** counts the number of people who enter this step in the journey but haven't yet continued to the next step in the journey or exited the journey because of processing at this step. When a journey is in the **Completed** status, all tiles shouldn't have any people in **Processing** at any step.
* **Processed** counts the number of people who are evaluated by this step and continue to the next step in the journey.
* **Exit** counts the people who exit the journey while in this step. These people aren't evaluated by any later step in the journey. A person can exit a journey for many reasons, such as:
    * *Exit or suppression member*: The person is one of the exit or suppression segments set up by the journey entry or exit conditions.
    * *Repeat journey entry blocked by configuration*: An ongoing journey such as a trigger-based journey is set up not to let the same person enter the journey more than once. Each time the same person tries to start the journey again, they exit the journey immediately and are counted here.
    * *Unmet trigger condition*: For a trigger-based journey that has conditions set up, this exit reason counts the number of people who don't meet the trigger condition.
    * *Inactive or missing audience member*: The person's entity in Dataverse can't be found or is marked as inactive.
    * *Different business unit*: If business unit scoping is enabled, the journey prevents Dataverse entities that don't have the same business unit as the journey from starting the journey.

> [!TIP]
> Because journey analytics are real-time and update as a journey runs, sometimes the metrics can appear inconsistent temporarily. The metrics reach a steady, final value once processing of the journey step finishes. At that point, **Inflow** = (**Processing** + **Processed** + **Exit**).

### Entry analytics

The first step in every journey is the *Entry* action, which represents processing the audience segment or triggers at the start of the customer journey.

For example, immediately after a segment-based journey starts, the system processes each member of the segment. If you view a journey while the system processes the audience segment, you see the number of people in the segment (**Inflow**), the number of people in the segment who haven't yet moved to the next step in the journey (**Processing**), and the number of people who finish this step in the journey and move to the next step (**Processed**).

In the screenshot, you see that 36 people in the audience segment enter this journey. Five of those people haven't yet moved to the next step in the journey. Thirty-one people are analyzed and move to the next step in the journey. Nobody exits the journey because of processing at this step in the journey.

:::image type="content" source="media/real-time-tile-analytics-entry-tile-in-progress.png" alt-text="Screenshot of entry action analytics showing inflow, processing, and processed counts for a journey step.":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]