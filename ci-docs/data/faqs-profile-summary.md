---
title: FAQ for customer profile summary (preview)
description: This FAQ provides information about the AI technology used in the customer profile summary (preview). It provides key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 11/14/2023
ms.custom: 
  - responsible-ai-faqs
ms.topic: article
author: zacookmsft
ms.author: zacook
ms.reviewer: m-hartmann
---

# FAQ for customer profile summary (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

These frequently asked questions (FAQ) describe the AI impact of the Dynamics 365 Customer Insights - Data profile summary (preview) feature.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## What is customer profile summary?

This AI-powered feature enables you to see a summary of customer information to help you make better decisions about how to engage and interact with your customer. The summary loads automatically in the side bar when you view a page, like the Dynamics 365 Sales’ **Lead** pages.

## What are the feature’s capabilities?

The customer profile summary takes available information from customer activities and summarizes them to provide you with date and interaction based analysis, such as recency and frequency. This data helps you understand how a customer is engaging with your business. You can use this information, paired with your own business understanding, to engage a user with a personalized experience.

The feature uses information from your customer’s activity stream and performs analysis on the data using Azure OpenAI capabilities. You can view Azure OpenAI data privacy policies here: [Data, privacy, and security for Azure OpenAI Service - Azure AI services | Microsoft Learn](/legal/cognitive-services/openai/data-privacy)

## What is the feature’s intended use?

The summary is intended to help you understand more about what a customer has done, such as how frequently the customer engages with your business and enable you to better customize your interactions with the customer.

## How was the customer profile summary evaluated? What metrics are used to measure performance?

This feature has only been evaluated in English at this time.

The customer profile summary is evaluated from dimensions of accuracy of response and quality of insight. It is evaluated with embedded monitoring for Responsible AI. Specifically, this feature has been tested with an array of scenarios to ensure it captures and mitigates accordingly, including inappropriate language used, malicious intention of jail break, and data fabrication.

## What are the limitations of Customer Profile Summary? How can users minimize the impact of the Customer Profile Summary limitations when using the system?

The feature only analyzes information for a single customer at a time. The system only reviews a subset of the customer's activities, ordered by date, and identifies insights from the information to help you better understand how the customer engages with your business. To create better insights, add additional activity information for your customers.

## What are the supported geographies and languages?

The feature is available in the United States and supports English only.

## What operational factors and settings allow for effective and responsible use of the feature?

<!--- What admin page? Opt-in consent is provided through the Settings page and managed by admins of Customer Insights - Data?? --->
- On the admin page, there is a toggle for you to select your data sharing preference easily. Similarly as an Admin, in the Sales application you can select Customer Insights - Data as a source to be used in the respective summary.
- There's a reminder that the result is AI-generated and can be inaccurate.We suggest you always review and validate the result AI-generated result before applying it for business actions.
- In general, you should use the feature in a mindful way to ensure responsible and appropriate inputs and outputs to minimize bias and unfairness.
