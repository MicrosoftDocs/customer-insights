---
title: "Update a Common Data Model data source to use Delta tables"
description: "Learn how to convert Common Data Model tables in Azure Data Lake to Delta format in Customer Insights - Data."
ms.date: 04/21/2025
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Update a Common Data Model data source to use Delta tables

Update an existing data connection with Common Data Model tables and move to Delta-formatted tables without removing and recreating an existing configuration that depends on the data connection.

[!INCLUDE [delta-lake-benefits](./includes/delta-lake-benefits.md)]

[!INCLUDE [delta-lake-info](./includes/delta-lake-info.md)]

## Prerequisites

[!INCLUDE [delta-lake-prereqs](./includes/delta-lake-prereqs.md)]

- The Delta tables and their schema must match the tables in the existing Common Data Model data source and be in the same storage container. The tables in the new data folder must match exactly to the selected tables in the Common Data Model data source. The tables names and their schemas must match exactly. In Delta, table names are the same as the folder name where the data is stored. Therefore, the folder names must match exactly to the selected tables in the Common Data Model data source. Otherwise, the update fails.

  For example, if the selected Common Data Model data source tables are Table1 and Table2, then the folder you choose for the update must show Table1 and Table2 in the hierarchy.

  ```
  storageaccountroot/
   DeltaDataRoot/
      Table1/
      Table2/
  ```

## Update Common Data Model data tables to Delta tables

1. Go to **Data** > **Data sources**.

1. Select the Azure Data Lake Common Data Model data source and then select **Update to Delta tables**. Or, select **Begin update** from the **Add tables** page if you're editing the Common Data Model data source.

   :::image type="content" source="media/delta-lake-update.svg" alt-text="Data sources page showing a Common Data Model data source with Update to Delta tables highlighted.":::

1. Select **Browse** and navigate to the folder that contains the data in Delta format and *exactly matches* the selected Azure Data Lake data source table. Select it, and then select **Update data source**.

   The **Data sources** page opens showing the new data source in **Refreshing** status.

   > [!IMPORTANT]
   > Don't stop the refreshing process as it could negatively impact updating the data source.
   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

We recommend you continue to stream your data to the Data Lake Storage location through your existing pipeline and maintain the manifests and schemas until you determine the update was successful and everything is working as expected.

## Revert the conversion from Common Data Model tables to Delta tables

If you tried to update an Azure Data Lake Common Data Model data source to Delta tables and the process fails, perform the following steps.

### Prerequisites

- Your organization has continued to stream the Data Lake Storage data through your pipeline.
- Your organization has maintained the Data Lake Storage manifests and schemas.

### Revert back to an Azure Data Lake Common Data Model data source

1. Go to **Data** > **Data sources**.

1. Select the Azure Data Lake Common Data Model data source and then select **Revert to Common Data Model tables**.

1. Confirm that you want to revert. The **Data sources** page opens showing the new data source in **Refreshing** status.

   > [!IMPORTANT]
   > Don't stop the refreshing process as it could negatively impact reverting the data source.

[!INCLUDE [footer-include](includes/footer-banner.md)]
