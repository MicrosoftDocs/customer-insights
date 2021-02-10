# Product Recommendation prediction (preview) sample guide

We'll walk you through an end to end example of Product Recommendation prediction using the sample data provided below.

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines, which they sell through their Contoso Coffee website. Their goal is to understand which products should they recommend to their recurring customers. Knowing what customers are more **likely to purchase**, can help them save marketing efforts by focusing on specific items.

## Prerequisites

- At least [Contributor permissions](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/permissions) in Customer Insights.
- We recommend that you implement the following steps [in a new environment](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/manage-environments).

## Task 1 - Ingest Data

Review the articles [about data ingestion](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/data-sources) and [importing data sources using Power Query connectors](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/connect-power-query) specifically. The following information assumes you familiarized with ingesting data in general.

### Ingest customer data from eCommerce platform

1. Create a data source named **eCommerce**, choose the import option, and select the **Text/CSV** connector.
2. Enter the URL for eCommerce contacts https://aka.ms/ciadclasscontacts.
3. While editing the data, select **Transform** and then **Use First Row as Headers**.
4. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **CreatedOn**: Date/Time/Zone

![Transform DoB to Date](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/media/ecommerce-dob-date.png)

5. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **eCommerceContacts**

6. Save the data source.

### Ingest online purchase data

1. Add another data set to the same **eCommerce** data source. Choose the **Text/CSV** connector again.
2. Enter the URL for **Online Purchases** data https://aka.ms/ciadclassonline.
3. While editing the data, select **Transform** and then **Use First Row as Headers**.
4. Update the datatype for the columns listed below:
   - **PurchasedOn**: Date/Time
   - **TotalPrice**: Currency
5. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **eCommercePurchases**.
6. Save the data source.



### Ingest customer data from loyalty schema

1. Create a data source named **LoyaltyScheme**, choose the import option, and select the **Text/CSV** connector.
2. Enter the URL for eCommerce contacts https://aka.ms/ciadclasscustomerloyalty.
3. While editing the data, select **Transform** and then **Use First Row as Headers**.
4. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time
5. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **loyCustomers**.
6. Save the data source.



## Task 2 - Data unification

After ingesting the data we now begin the **Map, Match, Merge** process to create a unified customer profile. For more information, see [Data unification](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/data-unification).

### Map

1. After ingesting the data, map contacts from eCommerce and Loyalty data to common data types. Go to **Data** > **Unify** > **Map**.

2. Select the entities that represent the customer profile – **eCommerceContacts** and **loyCustomers**.

   ![unify ecommerce and loyalty datasources.](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/media/unify-ecommerce-loyalty.png)

3. Select **ContactId** as the primary key for **eCommerceContacts** and **LoyaltyID** as the primary key for **loyCustomers**.

   ![Unify LoyaltyId as primary key.](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/media/unify-loyaltyid.png)

### Match

1. Go to the **Match** tab and select **Set Order**.

2. In the **Primary** drop-down list, choose **eCommerceContacts : eCommerce** as the primary source and include all records.

3. In the **Entity 2** drop-down list, choose **loyCustomers : LoyaltyScheme** and include all records.

   ![Unify match eCommerce and Loyalty.](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/media/unify-match-order.png)

4. Select **Create a new rule**

5. Add your first condition using FullName.

   - For eCommerceContacts select **FullName** in the drop-down.
   - For loyCustomers select **FullName** in the drop-down.
   - Select the **Normalize** drop down and choose **Type (Phone, Name, Address, ...)**.
   - Set **Precision Level**: **Basic** and **Value**: **High**.

6. Enter the name **FullName, Email** for the new rule.

   - Add a second condition for email address by selecting **Add Condition**
   - For entity eCommerceContacts, choose **EMail** in drop-down.
   - For entity loyCustomers, choose **EMail** in the drop-down.
   - Leave Normalize blank.
   - Set **Precision Level**: **Basic** and **Value**: **High**.

   ![Unify match rule for name and email.](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/media/unify-match-rule.png)

7. Select **Save** and **Run**.

### Merge

1. Go to the **Merge** tab.

2. On the **ContactId** for **loyCustomers** entity, change the display name to **ContactIdLOYALTY** to differentiate it from the other IDs ingested.

   ![rename contactid from loyalty id.](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/media/unify-merge-contactid.png)

3. Select **Save** and **Run** to start the Merge Process.



## Task 3 - Configure Product Recommendation prediction

With the unified customer profiles in place, we can now run the subscription churn prediction. For detailed steps, see the [Product Recommendation prediction (Preview)]((https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/predict-subscription-churn) (preview)]) article.

1. Go to **Intelligence** > **Prediction** and select to use the **Product Recommendation**.

2. Select **Get started**.

3. Name the model **OOB Prod Rec Model Prediction** and the output entity **OOBProdRecModelPrediction**.

4. Define three conditions for the Product Recommendation model:

   - **Number of products**: **select 5**. This setting defines how many products you want to recommend to your customers.

   - **Suggest products customers have recently purchased?**: **Select "Yes"**. This will indicate that you want to include products in the recommendation that your customers have purchased before.

   - **Look back window:** **Select at least 365 days**. This setting defines how far the model will look back at customer's activity to use as input to their recommendations.![image-20210208095314320](typora-user-images/image-20210208095314320.png)

5. Select **Required data** and select **Add data** for purchase history.

6. Add the **eCommercePurchases : eCommerce** entity and map the fields from eCommerce to the corresponding fields required by the model.

7. Join the **eCommercePurchases : eCommerce** entity with **eCommerceContacts : eCommerce**.

   ![Join eCommerce entities.](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/media/model-purchase-join.png)

8. Select **Next** to set the model schedule.

   The model needs to train regularly to learn new patterns when there is new data ingested. For this example, select **Monthly**.

9. After reviewing all the details, select **Save and Run**.



## Task 4 - Review model results and explanations

Let the model complete the training and scoring of the data. You can now review the Product Recommendation model explanations. For more information, see [Review a prediction status and results](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/predict-subscription-churn#review-a-prediction-status-and-results).

## Task 5 - Create a segment of high purchased products

Running the production model creates a new entity that you can see in **Data** > **Entities**.

You can create a new segment based on the entity created by the model.

1. Go to **Segments**. Select **New** and choose **Create from** > **Intelligence**.

![Creating a segment with the model output.](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/media/segment-intelligence.png)

1. Select the **OOBProdRecModelPrediction** endpoint and define the segment:

   - Field: ProductID
   - Operator: Value
   - Value: Select the top 3 Products

   ![image-20210208112835617](typora-user-images/image-20210208112835617.png)

You now have a segment that is dynamically updated which identifies the customers who are more willing to purchase the top 3 recommended products 

For more information, see [Create and manage segments](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/segments).