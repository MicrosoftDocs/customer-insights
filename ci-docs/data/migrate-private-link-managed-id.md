---
title: Migrate private links to managed identities for Azure resources
description: Learn how to upgrade Azure Private Links to managed identities for Azure resources in Customer Insights - Data.
ms.date: 10/01/2024
ms.reviewer: v-smithwendy
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Migrate Private Links to managed identities for Azure resources

This article explains how to update existing data connections using Private Links to managed identities for Azure resources. Private links were previously used to grant access to Azure storage behind a firewall. Managed identities for Azure provide improved connection security with a system-assigned managed identity that can't be accessed or used outside of its configured endpoints.

## Prerequisites

- You have an Azure subscription Owner role.
- The Azure storage account is in the same region as the Customer Insights – Data Dataverse environment.
- The [Azure CLI is download and installed](https://aka.ms/InstallAzureCliWindows).
- The following PowerShell modules are installed
  - Azure Az PowerShell module: `Install-Module -Name Az`
  - Azure Az.Resources PowerShell module: `Install-Module -Name Az.Resources`
  - Power Platform admin PowerShell module: `Install-Module -Name Microsoft.PowerApps.Administration.PowerShell`
- This [GitHub compressed file](https://github.com/microsoft/PowerApps-Samples/blob/master/powershell/managed-identities/Common.zip) is downloaded and extracted in a location where you can run PowerShell commands.

## Upgrade to managed identities

1. Sign in to Customer Insights - Data.
   A message says that you have one or more storage accounts that must be upgraded.
1. From the Action required message, select **See details**.
   :::image type="content" source="media/upgrade-to-managed-id.jpg" alt-text="Dialog box to upgrade to managed identities for Azure.":::
1. Expand **Step 1 Enable Azure Managed Identity in Azure admin portal**.
1. Select **Copy storage account information**. If you want to view the information, select **Expand**.
1. Paste the information so it's easily accessible.
1. Enable access to managed identity.
1. Expand **Step 2 Update your connections** to view the status of your connections.

## Enable access to storage through managed identities

Perform these steps once per subscription.

1. [Enable the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#enable-enterprise-policy-for-the-selected-azure-subscription) for the Azure subscription.
1. [Create the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#create-enterprise-policy). One policy can be used for multiple Dataverse environments.
1. For each policy, [grant reader access to the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#grant-reader-access-to-the-enterprise-policy-via-azure).
1. [Connect the enterprise policy to the Dataverse environment](/power-apps/maker/data-platform/azure-synapse-link-msi#connect-enterprise-policy-to-dataverse-environment). First, make sure there isn't an existing policy.
1. [Grant enterprise policy access](#grant-enterprise-policy-access-to-azure-storage) to Azure storage.
1. [Allow enterprise policy access](#allow-enterprise-policy-access-to-the-storage-account-behind-the-firewall) to the storage account behind the firewall.

### Grant enterprise policy access to Azure storage

Perform these steps for each storage account or container.

1. Sign in to the [Azure portal](https://portal.azure.com/).
1. Open the storage account connected to your Dataverse environment.
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

[!INCLUDE [footer-include](includes/footer-banner.md)]
