---
title: "Create and manage environments"
description: "Learn how to sign up for the service and how to manage environments."
ms.date: 07/22/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
ms.reviewer: mhart
author: NimrodMagen
ms.author: nimagen
manager: shellyha
---

# Manage environments

[!INCLUDE [cc-data-platform-banner](../includes/cc-data-platform-banner.md)]

## Switch environments

Select the **Environment** control in the upper-right corner of the page to change environments.

:::image type="content" source="media/home-page-environment-switcher.png" alt-text="Screenshot of the control to switch environments.":::

Administrators can [create](get-started-paid.md) and manage environments.

## Edit an existing environment

You can edit some of the details of existing environments.

1.	Select the **Environment** picker in the header of the app.

2.	Select the **Edit** icon.

3. In the **Edit environment** box, you can update the environment's **Display name**, but you can't change the **Region** or **Type**.

4. If an environment is configured to store data in Azure Data Lake Storage, you can update the **Account key**. However, you can't change the **Account name** or **Container** name.

5. Optionally, you can update from an account key-based connection to a resource-based or subscription-based connection. Once upgraded, you cannot revert to account key after the update. For more information, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md). You can't change **Container** information when updating the connection.

6. Optionally, you can provide a Microsoft Dataverse environment URL under **Configure data sharing with Microsoft Dataverse and enable additional capabilities**. These capabilities include data sharing with applications and solutions based on Microsoft Dataverse, data ingestion from on-premises data sources, or the use [predictions](predictions.md). Select **Enable data sharing** to share Customer Insights output data with a Microsoft Dataverse Managed Data lake.

   > [!NOTE]
   > - Data sharing with Microsoft Dataverse Managed Data Lake is currently not supported when you save all data to your own Azure Data Lake Storage.
   > - [Prediction of missing values in an entity](predictions.md) is currently not supported when you enable data sharing with Microsoft Dataverse Managed Data Lake.

   After enabling data sharing with Microsoft Dataverse, a full refresh of your data sources and other processes starts. If processes are currently running, you don't see the option to enable data sharing with Microsoft Dataverse. Wait for those processes to complete or cancel them to enable data sharing. 
   
   :::image type="content" source="media/datasharing-with-DataverseMDL.png" alt-text="Configuration options to enable data sharing with Microsoft Dataverse.":::
   
   When you run processes, such as data ingestion or segment creation, corresponding folders will be created in the storage account you specified above. Data files and model.json files will be created and added to the respective subfolders, depending on the process you run.

## Copy the environment configuration

When you create a new environment, you can choose to copy the configuration from an existing environment. 

:::image type="content" source="media/environment-settings-dialog.png" alt-text="Screenshot of the settings options in the environment settings.":::

You'll see a list of all available environments in your organization where you can copy data from.

The following configuration settings are copied:

- Ingested/imported data sources
- Data unification (Map, Match, Merge) configuration
- Segments
- Measures
- Relationships
- Activities
- Search & filter Index
- Export destinations
- Scheduled refresh
- Enrichments
- Model management
- Role assignments

The following data is *not* copied:

- Customer profiles.
- Data source credentials. You'll have to provide the credentials for every data source and refresh the data sources manually.
- Data sources from Common Data Model folder and Dataverse managed Data Lake. You'll have to create those data sources manually with the same name as in the source environment.

When you copy an environment, you'll see a confirmation message that the new environment has been created. Select **Go to data sources** to see the list of data sources.

All the data sources will show a **Credentials Required** status. Edit the data sources and enter the credentials to refresh them.

:::image type="content" source="media/data-sources-copied.png" alt-text="List of data sources that were copied and need authentication.":::

After refreshing the data sources, go to **Data** > **Unify**. Here you'll find settings from the source environment. Edit them as needed or select **Run** to start the data unification process and create the unified customer entity.

When the data unification is complete, go to **Measures** and **Segments** to refresh them too.

## Reset an existing environment

As an administrator, you can reset an environment to an empty state if you want to delete all configurations and remove the ingested data.

1.	Select the **Environment** picker in the header of the app. 

2.	Select the environment you want to reset and select the ellipsis (**...**). 

3. Choose the **Reset** option. 

4.	To confirm the deletion, enter the environment name and select **Reset**.

## Delete an existing environment

As an administrator, you can delete an environment you administer.

1.	Select the **Environment** picker in the header of the app.

2.	Select the environment you want to reset and select the ellipsis (**...**). 

3. Choose the **Delete** option. 

4.	To confirm the deletion, enter the environment name and select **Delete**.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
