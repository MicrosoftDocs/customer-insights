---
title: "Machine learning powered suggested segments"
description: "Let machine learning help you find new and interesting segments based on customer attributes."
ms.date: 02/01/2021
ms.reviewer: jimsonc
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Suggested segments (preview)

Discover interesting segments of your customers with the help of an AI model. This machine learning powered feature suggests segments based on measures or customer attributes. Io can help improve your KPIs or better understand the influence of attributes in context of other attributes. 

> [!NOTE]
> The suggested segments feature uses automated means to evaluate data and make predictions based on that data, and therefore has the capability to be used as a method of profiling, as that term is defined by the General Data Protection Regulation ("GDPR"). Your use of this feature to process data may be subject to GDPR or other laws or regulations. You are responsible for ensuring that your use of Dynamics 365 Customer Insights, including this feature, complies with all applicable laws and regulations, including laws related to privacy, personal data, biometric data, data protection, and confidentiality of communications.

:::image type="content" source="media/suggested-segments-details.png" alt-text="Suggested segments page in Customer Insights showing details of a suggestion in a side pane.":::

## Suggested segments to improve your KPIs

As a user of audience insights, you likely have a series of [measures created](measures.md) that help track your Key Performance Indicators (KPIs). It's important to understand how certain attributes influence this KPI to create segments and run a highly targeted campaign.   
For example, you track a measure called *TotalSpendPerCustomer*. As a business, you’d like to see this number grow. Choosing a measure as primary attribute, lets you select the attributes that you want to assess for influence. Let's say *membership tier*, *membership period*, and *occupation*. Customer Insights can then suggest a segment that tells you who are the biggest influence of that measure. For example, *Accountants* who are *Gold* members, and who have been with your business for *at least five years* are the biggest influencer of *TotalSpendPerCustomer*. You’ll get an estimated segment size for every suggestion. You can use this information to create campaigns for the targeted audiences.

## Understand what influences a customer attribute

You can choose a customer attribute instead of a measure as the primary attribute. Based on your choice of influencing attributes, the AI model creates a series of suggestions that show how the selected attributes influence the primary attribute.   
For example, you choose *Rewards Member (Yes/No)* as the primary attribute. *Tenure*, *Occupation*, and *Number of Support Tickets* are set as other influencing attributes. The AI model could suggest segments indicating mostly IT professionals with tenure over two years are rewards members. Another suggestion could highlight that accountants with tenure over one year and fewer than three support tickets are rewards members. 

## Artificial intelligence usage

Using the primary attribute and influencing attributes, a decision tree algorithm suggests interesting segments. The suggestions are based on rules or patterns that were picked up by the AI algorithm. Only segments that significantly differ from the average population are shown as suggestions. The comparison to the average population is based on the selected measure or primary attribute.

### Responsible AI

Suggested segments lets you select attributes to create new segments and process the data you select. When choosing attributes, including sensitive attributes like race, sexual orientation, or gender, you must ensure that you can and should process that data. You are responsible to comply with any laws applicable to your organization and adhere to your organization’s principles and privacy policies.

### Different results for primary attributes with categorical and numeric values

Segment suggestions are different if you choose a numeric attribute or a categorical attribute as the primary attribute. Values in a categorical attribute contain two or more categories or types. A numeric attribute contains quantitative data and has a sense of measurement associated with it.

With a numeric attribute like *annual income* or *membership period* as the primary attribute, the system suggests segments that have a higher or lower average value of the numeric attribute when compared to all customers.

A categorical attribute like *customer satisfaction* as the primary attribute results in suggested segments that have a higher or lower percentage of customers belonging to a particular category when compared to the percentage of all customers belonging to that same category. For example, *customer satisfaction* is chosen as the primary attribute and it consists of three categories (*Low*, *Medium* and *High*). For each category, segments will be suggested that have a significantly higher or lower percentage of customers belonging to that category as compared to the proportion of all customers belonging to the same category. If 22% of all customers have a *High* satisfaction, then, only segments that have a significantly higher or lower proportion of customers with a *High* satisfaction as compared to 22% will be suggested for that category. Similarly, segments will be suggested for each of the other categories (*Low* and *Medium*) if they are statistically significant.

> [!IMPORTANT]
> Only categorical attributes that have at most 10 categories are supported.

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

Once the AI model has generated the suggestions, you'll find them listed on **Segments** > **Suggestions (preview)**.
 
Select a suggested segment to review the details of that suggestion including a comparison of the average value and the number of segment members. You can also review the attribute values or rules that the AI model learned to suggest the selected segment.

## Save a suggestion as a segment

1. Go to **Segments** > **Suggestions (preview)**.

1. Select the segment you want to save. 

1. In the side pane, select **Save as segment**. 

1. After saving the segment, it will show in the list of segments on the **All segments** tab. It can now be [refreshed, edited, or deleted like any other segment](segments.md).

## Refresh or edit a set of suggestions

1. Go to **Segments** > **Suggestions (preview)**.

1. Select **Refresh suggestions** to refresh the suggestions while keeping configured attributes. Or select **Edit attributes** to modify the configured attributes. The system will rerun the AI model, generate segment suggestions based on the latest data, and replace the current suggestions.

## Limitations

1. Estimated segment size mismatch: If you choose a primary attribute that contains empty values, it can affect the estimated segment size in the segment suggestions. When saving such segment, the actual segment size can be different to the original estimation.
 
2. Boolean type primary attributes don't work: Currently, we only support string and numeric types of data as the primary attribute.

3. Suggested segments aren't distinct enough: Keep in mind that the selected attributes and the distribution of values of those attributes influences the results. You can change your influencing attributes or even your primary attribute to get different results.

