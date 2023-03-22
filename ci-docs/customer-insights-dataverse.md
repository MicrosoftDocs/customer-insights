---
title: Work with Customer Insights data in Microsoft Dataverse
description: Learn how to connect Customer Insights and Microsoft Dataverse and understand the output entities that are exported to Dataverse.
ms.date: 01/16/2023
ms.topic: conceptual
author: mukeshpo
ms.author: mukeshpo
ms.custom: bap-template
searchScope: 
  - ci-system-diagnostic
  - customerInsights
---

# Work with Customer Insights data in Microsoft Dataverse

Customer Insights makes its output entities available in [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro). This integration enables easy data sharing and custom development through a low code/no code approach. The [output entities](#output-entities) are available as tables in a Dataverse environment. You can use the data for any other application based on Dataverse tables. These tables enable scenarios like automated workflows through Power Automate or building apps with Power Apps.

You can also [ingest data from on-premises data sources using Power Platform dataflows and gateways](connect-power-query.md#add-data-from-on-premises-data-sources) into your Dataverse environment.

## Prerequisites

- Customer Insights and Dataverse environments must be hosted in the same region.
- A global administrator role set up in the Dataverse environment. Verify if this [Dataverse environment is associated](/power-platform/admin/control-user-access#associate-a-security-group-with-a-dataverse-environment) to certain security groups and make sure you're added to those security groups.
- No other Customer Insights environment already associated with the Dataverse environment you want to connect. Learn how to [remove an existing connection to a Dataverse environment](#remove-an-existing-connection-to-a-dataverse-environment).
- A Microsoft Dataverse environment connected to a single storage account if you configure the environment to [use your Azure Data Lake Storage](own-data-lake-storage.md).

## Dataverse storage capacity entitlement

A Customer Insights subscription entitles you to extra capacity for your organization's existing [Dataverse storage capacity](/power-platform/admin/capacity-storage). The added capacity depends on the number of profiles that your subscription uses.

**Example:**

Assuming you get 15-GB database storage and 20-GB file storage per 100,000 customer profiles. If your subscription includes 300,000 customer profiles, your total storage capacity is 45 GB (3 x 15 GB) database storage and 60-GB file storage (3 x 20 GB). Similarly, if you have a B-to-B subscription with 30,000 accounts, your total storage capacity is 45 GB (3 x 15 GB) database storage, and 60-GB file storage (3 x 20 GB).

Log capacity isn't incremental and fixed for your organization.

For more information about the detailed capacity entitlements, see [Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/?LinkId=866544).

## Connect a Dataverse environment to Customer Insights

The **Microsoft Dataverse** step lets you connect Customer Insights with your Dataverse environment while [creating a Customer Insights environment](create-environment.md).

:::image type="content" source="media/dataverse-provisioning.png" alt-text="data sharing with Microsoft Dataverse auto-enabled for new environments.":::

1. Provide the URL to your Dataverse environment or leave blank to have one created for you.

   > [!NOTE]
   > After establishing the connection between Customer Insights and Dataverse, don't change the organization name for the Dataverse environment. The name of the organization is used in the Dataverse URL and a changed name breaks the connection with Customer Insights.

   [Power Platform admins can control who can create a new Dataverse environments](/power-platform/admin/control-environment-creation). If you're trying to set up a new Customer Insights environment and can't, the admin might have disabled the creation of Dataverse environments for everyone except admins.

1. If you're using your own Data Lake Storage account:
   1. Select **Enable data sharing** with Dataverse.
   1. Enter the **Permissions identifier**. To get the permission identifier, [enable data sharing with Dataverse from your own Azure Data Lake Storage](#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview).

## Enable data sharing with Dataverse from your own Azure Data Lake Storage (preview)

In [your own Azure Data Lake Storage account](own-data-lake-storage.md), verify the user setting up the Customer Insights environment has at least **Storage Blob Data Reader** permissions on the `customerinsights` container in the storage account.

> [!NOTE]
> Data sharing is applicable only if you use your own Azure Data Lake Storage account. This setting isn't available if the Customer Insights environment uses the default Dataverse storage.

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

When connecting to a Dataverse environment, the error message **This CDS organization is already attached to another Customer Insights instance** means that the Dataverse environment is already used in a Customer Insights environment. You can remove the existing connection as a global administrator on the Dataverse environment. It can take a couple of hours to populate the changes.

1. Go to [Power Apps](https://make.powerapps.com).
1. Select the environment from the environment picker.
1. Go to **Solutions**.
1. Uninstall the following Customer Insights solutions:
   - Dynamics 365 Customer Insights Base (*msdyn_CustomerInsightsAnchor*)
   - Dynamics 365 Customer Insights Data Tables (*msdyn_CustomerInsightsDataTables*)
   - Dynamics 365 Customer Insights (*msdyn_CustomerInsights*)
   - Dynamics 365 Customer Insights Customer Card (*CustomerInsightsCustomerCard*)
   - Dynamics 365 Customer Insights Prod First Party App User Management (*msdyn_CustomerInsightsAppUserManagementProd*)

If the removal of the connection fails due to dependencies, you need to remove the dependencies too. For more information, see [Removing dependencies](/power-platform/alm/removing-dependencies).

## Output entities

Some output entities from Customer Insights are available as tables in Dataverse. The sections below describe the expected schema of these tables.

- [CustomerProfile](#customerprofile)
- [ContactProfile](#contactprofile)
- [AlternateKey](#alternatekey)
- [UnifiedActivity](#unifiedactivity)
- [CustomerMeasure](#customermeasure)
- [Enrichment](#enrichment)
- [Prediction](#prediction)
- [Segment membership](#segment-membership)

### CustomerProfile

This table contains the unified customer profile from Customer Insights. The schema for a unified customer profile depends on the entities and attributes used in the data unification process. A customer profile schema usually contains a subset of the attributes from the [Common Data Model definition of CustomerProfile](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/solutions/customerinsights/customerprofile). For the B-to-B scenario, the customer profile contains unified accounts, and the schema usually contains a subset of the attributes from the [Common Data Model definition of Account](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/account).

### ContactProfile

A ContactProfile contains unified information about a contact. Contacts are [individuals that are mapped to an account](data-unification-contacts.md) in a B-to-B scenario.

| Column                       | Type                | Description     |
| ---------------------------- | ------------------- | --------------- |
|  BirthDate            | DateTime       |  Date of birth of the contact               |
|  City                 | Text |  City of the contact address               |
|  ContactId            | Text |  ID of the contact profile               |
|  ContactProfileId     | Unique identifier   |  GUID for the contact               |
|  CountryOrRegion      | Text |  Country/Region of the contact address               |
|  CustomerId           | Text |  ID of the account the contact is mapped to               |
|  EntityName           | Text |  Name of the entity               |
|  FirstName            | Text |  First name of the contact               |
|  Gender               | Text |  Gender of the contact               |
|  Id                   | Text |  Deterministic GUID based on `Identifier`               |
|  Identifier           | Text |  Internal ID of the contact profile: `ContactProfile|CustomerId|ContactId`               |
|  JobTitle             | Text |  Job title of the contact               |
|  LastName             | Text |  Last name of the contact               |
|  PostalCode           | Text |  ZIP code of the contact address               |
|  PrimaryEmail         | Text |  Email address of the contact               |
|  PrimaryPhone         | Text |  Telephone number of the contact               |
|  StateOrProvince      | Text |  State or province of the contact address               |
|  StreetAddress        | Text |  Street of the contact address               |

### AlternateKey

The AlternateKey table contains keys of the entities, which participated in the unify process.

|Column  |Type  |Description  |
|---------|---------|---------|
|DataSourceName    |Text         | Name of the data source. For example: `datasource5`        |
|EntityName        | Text        | Name of the entity in Customer Insights. For example: `contact1`        |
|AlternateValue    |Text         |Alternative ID that is mapped to the customer ID. Example: `cntid_1078`         |
|KeyRing           | Text        | JSON value  </br> Sample: [{"dataSourceName":" datasource5 ",</br>"entityName":" contact1",</br>"preferredKey":" cntid_1078",</br>"keys":[" cntid_1078"]}]       |
|CustomerId         | Text        | ID of the unified customer profile.         |
|AlternateKeyId     | Unique identifier        |  AlternateKey deterministic GUID based on `Identifier`      |
|Identifier |   Text      |   `DataSourceName|EntityName|AlternateValue`  </br> Sample: `testdatasource|contact1|cntid_1078`    |

### UnifiedActivity

This table contains activities by users that are available in Customer Insights.

| Column            | Type        | Description                                                                              |
|-------------------|-------------|------------------------------------------------------------------------------------------|
| CustomerId        | Text      | Customer profile ID                                                                      |
| ActivityType      | Text      | Semantic activity type or name of custom activity. For example: `SalesOrderLine`  |
| ExternalUrl       | Text      | Link to an external URL for this activity. Usually denotes the URL of the website visited by a customer.     |
| ActivityTime      | DateTime  | Activity time stamp. Usually denotes when the activity occurred. For example: `2021-12-24T21:00:00Z`  |
| ActivityId        | Text      | Internal ID of the customer activity (primary key)                                       |
| ActualActivityId  | Text      | Internal ID of the activity row in the source entity/table                                       |
| Title             | Text      | Title or name of the activity                                                               |
| EntityName        | Text      | Name of the source entity/table used for this activity                                            |
| ActivityName      | Text      | The event that happened for this activity. For example: `webpage view`                        |

### CustomerMeasure

This table contains the output data of customer attribute-based measures.

| Column             | Type             | Description                 |
|--------------------|------------------|-----------------------------|
| CustomerId         | Text           | Customer profile ID        |
| Measures           | Text      | Includes a list of key value pairs for measure name and values for the given customer |
| Identifier | Text           | `Customer_Measure|CustomerId` |
| CustomerMeasureId | Unique identifier     | Customer profile ID |

### Enrichment

This table contains the output of the enrichment process.

| Column               | Type             |  Description                                          |
|----------------------|------------------|------------------------------------------------------|
| CustomerId           | Text           | Customer profile ID                                 |
| EnrichmentProvider   | Text           | Name of the provider for the enrichment                                  |
| EnrichmentType       | Text           | Type of enrichment                                      |
| Values               | Text      | List of attributes produced by the enrichment process |
| EnrichmentId | Unique identifier            | Deterministic GUID generated from `Identifier` |
| Identifier   | Text           | `EnrichmentProvider|EnrichmentType|CustomerId`         |

### Prediction

This table contains the output of the model predictions.

| Column               | Type        | Description                                          |
|----------------------|-------------|------------------------------------------------------|
| CustomerId           | Text      | Customer profile ID                                  |
| ModelProvider        | Text      | Name of the provider of the model                                      |
| Model                | Text      | Model name                                                |
| Values               | Text | List of attributes produced by the model |
| PredictionId | Unique identifier       | Deterministic GUID generated from `Identifier` |
| Identifier   | Text      |  `Model|ModelProvider|CustomerId`                      |

### Segment membership

This table contains segment membership information of the customer profiles.

| Column        | Type | Description                        |
|--------------------|--------------|-----------------------------|
| CustomerId        | Text       | Customer Profile ID        |
| SegmentProvider      | Text       | App that publishes the segments.      |
| SegmentMembershipType | Text       | Type of customer for this segment membership record. Supports multiple types such as Customer, Contact, or Account. Default: Customer  |
| Segments       | Text  | List of unique segments the customer profile is a member of      |
| Identifier  | Text   | Unique identifier of the segment membership record. `CustomerId|SegmentProvider|SegmentMembershipType|Name`  |
| SegmentMembershipId | Unique identifier      | Deterministic GUID generated from `Identifier`          |

[!INCLUDE [footer-include](includes/footer-banner.md)]
