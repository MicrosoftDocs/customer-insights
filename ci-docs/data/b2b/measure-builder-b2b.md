---
title: "Create business account measures with measure builder"
description: "Build measures from scratch to analyze key metrics about your business accounts."
ms.date: 09/01/2023
ms.topic: how-to
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Create business account measures with measure builder



Create measures on the level of individual accounts (customer measure) or on the level of all accounts (business measure).

- Customer measure: Generates output as its own table. Customer measures don't show in the customer profile card.

- Business measure: Generates output as its own table and shows on the home page of your Dynamics 365 Customer Insights - Data environment.

> [!TIP]
> If your B2B environment [uses accounts with hierarchies](account-hierarchies.md), choose whether to aggregate the measure across related sub-accounts.

1. Go to **Insights** > **Measures**.

1. Select **New**.

   :::image type="content" source="media/measure-b2b.png" alt-text="Empty configuration screen for a B2B measure. ":::

1. Select **Edit details** next to Untitled measure. Provide a name for the measure. Optionally, add [tags](../work-with-tags-columns.md#manage-tags) to the measure. 

   :::image type="content" source="../media/measures_edit_details.png" alt-text="Edit details dialog box.":::

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
   1. Data table: Choose the table that includes the attribute you want to measure.
   1. Data attribute: Choose the attribute you want to use in the aggregation function to calculate the measure. You can only select one attribute at a time.
   1. Optionally, choose a data attribute from an existing measure by selecting the **Measures** tab, or search for a table or measure name.
   1. Select **Add** to add the selected attribute to the measure.

1. To build more complex measures, add more attributes or use math operators on your measure function.

1. To add filters, select the **Filter** in the configuration area. Applying filters will only use the records that match the filters to calculate the measure.
  
   1. In the **Add attribute** section of the **Filters** pane, select the attribute you want to use to create filters.
   1. Set the filter operators to define the filter for every selected attribute.
   1. Select **Apply** to add the filters to the measure.

1. Select **Dimension** to choose more fields to add as columns to the measure output table.

   1. Select **Edit dimensions** to add data attributes you want to group the measure values by. For example, city or gender.
      > [!TIP]
      > The *CustomerId* attribute is already added indicating this is a customer level measure type. If you remove the attribute, the measure type changes to business level.
   1. Select **Done** to add the dimensions to the measure.

1. If there are values in your data that must be replaced with an integer, select **Rules**. Configure the rule and make sure that you choose only whole numbers as replacements. For example, replace *null* with *0*.

1. If you [use accounts with hierarchies](account-hierarchies.md), review **Roll up sub-accounts**.
   - To calculate the measure for every account, select **No**. Every account gets its own result.
   - To calculate one result, select **Yes**. Select **Edit** to choose the account hierarchy according to the ingested hierarchies and select **Apply**. The measure yields only one result because it's aggregated with sub-accounts.

1. If there are multiple paths between the data table you mapped and the *Customer* table, choose one of the identified [relationship paths](../relationships.md). Measure results can vary depending on the selected path.

   1. Select **Relationship path** and choose the path that should be used to identify your measure. If there's only a single path to the *Customer* table, this control won't show.
   1. Select **Done** to apply your selection.

1. Select the vertical ellipsis (&vellip;) on the calculation to **Duplicate** or **Remove** a calculation from a measure.

1. In the **Preview** area, you'll see the data schema of the measure output table, including filters and dimensions. The preview reacts dynamically to changes in the configuration.

1. Select **Run** to calculate results for the configured measure. Select **Save and close** if you want to keep the current configuration and run the measure later. The **Measures** page displays.

[!INCLUDE [footer-include](../includes/footer-banner.md)]
