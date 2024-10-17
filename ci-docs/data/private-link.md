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

If you have Azure storage protected by firewalls, use managed identities for Azure resources to connect to Customer Insights - Data. Managed identities provide an automatically managed identity in Microsoft Entra ID for applications, such as Customer Insights - Data, to use when connecting to resources that support Microsoft Entra authentication. The managed identity can't be accessed or used outside of its configured endpoints. Learn more in [Managed identities for Azure resources](/entra/identity/managed-identities-azure-resources).

The following scenarios are appropriate for configuring Customer Insights - Data to use managed identities to connect to firewall-protected Azure storage containers:

- Configure Customer Insights - Data at setup to write processed customer insights output data to your private Azure storage container.
- Create data connections to ingest source data from your Azure storage containers.
- Configure exports to write specific tables to Azure storage containers.

If you use Azure Private Link, review the [prerequisites](#prerequisites) and then [migrate your private links to managed identities](#migrate-private-links-to-managed-identities-for-azure-resources).

## Prerequisites

- You have an Azure Subscription Owner role.
- You have access to the Power Platform admin center and Azure portal.
- The Azure storage account is in the same region as the Customer Insights – Data Dataverse environment.
- You have the Dataverse environment ID for Customer Insights - Data. [Edit the environment](manage-environments.md#edit-an-existing-environment) to get the Customers Insights - Data environment URL. Then, browse to the URL and [get the environment ID from the Power Platform admin center](/power-platform/admin/determine-org-id-name#find-your-environment-and-organization-id).
- You have the [Azure subscription ID](/azure/azure-portal/get-subscription-tenant-id), location, and resource group name for each storage container.
- The [Azure CLI is downloaded and installed](https://aka.ms/InstallAzureCliWindows).
- The following PowerShell modules are installed:
  - Azure Az PowerShell module: `Install-Module -Name Az`
  - Azure Az.Resources PowerShell module: `Install-Module -Name Az.Resources`
  - Power Platform admin PowerShell module: `Install-Module -Name Microsoft.PowerApps.Administration.PowerShell`
- You have downloaded and extracted the [managed identities GitHub compressed file](https://github.com/microsoft/PowerApps-Samples/blob/master/powershell/managed-identities/Common.zip) in a location where you can run PowerShell commands.

## Enable access to storage through managed identities

Perform these steps once per subscription.

1. Determine if an enterprise policy for the Dataverse environment exists. Run the script: `GetIdentityEnterprisePolicyForEnvironment`

    If a policy exists, get the policy ID and skip to step 5. If no enterprise policy exists, continue with the following steps.

1. [Enable the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#enable-enterprise-policy-for-the-selected-azure-subscription) for the Azure subscription.

1. [Create the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#create-enterprise-policy). One policy can be used for multiple Dataverse environments.

1. [Grant reader access to the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#grant-reader-access-to-the-enterprise-policy-via-azure).

1. [Connect the enterprise policy to the Dataverse environment](/power-apps/maker/data-platform/azure-synapse-link-msi#connect-enterprise-policy-to-dataverse-environment).

### Grant enterprise policy access to Azure storage

Perform these steps for each storage account or container.

1. Sign in to the [Azure portal](https://portal.azure.com/).

1. Open the storage account that you want to connect. To grant access to a specific container, go to **Containers** under **Data storage** and select the container.

1. On the left navigation pane, select **Access Control (IAM)**.

1. Select the **Role assignments** tab. Select **Add** > **Add role assignment**.

1. Search for and select **Storage Blob Data Contributor**.

1. Select the **Members** tab. Under **Assign access to**, select **Managed identity**.

1. Select **Select members**, select the correct subscription, and then select the **microsoft.powerplatform/enterprisepolicies[Identity]** option.

1. Select the enterprise policy that you created, and then select **Save**.

### Allow enterprise policy access to the storage account behind the firewall

1. Open the storage account in the Azure portal.

1. Select the **Networking** tab.

1. Select **Enabled from selected virtual networks and IP addresses**.

1. For the **Resource type**, select **Microsot.PowerPlatform/enterprisePolicies** and the instance name for the enterprise policy.

1. Select **Save**.

## Migrate private links to managed identities for Azure resources

Change the data connections that use Azure Private Link to use managed identities for Azure resources.

1. Sign in to Customer Insights - Data.

1. An *Action required* banner tells you that you have one or more storage accounts that must be upgraded to meet security requirements. In the banner, select **See details**.

   :::image type="content" source="media/upgrade-to-managed-id.jpg" alt-text="Screenshot showing the 'Action required' banner and message box to upgrade to managed identities for Azure.":::

1. Expand **Step 1: Enable Azure Managed Identity in Azure admin portal**.

1. Select **Copy storage account information**. All the information required for migration is copied. Send the information to your Azure subscription owner to enable managed identities. If you want to view the connection details, select **Expand**.

1. When your Azure subscription owner confirms they enabled managed identities for Azure access, [Enable access to managed identities](#enable-access-to-storage-through-managed-identities).

1. Expand **Step 2: Update your connections**, and then select **Attempt connections updates**.

1. Wait for the connections to be updated. If an error occurs, contact your Azure subscription owner.

[!INCLUDE [footer-include](includes/footer-banner.md)]
