---
title: "Connect data stored in Delta Lake format from your Azure Data Lake Storage"
description: "Work with data stored in Delta Lake format from Azure Data Lake Storage."
ms.date: 10/02/2023
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Connect to data stored in Delta format from your Azure Data Lake Storage (preview)

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

[!INCLUDE [public-preview-banner](./includes/public-preview-banner.md)]

Connect to data in Delta format and bring it into Dynamics 365 Customer Insights - Data. [Delta](https://go.microsoft.com/fwlink/?linkid=2248260) is a term introduced with Delta Lake, the foundation for storing data and tables in the Databricks Lakehouse Platform. Delta Lake is an open-source storage layer that brings ACID (atomicity, consistency, isolation, and durability) transactions to big data workloads. For more information, see the [Delta Lake Documentation Page.](https://docs.delta.io/latest/delta-intro.html)

Key reasons to connect to data stored in Delta format:

- Seamlessly bring in data that is already prepared and stored in your lakehouse
- Better manage large data sources that change frequently
- Have direct integration with stored data without the need for intermediate staging data copies in other formats or more transforms
- Minimize the time to prepare data for unification and insights

[!INCLUDE [public-preview-banner](./includes/public-preview-note.md)]

## Prerequisites

- The Azure Data Lake Storage you want to connect and ingest data from has to be in the same tenant and Azure region as the Dynamics 365 Customer Insights - Data environment.

- The Customer Insights - Data service principal must have Storage Blob Data Contributor permissions to access the storage account. For more information, see [Grant permissions to the service principal to access the storage account](connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).

- The user that sets up the data source connection needs at least Storage Blob Data Reader permissions on the Azure Data Lake Storage account.

- Data in your Azure Data Lake Storage must be in Delta format. Customer Insights - Data relies on the version property in the table's history to identify the latest changes for incremental processing.

- The Delta tables must be in a separate folder in the storage container and can't be in the container root directory.

> [!NOTE]
> Data stored in online services may be stored in a different location than where data is processed or stored. By importing or connecting to data stored in online services, you agree that data can be transferred. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

## Connect to Delta data from Azure Data Lake Storage

1. Go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Azure Data Lake Storage Gen 2 - Delta tables (Preview)**.

   :::image type="content" source="media/delta-lake-new.png" alt-text="Dialog box to enter connection details for Delta Lake.":::

1. Enter a **Data source name** and an optional **Description**. The name is referenced in downstream processes and it's not possible to change it after creating the data source.

1. Choose one of the following options for **Connect your storage using**.

   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**. Optionally, if you want to ingest data from a storage account through an Azure Private Link, select **Enable Private Link**. For more information, see [Private Links](private-link.md).
   - **Azure resource**: Enter the **Resource Id**. Optionally, if you want to ingest data from a storage account through an Azure Private Link, select **Enable Private Link**. For more information, see [Private Links](private-link.md).

1. Choose the name of the **Container** that contains the folder of your data, and select **Next**.

1. Navigate to the folder that contains the data in Delta format and select it. Then, select **Next**. A list of available tables displays.

   :::image type="content" source="media/delta-review-tables.png" alt-text="Dialog box of a list of tables to select":::

1. Select the tables you want to include.

1. To enable data profiling on any of the columns, select the number of **Columns** for the table. The **Manage attributes** page displays.

   :::image type="content" source="media/delta-dataprofiling-columns.png" alt-text="Dialog box to select data profiling.":::

   1. Select **Data profiling** for the whole table or for specific columns. By default, no table is enabled for data profiling.
   1. Select **Done**.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Tables**](tables.md) page.
