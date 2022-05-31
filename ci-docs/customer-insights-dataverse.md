---
title: Work with Customer Insights data in Microsoft Dataverse
description: "Use Customer Insights entities as tables in Microsoft Dataverse."
ms.date: 05/30/2022
ms.reviewer: mhart
ms.subservice: audience-insights
ms.topic: conceptual
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
searchScope: 
  - ci-system-diagnostic
  - customerInsights
---

# Work with Customer Insights data in Microsoft Dataverse

Customer Insights provides the option to make output entities available as [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro). This integration enables easy data sharing and custom development through a low code/no code approach. The [output entities](#output-entities) are available as tables in a Dataverse environment. You can use the data for any other application based on Dataverse tables. These tables enable scenarios like automated workflows through Power Automate or building apps with Power Apps.

Connecting to your Dataverse environment also enables you to [ingest data from on-premises data sources using Power Platform dataflows and gateways](data-sources.md#add-data-from-on-premises-data-sources).

## Prerequisites

- Customer Insights and Dataverse environments must be hosted in the same region.
- You must have a global administrator role in the Dataverse environment. Verify if this [Dataverse environment is associated](/power-platform/admin/control-user-access#associate-a-security-group-with-a-dataverse-environment) to certain security groups and make sure you are added to those security groups.
- No other Customer Insights environment is already associated with the Dataverse environment you want to connect. Learn how to [remove an existing connection to a Dataverse environment](#remove-an-existing-connection-to-a-dataverse-environment).
- A Microsoft Dataverse environment can only connect to a single storage account. This is only relevant if you configure the environment to [use your Azure Data Lake Storage](own-data-lake-storage.md).

## Connect a Dataverse environment to Customer Insights

The **Microsoft Dataverse** step lets you connect Customer Insights with your Dataverse environment while [creating a Customer Insights environment](create-environment.md).

:::image type="content" source="media/dataverse-provisioning.png" alt-text="data sharing with Microsoft Dataverse auto-enabled for net new environments.":::

Administrators can configure Customer Insights to connect an existing Dataverse environment. By providing the URL to the Dataverse environment, it's attaching to their new Customer Insights environment.

If you don't want to use an existing Dataverse environment, the system creates a new environment for the Customer Insights data in your tenant. [Power Platform admins can control who can create environments](/power-platform/admin/control-environment-creation). If you're setting up a new Customer Insights environment and the admin has disabled the creation of Dataverse environments for everyone except admins, you may not be able to create a new environment.

**Enable data sharing** with Dataverse by selecting the data sharing checkbox.

If you are using your own Data Lake Storage account, you also need the **Permissions identifier**. For more information how to get the permission identifier, review the following section.

## Enable data sharing with Dataverse from your own Azure Data Lake Storage (Preview)

Enabling data sharing with Microsoft Dataverse when your environment [uses your own Azure Data Lake Storage account](own-data-lake-storage.md) needs some extra configuration. The user setting up the Customer Insights environment must have at least **Storage Blob Data Reader** permissions on the *CustomerInsights* container in the Azure Data Lake Storage account.

1. Create two security groups on your Azure subscription - one **Reader** security group and one **Contributor** security group and set the Microsoft Dataverse service as the owner for both security groups.
2. Manage the Access Control List (ACL) on the CustomerInsights container in your storage account via these security groups. Add the Microsoft Dataverse service and any Dataverse-based business applications like Dynamics 365 Marketing to the **Reader** security group with **read-only** permissions. Add *only* the Customers Insights application to the **Contributor** security group to grant both **read and write** permissions to write profiles and insights.

### Limitations

There are two limitations when using Dataverse in connection with your own Azure Data Lake Storage account:

- There's one-to-one mapping between a Dataverse organization and an Azure Data Lake Storage account. Once a Dataverse organization is connected to a storage account, it can't connect to another storage account. This limitation prevents that a Dataverse doesn't populate multiple storage accounts.
- Data sharing won't work if an Azure Private Link setup is needed to access your Azure Data Lake storage account because it's behind a firewall. Dataverse currently doesn't support the connection to private endpoints through Private Link.

### Set up PowerShell

To execute the PowerShell scripts you first need to set up PowerShell accordingly.

1. Install the latest version of [Azure Active Directory PowerShell for Graph](/powershell/azure/active-directory/install-adv2).
   1. On your PC, select the Windows key on your keyboard and search for **Windows PowerShell** and select **Run as administrator**.
   1. In the PowerShell window that opens, enter `Install-Module AzureAD`.
2. Import three modules.
    1. In the PowerShell window, enter `Install-Module -Name Az.Accounts` and follow the steps.
    1. Repeat for `Install-Module -Name Az.Resources` and `Install-Module -Name Az.Storage`.

### Configuration steps

1. Download the two PowerShell scripts you need to run from our engineer's [GitHub repo](https://github.com/trin-msft/byol).
    1. `CreateSecurityGroups.ps1`
       - You need *tenant admin* permissions to run this PowerShell script.
       - This PowerShell script creates two security groups on your Azure subscription. One for the Reader group and another for the Contributor group and will make Microsoft Dataverse service as the owner for both these security groups.
       - Execute this PowerShell script in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage. Open the PowerShell script in an editor to review additional information and the logic implemented.
       - Save both the security group ID values generated by this script because we'll use them in the `ByolSetup.ps1` script.

        > [!NOTE]
        > Security group creation can be disabled on your tenant. In that case, a manual setup would be needed and your Azure AD admin would have to [enable security group creation](/azure/active-directory/enterprise-users/groups-self-service-management).

    2. `ByolSetup.ps1`
        - You need *Storage Blob Data Owner* permissions at the storage account/container level to run this script or this script will create one for you. Your role assignment can be removed manually after successfully running the script.
        - This PowerShell script adds the required tole-based access control (RBAC) for the Microsoft Dataverse service and any Dataverse-based business applications. It also updates the Access Control List (ACL) on the CustomerInsights container for the security groups created with the `CreateSecurityGroups.ps1` script. The Contributor group will have *rwx* permission and Readers group will have *r-x* permission only.
        - Execute this PowerShell script in Windows PowerShell by providing the Azure subscription ID containing your Azure Data Lake Storage, storage account name, resource group name, and the Reader and Contributor security group id values. Open the PowerShell script in an editor to review additional information and the logic implemented.
        - Copy the output string after successfully running the script. The output string looks like this: `https://DVBYODLDemo/customerinsights?rg=285f5727-a2ae-4afd-9549-64343a0gbabc&cg=720d2dae-4ac8-59f8-9e96-2fa675dbdabc`

2. Enter the output string copied from above into the **Permissions identifier** field of the environment configuration step for Microsoft Dataverse.

:::image type="content" source="media/dataverse-enable-datasharing-BYODL.png" alt-text="Configuration options to enable data sharing from your own Azure Data Lake Storage with Microsoft Dataverse.":::

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

If the removal of the connection fails due to dependencies, you need to remove the dependencies too. For more information, see [Removing dependencies](/power-platform/alm/removing-dependencies).

## Output entities

Some output entities from Customer Insights are available as tables in Dataverse. The sections below describe the expected schema of these tables.

- [CustomerProfile](#customerprofile)
- [AlternateKey](#alternatekey)
- [UnifiedActivity](#unifiedactivity)
- [CustomerMeasure](#customermeasure)
- [Enrichment](#enrichment)
- [Prediction](#prediction)
- [Segment membership](#segment-membership)

### CustomerProfile

This table contains the unified customer profile from Customer Insights. The schema for a unified customer profile depends on the entities and attributes used in the data unification process. A customer profile schema usually contains a subset of the attributes from the [Common Data Model definition of CustomerProfile](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/solutions/customerinsights/customerprofile).

### AlternateKey

The AlternateKey table contains keys of the entities, which participated in the unify process.

|Column  |Type  |Description  |
|---------|---------|---------|
|DataSourceName    |String         | Name of the data source. For example: `datasource5`        |
|EntityName        | String        | Name of the entity in Customer Insights. For example: `contact1`        |
|AlternateValue    |String         |Alternative ID that is mapped to the customer ID. Example: `cntid_1078`         |
|KeyRing           | Multiline text        | JSON value  </br> Sample: [{"dataSourceName":" datasource5 ",</br>"entityName":" contact1",</br>"preferredKey":" cntid_1078",</br>"keys":[" cntid_1078"]}]       |
|CustomerId         | String        | ID of the unified customer profile.         |
|AlternateKeyId     | GUID         |  AlternateKey deterministic GUID based on msdynci_identifier       |
|msdynci_identifier |   String      |   `DataSourceName|EntityName|AlternateValue`  </br> Sample: `testdatasource|contact1|cntid_1078`    |

### UnifiedActivity

This table contains activities by users that are available in Customer Insights.

| Column            | Type        | Description                                                                              |
|-------------------|-------------|------------------------------------------------------------------------------------------|
| CustomerId        | String      | Customer Profile ID                                                                      |
| ActivityId        | String      | Internal ID of the customer activity (primary key)                                       |
| SourceEntityName  | String      | Name of the source entity                                                                |
| SourceActivityId  | String      | Primary key from the source entity                                                       |
| ActivityType      | String      | Semantic activity type or name of custom activity                                        |
| ActivityTimeStamp | DATETIME    | Activity Time stamp                                                                      |
| Title             | String      | Title or name of the activity                                                               |
| Description       | String      | Activity description                                                                     |
| URL               | String      | Link to an external URL specific to the activity                                         |
| SemanticData      | JSON String | Includes a list of key value pairs for semantic mapping fields specific to the type of activity |
| RangeIndex        | String      | Unix timestamp used for sorting activity timeline and effective range queries |
| mydynci_unifiedactivityid   | GUID | Internal ID of the customer activity (ActivityId) |

### CustomerMeasure

This table contains the output data of customer attribute-based measures.

| Column             | Type             | Description                 |
|--------------------|------------------|-----------------------------|
| CustomerId         | String           | Customer profile ID        |
| Measures           | JSON String      | Includes a list of key value pairs for measure name and values for the given customer | 
| msdynci_identifier | String           | `Customer_Measure|CustomerId` |
| msdynci_customermeasureid | GUID      | Customer profile ID |


### Enrichment

This table contains the output of the enrichment process.

| Column               | Type             |  Description                                          |
|----------------------|------------------|------------------------------------------------------|
| CustomerId           | String           | Customer profile ID                                 |
| EnrichmentProvider   | String           | Name of the provider for the enrichment                                  |
| EnrichmentType       | String           | Type of enrichment                                      |
| Values               | JSON String      | List of attributes produced by the enrichment process |
| msdynci_enrichmentid | GUID             | Deterministic GUID generated from msdynci_identifier |
| msdynci_identifier   | String           | `EnrichmentProvider|EnrichmentType|CustomerId`         |

### Prediction

This table contains the output of the model predictions.

| Column               | Type        | Description                                          |
|----------------------|-------------|------------------------------------------------------|
| CustomerId           | String      | Customer Profile ID                                  |
| ModelProvider        | String      | Name of the provider of the model                                      |
| Model                | String      | Model name                                                |
| Values               | JSON String | List of attributes produced by the model |
| msdynci_predictionid | GUID        | Deterministic GUID generated from msdynci_identifier | 
| msdynci_identifier   | String      |  `Model|ModelProvider|CustomerId`                      |

### Segment membership

This table contains segment membership information of the customer profiles.

| Column        | Type | Description                        |
|--------------------|--------------|-----------------------------|
| CustomerId        | String       | Customer Profile ID        |
| SegmentProvider      | String       | App that publishes the segments.      |
| SegmentMembershipType | String       | Type of the customer this segment membership record. Supports multiple types such as Customer, Contact, or Account. Default: Customer  |
| Segments       | JSON String  | List of unique segments the customer profile is a member of      |
| msdynci_identifier  | String   | Unique identifier of the segment membership record. `CustomerId|SegmentProvider|SegmentMembershipType|Name`  |
| msdynci_segmentmembershipid | GUID      | Deterministic GUID generated from `msdynci_identifier`          |

## FAQ: Update existing environments to use Microsoft Dataverse

Between mid-May 2022 and June 13, 2022, administrators can update the environment settings with a Dataverse environment that Customer Insights can use. On June 13, 2022, your environment will be updated automatically and we'll create a Dataverse environment on your tenant for you.

1. My environment uses my own Azure Data Lake Storage account. Do I still need to update?

   If there is already a Dataverse environment configured in your environment, the update isn't required. If no Dataverse is environment configured, the **Update now** button will provision a Dataverse environment and update from the Customer Insights database to a Dataverse database.

1. Will we get additional Dataverse capacity, or will the update use my existing Dataverse capacity?

   If there is already a Dataverse environment configured in your Customer Insights environment, or connected with other Dynamics 365 or PowerApps applications, the capacity remains unchanged. If the Dataverse environment is new, it will add new storage and database capacity. The storage and database capacity added varies per environment and entitlements. You'll get 3 GB for trial and sandbox environment. Production environments get 15 GB.

1. I proceeded with the update and it seems like nothing happened. Is the update complete?

   If the notification in Customer Insights no longer shows, the update is complete. You can check the status of the update by reviewing your environment settings.

1. Why do I still see the banner after completing the update steps?

   This could be due to an upgrade or refresh failure. Please contact support.

1. I received a "Failed to provision Dataverse environment" error after starting the update. What happened?

   This could be due to an upgrade or refresh failure. Please contact support.
   Common causes:
    - Insufficient capacity. There are many DV environments already provisioned and there is no more capacity to provision additional environment. For more information, see [Manage capacity action](/power-platform/admin/capacity-storage#actions-to-take-for-a-storage-capacity-deficit).
    - Region mismatch between tenant region and Customer Insights environment region in the Australia and India regions.
    - Insufficient privileges to provision Dataverse. The users starting the update needs a Dynamics 365 admin role.
