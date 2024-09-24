---
title: Use your own Azure Data Lake Storage account
description: Learn about the requirements to use your own Azure Data Lake Storage account in Customer Insights - Data.
author: Scott-Stabbert
ms.author: sstabbert
ms.date: 09/23/2024
ms.topic: how-to
ms.collection: get-started
ms.reviewer: mhart
ms.custom: bap-template
---

# Use your own Azure Data Lake Storage account

Dynamics 365 Customer Insights - Data gives you the option to store your customer data in [Azure Data Lake Storage](/azure/storage/blobs/data-lake-storage-introduction). Customer data includes data that you import and the output data like unified profiles and segments. [Some of the output data](tables.md#customer-insights---data-tables-in-dataverse) is also stored as tables in Microsoft Dataverse along with metadata like match rules or segment configuration, and search index. By saving data to Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account. For more information, see [Microsoft Trust Center](https://www.microsoft.com/trust-center).

Administrators in Customer Insights - Data can [create environments](create-environment.md) and [specify the data storage option](create-environment.md#step-2-configure-data-storage) in the process.

## Prerequisites

- Azure Data Lake Storage accounts must be in the same Azure region that you selected when creating the Customer Insights - Data environment. To know the region of the environment, go to **Settings** > **System** > **About**.
- The Data Lake Storage account must have [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace).
- The administrator setting up the Customer Insights - Data environment needs the Storage Blob Data Contributor or Storage Blob Data Owner role on the storage account or the `customerinsights` container. For more information on assigning permission in a storage account, see [Create a storage account](/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal).

## Connect Customer Insights - Data with your own Azure Data Lake Storage

When you create a new environment, make sure the Data Lake Storage account exists and all prerequisites are met.

1. In the **Data storage** step during environment creation, set **Save output data** to **Azure Data Lake Storage Gen2**.
1. Choose how to **Connect your storage**. You can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect to an Azure Data Lake Storage account by using a Microsoft Entra service principal](connect-service-principal.md).
   - For **Azure subscription**, choose the **Subscription**, **Resource group**, and **Storage account** that contains the `customerinsights` container.
   - For **Account key**, provide the **Account name** and the **Account key** for your Data Lake Storage account. Using this authentication method implies that you're informed if your organization rotates the keys. You must [update the environment configuration](manage-environments.md#edit-an-existing-environment) with the new key when it's rotated.
1. Choose if you want to use Azure Private Link to connect to your storage account and [create the connection to Private Link](private-link.md).

When system processes like data ingestion complete, the system creates corresponding folders in the storage account. Data files and model.json files are created and added to folders based on the process name.

If you create multiple environments and choose to save the output tables from those environments to your storage account, the system creates separate folders for each environment with `ci_environmentID` in the container.

## Enable data sharing with Dataverse from your own Azure Data Lake Storage (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Dynamics 365 Customer Insights - Data writes output data like unified profiles and segments to your Azure Data Lake Storage. You can enable data sharing to make output data in your Azure Data Lake Storage available to your [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro) environment. The user who sets up the Customer Insights - Data environment needs at least **Storage Blob Data Reader** permissions on the `customerinsights` container in the storage account.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

### Limitations

- A single one-to-one mapping between a Dataverse organization and an Azure Data Lake Storage account is supported.
- The target storage account can't be changed.
- Data sharing doesn't work if an Azure Private Link setup is needed to access your Azure Data Lake Storage account because it's behind a firewall. Dataverse currently doesn't support the connection to private endpoints through Private Link.
- [Automatic linking of customer profiles](integrate-d365-apps.md) in Dataverse isn't supported when using your own Azure Data Lake Storage.

### Set up security groups on your own Azure Data Lake Storage

1. Create two security groups on your Azure subscription - one **Reader** security group and one **Contributor** security group and set the Microsoft Dataverse service as the owner for both security groups.

1. Manage the Access Control List (ACL) on the `customerinsights` container in your storage account through these security groups.
   1. Add the Microsoft Dataverse service and any Dataverse-based business applications like Dynamics 365 Sales to the **Reader** security group with **read-only** permissions.
   1. Add *only* the Customers Insights application to the **Contributor** security group to grant both **read and write** permissions to write profiles and insights.

### Set up PowerShell

Set up PowerShell to execute PowerShell scripts.

1. Install the latest version of [Azure Active Directory PowerShell for Graph](/powershell/azure/active-directory/install-adv2).
   1. On your PC, select the Windows key on your keyboard and search for **Windows PowerShell** and select **Run as administrator**.
   1. In the PowerShell window that opens, enter `Install-Module AzureAD`.

1. Import three modules.
   1. In the PowerShell window, enter `Install-Module -Name Az.Accounts` and follow the steps.
   1. Repeat for `Install-Module -Name Az.Resources` and `Install-Module -Name Az.Storage`.

### Execute PowerShell scripts and obtain the Permission Identifier

1. Download the two PowerShell scripts you need to run from our engineer's [GitHub repo](https://github.com/trin-msft/byol).
   - `CreateSecurityGroups.ps1`: Requires tenant admin permissions.
   - `ByolSetup.ps1`: Requires Storage Blob Data Owner permissions at the storage account/container level. This script creates the permission for you. Your role assignment can be removed manually after successfully running the script.

1. Execute `CreateSecurityGroups.ps1` in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage. Open the PowerShell script in an editor to review additional information and the implemented logic.

   This script creates two security groups on your Azure subscription: one for the Reader group and another for the Contributor group. Microsoft Dataverse service is the owner for both these security groups.

1. Save both the security group ID values generated by this script to use in the `ByolSetup.ps1` script.

   > [!NOTE]
   > Security group creation can be disabled on your tenant. In that case, a manual setup would be needed and your Azure AD admin would have to [enable security group creation](/azure/active-directory/enterprise-users/groups-self-service-management).

1. Execute `ByolSetup.ps1` in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage, storage account name, resource group name, and the Reader and Contributor security group ID values. Open the PowerShell script in an editor to review additional information and the implemented logic.

   This script adds the required role-based access control for the Microsoft Dataverse service and any Dataverse-based business applications. It also updates the Access Control List (ACL) on the `customerinsights` container for the security groups created with the `CreateSecurityGroups.ps1` script. The Contributor group is given *rwx* permission and Readers group is given *r-x* permission only.

1. Copy the output string that looks like: `https://DVBYODLDemo/customerinsights?rg=285f5727-a2ae-4afd-9549-64343a0gbabc&cg=720d2dae-4ac8-59f8-9e96-2fa675dbdabc`

1. Enter the copied output string into the **Permissions identifier** field during [environment configuration  for Microsoft Dataverse](create-environment.md#step-3-choose-dataverse-environment).

   :::image type="content" source="media/dataverse-enable-datasharing-BYODL.png" alt-text="Configuration options to enable data sharing from your own Azure Data Lake Storage with Microsoft Dataverse.":::

[!INCLUDE [footer-include](includes/footer-banner.md)]
