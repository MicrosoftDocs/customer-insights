---
title: Set up managed identities for storage accounts behind firewalls
description: Learn how to set up managed identities for Azure resources to connect your Data Lake Storage behind firewalls.
ms.date: 10/17/2024
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: mhart
ms.custom: bap-template
---

# Set up managed identities for storage accounts behind firewalls

If you have Azure storage protected by firewalls, use managed identities for Azure resources to connect to Customer Insights - Data. Managed identities provide an automatically managed identity in Microsoft Entra ID for applications, such as Customer Insights - Data, to use when connecting to resources that support Microsoft Entra authentication. The managed identity can't be accessed or used outside of its configured endpoints. Learn more in [Managed identities for Azure resources](/entra/identity/managed-identities-azure-resources).

There are three scenarios where Customer Insights - Data can be configured to connect to firewall-protected Azure storage containers:

- Output storage can be configured at setup to use your own Azure data lake.
- Data sources that read from an Azure data lake storage, Common Data Models (CDM), Delta tables, or Synapse.
- Exports that write to an Azure data lake.

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

Existing Azure Private Links must be updated to managed identities for Azure resources by November 30, 2024. Customer Insights - Data provides the information your Azure subscription owner needs to enable managed identities. If you're unable to update your instance by the deadline, request a 30 day extension at CIDManagedIdentity@Microsoft.com.

An *Action required* banner tells you that you have one or more storage accounts that must be upgraded to meet security requirements. In the banner, select **See details**.

   :::image type="content" source="media/upgrade-to-managed-id.png" alt-text="Screenshot showing the 'Action required' banner and message box to upgrade to managed identities for Azure.":::

1. Expand **Step 1: Enable Azure Managed Identity in Azure admin portal**.

   - Select **Copy storage account information**. All the information required for migration is copied. Send the information to your Azure subscription owner to enable managed identities. If you want to view the connection details, select **Expand**.

   - When your Azure subscription owner confirms they enabled managed identities for Azure access, go to step 2 to update your connections.

1. Expand **Step 2: Update your connections**, and then select **Attempt connections updates**. Wait for the connections to be updated. If an error occurs, contact your Azure subscription owner.

### FAQ

#### Why are we doing this?

Managed identities for Azure resources is the new recommended way to connect to Azure resources behind a firewall using a restricted service principal that can only be used between two designated endpoints. The credentials for the service principal can't be exported or viewed.

#### Where can I learn more about managed identities for Azure resources? 

Go to [Managed identities for Azure resources](/entra/identity/managed-identities-azure-resources/overview).

#### How do I enable managed identity for Azure resources access to storage containers?

The Azure subscription owner enables managed identities in the Azure CLI using a script provided by Microsoft. Go to [Set up managed identities for storage accounts behind firewalls](#set-up-managed-identities-for-storage-accounts-behind-firewalls).

#### How do I configure connections in Customer Insights - Data to use managed identities for Azure resources?

Select **This storage account is behind a firewall** when creating a connection. The storage container must exist and be configured to allow access via managed identities for Azure resources before the data connection can be saved.

#### We have other products that use private links to these containers. Will they continue to function after we move to managed identities? 

Yes, existing private links will continue to function. If you no longer need them, we recommend removing the private links in Azure after moving to managed identities.

#### I’m still seeing "Enable private links" in my instance.

Instances where connections show **Enable private links** will be updated soon. Your instance is ready to use managed identities when new data connections show **This storage account is behind a firewall**.

#### What are the scenarios in Customer Insights – Data that use managed identities for Azure?

There are three scenarios where CI-Data connects to an Azure data lake that can be behind a firewall:

1. Output storage. At setup, the instance primary output can be configured to be your own data lake.
1. Data sources using Azure data lake storage with CDM tables, Delta tables, or Synapse.
1. Exports that write to an Azure data lake.

#### How do we request an extension?

Send extension requests to CIDManagedIdentity@Microsoft.com. Include all Customer Insights – Data InstanceIDs (located on the URL) in the request.

For other questions, contact CIDManagedIdentity@Microsoft.com.


[!INCLUDE [footer-include](includes/footer-banner.md)]
