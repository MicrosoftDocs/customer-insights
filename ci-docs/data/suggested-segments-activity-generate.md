---
title: Generate and manage suggested segments based on activity (preview)
description: Generate suggested segments based on customer activity data 
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.topic: how-to
ms.date: 09/01/2023
ms.custom: bap-template
---

# Generate and manage suggested segments based on activity (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Find suggested segments based on activity. For more information, see [Suggested segments based on activity](suggested-segments.md).

## Required data

Suggestions are generated based on the selected input data.

- Customer profiles: All customers or members of a specific segment.

- Time period: Last month, last year, or any custom time frame.

- Activity type: purchases, retail transactions, online transactions, customer support cases, subscriptions, and so on.  

- Table in Dynamics 365 Customer Insights - Data that contains the activity data: The UnifiedActivity table or the table for a specific activity.

- Dimensions to include: Recency, frequency, or monetary dimension, depending on your business requirements.

## Generate suggested segments based on activity

1. Go to **Insights** > **Segments** and select the **Suggestions (preview)** tab.

1. Select **Find new suggestions** and choose **See or anticipate customer behavior**. Select **Start**.

   :::image type="content" source="media/suggested-segments-activity-wizard.png" alt-text="First step of the configuration wizard for a suggested segment based on activity.":::

1. Provide the required input data and select **Next**.

   - Choose customers: Include all customers or a specific segment.
   - Choose activity: Select the activity type and the tables that describe the activity.
   - Preferences: Set the time period to consider, the factors for suggestions, and map the attributes.

1. Review your input and select **Run** to run the model and generate suggestions.

Depending on the number of customer profiles and selected activities, it can take a few minutes to complete.

After generating the suggestions, you can filter them by the dimension or value you're most interested in.

## Manage suggested segments based on activity

Go to **Insights** > **Segments** and select the **Suggestions (preview)** tab. In the **Activity-based suggestions** section, select a suggested segment to view available actions.

- **See suggestion** to view the details of that segment like the extent of each dimension in comparison to the target group. It also highlights the number of potential members in the segment and the corresponding percentage of the total customers.
- **Create segment** to save the suggested as a segment. It displays on the **All segments** tab and can be [refreshed or deleted](segments.md). You can't edit the segment details. However, you can change the input criteria for the suggestions and generate different suggestions.
- **Edit suggestions** to modify the configured attributes which will replace the current suggestions.
- **Refresh suggestions** to refresh the suggestions while keeping configured attributes.

[!INCLUDE [footer-include](includes/footer-banner.md)]
