---
title: Work with Customer Insights - Data and Microsoft Dataverse
description: Learn how to connect Customer Insights and Microsoft Dataverse and understand the output tables that are exported to Dataverse.
ms.date: 09/01/2023
ms.topic: conceptual
author: kishorem
ms.author: kishorem
ms.custom: bap-template
---

# Work with Customer Insights - Data and Microsoft Dataverse

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 Customer Insights - Data makes its output tables available in [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro). This integration enables easy data sharing and custom development through a low code/no code approach. The output tables are available as tables in a Dataverse environment. You can use the data for any other application based on Dataverse tables. These tables enable scenarios like automated workflows through Power Automate or building apps with Power Apps.

You can also [ingest data from on-premises data sources using Power Platform dataflows and gateways](connect-power-query.md#add-data-from-on-premises-data-sources) into your Dataverse environment.

## Prerequisites

- Customer Insights and Dataverse environments must be hosted in the same region.
- A global administrator role set up in the Dataverse environment. Verify if this [Dataverse environment is associated](/power-platform/admin/control-user-access#associate-a-security-group-with-a-dataverse-environment) to certain security groups and make sure you're added to those security groups.
- A Common Data Service/Dataverse [license is assigned](/power-platform/admin/create-users#to-assign-a-license) to you to get Read-Write access mode. Unlicensed administrators get Administrative access mode only.
- No other Customer Insights - Data environment already associated with the Dataverse environment you want to connect. Learn how to [remove an existing connection to a Dataverse environment](#remove-an-existing-connection-to-a-dataverse-environment).
- A Microsoft Dataverse environment connected to a single storage account if you configure the environment to [use your Azure Data Lake Storage](own-data-lake-storage.md).

## Dataverse storage capacity entitlement

A Customer Insights - Data subscription entitles you to extra capacity for your organization's existing [Dataverse storage capacity](/power-platform/admin/capacity-storage). The added capacity depends on the number of profiles that your subscription uses.

**Example:**

Assuming you get 15-GB database storage and 20-GB file storage per 100,000 customer profiles. If your subscription includes 300,000 customer profiles, your total storage capacity is 45 GB (3 x 15 GB) database storage and 60-GB file storage (3 x 20 GB). Similarly, if you have a B-to-B subscription with 30,000 accounts, your total storage capacity is 45 GB (3 x 15 GB) database storage, and 60-GB file storage (3 x 20 GB).

Log capacity isn't incremental and fixed for your organization.

For more information about the detailed capacity entitlements, see [Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/?LinkId=866544).

## Connect a Dataverse environment to Customer Insights - Data

The **Microsoft Dataverse** step lets you connect Customer Insights - Data with your Dataverse environment while [creating an environment](create-environment.md).

:::image type="content" source="media/dataverse-provisioning.png" alt-text="data sharing with Microsoft Dataverse auto-enabled for new environments.":::

1. Provide the URL to your Dataverse environment or leave blank to have one created for you.

   [Power Platform admins can control who can create a new Dataverse environments](/power-platform/admin/control-environment-creation). If you're trying to set up a new environment and can't, the admin might have disabled the creation of Dataverse environments for everyone except admins.

1. If you're using your own Data Lake Storage account:
   1. Select **Enable data sharing** with Dataverse.
   1. Enter the **Permissions identifier**. To get the permission identifier, [enable data sharing with Dataverse from your own Azure Data Lake Storage](#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview).

## Enable data sharing with Dataverse from your own Azure Data Lake Storage (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

In [your own Azure Data Lake Storage account](own-data-lake-storage.md), verify the user who sets up the Customer Insights - Data environment has at least **Storage Blob Data Reader** permissions on the `customerinsights` container in the storage account.

> [!NOTE]
> Data sharing is applicable only if you use your own Azure Data Lake Storage account. This setting isn't available if the environment uses the default Dataverse storage.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

### Limitations

- Only one-to-one mapping between a Dataverse organization and an Azure Data Lake Storage account. Once a Dataverse organization is connected to a storage account, it can't connect to another storage account. This limitation prevents Dataverse from populating multiple storage accounts.
- Data sharing won't work if an Azure Private Link setup is needed to access your Azure Data Lake Storage account because it's behind a firewall. Dataverse currently doesn't support the connection to private endpoints through Private Link.

### Set up security groups on your own Azure Data Lake Storage

1. Create two security groups on your Azure subscription - one **Reader** security group and one **Contributor** security group and set the Microsoft Dataverse service as the owner for both security groups.

1. Manage the Access Control List (ACL) on the `customerinsights` container in your storage account through these security groups.
   1. Add the Microsoft Dataverse service and any Dataverse-based business applications like Dynamics 365 Marketing to the **Reader** security group with **read-only** permissions.
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
   - `ByolSetup.ps1`: Requires Storage Blob Data Owner permissions at the storage account/container level. This script will create the permission for you. Your role assignment can be removed manually after successfully running the script.

1. Execute `CreateSecurityGroups.ps1` in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage. Open the PowerShell script in an editor to review additional information and the implemented logic.

   This script creates two security groups on your Azure subscription: one for the Reader group and another for the Contributor group. Microsoft Dataverse service is the owner for both these security groups.

1. Save both the security group ID values generated by this script to use in the `ByolSetup.ps1` script.

   > [!NOTE]
   > Security group creation can be disabled on your tenant. In that case, a manual setup would be needed and your Azure AD admin would have to [enable security group creation](/azure/active-directory/enterprise-users/groups-self-service-management).

1. Execute `ByolSetup.ps1` in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage, storage account name, resource group name, and the Reader and Contributor security group ID values. Open the PowerShell script in an editor to review additional information and the implemented logic.

   This script adds the required role-based access control for the Microsoft Dataverse service and any Dataverse-based business applications. It also updates the Access Control List (ACL) on the `customerinsights` container for the security groups created with the `CreateSecurityGroups.ps1` script. The Contributor group is given *rwx* permission and Readers group is given *r-x* permission only.

1. Copy the output string that looks like: `https://DVBYODLDemo/customerinsights?rg=285f5727-a2ae-4afd-9549-64343a0gbabc&cg=720d2dae-4ac8-59f8-9e96-2fa675dbdabc`

1. Enter the copied output string into the **Permissions identifier** field of the environment configuration step for Microsoft Dataverse.

   :::image type="content" source="media/dataverse-enable-datasharing-BYODL.png" alt-text="Configuration options to enable data sharing from your own Azure Data Lake Storage with Microsoft Dataverse.":::

## Remove an existing connection to a Dataverse environment

When connecting to a Dataverse environment, the error message **This CDS organization is already attached to another Customer Insights instance** means that the Dataverse environment is already used in a Customer Insights - Data environment. You can remove the existing connection as a global administrator on the Dataverse environment. It can take a couple of hours to populate the changes.

1. Go to [Power Apps](https://make.powerapps.com).
1. Select the environment from the environment picker.
1. If you have Dynamics 365 Customer Insights - Journeys installed on the Dataverse environment, and you have [it connected to your Customer Insights - Data environment](/dynamics365/marketing/real-time-marketing-ci-profile), remove this connection first. Otherwise, skip this step and proceed to step 4.
    1. Go to **Tables**.
    1. Find the table *msdynmkt_configuration*.
    1. Go to the *CXPConfig* row in this table.
    1. Go to the *Customer Insights Status* column and change the value from *Configured* to *NotConfigured*.
    1. Go to **Solutions**.
    1. Uninstall the following Dynamics 365 Marketing solutions:
        - DynamicsMKT_AttachCIApplicationUser (*DynamicsMKT_AttachCIApplicationUser*)
        - Dynamics Marketing Consent For Customer Insights (*DynamicsMKT_ConsentAttachCI*)
        - DynamicsMKT_OrchestrationEngineAttachCI (*DynamicsMKT_OrchestrationEngineAttachCI*)
1. Go to **Solutions**.
1. Uninstall the following Customer Insights solutions:
   - Dynamics 365 Customer Insights Base (*msdyn_CustomerInsightsAnchor*)
   - Dynamics 365 Customer Insights Data Tables (*msdyn_CustomerInsightsDataTables*)
   - Dynamics 365 Customer Insights (*msdyn_CustomerInsights*)
   - Dynamics 365 Customer Insights Customer Card (*CustomerInsightsCustomerCard*)
   - Dynamics 365 Customer Insights Prod First Party App User Management (*msdyn_CustomerInsightsAppUserManagementProd*)

If the removal of the connection fails due to dependencies, you need to remove the dependencies too. For more information, see [Removing dependencies](/power-platform/alm/removing-dependencies).

## Output tables in Dataverse

Some output tables are available in Dataverse. For more information, see [Customer Insights - Data tables in Dataverse](tables.md#customer-insights-tables-in-dataverse).

[!INCLUDE [footer-include](includes/footer-banner.md)]
