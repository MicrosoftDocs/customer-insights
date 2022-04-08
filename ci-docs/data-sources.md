---
title: "Use data sources to ingest data"
description: "Learn how to import data from various sources."
ms.date: 03/18/2022

ms.subservice: audience-insights
ms.topic: overview
author: adkuppa
ms.author: adkuppa
ms.reviewer: mhart
manager: shellyha
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - customerInsights
---

# Data sources overview



Dynamics 365 Customer Insights connects to data from a broad set of sources. Connecting to a data source is often referred to as the process of *data ingestion*. After ingesting the data, you can [unify](data-unification.md) and take action on it.

## Add a data source

Refer to the detailed articles for how to add a data source, depending on the option you choose.

You can add the following data sources:

- [Through dozens of Power Query connectors](connect-power-query.md)
- [From a Common Data Model folder](connect-common-data-model.md)
- [From your own Microsoft Dataverse lake](connect-dataverse-managed-lake.md)
- [From an Azure Synapse Analytics database](connect-synapse.md)

> [!NOTE]
> If you're using the trial version, the import methods section includes a **Customer Insights data library** option. Choose this option to select a sample dataset available for various industries. For more information, see [Dynamics 365 Customer Insights trial](../trial-signup.md).

## Add data from on-premises data sources

Ingesting data from on-premises data sources is supported based on Microsoft Power Platform dataflows. You can enable Dataflows in Customer Insights by [providing the Microsoft Dataverse environment URL](create-environment.md) when setting up the environment.

Data sources that are created after associating a Dataverse environment with Customer Insights use [Power Platform dataflows](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365) by default. Dataflows support on-premises connectivity using the data gateway. You can remove and recreate data sources that existed before a Dataverse environment was associated [using on-premises data gateways](/data-integration/gateway/service-gateway-app).

Data gateways from an existing Power BI or Power Apps environment will be visible and you can reuse in Customer Insights. The data sources page shows links to go to the Microsoft Power Platform environment where you can view and configure on-premises data gateways.

> [!IMPORTANT]
> Make sure your gateways are updated to latest version. You can install an update and reconfigure a gateway from a prompt shown on the gateway screen directly or [download the latest version](https://powerapps.microsoft.com/downloads/). If you don't use the latest gateway version, the dataflow refresh fails with error messages like **The keyword isn't supported: configuration properties. Parameter name: keyword**.

## Review ingested data
If your environment contains Power Platform dataflows, the **Data Sources** page lists three sections: 
- **Shared**: Data sources that can be managed by all Customer Insights admins. Power BI dataflows,  your own storage account, and attaching to a Dataverse-managed data lake are examples of shared data sources.
- **Managed by me**: Power Platform dataflows created and can be managed only by you. Other Customer Insights admins can only view these dataflows but not edit, refresh, or delete them.
- **Managed by others**: Power Platform dataflows created by other admins. You can only view them. It lists the owner of the dataflow to reach out to for any assistance.
> [!NOTE]
> All entities can be viewed and used by other users. User contextuality applies only to the data sources and not to the entities that result from these dataflows.

If no Power Platform dataflows are used, you won't see any groups or sections. The **Data Sources** page contains only a list of all data sources.

You'll see the name of each ingested data source, its status, and the last time the data was refreshed for that source. You can sort the list of data sources by every column.

> [!div class="mx-imgBorder"]
> ![Data source added.](media/configure-data-datasource-added.png "Data source added")

[!INCLUDE [progress-details-include](../includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the **Entities** page. For more information, see [Entities](entities.md).

## Refresh a data source

Data sources can be refreshed on an automatic schedule or refreshed manually on demand. 

Go to **Admin** > **System** > [**Schedule**](system.md#schedule-tab) to configure scheduled refreshes of all your ingested data sources.

To refresh a data source on demand, follow these steps:

1. Go to **Data** > **Data sources**.

2. Select the vertical ellipsis next to the data source you want to refresh and select **Refresh** from the dropdown list.

3. The data source is now triggered for a manual refresh. Refreshing a data source will update both the entity schema and data for all the entities specified in the data source.

4. Select **Stop refreshing** if you want to cancel an existing refresh and the data source will revert to its last refresh status.

## Delete a data source

1. Go to **Data** > **Data sources**.

2. Select the vertical ellipsis next to the data source you want to remove and select **Delete** from the dropdown menu.

3. Confirm your deletion.


[!INCLUDE[footer-include](includes/footer-banner.md)]
