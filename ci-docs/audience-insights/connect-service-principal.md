---
title: "Connect to an Azure Data Lake Storage Gen2 account with a service principal"
description: "Use an Azure service principal for audience insights to connect to your own data lake when attaching it to audience insights."
ms.date: 02/10/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: adkuppa
ms.author: adkuppa
ms.reviewer: mhart
manager: shellyha
---

# Connect to an Azure Data Lake Storage Gen2 account with an Azure service principal for audience insights

Automated tools that use Azure services should always have restricted permissions. Instead of having applications sign in as a fully privileged user, Azure offers service principals. Read on to learn how to connect audience insights with an Azure Data Lake Storage Gen2 account using an Azure service principal instead of storage account keys. 

You can use the service principal to securely [add or edit a Common Data Model folder as a data source](connect-common-data-model.md) or [create a new or update an existing environment](manage-environments.md#create-an-environment-in-an-existing-organization).

> [!IMPORTANT]
> - The Azure Data Lake Gen2 storage account that intends to use the service principal must have [Hierarchical Name Space (HNS) enabled](https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-namespace).
> - You need admin permissions for your Azure subscription to create the service principal.

## Create Azure service principal for audience insights

Before creating a new service principal for audience insights, check if it already exists in your organization.

### Look for an existing service principal

1. Go to the [Azure admin portal](https://portal.azure.com) and sign in to your organization.

2. Select **Azure Active Directory** from the Azure services.

3. Under **Manage**, select **Enterprise Applications**.

4. Search for the audience insights first party application ID `0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff` or the name `Dynamics 365 AI for Customer Insights`.

5. If you find a matching record, it means that the service principal for audience insights exists. You don't need to create it again.
   
   :::image type="content" source="media/ADLS-SP-AlreadyProvisioned.png" alt-text="Screenshot showing the existing service principal.":::
   
6. If no results are returned, create a new service principal.

### Create a new service principal

1. Install the latest version of the **Azure Active Directory PowerShell for Graph**. For more information, see [Install Azure Active Directory PowerShell for Graph](https://docs.microsoft.com/powershell/azure/active-directory/install-adv2).
   - On your PC, select the Windows key on your keyboard and search for **Windows PowerShell** and **Run as Administrator**.
   
   - In the PowerShell window that opens, enter `Install-Module AzureAD`.

2. Create the  service principal for audience insights with the Azure AD PowerShell Module.
   - In the PowerShell window, enter `Connect-AzureAD -TenantId "[your tenant ID]" -AzureEnvironmentName Azure`. Replace “your tenant ID” with the actual ID of your tenant where you want to create the service principal. The environment name parameter `AzureEnvironmentName` is optional.
  
   - Enter `New-AzureADServicePrincipal -AppId "0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff" -DisplayName "Dynamics 365 AI for Customer Insights"`. This command creates the service principal for audience insights on the selected tenant.  

## Grant permissions to the service principal to access the storage account

Go to the Azure portal to grant permissions to the service principal for the storage account you want to use in audience insights.

1. Go to the [Azure admin portal](https://portal.azure.com) and sign in to your organization.

1. Open the storage account you want the service principal for audience insights to have access to.

1. Select **Access control (IAM)** from the navigation pane and select **Add** > **Add role assignment**.
   
   :::image type="content" source="media/ADLS-SP-AddRoleAssignment.png" alt-text="Screeshot showing Azure portal while adding a role assignment.":::
   
1. In the **Add role assignment** pane, set the following properties:
   - Role: *Storage Blob Data Contributor*
   - Assign access to: *User, group, or service principal*
   - Select: *Dynamics 365 AI for Customer Insights* (the [service principal you created](#create-a-new-service-principal))

1.	Select **Save**.

It can take up to 15 minutes to propagate the changes.

## Enter the Azure Resource ID or the Azure Subscription details in the storage account attachment to Audience Insights.

Attach an Azure Data Lake storage account in audience insights to [store output data](manage-environments.md) or [use it as a data source](connect-common-data-service-lake.md). Choosing the Azure Data Lake option lets you choose between a resource-based or a subscription-based based approach.

Follow the below steps to provide the required information on the selected approach.

### Resource-based storage account connection

1. Go to the [Azure admin portal](https://portal.azure.com), sign in to your subscription and open the storage account.

1. Go to **Settings** > **Properties** on navigation pane.

1. Copy the storage account resource ID value.

   :::image type="content" source="media/ADLS-SP-ResourceId.png" alt-text="Copy the storage account resource ID.":::

1. In audience insights, insert the resource ID in the resource field displayed in the storage account connection screen.

   :::image type="content" source="media/ADLS-SP-ResourceIdConnection.png" alt-text="Enter the storage account resource ID information.":::   
   
1. Continue with the remaining steps in audience insights to attach the storage account.

### Subscription-based storage account connection

1. Go to the [Azure admin portal](https://portal.azure.com), sign in to your subscription and open the storage account.

1. Go to **Settings** > **Properties** on navigation pane.

1. Review the **Subscription**, **Resource group**, and the **Name** of the storage account to make sure you select the right values in audience insights.

1. In audience insights, choose the values or for the corresponding fields when attaching the storage account.
   
1. Continue with the remaining steps in audience insights to attach the storage account.
