---
title: FAQ for segment creation (preview)
description: Segment creation (preview) uses AI in Customer Insights - Data. This FAQ covers capabilities, evaluation, and limitations.
ms.date: 07/10/2026
ms.update-cycle: 180-days
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: alfergus
ms.collection: bap-ai-copilot 
---

# FAQ for segment creation (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

These frequently asked questions (FAQ) describe the AI impact of the Dynamics 365 Customer Insights - Data segment creation (preview) feature.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## What is segment creation with Copilot in Customer Insights?

This feature accepts natural language prompts in a chat experience to help you build segments and specify their criteria in Dynamics 365 Customer Insights - Data. Based on your prompt and available customer data, Copilot suggests a segment configuration and data mapping that you can review and refine.

## What are capabilities of the segment creation feature?

The segment creation feature provides the following components or capabilities:

- AI-generated suggested segments based on the data in your environment.

- Translate natural language into SQL statements to generate the suggested segment criteria.  

- Find the shortest relationship path for the input on segment definition and providing an option to change the relationship path.  

- Share feedback to the system to improve the accuracy of future segment results.  

## What is the intended use of the segment creation feature?

Segment creation with Copilot in Customer Insights - Data helps users of all technical skill levels create complex segments using natural language.

## How was the feature evaluated? What metrics are used to measure performance?

You measure Copilot's performance by tracking the successful creation of AI-generated segment criteria and the publishing of segments based on Copilot's suggestions. You also track feedback from the thumbs up and thumbs down buttons to gauge customer satisfaction with the feature.

## What are the supported geographies and languages?

Go to [Copilot International Availability report](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport).

## What operational factors and settings allow for effective and responsible use of the feature?

Copilot doesn't share data across environments. Admins of Customer Insights - Data provide opt-in consent through the Settings page and can revoke consent or turn off the feature at any time.

## See also

- [Create segments with Copilot (preview)](segments-copilot.md)

[!INCLUDE [footer-banner](includes/footer-banner.md)]
