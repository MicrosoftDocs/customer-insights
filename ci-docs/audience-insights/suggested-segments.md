---
title: "Machine learning powered suggested segments"
description: "Let machine learning help you find new and interesting segments based on customer attributes."
ms.date: 01/27/2021
ms.reviewer: jimsonc
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Suggested segments (preview)

Discover interesting segments of your customers with the help of an AI model. This machine learning powered feature suggests segments based on measures or customer attributes, to improve your KPIs. 

> [!NOTE]
> The suggested segments feature uses automated means to evaluate data and make predictions based on that data, and therefore has the capability to be used as a method of profiling, as that term is defined by the General Data Protection Regulation ("GDPR"). Your use of this feature to process data may be subject to GDPR or other laws or regulations. You are responsible for ensuring that your use of Dynamics 365 Customer Insights, including this feature, complies with all applicable laws and regulations, including laws related to privacy, personal data, biometric data, data protection, and confidentiality of communications.

## Measure based suggested segments

Measures that capture customer interactions (purchases, reviews, etc.) help create suggestions based on customer activity information. Using common operators like SUM, AVG, MAX, MIN, and COUNT UNIQUE when creating a measure help you build specific measures. Identifying segments of your customers that influence a KPI (a [customer measure created](measures.md) in Customer Insights) can help you run a highly targeted campaign.  Based on budget and location constraints, it's important to understand how certain attributes influence this KPI.    
For example, you track a measure called *TotalSpendPerCustomer*. As a business, you’d like to see this number grow. After choosing a measure as primary attribute, you can select the attributes that you want to assess for influence. For example, *membership tier*, *membership period*, and *occupation*. Customer Insights can then suggest a segment that tells you who are the biggest influence of that measure. For example, *Accountants* who are *Gold* members, and who have been with your business for *at least five years* are the biggest influencer of *TotalSpendPerCustomer*. For all suggestions, you’ll get an estimated segment size. This information helps determining what kind of campaign might work best for that audience in your business constraints.

## Customer attribute based suggested segments

You can choose a customer attribute instead of a measure as the primary attribute. Based on your choice of influencing attributes, the AI model creates a series of suggestions that show how the selected attributes influence the primary attribute. 
For example, you choose *Housing(Yes/No)* as the primary attribute. *annual income* and *education level* are set as influencing attributes. The AI model can suggest segments that indicate mostly people with and income over *$100,000* and a *Bachelor's degree* who own houses. 

## Artificial intelligence usage

Using the primary attribute and influencing attributes, a decision tree algorithm suggests interesting segments. The suggestions are based on rules or patterns that were picked up by the AI algorithm. Only segments that significantly differ from the average population are shown as suggestions. The comparison to the average population is based on the selected measure or primary attribute.

### Responsible AI

Suggested segments lets you select attributes to create new segments will process the data you select. When choosing attributes, including sensitive attributes such as race, sexual orientation, or gender, you are responsible for ensuring that you can and should process that data in a manner that is compliant with any laws applicable to your organization and consistent with your organization’s principles and privacy policies.

### Different results for primary attributes with categorical and numeric values

Segment suggestions are different if you choose a numeric attribute or a categorical attribute as the primary attribute. Values in a categorical attribute contain two or more categories or types. A numeric attribute contains quantitative data and has a sense of measurement associated with it.

With a numeric attribute like *annual income* or *membership period* as the primary attribute, the system suggests segments that have a higher or lower average value of the numeric attribute when compared to all customers.

A categorical attribute like *education level* set as the primary attribute, results in suggested segments that have a higher or lower percentage of customers belonging to a particular category when compared to the percentage of all customers belonging to that same category. For example,  *education level* consists of seven categories. *16%* of all customers have an education level of *Bachelor’s degree*. The system suggests segments that have a bigger or smaller proportion of customers with a *Bachelor's degree*. Additionally, segments will be suggested for all other, if they are statistically significant.

> [!IMPORTANT]
> Only categorical attributes that have at most 10 categories are supported.

## Generate suggested segments

1. Go to **Segments**.

1. Select the **Suggestions (preview)** tab.

1. Select **Get suggestions** to start the guided experience.

1. Choose a measure or a customer attribute as the primary attribute and select **Next**.

1. Select the influencing attributes and select **Save**.
   
   > [!TIP]
   > Selecting multiple influencing attributes improved the chances of evaluating how they influence the primary attribute.

1. It will take moment to process the selected attributes. 

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

### Known Issues

1. Estimated segment size mismatch: If you choose a primary attribute that contains empty values, it can affect the estimated segment size in the segment suggestions. When saving such segment, the actual segment size can be different to the original estimation.
 
2. Boolean type primary attributes don't work: Currently, we only support string and numeric types of data as the primary attribute.

3. Suggested segments aren't distinct enough: Keep in mind that the selected attributes and the distribution of values of those attributes influences the results.


<!-- turn into a troubleshooting section or remove. It's private preview focus

## FAQ 

**Why am I seeing only a few suggestions? I have lot of data/profiles**

*The AI model used tries to determine if the suggestions shown to you are statistically significant. If deemed insignificant, the AI model will eliminate such suggestions from the output. We do this in order to present you with a set of suggestions that are likely to offer you the best value/outcome.* 

*To try and get the AI model to give you better suggestions, you can try changing your influencing attributes or even your primary attribute.*

**The suggestions I see does not make any sense or I’m not able to understand/interpret these suggestions?**

*We’d be more than happy to understand why you feel so. Please contact us so that we can try and schedule some time to go over your observations and feedback*

**Is it ok to just select all attributes and measures as influencing attributes?**

*Recommendation would be to include all attributes that have a potential to influence the primary attribute. For instance, if all your customers are from the US and if country is an available attribute for selection, this attribute will not have any measurable impact on the outcome and can be left out.  Moreover, you should ensure that any attributes you select can and should be processed in a manner that is compliant with any laws applicable to your organization and consistent with your organization’s principles and privacy policies.*

**How much time do I need to wait before I can see results?**

*Depending on the number of customer profiles you have and the number of attributes you’ve selected, it can take several minutes. However if you do not see results after an hour and no error is shown, please contact us.*

**I see this error that I don’t understand, what do I do?**

*Please contact us with the following details*

- *Your CI instance ID*
- *A screenshot of the error you are seeing*
- *A description of the steps you took before you encountered the error, preferably with the specific inputs you provided or selections you made on the page*
- *Also mention if this was a 1 time occurrence*

**This feature is not working for me, what do I do?**

*Please contact us with the following details*

- *Your CI instance ID*
- *A screenshot of the error you are seeing*
- *A description of the steps you took before you encountered the error, preferably with the specific inputs you provided or selections you made on the page*
- *Also mention if this was a 1 time occurrence*


-->
