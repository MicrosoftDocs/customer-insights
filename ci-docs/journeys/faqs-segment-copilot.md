---
title: Responsible AI FAQs for the segment copilot
description: Segment copilot responsible AI FAQs explain how natural language prompts generate segments, plus capabilities, limitations, and operational controls.
ms.date: 07/09/2026
ms.update-cycle: 180-days
ms.topic: faq
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - transparency-note
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Responsible AI FAQs for the segment copilot

These responsible AI FAQs explain how segment copilot uses AI, how Microsoft evaluated it, and what limits and operational considerations apply.

## What is the segment copilot?

Segment copilot lets users enter a natural language prompt on the segments page in Customer Insights to build segments with specified criteria through the Microsoft 365 Copilot experience. The feature generates a suggested segment configuration and data mapping based on the prompt and the data available in Customer Insights. Users then verify the segment and edit it as needed.

## What are the capabilities of the segment copilot?

The segment copilot provides the following components or capabilities:
- An AI-generated suggested segment based on data within the user's environment.
- The ability to translate natural language into SQL statements to generate the segment criteria.
- The ability to default to the shortest relationship path based on the user's segment definition, while still allowing the relationship path to be edited.
- The ability to give feedback to the copilot to improve the accuracy of future segment results. 

## What is the intended use of the segment copilot?

Segment copilot helps users with different technical skill levels create complex segments through natural language.

## How was the segment copilot evaluated? What metrics are used to measure performance?

Performance is measured by whether segment copilot successfully generates AI-based segment criteria and whether users publish the segment it creates. Thumbs-up and thumbs-down feedback helps track satisfaction with the feature.

## What are the limitations of the segment copilot? How can users minimize the impact of the limitations when using the system?

The segment copilot feature is currently only available in North America and Europe; it's available in English only.

## What operational factors and settings allow for effective and responsible use of the feature?

Segment copilot doesn't share data across environments. It can't be used to create or generate content that could lead to harm. Opt-in consent for the data prep report is available on the **Settings** page and is managed by the Admin role for Customer Insights - Data. Consent can be revoked at any time to turn off the feature.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
