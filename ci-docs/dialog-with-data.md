---
title: Have a dialog with data using Copilot in Customer Insights
description: "Use copilot in Dynamics 365 Customer Insights to ask questions about your unified data." 
ms.date: 05/22/2023
ms.reviewer: mhart
ms.topic: how-to
author: wmelewong
ms.author: wameng
ms.custom: bap-template
---

# Have a dialog with data using Copilot in Customer Insights (preview)

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 Customer Insights lets you use copilot capabilities to generate insights about your customers. Start asking questions in natural language, powered by [Azure OpenAI Service](https://azure.microsoft.com/products/cognitive-services/openai-service) models to get insights. Have a dialog with data to explore, assess and better understand profiles, behavior, and activity by your customers. This feature aims to help you create optimal personalized experiences and engage with your customers through effective channels.

## Prerequisites

- Customer data is [imported](data-sources.md) and [unified](data-unification.md).
- You have at least Contributor permissions in Customer Insights.
- The Customer Insights environment is hosted in one of the US regions.

## Discover insights from your data

1. In Customer Insights, go to **Insights** > **Discovery**.
1. A pop-up dialog explains the feature and asks for your consent to share your prompts to continuously improve the quality of the results or answers generated. Choose your preference. You can always change your preference using a toggle on the **Discovery** page later.

   :::image type="content" source="media/copilot-customer-insights.png" alt-text="Screenshot of the dialog with data feature with copilot answering a user question.":::

1. The **Discover insights about your customers in natural language (preview)** page contains four key components:

    - **Prompt box**: Enter your question in natural language. For example: ‘How many customers in my loyalty program have more than 100 reward points?’ Copilot in Customer Insights currently supports English questions with up to 2000 characters. This section also contains the consent setting for sharing your prompts.
    Ask a specific and relevant question about your customers and make sure you have corresponding data imported to answer the question asked. Avoid asking questions that are too ambiguous or contain inappropriate content.

      > [!TIP]
      >
      > - Ask one question at a time and don't combine multiple questions in one prompt. Add clarifying information, for example when using abbreviations.
      > - Enter questions about your customer data and make them as specific as possible by referring to names of tables and columns.
      > - Don't enter SQL statements as questions. Use conversational language.

    - **Results**: Answers and results generated to your question show in this section. It also includes other insights related to your question. Responses use content filter and moderator solutions in accordance with [Microsoft Responsible AI Standards](https://www.microsoft.com/ai/responsible-ai).

    - **Explore further**: This section contains questions suggested by the system to further explore and generate new insights. Select a question to prompt a response. Select **See more examples** to generate a new set of suggested questions.

      > [!NOTE]
      > Sections with additional information might not be available if there is insufficient data or no additional insights worth surfacing.

    - **SQL query for verification**: Copilot provides the SQL query created from your natural language question to generate the result/answer. Use this query to verify the results. If the query or output doesn’t reflect your business need, ask a rephrased or new question.

## Share your feedback

We want to hear your feedback so we can continually enhance the relevancy, precision, and value of the results and the user experience in general. Use the thumbs up/down and the feedback dialog to share your thoughts.

## Next steps

- [Create complex segments with segment builder](segment-builder.md)
- [Create measures with measure builder](measure-builder.md)
- [Predictions overview](predictions-overview.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
