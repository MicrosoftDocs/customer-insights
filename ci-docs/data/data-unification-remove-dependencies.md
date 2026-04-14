---
title: Remove unified fields, unified tables, and dependencies
description: Learn how to remove unified fields and tables and their dependencies in Customer Insights - Data.
ms.date: 04/09/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---
# Remove unified fields, unified tables, and dependencies

To protect your downstream processes that use the unified customer profile, Customer Insights - Data blocks removing fields that are in use. You can only remove a field after you remove downstream dependencies. When you remove all fields from a table, you can then remove the table. Remove dependencies in the reverse order they were created.

## Summary

1. In Dataverse, remove Dataverse dependencies on the field, such as a form that displays the field you wish to remove. Save your changes.

1. In Customer Insights - Data, remove dependencies on the unified field such as any segments, measures or other insights that use the field you wish to remove. Save your changes.

1. On the Unified data view step, exclude the field.  If you are removing an entire table, exclude all fields from the table. Save your changes.

1. On the Duplicate rules step, remove any deduplication rules that use the field(s). If you are removing an entire table, removal all deduplication rules for the table. Save your changes.

1. On the Matching conditions step, remove the field(s) from any rules. If you are removing an entire table, select the table and click Delete.

## Remove dependencies blocking unification

To identify specific dependencies, exclude a single field in the data unification configuration. Excluding multiple fields at once that have dependencies provides only a general error.

1. Go to **Data** > **Unify**.

1. Select **Edit** on the **Unified data view** tile.

1. Select a single field and then select **Exclude**.

1. Select **Done** to confirm and then select **Save and close**.

   If there are any dependencies, one of the following errors appears.

   - `Detected DataVerse dependencies in msdynci_customerprofile entity on these attribute(s): \<attribute names\>. Please delete these dependencies and merge again.` This message indicates there is a Dataverse dependency. Go to [Remove a Dataverse dependency](#remove-a-dataverse-dependency).
   - `The specified resource cannot be modified or deleted due to downstream dependency(s). To proceed, remove its usage from the following, in the order specified: {Segment, Measure, Export, or Insight name}.` This message indicates a Customer Insights - Data dependency. Remove the field from use in the specified feature.

1. After you remove all listed dependencies, return to **Customer Insights - Data** > **Unify** > **Merge** and run the merge again.

### Remove a Dataverse dependency

When you update the **Unify** configuration in Dynamics 365 Customer Insights - Data, the system checks whether other solution components reference any attributes that you want to remove from the `msdynci_customerprofile` table in Dataverse. Customer Insights - Data writes unified customer profiles to this table in your Dataverse environment. Each mapped and merged field from your data sources becomes a column on this table. When other users in the organization create forms, views, workflows, or other components that reference those columns, Dataverse prevents the deletion of those columns, even when Customer Insights requests the deletion.

1. In [Power Apps](https://make.powerapps.com), open the environment associated with your Customer Insights instance.

1. Go to **Tables**, search for **CustomerProfile** (`msdynci_customerprofile`), and open it.

1. Select a column listed in the error message, and then choose **Advanced** > **Show dependencies**.

1. Review the **Dependent components** list, which shows exactly which forms, views, workflows, or other components reference that column.

   | Component type | How to remove the dependency |
   |---|---|
   | **Form** | Open the form in the form designer, remove the column from the form layout, and then save and publish. |
   | **View** | Open the view editor, remove the column from the view's columns and filter criteria, and then save and publish. |
   | **Chart** | Edit the chart and remove references to the column. |
   | **Cloud flow / workflow** | Edit the flow in Power Automate and remove any steps that reference the column. |
   | **Business rule** | Edit the business rule and remove conditions or actions that reference the column. |
   | **Business process flow** | Edit the business process flow and remove any stage fields that reference the column. |

## Remove a unified field

1. [Remove the dependencies](#remove-dependencies-blocking-unification) for the field.

1. Go to **Data** > **Unify**.

1. Select **Edit** on the **Unified data view** tile.

1. Select all occurrences of the field and then select **Exclude**.

   :::image type="content" source="media/m3_remove_attribute1.png" alt-text="Screenshot of Unified fields page showing selected fields and Exclude button":::

1. Select **Done** to confirm and then select **Save and close**.

   > [!TIP]
   > If you see the message "Couldn't save unify. The specified resource can't be modified or deleted due to downstream dependencies", the field is still used in a downstream dependency. Go to [Remove dependencies blocking unification](#remove-dependencies-blocking-unification).

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

Tables can be removed from unification after you [remove all the fields from the table](#remove-a-unified-field).

1. Go to **Data** > **Unify** and select **Edit** on the **Customer data** tile.

1. Select **Select tables and columns** and clear the checkbox next to the table.

   :::image type="content" source="media/m3_remove_table3.png" alt-text="Screenshot of Select tables and columns dialog box with table checkbox cleared":::

   > [!TIP]
   > If you see any fields in a disabled state, the field is still used in a downstream dependency. Go to [Remove dependencies blocking unification](#remove-dependencies-blocking-unification).

1. Select **Apply**.

1. Select **Save and close**.

1. Run unification by selecting **Unify** > **Unify customer profiles and dependencies** to update the unified profile.

[!INCLUDE[footer-include](includes/footer-banner.md)]