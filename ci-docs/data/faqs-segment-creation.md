---
title: FAQ for segment creation (preview)
description: This FAQ provides information about the AI technology used in segment creation (preview). It provides key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: jimsonc
ms.author: jimsonc
ms.reviewer: alfergus
ms.collection: bap-ai-copilot 
---

# FAQ for segment creation (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

These frequently asked questions (FAQ) describe the AI impact of the Dynamics 365 Customer Insights - Data segment creation (preview) feature.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## What is segment creation with Copilot in Customer Insights?

This feature accepts natural language prompts in a chat experience to help build segments and specify their criteria in Dynamics 365 Customer Insights - Data. The suggested segment configuration and data mapping based on the prompt and the available customer data is available to users for tweaks and refinement.

## What are capabilities of the segment creation feature?

The segment creation feature provides the following components or capabilities:

- AI-generated suggested segments based on the data in your environment.

- Translate natural language into SQL statements to generate the suggested segment criteria.  

- Find the shortest relationship path for the input on segment definition and providing an option to change the relationship path.  

- Share feedback to the system to improve the accuracy of future segment results.  

## What is the intended use of the segment creation feature?

Segment creation with Copilot in Customer Insights - Data democratizes the varying technical ability of users and helps them create complex segments via natural language.

## How was the feature evaluated? What metrics are used to measure performance?

We measure performance of the Copilot by the successful creation of AI-generated segment criteria, and the publishing of the segment based on the suggestion of Copilot. We keep track of feedback provided through the thumbs up or thumbs down buttons to understand customer satisfaction with the feature.

## What are the supported geographies and languages?

Go to [Copilot International Availability report](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport).

## What operational factors and settings allow for effective and responsible use of the feature?

Copilot doesn't share data across environments. Opt-in consent is provided through the Settings page and managed by admins of Customer Insights - Data. Admins can revoke consent at any time and turn off the feature.

## See also

- [Create segments with Copilot (preview)](segments-copilot.md)

[!INCLUDE [footer-banner](includes/footer-banner.md)]
