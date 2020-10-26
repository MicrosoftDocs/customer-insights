---
title: Configure connections
description: How set up and manage connections
author: m-hartmann
ms.reviewer: ruthai
ms.author: mhart
ms.date: 10/26/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Configure connections

Connecting [Dynamics 365 Customer Insights audience insights](../audience-insights/index.yml) and engagement insights capabilities lets you perform interactive analysis on customer data.

> [!IMPORTANT]
> The audience insights environment you plan to connect must write the data to a customer's own Azure Data Lake Stoarge Gen 2 account. Audience insights administrators define this in the advanced settings when [creating an environment](../audience-insights/manage-environments.md#create-an-environment-in-an-existing-organization).

## Set up the connection with audience insights

As an [environment admin](user-roles.md), you can set up connections from all environments you administer. To change to a different environment, see [Choose the environment to configure](manage-environments-workspaces.md#choose-the-environment-to-configure).

1. Go to **Admin** > **Settings** > **General**.

1. Select **Go to admin center**.

1. Select **Connections**.

1. If it's your first connection, select **Create a connection**. To create more connections, select **Add a connection**.
   :::image type="content" source="media/create-connection.png" alt-text="Create a new connection to Customer Insights":::

1. Provide the settings to your audience insights Azure Data Lake Storage Gen2. For more information about storage accounts, see [Create and manage storage accounts](https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-quickstart-create-account).
   - **ADLS gen2 storage account**: Provide the storage account name. For example, my-storage-account.
   - **Shared Key**: The access key to authenticate your applications. The can be found in Azure portal under **Access keys** in the storage account settings.
   - **AUI Environment ID**:  The audience insights environment ID. You can find the ID in audience insights, under **Settings** > **About**.
   - **AUI Instance Folder name**: The folder path to the audience insights instance in the storage account. For example, `customerInsights/ci_xxxxxx-xxx-xxxxx`.

1. Select Next.

1. Customer profile data often contains sensitive customer details such as age, gender, and income. Only the environment admins will have access to the customer profile data, unless explicitly granted.    
   You can add or remove access to this data in the Connections area of the admin center.
 
1. As a last step, review the settings before creating the connection. 

> [!NOTE]
> It may take several hours for the data to become available in engagement insights. You can check the status in the Connections area.

