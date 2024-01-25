---
title: "Schedule measures"
description: "How to create custom schedules for measures."
ms.date: 11/28/2022
ms.topic: how-to
author: v-wendysmith
ms.author: wameng
ms.reviewer: v-wendysmith
---

# Schedule measures

Measures can be refreshed on the [scheduled system refresh](schedule-refresh.md), weekly, monthly, or refreshed manually on demand. You might want to schedule last season's measures or measures that don't change often on a slower cadence such as monthly to help your most needed measures refresh faster. The default is every scheduled system refresh.

## Prerequisites for automatic refresh of a measure

- A [system refresh must be scheduled](schedule-refresh.md). Daily system refresh is recommended.
- The custom schedule for a measure must align with the system refresh schedule.
  > [!CAUTION]
  > If the system refresh date is changed after you have set custom schedules for your measures so that the dates no longer align, your measures won't refresh as scheduled until their custom schedules align with the new system refresh schedule. Change your measures custom schedules to align with the new system refresh schedule or refresh the measures manually.

## Create custom refresh schedules for measures

Define refresh schedules for one or more measures. The currently defined schedule is listed in the **Schedule** column of the measure list.

1. Go to **Measures**.

1. Select the measures you want to schedule.

1. Select **Schedule**.

1. In the **Schedule** pane, set the **Schedule run** to **On** to run the measure automatically. Set it to **Off** to refresh it manually.

1. For automatically refreshed measures, select **Recurrence** and the details for it.

1. When defining the schedule for several measures, make a selection under **Keep or override schedules**:
   - **Keep individual schedules**: Keep the previously defined schedule for the selected measures.
   - **Define new schedule for all selected measures**: Override the existing schedules of the selected measures.

   :::image type="content" source="media/measures-schedule.png" alt-text="Selected measure with Schedule pane.":::

1. Select **Save** and then confirm the change. The measures are refreshed on the scheduled date during the system refresh.

[!INCLUDE [footer-include](includes/footer-banner.md)]
