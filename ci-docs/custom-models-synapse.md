---
title: "Custom machine learning models from Azure Synapse"
description: "Work with custom models from Azure Synapse in Dynamics 365 Customer Insights."
ms.date: 11/8/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: tutorial
author: radsay01
ms.author: rsayyaparaju
manager: shellyha
searchScope: 
  - ci-custom-models
  - customerInsights
---

# Custom machine learning models from Azure Synapse

## Prerequisites

- Workspace: An Azure Synapse workspace

- Storage account: An [Azure Data Lake Gen2 storage account](/azure/storage/blobs/data-lake-storage-quickstart-create-account) associated with your Azure Studio instance.

## Set up a Synapse connection

1. Go to **Admin** > **Connections**.

1. Scroll to **Miscellaneous connections**.

1. Select **Set up** on the **Azure Synapse Analytics** tile.

1. Enter the following information.

   :::image type="content" source="media/Synapse-connection.png" alt-text="Screenshot of the Azure Synapse Analytics connection page.":::

   - **Display name**: A unique, recognizable name that describes this connection. Must start with a letter and contain only letters, numbers, and underscores.
   - **Choose who can use this connection**: Select administrators only or administrators and contributors.
   - **Subscription**: The Azure Synapse subscription to use for the custom model. 
   - **Workspace**: The Synapse workspace. To set up a new workspace, select [**Create new**](/azure/synapse-analytics/quickstart-create-workspace).
   - **Storage account**: The Synapse storage account. To set up a new account, select [**Link new**](/azure/storage/common/storage-account-create?bc=%2Fazure%2Fsynapse-analytics%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal).
   - **Container**: The container within the storage account.

1. Review the data privacy and compliance and select **I agree**.

1. Select **Save**.

## Add a new workflow