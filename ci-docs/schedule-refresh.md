---
title: "Schedule system refresh"
description: "Schedule the time when the system should be refreshed"
ms.date: 11/16/2022

ms.subservice: audience-insights
ms.topic: conceptual
author: NimrodMagen
ms.author: nimagen
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-system-schedule
  - customerInsights
---

# Schedule system refresh

Schedule automatic refreshes of all your [ingested data sources](data-sources.md). Automatic refreshes help ensure that updates from your data sources are reflected in your unified customer profiles.

> [!NOTE]
> Power Query data sources managed by you refresh on their own schedules. To schedule refresh of these Power Query data sources, configure refresh settings on that specific data source from the **Data sources** page. Align the timing with the upstream data refresh schedule so that refreshes do not all occur at once.
> :::image type="content" source="media/PPDF-edit-refresh.png" alt-text="Power Platform Dataflow refresh settings.":::

## Set system refresh schedule

1. Go to **Admin** > **System** and select the **Schedule** tab.

   :::image type="content" source="media/schedule_refresh.png" alt-text="Schedule refresh tab from System page.":::

1. The default state for the scheduled refresh is **Off**. To enable scheduled refreshes, change the toggle at the top of the screen to **On**.

1. Choose between **Weekly** (default) and **Daily** refreshes. If you intend to schedule weekly refreshes, select one or more days on which you want to run the refresh.

1. Set your **Time zone**, then use the **Time** dropdown to set your refresh timing. If you'd like to schedule multiple refreshes in a single day, select **Add another time**. You can add up to four refreshes.

1. Select **Save** to apply your changes.

> [!CAUTION]
> If you change an existing system refresh date, it might impact custom schedules for segments and measures causing them to not run. Check the schedules for both [segments](segments.md#schedule-segments) and [measures](measures.md#schedule-measures).

[!INCLUDE [footer-include](includes/footer-banner.md)]
