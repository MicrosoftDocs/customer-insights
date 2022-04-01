---
title: "Create and manage environments"
description: "Learn how to sign up for the service and how to manage environments."
ms.date: 03/28/2022
ms.subservice: audience-insights
ms.topic: how-to
ms.reviewer: mhart
author: adkuppa
ms.author: adkuppa
manager: shellyha
searchScope: 
  - ci-system-about
  - customerInsights
---

# Manage environments

## Switch environments

Select the **Environment** control in the upper-right corner of the page to change environments.

:::image type="content" source="media/home-page-environment-switcher.png" alt-text="Screenshot of the control to switch environments.":::

Administrators can [create](create-environment.md) and manage environments.

## Edit an existing environment

You can edit some of the details of existing environments.

1.	Select the **Environment** picker in the header of the app.

2.	Select the **Edit** icon.

3. In the **Edit environment** box, you can update the environment settings.

For more information on environment settings, see [Create a new environment](create-environment.md).

## Connect to Microsoft Dataverse
   
The **Microsoft Dataverse** step lets you connect Customer Insights with your Dataverse environment. 

Provide your own Microsoft Dataverse environment to share data (profiles and insights) with business applications based on Dataverse, like Dynamics 365 Marketing or model-driven applications in Power Apps.

To use [out-of-box prediction models](predictions-overview.md#out-of-box-models), configure data sharing with Dataverse. Or you can enable data ingestion from on-premises data sources, providing the Microsoft Dataverse environment URL that your organization administers.

Enabling data sharing with Microsoft Dataverse by selecting the data sharing checkbox will trigger a one time full refresh of your data sources and all other processes.

> [!IMPORTANT]
> 1. Customer Insights and Dataverse have to be in the same region to enable data sharing.
> 1. You must have a global administrator role in the Dataverse environment. Verify if this [Dataverse environment is associated](/power-platform/admin/control-user-access#associate-a-security-group-with-a-dataverse-environment) to certain security groups and make sure you are added to those security groups.
> 1. No existing Customer Insights environment is already associated with that Dataverse environment. Learn how to [remove an existing connection to a Dataverse environment](#remove-an-existing-connection-to-a-dataverse-environment).

:::image type="content" source="media/dataverse-enable-datasharing.png" alt-text="Configuration options to enable data sharing with Microsoft Dataverse.":::

### Enable data sharing with Dataverse from your own Azure Data Lake Storage (Preview)

If your environment is configured to use your own Azure Data Lake Storage to store Customer Insights data, enabling data sharing with Microsoft Dataverse needs some extra configuration.

1. Create two security groups on your Azure subscription - one **Reader** security group and one **Contributor** security group and set the Microsoft Dataverse service as the owner for both security groups.
2. Manage the Access Control List (ACL) on the CustomerInsights container in your storage account via these security groups. Add the Microsoft Dataverse service and any Dataverse-based business applications like Dynamics 365 Marketing to the **Reader** security group with **read-only** permissions. Add *only* the Customers Insights application to the **Contributor** security group to grant both **read and write** permissions to write profiles and insights.
   
#### Prerequisites

To execute the PowerShell scripts you need to have the following three modules imported. 

1. Install the latest version of [Azure Active Directory PowerShell for Graph](/powershell/azure/active-directory/install-adv2).
   1. On your PC, select the Windows key on your keyboard and search for **Windows PowerShell** and select **Run as administrator**.
   1. In the PowerShell window that opens, enter `Install-Module AzureAD`.
2. Import three modules.
    1. In the PowerShell window, enter `Install-Module -Name Az.Accounts` and follow the steps. 
    1. Repeat for `Install-Module -Name Az.Resources` and `Install-Module -Name Az.Storage`.

#### Configuration steps

1. Download the two PowerShell scripts you need to run from our engineer's [GitHub repo](https://github.com/trin-msft/byol).
    1. `CreateSecurityGroups.ps1`
       - You need *tenant admin* permissions to run this PowerShell script. 
       - This PowerShell script creates two security groups on your Azure subscription. One for the Reader group and another for the Contributor group and will make Microsoft Dataverse service as the owner for both these security groups.
       - Execute this PowerShell script in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage. Open the PowerShell script in an editor to review additional information and the logic implemented.
       - Save both the security group ID values generated by this script because we'll use them in the `ByolSetup.ps1` script.
       
        > [!NOTE]
        > Security group creation can be disabled on your tenant. In that case, a manual setup would be needed and your Azure AD admin would have to[ enable security group creation](/azure/active-directory/enterprise-users/groups-self-service-management).

    2. `ByolSetup.ps1`
        - You need *Storage Blob Data Owner* permissions at the storage account/container level to run this script or this script will create one for you. Your role assignment can be removed manually after successfully running the script.
        - This PowerShell script adds the required tole-based access control (RBAC) for the Microsoft Dataverse service and any Dataverse-based business applications. It also updates the Access Control List (ACL) on the CustomerInsights container for the security groups created with the `CreateSecurityGroups.ps1` script. The Contributor group will have *rwx* permission and Readers group will have *r-x* permission only.
        - Execute this PowerShell script in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage, storage account name, resource group name, and the Reader and Contributor security group id values. Open the PowerShell script in an editor to review additional information and the logic implemented.
        - Copy the output string after successfully running the script. The output string looks like this: `https: //DVBYODLDemo/customerinsights?rg=285f5727-a2ae-4afd-9549-64343a0gbabc&cg=720d2dae-4ac8-59f8-9e96-2fa675dbdabc`
        
2. Enter the output string copied from above into the **Permissions identifier** field of the environment configuration step for Microsoft Dataverse.

:::image type="content" source="media/dataverse-enable-datasharing-BYODL.png" alt-text="Configuration options to enable data sharing from your own Azure Data Lake Storage with Microsoft Dataverse.":::

Customer Insights does not support the following data sharing scenarios:
- If you enable data sharing with Dataverse, you won't be able to [create predicted or missing values in an entity](predictions.md).
- If you enable data sharing with Dataverse, you won't be able to view any optional PowerBI Embedded reports in your Customer Insights environment.

### Remove an existing connection to a Dataverse environment

When connecting to a Dataverse environment, the error message **This CDS organization is already attached to another Customer Insights instance** means that the Dataverse environment is already used in a Customer Insights environment. You can remove the existing connection as a global administrator on the Dataverse environment. It can take a couple of hours to populate the changes.

1. Go to [Power Apps](https://make.powerapps.com).
1. Select the environment from the environment picker.
1. Go to **Solutions**
1. Uninstall or delete the solution named **Dynamics 365 Customer Insights Customer Card Add-in (Preview)**.

OR 

1. Open your Dataverse environment.
1. Go to **Advanced Settings** > **Solutions**.
1. Uninstall the **CustomerInsightsCustomerCard** solution.

## Copy the environment configuration

As an admin, you can choose to copy the configuration from an existing environment when you create a new one. 

:::image type="content" source="media/environment-settings-dialog.png" alt-text="Screenshot of the settings options in the environment settings.":::

You'll see a list of all available environments in your organization where you can copy data from.

The following configuration settings are copied:

- Ingested/imported data sources
- Data unification configuration
- Segments
- Measures
- Relationships
- Activities
- Search & filter Index
- Export destinations
- Scheduled refresh
- Enrichments
- Model management
- Role assignments

## Set up a copied environment

When you copy the environment configuration, the following data is *not* copied:

- Customer profiles.
- Data source credentials. You'll have to provide the credentials for every data source and refresh the data sources manually.
- Data sources from the Common Data Model folder and Dataverse-managed data lake. You'll have to create those data sources manually with the same name as in the source environment.
- Connection secrets that are used for exports and enrichments. You have to reauthenticate the connections and then reactivate enrichments and exports. 

When you copy an environment, you'll see a confirmation message that the new environment has been created. Select **Go to data sources** to see the list of data sources.

All the data sources will show a **Credentials Required** status. Edit the data sources and enter the credentials to refresh them.

:::image type="content" source="media/data-sources-copied.png" alt-text="List of data sources that were copied and need authentication.":::

After refreshing the data sources, go to **Data** > **Unify**. Here you'll find settings from the source environment. Edit them as needed or select **Run** to start the data unification process and create the unified customer entity.

When the data unification is complete, go to **Measures** and **Segments** to refresh them too.

Before you reactivate exports and enrichments, go to **Admin** > **Connections** to reauthenticate the connections in your new environment.

## Change the owner of an environment

While several users can have admin permissions in Customer Insights, only one user is the owner of an environment. By default, it's the admin who creates an environment initially. As the admin of an environment, you can assign ownership to another user with admin permissions.

1. Select the **Environment** picker in the header of the app.

1. Select the **Edit** icon.

1. In the **Edit environment** box, go to the **Basic information** step.

1. In the **Change owner of environment** field, choose the new owner of the environment.  

1. Select **Review and finish**, then **Update** to apply the changes. 

## Claim ownership of an environment

If the owner of an environment leaves the organization or their user account is deleted, the environment will have no owner. A user with admin permissions can claim the ownership and become the new owner. They can continue to own the environment or [change the ownership to another admin](#change-the-owner-of-an-environment). 

To claim ownership, select the **Take ownership** button that shows at the top of every page in Customer Insights when the original owner left the organization.

## Reset an existing environment

As the owner of an environment, you can reset an environment to an empty state if you want to delete all configurations and remove the ingested data.

1.	Select the **Environment** picker in the header of the app. 

2.	Select the environment you want to reset and select the ellipsis (**...**). 

3. Choose the **Reset** option. 

4.	To confirm the deletion, enter the environment name and select **Reset**.

## Delete an existing environment

As the owner of an environment, you can delete an environment you administer.

1.	Select the **Environment** picker in the header of the app.

2.	Select the environment you want to reset and select the ellipsis (**...**). 

3. Choose the **Delete** option. 

4.	To confirm the deletion, enter the environment name and select **Delete**.

> [!NOTE]
> Deleting an environment does not remove the association to a Dataverse environment.Learn how to [remove an existing connection to a Dataverse environment](#remove-an-existing-connection-to-a-dataverse-environment).


[!INCLUDE[footer-include](../includes/footer-banner.md)]
