---
title: "Connect to data in Microsoft Dataverse"
description: "Attach data from a Microsoft Dataverse to Customer Insights - Data."
ms.date: 12/02/2025
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Connect to data in Microsoft Dataverse

Microsoft Dataverse users can quickly connect to analytical tables in Dataverse. Only one data source of an environment can simultaneously use the same Dataverse environment.
Because your Dataverse tables are ingested into Customer Insights - Data in Delta format, you can take advantage of the benefits Delta format has to offer.

## Prerequisites

- Data stored in online services, such as Azure Data Lake Storage, might be stored in a different location than where data is processed or stored in Dynamics 365 Customer Insights. By importing or connecting to data stored in online services, you agree that data can be transferred to and stored with Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- Only Dataverse tables with [change tracking](/power-platform/admin/enable-change-tracking-control-data-synchronization) enabled are visible. Out-of-box Dataverse tables have change tracking enabled by default. You need to turn on change tracking for custom tables. To check if a Dataverse table is enabled for change tracking, go to [Power Apps](https://make.powerapps.com) > **Data** > **Tables**. Find the table of your interest and select it. Go to **Settings** > **Advanced options** and review the **Track changes** setting.

- You must be an admin on the Dataverse organization to proceed and view the list of tables.

## Connect to Dataverse

1. Go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Microsoft Dataverse**.

    :::image type="content" source="media/data-source-dataverse.svg" alt-text="Screenshot of adding a Microsoft Dataverse data source.":::

1. Enter a **Name** for the data source and an optional **Description**.

1. Provide the **Server address** for the Dataverse organization, and select **Sign in**.

1. Select the tables you want to import from the list.

   <!--- 
    :::image type="content" source="media/select-dataverse-tables.png" alt-text="Dialog box showing a list of tables in the Dataverse environment.":::
   --->

1. Save your selection to start syncing the selected tables from Dataverse. You find the newly added connection on the **Data sources** page. It's queued for refresh and show the table count as 0 until all the selected tables are synced.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Data** > **Tables**](tables.md) page.

## Edit a Dataverse data source

You only edit the table selection after creating the data source. For example, if tables were added to Dataverse and you want to import them too.
To connect to a different Dataverse environment, [create a new data source](#connect-to-dataverse).

1. Go to **Data** > **Data sources**. Next to the data source you'd like to update, select **Edit**.

1. Select the tables from the available list of tables.

1. Select **Save** to apply your changes and return to the **Data sources** page.

> [!TIP] 
> We recommend scheduling regular refreshes of your Dataverse data source (for example, daily or every other day). You should immediately trigger downstream tasks after ingestion completes; scheduled refreshes are often the most convenient way to do this. This ensures that downstream processes (such as match and merge) always operate on the most up-to-date data.

## Next steps

- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
