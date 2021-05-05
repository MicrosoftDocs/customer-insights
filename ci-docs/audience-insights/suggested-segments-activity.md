---
title: "Suggested segments based on activity."
description: "Let machine learning help you find new and interesting segments based on customer activity."
ms.date: 05/05/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
manager: shellyha
---

# Suggested segments (preview)

Discover interesting segments of your customers with the help of an AI model. In addition to suggesting segments that can help you improve a KPI or measure or better understand what influences an attribute, we now have a way to suggest segments that you can create based on customer activity data that you bring in – this could be transaction data, support call duration data, etc. We do this by analyzing your activity/engagement/transaction data along the 3 dimensions of Recency, Frequency and Monetary value (or Time duration).  

## Suggested segments to categorize your customers by activity

As a customer of CI, you likely have various activity data that you have brought in into CI. With this new feature, CI can now suggest segments that represent cohorts like: 

your most active customers 

customers that have made the most purchases 

customers that brought you the most revenue 

customers who haven’t been active lately 

customers who frequent your business  

For example, say you have a retail business and you’d like to understand  

who are your most frequent customers so that you can run a survey to understand what needs to be improved 

who brings in the most sales in any given month, maybe you want to reward them with a coupon 

who are you occasional customers, maybe you want to offer them a chance to join the rewards program to entice them to visit your business more often 

who are your top customers (maybe ones that frequent your business most often, brings in the most sales and have been active very recently) 

As another example, say you are in the healthcare business providing public healthcare. Your goal is to reduce patient care expense, reduce recurring visits by providing holistic care in as few visits as possible, etc. In this case you might be interested in c 

customers that have had to visit you less often  

customers who have lower recurring costs + have to visit less often + haven’t had to visit in a while, maybe these are your ideal/top customers 

customers who have high recurring costs, maybe you want to understand what is going on with these customers 

## H ow does this work? 

Suggestions are generated based on the following input that you provide: 

Who should this analysis be carried out on? For ex.: all your customers or customers from a specific segment? 

What time period do you want to do the analysis for? For ex.: Last month, last 3 months, last year, or holiday period of 2020 etc. 

Which activity do you want to do this analysis on (dependent on the activity data you have ingested into CI)? For ex.: purchases, retail transactions, online transactions, customer support incidents, subscriptions etc.  

Which entity/table/datset in CI contains this data? For ex.: unified activity entity or the new activity specific entity 

Which dimensions do you want to include in this analysis? For ex.: Recency +  Frequency + Monetary (coz you have data along all these dimensions) OR Recency + Frequency (coz your business relies on high volumes and hence these two factors are most important for you) OR Frequency only, etc 

Once the suggestions have been generated, depending on your business goal, you can quickly filter for the desired set of suggestions by filtering the dimension you are most interested in among Recency, Frequency and Monetary. You can also filter based on high, medium or low, the 3 buckets we use to classify users along the 3 dimensions. 

Once you see the desired suggestions, you can save them as segments to then initiate a campaign or activate the segment in another tool or service. 

## Generate suggested segments

1. Go to **Segments**.

1. Select the **Suggestions (preview)** tab.

1. Select **Get new suggestions** to start the guided experience.

1. Choose a measure or a customer attribute as the primary attribute and select **Next**.

   :::image type="content" source="media/suggested-segments-primary-attribute.png" alt-text="Choosing the primary attribute for suggestions on the suggested segments.":::

1. Select the influencing attributes and select **Save**.
   
   > [!TIP]
   > Selecting multiple influencing attributes improves the chances of evaluating how they influence the primary attribute. Don't include attributes that have no influence the primary attribute. For example, if all your customers are from a specific country, don't include the *country* attribute because it won't have any impact on the output.

1. Depending on the number of customer profiles and selected attributes, it can take a few minutes to process the selected attributes. 

## View details of a suggested segment

Once the AI model has generated the suggestions, you'll find them listed on **Segments** > **Suggestions (preview)** in the **Activity based suggestions** section.

<screenshot>

Select any suggested segment to view the details of that segment in the side panel. The side panel provides details like the extent of each dimension (recency, frequency and/or monetary) in comparison to the target group. It also highlights the number of members in the segment and the corresponding percentage of the total customers.    

## Save a suggestion as a segment

1. Go to **Segments** > **Suggestions (preview)**.

1. Select the segment you want to save. 

1. In the side pane, select **Save as segment**. 

1. After saving the segment, it will show in the list of segments on the **All segments** tab. It can now be [refreshed, edited, or deleted like any other segment](segments.md).

## Refresh or edit a set of suggestions

1. Go to **Segments** > **Suggestions (preview)** and look for the segment in the **Activity based suggestions** section.

1. Select **Refresh suggestions** to refresh the suggestions while keeping configured attributes. Or select **Edit attributes** to modify the configured attributes. The system will rerun the AI model, generate segment suggestions based on the latest data, and replace the current suggestions.

## Known Issues  

The following are some known issues in the feature. These will be fixed before we hit Public Preview. 

A saved activity based segment cannot be edited:  The workaround would be to start from a new set of suggestions, where the inputs have been sufficiently tweaked to reflect the edits you want to perform on the segment. 

While we do our best to not suggest segments that are not distinct enough, do keep in mind that the attributes selected and the distribution of values of those attributes will influence the outcome. We are looking at ways to improve this. 

 

## FAQ  

How much time do I need to wait before I can see results? 

Depending on the number of customer profiles you have and the amount of activity data you’ve selected, it can take several minutes. However if you do not see results after an hour and no error is shown, please contact us. 

 

How can I limit the number of suggestions?  

Use filters to limit suggestions that reflect your priorities. 



[!INCLUDE[footer-include](../includes/footer-banner.md)]