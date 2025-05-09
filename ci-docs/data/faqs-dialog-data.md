---
title: FAQ for dialog with data
description: This FAQ provides information about the AI technology used in dialog with data. It provides key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 11/12/2024
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: radsay01
ms.author: rsayyaparaju
ms.reviewer: m-hartmann
ms.collection: bap-ai-copilot 
---

# FAQ for dialog with data (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

These frequently asked questions (FAQ) describe the AI impact of Dynamics 365 Customer Insights - Data dialog with data feature.

## What is dialog with data?

Dialog with data lets you ask questions in natural language and uses Copilot in Customer Insights - Data to answer them and generate insights.

## What are the feature’s capabilities?

Dialog with data can help you:

- Ask questions to generate insights about your customer’s profiles, such as understanding the gender distribution of your customers.

- Ask questions to generate insights about your customer’s preferences, behaviors, transactions, such as identifying where your highest-value customers live.

- Get more information on your customers that's automatically generated related to the question you asked to help you uncover more insights about customers.

- Get automatically generated suggested questions to enable deeper exploration even beyond your original question.

- Verify AI-generated results with a SQL statement and associated natural language explanation so you can easily understand what tables, columns, and attributes were used to produce results.

## What is the feature’s intended use?

Dialog with data is intended to enable end users like marketers, sellers, and service agents gain insights to better understand and serve customers easily without the support of IT teams or other tools.

## How was dialog with data evaluated? What metrics are used to measure performance?

Dialog with data has been evaluated for usability, accuracy, performance, and adherence to responsible AI principles. Evaluation included usability testing to ensure valid understanding of user intent, accurately generated results, overall system performance, and responsible AI. This feature had scenario testing for inappropriate content, malicious intent, jail break, and more. Ongoing monitoring is in place for system performance and responsible AI.  

## What are the limitations of dialog with data? How can users minimize the impact of the limitations when using the system?

The feature transforms your prompts in natural language into a SQL query to run by Synapse Serverless Server, and generates result that gets translated back into natural language response.

- Only questions related to your customers are supported. We suggest you don't enter any non-business-related questions.

- Only questions with corresponding data existing in Customer Insights - Data are supported.

- ‘Did you know’ section and ‘Explore further’ result generation is dependent on Azure OpenAI Service model.  

## What are the supported geographies and languages?

Go to [Copilot International Availability report](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport).

## What operational factors and settings allow for effective and responsible use of the feature?

- Administrators in Customer Insights - Data can choose to disable all Copilot functionality for each solution, by using the [consent experience](copilot-global-consent.md).

- There's a reminder that the result is AI-generated and can be inaccurate. AI feature results should always be reviewed and validated for accuracy and appropriateness before being used to make business decisions. AI features should always be used with caution and responsibility to minimize potential bias and unfairness in business decisions.

## See also

- [Have a dialog with data using Copilot in Customer Insights - Data](dialog-with-data.md)

[!INCLUDE[footer-include](includes/footer-banner.md)]
