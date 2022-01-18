---
title: "Sentiment analysis for customer feedback"
description: "Learn how to use a sentiment analysis model on customer feedback in Dynamics 365 Customer Insights." 
ms.date: 12/23/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.reviewer: mhart
ms.topic: conceptual
author: wmelewong 
ms.author: wameng
manager: shellyha
---

# Analyze sentiment in customer feedback (Preview)

Customers expect high quality products, services, and experiences these days. Especially customers who share their feedback. It's very challenging for organizations to analyze an increasing volume of data without lowering accuracy and higher labor cost. Dynamics 365 Customer Insights offers a sentiment analysis model for customer feedback that enables organizations to analyze their data more accurately and at a lower cost.

Sentiment analysis enables you to synthesize customer sentiment and identify business aspects as opportunities for improvement. This Customer Insights feature helps you understand what works well and what you need to address. Focus on the most relevant and impactful areas of business to improve the experience for your customers. Ultimately, it can help you to drive business actions that enable experiences that result in high customer satisfaction and loyalty.

## Overview

The sentiment analysis feature generates two derived insights per customer ID. A sentiment score (of -5 to 5) and list of applicable business aspects (areas of business) together help you better understand the customer feedback. 

This information can help you achieve the following results: 
- Get an overview of customer sentiments towards a brand or organization
- Identify customers with negative sentiment to focus your campaigns and engagements and optimize for higher return  
- Identify business aspects with issues pointed out by customers  
- Segment customers based on their sentiment to run personalized campaigns with targeted sales, marketing, and support efforts
- Optimize business operations by addressing areas of concern or opportunities that were mentioned by customers
- Recognize business aspects that are doing well and reward happy customers through loyalty and promotion programs

To ensure you can trust the results of the models, we provide transparent information about how the models make decisions. You'll get a list of words that affected the models’ decision to assign a particular sentiment score or business aspect to feedback comments.  

We use two **Natural Language Processing (NLP) models**: The first assigns each feedback comment a sentiment score. The second model associates each feedback with all applicable business aspects. The models are trained on public data from sources across social media, retail, restaurant, consumer products, and automotive industries.    
  
Pre-defined business aspects for the model to associate with feedback data include:
-	Account management
-	Checkout and payment
-	Customer support
-	In-store pickup
-	Packaging shipping and retrieval
-	Pre-ordering
-	Price
-	Privacy and security
-	Promotions and rewards
-	Receipt and warranty
-	Return exchange and cancellation
-	Fulfillment accuracy
-	Website/app quality

> [!NOTE]
> Currently, we only support sentiment analysis on English customer feedback. More languages will be supported in the future. If feedback in other languages is uploaded, the model will still return results. However, these results won't be accurate. 

## Prerequisites

Sentiment analysis is based on text feedback data that has gone through the [data unification process](data-unification.md). We highly recommend that you [configure your feedback data entities as semantic type activity entities](map-entities.md#select-primary-key-and-semantic-type-for-attributes) (Feedback type) beforehand. 

To configure a sentiment analysis model, you need at least [Contributor permissions](permissions.md).

Customer Insights can process up to 10 million feedback records for a single model run. The model can analyze feedback comments up to 128 words. If a feedback comment is longer, the analysis considers only the first 128 words.

### Data requirements
  
The following data attributes are required:
- Unified Customer ID (UCID) to match text feedback data records to an individual customer. This ID is a result of the [data unification process](data-unification.md).
- Feedback ID
- Feedback timestamp
- Feedback text   

> [!TIP]
> Sentiment analysis requires the text feedback of your customers. Only one feedback entity can be configured currently. If there are multiple feedback entities, you can union them in Power Query before data ingestion begins.

## Configure a sentiment analysis 

1. In Customer Insights, go to **Intelligence** > **Predictions**.

1. On the **Customer sentiment analysis** tile, select **Use model**.

1. In the **Customer sentiment analysis (preview)** pane, select **Get started**.

1. In the **Model name** step, provide a **Name** for your analysis. 

1. Provide the **Business aspect output entity name** and the **Sentiment score output entity name**, then select **Next**.

1. In the **Required data** step, select **Add data**.

   :::image type="content" source="media/sentiment-add-data.png" alt-text="Add data flow in the sentiment analysis model.":::

1. In the **Add data** pane, choose the semantic type **Feedback** from the list.

   :::image type="content" source="media/sentiment-add-feedback-activities.png" alt-text="Configuration step to select feedback activities for sentiment analysis.":::

1. Select the activities to use for this sentiment analysis, then select **Next**.
 
1. Map the attributes in your data to the model attributes. Select **Save** to apply your selections. 

1. You see the status of data mapping. Select **Next** to continue. 

1. In the **Review your model details** step, validate the configuration of your sentiment analysis. You can go back to any part of the prediction configuration. Select **Save and run** to start the analysis. 

   :::image type="content" source="media/sentiment-model-review-config.png" alt-text="Review step for the sentiment model showing all configured items.":::

1. Select **Done** to leave the configuration experience. The process may take several hours to complete depending on the amount of data used. 

## Review analysis status

1.	Go to **Intelligence** > **Predictions** and select the **My predictions** tab.
2.	Select the prediction you want to review.
- **Prediction name**: Name of the prediction provided when creating it.
- **Prediction type**: Type of model used for the prediction.
- **Output entity**: Name of the entity to store the output of the prediction. Go to **Data** > **Entities** to find the entity with this name.
- **Predicted field**: This field is populated only for some types of predictions, and isn't used in customer lifetime value prediction.
- **Status**: Status of the prediction run.
  - **Queued**: Prediction is waiting for other processes to complete.
  - **Refreshing**: Prediction is currently running to create results that will flow into the output entity.
  - **Failed**: Prediction run has failed. Review the logs for more details.
  - **Succeeded**: Prediction has succeeded. Select View under the vertical ellipses to review the prediction results.
- **Edited**: The date the configuration for the prediction was changed.
- **Last refreshed**: The date the prediction had refreshed results in the output entity.

## Manage sentiment analysis

You can optimize, troubleshoot, refresh, or delete predictions. Review an input data usability report to find out how to make a prediction faster and more reliable. For more information, see [Manage predictions](manage-predictions.md).

## Review analysis results
 
1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab. 
1. Select the name of the prediction you want to review results for. In this case, select the sentiment analysis you want to review. 

### Summary tab

There are four primary sections of data within the results page. 

- **Average sentiment score**: Helps you understand the overall sentiment across all customers. Sentiment scores are grouped in three categories: 
  1.	Negative (-5 > 2)
  2.	Neutral (-1 > 1)
  3.	Positive (2 > 5) 
  
  :::image type="content" source="media/overall-customer-sentiment.png" alt-text="Visual representation of the overall customer sentiment.":::

- **Distribution of customers by sentiment score**: Customers are categorized into negative, neutral, and positive groups based on their sentiment scores. Hover over the bars in the histogram to see the number of customers and average sentiment score in each group. This data can help you [create segments of customers](segments.md) based on their sentiment scores.  

  :::image type="content" source="media/distribution-customer-sentiment.png" alt-text="Bar chart showing the customer sentiment across the three sentiment groups.":::

- **Average sentiment score over time**: Customer sentiment may change over time. We provide trends in your customers’ sentiments for the time range of your data. This view can help you gauge the effect of seasonal promotions, product launches, or other time-bound interventions on customer sentiment. See the graph by selecting the year-of-interest from the dropdown menu. 

  :::image type="content" source="media/sentiment-score-over-time.png" alt-text="History chart with the sentiment score over time represented as a line.":::
 
- **Sentiment across business aspects**: This table lists the average sentiment across business aspects. It can help you gauge which aspects of your business already satisfy customers or aspects that require more attention. Feedback records that don't align to any of the supported business aspects are categorized under **Other**. The table is sorted alphabetically by default. You can modify the sorting by selecting a table header.

  :::image type="content" source="media/sentiment-across-business-aspects.png" alt-text="List of business aspects with the associated sentiment value and the number of customers mentioning it.":::
 
  Select the name of a business aspect to see additional information how a business aspect is identified by the model. There are two parts in this pane: 

  - **Influential words**: Shows the top words that influenced the AI model’s identification of a business aspect in customer feedback. 
    **Show offensive words**: Lets you include offensive words in the list from original customer feedback data. By default, it's turned off.  Offensive word masking is powered by an AI model and may not detect all offensive words. We continue iterating and training the classifier for optimal performance. If you detect an offensive word that wasn't filtered as expected, let us know. 
    
    :::image type="content" source="media/offensive-words-sentiment.png" alt-text="List of influential words with the toggle to show or hide offensive words.":::
 
  - **Feedback samples**: Shows actual feedback records in your data. Words are color-coded according to their influence on the identification of a business aspect. 


### Influential words analysis tab

There are three sections of additional information that explain how the sentiment model works.
  
1. **Top words contributing to positive sentiment**: Shows top words that influenced the AI model’s identification of positive sentiment in customer feedback.  
2. **Top words contributing to negative sentiment**: Shows top words that influenced the AI model’s identification of negative sentiment in customer feedback.  
3. **Feedback samples**: Shows actual feedback records, one with a negative sentiment and one with a positive sentiment. Words in the feedback records are highlighted according to their contribution to the assigned sentiment score. Words that contribute to a positive sentiment score are highlighted in green. Words contributing to a negative score are highlighted in red.
   Select **See more** to load more feedback samples that provide more information and context of how the sentiment model works.
   
   :::image type="content" source="media/sentiment-feedback-samples.png" alt-text="Examples of sentiment analysis on customer feedback.":::
 
**Show offensive words**: Lets you include offensive words in the list from original customer feedback data. By default, it's turned off.  Offensive word masking is powered by an AI model and may not detect all offensive words. We continue iterating and training the classifier for optimal performance. If you detect an offensive word that wasn't filtered as expected, let us know. 

## Act on analysis results

You can easily start creating new segments of customers from the sentiment analysis results page by selecting **Create segments** at the top of the model result page.

:::image type="content" source="media/create-segment-model.png" alt-text="Command bar with options on prediction models.":::
 
## Potential bias

As with any feature that uses predictive artificial intelligence, you should be aware of potential bias in the data you use to predict customer sentiment. For example, if you only collect feedback digitally, you could miss feedback from customers who primarily conduct business with you in person, which could affect the feature’s output.

As this feature uses automated means to evaluate data and make predictions based on that data, it therefore has the capability to be used as a method of profiling, as that term is defined by the General Data Protection Regulation ("GDPR"). Your use of this feature to process data may be subject to GDPR or other laws or regulations. You are responsible for ensuring that your use of Dynamics 365 Customer Insights, including sentiment analysis, complies with all applicable laws and regulations, including laws related to privacy, personal data, biometric data, data protection, and confidentiality of communications.

[!INCLUDE[footer-include](../includes/footer-banner.md)]

