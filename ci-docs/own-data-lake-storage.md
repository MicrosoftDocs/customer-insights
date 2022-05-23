---
title: Store Customer Insights data in your own Azure Data Lake Storage account
author: mukeshpo
description: Learn about the requirements to use your own Azure Data Lake Storage account for Customer Insights.
ms.author: mukeshpo
ms.date: 05/18/2022
ms.topic: conceptual
ms.manager: shellyha
ms.custom: intro-internal
ms.reviewer: mhart
---

# Use your own Azure Data Lake Storage Gen2 account

Dynamics 365 Customer Insights gives you the option to store all your data in [Azure Data Lake Storage Gen2](/azure/storage/blobs/data-lake-storage-introduction). Choosing this option gives you the highest level of control over your data.

By saving data to Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account. For more information, see [Microsoft Trust Center](https://www.microsoft.com/trust-center).

Administrators in Customer Insights can [create environments](create-environment.md) and [specify the data storage option](create-environment.md#step-2-configure-data-storage) in the process.

## Prerequisites to use your storage account

- Azure Data Lake Storage accounts must be in the same Azure region that you selected when creating the Customer Insights environment. You can check the region of the Customer Insights environment under **Admin** > **System** > **About**.
- Data Lake Storage must be Gen2 and have [hierarchical namespace enabled](/azure/storage/blobs/create-data-lake-storage-account). Gen1 storage accounts are not supported.
- A container named `customerinsights` has to exist on the storage account. You have to create it before you use your own Data Lake Storage in Customer Insights. The administrator setting up the Customer Insights environment needs the Storage Blob Data Reader, Storage Blob Data Contributor, or Storage Blob Data Owner role on the storage account or the `customerinsights` container. For more information, see [Create a storage account](/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal).

## Connect Customer Insights with your storage account

When you create a new environment, make sure the Data Lake Storage account exists and all prerequisites are met.

1. In the **Data storage** step during environment creation, set **Save output data** to **Azure Data Lake Storage Gen2**.
1. Choose how to **Connect your storage**. You can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect to an Azure Data Lake Storage account by using an Azure Service Principal](connect-service-principal.md).
   - For **Azure subscription**, choose the **Subscription**, **Resource group**, and **Storage account** that contains the `customerinsights` container.
   - For **Account key**, provide the **Account name** and the **Account key** for the Data Lake Storage account.

When system processes such as data ingestion complete, the system creates corresponding folders in the storage account you specified. Data files and *model.json* files are created and added to folders based on the process name.

If you create multiple environments of Customer Insights and choose to save the output entities from those environments to your storage account, Customer Insights creates separate folders for each environment with `ci_environmentID` in the container.

## Enable data sharing with Dataverse (Preview)

Enabling data sharing with Microsoft Dataverse needs some extra configuration. The user setting up the Customer Insights environment must have at least **Storage Blob Data Reader** permissions on the *CustomerInsights* container in the Azure Data Lake Storage account.

1. Create two security groups on your Azure subscription - one **Reader** security group and one **Contributor** security group and set the Microsoft Dataverse service as the owner for both security groups.
2. Manage the Access Control List (ACL) on the CustomerInsights container in your storage account via these security groups. Add the Microsoft Dataverse service and any Dataverse-based business applications like Dynamics 365 Marketing to the **Reader** security group with **read-only** permissions. Add *only* the Customers Insights application to the **Contributor** security group to grant both **read and write** permissions to write profiles and insights.

### Limitations

There are two limitations when using Dataverse in connection with your own Azure Data Lake Storage account:

- There's one-to-one mapping between a Dataverse organization and an Azure Data Lake Storage account. Once a Dataverse organization is connected to a storage account, it can't connect to another storage account. This limitation prevents that a Dataverse doesn't populate multiple storage accounts.
- Data sharing won't work if an Azure Private Link setup is needed to access your Azure Data Lake storage account because it's behind a firewall. Dataverse currently doesn't support the connection to private endpoints through Private Link.

### Set up PowerShell

To execute the PowerShell scripts you first need to set up PowerShell accordingly.

1. Install the latest version of [Azure Active Directory PowerShell for Graph](/powershell/azure/active-directory/install-adv2).
   1. On your PC, select the Windows key on your keyboard and search for **Windows PowerShell** and select **Run as administrator**.
   1. In the PowerShell window that opens, enter `Install-Module AzureAD`.
2. Import three modules.
    1. In the PowerShell window, enter `Install-Module -Name Az.Accounts` and follow the steps. 
    1. Repeat for `Install-Module -Name Az.Resources` and `Install-Module -Name Az.Storage`.

### Configuration steps

1. Download the two PowerShell scripts you need to run from our engineer's [GitHub repo](https://github.com/trin-msft/byol).
    1. `CreateSecurityGroups.ps1`
       - You need *tenant admin* permissions to run this PowerShell script. 
       - This PowerShell script creates two security groups on your Azure subscription. One for the Reader group and another for the Contributor group and will make Microsoft Dataverse service as the owner for both these security groups.
       - Execute this PowerShell script in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage. Open the PowerShell script in an editor to review additional information and the logic implemented.
       - Save both the security group ID values generated by this script because we'll use them in the `ByolSetup.ps1` script.

        > [!NOTE]
        > Security group creation can be disabled on your tenant. In that case, a manual setup would be needed and your Azure AD admin would have to [enable security group creation](/azure/active-directory/enterprise-users/groups-self-service-management).

    2. `ByolSetup.ps1`
        - You need *Storage Blob Data Owner* permissions at the storage account/container level to run this script or this script will create one for you. Your role assignment can be removed manually after successfully running the script.
        - This PowerShell script adds the required tole-based access control (RBAC) for the Microsoft Dataverse service and any Dataverse-based business applications. It also updates the Access Control List (ACL) on the CustomerInsights container for the security groups created with the `CreateSecurityGroups.ps1` script. The Contributor group will have *rwx* permission and Readers group will have *r-x* permission only.
        - Execute this PowerShell script in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage, storage account name, resource group name, and the Reader and Contributor security group id values. Open the PowerShell script in an editor to review additional information and the logic implemented.
        - Copy the output string after successfully running the script. The output string looks like this: `https://DVBYODLDemo/customerinsights?rg=285f5727-a2ae-4afd-9549-64343a0gbabc&cg=720d2dae-4ac8-59f8-9e96-2fa675dbdabc`

2. Enter the output string copied from above into the **Permissions identifier** field of the environment configuration step for Microsoft Dataverse.

:::image type="content" source="media/dataverse-enable-datasharing-BYODL.png" alt-text="Configuration options to enable data sharing from your own Azure Data Lake Storage with Microsoft Dataverse.":::