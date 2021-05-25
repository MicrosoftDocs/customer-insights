---
title: Customer lifetime value prediction sample guide
description: Use this sample guide to try out the customer lifetime value prediction model.
ms.date: 05/25/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: tutorial
author: yashlundia
ms.author: yalundia        
manager: shellyha
---

# **Customer lifetime value (CLV) prediction (preview) sample guide**

This guide will walk you through an end to end example of Customer lifetime value (CLV) prediction in Customer Insights using the data provided below. All data used in this guide is not real customer data and is part of the Contoso dataset found in the _Demo_ environment within your Customer Insights Subscription.

**Scenario**

Contoso is a company that produces high-quality coffee and coffee machines, which they sell through their Contoso Coffee website. Their goal is to understand the value (revenue) that each of their customers could bring in the next 12 months. Knowing the expected value of their customers in the next 12 months will help them prioritize and focus their marketing efforts on high value customers.

**Prerequisites**

- At least [Contributor permissions](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/permissions) in Customer Insights.
- We recommend that you implement the following steps [in a new environment](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/manage-environments).

**Task 1 - Ingest data**

Review the articles [about data ingestion](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/data-sources) and [importing data sources using Power Query connectors](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/connect-power-query) specifically. The following information assumes you familiarized with ingesting data in general.

**Ingest customer data from eCommerce platform**

1. Create a data source named  **eCommerce** , choose the import option, and select the  **Text/CSV**  connector.
2. Enter the URL for eCommerce contacts [https://aka.ms/ciadclasscontacts](https://aka.ms/ciadclasscontacts).
3. While editing the data, select  **Transform**  and then  **Use First Row as Headers**.
4. Update the datatype for the columns listed below:
  - **DateOfBirth** : Date
  - **CreatedOn** : Date/Time/Zone

[!div class=&quot;mx-imgBorder&quot;]  ![](RackMultipart20210502-4-11vawqk_html_fa7480cb4ad34fc1.png)

1. In the &#39;Name&#39; field on the right-hand pane, rename your data source from  **Query**  to  **eCommerceContacts**
2. Save the data source.

**Ingest online purchase data**

1. Add another data set to the same  **eCommerce**  data source. Choose the  **Text/CSV**  connector again.
2. Enter the URL for  **Online Purchases**  data [https://aka.ms/ciadclassonline](https://aka.ms/ciadclassonline).
3. While editing the data, select  **Transform**  and then  **Use First Row as Headers**.
4. Update the datatype for the columns listed below:
  - **PurchasedOn** : Date/Time
  - **TotalPrice** : Currency
5. In the &#39;Name&#39; field on the right-hand pane, rename your data source from  **Query**  to  **eCommercePurchases**.
6. Save the data source.

**Ingest customer data from loyalty schema**

1. Create a data source named  **LoyaltyScheme** , choose the import option, and select the  **Text/CSV**  connector.
2. Enter the URL for eCommerce contacts [https://aka.ms/ciadclasscustomerloyalty](https://aka.ms/ciadclasscustomerloyalty).
3. While editing the data, select  **Transform**  and then  **Use First Row as Headers**.
4. Update the datatype for the columns listed below:
  - **DateOfBirth** : Date
  - **RewardsPoints** : Whole Number
  - **CreatedOn** : Date/Time
5. In the &#39;Name&#39; field on the right-hand pane, rename your data source from  **Query**  to  **loyCustomers**.
6. Save the data source.

**Ingest customer data from Website Reviews**

1. Create a data source named  **Website** , choose the import option, and select the  **Text/CSV**  connector.
2. Enter the URL for eCommerce contacts https://aka.ms/CI-ILT/[WebReviews](https://aka.ms/CI-ILT/WebReviews).
3. While editing the data, select  **Transform**  and then  **Use First Row as Headers**.
4. Update the datatype for the columns listed below:
  - **ReviewRating** : Decimal number
  - **ReviewDate** : Date
5. In the &#39;Name&#39; field on the right-hand pane, rename your data source from  **Query**  to  **Reviews**.
6. Save the data source.

**Task 2 - Data unification**

After ingesting the data we now begin the  **Map, Match, Merge**  process to create a unified customer profile. For more information, see [Data unification](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/data-unification).

**Map**

1. After ingesting the data, map contacts from eCommerce and Loyalty data to common data types. Go to  **Data**  \&gt;  **Unify**  \&gt;  **Map**.
2. Select the entities that represent the customer profile –  **eCommerceContacts**  and  **loyCustomers**.

![](RackMultipart20210502-4-11vawqk_html_a4bead166755f31a.png)

1. Select  **ContactId**  as the primary key for  **eCommerceContacts**  and  **LoyaltyID**  as the primary key for  **loyCustomers**.

![](RackMultipart20210502-4-11vawqk_html_9e861c286b64289b.png)

**Match**

1. Go to the  **Match**  tab and select  **Set Order**.
2. In the  **Primary**  drop-down list, choose  **eCommerceContacts : eCommerce**  as the primary source and include all records.
3. In the  **Entity 2**  drop-down list, choose  **loyCustomers : LoyaltyScheme**  and include all records.

![](RackMultipart20210502-4-11vawqk_html_7833e5505d2302a6.png)

1. Select  **Create a new rule**
2. Add your first condition using FullName.
  - For eCommerceContacts select  **FullName**  in the drop-down.
  - For loyCustomers select  **FullName**  in the drop-down.
  - Select the  **Normalize**  drop down and choose **Type (Phone, Name, Address, ...)**.
  - Set  **Precision Level** :  **Basic**  and  **Value** :  **High**.
3. Enter the name  **FullName, Email**  for the new rule.
  - Add a second condition for email address by selecting  **Add Condition**
  - For entity eCommerceContacts, choose  **EMail**  in drop-down.
  - For entity loyCustomers, choose  **EMail**  in the drop-down.
  - Leave Normalize blank.
  - Set  **Precision Level** :  **Basic**  and  **Value** :  **High**.

![](RackMultipart20210502-4-11vawqk_html_772c0722c6a3fed7.png)

1. Select  **Save**  and  **Run**.

**Merge**

1. Go to the  **Merge**  tab.
2. On the  **ContactId**  for  **loyCustomers**  entity, change the display name to  **ContactIdLOYALTY**  to differentiate it from the other IDs ingested.

![](RackMultipart20210502-4-11vawqk_html_94381d100ad9cd6f.png)

1. Select  **Save**  and  **Run**  to start the Merge Process.

**Task 3 - Configure customer lifetime value prediction**

With the unified customer profiles in place, we can now run the customer lifetime value prediction. For detailed steps, see the [Customer Lifetime Value prediction (preview)](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/predict-customer-lifetime-value) article.

1. Go to  **Intelligence**  \&gt;  **Discover**  and select to use the  **Customer lifetime value model**.
2. Go through the information in the side panel and select  **Get started**.
3. Name the model  **OOB eCommerce CLV Prediction** and the output entity  **OOBeCommerceCLVPrediction**.
4. Next, define model preferences for the CLV model:
  - **Prediction time period** :  **12 months or 1 year**. This setting defines how far into the future do we want to predict customer lifetime value.
  - **Active customers:** Specify what Active customers mean for your business. Set the historical time frame in which a customer must have had at least one transaction to be considered active. The model will only predict CLV for active customers. From the dropdown, you can choose to either let the model calculate this time period based on your historical transaction data or you could choose to provide a specific time period. In this scenario, we will **let the model calculate purchase interval**.
  - **High value customers:** Define High value customers as a percentile of top-paying customers – the model uses this input to provide results that fit your business definition of high value customers. You could choose to rely on the model to define high value customers for your business (the model uses a heuristic rule to derive the percentile of top paying customers for your business) or you could define high value customers in terms of a percentile of top future paying customers. For this scenario, we will define high value customers as **top 30% of active paying customers**.

![](RackMultipart20210502-4-11vawqk_html_662fc29816adbc3.png)

1. Next, in the **Required Data** step, select **Add data**. This is where you map the required customer transaction history data for the model.
2. Add the  **eCommercePurchases : eCommerce**  entity and map the fields from eCommerce to the corresponding fields required by the model.
3. Join the  **eCommercePurchases : eCommerce**  entity with  **eCommerceContacts : eCommerce**.

![](RackMultipart20210502-4-11vawqk_html_d06876bcd8c971c.png)

1. Next, the **Additional data (optional)** step allows you to add any other customer activity data that would help provide a holistic view of your customers&#39; interactions with your business. Adding key customer interactions like web logs, customer service logs, rewards program history, email click history, etc can improve the accuracy of predictions. Select **Add data** to map additional customer activity data.
2. Add the **webReviews : Website** Entity and map the fields from the entity to the corresponding fields required by the Model. Click on Next when done.
3. Select **Activity type = choose existing** and **Activity label = Review**. Join the **webReviews : Website** entity with **eCommerceContacts : eCommerce.**

![](RackMultipart20210502-4-11vawqk_html_c3beb90dbb854562.png)

1. Click on  **Next**  to set the model schedule.

The model needs to train regularly to learn new patterns when there is new data ingested. For this example, select  **Monthly**.

1. After reviewing all the details, select  **Save and Run**.

**Task 4 - Review model results and explanations**

Let the model complete the training and scoring of the data. You can now review the subscription churn model explanations. For more information, see [Review a prediction status and results](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/predict-customer-lifetime-value#review-prediction-status-and-results).

**Task 5 - Create a segment of high value customers**

Running the production model creates a new entity that you can see in  **Data**  \&gt;  **Entities**.

You can create a new segment based on the entity created by the model.

1. Go to  **Segments**. Select  **New**  and choose  **Create from**  \&gt;  **Intelligence**.

![](RackMultipart20210502-4-11vawqk_html_7747f6d8d47fc353.png)

1. Select the  **OOBeCommerceCLVPrediction**  entity and define the segment:
  - Field: CLVScore
  - Operator: greater than
  - Value: 1500

![](RackMultipart20210502-4-11vawqk_html_33bc538ab9fab1bc.png)

1. **Review** and **Save** the segment.

You now have a segment that is dynamically updated which identifies high value customers (customers that are predicted to generated more than $1500 of revenue in the next 12 months).

For more information, see [Create and manage segments](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/segments).
