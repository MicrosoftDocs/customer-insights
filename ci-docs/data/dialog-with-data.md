---
title: Have a dialog with data using Copilot in Customer Insights (preview)
description: Learn how to get more insights from your data by asking natural-language questions with Copilot in Dynamics 365 Customer Insights. 
ms.date: 10/05/2023
ms.topic: how-to
author: wmelewong
ms.author: radsay01
ms.reviewer: mhart
ms.custom: bap-template
---

# Have a dialog with data using Copilot in Customer Insights (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Understanding your customers’ profiles and preferences is essential for driving personalized experience. Customer Insights – Data uses copilot generative AI capabilities to let you ask questions in natural language to quickly generate insights about your customers. Now end users like marketers, sellers, and service agents can get insights seamlessly. For example, you’d like to run a campaign targeted at improving customer loyalty. You can ask Copilot “How many customers aren't members of the loyalty program but have spent over $1,000 in the last six months?” Then use this information to create a segment and run an email campaign. The possibilities are endless. Have a dialog with your data by asking questions in every day words to explore, assess, and better understand the profiles, behaviors, and activities of your customers.

Responses are generated in accordance with [Microsoft Responsible AI Standards](https://www.microsoft.com/ai/responsible-ai). For more information, see [FAQ for dialog with data](faqs-dialog-data.md)

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Prerequisites

- Customer data is [imported](data-sources.md) and [unified](data-unification.md).
- You have at least Contributor permissions.
- The environment is hosted in one of the US regions.

## Discover insights from your data

1. In Customer Insights - Data, go to **Insights** > **Discovery**.

1. A pop-up box explains the feature and asks for your consent to share your prompts to continuously improve the quality of the results, or answers, generated. Choose your preference. You only need to do give consent once, and you can always change your preference on the **Discovery** page later.

   :::image type="content" source="media/copilot-customer-insights.png" alt-text="Screenshot of the dialog with data feature, with copilot AI answering a user question.":::

The **Discover insights about your customers in natural language (preview)** page contains four key components:

- **Prompt box**: Enter your question in natural language; for example, *How many customers in my loyalty program have more than 100 reward points?* Copilot in Customer Insights supports questions in English with up to 2,000 characters. This section also contains the consent setting for sharing your prompts. Ask a specific question about your customers and make sure you have the relevant data imported to answer the question. Avoid asking questions that are too ambiguous or contain inappropriate content.

  > [!TIP]
  >
  > - Ask one question at a time. Don't combine multiple questions in one prompt.
  > - Add clarifying information, for example when your question contains an abbreviation.
  > - Make your questions as specific as possible by referring to names of tables and columns.
  > - Don't enter SQL statements as questions. Use conversational language.

- **Results**: Answers and results generated in response to your question, along with other related insights, if any, appear in this section. Other insights might not be available if the data is insufficient or the insights are insignificant.

- **Explore further**: This section contains questions to further explore and generate new insights. Select a question to prompt a response. To generate a new set of suggested questions, select **See more examples**.

- **SQL query for verification**: This section displays the SQL query that generated the answer. It represents your natural-language question. Use it to verify the system understood your question and returned relevant results.

## Share your feedback

We want to hear your feedback so we can continually enhance the relevancy, precision, and value of the results and the user experience in general. Use the thumbs up or down and the feedback box to share your thoughts.

## Next steps

- [Create complex segments with segment builder](segment-builder.md)  
- [Create measures with measure builder](measure-builder.md)  
- [Responsible AI FAQs for Dynamics 365 Customer Insights](responsible-ai-overview.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
