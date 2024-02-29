---
title: FAQ for Environment status summary (preview)
description: This FAQ provides information about the AI technology used in the environment status summary. It includes key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 10/11/2023
ms.custom: 
  - responsible-ai-faqs
ms.topic: article
author: m-hartmann
ms.author: mhart
ms.reviewer: wameng
ms.collection: bap-ai-copilot 
---

# FAQ for Environment status summary (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

These frequently asked questions (FAQ) describe the AI impact of Dynamics 365 Customer Insights - Data environment status summary feature.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## What is Environment status summary?

This AI-powered feature is designed to summarize business impacting jobs in the system and surface the root failure jobs, if any, so you can quickly investigate the issue. This feature helps eliminate the need to review hundreds of jobs to identify if your environment is processing normally. The Environment status summary uses Azure OpenAI and passes information about the job statuses, as well as other information like job names, to allow the model to create a summary. To learn more about how Azure OpenAI handles your data, see [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy).

## What are the feature’s capabilities?

The Environment status summary detects if a key job has been skipped or failed, based on job priority order. A link to the job is provided so you can quickly access the issue.

## What is the feature’s intended use?

The intention is to aid administrators in determining the status of their Customer Insights - Data environment in less time and with less manual effort.

## How was Environment status summary evaluated? What metrics are used to measure performance?

This feature has only been evaluated in English at this time.

The Environment status summary is evaluated from dimensions of accuracy of result and performance of generation. In addition, it's evaluated with embedded monitoring for Responsible AI. Specifically, this feature has been tested with an array of scenarios to ensure it captures and mitigates accordingly, including inappropriate language used, malicious intention of jail break, and data fabrication.

## What are the limitations of Environment status summary? How can users minimize the impact of the Environment status summary limitations when using the system?

The feature reviews jobs in the following order, if they're configured:

- Exports
- Segments used in Customer Journey Orchestrator
- Dataverse hydration jobs
- Merge in data unification

The feature reports only on these jobs and one at a time based on the priority order. For example, if exports are configured, then the feature only identifies if there's an issue with an export.

## What are the supported geographies and languages?

For more information, see [Copilot International Availability report](https://dynamics.microsoft.com/availability-reports/copilotreport/).

## What operational factors and settings allow for effective and responsible use of the feature?

- On the Environment status summary, users are reminded that AI-generated content can be inaccurate.
- Users should be mindful when adding data sources, creating segments, measures, and other insights that the names are used in processing the jobs. Users should use responsible, appropriate names.

## See also

- [Environment status summary (preview)](system.md#environment-status-summary-preview)

[!INCLUDE [footer-include](includes/footer-banner.md)]
