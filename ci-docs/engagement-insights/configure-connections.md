---
title: Configure connections
description: How set up and manage connections to audience insights.
author: mochimochi016
ms.reviewer: mhart
ms.author: jefhar
ms.date: 10/30/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Configure connections

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Connecting [Dynamics 365 Customer Insights audience insights](../audience-insights/index.yml) and engagement insights capabilities lets you see [reports on customer data](profile-reports.md).

> [!IMPORTANT]
> The audience insights environment you plan to connect must write the data to a customer's own Azure Data Lake Stoarge Gen 2 account. Audience insights administrators define this in the advanced settings when [creating an environment](../audience-insights/manage-environments.md#create-an-environment-in-an-existing-organization).

## Prerequisites

- The person who sets up the connection has [environment admin](user-roles.md) permissions in engagement insights.
- The same environment admin should be the admin for the storage account or have access to the storage account details such as shared keys.

## Set up the connection with audience insights

As an [environment admin](user-roles.md), you can set up connections from all environments you administer. To change to a different environment, see [Choose the environment to configure](manage-environments-workspaces.md#choose-an-environment-and-create-a-workspace).

1. Go to **Admin** > **Environment**  and select **Connections**.

1. If it's your first connection, select **Create a connection**. To create more connections, select **Add a connection**.
   :::image type="content" source="media/create-connection.png" alt-text="Create a new connection to Customer Insights":::

1. Provide the settings to your audience insights Azure Data Lake Storage Gen2. For more information about storage accounts, see [Create and manage storage accounts](/azure/storage/blobs/data-lake-storage-quickstart-create-account).
   - **ADLS gen2 storage account**: Provide the storage account name. For example, my-storage-account.
   - **Shared Key**: The access key to authenticate your applications. The can be found in Azure portal under **Access keys** in the storage account settings.
   - **Audience insights Environment ID**:  The audience insights environment ID. You can find the ID in audience insights, under **Settings** > **About**.
   - **Audience insights Environment Folder name**: The folder path to the audience insights environment in the storage account. For example, `ci_xxxxxx-xxx-xxxxx`.

1. Select **Next**.

1. Customer profile data often contains sensitive customer details such as age, gender, and income. Only the environment admin who sets up the connection has access to the customer profile report automatically. Other members can't see the report unless explicitly granted access.    
   You can add or remove members who have access to this data in the **Connections** area of the environment settings.
 
1. Review the settings and select **Done** to create the connection. 

> [!NOTE]
> It may take several hours for the data to become available in engagement insights. You can check if a connection has been made in the **Connections** area.

To see the customer profiles report, go to **Discover** > **Profiles**. 
For more information, see [Customer profile report](profile-reports.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]