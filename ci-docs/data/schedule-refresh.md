---
title: "Schedule system refresh"
description: "Schedule the time when the system should be refreshed"
ms.date: 02/12/2024
ms.topic: how-to
author: NimrodMagen
ms.author: nimagen
ms.reviewer: v-wendysmith
searchScope: 
  - ci-system-schedule
  - customerInsights
---

# Schedule system refresh

Schedule automatic refreshes of all your [ingested data sources](data-sources.md). Automatic refreshes help ensure that updates from your data sources are reflected in your unified customer profiles.

## Set system refresh schedule

1. Go to **Settings** > **System** and select the **Schedule** tab.

   :::image type="content" source="media/schedule_refresh.svg" alt-text="Schedule refresh tab from System page.":::

1. The default state for the scheduled refresh is **Off**. To enable scheduled refreshes, change the toggle at the top of the screen to **On**.

1. Choose between **Weekly** and **Daily** refreshes. If you intend to schedule weekly refreshes, select one or more days on which you want to run the refresh.

1. Set your **Time zone**, then use the **Time** dropdown to set your refresh timing. If you'd like to schedule multiple refreshes in a single day, select **Add another time**. You can add up to four refreshes.

1. Select **Save** to apply your changes.

> [!CAUTION]
> If you change an existing system refresh date, it might impact custom schedules for segments and measures causing them to not run as scheduled. Check the schedules for both [segments](segments-schedule.md) and [measures](measures-schedule.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
