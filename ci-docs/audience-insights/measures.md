---
title: "Create and manage measures"
description: "Define measures to analyze and reflect the performance of your business."
ms.date: 04/08/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: wameng
ms.reviewer: mhart
manager: shellyha
---

# Define and manage measures

Measures help you to better understand customer behaviors and business performance. They look at relevant values from [unified profiles](data-unification.md). For example, a business wants to see the *total spend per customer* to understand individual customer’s purchase history. Or measure *total sales of the company* to understand the aggregate-level revenue in the whole business.  

Measures are created using the measure builder, a data query platform with various operators and simple mapping options. It lets you filter the data, group results, detect [entity relationship paths](relationships.md), and preview the output.

Use the measure builder to plan business activities by querying customer data and extract insights. For example, creating a measure of *total spend per customer* and *total return per customer* helps identify a group of customers with high spend yet high return. You can [create a segment](segments.md) to drive next best actions. 

## Build your own measure from scratch

This section walks you through creating a new measure from scratch. You can build a measure with data attributes from data entities that have a relationship set up to connect with the Customer entity. 

1. In audience insights, go to **Measures**.

1. Select **New** and choose **Build your own**.

   :::image type="content" source="media/build-own-measure.png" alt-text="Screenshot of drop-down menu with options to create a new measure.":::

1. Select **Edit name** and provide a **Name** for the measure. 
   > [!NOTE]
   > If your new measure configuration has only two fields, for exmample, CustomerID and one calculation, the output will be added as a new column to the system generated entity called Customer_Measure. And you will be able to see the measure’s value in the unified customer profile. Other measures will generate their own entities.

1. In the configuration area, choose the aggregation function from the **Select Function** drop-down menu. Aggregation functions include: 
   - **Sum**
   - **Average**
   - **Count**
   - **Count Unique**
   - **Max**
   - **Min**
   - **First**: takes the first value of the data record
   - **Last**: takes the last value that was added to the data record

   :::image type="content" source="media/measure-operators.png" alt-text="Operators for measure calculations.":::

1. Select **Add attribute** to select the data you need to create this measure.
   
   1. Select the **Attributes** tab. 
   1. Data entity: Choose the entity that includes the attribute you want to measure. 
   1. Data attribute: Choose the attribute you want to use in the aggregation function to calculate the measure. You can only select one attribute at a time.
   1. You can also select a data attribute from an existing measure by selecting the **Measures** tab. Or, you can search for an entity or measure name. 
   1. Select **Add** to add the selected attribute to the measure.

   :::image type="content" source="media/measure-attribute-selection.png" alt-text="Select an attribute to use in calculations.":::

1. To build more complex measures, you can add more attributes or use math operators on your measure function.

   :::image type="content" source="media/measure-math-operators.png" alt-text="Create a complex measure with math operators.":::

1. To add filters, select the **Filter** in the configuration area. 
  
   1. In **Add attribute** section of the **Filters** pane, select the attribute you want to use to create filters.
   1. Set the filter operators to define the filter for every selected attribute.
   1. Select **Apply** to add the filters to the measure.

1. To add dimensions, select **Dimension** in the configuration area. Dimensions will show as columns in the measure output entity.
   1. Select **Edit dimensions** to add data attributes you want to group the measure values by. For example, city or gender. By default, the *CustomerID* dimension is selected to create *customer-level measures*. You can remove the default dimension if you want to create *business-level measures*.
   1. Select **Done** to add the dimensions to the measure.

1. If there are values in your data that you need to replace with an integer, for example, replace *null* with *0*, select **Rules**. Configure the rule and make sure that you choose only whole numbers as replacements.

1. If there are multiple paths between the data entity you mapped and the *Customer* entity, you have to choose one of the identified [entity relationship paths](relationships.md). Measure results can vary depending on the selected path. 
   1. Select **Data preferences** and choose the entity path that should be used to identify your measure. If there's only a single path to the *Customer* entity, this control won't show.
   1. Select **Done** to apply your selection. 

   :::image type="content" source="media/measures-data-preferences.png" alt-text="Select the entity path for the measure.":::

1. To add more calculations for the measure, select **New calculation**. You can only use entities on the same entity path for new calculations. More calculations will show as new columns in the measure output entity.

1. Select **...** on the calculation to **Duplicate**, **Rename**, or **Remove** a calculation from a measure.

1. In the **Preview** area, you'll see the data schema of the measure output entity, including filters and dimensions. The preview reacts dynamically to changes in the configuration.

1. Select **Run** to calculate results for the configured measure. Select **Save and close** if you want to keep the current configuration and run the measure later.

1. Go to **Measures** to see the newly created measure in the list.

## Use a template to build a measure

You can use predefined templates of commonly used measures to create them. Detailed descriptions of the templates and a guided experience help you with efficient measure creation. Templates build on mapped data from the *Unified Activity* entity. So make sure you have configured [customer activities](activities.md) before you create a measure from a template.

Available measure templates: 
- Average transaction value (ATV)
- Total transaction value
- Average daily revenue
- Average yearly revenue
- Transaction count
- Loyalty points earned
- Loyalty points redeemed
- Loyalty points balance
- Active customer lifespan
- Loyalty membership duration
- Time since last purchase

The following procedure outlines the steps to build a new measure using a template.

1. In audience insights, go to **Measures**.

1. Select **New** and select **Choose a template**.

1. Find the template that fits your need and select **Choose template**.

1. Review the required data and select **Get started** if you have all the data in place.

1. In the **Edit name** pane, set the name for your measure and the output entity. 

1. Select **Done**.

1. In the **Set time period** section, define the time frame of the data to use. Choose if you want the new measure to cover the entire data set by selecting **All time**. Or if you want the measure to focus on a **Specific time period**.

   :::image type="content" source="media/measure-set-time-period.png" alt-text="Screenshot showing the time period section when configuring a measure from a template.":::

1. In the next section, select **Add data** to choose the activities and map the corresponding data from your *Unified Activity* entity.

    1. Step 1 of 2: Under **Activity type**, choose the type of the entity you want to use. For **Activities**, select the entities you want to map.
    1. Step 2 of 2: Choose the attribute from the *Unified Activity* entity for the component required by the formula. For example, for Average transaction value, it's the attribute representing the Transaction value. For **Activity timestamp**, choose the attribute from the Unified Activity entity that represents the date and time of the activity.
   
1. Once the data mapping is successful, you can see the status as **Complete** and the name of the mapped activities and attributes.

   :::image type="content" source="media/measure-template-configured.png" alt-text="Screenshot of a completed measure template configuration.":::

1. You can now select **Run** to calculate the results of the measure. To refine it later, select **Save draft**.

## Manage your measures

You can find the list of measures on the **Measures** page.

You'll find information about the measure type, the creator, creation date, status, and state. When you select a measure from the list, you can preview the output and download a .CSV file.

To refresh all of your measures at the same time, select **Refresh all** without selecting a specific measure.

> [!div class="mx-imgBorder"]
> ![Actions to manage single measures](media/measure-actions.png "Actions to manage single measures")

Select a measure from the list for the following options:

- Select the measure name to see its details.
- **Edit** the configuration of the measure.
- **Refresh** the measure based on the latest data.
- **Rename** the measure.
- **Delete** the measure.
- **Activate** or **Deactivate**. Inactive measures won't get refreshed during a [scheduled refresh](system.md#schedule-tab).

> [!TIP]
> There are [six types of status](system.md#status-types) for tasks/processes. Additionally, most processes [depend on other downstream processes](system.md#refresh-policies). You can select the status of a process to see details on the progress of the entire job. After selecting **See details** for one of the job's tasks, you find additional information: processing time, the last processing date, and all errors and warnings associated with the task.

## Next step

You cam use existing measures to create [a customer segment](segments.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]