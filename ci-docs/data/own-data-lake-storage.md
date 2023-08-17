---
title: Use your own Azure Data Lake Storage Gen2 account
author: mukeshpo
description: Learn about the requirements to use your own Azure Data Lake Storage account to store Customer Insights data.
ms.author: mukeshpo
ms.date: 07/28/2023
ms.topic: conceptual
ms.collection: get-started
ms.reviewer: mhart
---

# Use your own Azure Data Lake Storage Gen2 account

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 Customer Insights gives you the option to store your customer data in [Azure Data Lake Storage Gen2](/azure/storage/blobs/data-lake-storage-introduction). Customer data includes data that you import into Customer Insights and the output data like unified profiles and segments. [Some of the output data](tables.md#customer-insights-data-tables-in-dataverse) is also stored as tables in Microsoft Dataverse along with metadata like match rules or segment configuration, and search index. By saving data to Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account. For more information, see [Microsoft Trust Center](https://www.microsoft.com/trust-center).

Administrators in Customer Insights can [create environments](create-environment.md) and [specify the data storage option](create-environment.md#step-2-configure-data-storage) in the process.

## Prerequisites

- Azure Data Lake Storage accounts must be in the same Azure region that you selected when creating the Customer Insights environment. To know the region of the environment, go to **Settings** > **System** > **About** in Customer Insights.
- The Data Lake Storage account must be Gen2. Azure Data Lake Gen1 storage accounts are not supported.
- The Data Lake Storage account must have [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace).
- A container named `customerinsights` has to exist on the storage account. Create it before you use your own Data Lake Storage in Customer Insights.
- The administrator setting up the Customer Insights environment needs the Storage Blob Data Contributor or Storage Blob Data Owner role on the storage account or the `customerinsights` container. For more information on assigning permission in a storage account, see [Create a storage account](/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal).

## Connect Customer Insights with your storage account

When you create a new environment, make sure the Data Lake Storage account exists and all prerequisites are met.

1. In the **Data storage** step during environment creation, set **Save output data** to **Azure Data Lake Storage Gen2**.
1. Choose how to **Connect your storage**. You can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect to an Azure Data Lake Storage account by using an Azure Service Principal](connect-service-principal.md).
   - For **Azure subscription**, choose the **Subscription**, **Resource group**, and **Storage account** that contains the `customerinsights` container.
   - For **Account key**, provide the **Account name** and the **Account key** for the Data Lake Storage account. Using this authentication method implies that you're informed if your organization rotates the keys. You must [update the environment configuration](manage-environments.md#edit-an-existing-environment) with the new key when it's rotated.
1. Choose if you want to use Azure Private Link to connect to the storage account and [create the connection to Private Link](private-link.md).

When system processes like data ingestion complete, the system creates corresponding folders in the storage account. Data files and model.json files are created and added to folders based on the process name.

If you create multiple environments of Customer Insights and choose to save the output tables from those environments to your storage account, Customer Insights creates separate folders for each environment with `ci_environmentID` in the container.
