---
title: Set up managed identities for storage accounts behind firewalls
description: Learn how to set up managed identities for Azure resources to connect your Data Lake Storage behind firewalls.
ms.date: 10/02/2024
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: mhart
ms.custom: bap-template
---

# Set up managed identities for storage accounts behind firewalls

You can have Customer Insights - Data connect to Azure storage protected by firewalls using managed identities for Azure resources. Managed identities for Azure provide improved connection security with a system-assigned managed identity that can't be accessed or used outside of its configured endpoints.

Configure Customer Insights - Data to connect with Azure storage containers protected by firewalls in the following scenarios:

- Data output - Configure Customer Insights - Data at setup to write processed customer insights output data to your private Azure storage container.
- Data input - Create data connections to ingest source data from your Azure storage containers.
- Exports - Configure exports to write specific tables to Azure storage containers.

<!--->
In Customers Insights you can create private links in the following ways:

- When creating a new Customer Insights - Data environment for which you would like to [Use your own Azure Data Lake Storage account](own-data-lake-storage.md) that is protected by your virtual network.
- When creating a [data source](connect-common-data-model.md) for which the data is stored in your protected account.
- Directly from the **Settings** > **Permissions** > **Private Links** page in Customer Insights - Data.

Regardless of the method you use to create the connection, it shows under the **Settings** > **Permissions** > **Private Links** tab in Customer Insights - Data.
--->
## Prerequisites

- You have an Azure subscription Owner role.
- You have access to the Power Platform admin center and Azure portal.
- The Azure storage account is in the same region as the Customer Insights – Data Dataverse environment.
- The [Dataverse environment ID](/power-platform/admin/determine-org-id-name#find-your-environment-and-organization-id).
- The [Azure subscription ID](/azure/azure-portal/get-subscription-tenant-id), location, and resource group name for each storage container.
- The [Azure CLI is download and installed](https://aka.ms/InstallAzureCliWindows).
- The following PowerShell modules are installed
  - Azure Az PowerShell module: `Install-Module -Name Az`
  - Azure Az.Resources PowerShell module: `Install-Module -Name Az.Resources`
  - Power Platform admin PowerShell module: `Install-Module -Name Microsoft.PowerApps.Administration.PowerShell`
- This [GitHub compressed file](https://github.com/microsoft/PowerApps-Samples/blob/master/powershell/managed-identities/Common.zip) is downloaded and extracted in a location where you can run PowerShell commands.

## Enable access to storage through managed identities

Perform these steps once per subscription.

1. [Enable the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#enable-enterprise-policy-for-the-selected-azure-subscription) for the Azure subscription.
1. [Create the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#create-enterprise-policy). One policy can be used for multiple Dataverse environments.
1. For each policy, [grant reader access to the enterprise policy](/power-apps/maker/data-platform/azure-synapse-link-msi#grant-reader-access-to-the-enterprise-policy-via-azure).
1. [Connect the enterprise policy to the Dataverse environment](/power-apps/maker/data-platform/azure-synapse-link-msi#connect-enterprise-policy-to-dataverse-environment). First, make sure there isn't an existing policy.
1. Grant enterprise policy access to Azure storage.
1. Allow enterprise policy access to the storage account behind the firewall.

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

<!--- Has this been updated? --->
## Set up a managed identity when creating a Customer Insights - Data environment

When creating a [Customer Insights - Data environment](create-environment.md) that connects to your virtual network protected storage:

1. Select **Enable Azure Private Link**.

   :::image type="content" source="media/Private-Endpoint-Creation.png" alt-text="Private endpoint creation.":::

1. Select **Create Private Link** to initiate the creation process.

1. [Approve the Private Link](#approve-your-private-link-in-the-azure-portal) in the Azure portal.

1. Once all links are approved, select **Validate Private Link**. Upon successful validation, you can continue configuring your new environment.

## Delete a managed identity

1. In Customer Insights - Data, go to **Settings** > **Permissions** and select the **Private Links** tab.

1. Select the storage account name for which you would like to delete the managed identity.

1. Select **Delete**.

[!INCLUDE [footer-include](includes/footer-banner.md)]
