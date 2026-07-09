---
title: Schedule segments
description: Schedule segments to refresh weekly, monthly, or on demand. Create custom refresh schedules and speed up your most needed segments.
ms.date: 07/08/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Schedule segments

You can refresh segments based on the [scheduled system refresh](schedule-refresh.md), weekly, monthly, or refresh them manually on demand. The default is every scheduled system refresh. To help your most needed segments refresh faster, schedule last season's segments or segments that don't change often on a slower cadence such as monthly.

## Prerequisites for automatic refresh of a segment

- A [system refresh must be scheduled](schedule-refresh.md). Daily system refresh is recommended.
- The segment must have the type **Dynamic** or **Expansion**. **Static** segments *aren't* refreshed automatically.
- The custom schedule for a segment must align with the system refresh schedule.
  > [!CAUTION]
  > If someone changes the system refresh date after you set custom schedules for your segments so that the dates no longer align, your segments don't refresh as scheduled until their custom schedules align with the new system refresh schedule. Change your segments custom schedules to align with the new system refresh schedule or refresh the segments manually.

## Create custom refresh schedules for segments

Define refresh schedules for one or more segments. The currently defined schedule appears in the **Schedule** column of the segment list.

1. Go to **Insights** > **Segments**.

1. Select the segments you want to schedule.

1. Select **Schedule**.

1. In the **Schedule** pane, set the **Schedule run** to **On** to run the segment automatically. Set it to **Off** to refresh it manually.

1. For automatically refreshed segments, select **Recurrence** and enter the details.

1. When defining the schedule for several segments, make a selection under **Keep or override schedules**:
   - **Keep individual schedules**: Keep the previously defined schedule for the selected segments.
   - **Define new schedule for all selected segments**: Override the existing schedules of the selected segments.

   :::image type="content" source="media/segments-schedule.png" alt-text="Screenshot of selected segments with the Schedule pane." lightbox="media/segments-schedule.png":::

1. Select **Save** and then confirm the change. The system refreshes the segments on the scheduled date during the system refresh.

[!INCLUDE [footer-include](includes/footer-banner.md)]
