---
title: "Create measures with measure builder"
description: "Build measures from scratch to analyze key metrics about your business."
ms.date: 11/28/2022

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

# Create measures with measure builder

Measure builder lets you define calculations using math operators, aggregation functions, and filters. Define measures using attributes from entities that are related to the unified *Customer* entity.

Creating measures in B-to-C and B-to-B environments works the same way. However, if your B-to-B environment [uses accounts with hierarchies](relationships.md#set-up-account-hierarchies), choose whether to aggregate the measure across related sub-accounts.

# [Individual consumers (B-to-C)](#tab/b2c)

Create measures on the level of individual customers (customer attribute, customer measure) or on the level of the business/organization (business measure). Customer attribute and customer measure enable you to track performance per customer. For example, the total spend by each customer. Business measures track performance per business. For example, the total revenue by the company.

- Customer attribute: Generates output as a new attribute, which gets saved as a new column in the system-generated entity named *Customer_Measure*. When refreshing a customer attribute, all the other customer attributes in the *Customer_Measure* entity refresh simultaneously. In addition, customer attributes are shown in the customer profile card. Once run or saved, you can't change a customer attribute to a customer measure.

- Customer measure: Generates output as its own entity and you can't change it to a customer attribute once run or saved. Customer measures don't show in the customer profile card.

- Business measure: Generates output as its own entity and shows on the home page of your Customer Insights environment.

1. Go to **Measures**.

1. Select **New** > **Build your own**.

   :::image type="content" source="media/measure-b2c.png" alt-text="Empty configuration screen for a B-to-C measure." lightbox="media/measure-b2c.png":::

1. Select **Edit details** next to Untitled measure. Provide a name for the measure. Optionally, add [tags](work-with-tags-columns.md#manage-tags) to the measure.

   :::image type="content" source="media/measures_edit_details.png" alt-text="Edit details dialog box.":::

1. Select **Done**.

1. To track business-level performance, toggle **Measure type** to **Business level**. **Customer level** is selected by default. **Customer level** automatically adds the *CustomerId* attribute to Dimensions while **Business level** automatically removes it.

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

1. Select **Add attribute** to select the data to create this measure.

   1. Select the **Attributes** tab.
   1. Data entity: Choose the entity that includes the attribute you want to measure.
   1. Data attribute: Choose the attribute you want to use in the aggregation function to calculate the measure. You can only select one attribute at a time.
   1. Optionally, choose a data attribute from an existing measure by selecting the **Measures** tab, or search for an entity or measure name.
   1. Select **Add**.

1. To build more complex measures, add more attributes or use math operators on your measure function.

1. To add filters, select the **Filter** in the configuration area. Applying filters will only use the records that match the filters to calculate the measure.
  
   1. In the **Add attribute** section of the **Filters** pane, select the attribute you want to use to create filters.
   1. Set the filter operators to define the filter for every selected attribute.
   1. Select **Apply**.

1. Select **Dimension** to choose more fields to add as columns to the measure output entity.

   1. Select **Edit dimensions** to add data attributes you want to group the measure values by. For example, city or gender.
      > [!TIP]
      > If you selected **Customer level** as the **Measure type** the *CustomerId* attribute is already added. If you remove the attribute, **Measure type** toggles to **Business level**.
   1. Select **Done**.

1. If there are values in your data that must be replaced with an integer, select **Rules**. Configure the rule and make sure that you choose only whole numbers as replacements. For example, replace *null* with *0*.

1. If there are multiple paths between the data entity you mapped and the *Customer* entity, choose one of the identified [entity relationship paths](relationships.md). Measure results can vary depending on the selected path.

   1. Select **Relationship path** and choose the entity path that should be used to identify your measure. If there's only a single path to the *Customer* entity, this control won't show.
   1. Select **Done**.

1. To add more calculations for the measure, select **New calculation**. Only use entities on the same entity path for new calculations. More calculations will show as new columns in the measure output entity. Optionally, select **Edit name** to create a name for the calculation.

1. Select the vertical ellipsis (&vellip;) on the calculation to **Duplicate** or **Remove** a calculation from a measure.

1. In the **Preview** area, you'll see the data schema of the measure output entity, including filters and dimensions. The preview reacts dynamically to changes in the configuration.

1. Select **Run** to calculate results for the configured measure. Select **Save and close** if you want to keep the current configuration and run the measure later. The **Measures** page displays.

# [Business accounts (B-to-B)](#tab/b2b)

Create measures on the level of individual accounts (customer measure) or on the level of all accounts (business measure).

- Customer measure: Generates output as its own entity. Customer measures don't show in the customer profile card.

- Business measure: Generates output as its own entity and shows on the home page of your Customer Insights environment.

1. Go to **Measures**.

1. Select **New**.

   :::image type="content" source="media/measure-b2b.png" alt-text="Empty configuration screen for a B-to-B measure. ":::

1. Select **Edit details** next to Untitled measure. Provide a name for the measure. Optionally, add [tags](work-with-tags-columns.md#manage-tags) to the measure. 
   :::image type="content" source="media/measures_edit_details.png" alt-text="Edit details dialog box.":::

1. Select **Done**.

1. In the configuration area, choose the aggregation function from the **Select function** dropdown menu. Aggregation functions include:
   - **Sum**
   - **Average**
   - **Count**
   - **Count Unique**
   - **Max**
   - **Min**
   - **First**: takes the first value of the data record
   - **Last**: takes the last value that was added to the data record

1. Select **Add attribute** to select the data to create this measure.

   1. Select the **Attributes** tab.
   1. Data entity: Choose the entity that includes the attribute you want to measure.
   1. Data attribute: Choose the attribute you want to use in the aggregation function to calculate the measure. You can only select one attribute at a time.
   1. Optionally, choose a data attribute from an existing measure by selecting the **Measures** tab, or search for an entity or measure name.
   1. Select **Add** to add the selected attribute to the measure.

1. To build more complex measures, add more attributes or use math operators on your measure function.

1. To add filters, select the **Filter** in the configuration area. Applying filters will only use the records that match the filters to calculate the measure.
  
   1. In the **Add attribute** section of the **Filters** pane, select the attribute you want to use to create filters.
   1. Set the filter operators to define the filter for every selected attribute.
   1. Select **Apply** to add the filters to the measure.

1. Select **Dimension** to choose more fields to add as columns to the measure output entity.

   1. Select **Edit dimensions** to add data attributes you want to group the measure values by. For example, city or gender.
      > [!TIP]
      > The *CustomerId* attribute is already added indicating this is a customer level measure type. If you remove the attribute, the measure type changes to business level.
   1. Select **Done** to add the dimensions to the measure.

1. If there are values in your data that must be replaced with an integer, select **Rules**. Configure the rule and make sure that you choose only whole numbers as replacements. For example, replace *null* with *0*.

1. If you [use accounts with hierarchies](relationships.md#set-up-account-hierarchies), review **Roll up sub-accounts**.
   - If it's set to **Off**, the measure is calculated for every account. Every account gets its own result.
   - If it's set to **On**, select **Edit** to choose the account hierarchy according to the ingested hierarchies. The measure will yield only one result because it's aggregated with sub-accounts.

1. If there are multiple paths between the data entity you mapped and the *Customer* entity, choose one of the identified [entity relationship paths](relationships.md). Measure results can vary depending on the selected path.

   1. Select **Relationship path** and choose the entity path that should be used to identify your measure. If there's only a single path to the *Customer* entity, this control won't show.
   1. Select **Done** to apply your selection.

1. Select the vertical ellipsis (&vellip;) on the calculation to **Duplicate** or **Remove** a calculation from a measure.

1. In the **Preview** area, you'll see the data schema of the measure output entity, including filters and dimensions. The preview reacts dynamically to changes in the configuration.

1. Select **Run** to calculate results for the configured measure. Select **Save and close** if you want to keep the current configuration and run the measure later. The **Measures** page displays.

---

## Next steps

- [Schedule a measure](measures.md#schedule-measures).
- Use existing measures to create [a customer segment](segments.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
