---
title: Connect to storage accounts behind firewalls
description: 'Azure Private Link: Set up secure connections to Data Lake Storage accounts behind firewalls. Learn how to configure private endpoints and keep your data protected.'
ms.date: 07/21/2025
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: alfergus
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:07/21/2025
---

# Connect to storage accounts behind firewalls

Sometimes you want Customer Insights – Data to connect to an Azure Data Lake Storage account that's behind a firewall. These are storage accounts where "Public network access" is disabled. To grant access to these storage accounts, you need to create a private endpoint.

:::image type="content" source="media/connect-to-storage-accounts-behind-firewalls/image1.png" alt-text="Screenshot of Azure Data Lake Storage account firewall settings.":::

There are three scenarios where Customer Insights – Data connects to Azure storage:

1. Instance output is written to your firewalled storage account.
1. Data source connects to a firewalled storage account (see [Data sources overview](data-sources.md)).
1. Data is exported to a firewalled storage account (see [Exports overview](export-destinations.md)).

> [!IMPORTANT]
> Regardless of a storage account's network access setting, if a storage account has any private link connections to it, Customer Insights - Data must also connect using a private link. This is due to Azure treating the storage account as if the public access has been disabled.

## Azure Virtual Network support for Power Platform

To connect Customer Insights – Data to a firewalled storage account, private endpoints must be configured to use **Azure Virtual Network support for Power Platform**. Using Azure Virtual Network support for Power Platform securely routes data between the storage account and Customer Insights – Data over your own virtual network.

When creating a data connection, the "Validate private endpoint" button shown when “This storage account is behind a firewall” is checked indicates whether the private endpoint exists. Ask your Power Platform and Azure administrators to configure private endpoints following the guidance in this article for all firewalled storage accounts you want to use in Customer Insights – Data.

### Prerequisites to enable Azure Virtual Network support for Power Platform

- The Power Platform environment associated with Customer Insights – Data must be a Managed Environment.
- Minimum role requirements
  - **Customer Insights – Data**: Administrator (required to create data connections).
  - **Power Platform**: Administrator (required to configure the Power Platform environment).
  - **Azure**: Administrator (required to create resources and private endpoints in Azure).

## Overview of enabling private endpoints

Private endpoints must be created in Azure before data connections can
be created in Customer Insights - Data. Once the Azure resources have
been created and permissions granted, adding private endpoints for
additional storage account becomes a relatively simple manual exercise.

**Power Platform administrator**

- Runs the ‘prepare’ script which determines the Power Platform region
  and creates specific steps for the Azure administrator to execute.
- The ‘prepare’ script does not make any environment changes.

**Azure administrator**

- Runs scripts using the information provided by the Power Platform
  administrator to create several resources (resource groups, Virtual
  network, subnet) and allows the Power Platform to request IP addresses
  from the subnets. This is a one-time task.
- Manually creates private endpoints in <https://Portal.Azure.com> for
  each storage container.

**Power Platform administrator**

- Runs a script which configures the Power Platform to use the new
  private endpoints.

**Customer Insights – Data administrator**

- Creates data connections, selecting “This storage account is behind a
  firewall”.
- If the private endpoints has been correction configured, the
  connection will

## Updating legacy private links

Instances with older private links will be prompted to update to private
endpoints with the message shown below.

<img src="media/connect-to-storage-accounts-behind-firewalls/image2.png" style="width:5.7716in;height:0.30556in" />

The See details button will show the Update private links dialog.

<img src="media/connect-to-storage-accounts-behind-firewalls/image3.png" style="width:5.01in;height:3.26in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

1. Click Copy storage accounts information to copy details to the clipboard.

2. Send the copied details to your Power Platform and Azure administrators, requesting the creation of private endpoints.

> <u>Wait for your Power Platform administrator and Azure administrator
> to confirm they have configured the private endpoints.</u>

3.  Once you have received confirmation the resources are ready to be
    used, you can then click the “Attempt connections update” button in
    Step 2 in this dialog to configure Customer Insights – Data to use
    the new private endpoints.

4.  When all connections show “Completed”, your update is done.

## Configuring private endpoints using Azure Virtual Network support for Power Platform 

### Customer Insights – Administrator steps

1.  Engage your Power Platform and Azure administrators.

2.  Provide this document and the storage accounts you want Customer
    Insights – Data to have access to.

3.  If you were prompted to update legacy private links, provide the
    information from the “Copy storage accounts information” link in
    ‘Update private links’ dialog.

4.  When you have received confirmation that private endpoints have been
    configured, you can proceed with creating or update data
    connections.

### Power Platform administrator steps

1.  Confirm the Power Platform environment is “Managed”. This is
    required.

    1.  Sign into <https://admin.powerplatform.com>

    2.  In Environment settings, “Managed environments” must be ‘Yes’  
        [Managed Environments overview - Power Platform \| Microsoft
        Learn](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview)

<!-- -->

5.  Download and extract the CI-Data script package to your machine  
    <https://download.microsoft.com/download/77c5dfb9-4555-4b30-9e96-08408855aab3/SubnetDelegationSetup.zip>

6.  Launch PowerShell and run the script:
    PrepareCIDataPrivateEndpoints.ps1

    1.  Navigate to the folder you extracted the scripts

    2.  Enter ./ PrepareCIDataPrivateEndpoints.ps1 and press enter.

    3.  When prompted, enter the EnvironmentID, Storage account name,
        and SubscriptionId provided by your Customer Insights – Data
        administrator.

7.  Copy the output and send to your Azure admin. They will use the
    details to create private endpoints.

<u>Wait for your Azure admin to confirm that private endpoints are ready
to be used.  
</u>

8.  After receiving confirmation from your Azure admin that private
    endpoints have been created, run the script command
    New-SubnetInjectionForPowerPlatformEnv.ps1 you generated in step 3
    to configure your Power Platform to use the new private endpoints.
    This will include your SubscriptionId and EnvironmentId as input
    parameters.

Notes

- You can safely Ignore a standard warning about verbs that are not
  discoverable.

- You will be prompted to sign in. Please follow your standard sign in
  process.

**Example script output**

<img src="media/connect-to-storage-accounts-behind-firewalls/image4.png" style="width:5.93358in;height:3.49941in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

## Azure administrator steps

When the Azure admin has received the “For Azure admin” details from the
Power Platform administrator, you can create the required resources and
private endpoints for the secured storage accounts that Customer
Insights – Data needs to access.

### Azure administrator creates resources using scripts

9.  Download and extract the CI-Data script package  
    (This is the same link scripts downloaded by the Power Platform
    admin)  
    [https://download.microsoft.com/download/77c5dfb9-4555-4b30-9e96-08408855aab3/SubnetDelegationSetup.zip  
    ](https://download.microsoft.com/download/77c5dfb9-4555-4b30-9e96-08408855aab3/SubnetDelegationSetup.zip)

<!-- -->

1.  Launch PowerShell and run the
    **Setup-SubnetDelegationForCiData.ps1** command provided to you by
    your Power Platform administrator. This will include your
    SubscriptionId and Power Platform Region.

> When the script is running, it will provide you values to enter.  
> For example, you will see a message similar to the below:  
>   
> Pass the parameters as printed below.
>
> .\SetupVnetForSubnetDelegation.ps1
>
> -virtualNetworkSubscriptionId: 44444444-0a57-4571-b790-666666666666
>
> -virtualNetworkName: cidata-subnetdelegation-eastus-resource-vnet
>
> -subnetName: cidata-delegated
>
> When prompted for each value, please enter the values provided.
>
> **What Setup-SubnetDelegationForCiData.ps1 does**

- Creates 1 or 2 Azure virtual networks - one in each Azure region used
  by your Power Platform region.  
  (Most Power Platform regions have a primary and secondary Azure
  region, while a few have only a primary.)

- Creates a sub-net in each virtual network.

- Delegates each subnet to the Power Platform to allow the Power
  Platform to request an IP in the subnet.

- Creates an enterprise policy which allows the Power Platform to find
  the subnets delegated to it.

2.  Manually create Private Endpoints

    - Sign in to azure portal

    - Using the storage account details provided by Power Platform
      admin, manually create private endpoints.

### Azure administrator creates private endpoints manually 

Using the “For Azure Admin” details provided by your Power Platform
administrator, manually create private endpoints for each storage
account.

- Each storage account requires at least 2 private endpoints (blob and
  dfs)

- If your Power Platform region has primary and secondary Azure regions,
  then you will create 4 private endpoints for each storage account – a
  blob and dfs private endpoint in each Azure region.

**Manually create private endpoints**

1.  Sign in to <https://Portal.azure.com>.

2.  Navigate to the first storage account.

3.  Under Security + networking, click Networking

4.  Click **+ Private endpoint** on the **Private endpoint connections**
    tab.  
    Use the following values provided:

> **Basics:** Subscription: The Azure subscription
>
> **Basics**: Resource group: The primary resource group provided
>
> **Basics**: Name: The recommended name, or a name of your choice.
>
> **Basics**: Region: The region provided.
>
> **Resource**: Target sub-resource: Blob or dfs as needed.
>
> **Virtual network:** Virtual network: Select the value provided

Click through defaults and click “Create”

Repeat these steps to create private endpoints for each storage account,
region, and target sub-resource as needed.

## Resources

Power Platform region to Azure regions mapping:  
[Virtual Network support overview – Supported
regions](https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview#supported-regions)

[!INCLUDE [footer-include](includes/footer-banner.md)]