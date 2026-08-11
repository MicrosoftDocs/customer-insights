---
title: Connect to Microsoft Fabric OneLake
description: Connect to Delta tables in a Microsoft Fabric OneLake Lakehouse and ingest the data into Dynamics 365 Customer Insights - Data.
ms.date: 08/05/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Connect to Microsoft Fabric OneLake

Connect Customer Insights - Data directly to your Microsoft Fabric OneLake lakehouse to ingest data. The Fabric OneLake connector reads Delta tables directly from your Fabric workspace, so you don't need to copy or stage data in Azure Data Lake.

## Supported capabilities

The Fabric OneLake connector supports:

- Ingestion of managed **Delta tables** from Fabric lakehouses.
- Use of **Fabric shortcuts** to provide access to Delta tables outside the target workspace.

## Prerequisites

Before you create a Fabric OneLake data source:

- [Enable external access to the OneLake data](#enable-external-access-to-onelake-data).
- [Add Customer Insights - Data service principal to the Fabric workspace](#add-customer-insights---data-service-principal-to-the-fabric-workspace).
- [Create private links](connect-fabric-inbound-access-protection.md) if **Inbound Access Protection** is enabled. To check if **Inbound Access Protection** is enabled in your tenant, sign in to the Microsoft Fabric admin portal. Go to **Admin Portal** > **Tenant Settings** > **Advanced Networking**. Check if **Azure Private Links** and **Block Public Internet Access** are enabled.
- Verify that the following workspace and data requirements are met.

### Workspace prerequisites

- A Microsoft Fabric workspace with Delta tables exists in the same Microsoft Entra tenant used by Customer Insights - Data.
- The admin who creates or updates the data source needs at least the **Viewer** workspace role.

### Data prerequisites

- Tables must have a primary key column with unique, non-null values. String, integer, and GUID data types are supported as primary keys.
- Tables must be in the Delta format.
- Tables must be limited to Delta features that require `minReaderVersion` 1 or 2. For more information, see [Supported Databricks features](connect-delta-lake.md#supported-databricks-features-and-versions).

## Limitations

This feature has the following limitations:

- Files or tables that aren't in **Delta format** (for example, CSV or non-Delta Parquet) aren't supported.
- Only **one Fabric OneLake data source per workspace**. To ingest data from another workspace, create another data source or use a Fabric shortcut to expose the remote table in the workspace.
- Fabric **Data Warehouse** tables aren't supported.
- Tables configured with Delta features that require `minReaderVersion` greater than 2, such as deletion vectors aren't supported. For more information, see [Supported Databricks features](connect-delta-lake.md#supported-databricks-features-and-versions).
- The option to **upgrade in place** an existing Azure Data Lake Delta tables data source to a Fabric OneLake data source will be released by October 2026.


## Enable external access to OneLake data

A Fabric tenant administrator must enable external access to OneLake data *once* for the Fabric tenant. This setting allows services such as Customer Insights - Data to read Delta tables from your Fabric lakehouses.

1. Sign in to the [Fabric admin portal](https://app.fabric.microsoft.com/admin-portal) as a Fabric administrator.
1. Select **Tenant settings**.
1. Under **OneLake settings**, expand **Users can access data stored in OneLake with apps external to Fabric**.
1. Ensure the toggle is set to **Enabled** and apply it to the organization or to specific security groups, as required by your tenant policy. Tenant settings changes can take up to 15 minutes to take effect.

## Add Customer Insights - Data service principal to the Fabric workspace

Add the Customer Insights - Data service principal (**Dynamics 365 AI for Customer Insights**) to the Fabric workspace with at least the **Contributor** role so it can read Delta tables at runtime and write a small amount of metadata for each table. As a best practice, put the service principal in a security group.

### Enable the service principal in the Fabric tenant

1. Sign in to the [Fabric admin portal](https://app.fabric.microsoft.com/admin-portal) as a Fabric administrator.
1. Select **Tenant settings**. Scroll to **Developer settings**.
1. Enable **Service principals can call Fabric public APIs**.

### Add the service principal or security group to the Fabric workspace

1. Open your Fabric workspace.
1. Select **Manage access**.
1. Select **Add people or groups**.
1. Search for the service principal name or the security group that contains it.
1. Assign the **Contributor** role.

## Connect to data in Fabric OneLake

Data source names and table names must start with a letter and can contain only letters, numbers, and special characters. 

1. In Customer Insights - Data, go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Microsoft Fabric OneLake**.

1. Enter the following information:

   - **Data source name** – A unique name to identify the data source in Customer Insights - Data. You can't change the data source name after you save it.
   - **Description** *(optional)* – A short description of the data the source contains.
   - **Workspace** – The Fabric workspace that contains the Delta tables to ingest.
   - **Enable Private Link** – If the workspace is protected by Fabric inbound access protection, check **Enable Private Link** to connect by using an Azure Private Link. For more information, see [Connect to a Microsoft Fabric workspace with inbound access protection enabled](connect-fabric-inbound-access-protection.md).

   :::image type="content" source="media/onelake-add-data-source.png" alt-text="Screenshot of the Add a data source pane with Fabric OneLake selected." lightbox="media/onelake-add-data-source.png":::

1. Select **Next**. Customer Insights - Data lists every Delta table it finds across the lakehouses in the selected workspace. Table names use the pattern `<lakehouse>_Lakehouse_<schema>_<table>`.

1. Select **Include** for each table you want to ingest.

   :::image type="content" source="media/onelake-add-delta-tables.png" alt-text="Screenshot of the Add Fabric Delta tables page listing tables from lakehouses with two tables selected.":::

   > [!TIP]
   > If no tables are listed, ensure you completed the prerequisites to provide Customer Insights - Data. If tables are shown and a specific table isn't listed, confirm the table is a managed Delta table in a Fabric lakehouse and that the workspace contains it. Tables stored in a Fabric Data Warehouse aren't listed as these tables are exposed as SQL tables.

1. For each selected table where a primary key isn't automatically detected, **Required** appears under **Primary key**. For each of these tables:

   1. Select **Required**. The **Edit table** panel opens.
   1. Choose the **Primary key** column. The primary key must be unique and can't contain null or missing values.
   1. Select **Close** to save and close the panel.

1. To enable [data profiling](data-sources.md#data-profiling) on a table, select the number under **Columns** for that table. The **Manage attributes** page opens.

   :::image type="content" source="media/onelake-manage-attributes.png" alt-text="Screenshot of the Manage attributes page showing columns, data formats, and data profiling checkboxes.":::

   1. Review the **Name** and **Data format** for each column.
   1. Select **Data profiling** for the whole table or for individual columns. By default, data profiling is off.
   1. Select **Done**.

1. Select **Next**, review the summary, and then select **Save**.

The **Data sources** page opens and shows the new data source in **Refreshing** status.-

Loading data can take time while tables are read and metadata is created. After a successful refresh, you can review the ingested data on the [**Tables**](tables.md) page. Data ingested to Customer Insights - Data is transferred and processed in the geographic location of the Customer Insights - Data environment. For more information, see the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Edit a Fabric OneLake data source

You can edit a data source connection to add tables and remove tables if no downstream dependencies on the table exist. You can't change the data source name or workspace.

1. Go to **Data** > **Data sources**. Next to the data source you want to update, select  **Edit**.

1. Change any of the following information:

   - **Description**
   - **Enable Private Link** – To ingest data from a storage account through an Azure Private Link, see [Connect to a Microsoft Fabric workspace with inbound access protection enabled](connect-fabric-inbound-access-protection.md).

1. Select **Next**.

1. Select **Include** for each table you want to ingest.

1. For each selected table where a primary key isn't detected, **Required** appears under **Primary key**. For each of these tables:

   1. Select **Required**. The **Edit table** panel opens.
   1. Choose the **Primary key**. The primary key must be unique and can't contain null or missing values.
   1. Select **Close** to save and close the panel.

1. To enable [data profiling](data-sources.md#data-profiling) on a table, select the number under **Columns** for that table. The **Manage attributes** page opens.

   :::image type="content" source="media/onelake-manage-attributes.png" alt-text="Screenshot of the Manage attributes page showing columns, data formats, and data profiling checkboxes.":::

   1. Review the **Name** and **Data format** for each column.
   1. Select **Data profiling** for the whole table or for individual columns. By default, data profiling is off.
   1. Select **Done**.

1. Select **Next**, review the summary, and then select **Save**.

## Manage schema changes

If you change the schema of a table that Customer Insights - Data is configured to ingest, the change typically causes a data refresh failure. To update the schema for the connection, see [Manage schema changes](connect-delta-lake.md#manage-schema-changes).

## Delta logs and data refreshes

Customer Insights - Data uses Delta logs when ingesting data and requires all log versions since the previous refresh. To avoid refresh failures due to missing Delta logs:

- Maintain a longer Delta log version history than your longest refresh cadence. For example, if a development instance only refreshes data every two weeks, maintain at least three weeks of version history.
- In your Fabric lakehouse, set both `delta.logRetentionDuration` and `delta.deletedFileRetentionDuration` to an appropriate value.
- Avoid aggressive `VACUUM` operations against tables that Customer Insights - Data ingests.

If Delta log versions are missing (for example, after an aggressive `VACUUM` operation), manually run a full refresh on the table. To learn more, see [Manually run a full refresh on a Delta table](connect-delta-lake.md#manually-run-a-full-data-refresh-on-a-delta-table-folder).

## Common issue

### The Add Fabric Delta tables page appears unresponsive and no tables are shown

Customer Insights - Data can't read the list of tables in the workspace. One or more of the following situations can cause this issue:

- External access to OneLake data wasn't enabled for the Fabric tenant. [Enable external access](#enable-external-access-to-onelake-data).
- The Customer Insights - Data service principal wasn't added to the Fabric workspace. [Add Customer Insights - Data service principal to the Fabric workspace](#add-customer-insights---data-service-principal-to-the-fabric-workspace).
- The workspace is protected by Fabric inbound access protection, and you must create and use private links to connect to the workspace.

## Related information

- [Data sources overview](data-sources.md)
- [Connect to Delta tables in Azure Data Lake Storage](connect-delta-lake.md)
- [Microsoft Fabric OneLake overview](/fabric/onelake/onelake-overview)
- [Create OneLake shortcuts](/fabric/onelake/onelake-shortcuts)

[!INCLUDE [footer-include](includes/footer-banner.md)]
