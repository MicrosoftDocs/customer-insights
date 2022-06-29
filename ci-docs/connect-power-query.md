---
title: "Connect to a Power Query data source (contains video)"
description: "Ingest data through a Power Query connector (contains video)."
ms.date: 06/13/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: how-to
author: adkuppa
ms.author: matgos
manager: shellyha
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - customerInsights
---

# Connect to a Power Query data source

Power Query offers a broad set of connectors to ingest data. Most of these connectors are supported by Dynamics 365 Customer Insights.

Adding data sources based on Power Query connectors generally follows the steps outlined in this section. However, depending on the connector you use, different information is required. To learn more, see the documentation about individual connectors in the [Power Query connector reference](/power-query/connectors/).

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWN6EK]

## Create a new data source

1. Go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Select **Microsoft Power Query**.

1. Provide a **Name** and an optional **Description** for the data source, and select **Next**.

1. Choose one of the [available connectors](#available-power-query-data-sources). In this example, we select the **Text/CSV** connector.

1. Enter the required details in the **Connection settings** for the selected connector and select **Next** to see a preview of the data.

1. Select **Transform data**. In this step, you'll add entities to your data source. Entities are datasets. If you have a database that includes multiple datasets, each dataset is its own entity.

1. The **Power Query - Edit queries** dialog lets you review and refine the data. The entities that the systems identified in your selected data source appear in the left pane.

   :::image type="content" source="media/data-manager-configure-edit-queries.png" alt-text="Edit queries dialog":::

1. You can also transform your data. Select an entity to edit or transform. Use the options in the Power Query window to apply transformations. Each transformation is listed under **Applied steps**. Power Query provides numerous pre-built transformation options. For more information, see [Power Query Transformations](/power-query/power-query-what-is-power-query#transformations).

   We recommend you use the following transformations:

   - If you're ingesting data from a CSV file, the first row often contains headers. Go to **Transform** and select **Use first row as headers**.
   - Ensure the data type is set appropriately. For example, for date fields, select a date type.

1. To add additional entities to your data source in the **Edit queries** dialog, go to **Home** and select **Get data**. Repeat steps 6-10 until you have added all entities for this data source.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

### Available Power Query data sources

See the [Power Query connector reference](/power-query/connectors/) for a list of connectors that you can use to import data to Customer Insights.

Connectors with a checkmark in the **Customer Insights (Dataflows)** column are available to create new data sources based on Power Query. Review the documentation of a specific connector to learn more about its prerequisites, [query limitations](/power-query/power-query-online-limits), and other details.

## Add data from on-premises data sources

Ingesting data from on-premises data sources is supported based on Microsoft Power Platform dataflows (PPDFs). You can enable dataflows in Customer Insights by [providing the Microsoft Dataverse environment URL](create-environment.md) when setting up the environment.

Data sources that are created after associating a Dataverse environment with Customer Insights use [Power Platform dataflows](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365) by default. Dataflows support on-premises connectivity using the data gateway. You can remove and recreate data sources that existed before a Dataverse environment was associated [using on-premises data gateways](/data-integration/gateway/service-gateway-app).

Data gateways from an existing Power BI or Power Apps environment will be visible and you can reuse in Customer Insights. The data sources page shows links to go to the Microsoft Power Platform environment where you can view and configure on-premises data gateways.

> [!IMPORTANT]
> Make sure your gateways are updated to latest version. You can install an update and reconfigure a gateway from a prompt shown on the gateway screen directly or [download the latest version](https://powerapps.microsoft.com/downloads/). If you don't use the latest gateway version, the dataflow refresh fails with error messages like **The keyword isn't supported: configuration properties. Parameter name: keyword**.

## Edit Power Query data sources

> [!NOTE]
> It might not be possible to make changes to data sources that are currently being used in one of the app's processes (*segmentation*, *match*, or *merge*, for example).
>
> In the **Settings** page, you can track the progress of each of the active processes. When a process completes, you can return to the **Data Sources** page and make your changes.

1. Go to **Data** > **Data sources**.

1. Next to the data source you'd like to update, select **Edit**.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

1. Apply your changes and transformations in the **Power Query - Edit queries** dialog as described in the [Create a new data source](#create-a-new-data-source) section.

1. Select **Save** in Power Query after completing your edits to save your changes.
