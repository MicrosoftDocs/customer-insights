---
title: "Create measures with measure builder"
description: "Build measures from scratch to analyze key metrics about your business."
ms.date: 04/16/2025
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: v-wendysmith
ms.custom:
  - bap-template
  - sfi-image-nochange
---

# Create measures with measure builder

Measure builder lets you define calculations using math operators, aggregation functions, and filters. Define measures using attributes from tables that are related to the unified *Customer* table.

## Measure types

There are three types of measures that can be created in four different ways:

- Customer attribute: Generates output as a new attribute, which gets saved as a new column in the system-generated table named *Customer_Measure*. When refreshing a customer attribute, all the other customer attributes in the *Customer_Measure* table refresh simultaneously. In addition, customer attributes are shown in the customer profile card. Once run or saved, you can't change a customer attribute to a customer measure. Customer attribute measures have a direct relationship to the unified customer profile.

- Customer measure: Generates output as its own table named after the name of the measure you define. You can't change it to a customer attribute once run or saved. Customer measures don't show in the customer profile card. Customer measures have a direct relationship to the unified customer profile.

  You can also [create a customer measure - table that can be used in Customer Insights - Journeys and other Dataverse applications](dataverse-measures.md). 

- Business measure: Generates output as its own table and shows on the home page of your Dynamics 365 Customer Insights - Data environment. Business measures don't have a direct relationship to individual customer profiles. Business measures look across all customer profiles or are grouped by another attribute. For example, a calculation for all customers in a specific state.

The following table provides key points about the different measure types. The dimension, *CustomerId* is the unique profile identifier from the *Customer* table.

|Key points  |Customer attribute  |Customer measure  |Customer measure table - For use in Journeys and other Dynamics 365 apps |Business measure
|---------|---------|---------|---------|---------|
|Definition |A single value calculated per unique profile. |A single value or multiple values calculated per unique profile and split by one or more dimensions. |A single value or multiple values calculated per unique profile. |A value calculated without a direct link to a unique profile, optionally split by one or more dimensions. |
|Dimensions | CustomerId only |CustomerId and more |CustomerId only |0 or more except CustomerId |
|# of calculations/attributes in the measure |A single calculation/attribute. |A single or multiple calculations/attributes with CustomerId + at least 1 other dimension. |A single or multiple calculations/attributes with CustomerId dimension. |A single calculation/attribute with no dimension *or* a single or multiple calculations/attributes with at least 1 dimension that isn't the CustomerId. |
|Table |All customer attributes are stored in a table called *Customer_Measure* where the first column is CustomerId and 1 column for each added Customer attribute. |Stored in its own dedicated table |Stored in its own dedicated table |Stored in its own dedicated table |
|Displays on [**Customer** card](customer-profiles.md) |Yes |No |No |No |
|Available as [elastic table in Dataverse](tables.md#view-customer-insights---data-tables-in-dataverse) |Yes (a different format than the [*Customer_Measure*](tables.md#customermeasure) table and not readily usable in other Dynamics 365 apps) |No |Yes |No |
|Refresh |Refresh of a customer attribute results in refresh of all the customer attributes in the instance |Can be refreshed on its own |Can be refreshed on its own |Can be refreshed on its own |

## Create a build-your-own measure

1. Go to **Insights** > **Measures**.

1. Select **New** > **Build your own**.

   :::image type="content" source="media/measure-b2c.png" alt-text="Empty configuration screen for a measure." lightbox="media/measure-b2c.png":::

1. Select **Edit details** next to Untitled measure. Provide a name for the measure. Optionally, add [tags](work-with-tags-columns.md#manage-tags) to the measure.

   :::image type="content" source="media/measures_edit_details.png" alt-text="Edit details dialog box.":::

1. Select **Done**.

1. Select the [**Measure type**](#measure-types).

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
   1. Data table: Choose the table that includes the attribute you want to measure.
   1. Data attribute: Choose the attribute you want to use in the aggregation function to calculate the measure. You can only select one attribute at a time.
   1. Optionally, choose a data attribute from an existing measure by selecting the **Measures** tab, or search for a table or measure name.
   1. Select **Add**.

1. To build more complex measures, add more attributes or use math operators on your measure function.

1. To add filters, select the **Filter** in the configuration area. Applying filters will only use the records that match the filters to calculate the measure.
  
   1. In the **Add attribute** section of the **Filters** pane, select the attribute you want to use to create filters.
   1. Set the filter operators to define the filter for every selected attribute.
   1. Select **Apply**.

1. Select **Dimension** to choose more fields to add as columns to the measure output table.

   1. Select **Edit dimensions** to add data attributes you want to group the measure values by. For example, city or gender.
      > [!TIP]
      > If you selected **Customer** as the **Measure type**, the *CustomerId* attribute is already added. If you remove the attribute, **Measure type** toggles to **Business**.
   1. Select **Done**.

1. If there are values in your data that must be replaced with an integer, select **Rules**. Configure the rule and make sure that you choose only whole numbers as replacements. For example, replace *null* with *0*.

1. If there are multiple paths between the data table you mapped and the *Customer* table, choose one of the identified [table relationship paths](relationships.md). Measure results can vary depending on the selected path.

   1. Select **Relationship path** and choose the table path that should be used to identify your measure. If there's only a single path to the *Customer* table, this control doesn't show.
   1. Select **Done**.

1. To add more calculations for the measure, select **New calculation**. Only use tables on the same path for new calculations. More calculations show as new columns in the measure output table. Optionally, select **Edit name** to create a name for the calculation.

1. Select the vertical ellipsis (&vellip;) on the calculation to **Duplicate** or **Remove** a calculation from a measure.

1. In the **Preview** area, you can see the data schema of the measure output table, including filters and dimensions. The preview reacts dynamically to changes in the configuration.

1. Select **Run** to calculate results for the configured measure. Select **Save and close** if you want to keep the current configuration and run the measure later. The **Measures** page displays.

## Next steps

- [Schedule a measure](measures-schedule.md).
- Use existing measures to create [a customer segment](segments.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
