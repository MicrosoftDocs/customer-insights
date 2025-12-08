---
title: FAQ for docs-based Q&A Copilot (preview)
description: This FAQ provides information about the AI technology docs-based Q&A skill used in Customer Insights - Data, along with key considerations and details about how the capability is used, how it was tested and evaluated, and any specific limitations.
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.custom:
  - responsible-ai-faqs
ms.topic: faq
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: alfergus
ms.collection: bap-ai-copilot 
---

# FAQ for docs-based Q&A capability (preview)

These frequently asked questions (FAQ) describe the AI impact of [Get answers to questions about capabilities from Copilot](help-pane-copilot.md) feature in Customer Insights - Data.

## What is docs-based Q&A skill?

Setting up Customer Insights - Data and managing it can be complex at times. Copilot in Customer Insights - Data assists you by providing timely guidance in everyday words. You can ask your own questions to help clarify concepts or understand what you need to do achieve your goals in Customer Insights - Data.

## What are capabilities of the docs-based Q&A skill?

This Copilot capability is to answer user's question by using the ["Generative Answers" service](/power-virtual-agents/nlu-boost-conversations#ai-response-generation-training-model-and-usage-notes). The answers are based solely on the following public available sources: Product's public documentation, related [troubleshooting pages](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights) and blogs by the Microsoft team on how to set up Customer Insights - Data. These sources are organized as a Bing Search index, which is the reason for Copilot showing the disclaimer about Bing Search being used for certain capabilities.

## What is the intended use of the docs-based Q&A skill?

Users working in the Customer Insights - Data app can ask questions in writing about the user experience or capabilities. Any input by the user is treated as a question towards our product’s public documentation. The user is expected to review the answer given using the referenced sources.

## How was docs-based Q&A skill evaluated? What metrics are used to measure performance?

The capability was evaluated on a collection of manually curated question-and-answer datasets, covering multiple industries.
More evaluation was performed over custom datasets for offensive and malicious prompts and responses.

## What are the limitations of docs-based Q&A skill? How can users minimize the impact of the capabilities' limitations when using the system?

- Inaccurate responses might be returned when users converse with the system in languages other than English.
- The capability can only answer questions that are covered in [this product's public documentation](overview.md) and [troubleshooting pages](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights).
- This capability can't access your data tables to answer questions about it. You can use the following capability for such questions: [Have a dialog with data using Copilot](dialog-with-data.md).
- The capability doesn't answer questions about the [roadmap of our product](https://releaseplans.microsoft.com/).

## What are the supported geographies and languages?

Go to [Copilot International Availability report](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport).

## What operational factors and settings allow for effective and responsible use of the feature?

This capability doesn't need setting up by users. It's offered as a base plugin of our Copilot. Administrators in Customer Insights - Data can choose to disable all Copilot functionality for each solution, by using the [consent experience](copilot-global-consent.md).

## Next steps

- [Get answers to questions about capabilities from Copilot (preview)](help-pane-copilot.md)
- [Responsible AI FAQs for Dynamics 365 Customer Insights - Data](responsible-ai-overview.md)

[!INCLUDE[footer-include](./includes/footer-banner.md)]
