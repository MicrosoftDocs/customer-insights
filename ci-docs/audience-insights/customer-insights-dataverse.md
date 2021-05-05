---
title: "Customer Insights data in Microsoft Dataverse"
description: "Use Customer Insights entities as tables in Microsoft Dataverse."
ms.date: 04/29/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: wimohabb
manager: shellyha
---

# Work with Customer Insights data in Microsoft Dataverse

Customer Insights provides the option to make output entities available in Dataverse. This integration enables easy data sharing and custom development through a low code / no code approach. The output entities will be available as tables in Dataverse. These tables enable scenarios like [automated workflows through Power Automate](/power-automate/getting-started), [model-driven apps](/powerapps/maker/model-driven-apps/) and [canvas apps](/powerapps/maker/canvas-apps/) through Power Apps. Of course, you can use the data for any other application that is based on Dataverse tables. The current implementation mainly supports lookups where data from the available audience insights entities can be fetched for a given customer id.

## Attach a Dataverse environment to Customer Insights

**Organizations with existing Dataverse environments**

Organizations that already use Dataverse can choose to [use one of their existing Dataverse environments](manage-environments.md#create-an-environment-in-an-existing-organization) when creating the audience insights environment. By providing the URL to the Dataverse environment, it's attaching to their new audience insights environment. To ensure the best possible performance, Customer Insights and Dataverse environments must be hosted in the same region.

<!-- update/review configuration of environment articles-->

**New organization**

If a new organization is created when signing up for Customer Insights, it'll automatically get a new Dataverse environment during the provisioning process.

<!-- Do new orgs still need to provide the DV env URL in the environment step or check the data sharing checkbox? might need to be more specific here.-->

Trial specs: 
For customers who already use Dataverse in their tenant, it’s important to remember that Dataverse environment creation is controlled by their admin. For example, if a customer is setting up a new trial AUI instance by using her organization account, and her tenant admin has disabled creation of Dataverse trial environments for everyone except admins (see screenshot below), then she will not be able to create an AUI trial instance. This is controlled by a setting in Power Platform admin center, under Power Platform settings as shown in the following screenshots:

The trial Dataverse environments provisioned through AUI will all come with 3GB of storage so this will not have any impact on the overall capacity entitled to the tenant. The Dataverse entitlement for paid AUI instances is 15 GB for database and 20GB for file storage.


## Output entities

A set of output entities from audience insights are available as tables in Dataverse. 

- [CustomerProfile](#customerprofile)
- [AlternateKey](#alternatekey)
- [UnifiedActivity](#unifiedactivity)
- [CustomerMeasure](#customermeasure)
- [Enrichment](#enrichment)
- [Prediction](#prediction)


### CustomerProfile

This entity models the unified profile in CI. The shape and the schema for unified profile can vary from customer to customer based on the entities the customer brings in to participate the unify process and the attributes that they select in the merge process. A typical customer profile schema contains a subset of attributes from the CI standard [CDM definition of CustomerProfile](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/solutions/customerinsights/customerprofile).

### AlternateKey

AlternateKey entity models the natural keys of the entities participated in the unify process and has the following schema.


|Column  |Type  |Description  |
|---------|---------|---------|
|DataSourceName    |String         | Name of the data source. For example: datasource5        |
|EntityName        | String        | Name of the entity in audience insights. For example: contact1        |
|AlternateValue    |String         |Alternative ID that is mapped to the customer ID. Example: cntid_1078         |
|KeyRing           | Multi line text        | JSON value  </br> Sample: ```[{"dataSourceName":" testdatasource ",
"entityName":" contact1",
"preferredKey":" cntid_1078",
"keys":[" cntid_1078"]}]```       |
|CustomerId         | String        | ID of the unified customer profile.         |
|AlternateKeyId     | GUID         |  AlternateKey deterministic GUID based on msdynci_identifier       |
|msdynci_identifier |   String      |   DataSourceName|EntityName|AlternateValue  </br> Sample: `testdatasource|contact1|cntid_1078`    |

### UnifiedActivity

Unified Activity models an activity by the user that has observational value to the business. 

| Column            | Type        | Description                                                                              |
|-------------------|-------------|------------------------------------------------------------------------------------------|
| CustomerId        | String      | Customer Profile Id                                                                      |
| ActivityId        | String      | Internal Id of the customer activity (primary key)                                       |
| SourceEntityName  | String      | Source Entity name                                                                       |
| SourceActivityId  | String      | Primary Key from the source entity                                                       |
| ActivityType      | String      | Semantic activity type or name of custom activity                                        |
| ActivityTimeStamp | DATETIME    | Activity Time stamp                                                                      |
| Title             | String      | Title/Name of the activity                                                               |
| Description       | String      | Activity Description                                                                     |
| URL               | String      | Link to an external URL specific to the activity                                         |
| SemanticData      | JSON String | Includes a list of key value pairs for semantic mapping fields specific to Activity Type |
| RangeIndex        | String      | Unix timestamp used for sorting activity timeline and effective range queries |
| mydynci_unifiedactivityid   | GUID | Internal Id of the customer activity (ActivityId) |

### CustomerMeasure

CustomerMeasure entity keeps the customer attribute-based measures.

| Column             | Type             | Description                 |
|--------------------|------------------|-----------------------------|
| CustomerId         | String           | Customer Profile Id         |
| Measures           | JSON String      | Includes a list of key value pairs for measure name and values for the given customer | 
| msdynci_identifier | String           | Customer_Measure|CustomerId |
| msdynci_customermeasureid | GUID      | Customer Profile Id |


### Enrichment

The output of the enrichment process is persisted in the Enrichment entity.

| Column               | Type             |  Description                                          |
|----------------------|------------------|------------------------------------------------------|
| CustomerId           | String           | Customer Profile Id                                  |
| EnrichmentProvider   | String           | Enrichment Provider                                  |
| EnrichmentType       | String           | Enrichment Type                                      |
| Values               | JSON String      | List of attributes produced by the enrichment process. |
| msdynci_enrichmentid | GUID             | Deterministic GUID generated from msdynci_identifier |
| msdynci_identifier   | String           | EnrichmentProvider|EnrichmentType|CustomerId         |

### Prediction

The output of the model predictions is persisted in this entity.

| Column               | Type        | Description                                          |
|----------------------|-------------|------------------------------------------------------|
| CustomerId           | String      | Customer Profile Id                                  |
| ModelProvider        | String      | Model Provider                                       |
| Model                | String      | Model                                                |
| Values               | JSON String | List of attributes produced by the model. |
| msdynci_predictionid | GUID        | Deterministic GUID generated from msdynci_identifier | 
| msdynci_identifier   | String      |  Model|ModelProvider|CustomerId                      |



