---
title: "Create new measures with the measure builder"
description: "Build measures from scratch to analyze key metrics about your business."
ms.date: 03/25/2022

ms.subservice: audience-insights
ms.topic: conceptual
author: v-wendysmith
ms.author: wameng
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-measure-builder
  - customerInsights
---

# Use measure builder to create measures from scratch

This article explains how to create a new [measure](measures.md) from scratch. The measure builder lets you define calculations using math operators, aggregation functions, and filters. You can build a measure with attributes from entities that are related to the unified *Customer* entity.

Creating measures in B-to-C and B-to-B environments works the same way. However, if you're B-to-B environment [uses accounts with hierarchies](relationships.md#set-up-account-hierarchies), you can choose to aggregate the measure across related sub-accounts.

You can also quickly create a measure by choosing from a set of commonly used and predefined measures. For more information, see [Use a template to build a measure](measure-templates.md).

# [Individual consumers (B-to-C)](#tab/b2c)

You can create measures on the level of individual customers (customer attribute, customer measure) or on the level of the business/organization (business measure). Customer attribute and customer measure are two types that enable you to track performance per customer. For example, the total spend by each customer. Business measures enable you to track performance per business. For example, the total revenue by the company.

- Customer attribute: Generates output as a new attribute, which gets saved as a new column in the system-generated entity named *Customer_Measure*. When refreshing a customer attribute, all the other customer attributes in the *Customer_Measure* entity refresh simultaneously. In addition, customer attributes are shown in the customer profile card. Once run or saved, customer attribute you can't change it to a customer measure.

- Customer measure: Generates output as its own entity and you can't change it to a customer attribute once run or saved. Customer measures don't show in the customer profile card.

- Business measure: Generates output as its own entity and show on the home page of your Customer Insights environment.

1. Go to **Measures**.

1. Select **New** and choose **Build your own**.

   :::image type="content" source="media/measure-b2c.png" alt-text="Empty configuration screen for a B-to-C measure. ":::

1. To track business-level performance, toggle **Measure type** to **Business level**. **Customer level** is selected by default. **Customer level** automatically adds the *CustomerId* attribute to Dimensions while **Business level** will remove it.

1. In the configuration area, choose the aggregation function from the **Select function** dropdown menu. Aggregation functions include:
   - **Sum**
   - **Average**
   - **Count**
   - **Count Unique**
   - **Max**
   - **Min**
   - **First**: takes the first value of the data record
   - **Last**: takes the last value that was added to the data record
   - **ArgMax**: finds the data record giving the maximum value from a target function
   - **ArgMin**: finds the data record giving the minimum value from a target function

1. Select **Add attribute** to select the data you need to create this measure.

   1. Select the **Attributes** tab.
   1. Data entity: Choose the entity that includes the attribute you want to measure.
   1. Data attribute: Choose the attribute you want to use in the aggregation function to calculate the measure. You can only select one attribute at a time.
   1. You can also select a data attribute from an existing measure by selecting the **Measures** tab, or you can search for an entity or measure name.
   1. Select **Add** to add the selected attribute to the measure.

1. To build more complex measures, you can add more attributes or use math operators on your measure function.

1. To add filters, select the **Filter** in the configuration area. Applying filters will only use the records that match the filters to calculate the measure.
  
   1. In the **Add attribute** section of the **Filters** pane, select the attribute you want to use to create filters.
   1. Set the filter operators to define the filter for every selected attribute.
   1. Select **Apply** to add the filters to the measure.

1. Select **Dimension** to choose more fields that are added as columns to the measure output entity.

   1. Select **Edit dimensions** to add data attributes you want to group the measure values by. For example, city or gender.
   > [!TIP]
   > If you selected **Customer level** as the **Measure type** the *CustomerId* attribute is already added. If you remove the attribute, **Measure type** switches to **Business level**.
   1. Select **Done** to add the dimensions to the measure.

1. If there are values in your data that you need to replace with an integer, select **Rules**. Configure the rule and make sure that you choose only whole numbers as replacements. For example, replace *null* with *0*.

1. If there are multiple paths between the data entity you mapped and the *Customer* entity, you have to choose one of the identified [entity relationship paths](relationships.md). Measure results can vary depending on the selected path.

   1. Select **Relationship path** and choose the entity path that should be used to identify your measure. If there's only a single path to the *Customer* entity, this control won't show.
   1. Select **Done** to apply your selection.

1. To add more calculations for the measure, select **New calculation**. You can only use entities on the same entity path for new calculations. More calculations will show as new columns in the measure output entity.

1. Select **...** on the calculation to **Duplicate**, **Rename**, or **Remove** a calculation from a measure.

1. In the **Preview** area, you'll see the data schema of the measure output entity, including filters and dimensions. The preview reacts dynamically to changes in the configuration.

1. Select **Edit details** next to Untitled measure. Provide a name for the measure. Optionally, add [tags](work-with-tags-columns.md#manage-tags) to the measure.

   :::image type="content" source="media/measures_edit_details.png" alt-text="Edit details dialog box.":::

1. Select **Run** to calculate results for the configured measure. Select **Save and close** if you want to keep the current configuration and run the measure later.

1. Go to **Measures** to see the newly created measure in the list.

# [Business accounts (B-to-B)](#tab/b2b)

You can create measures on the level of individual accounts (customer measure) or  on the level of all accounts (business measure).

- Customer measure: Generates output as its own entity. Customer measures don't show in the customer profile card.

- Business measure: Generates output as its own entity and show on the home page of your Customer Insights environment.

1. Go to **Measures**.

1. Select **New**.

   :::image type="content" source="media/measure-b2b.png" alt-text="Empty configuration screen for a B-to-B measure. ":::

1. In the configuration area, choose the aggregation function from the **Select function** dropdown menu. Aggregation functions include:
   - **Sum**
   - **Average**
   - **Count**
   - **Count Unique**
   - **Max**
   - **Min**
   - **First**: takes the first value of the data record
   - **Last**: takes the last value that was added to the data record

1. Select **Add attribute** to select the data you need to create this measure.

   1. Select the **Attributes** tab.
   1. Data entity: Choose the entity that includes the attribute you want to measure.
   1. Data attribute: Choose the attribute you want to use in the aggregation function to calculate the measure. You can only select one attribute at a time.
   1. You can also select a data attribute from an existing measure by selecting the **Measures** tab, or you can search for an entity or measure name.
   1. Select **Add** to add the selected attribute to the measure.

1. To build more complex measures, you can add more attributes or use math operators on your measure function.

1. To add filters, select the **Filter** in the configuration area. Applying filters will only use the records that match the filters to calculate the measure.
  
   1. In the **Add attribute** section of the **Filters** pane, select the attribute you want to use to create filters.
   1. Set the filter operators to define the filter for every selected attribute.
   1. Select **Apply** to add the filters to the measure.

1. Select **Dimension** to choose more fields that are added as columns to the measure output entity.

   1. Select **Edit dimensions** to add data attributes you want to group the measure values by. For example, city or gender. 
      > [!TIP]
      > If you selected **Customer level** as the **Measure type** the *CustomerId* attribute is already added. If you remove the attribute, **Measure type** switches to **Business level**.
   1. Select **Done** to add the dimensions to the measure.

1. If there are values in your data that you need to replace with an integer, select **Rules**. Configure the rule and make sure that you choose only whole numbers as replacements. For example, replace *null* with *0*.

1. You can use the **Roll up sub-accounts** toggle if you [use accounts with hierarchies](relationships.md#set-up-account-hierarchies).
   - If it's set to **Off**, the measure is calculated for every account. Every account gets own of result.
   - If it's set to **On**, select **Edit** to choose the account hierarchy according to the ingested hierarchies. The measure will yield only one result because it's aggregated with sub accounts.

1. If there are multiple paths between the data entity you mapped and the *Customer* entity, you have to choose one of the identified [entity relationship paths](relationships.md). Measure results can vary depending on the selected path.

   1. Select **Relationship path** and choose the entity path that should be used to identify your measure. If there's only a single path to the *Customer* entity, this control won't show.
   1. Select **Done** to apply your selection.

1. Select **...** on the calculation to **Duplicate**, **Rename**, or **Remove** a calculation from a measure.

1. In the **Preview** area, you'll see the data schema of the measure output entity, including filters and dimensions. The preview reacts dynamically to changes in the configuration.

1. Select **Edit details** next to Untitled measure. Provide a name for the measure. Optionally, add [tags](work-with-tags-columns.md#manage-tags) to the measure.

   :::image type="content" source="media/measures_edit_details.png" alt-text="Edit details dialog box.":::

1. Select **Run** to calculate results for the configured measure. Select **Save and close** if you want to keep the current configuration and run the measure later.

1. Go to **Measures** to see the newly created measure in the list.
