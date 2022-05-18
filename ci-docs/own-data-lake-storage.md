---
title: Store Customer Insights data in your own Azure Data Lake Storage account
author: mukeshpo
ms.author: mukeshpo
description: Learn about the requirements to use your own Azure Data Lake Storage account for Customer Insights.
ms.author: mhart
ms.date: 05/18/2022
ms.topic: conceptual
ms.manager: shellyha
ms.custom: intro-internal
ms.reviewer: mhart
---

# Use your own Azure Data Lake Storage account

Dynamics 365 Customer Insights gives you the option to store all your data in an Azure Data Lake Storage Gen2 account. Choosing this option gives you the highest level of control over your data.

By saving data to Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account. Learn more at the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

Administrators in Customer Insights can [create environments](create-environment.md) and [specify the data storage option](create-environment.md#step-2-configure-data-storage) in the process.

## Important considerations

- Azure Data Lake Storage accounts must be in the same Azure region that you selected when creating the Customer Insights environment. You can check the region of the Customer Insights environment under **Admin** > **System** > **About**.
- Data Lake Storage must be Gen2 and have [hierarchical namespace enabled](/azure/storage/blobs/create-data-lake-storage-account). Gen1 storage accounts are not supported.
- The administrator setting up the Customer Insights environment needs Storage Blob Data reader, Storage Blob Data Contributor, or Storage Blob Data Owner role on the storage container.
- A Microsoft Dataverse environment can only connect to a single storage account.

## TODO Connect to the storage account

2 options? SPN and subscription/key?

For the Azure Data Lake Storage option, you can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect to an Azure Data Lake Storage account by using an Azure Service Principal](connect-service-principal.md). A container named `customerinsights` has to exist on the storage account.

When system processes such as data ingestion complete, the system creates corresponding folders in the storage account you specified. Data files and *model.json* files are created and added to folders based on the process name.

If you create multiple environments of Customer Insights and choose to save the output entities from those environments to your storage account, Customer Insights creates separate folders for each environment with `ci_environmentID` in the container.
