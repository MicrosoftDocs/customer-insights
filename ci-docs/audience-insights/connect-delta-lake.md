---
title: "Connect to data in Databricks delta lake"
description: "Work with data in Databricks delta lake"
ms.date: 03/25/2022
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: v-wendysmith
ms.author: matgos
ms.reviewer: mhart
manager: shellyha
---

# Connect to data from Databricks delta lake

This article provides information on how to ingest data from Delta Lake on Databricks. The delta lake runs on top of an Azure data lake.

## Important considerations

- Data ingestion supports Azure Data Lake *Gen2* storage accounts exclusively. You can't use Azure Data Lake Gen1 storage accounts to ingest data.

- The Delta Lake storage account must have [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace).

- To authenticate with an Azure service principal, make sure it's configured in your tenant. For more information, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

- The Delta Lake you want to connect and ingest data from must be in the same Azure region as the Dynamics 365 Customer Insights environment. To know the Azure region of the environment, go to **Admin** > **System** > **About** in audience insights.

- Data stored in online services may be stored in a different location than where data is processed or stored in Dynamics 365 Customer Insights. By importing or connecting to data stored in online services, you agree that data can be transferred to and stored with Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

## Connect to Databricks delta lake storage

1. Go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Select **Databricks delta lake**.

   :::image type="content" source="media/data_sources_deltalake.png" alt-text="Dialog box to enter connection details for Databricks delta lake.":::

1. Enter a **Name** for the data source and an optional **Description**.

1. Choose your preferred option for **Connect your storage using**. For a resource or a subscription-based option for authentication, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

   - **Azure resource**: Enter the **Resource Id**.
   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**.
   - **Account key**: Enter the **Account name** and **Account key**.

1. If you have an Azure resource or subscription connection and want to enable an Azure private link, select **Enable Private link**. For more information, see  [What is Azure Private Link?](/azure/private-link/private-link-overview).

1. Enter the name of the **Container** that contains the delta lake folder to import data from.

1. Choose the **Connection to Azure Synapse** and **Spark pool**, and select **Next**.

1. Navigate to the delta lake folder that contains the list of entities and select it. A list of available entities displays.  

   :::image type="content" source="media/deltalake_select_entities.png" alt-text="Dialog box to select entities":::
  
1. Select the entities you want to include.

   :::image type="content" source="media/deltalake_required.png" alt-text="Dialog box showing selected entities requiring a Primary Key":::

1. For selected entities where a primary key has not been defined, **Required** displays under **Primary key**. For each of these entities:
   1. Select **Required**. The **Edit entity** pane displays.
   1. Choose the **Primary key**.
   1. Select **X** to save and close the pane.

1. To enable analytics and other capabilities, select **Attributes**. The Manage attributes page displays. Select **Data profiling** for the whole entity or for specific attributes and then select **Done**. By default, no entity is enabled for data profiling.

1. To enable an incremental refresh, see [Incremental refresh for Azure data lake and Databricks data sources](incremental-refresh-data-sources.md).

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

## Edit a Deltabricks delta lake storage data source

1. Go to **Data** > **Data sources**.

1. Next to the data source you'd like to update, select **Edit**.

   :::image type="content" source="media/data_sources_edit_deltalake.png" alt-text="Dialog box to edit delta lake storage":::

1. Optionally, change the description. You can't change the connection information.

1. Select **Next**.

1. Change any of the following:
   - To add additional entities to ingest, select **New entity**.
   - To remove any already selected entities if there are no dependencies, select the entity and **Delete**.
   - To edit an entity, change the [incremental refresh](incremental-refresh-data-sources.md), or run a one-time full refresh, select **Edit**.

     :::image type="content" source="media/data_sources_editdelta_entity.png" alt-text="Dialog box to edit an entity":::

1. Select **Attributes** to add or change attributes, or to enable data profiling. Then select **Done**.

1. Click **Save** to apply your changes and return to the **Data sources** page.
