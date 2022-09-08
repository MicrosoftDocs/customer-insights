---
title: "Product recommendation prediction"
description: "Predict the products a customer is likely to purchase or interact with."
ms.date: 09/07/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: wmelewong 
ms.author: wameng
manager: shellyha
---

# Product recommendation prediction

The product recommendation model creates sets of predictive product recommendations. Recommendations are based on previous purchase behavior and customers with similar purchase patterns.

Product recommendations may be subject to local laws and regulations and customer expectations, which the model is not built to specifically take into account. Therefore, **you must review the recommendations prior to delivering them to your customers** to ensure you are complying with any applicable laws or regulations, and customer expectations for what you may recommend.

The output of this model provides recommendations based on the product ID. Your delivery mechanism must map the predicted product IDs to appropriate content for your customers to account for localization, image content, and other business-specific content or behavior.

## Sample Guide

If you're interested in trying this feature but don't have data to complete the requirements below, [create a sample implementation](sample-guide-predict-product-recommendation.md).

## Prerequisites

- At least [Contributor permissions](permissions.md).

- Business knowledge on the different types of products for your business and how your customers interact with them. We support recommending products that have been previously purchased by your customers or recommendations for new products.

- Your environment is configured for the **individual consumers** primary target audience.

- Data about transactions, purchases, and their history:
  - Transaction identifiers to distinguish purchases or transactions.
  - Customer identifiers to map transactions to your customers.
  - Transaction event dates that specify the date a transaction occurred.
  - Product ID information for the transaction.
  - A product catalog data entity to use as a product filter (optional).
  - Whether the transaction is a return (optional).
  - The following semantic data schema:
    - **Transaction ID:** Unique identifier of a purchase or transaction.
    - **Transaction date:** Date of the purchase or transaction.
    - **Value of the transaction:** Numerical value of the purchase or transaction.
    - **Unique product ID:** ID of the product or service purchased if your data is at a line item level.
    - **Purchase or return** (optional): A boolean value where *true* identifies that a transaction was a return. If the Purchase or Return data is not provided and the model and the **Value of the transaction** is negative, we infer a return.
- Suggested data characteristics:
  - Sufficient historical data: At least one year of transactional data, preferably two to three years to include some seasonality.
  - Multiple purchases per customer: Three or more transactions per Customer ID.
  - Number of customers: At least 100 customers, preferably more than 10,000 customers. The model will fail with fewer than 100 customers.

> [!NOTE]
> - The model requires the transaction history of your customers. The definition of a transaction is quite flexible. Any data that describes a user-product interaction can work as an input. For example, purchasing a product, taking a class, or attending an event.
> - Only one transaction history entity can be configured. If there are multiple purchase entities, combine them in Power Query before data ingestion.
> - If order and order details are different entities, join them before using in the model. The model doesn't work with only an order ID or receipt ID in an entity.

## Create a product recommendation prediction

1. Go to **Intelligence** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Product recommendations model** tile.

1. In the **Product recommendations (preview)** pane, select **Get started**.

1. **Name this model** and the **Output entity name** to distinguish them from other models or entities.

1. Select **Next**.

### Define product recommendation preferences

1. For the **Model preferences** step, set the **Number of products** you want to recommend to a customer. This value depends on how your delivery method fills data. If you can recommend three products, set this value accordingly.

   >[!TIP]
   > You can select **Save draft** at any time to save the prediction as a draft. The draft prediction displays in the **My predictions** tab.

1. Choose if you want to include products customers have recently purchased in the **Repeat purchases expected** field.

1. Set the **Look back window** which specifies the time frame the model considers before recommending the product to the user again. For example, indicate a customer purchases a laptop every two years. The model will look at the purchase history for the last two years, and if it finds an item, the item will be filtered from the recommendations.

1. Select **Next**

### Add required data

1. For the **Required data** step, select **Add data**  for **Customer transaction history**.

1. Select **SalesOrderLine** which is the semantic activity type that contains the required transaction or purchase history information. If the activity has not been set up, select **here**.

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or entity you'd like the calculation to focus on. If semantic mapping did not occur, select **Edit** and map your data.

   :::image type="content" source="media/product-recommendation-select-semantic-activity.PNG" alt-text="Side pane showing choosing specific activities under the semantic type.":::

1. Select **Next** and review the attributes required for this model.

1. Select **Save**.

1. Select **Next**.

### Configure product filters

Sometimes, only certain products are beneficial or appropriate for the type of prediction you build. Use product filters to identify a subset of products with specific characteristics to recommend to your customers. The model will use all the products available to learn patterns but only use the products matching the product filter in its output.

1. In the **Add product information** step, add your product catalog entity that contains information for each product. Map the information required and select **Save**.

1. Select **Next**.

1. In the **Product filters** step, choose between the following options.

   - **No filters**: Use all products in the product recommendation prediction.

   - **Define specific product filters**: Use specific products in the product recommendation prediction. In the **Product catalog attributes** pane, select the attributes from your Product Catalog entity that you want include in the filter.

   :::image type="content" source="media/product-filters-sidepane.png" alt-text="Side pane showing attributed in the product catalog entity to select for product filters.":::

1. Choose if you want the product filter to use **and** or **or** to logically combine your selection of attributes from the product catalog.

   :::image type="content" source="media/product-filters-sample.png" alt-text="Sample configuration of product filters combined with logical AND connectors.":::

1. Select **Next**.

### Set update schedule and review configuration

1. For the **Data update schedule** step, choose a frequency to retrain your model. This setting is important to update the accuracy of predictions as new data is ingested into Customer Insights. Most businesses can retrain once per month and get a good accuracy for their prediction.

1. Select **Next**.

### Review and run the model configuration

The **Review your model details** step shows a summary of the configuration and provides a chance to make changes before you create the prediction.

1. Select **Edit** on any of the steps to review and make any changes.

1. If you are satisfied with your selections, select **Save and run** to start running the model. Select **Done**. The **My predictions** tab displays while the prediction is being created. The process may take several hours to complete depending on the amount of data used in the prediction.

[!INCLUDE [progress-details](includes/progress-details-pane.md)]

## View prediction results

1. Go to **Intelligence** > **Predictions**.

1. In the **My predictions** tab, select the prediction you want to view.

There are five primary sections of data within the results page.

- **Training model performance:** Grades A, B, or C indicate the performance of the prediction and can help you make the decision to use the results stored in the output entity.
  
  :::image type="content" source="media/product-recommendation-modelperformance.PNG" alt-text="Image of the model performance result with the grade A.":::

  Grades are determined based on the following rules:
  - **A** when the "Success @ K" metric is at least 10% more the baseline.
  - **B** when the "Success @ K" metric is 0% to 10% more than the baseline.
  - **C** when the "Success @ K" metric is less than the baseline.
  - **Baseline**: The model takes the top most recommended products by purchase count across all customers, and uses learned rules identified by the model to create a set of recommendations for the customers. The predictions are then compared to the top products, as calculated by the number of customers that had purchased the product. If a customer has at least one product in their recommended products that was also seen in the top purchased products, they're considered a part of the baseline. If there were 10 of these customers that had a recommended product purchased out of 100 total customers, the baseline would be 10%.
  - **Success @ K**: Using a validation set of time period of transactions, recommendations are created for all customers and compared against the validation set of transactions. For example, in a 12-month period, month 12 might be set aside as a validation set of data. If the model predicts at least one thing you would purchase in month 12 based on what it learned from the previous 11 months, the customer would increase the "Success @ K" metric.

- **Most suggested products (with tally):** The top five products that were predicted for your customers.
  
  :::image type="content" source="media/product-recommendation-topproducts.PNG" alt-text="Graph showing the top 5 most recommended products.":::

- **Key recommendation factors:** The model uses the customers' transaction history to make product recommendations. It learns patterns based on past purchases and finds similarities between customers and products. These similarities are then utilized to generate product recommendations.
  The following factors could influence a product recommendation generated by the model.
  - **Past transactions**: A product was recommended based on past purchase patterns in the past were utilized to generate product recommendations. For example, the model can recommend a *Surface Arc Mouse* if someone recently purchased a *Surface Book 3* and a *Surface Pen*. The model learned that historically, many customers had purchased a *Surface Arc Mouse* after purchasing a *Surface Book 3* and a *Surface Pen*.
  - **Customer similarity**: A recommended product was historically purchased by other customers who show similar purchase patterns. For example, John was recommended *Surface Headphones 2* because Jennifer and Brad recently purchased *Surface Headphones 2*. The model believes John is similar to Jennifer and Brad because they have historically had similar purchase patterns.
  - **Product similarity**: A recommended product is similar to other products that the customer had previously purchased. The model considers two products to be similar if they were bought together or by similar customers. For example, someone gets a recommendation for a *USB Storage Drive* because they previously purchased a *USB-C to USB Adapter* and the model believes that *USB Storage Drive* is similar to *USB-C to USB Adapter* based on historical purchase patterns.

  Every product recommendation is influenced by one or more of these factors. The percentage of recommendations where each influencing factor played a role is visualized in a chart. In the following example, 100% of the recommendations were influenced by past transactions, 60% by customer similarity and 22% by product similarity. Hover over the bars in the chart to see the exact percentage where the influencing factors contributed.
  
  :::image type="content" source="media/product-recommendation-keyrecommendationfactors.png" alt-text="Key recommendation factors learned by the model to generate product recommendations.":::

- **Data statistics**: Gives an overview of the number of transactions, customers, and products the model considered. It's based on the input data that was used to learn patterns and generate product recommendations.

  :::image type="content" source="media/product-recommendation-datastatistics.png" alt-text="Data statistics around input data used by the model to learn patterns.":::
  
  This section shows stats around the data points that were used by the model to learn patterns and generate product recommendations. Filtering, as configured in the model configuration, will apply on the output generated by the model. However, the model uses all available data to learn patterns. Therefore, if you use product filtering in the model configuration, this section will show the total number of products that the model analyzed to learn patterns, which might differ from the number of products that match the defined filtering criteria.

- **High-confidence product recommendations:** A sample of recommendations provided to your customers that the model believes are likely to be purchased by the customer. If a product catalog is added, the product IDs get replaced with product names. Product names provide a more actionable and intuitive information about the predictions.

  :::image type="content" source="media/product-recommendation-highconfidence.PNG" alt-text="List showing high confidence suggestions for a select set of individual customers.":::
  
## Manage predictions

It's possible to optimize, troubleshoot, refresh, or delete predictions. Review an input data usability report to find out how to make a prediction faster and more reliable. For more information, see [Manage predictions](predictions-overview.md#manage-existing-predictions).

[!INCLUDE [footer-include](includes/footer-banner.md)]
