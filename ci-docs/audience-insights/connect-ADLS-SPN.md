---
title: "Connect to Azure Data Lake Storage account by provisioning Audience Insights Service Principal Name (SPN)"
description: "Connect to Azure Data Lake Storage account by provisioning Audience Insights Service Principal Name (SPN)."
ms.date: 11/22/2020
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: adkuppa
ms.author: adkuppa
ms.reviewer: adkuppa
manager: shefym
---

# Connect to an Azure Data Lake Storage Gen2 account by provisioning Audience Insights Azure AD Service Principal Name (SPN) to your Azure AD tenant.

This article provides information on how to connect to an Azure Data Lake Storage Gen2 account by provisioning Audience Insights Azure AD Service Principal Name (SPN) to your Azure AD tenant.

### This process involves two steps

1. Provision Audience Insights Azure AD Service Principal in your Azure AD tenant

2. Grant permissions to the Audience Insights Azure AD Service Principal access on your storage account.

## Provision Audience Insights Azure AD Service Principal in your Azure AD tenant

### Prerequisites
- You should be a tenant admin to provision the Audience Insights Azure AD Service Principal in your Azure AD tenant.

### Instructions

1. Install the latest version of the “Azure Active Directory PowerShell for Graph” on your machine.
- On your machine, select the Windows key on your keyboard and search for “Windows PowerShell” and select “run as administrator”.

- In the PowerShell window that opens, type in / copy paste this instruction.
  
  Install-Module AzureAD
  
- Refer to this document for more information on installing the PowerShell for Azure AD https://docs.microsoft.com/en-us/powershell/azure/active-directory/install-adv2?view=azureadps-2.0

2. Tenant specific Service Principal Provisioning with Azure AD PowerShell Module
- In the PowerShell window opened from step #1 above, copy/paste the following command to provision Audience Insights Service Principal in your tenant. Replace “The tenant id” with your tenant where you want provision the CI Service Principal.

- The environment name parameter ‘AzureEnvironmentName’ is an optional field so you can skip this parameter if you choose to.

  Connect-AzureAD -TenantId "[your tenant Id]" -AzureEnvironmentName Azure
  
- Provision the Audience Insights App ID “0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff” and Display Name "Dynamics 365 AI for Customer Insights" by the following command.
  
  New-AzureADServicePrincipal -AppId "0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff" -DisplayName "Microsoft Dynamics 365 Customer Insights"
  
- You might be asked to login to the tenant using the user account from the tenant.

##Grant permissions to the Audience Insights Service Principal to access the storage account

###Prerequisites
- You should be a an admin/co-admin/owner  on the storage account to grant required roles for the Audience Insights Service Principal on the storage account.

###Instructions

1. Once the Audience Insights Service Principal is granted access as above, go to your Azure portal to manually grant permissions to the Audience Insights SP on the storage account you wish to attach to Audience Insights.

2. Go to https://portal.azure.com and login to your tenant.

3. Search and navigate to the storage account you wish to grant Audience Insights Service Principal access.

4. Once opened that storage account, select “Access control (IAM)” from the left side navigation pane and select “+ Add” and select “Add role assignment”
   > [!div class="mx-imgBorder"]
   > ![Screen showing how to add a role assignment in Azure portal](media/ADLS-SP-AddRoleAssignment.png)
   
5. In the “Add role assignment” blade/panel that opens, select the following.
- Role: Storage Blob Data Contributor

- Assign access to: User, group, or service principal.

- Select: Copy paste the CI First party app display name "Dynamics 365 AI for Customer Insights" to search.

- Select the item returned in the search

6. You will see that the Audience Insights Service Principal will be listed in the “Selected members:” list
   > [!div class="mx-imgBorder"]
   > ![Select the Audience Insights Service Principal](media/ADLS-SP-SelectSP.png)
   
7.	Click Save.

8.	You will get a confirmation message that the role assignment is granted for the Audience Insights Service Principal.

9.	You can go to either “Role assignment” tab or “Roles” tab and select “Contributor” role to confirm that the Audience Insights Service Principal is granted the required role assignment.

10.	It may take up to 15 minutes for the changes to propagate.
