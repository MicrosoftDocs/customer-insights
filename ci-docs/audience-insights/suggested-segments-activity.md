---
title: "Suggested segments based on activity."
description: "Let machine learning help you find new and interesting segments based on customer activity."
ms.date: 05/11/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
manager: shellyha
---

# Suggested segments based on activity data (preview)

Discover interesting segments of your customers based on customer activity data that is ingested to Customer Insights. Examples of activity data are transactions, support call duration, purchases, or returns. To suggest segments, activity data gets analyzed for recency, frequency, and monetary value (or duration). Alternatively, you can generate [suggested segments to improve a measure or better understand what influences an attribute](suggested-segments.md).

:::image type="content" source="media/suggested-segments-tab.png" alt-text="Suggested segments tab showing segment suggestions for activity-based and attribute-based segments.":::

## Categorize customers by activity

With [activity data](activities.md) available in Customer Insights, we can generate suggestions that represent customer groups:

- most active customers 
- customers that have made the most purchases 
- customers that generated the most revenue 
- customers who haven’t been active lately 
- customers who frequently interact with your business  

If you have a retail business, you could find out which customers generate the most revenue and reward them with a coupon. Or you can identify occasional customers and offer them to join a rewards program so they visit your business more often.
If you're in the healthcare business providing public healthcare and your goal is to minimize the expenses for individual patients. A way to do so could be to reduce recurring visits by providing best possible care in as few visits as possible. In this case, your goal is to keep the visit frequency low and minimize recurring cost for the patients. Or you can identify segments of patients who have frequent appointments and high recurring costs and analyze these cases to improve the treatment of the individual. 

## Required data

Suggestions are generated based on the selected input data. 

- Customer profiles: All customers or members of a specific segment. 

- Time period: Last month, last year, or any custom time frame.

- Activity type: purchases, retail transactions, online transactions, customer support cases, subscriptions, and so on.  

- Entity in Customer Insights that contains the activity data: The UnifiedActivity entity for a specific activity. 

- Dimensions to include: Recency, frequency, or monetary dimension, depending on your business requirements.

## Generate suggested segments

1. Go to **Segments**.

1. Select the **Suggestions (preview)** tab.

1. Select **Find new suggestions** and choose **See or anticipate customer behavior**. Select **Start** to run the guided experience.

   :::image type="content" source="media/suggested-segments-activity-wizard.png" alt-text="First step of the configuration wizard for a suggested segment based on activity.":::

1. Provide the required input data and select **Next** proceed.

   - Choose customers: Include all customers or a specific segment.
   - Choose activity: Select the activity type and the entities that describe the activity.
   - Preferences: Set the time period to consider, the factors for suggestions, and map the attributes.

1. Review your input and select **Run** to run the model and generate suggestions.

1. Depending on the number of customer profiles and selected activities, it can take a few minutes to complete. 

After generating the suggestions, you can filter them by the dimension or value you're most interested in. 

## View details of a suggested segment

Once the AI model has generated the suggestions, you'll find them listed on **Segments** > **Suggestions (preview)** in the **Activity based suggestions** section.

:::image type="content" source="media/suggested-segments-details.png" alt-text="Expanded side pane showing detailed data of a suggested segment.":::

Select **See suggestion** on a suggested segment to view the details of that segment. The side pane provides details like the extent of each dimension in comparison to the target group. It also highlights the number of potential members in the segment and the corresponding percentage of the total customers. If you want to keep the suggestion as a segment, select **Create segment**.    

## Save a suggestion as a segment

1. Go to **Segments** > **Suggestions (preview)**.

1. Select the segment you want to save. 

1. In the side pane, select **Create segment**. 

1. After saving the segment, it will show in the list of segments on the **All segments** tab. It can now be [refreshed, edited, or deleted like any other segment](segments.md).

## Refresh or edit a set of suggestions

1. Go to **Segments** > **Suggestions (preview)** and look for the segment in the **Activity based suggestions** section.

1. Select **Refresh suggestions** to refresh the suggestions while keeping configured attributes. Or select **Edit suggestions** to modify the configured attributes. The system will rerun the AI model, generate segment suggestions based on the latest data, and replace the current suggestions.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
