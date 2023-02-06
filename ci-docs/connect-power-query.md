---
title: "Connect to a Power Query data source (contains video)"
description: "Ingest data through a Power Query connector (contains video)."
ms.date: 01/06/2023
ms.reviewer: v-wendysmith

ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
ms.custom: bap-template
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - customerInsights
---

# Connect to a Power Query data source

Power Query offers a broad set of connectors to ingest data. Most of these connectors are supported by Dynamics 365 Customer Insights. Adding data sources based on Power Query connectors generally follows the steps outlined in this section. However, depending on the connector you use, different information is required. To learn more, see the documentation about individual connectors in the [Power Query connector reference](/power-query/connectors/).

To securely connect data in a private network, Power Query supports the use of [virtual network data gateways (preview)](/data-integration/vnet/data-gateway-power-platform-dataflows).

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWN6EK]

## Create a new data source

1. Go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Select **Microsoft Power Query**.

1. Provide a **Name** and an optional **Description** for the data source, and select **Next**.

1. Choose one of the [available connectors](#available-power-query-data-sources). In this example, we select the **Text/CSV** connector.

1. Enter the required details in the **Connection settings** for the selected connector and select **Next** to see a preview of the data.

1. Select **Transform data**.

1. Review and refine your data in the **Power Query - Edit queries** page. The entities that the systems identified in your selected data source appear in the left pane.

   :::image type="content" source="media/data-manager-configure-edit-queries.png" alt-text="Edit queries dialog":::

1. Transform your data. Select an entity to edit or transform. Use the options in the Power Query window to apply transformations. Each transformation is listed under **Applied steps**. Power Query provides numerous [pre-built transformation](/power-query/power-query-what-is-power-query#transformations) options.

   > [!IMPORTANT]
   > We recommend you use the following transformations:
   >
   > - If you're ingesting data from a CSV file, the first row often contains headers. Go to **Transform** and select **Use first row as headers**.
   > - Ensure the data type is set appropriately and matches the data. For example, for date fields, select a date type.

1. To add additional entities to your data source in the **Edit queries** dialog, go to **Home** and select **Get data**. Repeat steps 5-10 until you have added all entities for this data source. If you have a database that includes multiple datasets, each dataset is its own entity.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Entities**](entities.md) page.

> [!CAUTION]
>
> - A data source based on Power Query creates a [dataflow in Dataverse](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365). Don't change the name of a dataflow in the Power Platform admin center that is used in Customer Insights. Renaming a dataflow causes issues with the references between the Customer Insights data source and the Dataverse dataflow.
> - Concurrent evaluations for Power Query data sources in Customer Insights have the same [refresh limits like Dataflows in PowerBI.com](/power-query/power-query-online-limits#refresh-limits). If a data refresh fails because it reached the evaluation limit, we recommend you adjust the refresh schedule for each dataflow to ensure the data sources aren't processed at the same time.

### Available Power Query data sources

See the [Power Query connector reference](/power-query/connectors/) for a list of connectors that you can use to import data to Customer Insights.

Connectors with a checkmark in the **Customer Insights (Dataflows)** column are available to create new data sources based on Power Query. Review the documentation of a specific connector to learn more about its prerequisites, [query limitations](/power-query/power-query-online-limits), and other details.

## Add data from on-premises data sources

Ingesting data from on-premises data sources is supported based on Microsoft Power Platform dataflows (PPDFs). You can enable dataflows in Customer Insights by [providing the Microsoft Dataverse environment URL](create-environment.md) when setting up the environment.

Data sources that are created after associating a Dataverse environment with Customer Insights use [Power Platform dataflows](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365) by default. Dataflows support on-premises connectivity using the data gateway. You can remove and recreate data sources that existed before a Dataverse environment was associated [using on-premises data gateways](/data-integration/gateway/service-gateway-app).

Data gateways from an existing Power BI or Power Apps environment will be visible and you can reuse them in Customer Insights if the data gateway and the Customer Insights environment are in the same Azure Region. The data sources page shows links to go to the Microsoft Power Platform environment where you can view and configure on-premises data gateways.

> [!IMPORTANT]
> Make sure your gateways are updated to latest version. You can install an update and reconfigure a gateway from a prompt shown on the gateway screen directly or [download the latest version](https://powerapps.microsoft.com/downloads/). If you don't use the latest gateway version, the dataflow refresh fails with error messages like **The keyword isn't supported: configuration properties. Parameter name: keyword**.
>
> Errors with on-premises data gateways in Customer Insights are often caused by configuration issues. For more information about troubleshooting data gateways, see [Troubleshoot the on-premises data gateway](/data-integration/gateway/service-gateway-tshoot).

## Edit Power Query data sources

> [!NOTE]
> It might not be possible to make changes to data sources that are currently being used in one of the app's processes (segmentation or data unification for example).
>
> In the **Settings** page, you can track the progress of each of the active processes. When a process completes, you can return to the **Data Sources** page and make your changes.

1. Go to **Data** > **Data sources**.

1. Next to the data source you'd like to update, select **Edit**.

1. Apply your changes and transformations in the **Power Query - Edit queries** dialog as described in the [Create a new data source](#create-a-new-data-source) section.

1. Select **Save** to apply your changes and return to the **Data sources** page.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Common reasons for ingestion errors or corrupt data

### Data type does not match data

The most common data type mismatch occurs when a date field is not set to the correct date format.

The data can be fixed at the source and re-ingested. Or fix the transformation within Customer Insights. To fix the transformation:

1. Go to **Data** > **Data sources**.

1. Next to the data source with the corrupted data, select **Edit**.

1. Select **Next**.

1. Select each of the queries and look for transformations applied inside "Applied Steps" that are incorrect, or date columns that have not been transformed with a date format.

   :::image type="content" source="media/PQ_corruped_date.png" alt-text="Power Query - Edit showing incorrect date format":::

1. Change the data type to correctly match the data.

1. Select **Save**. That data source is refreshed.

> [!TIP]
> For troubleshooting information, go to [Microsoft Dynamics 365 Customer Insights troubleshooting](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights).


[!INCLUDE [footer-include](includes/footer-banner.md)]
