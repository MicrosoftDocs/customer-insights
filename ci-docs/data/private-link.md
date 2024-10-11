---
title: Set up managed identities for storage accounts behind firewalls
description: Learn how to set up managed identities for Azure resources to connect your Data Lake Storage behind firewalls.
ms.date: 10/11/2024
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: mhart
ms.custom: bap-template
---

# Set up managed identities for storage accounts behind firewalls

If you have Azure storage protected by firewalls, use managed identities for Azure resources to connect to Customer Insights - Data. Managed identities for Azure provides improved connection security with a system-assigned managed identity that can't be accessed or used outside of its configured endpoints.

Configure Customer Insights - Data to connect to Azure storage containers protected by firewalls in the following scenarios:

- Data output - Configure Customer Insights - Data at setup to write processed customer insights output data to your private Azure storage container.
- Data input - Create data connections to ingest source data from your Azure storage containers.
- Exports - Configure exports to write specific tables to Azure storage containers.

> [!NOTE]
> If you currently use Azure Private Links, review the prerequisites and then [migrate your private links to managed identities](#migrate-private-links-to-managed-identities-for-azure-resources).

## Prerequisites

- You have an Azure subscription Owner role.
- You have access to the Power Platform admin center and Azure portal.
- The Azure storage account is in the same region as the Customer Insights – Data Dataverse environment.
- You have the Dataverse environment ID for Customers Insights - Data. [Edit the environment](manage-environments.md#edit-an-existing-environment) and obtain the Customers Insights - Data environment URL. Then, obtain the [environment ID from the Power Platform admin center](/power-platform/admin/determine-org-id-name#find-your-environment-and-organization-id).
- You have the [Azure subscription ID](/azure/azure-portal/get-subscription-tenant-id), location, and resource group name for each storage container.
- The [Azure CLI is download and installed](https://aka.ms/InstallAzureCliWindows).
- The following PowerShell modules are installed
  - Azure Az PowerShell module: `Install-Module -Name Az`
  - Azure Az.Resources PowerShell module: `Install-Module -Name Az.Resources`
  - Power Platform admin PowerShell module: `Install-Module -Name Microsoft.PowerApps.Administration.PowerShell`
- This [GitHub compressed file](https://github.com/microsoft/PowerApps-Samples/blob/master/powershell/managed-identities/Common.zip) is downloaded and extracted in a location where you can run PowerShell commands. This file contains PowerShell comments put it where you can run it.

## Enable access to storage through managed identities

Perform these steps once per subscription.

1. Determine if there is an existing enterprise policy for the Dataverse environment. Run the script:
   `GetIdentityEnterprisePolicyForEnvironment`
   If a policy exists, the policy ID is returned.
   - If there is an existing policy, obtain the policy ID and skip to step 5.
   - If there isn't an existing enterprise policy, perform the following steps.  
1. [Enable the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#enable-enterprise-policy-for-the-selected-azure-subscription) for the Azure subscription.
1. [Create the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#create-enterprise-policy). One policy can be used for multiple Dataverse environments.
1. [Grant reader access to the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#grant-reader-access-to-the-enterprise-policy-via-azure).
1. [Connect the enterprise policy to the Dataverse environment](/power-apps/maker/data-platform/azure-synapse-link-msi#connect-enterprise-policy-to-dataverse-environment).
1. Continue to grant enterprise policy access to Azure storage and then allow the enterprise policy access to the storage account or container.

### Grant enterprise policy access to Azure storage

Perform these steps for each storage account or container.

1. Sign in to the [Azure portal](https://portal.azure.com/).
1. Open the storage account that you want to connect. To grant access to a specific container, go to containers under the **Data storage** section and select the container.
1. On the left navigation pane, select **Access Control (IAM)**.
1. Select the **Role assignments** tab. Select **Add** > **Add role assignment**.
1. Search for and select **Storage Blob Data Contributor**.
1. Select the **Members** tab. Under **Assign access to**, select **Managed identity**.
1. Select **Select members**, select the correct subscription, and the **microsoft.powerplatform/enterprisepolicies[Identity]** option.
1. Select the enterprise policy you created and **Save**.

### Allow enterprise policy access to the storage account behind the firewall

1. Open the storage account in the Azure portal.
1. Select the **Networking** tab.
1. Select **Enabled from selected virtual networks and IP addresses**.
1. For the **Resource type**, select **Microsot.PowerPlatform/enterprisePolicies** and the instance name for the enterprise policy.
1. Select **Save**.

## Migrate Private Links to managed identities for Azure resources

If you currently use Azure Private Links, update existing data connections using Private Links to managed identities for Azure resources.

1. Sign in to Customer Insights - Data.
   A message says that you have one or more storage accounts that must be upgraded.
1. From the Action required message, select **See details**.
   :::image type="content" source="media/upgrade-to-managed-id.jpg" alt-text="Dialog box to upgrade to managed identities for Azure.":::
1. Expand **Step 1 Enable Azure Managed Identity in Azure admin portal**.
1. Select **Copy storage account information**. If you want to view the information, select **Expand**.
1. Paste the information so it's easily accessible.
1. [Enable access to managed identity](#enable-access-to-storage-through-managed-identities).
1. Expand **Step 2 Update your connections** and select **Attempt connections updates**.

[!INCLUDE [footer-include](includes/footer-banner.md)]
