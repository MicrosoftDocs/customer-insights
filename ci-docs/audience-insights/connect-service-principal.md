---
title: "Connect to an Azure Data Lake Storage account by using a service principal"
description: "Use an Azure service principal to connect to your own data lake."
ms.date: 07/23/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: adkuppa
ms.author: adkuppa
ms.reviewer: mhart
manager: shellyha
---

# Connect to an Azure Data Lake Storage account by using an Azure service principal
<!--note from editor: The Cloud Style Guide would have us just use "Azure Data Lake Storage" to mean the current version, unless the old version (Gen1) is mentioned. I've followed this guidance, even though it seems that our docs and Azure docs are all over the map on this.-->
Automated tools that use Azure services should always have restricted permissions. Instead of having applications sign in as a fully privileged user, Azure offers service principals. Read on to learn how to connect Dynamics 365 Customer Insights with an Azure Data Lake Storage account by using an Azure service principal instead of storage account keys. 

You can use the service principal to securely [add or edit a Common Data Model folder as a data source](connect-common-data-model.md), or [create or update an environment](get-started-paid.md).<!--note from editor: Suggested. Or it could be ", or create a new environment or update an existing one". I think "new" is implied with "create". The comma is necessary.-->

> [!IMPORTANT]
> - The Data Lake Storage account that will use<!--note from editor: Suggested. Or perhaps it could be "The Data Lake Storage account to which you want to give access to the service principal..."--> the service principal must have [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace).
> - You need admin permissions for your Azure subscription to create the service principal.

## Create an Azure service principal for Customer Insights

Before creating a new service principal for audience insights or engagement insights, check whether it already exists in your organization.

### Look for an existing service principal

1. Go to the [Azure admin portal](https://portal.azure.com) and sign in to your organization.

2. From **Azure services**, select **Azure Active Directory**.

3. Under **Manage**, select **Enterprise Applications**.

4. Search for the Microsoft<!--note from editor: Via Microsoft Writing Style Guide.--> application ID:
   - Audience insights: `0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff` with the name `Dynamics 365 AI for Customer Insights`
   - Engagement insights: `ffa7d2fe-fc04-4599-9f6d-7ca06dd0c4fd` with the name `Dynamics 365 AI for Customer Insights engagement insights`

5. If you find a matching record, it means that the service principal already exists. 
   
   :::image type="content" source="media/ADLS-SP-AlreadyProvisioned.png" alt-text="Screenshot showing an existing service principal.":::
   
6. If no results are returned, create a new service principal.

>[!NOTE]
>To make use of the full power of Dynamics 365 Customer Insights, we suggest that you add both apps to the service principal.<!--note from editor: Using the note format is suggested, just so this doesn't get lost by being tucked up in the step.-->

### Create a new service principal
<!--note from editor: Some general formatting notes: The MWSG wants bold for text the user enters (in addition to UI strings and the settings users select), but there's plenty of precedent for using code format for entering text in PowerShell so I didn't change that. Note that italic should be used for placeholders, but not much else.-->
1. Install the latest version of Azure Active Directory PowerShell for Graph. For more information, go to [Install Azure Active Directory PowerShell for Graph](/powershell/azure/active-directory/install-adv2).

   1. On your PC, select the Windows key on your keyboard and search for **Windows PowerShell** and select **Run as administrator**.<!--note from editor: Or should this be something like "search for **Windows PowerShell** and, if asked, select **Run as administrator**."?-->
   
   1. In the PowerShell window that opens, enter `Install-Module AzureAD`.

2. Create the service principal for Customer Insights with the Azure AD PowerShell module.

   1. In the PowerShell window, enter `Connect-AzureAD -TenantId "[your tenant ID]" -AzureEnvironmentName Azure`. Replace *"[your tenant ID]"*<!--note from editor: Edit okay? Or should the quotation marks stay in the command line, in which case it would be "Replace *[your tenant ID]* --> with the actual ID of your tenant where you want to create the service principal. The environment name parameter, `AzureEnvironmentName`, is optional.
  
   1. Enter `New-AzureADServicePrincipal -AppId "0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff" -DisplayName "Dynamics 365 AI for Customer Insights"`. This command creates the service principal for audience insights on the selected tenant. 

   1. Enter `New-AzureADServicePrincipal -AppId "ffa7d2fe-fc04-4599-9f6d-7ca06dd0c4fd" -DisplayName "Dynamics 365 AI for Customer Insights engagement insights"`. This command creates the service principal for engagement insights<!--note from editor: Edit okay?--> on the selected tenant.

## Grant permissions to the service principal to access the storage account

Go to the Azure portal to grant permissions to the service principal for the storage account you want to use in audience insights.

1. Go to the [Azure admin portal](https://portal.azure.com) and sign in to your organization.

1. Open the storage account you want the service principal for audience insights to have access to.

1. On the left pane, select **Access control (IAM)**, and then select **Add** > **Add role assignment**.

   :::image type="content" source="media/ADLS-SP-AddRoleAssignment.png" alt-text="Screenshot showing the Azure portal while adding a role assignment.":::

1. On the **Add role assignment** pane, set the following properties:
   - Role: **Storage Blob Data Contributor**
   - Assign access to: **User, group, or service principal**
   - Select: **Dynamics 365 AI for Customer Insights** and **Dynamics 365 AI for Customer Insights engagement insights** (the two [service principals](#create-a-new-service-principal) you created earlier in this procedure)

1.	Select **Save**.

It can take up to 15 minutes to propagate the changes.

## Enter the Azure resource ID or the Azure subscription details in the storage account attachment to audience insights

You can<!--note from editor: Edit suggested only if this section is optional.--> attach a Data Lake Storage account in audience insights to [store output data](manage-environments.md) or [use it as a data source](connect-common-data-service-lake.md). This option lets you choose between a resource-based or a subscription-based approach. Depending on the approach you choose, follow the procedure in one of the following sections.<!--note from editor: Suggested.-->

### Resource-based storage account connection

1. Go to the [Azure admin portal](https://portal.azure.com), sign in to your subscription, and open the storage account.

1. On the left pane, go to **Settings** > **Properties**.

1. Copy the storage account resource ID value.

   :::image type="content" source="media/ADLS-SP-ResourceId.png" alt-text="Copy the storage account resource ID.":::

1. In audience insights, insert the resource ID in the resource field displayed on the storage account connection screen.

   :::image type="content" source="media/ADLS-SP-ResourceIdConnection.png" alt-text="Enter the storage account resource ID information.":::   

1. Continue with the remaining steps in audience insights to attach the storage account.

### Subscription-based storage account connection

1. Go to the [Azure admin portal](https://portal.azure.com), sign in to your subscription, and open the storage account.

1. On the left pane, go to **Settings** > **Properties**.

1. Review the **Subscription**, **Resource group**, and the **Name** of the storage account to make sure you select the right values in audience insights.

1. In audience insights, choose the values for the corresponding fields when attaching the storage account.

1. Continue with the remaining steps in audience insights to attach the storage account.


[!INCLUDE[footer-include](../includes/footer-banner.md)]