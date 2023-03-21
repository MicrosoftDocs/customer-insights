---
title: "View system configuration"
description: "Learn about system settings in Dynamics 365 Customer Insights."
ms.date: 03/20/2023
ms.topic: conceptual
author: NimrodMagen
ms.author: nimagen
ms.reviewer: mhart
ms.custom: bap-template
searchScope: 
  - ci-system-status
  - ci-system-about
  - ci-system-general
  - ci-system-api-usage
  - customerInsights
---

# View system configuration

View system information and system status.

## View system information

View the environment display name, ID, region, type and session ID.

1. Go to **Admin** > **System** and select the **About** tab.

1. To view the language and country/region, select the **General** tab.

### Update preferred language or country/region

Customer Insights [supports many languages](/dynamics365/get-started/availability). The app uses your language preference to display elements like the menu, label text, and system messages in your preferred language.

Imported data and information you entered manually aren't translated.

1. Go to **Admin** > **System** and select the **General** tab.

1. To change your preferred language, choose a **Language** from the dropdown.

1. To change your preferred formatting for dates, time, and numbers, use the **Country/Region format** dropdown. A formatting preview is displayed. The system automatically suggests a selection when you choose a new language.

1. Select **Save**.

## View system status

Track the progress of tasks, data ingestion, data exports, and several other important product processes. Review the information to ensure the completeness of your active tasks and processes.

1. Go to **Admin** > **System** and select the **Status** tab.

   Status and processing information for various processes display. View the **Name** of the task, the **Status** of its most recent run, and when it was **Last updated**.

1. To view the details of the last several runs, select the task or process name.

1. To view progress details for a task, select the status. The **Progress details** pane displays.

   :::image type="content" source="media/system-progress-details.png" alt-text="System progress details pane":::

1. To view progress details for all tasks, select **Entire workflow**.

### Status definitions

The system uses the following statuses for tasks and processes:

|Status  |Definition  |
|---------|---------|
|Canceled |Task or process was canceled by the user before it finished.   |
|Failed   |Task or process ran into errors.         |
|Failure  |Task or process has failed.  |
|Not started   |Data source has no data ingested yet or the task is still in draft mode.         |
|Processing  |Task or process is in progress.  |
|Refreshing    |Task or process is in progress. To cancel this operation, select **Refreshing** and **Cancel job**. Stopping the refresh of a task or process will revert it to its last refresh state.       |
|Skipped  |Task or process got skipped. One or more of the downstream processes this task depends on are failing or got skipped.|
|Successful  |Task or process completed successfully. For data sources, indicates the data has been successfully ingested if a time is mentioned in the **Refreshed** column.|
|Queued | Processing is queued and will start once all the upstream tasks and processes are completed. For more information, see [Refresh processes](#refresh-processes).|

### Refresh processes

Refresh for tasks and processes is run according to the [configured schedule](schedule-refresh.md).

|Process  |Description  |
|---------|---------|
|Activity  |Runs manually (single time refresh). Depends on merge process. Insights depend on its processing.|
|Analysis linking |Runs manually (single time refresh). Depends on segments.  |
|Analysis preparation |Runs manually (single time refresh). Depends on segments.  |
|Data preparation   |Needs an entity to run on. Data source entities depend on ingestion. Enriched entities depends on enrichments. The Customer entity depends on merge.  |
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


[!INCLUDE [footer-include](includes/footer-banner.md)]
