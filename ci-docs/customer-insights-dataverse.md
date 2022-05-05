---
title: "Customer Insights data in Microsoft Dataverse"
description: "Use Customer Insights entities as tables in Microsoft Dataverse."
ms.date: 04/05/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: wimohabb
manager: shellyha
searchScope: 
  - ci-system-diagnostic
  - customerInsights
---

# Work with Customer Insights data in Microsoft Dataverse

Customer Insights provides the option to make output entities available in [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro). This integration enables easy data sharing and custom development through a low code/no code approach. The [output entities](#output-entities) are available as tables in a Dataverse environment. You can use the data for any other application based on Dataverse tables. These tables enable scenarios like automated workflows through Power Automate or building apps with Power Apps. The current implementation mainly supports lookups where data from the available Customer Insights entities can be fetched for a given customer ID.

## Connect a Dataverse environment to Customer Insights

**Existing organization**

Administrators can configure Customer Insights to [use an existing Dataverse environment](create-environment.md) when they create a Customer Insights environment. By providing the URL to the Dataverse environment, it's attaching to their new Customer Insights environment. Customer Insights and Dataverse environments must be hosted in the same region. 

If you don't want to use an existing Dataverse environment, the system creates a new environment for the Customer Insights data in your tenant. 

> [!NOTE]
> If your organizations already uses Dataverse in their tenant, it’s important to remember that [Dataverse environment creation is controlled by an admin](/power-platform/admin/control-environment-creation). For example, if a you're setting up a new Customer Insights environment with your organizational account and the admin has disabled the creation of Dataverse trial environments for everyone except admins, you can't create a new trial environment.
> 
> The Dataverse trial environments created in Customer Insights have 3 GB of storage which won't count towards the overall capacity entitled to the tenant. Paid subscriptions get Dataverse entitlement of 15 GB for database and 20 GB for file storage.

**New organization**

If you create a new organization when setting up Customer Insights, the system automatically creates a new Dataverse environment in your organization for you.

### TODO from other articles

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

Connecting to your Dataverse environment also enables you to [ingest data from on-premises data sources using Power Platform dataflows and gateways](data-sources.md#add-data-from-on-premises-data-sources).

> [!IMPORTANT]
> 1. Customer Insights and Dataverse have to be in the same region to enable data sharing.
> 1. You must have a global administrator role in the Dataverse environment. Verify if this [Dataverse environment is associated](/power-platform/admin/control-user-access#associate-a-security-group-with-a-dataverse-environment) to certain security groups and make sure you are added to those security groups.
> 1. No existing Customer Insights environment is already associated with that Dataverse environment. Learn how to [remove an existing connection to a Dataverse environment](manage-environments.md#remove-an-existing-connection-to-a-dataverse-environment).


For more information about enabling data sharing with Microsoft Dataverse from your own Azure Data Lake Storage, see [Connect to Microsoft Dataverse](manage-environments.md#connect-to-microsoft-dataverse).

Customer Insights does not support the following data sharing scenarios:
- If you enable data sharing with Dataverse, you won't be able to [create predicted or missing values in an entity](predictions.md).

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

This table contains the unified customer profile from Customer Insights. The schema for a unified customer profile depends on the entities and attributes used in the merge process. A customer profile schema usually contains a subset of the attributes from the [Common Data Model definition of CustomerProfile](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/solutions/customerinsights/customerprofile).

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
