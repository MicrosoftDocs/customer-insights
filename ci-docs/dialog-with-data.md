---
title: Have a dialog with data using Copilot in Customer Insights
description: "Define customer or business contact activities and view them in a timeline on customer profiles." 
ms.date: 03/13/2023
ms.reviewer: mhart
ms.topic: how-to
author: wameng
ms.author:  wameng
ms.custom: bap-template
---

# Have a dialog with data using Copilot in Customer Insights

Dynamics 365 Customer Insights lets you use copilot capabilities to generate insights about your customers by simply asking questions in natural language, powered by Azure OpenAI Service models. Have a dialog with data to explore, assess and better understand profiles, behavior, and activity by your customers. This feature aims to help you create optimal personalized experiences and engage with your customers through effective channels.

## Prerequisites

- Customer data is imported and unified.
- You have at least Contributor permissions in Customer Insights.
- The Customer Insights environment is hosted in one the US regions.

## Discover insights from your data

1. Go to Insights > Discovery.
1. A pop-up dialog explains the feature and asks for your consent to share your prompts to continuously improve the quality of the results or answers generated. Choose your preference.  You can always change your using a toggle on the Discovery page later.
1. The Discover insights about your customers in natural language (preview) page contains four key components:

    - Prompt box: Enter your question in natural language. For example: ‘How many customers are in my loyalty program and have more than 100 rewards points?’ Copilot in Customer Insights currently supports English questions with up to 2000 characters. This section also contains the consent setting for sharing your prompts.
    Ask a specific and relevant question about your customers and make sure you have corresponding data imported to answer the question asked. Avoid asking questions that are too ambiguous or contain inappropriate content.
    - Results: Answers and results generated to your question show in this section. It also includes additional insights related to your question under Did you know?

    - Explore further: This sections contains additional questions suggested by the system to further explore and generate new insights. Select a question to prompt a response. Select See more examples to generate a new set of suggested questions.

      > [!NOTE]
      > Sections with additional information might not be available if there is insufficient data or no additional insights worth surfacing.

    - SQL query for verification: Copilot provides the SQL query created from your natural language question to generate the result/answer. Use this query to verify the results. If the query or output doesn’t reflect your business need, ask a rephrased or new question.

      > [!NOTE]
      > Responses use content filter and moderator solutions in accordance with Microsoft Responsible AI Standards.

## Share your feedback

We want to hear your feedback so we can continually enhance the relevancy, precision, and value of the results and the user experience in general. Use the thumbs up/down and the feedback dialog to share your thoughts.

## Next steps

- [Create complex segments with segment builder](segment-builder.md)
- [Create measures with measure builder](measure-builder.md)
- [Predictions overview](predictions-overview.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
