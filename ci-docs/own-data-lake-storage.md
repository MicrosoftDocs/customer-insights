---
title: Use your own Azure Data Lake Storage Gen2 account
author: mukeshpo
description: Learn about the requirements to use your own Azure Data Lake Storage account to store Customer Insights data.
ms.author: mukeshpo
ms.date: 06/08/2022
ms.topic: conceptual
ms.manager: shellyha
ms.custom: intro-internal
ms.reviewer: mhart
---

# Use your own Azure Data Lake Storage Gen2 account

Dynamics 365 Customer Insights gives you the option to store all your data in [Azure Data Lake Storage Gen2](/azure/storage/blobs/data-lake-storage-introduction).

By saving data to Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account. For more information, see [Microsoft Trust Center](https://www.microsoft.com/trust-center).

Administrators in Customer Insights can [create environments](create-environment.md) and [specify the data storage option](create-environment.md#step-2-configure-data-storage) in the process.

## Prerequisites to use your storage account

- Azure Data Lake Storage accounts must be in the same Azure region that you selected when creating the Customer Insights environment. You can check the region of the Customer Insights environment under **Admin** > **System** > **About**.
- Data Lake Storage must be Gen2 and have [hierarchical namespace enabled](/azure/storage/blobs/create-data-lake-storage-account). Gen1 storage accounts aren't supported.
- A container named `customerinsights` has to exist on the storage account. You have to create it before you use your own Data Lake Storage in Customer Insights. The administrator setting up the Customer Insights environment needs the Storage Blob Data Contributor or Storage Blob Data Owner role on the storage account or the `customerinsights` container. For more information on assigning permission in a storage account, see [Create a storage account](/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal).

## Connect Customer Insights with your storage account

When you create a new environment, make sure the Data Lake Storage account exists and all prerequisites are met.

1. In the **Data storage** step during environment creation, set **Save output data** to **Azure Data Lake Storage Gen2**.
1. Choose how to **Connect your storage**. You can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect to an Azure Data Lake Storage account by using an Azure Service Principal](connect-service-principal.md).
   - For **Azure subscription**, choose the **Subscription**, **Resource group**, and **Storage account** that contains the `customerinsights` container.
   - For **Account key**, provide the **Account name** and the **Account key** for the Data Lake Storage account. Using this authentication method implies that you're informed if your organization rotates the keys. You must [update the environment configuration](manage-environments.md#edit-an-existing-environment) with the new key when it's rotated.
1. Choose if you want to use Azure Private Link to connect to the storage account and c[reate the connection to Private Link](security-overview.md#private-links-tab) with a two-step process.

When system processes like data ingestion complete, the system creates corresponding folders in the storage account. Data files and *model.json* files are created and added to folders based on the process name.

If you create multiple environments of Customer Insights and choose to save the output entities from those environments to your storage account, Customer Insights creates separate folders for each environment with `ci_environmentID` in the container.
