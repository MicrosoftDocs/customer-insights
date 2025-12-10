---
title: "View system configuration"
description: "Learn about system settings in Dynamics 365 Customer Insights - Data."
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: alfergus
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# View system configuration

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

> [!IMPORTANT]
> Copilot features in Customer Insights - Data are only available in environments in the United States and Switzerland regions. These features may become available in additional regions in future releases.

View system information and system status.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## View system information

View the environment display name, ID, region, type and session ID.

1. Go to **Settings** > **System** and select the **About** tab.

1. To view the language and country/region, select the **General** tab.

### Update preferred language or country/region

Dynamics 365 Customer Insights - Data [supports many languages](/dynamics365/get-started/availability). The app uses your language preference to display elements like the menu, label text, and system messages in your preferred language.

Imported data and information you entered manually aren't translated.

1. Go to **Settings** > **System** and select the **General** tab.

1. To change your preferred language, choose a **Language** from the dropdown.

1. To change your preferred formatting for dates, time, and numbers, use the **Country/Region format** dropdown. A formatting preview is displayed. The system automatically suggests a selection when you choose a new language.

1. Select **Save**.

## View system status

Track the progress of tasks, data ingestion, data exports, and several other important product processes. Review the information to ensure the completeness of your active tasks and processes.

1. Go to **Settings** > **System** and select the **Status** tab.

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
|Refreshing    |Task or process is in progress. To cancel this operation, select **Refreshing** and **Cancel job**. Stopping the refresh of a task or process reverts it to its last refresh state.       |
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
|Data prep report   |Needs a table to run on. Data source tables depend on ingestion. Enriched tables depends on enrichments. The Customer table depends on merge.  |
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
|User  |Runs manually (single time refresh). Depends on tables.  |

Select the status of a process to see the progress details of the entire job it was in. The refresh processes can help to understand what you can do to address a **Skipped** or **Queued** task or process.

## Environment status summary (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

The Environment status summary is designed to help you quickly understand the status of your environment based on the business impact of what you’ve configured. The summary reviews jobs in the following order:

- If exports are configured, the system summarizes export job statuses.
- If exports aren't configured, the system summarizes segment job statuses for segments configured for Customer Journey Orchestrator.
- If you haven't configured any segments for Customer Journey Orchestrator, the system summarizes job statuses for jobs that put data into Dataverse.
- If you haven’t configured any features that move data into Dataverse, the system reviews the unification (merge) job to help indicate if your unification is running normally.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

### Prerequisites

- [Enable Copilot features powered by Azure OpenAI](copilot-global-consent.md) setting turned **On**. Default is **On**.
- Environment is in a supported geography and uses a supported language.

### View the Environment status summary

Use the summary to help you determine if your environment is running normally or if there's a problem. If the system detects one of the jobs has been skipped or failed, the summary shows the earliest dependency area for the job, so you know where to investigate first and get things running again quickly. Select the link to go to the respective area and investigate the issue.

- Go to **Settings** > **System**.

  :::image type="content" source="media/environment-status-summary.svg" alt-text="Screenshot of Environment status summary dialog box.":::

  - To research the skipped or failed job, select the link.
  - To copy the summary to your clipboard, select **Copy**.
  - To refresh the summary if you’re waiting for a job to finish, select **Refresh**.
  - To provide your feedback, select the thumbs up or thumbs down icons.

[!INCLUDE [copilot-availability](includes/copilot-availability.md)]

### Next steps

- [Responsible AI FAQs for the Environment status summary](faqs-environment-status.md)
- [Responsible AI FAQs for Customer Insights - Data](responsible-ai-overview.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
