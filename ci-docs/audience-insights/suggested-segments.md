
# ML Powered Suggested Segments (preview)

## What are suggested segments?
We now have a new way for you to create Segments in CI. This machine learning powered feature is one of the first in a series of features aimed at making it easy for you to identify interesting segments of your customers. We use an AI model to suggest segments that you can create, making it easy to discover segments that presents high opportunity.

>### Note
>
>The suggested segments feature uses automated means to evaluate data and make predictions based on that data, and therefore has the capability to be used as a method of profiling, as that term is defined by the General Data Protection Regulation ("GDPR"). Your use of this feature to process data may be subject to GDPR or other laws or regulations. You are responsible for ensuring that your use of Dynamics 365 Customer Insights, including this feature, complies with all applicable laws and regulations, including laws related to privacy, personal data, biometric data, data protection, and confidentiality of communications.

## What’s in it for me?

### Improve your KPI

As a customer of CI, you likely have a series of measures created that helps track your KPIs (Key Performance Indicator). With this new feature, using an AI model, CI can suggest segments that can help you improve that KPI.

For example, Let’s say you have a KPI (or a customer measure created in CI) called ***TotalSpendPerCustomer***. As a business, you’d like to see this grow/improve. And for that you need to identify segments of your customers that influences this KPI, so that you can run a highly targeted campaign. Based on budget and location constraints, say you want to understand how certain attributes influence this KPI. You can now pick your KPI, and pick the attributes that you want to assess for influence, say ***membership tier***, ***membership period*** & ***occupation***. Customer Insights can then suggest a segment that tells you that ***Accountants*** who are ***Gold*** members, and who have been with your business for ***at least 5*** years are the biggest influencer of ***TotalSpendPerCustomer***. Another suggestion it might tell you is that ***IT professionals*** who are ***Silver*** members, who have been with your business for ***at least 1*** year comes next in terms of influence on ***TotalSpendPerCustomer***. And for each of these suggestions, you’ll also get an estimated segment size, that you can then use to determine what kind of campaign might work best for that size of audience, given the budget you have. In this manner, the AI model can help you discover interesting segments of your customers that you can then use to potentially run a highly targeted campaign to improve engagement with those customers helping you improve that KPI.

### Understand influencing attributes for a chosen customer attribute

If you decide to pick a customer attribute, instead of a measure as the primary attribute, then based on your choice of additional influencing attributes, the AI model can showcase a series of suggestions that highlight how these additional attributes influence the primary attribute. 
For example, let’s say you select ***Housing(Yes/No)*** as the primary attribute, and ***Annual Income*** and ***Education*** as additional influencing attributes. This time the AI model can suggest segments that indicate that it’s mostly those with income over ***$100,000*** and completed ***Bachelors*** degree that own houses. Those with income over ***$175,000***, and completed ***Masters*** degree are also home owners.

## Does this use artificial intelligence?

Based on the KPI/primary attribute specified by you and the corresponding influencing attributes chosen, behind the scenes, a decision tree algorithm highlights interesting segments based on rules or patterns that were picked up by the AI algorithm. Only those segments are shown as suggestions that significantly differ from the average population when compared based on the chosen KPI/primary attribute. The segment suggestions that fit your business use-case can then be saved and used to carry out targeted marketing campaigns or any other actions to drive your business goals.

## Choosing a categorical vs numeric attribute as the primary attribute

Segment suggestions are displayed slightly differently when you choose a numeric attribute as the primary attribute as compared to when you choose a categorical attribute.

A categorical attribute has two or more categories or types (generally qualitative) associated with it (eg - country, gender, marital status, etc). A numeric attribute, on the other hand, contains quantitative data and has a sense of measurement/magnitude associated with it (eg – age, purchase amount, etc). 

When you choose a numeric attribute like ***income*** or ***membership period*** as the primary attribute, those segments are suggested that have a significantly higher or lower average value of the numeric attribute when compared to the average value of the attribute across all customers. Eg – if ***membership period*** is chosen as the primary attribute and if the average membership period across all customers is 3 years then only those segments will be suggested that have a significantly higher or lower average membership period as compared to 3 years.

When you choose a categorical attribute like ***education level*** as the primary attribute,  segments are suggested that have a significantly higher or lower percentage of customers belonging to a particular category when compared to the percentage of all customers belonging to that same category. For instance if ***education*** level is chosen as the primary attribute and it comprises of 7 categories (***Elementary School***, ***Middle School***, ***High school*** diploma, ***Associate’s degree***, ***Bachelor's degree***, ***Master’s degree***, ***Doctoral degree***), then for each category, segments will be suggested that have a significantly higher or lower percentage of customers belonging to that category as compared to the proportion of all customers belonging to the same category - if ***16%*** of all customers have an education level of ***Master’s degree***, then, only those segments that have a significantly higher or lower proportion of customers with education level of ***Master's degree*** as compared to 16% will be suggested for that category. In a similar manner, segments will be suggested for each of the other 6 categories, if they are statistically significant.

>Note
>
> Only categorical attributes that have at most 10 categories are supported.

## Leveraging measures for improved suggestions

A good idea to get the most out of this new feature is to leverage customer measures as input attributes. By creating different measures that help capture customer interactions (purchases, reviews, customer service activity, etc.), you can obtain segment suggestions based on not only customer profile attributes, but also customer activity information.

The feature allows you to choose any of the customer profile attributes or measures created in Customer Insights as a primary attribute or influencing attributes. If not created already, you could leverage the following instructions to create various measures in Customer Insights that would help you use your customer activity data along with customer profile data to provide you segment suggestions (Link to Measures doc page).  

For any transactional activity table that is associated with your customers (eg - purchases, email campaigns, events, etc), you can define measures like SUM, AVG, MAX, MIN, and COUNT UNIQUE etc. COUNT UNIQUE can also be interesting in case you want to capture ‘variety’ per customer (for instance - the number of distinct products the customer has purchased).
By adding these additional customer attributes (via Measures) you will get the most out of this feature as the segments suggested by the AI model would be able to leverage these additional fields to find interesting groups of customers.

## Responsible AI

Suggested segments gives you control of what attributes you choose to create new segments and this feature will only process the data you select.  When choosing attributes, including sensitive attributes such as race, sexual orientation, or gender, you are responsible for ensuring that you can and should process that data in a manner that is compliant with any laws applicable to your organization and consistent with your organization’s principles and privacy policies.

## How do I do this?

### Create a set of suggestions

To start, navigate to the **Segments** area in Customer Insights

1. You now have a new tab ‘Suggestions (preview)’
2. Click on the tab to start creating your first set of suggestions
3. Fire up the wizard by clicking on ***Get suggestions*** in that tab
4. The wizard will to pick the primary attribute and the influencing attributes, and in either case, these could be customer attributes or measures
   
> **Pro tip**: Selecting a high number of influencing attributes will improve your chances of evaluating how all these attributes influence the primary attribute.

5. Once done, sit back and let CI compute the suggestions for you
6. Once the suggestions are available, you can click through each one to understand how each suggestion is determined and what are the influencers

### View a suggestion

1. Once the AI model has generated the suggestions, you'll find them listed under the Suggestions tab.
 
Select any suggested segment to view the details of that segment in the side panel. The side panel provides details like comparison of the average value of the chosen KPI/primary attribute for customers in the selected segment to the average value of the KPI/primary attribute across all customers. It also highlights the number of members in the segment and the corresponding percentage of the total customers. Finally, it showcases the attribute values or rules that the AI model learned that define the selected segment.

### Save a suggestion as a segment

To save a selected segment, click on Save as Segment in the details side panel. Once a segment is saved, you will be able to view it in the All Segments tab. The saved segment can then be used like any other segment that you create in CI. 


### Refresh or edit a set of suggestions

To refresh a set of suggestions while keeping the input attributes same, select Refresh suggestions in the action bar on the Suggestions tab. This will re-run the AI model to generate segment suggestions based on the latest data.
To edit a set of suggestions, select Edit attributes in the action bar. You can then modify any of the input attributes and run the AI model to get new segment suggestions.

> **Note**: When you refresh or edit a set of suggestions, if new suggestions are generated, they will replace your previous suggestions.

### Refresh, Edit or Delete a saved segment

You can refresh, edit or delete a saved suggested segment like any other segment from the All Segments tab. 

### Known Issues

The following are some known issues in the feature. These will be fixed before we hit Public Preview.

1. Estimated segment size mismatch: If you choose a primary attribute that has too many empty values, that might affect the estimated segment size shown to you in the generated segment suggestions. On saving such a segment, you might observe that the real segment size significantly varies as compared to the estimated size that was shown. We are in the process of fixing this and the fix should be enabled soon in the product
 
2. No support for boolean type primary attribute: As of now, we only support string and numeric types of data to be chosen as the primary attribute and not boolean data. We should have this fixed in a couple of weeks.

3. While we do our best to not suggest segments that are not distinct enough, do keep in mind that the attributes selected and the distribution of values of those attributes will influence the outcome. We are looking at ways to improve this.


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



