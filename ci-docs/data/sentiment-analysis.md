---
title: Analyze sentiment for customer feedback (preview)
description: Learn how to use a sentiment analysis model on customer feedback in Dynamics 365 Customer Insights - Data."
ms.date: 09/01/2023
ms.update-cycle: 180-days
ms.reviewer: mhart
ms.topic: how-to
author: wmelewong 
ms.author: wameng
ms.collection: bap-ai-copilot 
---

# Analyze sentiment in customer feedback (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Sentiment analysis enables you to synthesize customer sentiment and identify business aspects as opportunities for improvement. This feature helps you understand what works well and what you need to address. It can help you drive business actions that enable experiences that result in high customer satisfaction and loyalty.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Overview

The sentiment analysis feature generates two derived insights per customer ID. A sentiment score (of -5 to 5) and list of applicable business aspects (areas of business) that together help you better understand the customer feedback.

This analysis helps you:
- Get an overview of customer sentiments towards a brand or organization
- Identify customers with negative sentiment to focus your campaigns and engagements and optimize for higher return  
- Identify business aspects with issues pointed out by customers  
- Segment customers based on their sentiment to run personalized campaigns with targeted sales, marketing, and support efforts
- Optimize business operations by addressing areas of concern or opportunities that were mentioned by customers
- Recognize business aspects that are doing well and reward happy customers through loyalty and promotion programs

The model provides a list of words that affected the model's decision to assign a particular sentiment score or business aspect to feedback comments.  

We use two **Natural Language Processing (NLP) models**: The first assigns each feedback comment a sentiment score. The second model associates each feedback with all applicable business aspects. The models are trained on public data from sources across social media, retail, restaurant, consumer products, and automotive industries.
  
Pre-defined business aspects for the model to associate with feedback data include:
- Account management
- Checkout and payment
- Customer support
- In-store pickup
- Packaging shipping and retrieval
- Pre-ordering
- Price
- Privacy and security
- Promotions and rewards
- Receipt and warranty
- Return exchange and cancellation
- Fulfillment accuracy
- Website/app quality

> [!NOTE]
> Currently, we only support sentiment analysis on English customer feedback. More languages will be supported in the future. If feedback in other languages is uploaded, the model will still return results. However, these results won't be accurate.

## Prerequisites

- At least [Contributor permissions](user-roles.md)
- [Unified](data-unification.md) text feedback data. We highly recommend that you [configure your feedback data tables as semantic type activity tables](data-unification-map-tables.md#select-primary-key) (Feedback type).
- Unified Customer ID (UCID) from data unification to match text feedback data records to an individual customer.
- Feedback ID
- Feedback timestamp
- Feedback text

Dynamics 365 Customer Insights - Data can process up to 10 million feedback records for a single model run. The model can analyze feedback comments up to 128 words. If a feedback comment is longer, the analysis considers only the first 128 words.

> [!NOTE]
> Only one feedback table can be configured. If there are multiple feedback tables, combine them in Power Query before data ingestion.

## Configure a sentiment analysis

1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Customer sentiment analysis (preview)** tile.

1. Select **Get started**.

1. **Name** the analysis and provide the **Business aspect output table name** and the **Sentiment score output table name**.

1. Select **Next**.

1. Select **Add data** for **Customer feedback**.

1. Select the semantic activity type **Feedback** that contains the feedback data. If the activity has not been set up, select **here** and create it.

   :::image type="content" source="media/sentiment-add-feedback-activities.png" alt-text="Configuration step to select feedback activities for sentiment analysis.":::

1. Select the activities to use for this sentiment analysis, then select **Next**.

1. Map the attributes in your data to the model attributes.

1. Select **Save**.

1. Select **Next**. The **Review and run** step shows a summary of the configuration and provides a chance to make changes before you create the analysis.

1. Select **Edit** on any of the steps to review and make any changes.

1. If you are satisfied with your selections, select **Save and run** to start running the model. Select **Done**. The **My predictions** tab displays while the prediction is being created. The process may take several hours to complete depending on the amount of data used in the prediction.

[!INCLUDE [progress-details](includes/progress-details-pane.md)]

## View analysis results

1. Go to **Insights** > **Predictions**.

1. In the **My predictions** tab, select the prediction you want to view.

There are two tabs of results.

### Summary tab

There are four primary sections of data within the results page.

- **Average sentiment score**: Sentiment scores helps you understand the overall sentiment across all customers.
  - **Negative** (-5 > 2)
  - **Neutral** (-1 > 1)
  - **Positive** (2 > 5)
  
  :::image type="content" source="media/overall-customer-sentiment.png" alt-text="Visual representation of the overall customer sentiment.":::

- **Distribution of customers by sentiment score**: Customers are categorized into negative, neutral, and positive groups based on their sentiment scores. Hover over the bars in the histogram to see the number of customers and average sentiment score in each group. This data can help you [create segments of customers](prediction-based-segment.md) based on their sentiment scores.  

  :::image type="content" source="media/distribution-customer-sentiment.png" alt-text="Bar chart showing the customer sentiment across the three sentiment groups.":::

- **Average sentiment score over time**: Customer sentiment may change over time. We provide trends in your customers’ sentiments for the time range of your data. This view helps you gauge the effect of seasonal promotions, product launches, or other time-bound interventions on customer sentiment. See the graph by selecting the year-of-interest from the dropdown menu.

  :::image type="content" source="media/sentiment-score-over-time.png" alt-text="History chart with the sentiment score over time represented as a line.":::

- **Sentiment across business aspects**: Average sentiment across business aspects helps you gauge which aspects of your business already satisfy customers or require more attention. Feedback records that don't align to any of the supported business aspects are categorized under **Other**. Sort the data by selecting any column.

  :::image type="content" source="media/sentiment-across-business-aspects.png" alt-text="List of business aspects with the associated sentiment value and the number of customers mentioning it.":::

  Select the name of a business aspect to see how a business aspect is identified by the model:

  - **Influential words**: Top words that influenced the AI model’s identification of a business aspect in customer feedback.
    **Show offensive words**: Lets you include offensive words in the list from original customer feedback data. By default, it's turned off.  Offensive word masking is powered by an AI model and may not detect all offensive words. If you detect an offensive word that wasn't filtered as expected, let us know.

    :::image type="content" source="media/offensive-words-sentiment.png" alt-text="List of influential words with the toggle to show or hide offensive words.":::

  - **Feedback samples**: Actual feedback records in your data. Words are color-coded according to their influence on the identification of a business aspect.

### Influential words analysis tab

There are three sections of additional information that explain how the sentiment model works.
  
- **Top words contributing to positive sentiment**: Top words that influenced the AI model’s identification of positive sentiment in customer feedback.  

- **Top words contributing to negative sentiment**: Top words that influenced the AI model’s identification of negative sentiment in customer feedback.

- **Feedback samples**: Actual feedback records, one with a negative sentiment and one with a positive sentiment. Words in the feedback records are highlighted according to their contribution to the assigned sentiment score. Words that contribute to a positive sentiment score are highlighted in green. Words contributing to a negative score are highlighted in red.
   Select **See more** to load more feedback samples.
  
   :::image type="content" source="media/sentiment-feedback-samples.png" alt-text="Examples of sentiment analysis on customer feedback.":::

**Show offensive words**: Lets you include offensive words in the list from original customer feedback data. By default, it's turned off.  Offensive word masking is powered by an AI model and may not detect all offensive words. If you detect an offensive word that wasn't filtered as expected, let us know.

## Act on analysis results

To create new segments of customers from the sentiment analysis results, select **Create segments** at the top of the model result page.

## Potential bias

As with any feature that uses predictive artificial intelligence, there could be potential bias in the data you use to predict customer sentiment. For example, if you only collect feedback digitally, you might miss feedback from customers who primarily conduct business with you in person, which affect the feature’s output.

As this feature uses automated means to evaluate data and make predictions based on that data, it therefore has the capability to be used as a method of profiling, as that term is defined by privacy laws and regulations. Your use of this feature to process data may be subject to those laws or regulations. You are responsible for ensuring that your use of Customer Insights - Data, including sentiment analysis, complies with all applicable laws and regulations, including laws related to privacy, personal data, biometric data, data protection, and confidentiality of communications.

[!INCLUDE [footer-include](includes/footer-banner.md)]
