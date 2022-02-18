---
title: "Connect to data in Databricks delta lake"
description: "Work with data in Databricks delta lake"
ms.date: 02/14/2022
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: v-wendysmith
ms.author: matgos
ms.reviewer: mhart
manager: shellyha
---

# Connect to data in Databricks delta lake

This article provides information on how to ingest data from Databricks delta lake.

## Connect to Databricks delta lake

1. In audience insights, go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Select **Databricks delta lake**.

   :::image type="content" source="media/data_sources_deltalake.png" alt-text="Dialog box to enter connection details for Databricks delta lake.":::
   
1.  Enter a **Name** for the data source and an optional **Description**.

1. Choose your preferred option for **Connect your storage using**. For a resource or a subscription-based option for authentication, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

   -  **Azure resource**: Enter the **Resource Id**.
   -  **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**.
   -  **Account key**: Enter the **Account name** and **Account key**.

1. Enter the name of the **Container** that contains the delta lake folder to import data from.
 
1. Choose the **Connection to Azure Synapse** and **Spark pool**, and select **Next**.

1. Navigate to the delta lake folder that contains the list of entities and select it. A list of available entities displays.  

   :::image type="content" source="media/deltalake_select_entities.png" alt-text="Dialog box to select entities":::
  
1. Select the entities you want to include.

   :::image type="content" source="media/deltalake_required.png" alt-text="Dialog box showing selected entities requiring a Primary Key":::

1. For selected entities where a primary key has not been defined, **Required** displays under **Primary key**. For each of these entities:
   1. Select **Required**. The **Edit entity** panel displays. 
   1. Choose the **Primary key**. 
   1. Select **X** to save and close the panel.

1. To enable analytics and other capabilities, select **Attributes**. The Manage attributes page displays. Select **Data profiling** for the whole entity or for specific attributes and then select **Done**. By default, no entity is enabled for data profiling.

1. Select **Save**. The **Data sources** page opens showing the new data source.

## Edit a Deltabricks delta lake storage data source

1. In audience insights, go to **Data** > **Data sources**.

1. Next to the data source you'd like to update, select the ellipsis.

1. Select the **Edit** option from the list.

   :::image type="content" source="media/data_sources_edit_deltalake.png" alt-text="Dialog box to edit delta lake storage":::
   
1. Optionally, change the description. You can't change the connection information.

1. Select **Next**.

1. Optionally, you can select additional entities to ingest. You can also remove any already selected entities if there are no dependencies.

1. Optionally, you can select additional attributes or entities to enable data profiling on or disable already selected ones.
 
1. Click **Save** to apply your changes and return to the Data Sources page.
