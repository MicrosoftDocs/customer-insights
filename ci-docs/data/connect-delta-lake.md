---
title: "Connect data stored in Delta Lake format from your Azure Data Lake Storage"
description: "Work with data stored in Delta Lake format from Azure Data Lake Storage."
ms.date: 09/19/2023
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Connect data stored in Delta Lake format from your Azure Data Lake Storage (preview)

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

[!INCLUDE [public-preview-banner](./includes/public-preview-banner.md)]

Ingest data that is already prepared and stored in your lake houses into Dynamics 365 Customer Insights - Data quickly and seamlessly using Delta Lake. Key benefits include:

- Direct integration with stored data in delta lake format. No need for intermediate staging data copies in .parquet format or additional transforms.
- Faster insights due to processing data that has last changed rather than the full data set.
- Efficient and scalable way of handling and processing data in real time.

[!INCLUDE [public-preview-banner](./includes/public-preview-note.md)]

## Prerequisites

- Data stored in online services may be stored in a different location than where data is processed or stored. By importing or connecting to data stored in online services, you agree that data can be transferred. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- The Customer Insights - Data service principal must have Storage Blob Data Contributor to access the storage account. For more information, see [Grant permissions to the service principal to access the storage account](connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).

- The user that sets up the data source connection needs at least Storage Blob Data Reader permissions on the Azure Data Lake Storage account.

- Data in your Data Lake Storage must be in delta format.

- The delta table can't be in the container root directory.

## Connect to Delta Lake data from Azure Data Lake Storage

1. Go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Delta Lake (Preview)**.

   :::image type="content" source="media/delta-lake-new.png" alt-text="Dialog box to enter connection details for Delta Lake." lightbox="media/Delta-lake-new.png":::

1. Enter a **Data source name** and an optional **Description**. The name is referenced in downstream processes and it's not possible to change it after creating the data source.

1. Choose one of the following options for **Connect your storage using**.

   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**. Optionally, if you want to ingest data from a storage account through an Azure Private Link, select **Enable Private Link**. For more information, see [Private Links](private-link.md).
   - **Azure resource**: Enter the **Resource Id**. Optionally, if you want to ingest data from a storage account through an Azure Private Link, select **Enable Private Link**. For more information, see [Private Links](private-link.md).

1. Choose the name of the **Container** that contains the folder of your data, and select **Next**.

1. Navigate to the folder that contains the data in delta lake format and select it. Then, select **Next**. A list of available tables displays.

   :::image type="content" source="media/delta-review-tables.png" alt-text="Dialog box of a list of tables to select":::

1. Select the tables you want to include. To add tables, select **New table** and enter the required information.

1. For each included table:
   1. Select **Required**. The **Edit table** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the table. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Select **Close** to save and close the panel.

1. Select the number of **Columns** for each included table. The **Manage attributes** page displays.

   :::image type="content" source="media/delta-dataprofiling-columns.png" alt-text="Dialog box to select data profiling.":::

   1. Create new columns, edit, or delete existing columns. You can change the name, the data format, or add a semantic type.
   1. To enable analytics and other capabilities, select **Data profiling** for the whole table or for specific columns. By default, no table is enabled for data profiling.
   1. Select **Done**.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Tables**](tables.md) page.
