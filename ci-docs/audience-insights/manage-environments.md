---
title: "Create and manage environments"
description: "Learn how to sign up for the service and how to manage environments."
ms.date: 06/15/2021
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
