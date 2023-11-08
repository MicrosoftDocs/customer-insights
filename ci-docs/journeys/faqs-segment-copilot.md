---
title: Responsible AI FAQs for segment copilot
description: The Responsible AI FAQs discuss segment copilot and the key considerations for making use of this technology responsibly.
ms.date: 11/08/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Responsible AI FAQs for segment copilot

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

This FAQ provides information about the AI technology used in Customer Insights Data, along with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations

## What is Segment Copilot?

This feature will allow the user to enter a prompt in natural language and help build segments and specify criteria using natural language on the segments page in Customer Insights through copilot chat experience. Suggested segment configuration and data mapping based on user NL prompt and data available in CI for users to verify and tweak as needed.

## What are capabilities of the segment copilot?

The segment Copilot provides the following components or capabilities:
- An AI-generated suggested segment based on your data within your environment.
- The ability to translate natural language into SQL statements to generate the segment criteria. 
- The ability to default to the shortest relationship path per user’s input on segment definition, while offering the option to edit the relationship path 
- Give feedback to the Copilot to improve accuracy of future segment results. 

## What is the intended use of the segment copilot?

The segment copilot democratizes the varying technical ability of users and helps them create complex segments through natural language.

## How was Segment Copilot evaluated? What metrics are used to measure performance?

The performance of the segment copilot is determined by the successful generation of the AI-generated segment criteria, and the publishing of the segment containing the use of the Copilot. The feedback provided through the thumbs up, or thumbs down is tracked to understand customers’ satisfaction with the feature.

## What are the limitations of Segment Copilot? How can users minimize the impact of the limitations when using the system?

The feature is currently only available in the US region and in English. 

## What operational factors and settings allow for effective and responsible use of the feature?

The segment Copilot doesn't share data across customers’ environment. There's no ability to use or generate content that could lead to harm. Opt in consent to the data prep report is provided in the **Settings** page and managed by the Admin role for Customer Insights - Data. Consent can be revoked at any time to turn off the feature.

[!INCLUDE [footer-include](./includes/footer-banner.md)]