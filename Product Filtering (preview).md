# Product Filtering (preview)

While making product recommendations, you may identify cases where only certain products are beneficial or appropriate for the type of predictions you are making. You may want to identify a subset of products with specific characteristics that you want to recommend to your customers, increasing the personalization in the recommendations to your customers.  

 

## Prerequisites

- At least [Contributor permissions](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/permissions) in Customer Insights.
- Business knowledge to understand different types of products for your business and how your customers interact with them. We support recommending products that have been previously purchased by your customers or recommendations for new products.

## Configure a Product Recommendation model

1. To configure a Product Recommendation model review the Product Recommendation documentation [https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/predict-product-recommendation]



## Configure the Product Filter

1. On the Product Filters section, you can select between:

   * **No filters**: This option will not affect the products used in the Product Recommendation model.

   * **Define specific product filters**: Select this option to create a product filter and only use specific products in your Product Recommendation prediction.

     * Click **Next**.

     [Product_Filter.png]

2. From the right panel, select the attributes from your **Product Catalog Entity** that you want include in the Product Filter. You can add as many as you like.

   [Product_Filter_sidepanel.png]

3. Select whether you want your product filter to use **"and"** or **"or"** to combine your selection of attributes from product catalog.
   [Product_Filter_And_Or.png]

4. Click **Next** and complete setting up the Product Recommendation model.



The Product Recommendation Model with a Product Filter configured will use all the products available to the model to learn patterns, but will output recommendations using only the products selected in the Product Filter.