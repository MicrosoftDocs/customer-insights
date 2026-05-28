---
title: "Connect to Microsoft Fabric OneLake (preview)"
description: "Connect to Delta tables in a Microsoft Fabric OneLake lakehouse and ingest the data into Dynamics 365 Customer Insights - Data."
ms.date: 05/26/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom:
  - bap-template
---

# Connect to Microsoft Fabric OneLake (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Connect to managed Delta tables in a Microsoft Fabric OneLake lakehouse and ingest the data into Dynamics 365 Customer Insights - Data. The Fabric OneLake connector reads Delta tables directly from your Fabric workspace, so you don't need to copy or stage data in Azure Data Lake Storage first.

Key reasons to connect to data stored in Fabric OneLake:

- Ingest Delta tables directly from a Fabric lakehouse without an intermediate storage layer.
- Reduce data movement, storage costs, and pipeline maintenance.
- Use [Fabric shortcuts](/fabric/onelake/onelake-shortcuts) to bring Delta tables from other sources or workspaces into a single lakehouse, then ingest them through one connection.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Prerequisites

Before you create a Fabric OneLake data source:

- [Enable external access to the OneLake data](#enable-external-access-to-onelake-data).
- [Add Customer Insights - Data service principal to the Fabric workspace](#add-customer-insights---data-service-principal-to-the-fabric-workspace).
- Verify that the following workspace and data requirements are met.

### Workspace prerequisites

- A Microsoft Fabric workspace that contains one or more lakehouses with the Delta tables you want to ingest. The Fabric workspace and Customer Insights - Data environment must be in the same Microsoft Entra tenant.
- The admin who creates or updates the data source needs at least the **Viewer** workspace role.

### Data prerequisites

- You can ingest **managed Delta tables** in a Fabric lakehouse. Files (such as CSV or non-Delta Parquet) and Fabric Data Warehouse tables aren't supported.
- Each Delta table must have a primary key column with unique, non-null values. String, integer, and GUID data types are supported as primary keys.
- Delta tables exposed through [Fabric shortcuts](/fabric/onelake/onelake-shortcuts) are supported.
- Customer Insights - Data supports Databricks reader version 1 or 2. Customer Insights - Data doesn't support reading Delta tables with deletion vectors enabled. Deletion vectors require the Delta reader version 3, which isn't supported. Learn more: [Supported Databricks features](connect-delta-lake.md#supported-databricks-features-and-versions).

## Preview limitations

The following limitations apply during public preview:

- **One Fabric OneLake data source per workspace**. To ingest from another workspace, create another data source or use a Fabric shortcut.
- **Editing an existing Fabric OneLake data source isn't supported**. To change the selected tables, remove the data source and create a new one. [Remove any downstream dependencies](data-unification-remove-dependencies.md) first. Editing existing connections is planned before general availability (GA).
- **Upgrade in place** from an existing Azure Data Lake Delta tables data source to a Fabric OneLake data source isn't yet available. In-place upgrade is planned before GA.
- **Private Link for Inbound Access Protection** isn't yet available for Fabric OneLake connections. Private endpoint support is planned before GA. To check if Inbound Access Protection is enabled in your tenant, sign in to the Microsoft Fabric Admin Portal. Go to **Admin Portal** > **Tenant Settings** > **Advanced Networking**. Check if **Azure Private Links** and **Block Public Internet Access** are enabled.

## Enable external access to OneLake data

A Fabric tenant administrator must enable external access to OneLake data *once* for each Fabric tenant. This setting allows the Customer Insights - Data service to read Delta tables from your Fabric lakehouses.

1. Sign in to the [Fabric Admin portal](https://app.fabric.microsoft.com/admin-portal) as a Fabric administrator.
1. Select **Tenant settings**.
1. Under **OneLake settings**, expand **Users can access data stored in OneLake with apps external to Fabric**.
1. Set the toggle to **Enabled** and apply the setting to the entire organization (or to specific security groups, as required by your tenant policy).

> [!NOTE]
> Tenant setting changes can take up to 15 minutes to take effect.

## Add Customer Insights - Data service principal to the Fabric workspace

Add the Customer Insights - Data service principal (**Dynamics 365 AI for Customer Insights**) to the Fabric workspace with at least the **Contributor** role so that it can read Delta tables at runtime and write a small amount of metadata for each table. As a best practice, put the service principal in a security group.

### Enable the service principal in the Fabric tenant

1. Sign in to the [Fabric Admin portal](https://app.fabric.microsoft.com/admin-portal) as a Fabric administrator.
1. Select **Tenant settings**. Scroll to **Developer settings**.
1. Enable **Service principals can call Fabric public APIs**.

### Add the service principal or security group to the Fabric workspace

1. Open your Fabric workspace.
1. Select **Manage access**.
1. Select **Add people or groups**.
1. Search for the service principal name or the security group that contains it.
1. Assign the **Contributor** role.

## Connect to data in Fabric OneLake

Data source names and table names must start with a letter and can only contain letters, numbers, and underscores (_). You can't use spaces or special characters. You also can't rename a data source after you save it. When you create the Fabric OneLake data source, you use the identity of the Customer Insights - Data administrator who configures it.

1. In Customer Insights - Data, go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Microsoft Fabric OneLake (Preview)**.

1. Enter the following information:

   - **Data source name** – A unique name for the data source. Downstream processes reference this name and you can't change it later.
   - **Description** *(optional)* – A short description of the data the source contains.
   - **Workspace** – The Fabric workspace that contains the lakehouse with the Delta tables you want to ingest.

   :::image type="content" source="media/onelake-add-data-source.png" alt-text="Screenshot of the Add a data source pane with Fabric OneLake (Preview) selected." lightbox="media/onelake-add-data-source.png":::

   > [!NOTE]
   > Each Fabric OneLake data source connects to a single workspace. To ingest tables from a different workspace, either create another data source for that workspace or use a Fabric shortcut to reference the tables from the connected workspace.

1. Select **Next**. Customer Insights - Data lists every Delta table it finds across the lakehouses in the selected workspace. Table names use the pattern `<lakehouse>_Lakehouse_<schema>_<table>`.

1. Select **Include** for each table you want to ingest.

   :::image type="content" source="media/onelake-add-delta-tables.png" alt-text="Screenshot of the Add Fabric Delta tables page listing tables from lakehouses with two tables selected.":::

   > [!TIP]
   > If a table doesn't appear, confirm that it's a managed Delta table in a Fabric lakehouse and that the workspace contains it. Tables stored in a Fabric Data Warehouse aren't listed.

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

The **Data sources** page opens and shows the new data source in **Refreshing** status. 

Loading data can take time. After a successful refresh, you can review the ingested data from the [**Tables**](tables.md) page. Data ingested to Customer Insights - Data transfers and processes data in the geographic location of the Customer Insights - Data environment. Learn more at the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Supported capabilities

The Fabric OneLake connector supports:

- Ingestion of managed **Delta tables** from Fabric lakehouses.
- Delta tables exposed through **Fabric shortcuts** (including shortcuts to OneLake, Azure Data Lake Storage Gen2, Amazon S3, and Google Cloud Storage).
- Incremental refresh using Delta versioning.

## Unsupported capabilities

The following capabilities aren't supported during preview:

- Fabric **Data Warehouse** tables.
- Files or tables that aren't in **Delta format** (for example, CSV or non-Delta Parquet).
- Connections to lakehouses across multiple Fabric workspaces from a single data source. Use shortcuts or create other data sources instead.

## Manage schema changes

If a column is added or removed from the schema of a Delta table, Customer Insights - Data runs a complete refresh of the data. Full refreshes take longer to process than incremental refreshes.

If the source schema changes after the data source is created, a schema mismatch error appears and asks you to update the data source. Because editing isn't supported during preview, remove and recreate the data source to pick up the new schema. In-place schema update is planned for GA.

## Delta time travel and data refreshes

Customer Insights - Data uses Delta version history when ingesting data. Customer Insights - Data needs all log versions since its last refresh. To avoid full-refresh failures caused by missing Delta versions:

- Maintain longer Delta log version history than your longest refresh cadence. For example, if a development instance only refreshes data every two weeks, maintain at least three weeks of version history.
- In your Fabric lakehouse, set both `delta.logRetentionDuration` and `delta.deletedFileRetentionDuration` to an appropriate value.
- Avoid aggressive `VACUUM` operations against tables that Customer Insights - Data ingests.

If Delta versions are missing (for example, after a `VACUUM` or after the table is recreated), recreate the data source to trigger a full refresh.

## Related information

- [Data sources overview](data-sources.md)
- [Connect to Delta tables in Azure Data Lake Storage](connect-delta-lake.md)
- [Microsoft Fabric OneLake overview](/fabric/onelake/onelake-overview)
- [Create OneLake shortcuts](/fabric/onelake/onelake-shortcuts)