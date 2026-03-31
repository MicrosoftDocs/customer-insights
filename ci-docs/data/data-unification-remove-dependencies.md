---
title: Remove unified fields, unified tables, and dependencies
description: Learn how to remove unified fields and tables and their dependencies in Customer Insights - Data.
ms.date: 03/27/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---
# Remove unified fields, unified tables, and dependencies

To remove a unified field or table, first remove the field or table from all dependencies such as segments, measures, enrichments, forms, or views. Then, you can remove them from the unification configuration.

## Remove a unified field

1. [Remove the dependencies](#remove-dependencies-blocking-unification) for the field.

1. Go to **Data** > **Unify**.

1. Select **Edit** on the **Unified data view** tile.

1. Select all occurrences of the field and then select **Exclude**.

   :::image type="content" source="media/m3_remove_attribute1.png" alt-text="Screenshot of Unified fields page showing selected fields and Exclude button":::

1. Select **Done** to confirm and then select **Save and close**.

   > [!TIP]
   > If you see the message "Couldn't save unify. The specified resource can't be modified or deleted due to downstream dependencies", the field is still used in a downstream dependency.

1. If the field is used in a rule for deduplication rules or matching rules, perform the following steps. Otherwise, go to the next step.
   1. Select **Edit** on the **Deduplication rules** tile.
   1. Remove the field from all rules it's used in, if any, and then select **Next**.
   1. On the **Matching rules** page, remove the field from all rules it's used in, if any, and then select **Save and close**.
   1. Select **Unify** > **Unify customer profiles and dependencies**. Wait for unification to complete before going to the next step.

1. Select **Edit** on the **Customer data** tile.

1. Select **Select tables and columns** and clear the checkbox next to each occurrence of the field.

   :::image type="content" source="media/m3_remove_attribute2.png" alt-text="Screenshot of Select tables and columns dialog box showing cleared checkboxes":::

1. Select **Apply**.

1. Select **Save and close**.

1. Select **Unify** > **Unify customer profiles and dependencies** to update the unified profile.

## Remove a unified table

1. [Remove the dependencies](#remove-dependencies-blocking-unification) for the table.

1. Go to **Data** > **Unify**.

1. Select **Edit** on the **Unified data view** tile.

1. Expand the columns and select all fields for the table. Then select **Exclude**.

   :::image type="content" source="media/m3_remove_table1.png" alt-text="Screenshot of Unified fields with all fields for a table selected and Exclude button":::

1. Select **Done** to confirm and then select **Save and close**.

   > [!TIP]
   > If you see the message "Couldn't save unify. The specified resource can't be modified or deleted due to downstream dependencies", the table is still used in a downstream dependency.

1. Select **Edit** on the **Deduplication rules** tile.

1. Remove all rules from the table, if any, and then select **Next**.

1. On the **Matching rules** page, select the table and then select **Delete**.

   :::image type="content" source="media/m3_remove_table2.png" alt-text="Screenshot of Matching rules with table selected and Delete button":::

   > [!TIP]
   > The **Delete** command isn't visible until you remove all dependencies and rules for the table.

1. Select **Save and close**.

1. Select **Edit** on the **Customer data** tile.

1. Select **Select tables and columns** and clear the checkbox next to the table.

   :::image type="content" source="media/m3_remove_table3.png" alt-text="Screenshot of Select tables and columns dialog box with table checkbox cleared":::

1. Select **Apply**.

1. Select **Save and close**.

1. Run unification by selecting **Unify** > **Unify customer profiles and dependencies** to update the unified profile.

## Remove dependencies blocking unification

When you update the **Unify** configuration in Dynamics 365 Customer Insights - Data (for example, by removing a data source, removing mapped fields, or changing merge policies), the system checks whether other solution components reference any attributes that you want to remove from the `msdynci_customerprofile` table in Dataverse.

If the system finds dependencies, you see an error similar to the following message:

`Detected Dataverse dependencies in msdynci_customerprofile entity on these attribute(s): \<attribute names\>. Please delete these dependencies and merge again.`

Customer Insights - Data writes unified customer profiles to a virtual table called `msdynci_customerprofile` in your Dataverse environment. Each mapped and merged field from your data sources becomes a column on this table. When other users in the organization create segments, measures, forms, views, workflows, or other components that reference those columns, Dataverse prevents the deletion of those columns, even when Customer Insights requests the deletion.

### Identify dependencies and remove them

1. In [Power Apps](https://make.powerapps.com), open the environment associated with your Customer Insights instance.

1. Go to **Tables**, search for **CustomerProfile** (`msdynci_customerprofile`), and open it.

1. Select a column listed in the error message, and then choose **Advanced** > **Show dependencies**.

1. Review the **Dependent components** list, which shows exactly which segments, measures, forms, views, workflows, or other components reference that column.

1. For segments, measures, enrichments, or relationships, edit the component in Customer Insights - Data and remove references to the column. For other dependent components listed:

   | Component type | How to remove the dependency |
   |---|---|
   | **Form** | Open the form in the form designer, remove the column from the form layout, and then save and publish. |
   | **View** | Open the view editor, remove the column from the view's columns and filter criteria, and then save and publish. |
   | **Chart** | Edit the chart and remove references to the column. |
   | **Cloud flow / workflow** | Edit the flow in Power Automate and remove any steps that reference the column. |
   | **Business rule** | Edit the business rule and remove conditions or actions that reference the column. |
   | **Business process flow** | Edit the business process flow and remove any stage fields that reference the column. |

1. After you remove all listed dependencies, return to **Customer Insights - Data** > **Unify** > **Merge** and run the merge again.

[!INCLUDE[footer-include](includes/footer-banner.md)]