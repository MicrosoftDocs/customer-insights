---
title: "Consent data in out-of-box predictions"
description: "Learn how to create prediction models that use consent data."
ms.date: 10/30/2021
ms.service: customer-insights
ms.topic: how-to
author: smithy7
ms.author: dimutako
ms.reviewer: mhart
manager: shellyha
---

# Use consent data in prediction models

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Audience insights provides out-of-box prediction models to predict customer churn or customer lifetime value. Use consent data from the consent management platform to increase the accuracy of the predictions. You can also understand the impact of customer consent on customer churn and the customer lifetime value. This article outlines how to use consent data in out-of-box models. The steps below focus on the transaction churn model. However, you can apply the same steps to the subscription churn and customer lifetime value models. 

## Required entities and fields

The following list includes the entities that are required and the fields these entities must contain.

1. Subscription consent data entity
    - Primary key or ID: A primary key for each unique consent value. This field must have unique values in each row. For example:  email or customer ID. 
    - Customer ID: A customer identifier that links the consent entity to the customer entity and their transaction data. This can be an ID, email, name, etc. This ID should be the same ID across all 3 entities listed here. 
    - Consent start date – The date consent was updated. This can include the time, but it is not required.
    - Consent Status – Consent value indicating which customers consented. This can be in any data type, numeric, Boolean, string, etc. 
    
2.	Customer Transaction Data entity with the following fields(similar to requirements for setting up the transaction churn model show here: Overview about supported prediction scenarios - Dynamics 365 Customer Insights | Microsoft Docs)
a.	Transaction ID – primary key corresponding to each transaction
b.	Customer ID – The key corresponding to each customer to indicate their transactions. This can be an Id, a name, email, or any customer identifier. This ID should be similar across all 3 entities listed here. 
c.	Transaction date – Date each transaction was held on
d.	Value of transaction – The amount associated with the transaction
e.	Label assigned to returns (Optional) – Boolean indicating if the transaction is a return.
f.	Unique product ID (Optional)– ID representing the product or service exchanged in the transaction. 

3.	Customer entity: This is the entity containing contact information, description & other details on the customers. It must have at least the following field:
a.	Customer ID: A primary key representing each unique customer. This ID should be similar across all 3 entities listed here.

## Set up instructions

Overview: This process details how to use consent data as activity data input to the transaction churn model. It involves setting up an activity with the consent data, then setting up the model as usual and adding the consent activity as an optional customer activity data in the model configuration.

### Step 1: Setup the consent activity
1.	Set up a consent activity: Follow the instructions below to set up an activity with your consent entity: Customer activities - Dynamics 365 Customer Insights | Microsoft Docs.
a.	On the relationship step: 
i.	Select the Customer ID of the consent entity as the Foreign Key
ii.	Select the Customer entity as the entity to map to
iii.	Select the Customer ID in the customer entity as the Primary key.
Consent Activity Relationship: in our case, the CustomerID is the ContactId, and our customer entity is the Contacts: eCommerce. 
 
b.	On Activity Unification Step:
i.	Select the Consent Status column in the consent entity under the Event activity field. 
ii.	Select Consent start date in the Timestamp field
c.	On Activity Type Step:
i.	Select Create new in the dropdown for Activity Type
ii.	Type “Consent” in the activity type name
Unified consent activity: in our case the consent status column is called Topics_Settings_State the Consent start date is ModifiedDate, whereas the Subscription name is the Topic Name.
d.	Review and run the act activity. Ensure the activity has run successfully before continuing. If you run into errors, please check out the FAQ page?

### Step 2: Configure & Run the Model 
1.	Follow the instructions to set up a transaction model up to “Customer activities” step. Instructions here: Transaction churn prediction - Dynamics 365 Customer Insights | Microsoft Docs
2.	Add Consent data on the Additional Data Step:
a.	Click Add Data for Customer activities
b.	Select the Consent activity created in the previous step and the corresponding Consent entity used.
c.	Select ActualActivityId as the Primary Key
d.	Select ActivityTime as the Timestamp
e.	Select ActivityName as the Activity Event
f.	Click Save and then Next. 
Optional data mapping 
3.	Data update schedule: Set how frequently the data will be updated and the model will be re-run. 
4.	Review & run: Confirm everything is as expected and click Run. You can also save this set up as a draft and run it later.  

## View & Interpret Results
Once the model has finished running, click on the model to see the results with the following information:
Training model performance: This score indicates the performance of the prediction based on how many customers it predicted accurately, and how the model compared to Churn. Adding consent data, as well as additional optional data helps increase the likelihood of accurate predictions. 
Likelihood to churn (number of customers): Groups of customers based on their predicted risk of churn. 
Most influential factors: This shows the factors affecting the results. Here you can see the impact the consent data had by looking at the “Activity” factors. Another way to gauge the impact of consent data is to set up a model without consent data and compare the results to that of the model. You can click on Learn more to see the impact in both cases.
You can read more information on results interpretation here: Transactional churn prediction - Dynamics 365 Customer Insights | Microsoft Docs
In our case, the model is called TrChurnConsent. 
 

