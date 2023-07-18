---
title: FAQ for Environment status summary
description: This FAQ provides information about the AI technology used in Dynamics 365 Customer Insights Environment status summary, along with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 07/17/2023
ms.custom: 
  - responsible-ai-faqs
ms.topic: article
author: m-hartmann
ms.author: mhart
ms.reviewer: wameng
---

# FAQ for Environment status summary (preview)

These frequently asked questions (FAQ) describe the AI impact of Dynamics 365 Customer Insights Environment status summary feature.

## What is Environment status summary?

This AI-powered feature is designed to summarize business impacting jobs in the system and surface the root failure, if any, so you can quickly investigate the issue. This feature helps eliminate the need to review hundreds of jobs to identify if your environment is processing normally.

## What are the feature’s capabilities?

The Environment status summary detects if a key job has been skipped or failed, based on job priority order. A link to the job is provided so you can quickly access the issue.

## What is the feature’s intended use?

The intention is to aid administrators in determining the status of their Customer Insights environment in less time and with less manual effort.

## How was Environment status summary evaluated? What metrics are used to measure performance?

[Provide evidence of system or feature accuracy and performance, and, when applicable, a description of the extent to which these results are generalizable across use cases that were not part of the evaluation.]

## What are the limitations of Environment status summary? How can users minimize the impact of the Environment status summary limitations when using the system?

The feature reviews jobs in the following order, if they are configured:

- Exports
- Segments used in Customer Journey Orchestrator
- Dataverse hydration jobs
- Merge in data unification

The feature reports only on these jobs and one at a time based on the priority order. For example, if exports are configured, then the feature only identifies if there is an issue with an export.

The feature is available only in the United States.

## What operational factors and settings allow for effective and responsible use of the feature?

- On the Environment status summary, users are reminded that AI-generated content can be inaccurate.
- Users should be mindful when adding data sources, creating segments, measures, and other insights that the names are used in processing the jobs. Users should use responsible, appropriate names.

## See also

- [Environment status summary](system.md#environment-status-summary-preview)

[!INCLUDE [footer-include](includes/footer-banner.md)]
