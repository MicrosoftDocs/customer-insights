---
title: Access Customer Insights - Data output tables in Microsoft Fabric
description: "Customer Insights - Data output tables: Link Dataverse data to Microsoft Fabric and use unified profiles, segments, measures, and predictions."
ms.date: 11/18/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Access Customer Insights - Data output tables in Microsoft Fabric

After you unify your customer data in Dynamics 365 Customer Insights - Data and build insights, such as measures, segments, enrichments, and predictions, you can use those results in other analytics tools. For example, data engineers want to join unified customer profiles with other data in a lakehouse, data scientists want to train models on segment membership and customer measures, and analysts want to build Power BI reports with prediction scores.

Customer Insights - Data writes its output tables to Microsoft Dataverse. Dataverse provides a built-in **Link to Microsoft Fabric** capability that makes Dataverse tables available in Microsoft OneLake. You don't need a new Customer Insights - Data feature, an export, or an extract, transform, and load (ETL) pipeline to get your Customer Insights - Data output into Fabric.

> [!NOTE]
> Link to Microsoft Fabric is a Dataverse and Power Apps capability. This article summarizes how to use it with Customer Insights - Data. For full setup steps, prerequisites, and limits, see [Link your Dataverse environment to Microsoft Fabric](/power-apps/maker/data-platform/azure-synapse-link-view-in-fabric) and [Configure your environment and link to Microsoft Fabric](/power-apps/maker/data-platform/fabric-link-to-data-platform).

## Prerequisites

- A Customer Insights - Data environment that has completed data unification and the insights you want to use, such as measures, segments, or predictions.
- The **System Administrator** security role in the Power Platform environment that Customer Insights - Data writes to.
- A Fabric capacity (or Power BI Premium capacity) and admin access to the target Fabric workspace.

For the complete list of Dataverse and Fabric prerequisites, including the required Fabric tenant settings and capacity permissions, see [Prerequisites for Link to Microsoft Fabric](/power-apps/maker/data-platform/fabric-link-to-data-platform#prerequisites).

## Link your Dataverse environment to Fabric

1. Sign in to [Power Apps](https://make.powerapps.com) and select the environment that's associated with your Customer Insights - Data environment.

1. On the left navigation pane, select **Link data**. If the item isn't in the pane, select **More** and then select **Link data**.

   :::image type="content" source="media/power-apps-link-data.png" alt-text="Screenshot of the Power Apps Link data page with Fabric Links tab." lightbox="media/power-apps-link-data.png":::

   > [!TIP]
   > If your environment already has a Fabric link, you don't need to create a new one. Select the existing link on the **Link data** page, and then select **Manage tables** to add the Customer Insights - Data tables to it.

1. Select **New link** (or **Create a new Fabric link**) and follow the wizard. The wizard checks your prerequisites, connects to your Fabric workspace, and lets you select the [tables to link](#customer-insights---data-output-tables-in-dataverse).

1. Make sure the Customer Insights - Data tables that you need, such as `msdynci_customerprofile` and `msdynci_segmentmembership`, are included in the link.

1. Review and create the link.

When you create the link, Dataverse creates a Fabric lakehouse, a SQL analytics endpoint, and a Power BI semantic model in the selected workspace. Dataverse tables, including your Customer Insights - Data output tables, link to the lakehouse through shortcuts. Your data stays in Dataverse. As data changes in Dataverse, for example after a Customer Insights - Data refresh, the changes automatically reflect in the lakehouse.

## Use Customer Insights - Data tables in Fabric

After the link is in place, you can work with your Customer Insights - Data output in any Fabric workload. For example:

- Query unified profiles, segment membership, and measures with T-SQL through the SQL analytics endpoint.
- Combine Customer Insights - Data output with other data in OneLake by using Spark or Python notebooks.
- Build Power BI reports on the generated semantic model.
- Grant other users access to the Fabric workspace so that they can work with the data.

## Customer Insights - Data output tables in Dataverse

As you work in Customer Insights - Data to unify data and create segments, measures, activities, enrichments, and predictions, the resulting tables appear on the **Tables** page under the **Output** tab. Customer Insights - Data also writes the main output tables to the Dataverse environment that's associated with your Customer Insights - Data environment, including the following tables:

| Output | Dataverse table |
|---|---|
| Unified customer profiles | `msdynci_customerprofile` |
| Unified activities | `msdynci_unifiedactivity` |
| Segment membership | `msdynci_segmentmembership` |
| Customer attribute measures | `msdynci_customermeasure` |
| Enrichment data | `msdynci_enrichment` |
| Prediction model output | `msdynci_prediction` |

Customer measures that you configure as tables are written to their own Dataverse tables. For more information, see [Use calculated measures in Dataverse-based applications](dataverse-measures.md).

For the full list of tables and their schemas, see [View Customer Insights - Data tables in Dataverse](tables.md#view-customer-insights---data-tables-in-dataverse) and [Table schemas](table-schemas.md).

> [!NOTE]
> Tables that you add to OneLake through Link to Microsoft Fabric consume Dataverse storage. Admins can view storage consumption in the Power Platform admin center.

## Tables that aren't written to Dataverse

Not all Customer Insights - Data tables are written to Dataverse. The following intermediate data unification tables are **not** written to Dataverse, so they aren't available through Link to Microsoft Fabric:

- **Deduplication tables** (`Deduplication_<TableName>`): the deduplicated records for each source table that's part of data unification.
- **Match pairs** (`ConflationMatchPairs`): the record pairs that matched across tables during data unification.

To use these tables in Fabric, export them from Customer Insights - Data to Azure Data Lake Storage Gen2, and then reference the exported data from Fabric with a OneLake shortcut.

1. In Customer Insights - Data, [set up an export to Azure Data Lake Storage Gen2](export-azure-data-lake-storage-gen2.md) and select the `Deduplication_<TableName>` and `ConflationMatchPairs` tables you need. Exports run with every scheduled refresh, and you can also run them on demand.

1. In Fabric, open a lakehouse and [create an Azure Data Lake Storage Gen2 shortcut](/fabric/onelake/create-adls-shortcut) that points to the export folder in your storage account.

> [!IMPORTANT]
> - The Azure Data Lake Storage Gen2 export writes CSV files. Exports of large tables can create multiple CSV files in the same folder. In Fabric, you can load the CSV files into Delta tables in your lakehouse by using a notebook, a pipeline, or a dataflow.
> - To create an Azure Data Lake Storage Gen2 shortcut, hierarchical namespace must be enabled on the storage account.

## Related content

- [Link your Dataverse environment to Microsoft Fabric](/power-apps/maker/data-platform/azure-synapse-link-view-in-fabric)
- [Configure your environment and link to Microsoft Fabric](/power-apps/maker/data-platform/fabric-link-to-data-platform)
- [View tables in Customer Insights - Data](tables.md)
- [Export data to Azure Data Lake Storage Gen2](export-azure-data-lake-storage-gen2.md)
- [Create an Azure Data Lake Storage Gen2 shortcut](/fabric/onelake/create-adls-shortcut)