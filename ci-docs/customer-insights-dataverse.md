---
title: "Customer Insights data in Microsoft Dataverse"
description: "Use Customer Insights entities as tables in Microsoft Dataverse."
ms.date: 05/20/2022
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

:::image type="content" source="media/dataverse-enable-datasharing.png" alt-text="Configuration options to enable data sharing with Microsoft Dataverse.":::

Administrators can configure Customer Insights to connect an existing Dataverse environment. By providing the URL to the Dataverse environment, it's attaching to their new Customer Insights environment.

If you don't want to use an existing Dataverse environment, the system creates a new environment for the Customer Insights data in your tenant. [Power Platform admins can control who can create environments](/power-platform/admin/control-environment-creation). If you're setting up a new Customer Insights environment and the admin has disabled the creation of Dataverse environments for everyone except admins, you may not be able to create a new environment.

**Enable data sharing** with Dataverse by selecting the data sharing checkbox.

If you are using your own Data Lake Storage account, you also need the **Permissions identifie**r. For more information how to get the permission identifier, see [Enable data sharing with Dataverse (Preview)](own-data-lake-storage.md#enable-data-sharing-with-dataverse-preview).

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
