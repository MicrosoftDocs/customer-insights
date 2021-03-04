---
title: "System configuration in audience insights"
description: "Learn about system settings in Dynamics 365 Customer Insights audience insights capability."
ms.date: 02/12/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: nimagen
manager: shellyha
---

# System configuration

The **System** page includes the following tabs:
- [Status](#status-tab)
- [Schedule](#schedule-tab)
- [API usage](#api-usage-tab)
- [About](#about-tab)
- [General](#general-tab)

> [!div class="mx-imgBorder"]
> ![System page](media/system-tabs.png "System page")

## Status tab

The **Status tab** lets you track the progress of data ingestion, data exports, and several other important product processes. Review the information on this tab to ensure the completeness of active processes.

This tab includes tables with status and processing information for various processes. Each table tracks the **Name** of the task and its corresponding entity, the **Status** of its most recent run, and when it was **Last updated**.

View the details of the tasks' last several runs by selecting its name.

### Status types

There are six types of status for tasks. The following status types also show on the *Match*, *Merge*, *Data sources*, *Segments*, *Measures*, *Enrichment*, *Activities*, and *Predictions* pages:

- **Processing:** Task is in progress. The status can change to Successful or Failure.
- **Successful:** Task completed successfully.
- **Skipped:** Task got skipped. One or more of the downstream processes this task depends on are failing or got skipped.
- **Failure:** Processing  of the task has failed.
- **Canceled:** Processing was canceled by the user before it finished.
- **Queued:** Processing is queued and will start once all the upstream tasks are completed. For more information, see [Refresh policies](#refresh-policies).

### Refresh policies

This list shows the refresh policies for each of the main processes:

- **Data sources:** Runs according to the [configured schedule](#schedule-tab). Doesn't depend on any other process. Match depends on the successful completion of this process.
- **Match:** Runs according to the [configured schedule](#schedule-tab). Depends on the processing of the data sources used in the match definition. Merge depends on the successful completion of this process.
- **Merge**: Runs according to the [configured schedule](#schedule-tab). Depends on the completion of the match process. Segments, measures, enrichment, search, activities, predictions, and data preparation depend on the successful completion of this process.
- **Segments**: Runs manually (single time refresh) and according to the [configured schedule](#schedule-tab). Depends on Merge. Insights depend on its processing.
- **Measures**: Runs manually (single time refresh) and according to the [configured schedule](#schedule-tab). Depends on Merge.
- **Activities**: Runs manually (single time refresh) and according to the [configured schedule](#schedule-tab). Depends on Merge.
- **Enrichment**: Runs manually (single time refresh) and according to the [configured schedule](#schedule-tab). Depends on Merge.
- **Search**: Runs manually (single time refresh) and according to the [configured schedule](#schedule-tab). Depends on Merge.
- **Data preparation**: Runs according to the [configured schedule](#schedule-tab). Depends on Merge.
- **Insights**: Runs manually (single time refresh) and according to the [configured schedule](#schedule-tab). Depends on Segments.

Select the status of a task to see the progress details of the entire job it was in. The refresh policies above can help to understand what you can do to address a **Skipped** or **Queued** task.

## Schedule tab

Use the **Schedule** tab to schedule automatic refreshes of all your [ingested data sources](data-sources.md). Automatic refreshes help ensure that updates from your data sources are reflected in your unified customer profiles.

1. In audience insights, go to **Admin** > **System** and select the **Schedule** tab.

2. The default state for the scheduled refresh is **Off**. To enable scheduled refreshes, change the toggle at the top of the screen to **On**.

3. Choose between **Weekly** (default) and **Daily** refreshes. If you intend to schedule weekly refreshes, select one or more days on which you want to run the refresh.

4. Set your **Time zone**, then use the **Time** dropdown to set your refresh timing. When you're finished, select **Set**. If you'd like to schedule multiple refreshes in a single day, select **Add another time**.

5. Select **Save** to apply your changes.

## About tab

The **About** tab contains your organization's **Display name**, the active **Environment ID**, the **Region**, and your **Session ID**. If you have more than one work environment, you should give each an easily identifiable display name.

## General tab

There are two options on the **General** tab, **Language** and **Country/Region format**.

The app [supports a number of languages](supported-languages.md). To change your preferred language, choose a **Language** from the dropdown.

To change your preferred formatting for dates, time, and numbers, use the **Country/Region format** dropdown. A formatting preview is displayed under this field. The system will automatically suggest a selection when you choose a new language.

Select **Save** to confirm your selections.

## API usage tab

Find details about the real-time API usage and see which events happened in a given time frame. You choose the time frame in the **Select a time frame** drop-down menu. 

The **API usage** contains three sections: 
- **API calls** - a chart that visualizes the aggregated number of calls to the API in the selected time frame.

- **Data transfer** - a chart that shows the amount of data that was transferred through the API in the selected time frame.

-  **Operations** - a table with rows for each available API operation and details about the usage of the operations. You can select an operation name to go to [the API reference](https://developer.ci.ai.dynamics.com/api-details#api=CustomerInsights&operation=Get-all-instances).

   Operations which use [real-time data ingestion](real-time-data-ingestion.md) contain a button with a binocular symbol to view real-time API usage. Select the button to open a side pane containing usage details for the real-time API usage in the current environment.   
   Use the **Group by** box in the **Real-time API usage** pane to choose how to best present your real-time interactions. You can group the data by API method, entity qualified name (ingested entity), created by (source of the event), result (success or failure) or error codes. The data is available as a history chart and as a table.


[!INCLUDE[footer-include](../includes/footer-banner.md)]