---
title: "Connect to a Power Query data source"
description: "Ingest data through a Power Query connector."
ms.date: 04/29/2025
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom:
  - bap-template
  - sfi-image-nochange
---

# Connect to a Power Query data source

[Power Query](/power-query/power-query-what-is-power-query) offers various connectors to ingest data, most of which Dynamics 365 Customer Insights supports. In the [Power Query connector reference](/power-query/connectors/), connectors with a checkmark in the **Customer Insights (Dataflows)** column you can use to import data to Customer Insights - Data. Review the documentation of a specific connector to learn more about its prerequisites, [query limitations](/power-query/power-query-online-limits), and other details.

Power Query has data size and performance limitations. It makes copies of data in the Dataverse managed data lake in the CSV format so data synchronization takes longer as opposed to other data source connections.

To securely connect data in a private network, Power Query supports the use of [virtual network data gateways (preview)](/data-integration/vnet/data-gateway-power-platform-dataflows).

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=ef3f2af9-7a02-44e6-9465-5ae4bebab382]

## Create a new data source

[!INCLUDE [data-connection-names](./includes/data-connection-names.md)]

1. Go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Microsoft Power Query**.

1. Provide a **Name** and an optional **Description** for the data source, and select **Next**.

1. Choose one of the [available connectors](/power-query/connectors/). In this example, we select the **Text/CSV** connector.

1. Enter the required details in the **Connection settings** for the selected connector and select **Next** to see a preview of the data.

1. Select **Transform data**.

1. Review and refine your data in the **Power Query - Edit queries** page. The tables that the systems identified in your selected data source appear in the left pane.

   :::image type="content" source="media/data-manager-configure-edit-queries.png" alt-text="Edit queries dialog":::

1. Transform your data. Select a table to edit or transform. To apply transformations, use the options in the Power Query window. Each transformation is listed under **Applied steps**. Power Query provides numerous [prebuilt transformation](/power-query/power-query-what-is-power-query#transformations) options.

   > [!IMPORTANT]
   > We recommend you use the following transformations:
   >
   > - If you're ingesting data from a CSV file, the first row often contains headers. Go to **Transform** and select **Use first row as headers**.
   > - Ensure the data type is set appropriately and matches the data. For example, for date fields, select a date type.

1. To add more tables to your data source in the **Edit queries** dialog, go to **Home** and select **Get data**. Repeat steps 5-10 until you add all tables for this data source. If you have a database that includes multiple datasets, each dataset is its own table.

1. Select whether you want to refresh the data source manually or automatically. To refresh automatically, set the time frame. 

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Data** > **Tables**](tables.md) page.

> [!CAUTION]
>
> - A data source based on Power Query creates a [dataflow in Dataverse](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365). Don't change the name of a dataflow in the Power Platform admin center that's used in Customer Insights - Data. Renaming a dataflow causes issues with the references between the data source and the Dataverse dataflow.
> - Concurrent evaluations for Power Query data sources in Customer Insights - Data have the same [refresh limits like Dataflows in PowerBI.com](/power-query/power-query-online-limits#refresh-limits). If a data refresh fails because it reached the evaluation limit, we recommend you adjust the refresh schedule for each dataflow to ensure the data sources aren't processed at the same time.

## Add data from on-premises data sources

Ingesting data from on-premises data sources is supported based on Microsoft Power Platform dataflows (PPDFs). You can enable dataflows in Customer Insights - Data by [providing the Microsoft Dataverse environment URL](create-environment.md) when setting up the environment.

Data sources that are created after associating a Dataverse environment with Customer Insights - Data use [Power Platform dataflows](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365) by default. [Dataflows support on-premises connectivity using the data gateway](/data-integration/gateway/service-gateway-onprem-indepth). You can remove and recreate data sources that existed before a Dataverse environment was associated [using on-premises data gateways](/data-integration/gateway/service-gateway-app).

Data gateways from an existing Power BI or Power Apps environment are visible and you can reuse them in Customer Insights if the data gateway and the Customer Insights environment are in the same Azure Region. The data sources page shows links to go to the Microsoft Power Platform environment where you can view and configure on-premises data gateways.

### Best practices and troubleshooting

Because an on-premises data gateway is in organization's network, Microsoft can't check its health. The following recommendations can help address gateway timeouts when importing data to Customer Insights:

- [Monitor and optimize on-premises data gateway performance](/data-integration/gateway/service-gateway-performance) and follow the [on-premises data gateway sizing guide](/power-bi/guidance/gateway-onprem-sizing).

- [Separate the ingestion and transformation dataflow](/power-query/dataflows/best-practices-developing-complex-dataflows#split-data-transformation-dataflows-from-stagingextraction-dataflows). Separation of dataflows for ingestion and transformation is helpful when dealing with multiple queries of slower data sources in one dataflow or multiple dataflows querying the same data sources.

- [Separate the entities into multiple dataflows](/power-query/dataflows/best-practices-reusing-dataflows#separate-entities-in-multiple-dataflows).

- [Choose the right connector and filter early](/power-query/best-practices?source=recommendations#choose-the-right-connector).

- Make sure all on-premises data gateway nodes are healthy and configured at decent network latency between the nodes and data source for SQL instances.

- Use a scalable data gateway cluster if you expect heavy data requests.

- Ensure the data source is scaled out appropriately and the resource utilization on the source isn't abnormally high.  

- Consider partitioning large tables into smaller tables.

- Consider hosting the data source and data gateway in the same geographical region.

- Optimize the data source query and indexes. Properly indexed and partitioned data can be accessed more quickly and efficiently, leading to better query and dataflow performance.

> [!IMPORTANT]
> Update your gateways to the latest version. You can install an update and reconfigure a gateway from a prompt shown on the gateway screen directly or [download the latest version](https://powerapps.microsoft.com/downloads/). If you don't use the latest gateway version, the dataflow refresh fails with error messages like **The keyword isn't supported: configuration properties. Parameter name: keyword**.
>
> Errors with on-premises data gateways are often caused by configuration issues. For more information about troubleshooting data gateways, go to [Troubleshoot the on-premises data gateway](/data-integration/gateway/service-gateway-tshoot).

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

You can transfer the data source ownership to other people in your organization. For example, if the owner leaves the organization or if changes are required for collaboration purposes. 

### Transfer the ownership

The user performing this action must have a *Dataverse Administrator* role.

1. Go to [Power Apps](https://make.powerapps.com).

1. Select the Dataverse environment that maps to your Customer Insights - Data environment.

1. Go to **Dataflows** and select **All Dataflows**.

1. Search for the owner of the dataflow that you want to take ownership.

1. Select the vertical ellipsis (&vellip;) and select **Change Owner**.

1. Enter the name of the new owner and select **Change Owner**.

## Update Power Query schedules to system refresh schedule
 
Customer Insights - Data is aligning Power Query separate refresh schedules with the system refresh schedule. To ensure that Customer Insights - Data reflects current data, remove your Power Query refresh schedules so that these data sources refresh as part of the system refresh. If your Power Query data source shows **Completed with warnings** on the **Data sources** page, your data source contains a separate refresh schedule. Remove the separate schedule. After a system refresh, the status changes to **Completed**.

> [!IMPORTANT]
> The data source refresh time is added to the total time for a system refresh. We recommend you [view your Power Query run durations](#view-power-query-run-durations) and then change the [system refresh schedule](schedule-refresh.md) if needed. For example, a Power Query source might take an average of 30 minutes to refresh. Therefore, we recommended you update the system refresh schedule to start 30 minutes earlier to receive results at a similar time.

### Remove Power Query schedules

1. Go to **Data** > **Data Sources**.

1. Select the desired Power Query data source.

1. Select the vertical ellipsis (&vellip;) and select **Edit refresh settings**.

1. Select **Refresh manually**.
   
1. Select **Save**.

### View Power Query run durations

1. Go to **Data** > **Data Sources**.

1. Select the desired Power Query data source.

1. Select **Status**. 

## Refresh Power Query data sources on demand

Power Query data sources can be refreshed on demand. 

1. Go to **Data** > **Data Sources**.

1. If you are the data source owner, find the data source under **Managed by me**. Otherwise, find it under **Managed by others**.

1. Select the desired Power Query data source, and then select **Refresh**.

## Next steps

- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
