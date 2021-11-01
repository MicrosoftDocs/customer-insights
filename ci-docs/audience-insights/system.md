---
title: "System configuration in audience insights"
description: "Learn about system settings in Dynamics 365 Customer Insights audience insights capability."
ms.date: 11/01/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: NimrodMagen
ms.author: nimagen
ms.reviewer: mhart
manager: shellyha
---

# System configuration

To access system configurations in audience insights, from the left navigation bar select **Admin** > **System** to view a list of system tasks and processes.

The **System** page includes the following tabs:
- [Status](#status-tab)
- [Schedule](#schedule-tab)
- [API usage](#api-usage-tab)
- [About](#about-tab)
- [General](#general-tab)
- [Security](#security-tab)

:::image type="content" source="media/system-tabs.png" alt-text="Settings tabs on the system page.":::

## Status tab

The **Status tab** lets you track the progress of tasks, data ingestion, data exports, and several other important product processes. Review the information on this tab to ensure the completeness of you active tasks and processes.

This tab includes tables with status and processing information for various processes. Each table tracks the **Name** of the task and its corresponding entity, the **Status** of its most recent run, and when it was **Last updated**. You can view the details of the last several runs by selecting the task or process name. 

Click the status next to the task or process in the **Status** column to open the **Progress details** pane.

   :::image type="content" source="media/system-progress-details.png" alt-text="System progress details pane":::

### Status definitions

These are the current statuses for tasks and processes:

|Status  |Definition  |
|---------|---------|
|Canceled |Processing was canceled by the user before it finished.   |
|Failed   |Data ingestion ran into errors.         |
|Failure  |Processing has failed.  |
|Not started   |The data source has no data ingested yet or still in draft mode.         |
|Processing  |Task or process is in progress.  |
|Refreshing    |Data ingestion is in progress. You can cancel this operation by selecting **Stop refreshing** in the **Actions** column. Stopping the refresh of a data source will revert it to its last refresh state.       |
|Skipped  |Task or process got skipped. One or more of the downstream processes this task depends on are failing or got skipped.|
|Successful  |Task or process completed successfully. For data sources, indicates the data has been successfully ingested if a time is mentioned in the **Refreshed** column.|
|Queued | Processing is queued and will start once all the upstream tasks and processes are completed. For more information, see [Refresh processes](#refresh-processes).|

### Refresh processes

Refresh for tasks and processes is run according to the [configured schedule](#schedule-tab). 

|Process  |Description  |
|---------|---------|
|Activity  |Runs manually (single time refresh). Depends on merge process. Insights depend on its processing.|
|Analysis linking |Runs manually (single time refresh). Depends on segments.  |
|Analysis preparation |Runs manually (single time refresh). Depends on segments.  |
|Data preparation   |Depends on merge.   |
|Data sources   |Doesn't depend on any other process. Match depends on the successful completion of this process.  |
|Enrichments   |Runs manually (single time refresh). Depends on merge process. |
|Exports destinations |Runs manually (single time refresh). Depends on segments.  |
|Insights |Runs manually (single time refresh). Depends on segments.  |
|Intelligence   |Depends on merge.   |
|Match |Depends on the processing of the data sources used in the match definition.      |
|Measures  |Runs manually (single time refresh). Depends on merge process.  |
|Merge   |Depends on the completion of the match process. Segments, measures, enrichment, search, activities, predictions, and data preparation depend on the successful completion of this process.   |
|Profiles   |Runs manually (single time refresh). Depends on merge process. |
|Search   |Runs manually (single time refresh). Depends on merge process. |
|Segments  |Runs manually (single time refresh). Depends on merge process. Insights depend on its processing.|
|System   |Depends on the completion of the match process. Segments, measures, enrichment, search, activities, predictions, and data preparation depend on the successful completion of this process.   |
|User  |Runs manually (single time refresh). Depends on entities.  |

Select the status of a process to see the progress details of the entire job it was in. The refresh processes above can help to understand what you can do to address a **Skipped** or **Queued** task or process.

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

You can change the language and the country/region format on the **General** tab.

Customer Insights [supports a number of languages](/dynamics365/get-started/availability). The app uses your language preference to display elements like the menu, label text, and system messages in your preferred language.

Imported data and information you entered manually aren't translated.

### Update the settings

To change your preferred language, choose a **Language** from the dropdown.

To change your preferred formatting for dates, time, and numbers, use the **Country/Region format** dropdown. A formatting preview is displayed under this field. The system will automatically suggest a selection when you choose a new language.

Select **Save** to confirm your selections.

## API usage tab

Find details about the real-time API usage and see which events happened in a given time frame. You choose the time frame in the **Select a time frame** dropdown menu. 

The **API usage** contains three sections: 
- **API calls** - a chart that visualizes the aggregated number of calls to the API in the selected time frame.

- **Data transfer** - a chart that shows the amount of data that was transferred through the API in the selected time frame.

-  **Operations** - a table with rows for each available API operation and details about the usage of the operations. You can select an operation name to go to [the API reference](https://developer.ci.ai.dynamics.com/api-details#api=CustomerInsights&operation=Get-all-instances).

   Operations which use [real-time data ingestion](real-time-data-ingestion.md) contain a button with a binocular symbol to view real-time API usage. Select the button to open a side pane containing usage details for the real-time API usage in the current environment.   
   Use the **Group by** box in the **Real-time API usage** pane to choose how to best present your real-time interactions. You can group the data by API method, entity qualified name (ingested entity), created by (source of the event), result (success or failure) or error codes. The data is available as a history chart and as a table.

## Security tab

The **Security** tab lets you link and manage your own [Azure key vault](/azure/key-vault/general/basic-concepts) to the environment.
The dedicated key vault can be used to stage and use secrets in an organization's compliance boundary. Audience insights can use the secrets in Azure Key Vault to [set up connections](connections.md) to third-party systems.

For more information, see [Bring your own Azure key vault](use-azure-key-vault.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]
