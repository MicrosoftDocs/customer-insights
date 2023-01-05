---
title: "Suggested segments based on measures (preview)"
description: "Let machine learning help you find new and interesting segments based on customer attributes."
author: JimsonChalissery
ms.author: jimsonc
manager: shellyha
ms.reviewer: v-wendysmith
ms.service: customer-insights
ms.subservice: audience-insights

ms.date: 01/05/2023
ms.topic: conceptual
ms.custom: bap-template
searchScope: 
  - ci-segment-suggestions
  - customerInsights
---

# Suggested segments based on measures (preview)

Discover interesting segments of your customers with the help of an AI model. This machine learning powered feature suggests segments based on measures or customer attributes. It can help improve your Key Performance Indicators (KPIs) or better understand the influence of attributes in context of other attributes.

> [!NOTE]
> The suggested segments feature uses automated means to evaluate data and make predictions based on that data. Therefore, it has the capability to be used as a method of profiling, as that term is defined by the General Data Protection Regulation ("GDPR"). Your use of this feature to process data may be subject to GDPR or other laws or regulations. You are responsible for ensuring that your use of Dynamics 365 Customer Insights, including this feature, complies with all applicable laws and regulations, including laws related to privacy, personal data, biometric data, data protection, and confidentiality of communications.

:::image type="content" source="media/suggested-segments.png" alt-text="Suggested segments page that shows details of a suggestion in a side pane.":::

## Suggested segments to improve your KPIs

If you use [measures created](measures.md) to help track your KPIs, create segments to view the influences on the KPI. You can use this information to run a highly targeted campaign.

For example, you track a measure called *TotalSpendPerCustomer*. As a business, you’d like to see this number grow. Choosing a measure as primary attribute, select the attributes that you want to assess for influence. Let's say *membership tier*, *membership period*, and *occupation*. Customer Insights can then suggest a segment that tells you who are the biggest influence of that measure. For example, *Accountants* who are *Gold* members, and who have been with your business for *at least five years* are the biggest influencer of *TotalSpendPerCustomer*. You’ll get an estimated segment size for every suggestion. You can use this information to create campaigns for the targeted audiences.

## Understand what influences a customer attribute

You can choose a customer attribute instead of a measure as the primary attribute. Based on your choice of influencing attributes, the AI model creates a series of suggestions that show how the selected attributes influence the primary attribute.

For example, you choose *Rewards Member (Yes/No)* as the primary attribute. *Tenure*, *Occupation*, and *Number of Support Tickets* are set as other influencing attributes. The AI model could suggest segments indicating mostly IT professionals with tenure over two years are rewards members. Another suggestion could highlight that accountants with tenure over one year and fewer than three support tickets are rewards members.

## Artificial intelligence usage

Using the primary attribute and influencing attributes, a decision tree algorithm suggests interesting segments. The suggestions are based on rules or patterns that were picked up by the AI algorithm. Only segments that significantly differ from the average population are shown as suggestions. The comparison to the average population is based on the selected measure or primary attribute.

### Responsible AI

With suggested segments, you select attributes to create new segments and process the data you select. When choosing attributes, including sensitive attributes like race, sexual orientation, or gender, you must ensure that you can and should process that data. You are responsible to comply with any laws applicable to your organization and adhere to your organization’s principles and privacy policies.

### Different results for primary attributes with categorical and numeric values

Segment suggestions are different if you choose a numeric attribute or a categorical attribute as the primary attribute. Values in a categorical attribute contain two or more categories or types. A numeric attribute contains quantitative data and has a sense of measurement associated with it.

With a numeric attribute like *annual income* or *membership period* as the primary attribute, the system suggests segments that have a higher or lower average value of the numeric attribute when compared to all customers.

A categorical attribute like *customer satisfaction* as the primary attribute results in suggested segments that have a higher or lower percentage of customers belonging to a particular category when compared to the percentage of all customers belonging to that same category. For example, *customer satisfaction* is chosen as the primary attribute and it consists of three categories (*Low*, *Medium* and *High*). For each category, segments will be suggested that have a higher or lower percentage of customers belonging to that category as compared to the proportion of all customers in the same category. If 22% of all customers have a *High* satisfaction, then, only segments that have a higher or lower proportion of customers with a *High* satisfaction as compared to 22% will be suggested for that category. Similarly, segments will be suggested for each of the other categories (*Low* and *Medium*) if they are statistically significant.

> [!NOTE]
> Currently, we only support primary categorical attributes that have up to 10 categories. If you want to see segment suggestions based on a primary attribute with more than 10 categories, we recommend grouping some of the categories to reduce the number of categories to 10 or fewer. This limitation only applies to primary attributes. For influencing categorical attributes, we currently support a maximum of 100 categories.


## Next steps

- [Generate segments based on measures](-suggested-segments-generate.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
