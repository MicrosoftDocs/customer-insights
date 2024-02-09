---
title: "Connect to a Power Query data source (contains video)"
description: "Ingest data through a Power Query connector (contains video)."
ms.date: 01/22/2024
ms.reviewer: v-wendysmith
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.custom: bap-template
---

# Connect to a Power Query data source

[Power Query](/power-query/power-query-what-is-power-query) offers a variety of connectors to ingest data, most of which are supported by Dynamics 365 Customer Insights. In the [Power Query connector reference](/power-query/connectors/), connectors with a checkmark in the **Customer Insights (Dataflows)** column you can use to import data to Customer Insights - Data. Review the documentation of a specific connector to learn more about its prerequisites, [query limitations](/power-query/power-query-online-limits), and other details.

To securely connect data in a private network, Power Query supports the use of [virtual network data gateways (preview)](/data-integration/vnet/data-gateway-power-platform-dataflows).

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWN6EK]

## Create a new data source

1. Go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Microsoft Power Query**.

1. Provide a **Name** and an optional **Description** for the data source, and select **Next**.

1. Choose one of the [available connectors](/power-query/connectors/). In this example, we select the **Text/CSV** connector.

1. Enter the required details in the **Connection settings** for the selected connector and select **Next** to see a preview of the data.

1. Select **Transform data**.

1. Review and refine your data in the **Power Query - Edit queries** page. The tables that the systems identified in your selected data source appear in the left pane.

   :::image type="content" source="media/data-manager-configure-edit-queries.png" alt-text="Edit queries dialog":::

1. Transform your data. Select a table to edit or transform. Use the options in the Power Query window to apply transformations. Each transformation is listed under **Applied steps**. Power Query provides numerous [pre-built transformation](/power-query/power-query-what-is-power-query#transformations) options.

   > [!IMPORTANT]
   > We recommend you use the following transformations:
   >
   > - If you're ingesting data from a CSV file, the first row often contains headers. Go to **Transform** and select **Use first row as headers**.
   > - Ensure the data type is set appropriately and matches the data. For example, for date fields, select a date type.

1. To add additional tables to your data source in the **Edit queries** dialog, go to **Home** and select **Get data**. Repeat steps 5-10 until you have added all tables for this data source. If you have a database that includes multiple datasets, each dataset is its own table.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Data** > **Tables**](tables.md) page.

> [!CAUTION]
>
> - A data source based on Power Query creates a [dataflow in Dataverse](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365). Don't change the name of a dataflow in the Power Platform admin center that is used in Customer Insights - Data. Renaming a dataflow causes issues with the references between the data source and the Dataverse dataflow.
> - Concurrent evaluations for Power Query data sources in Customer Insights - Data have the same [refresh limits like Dataflows in PowerBI.com](/power-query/power-query-online-limits#refresh-limits). If a data refresh fails because it reached the evaluation limit, we recommend you adjust the refresh schedule for each dataflow to ensure the data sources aren't processed at the same time.

## Add data from on-premises data sources

Ingesting data from on-premises data sources is supported based on Microsoft Power Platform dataflows (PPDFs). You can enable dataflows in Customer Insights - Data by [providing the Microsoft Dataverse environment URL](create-environment.md) when setting up the environment.

Data sources that are created after associating a Dataverse environment with Customer Insights - Data use [Power Platform dataflows](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365) by default. Dataflows support on-premises connectivity using the data gateway. You can remove and recreate data sources that existed before a Dataverse environment was associated [using on-premises data gateways](/data-integration/gateway/service-gateway-app).

Data gateways from an existing Power BI or Power Apps environment will be visible and you can reuse them in Customer Insights if the data gateway and the Customer Insights environment are in the same Azure Region. The data sources page shows links to go to the Microsoft Power Platform environment where you can view and configure on-premises data gateways.

> [!IMPORTANT]
> Make sure your gateways are updated to latest version. You can install an update and reconfigure a gateway from a prompt shown on the gateway screen directly or [download the latest version](https://powerapps.microsoft.com/downloads/). If you don't use the latest gateway version, the dataflow refresh fails with error messages like **The keyword isn't supported: configuration properties. Parameter name: keyword**.
>
> Errors with on-premises data gateways are often caused by configuration issues. For more information about troubleshooting data gateways, see [Troubleshoot the on-premises data gateway](/data-integration/gateway/service-gateway-tshoot).

## Edit Power Query data sources

You must be the owner of the dataflow to edit it.

> [!NOTE]
> It might not be possible to make changes to data sources that are currently being used in one of the app's processes (segmentation or data unification for example).
>
> In the **Settings** page, you can track the progress of each of the active processes. When a process completes, you can return to the **Data Sources** page and make your changes.

1. Go to **Data** > **Data sources**. Next to the data source you'd like to update, select **Edit**.

1. Apply your changes and transformations in the **Power Query - Edit queries** dialog as described in the [Create a new data source](#create-a-new-data-source) section.

1. Select **Save** to apply your changes and return to the **Data sources** page.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, review the ingested data from the [**Data** > **Tables**](tables.md) page.

## Transfer Power Query data source ownership

You can transfer the data source ownership to other people in your organization. For example, if the owner leaves the organization or if changes are required for collaboration purposes 

### Transfer the ownership,

The user performing this action must have a *Dataverse Administrator* role.

1. Go to [Power Apps](https://make.powerapps.com).

1. Select the Dataverse environment that maps to your Customer Insights environment.

1. Go to **Dataflows** and select **All Dataflows**.

1. Search for the owner of the dataflow which you want to take ownership.

1. Select the ellipsis &vellip; and select **Change Owner**.

1. Enter the name of the new owner and select **Change Owner**.

## Migrate Power Query Schedules to system refresh schedule
 
Customer Insights is retiring separate refresh schedules. 

Removing your Power Query refresh schedule ensures that Customer insights - Data reflects current data. Refreshing Power Query data sources as a part of the system refresh will ensure that the data source refresh will be fully complete before the system refresh starts.  

### Which Power Query sources are affected?
An indication of a Power Query data source needing migration is a refresh status of “Completed with warnings” on the Data Sources homepage.  After migration and a refresh, this status should change to “Completed”.

> [!IMPORTANT]
> This migration will add the refresh time to the total time for a system refresh. It is recommended to revisit the system refresh schedule to make sure this works for your solution. For example, a Power Query source may take on average 30 minutes to refresh. It would be ideal to update the system refresh to start 30 minutes earlier when results are needed 8 hours after the origninal system refresh. 

### Remove Power Query Schudule

1. Go to [**Data > Data Sources**] (#data-sources-manage.md).

2. Select the desired Power Query data source.

3.  Select the ellipsis &vellip; and select **Edit refresh settings**.

4. Select **Refresh manually**.

5. Click **Save** to keep your changes.


## Next steps

- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
