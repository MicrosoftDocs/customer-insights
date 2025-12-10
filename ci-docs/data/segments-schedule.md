---
title: "Schedule segments"
description: "How to create custom schedules for segments."
ms.date: 03/20/2023
ms.topic: how-to
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Schedule segments

Segments can be refreshed based on the [scheduled system refresh](schedule-refresh.md), weekly, monthly, or refreshed manually on demand. The default is every scheduled system refresh. You might want to schedule last season's segments or segments that don't change often on a slower cadence such as monthly to help your most needed segments refresh faster.

## Prerequisites for automatic refresh of a segment

- A [system refresh must be scheduled](schedule-refresh.md). Daily system refresh is recommended.
- The segment must have the type **Dynamic** or **Expansion**. **Static** segments *won't* be refreshed automatically.
- The custom schedule for a segment must align with the system refresh schedule.
  > [!CAUTION]
  > If the system refresh date is changed after you have set custom schedules for your segments so that the dates no longer align, your segments won't refresh as scheduled until their custom schedules align with the new system refresh schedule. Change your segments custom schedules to align with the new system refresh schedule or refresh the segments manually.

## Create custom refresh schedules for segments

Define refresh schedules for one or more segments. The currently defined schedule is listed in the **Schedule** column of the segment list.

1. Go to **Segments**.

1. Select the segments you want to schedule.

1. Select **Schedule**.

1. In the **Schedule** pane, set the **Schedule run** to **On** to run the segment automatically. Set it to **Off** to refresh it manually.

1. For automatically refreshed segments, select **Recurrence** and the details for it.

1. When defining the schedule for several segments, make a selection under **Keep or override schedules**:
   - **Keep individual schedules**: Keep the previously defined schedule for the selected segments.
   - **Define new schedule for all selected segments**: Override the existing schedules of the selected segments.

   :::image type="content" source="media/segments-schedule.png" alt-text="Selected segments with Schedule pane."lightbox="media/segments-schedule.png":::

1. Select **Save** and then confirm the change. The segments are refreshed on the scheduled date during the system refresh.

[!INCLUDE [footer-include](includes/footer-banner.md)]
