---
title: Responsible AI FAQs for the Customer Insights - Journeys copilot (preview)
description: The Responsible AI FAQs discuss the general copilot and the key considerations for making use of this technology responsibly.
ms.date: 03/12/2024
ms.topic: faq
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Responsible AI FAQs for the Customer Insights - Journeys copilot (preview)

[!INCLUDE [Preview banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

These responsible AI FAQs describe the AI impact of Copilot capabilities for model-driven apps in Dynamics 365 Customer Insights - Journeys. Review [the main FAQ for this Copilot capability](/power-apps/maker/common/faqs-copilot-model-driven-app)

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## What are the capabilities of Copilot in model-driven apps in Customer insights - Journeys?

The capabilities of Copilot are shared across every Power Apps model-driven app. Within Customer Insights - Journeys, the suggested prompts are adapted to fit the marketing scenarios our users focus on. These capabilities offer Power Apps app users insights about the data in their apps through conversation in natural language. Copilot helps users boost their productivity through AI-powered insights and intuitive app navigation. This feature is available throughout the model-driven apps.
Learn more: [Copilot in model-driven apps](/power-apps/maker/common/faqs-copilot-model-driven-app)

## What can this Copilot capability do in Customer insights - Journey do?

It can answer questions about the configured tables in an app and aids in navigation through queries such as "Take me to _page name_."
It can answer questions about how to use Customer Insights. These answers are based on [the publicly available documentation](/dynamics365/customer-insights/journeys/). This capability uses a Bing Search index to organize the public documentation. This is the reason for this capability needing consent for Bing Search.

## What is this capability of Copilot' intended use?

As an AI assistant to end users, it provides answers to questions about how the product works, the configured data in the app, and helps with app navigation.

## How was this Copilot capability evaluated? What metrics are used to measure performance?

Copilot in model-driven apps underwent substantial testing before the feature was released in preview. If you encounter issues while using Copilot in model-driven apps, submit your feedback. Your feedback is used to improve Microsoft products and services. For more information, go to: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy)

## What are the limitations of Copilot in model-driven apps? How can users minimize the impact of it limitations when using the system?

To use this capability your environment must be in the US region. The Power Platform environment's language needs to be set to English. This capability was tested for English language only. In future releases, this feature will be available in further regions. Review the [main documentation for these Copilot capabilities](/power-apps/maker/common/faqs-copilot-model-driven-app) to learn more about update availability.

Copilot in model-driven apps is a preview feature. Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. Review [the main FAQ for this Copilot capability](/power-apps/maker/common/faqs-copilot-model-driven-app)

This capability may be subject to usage limits or capacity throttling. The capability to answer based on the documentation uses a Bing Search index to organize the pages. If consent for to use Bing Search isn't given, then this capability won't be available.

## What operational factors and settings allow for effective and responsible use of Copilot in model-driven apps in Customer insights - Journeys?

Whether this Copilot is available in your environment is controlled by Power Platform administrator settings. [Learn how to add Copilot for model-driven apps](/power-apps/maker/model-driven-apps/add-ai-copilot)

When asking Copilot questions about how to use Customer Insights, it's recommended to describe your goal in addition the question itself. For example, "I'm organizing a two day event in a venue. How can I get started with setting up registration for it?" Clearly identify which page you want to navigate to. For example, "Take me to _page name_," such as "Take me to Accounts."

[!INCLUDE [footer-include](./includes/footer-banner.md)]
