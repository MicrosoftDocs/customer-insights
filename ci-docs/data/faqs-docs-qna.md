title: FAQ for docs-based Q&A Copilot
description: This FAQ provides information about the AI technology docs-based Q&A skill used in Customer Insights - Data, along with key considerations and details about how the capability is used, how it was tested and evaluated, and any specific limitations.
ms.date: [Date]
ms.custom: 
  - responsible-ai-faqs
ms.topic: article
author: [Author]
ms.author: [Author]
ms.reviewer: [Reviewer]
---

# FAQ for docs-based Q&A capability 

These frequently asked questions (FAQ) describe the AI impact of [Get answers about Customer Insights - Data from Copilot](copilot-global-sidecar.md) feature in Customer Insights - Data.

## What is docs-based Q&A skill?

Setting up Customer Insights - Data and managing it can be complex at times. Copilot in Customer Insights - Data will assist you by providing timely guidance in everyday words. You can ask your own questions to help clarify concepts or understand what you need to do achieve your goals in Customer Insights - Data.

## What are capabilities of the docs-based Q&A skill?

This Copilot capability is to answer user's question by using the ["Generative Answers" service](https://learn.microsoft.com/power-virtual-agents/nlu-boost-conversations#ai-response-generation-training-model-and-usage-notes). The answers are based solely on the following public available sources: Product's public documentation, related [troubleshooting pages](https://learn.microsoft.com/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights) and a blogs by the Microsoft team on how to setup Customer Insights - Data. These sources are organized as a Bing Search index, which is the reason for Copilot showing the disclaimer about Bing Search being used for certain capabilities. 

## What is the intended use of the docs-based Q&A skill?

While working in the Customer Insights - Data app, users can ask questions in writing about the user experience or capabilities. Any input by the user is treated as a question towards our product’s public documentation. The user is expected to review the answer given using the referenced sources.

## How was docs-based Q&A skill evaluated? What metrics are used to measure performance?

The capability was evaluated on a collection of manually curated question-and-answer datasets, covering multiple industries.
Additional evaluation was performed over custom datasets for offensive and malicious prompts and responses.

## What are the limitations of docs-based Q&A skill? How can users minimize the impact of this capabilities' limitations when using the system?

- The capability currently only supports English. Inaccurate responses may be returned when users converse with the system in languages other than English.
- The capability will not answer questions about the roadmap of our product. If you're interested in our roadmap, please visit https://releaseplans.microsoft.com/. 

## What operational factors and settings allow for effective and responsible use of the feature?

This capability does not need setting up by users. It is offered as a base plugin of our Copilot. Administrators in Customer Insights - Data can choose to disable all Copilot functionality for each solution, by using the [consent experience](copilot-global-consent.md).

## See also

- [Feature page]([Link])

[!INCLUDE[footer-include](../includes/footer-banner.md)]
