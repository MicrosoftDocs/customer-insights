---
title: "Create and edit measures"
description: "Define customer-related measures to analyze and reflect the performance of certain business areas."
ms.date: 04/17/2020
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: wameng
manager: shellyha
---

# Define and manage measures

**Measures** represent key performance indicators (KPIs) that reflect the performance and health of specific business areas. Audience insights provides an intuitive experience for building different types of measures, using a query builder that doesn't require you to code or validate your measures manually. You can track your business measures on the **Home** page, see measures for specific customers on the **Customer Card**, and use measures to define customer segments on the **Segments** page.

## Create a measure

This section walks you through creating a measure from scratch. You can build measures with data from multiple data sources that are connected through the Customer entity.

1. In audience insights, go to **Measures**.

2. Select **New measure**.

3. Choose the measure **Type**:

   - **Customer attribute**: A single field per customer that reflects a score, value, or state for the customer. Customer attributes are created as attributes in a new system-generated entity called **Customer_Measure**.

   - **Customer measure**: Insights on customer behavior with breakdown by selected dimensions. A new entity is generated for each measure, potentially with multiple records per customer.

   - **Business measure**: Tracks your business performance and health of the business. Business measures can have two different outputs: a numeric output that shows on the **Home** page or a new entity that you find on the **Entities** page.

4. Provide a **Name** and an optional **Display name**, then select **Next**.

5. In the **Entities** section, select the first entity from the drop-down list. At this point, you should decide whether additional entities are needed as part of your measure definition.

   > [!div class="mx-imgBorder"]
   > ![Measure definition](media/measure-definition.png "Measure definition")

   To add more entities, select **Add entity** and select entities you want to use for the measure.

   > [!NOTE]
   > You can select only entities that have relationships to your starting entity. For more information about defining relationships, see [Relationships](relationships.md).

6. Optionally, you can configure variables. In the **Variables** section, select **New variable**.

   Variables are calculations that are made on each of your selected records. For example, summing point-of-sale (POS) and online sales for each of your customers' records.

7. Provide a **Name** for the variable.

8. In the **Expression** area, choose a field to begin your calculation with.

9. Type an expression in the **Expression** area while choosing more fields to be included in your calculation.

   > [!NOTE]
   > Currently, only arithmetic expressions are supported. Additionally, variable calculation isn't supported for entities from different [entity paths](relationships.md).

10. Select **Done**.

11. In the **Measure definition** section, you'll define how your chosen entities and calculated variables are aggregated in a new measure entity or attribute.

12. Select **New dimension**. You can think of a dimension as a *group by* function. The data output of your Measure entity or attribute will be grouped by all of your defined dimensions.

    > [!div class="mx-imgBorder"]
    > ![Choose aggregate cycle](media/measures-businessreport-measure-definition2.png "Choose aggregate cycle")

    Select or enter the following information as part of your dimension's definition:

    - **Entity**: If you define a Measure entity, it should include at least one attribute. If you define a Measure attribute, it will include only one attribute by default. This selection is about choosing the entity that includes that attribute.
    - **Field**: Choose the specific attribute to be included either in your Measure entity or attribute.
    - **Bucket**: Choose whether you want to aggregate data on a daily, monthly, or annual basis. It's a required selection only if you've selected a Date type attribute.
    - **As**: Defines the name of your new field.
    - **Display name**: Defines the display name of your field.

    > [!NOTE]
    > Your business measure will be saved as a single-number entity and will appear on the **Home** page unless you add more dimensions to your measure. After adding more dimensions, the measure will *not* show up on the **Home** page.

13. Optionally, add aggregation functions. Any aggregation that you create results in a new value within your Measures entity or attribute. Supported aggregation functions are: **Min**, **Max**, **Average**, **Median**, **Sum**, **Count Unique**, **First** (takes the first record of a dimension value), and **Last** (takes the last record added to a dimension value).

14. Select **Save** to apply your changes to the measure.

## Manage your measures

After creating at least one measure, you'll see a list of measures on the **Measures** page.

You'll find information about the measure type, the creator, creation date and time, last edit date and time, status (whether the measure is active, inactive, or failed), and last refresh date and time. When you select a measure from the list, you can see a preview of its output.

To refresh all of your measures at the same time, select **Refresh all** without selecting a specific measure.

> [!div class="mx-imgBorder"]
> ![Actions to manage single measures](media/measure-actions.png "Actions to manage single measures")

Alternatively, select a measure from the list and perform one of the following actions:

- Select the measure name to see its details.
- **Edit** the configuration of the measure.
- **Rename** the measure.
- **Delete** the measure.
- Select the ellipsis (...) and then **Refresh** to start the refresh process for the measure.
- Select the ellipsis (...) and then **Download** to get a .CSV file of the measure.

> [!TIP]
> There are [six types of status](system.md#status-types) for tasks/processes. Additionally, most processes [depend on other downstream processes](system.md#refresh-policies). You can select the status of a process to see details on the progress of the entire job. After selecting **See details** for one of the job's tasks, you find additional information: processing time, the last processing date, and all errors and warnings associated with the task.

## Next step

You cam use existing measures to create your first customer segment on the **Segments** page. For more information, see [Segments](segments.md).
