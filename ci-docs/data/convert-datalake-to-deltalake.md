---
title: "Update a Common Data Model data source to use Delta tables (preview)"
description: "Update Common Data Model tables in Azure Data Lake to Delta format in Customer Insights - Data."
ms.date: 02/26/2024
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Update a Common Data Model data source to use Delta tables (preview)

[!INCLUDE [public-preview-banner](./includes/public-preview-banner.md)]

<!--- When remove preview, remove preview note from data-sources-manage.md --->

Take an existing Azure Data Lake data source with Common Data Model (CDM) tables and update it to use Delta tables (preview).

[!INCLUDE [delta-lake-info](./includes/delta-lake-info.md)]

[!INCLUDE [delta-lake-benefits](./includes/delta-lake-benefits.md)]

[!INCLUDE [public-preview-note](./includes/public-preview-note.md)]

## Prerequisites

[!INCLUDE [delta-lake-prereqs](./includes/delta-lake-prereqs.md)]

- The Delta tables and their schema must match the tables in the existing CDM data source and be in the same storage container. The tables in the new data folder must match exactly to the selected tables in the CDM data source. The tables names and their schemas must match exactly. In Delta, table names are the same as the folder name where the data is stored. Therefore, the folder names must match exactly to the selected tables in the CDM data source. Otherwise, the update fails.

  For example, if the selected CDM data source tables are Table1 and Table2, then the folder you choose for the update must show Table1 and Table2 in the hierarchy.

  ```
  storageaccountroot/
   DeltaDataRoot/
      Table1/
      Table2/
  ```

## Update a Common Data Model data source to use Delta tables

1. Go to **Data** > **Data sources**.

1. Select the Azure Data Lake CDM data source and then select **Update to Delta tables**. Or, select **Begin update** from the **Add tables** page if you're editing the CDM data source.

   :::image type="content" source="media/delta-lake-update.svg" alt-text="Dialog box to enter connection details for Delta Lake.":::

1. Select **Browse** and navigate to the folder that contains the data in Delta format and *exactly matches* the selected Azure Data Lake data source table. Select it, and then select **Update data source**.

   The **Data sources** page opens showing the new data source in **Refreshing** status.

   > [!IMPORTANT]
   > Don't stop the refreshing process as it could negatively impact updating the data source.
   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

We recommend you continue to stream your data to the Data Lake Storage location through your existing pipeline and maintain the manifests and schemas until you determine the update was successful and everything is working as expected.

## Revert the conversion from CDM tables to Delta tables

If you tried to update an Azure Data Lake CDM data source to Delta tables and the process fails, perform the following steps.

### Prerequisites

- Your organization has continued to stream the Data Lake Storage data through your pipeline.
- Your organization has maintained the Data Lake Storage manifests and schemas.

### Revert back to an Azure Data Lake CDM data source

1. Go to **Data** > **Data sources**.

1. Select the Azure Data Lake CDM data source and then select **Revert to ADLS**.

1. Confirm that you want to revert. The **Data sources** page opens showing the new data source in **Refreshing** status.

   > [!IMPORTANT]
   > Don't stop the refreshing process as it could negatively impact reverting the data source.

[!INCLUDE [footer-include](includes/footer-banner.md)]
