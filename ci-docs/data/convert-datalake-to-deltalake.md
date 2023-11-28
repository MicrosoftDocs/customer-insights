---
title: "Convert a Data Lake data source to a Delta Lake data source (preview)"
description: "Convert a Data Lake data source to a Delta Lake data source in Customer Insights - Data."
ms.date: 11/28/2023
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Convert a Data Lake data source to a Delta Lake data source (preview)

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

[!INCLUDE [public-preview-banner](./includes/public-preview-banner.md)]

<!--- When remove preview, remove preview note from data-sources-manage.md --->

Take an existing Azure Data Lake data source in Customers Insights - Data and convert it to an Azure Data Lake with Delta tables (preview) data source.

[Delta](https://go.microsoft.com/fwlink/?linkid=2248260) is a term introduced with Delta Lake, the foundation for storing data and tables in the Databricks Lakehouse Platform. Delta Lake is an open-source storage layer that brings ACID (atomicity, consistency, isolation, and durability) transactions to big data workloads. For more information, see the [Delta Lake Documentation Page.](https://docs.delta.io/latest/delta-intro.html)

Key reasons to connect to data stored in Delta format:

- Directly import Delta formatted data saving time and effort.
- Eliminate the compute and storage costs associated with transforming and storing a copy of your lakehouse data.
- Automatically improve the reliability of data ingestion to Customer Insights - Data provided by Delta versioning.

[!INCLUDE [public-preview-note](./includes/public-preview-note.md)]

## Prerequisites

- The Azure Data Lake Storage must be in the same tenant and Azure region as Customer Insights - Data.

- The Customer Insights - Data service principal must have Storage Blob Data Contributor permissions to access the storage account. For more information, see [Grant permissions to the service principal to access the storage account](connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).

- The user that converts the data source needs at least Storage Blob Data Reader permissions on the Azure Data Lake Storage account.

- Data stored in online services may be stored in a different location than where data is processed or stored. By importing or connecting to data stored in online services, you agree that data can be transferred. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- The Delta tables must be in a separate folder in the storage container and can't be in the container root directory. For example, c:\MyDeltaData\MyDeltaTable\_delta_log.

- The Delta tables must correspond to the tables in the existing Data Lake data source and be in the same storage container. The Delta tables must not reside in the storage container’s root, but must instead reside in a Delta root folder. For example:

  ```
  storage_container_root/
      ~~contoso_table~~
      DeltaLakeDataRoot/
         ADeltaLakeTable/
               _delta_log/
                   0000.json
                   0001.json
               part-0001-snappy.parquet
               part-0002-snappy.parquet
  ```

## Update a Data Lake data source to Delta Lake

1. Go to **Data** > **Data sources**.

1. Select the Azure Data Lake data source and then select **Update to Delta Lake**. Or, select **Begin update** from the **Add tables** page if you're editing the Data Lake data source.

   :::image type="content" source="media/delta-lake-convert.png" alt-text="Dialog box to enter connection details for Delta Lake.":::

1. Select **Browse** and navigate to the folder that contains the data in Delta format and select it. Then, select **Update data source**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   > [!IMPORTANT]
   > Don't stop the refreshing process as it could negatively impact updating the data source.
   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

We recommend you continue to stream your data to the Data Lake Storage location through your existing pipeline and maintain the manifests and schemas until you determine the update was successful and everything is working as expected.

## Revert the conversion from Delta Lake to Data Lake

If you tried to [convert an Azure Data Lake data source to a Delta Lake data source](/dynamics365/customer-insights/convert-datalake-to-deltalake) and the process fails, perform the following steps.

### Prerequisites

- Your organization has continued to stream the Data Lake Storage data through your pipeline.
- Your organization has maintained the Data Lake Storage manifests and schemas.

### Revert back to an Azure Data Lake data source

1. Go to **Data** > **Data sources**.

1. Select the Azure Data Lake data source and then select **Revert to ADLS**.

1. Confirm that you want to revert. The **Data sources** page opens showing the new data source in **Refreshing** status.

   > [!IMPORTANT]
   > Don't stop the refreshing process as it could negatively impact reverting the data source.


[!INCLUDE [footer-include](includes/footer-banner.md)]
