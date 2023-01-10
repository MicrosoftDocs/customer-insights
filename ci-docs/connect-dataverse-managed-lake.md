---
title: "Connect to data in a Microsoft Dataverse managed data lake"
description: "Import data from a Microsoft Dataverse managed data lake."
ms.date: 01/03/2023
ms.subservice: audience-insights
ms.topic: how-to
author: adkuppa
ms.author: adkuppa
manager: shellyha
ms.reviewer: v-wendysmith
searchScope: 
  - ci-dataverse
  - customerInsights
---

# Connect to data in a Microsoft Dataverse managed data lake

Microsoft Dataverse users can quickly connect to analytical tables in a Microsoft Dataverse managed lake. 
Only one data source of an environment can simultaneously use the same Dataverse managed lake.

> [!NOTE]
> You must be an admin on the Dataverse organization to proceed and view the list of tables available in the managed lake.

## Prerequisites

- Data stored in online services, such as Azure Data Lake Storage, may be stored in a different location than where data is processed or stored in Dynamics 365 Customer Insights. By importing or connecting to data stored in online services, you agree that data can be transferred to and stored with Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- Only Dataverse tables with [change tracking](/power-platform/admin/enable-change-tracking-control-data-synchronization) enabled are visible. These tables can be exported to the Dataverse-managed data lake and used in Customer Insights. Out-of-box Dataverse tables have change tracking enabled by default. You need to turn change tracking on for custom tables. To check if a Dataverse table is enabled for change tracking, go to [Power Apps](https://make.powerapps.com) > **Data** > **Tables**. Find the table of your interest and select it. Go to **Settings** > **Advanced options** and review the **Track changes** setting.

## Connect to a Dataverse managed lake

1. Go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Select **Microsoft Dataverse**.

1. Enter a **Name** for the data source and an optional **Description**.

1. Provide the **Server address** for the Dataverse organization, and select **Sign in**.

1. Select the tables you want to ingest to Customer Insights from the available list.

   > [!NOTE]
   > If some tables are already selected, they might be used by other Dynamics 365 applications (such as Dynamics 365 Sales Insights or Customer Service Insights). You can't change the selection. These tables will be available once the data source is created.

    :::image type="content" source="media/select-dataverse-entities.png" alt-text="Dialog box showing a list of tables in the Dataverse environment.":::

1. Save your selection to start syncing the selected tables from Dataverse. You'll find the newly added connection on the **Data sources** page. It will be queued for refresh and show the table count as 0 until all the selected tables are synced.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Data** > **Tables**](tables.md) page.

## Edit a Dataverse managed lake data source

You only edit the table selection after creating the data source. For example, if additional tables were added to Dataverse and you want to import them too.
To connect to a different Dataverse data lake, [create a new data source](#connect-to-a-dataverse-managed-lake).

1. Go to **Data** > **Data sources**.

1. Next to the data source you'd like to update, select **Edit**.

1. Select additional tables from the available list of tables.

1. Click **Save** to apply your changes and return to the **Data sources** page.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]


[!INCLUDE [footer-include](includes/footer-banner.md)]
