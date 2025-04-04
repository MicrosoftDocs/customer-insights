---
title: "Supported feature areas"
description: "Learn about supported features for business accounts (B2B) in Dynamics 365 Customer Insights - Data" 
ms.date: 02/06/2024
ms.reviewer: v-wendysmith
ms.topic: overview
author: Scott-Stabbert
ms.author:  sstabbert
ms.custom: bap-template
---

# Supported feature areas

This article describes information specific to legacy B2B environments. For all other information related to Customer Insights - Data, see [Dynamics 365 Customer Insights - Data documentation](../index.yml).

> [!NOTE]
> The legacy B2B version won't be updated with new features being added to the standard version of Customer Insights - Data.

## Supported features overview

|Feature |What's supported |
|----------|-----------|
|Activities |Activities for [accounts](../activities.md) and related [contacts](activities-contacts.md) that can be displayed in a timeline. |
|[Customer profiles](../customer-profiles.md) |In addition to the customer profile, **Contacts for this customer** appear on the **Customers** page. Each contact is shown with their fields. Empty fields are hidden. For more information, see [View customer profiles](../customer-profiles.md). Learn how to [filter contact activities within the timeline.](activities-contacts.md#contact-level-activity-timeline-filtering)|
|[Data ingestion](../data-sources.md) |Azure Data Lake Storage, Azure Synapse Analytics (Lake databases), Microsoft Dataverse data lake, and Power Query only. |
|[Data unification](data-unification-b2b.md) |Account and contact unification. |
|[Enrichment](#enrichments)| Only some enrichment types are available. |
|[Exports](#exports) | Most exports are available.|
|[Measures](../measures.md)| Measures created from the [measure builder](measure-builder-b2b.md) with one calculation. An optional setting allows the roll-up for sub accounts when creating measures.|
|Predictions |[Transactional churn predictions](#predict-transactional-churn) only. |
|[Relationships](../relationships.md) | Relationships created between tables so that the account view can show all activities from contacts. Contacts can drill up to see a contact view and [hierarchies](account-hierarchies.md) can be used for account activity aggregations. |
|[Segments](../segments.md) | Segments that are created from scratch with the [segment builder](segment-builder-b2b.md). Segments can be based on accounts or contacts. |
|[System settings](../system.md) and [user management](../permissions.md) | All features in this area are the same for business accounts. |

## Supported feature details

Review this section for details specific to legacy B2B environments.

### Enrichments

Go to **Data** > **Enrichment**. The **Discover** tab shows all supported enrichment options. You can create the following enrichments for B2B:

- [Account engagement data](enrichment-office.md) provided by Microsoft
- [Company data](enrichment-dnb.md) provided by Dun & Bradstreet
- [Company data](enrichment-leadspace.md) provided by Leadspace
- [Enhanced addresses](../enrichment-enhanced-addresses.md) provided by Microsoft
- [Location data](../enrichment-azure-maps.md) provided by Microsoft Azure Maps
- [SFTP custom data](../enrichment-SFTP-custom-import.md) through Secure File Transfer Protocol (SFTP)

For more information, see [data enrichment (preview) overview](../enrichment-hub.md).

### Environment

Administrators can [create an environment in an existing organization.](../create-environment.md) When creating the environment, select your business type: individual consumers (B2C) or business accounts (B2B).

For B2B, you can then [ingest data](../data-sources.md) for business accounts and related contacts as data sources from all supported sources. [Unify](data-unification-b2b.md) your account data followed by your contact data to connect contact and account tables.

#### Switch between primary target audience

If your organization maintains environments for B2C and B2B, you can use the switcher in the left pane to choose the primary target audience.

:::image type="content" source="media/switch-primary-target-audience.png" alt-text="Switcher to change the primary target audience between individual customers and business accounts.":::

### Exports

Most exports are available for business accounts. Go to [Set up and manage exports](../export-manage.md).

Some exports require extra configuration and contact information projected in the underlying segments to be valid for business accounts. For more information, see [Segment exports](#segment-exports).

#### Segment exports

You can export segment tables from Customer Insights - Data. Segments can represent a list of accounts or contacts. To export account segments as is, the target system needs to support pure account segments. This is the case for [LinkedIn](../export-linkedin-ads.md) when you choose the **company** option while defining the export.

All other target systems require fields from the contact table.

With two segment types (contacts and accounts), the system automatically identifies which type of segments are eligible for export based on the target system. For example, for a contact-focused target system like Mailchimp, the system only allows you to choose contact segments to export.

When configuring the export, you select the included data fields, depending on the target system you're exporting data to.

#### Limits on segment exports

- Third-party target systems might limit the number of customer profiles that you can export.
- For business accounts, you'll see the number of accounts or contacts depending on the segment. You get a warning if the segment is too large. Exceeding the limits of the target systems will skip the export.

#### Customer Card Add-in

If you install the [Customer Card Add-in](../customer-card-add-in.md) and want to add the Customer Card controls to forms, we recommend adding the controls to the Account form. In that case, replace "contact" with "account" in the steps. See [Add Customer Card controls to forms](../customer-card-add-in.md#add-customer-card-controls-to-forms).

The **Enrichment control** requires active enrichments. The card add-in supports [Office engagement data](enrichment-office.md) provided by Microsoft.

#### Power Apps connector

With a [Power Apps connector](../export-power-apps.md), you can choose the **UnifiedContact** table to display the contacts of a customer.

Delegation for **UnifiedContact** only works for the fields **ContactId** and **CustomerId**.

### Predict transactional churn

For environments based on business accounts, we can predict transactional churn for an account and also a combination of account and another level of information like product category. For example, adding a dimension can help determine how likely it is that the account "Contoso" will stop buying the product category "office stationery." In addition, for business accounts, we can also use AI to generate a list of potential reasons why an account is likely to churn for a category of secondary level information.

#### Create a transaction churn prediction

To create a transaction churn prediction, see [Predict transaction churn](../predict-transactional-churn.md). In addition to the listed prerequisites, add customer data aligned toward more static attributes to ensure the model performs best. For example, **Industry** in a coffee roaster might indicate if the customer was retail. **Classification** might be a field called "ValueSegment" that specifies the tier of customer based on the customer size.

When creating the prediction, you have the option to select a prediction level to predict churn for a branch of a customer, for example, rather than for the customer as a whole. You also have the option to add a list of your business customers and accounts that you want to use as benchmarks.

#### View prediction results

For B2B, the prediction results have an extra page called **Influential feature analysis** based on your selection of **Top customers** or **Benchmark customers**. Both lists are ordered by decreasing value of the churn score, whether the score is just for the customer or a combined score for customers and a secondary level like product category. Other sections include:

- **Churn score:** Shows the churn score for the selected item in the right pane.

- **Churn risk distribution:** Shows the churn risk distribution across customers and the percentile the selected customer is in.

- **Top features increasing and decreasing churn risk:** Lists the top five features that increased and decreased the churn risk for the selected item in the right pane. Shows the value of the feature for that item and its influence on the churn score for every influential feature. The average value of each feature across low, medium, and high churn customer segments is also shown. It helps to better contextualize the values of the top influential features for the selected item and compare it with low, medium, and high churn customer segments.

  - Low: accounts or combinations of account and secondary level with a churn score between 0 and 0.33.
  - Medium: accounts or combinations of accounts and secondary levels with a churn score between 0.33 and 0.66.
  - High: accounts or combinations of accounts and secondary levels with a churn score greater than 0.66.

  When you predict churn at the account level, all accounts are considered in deriving the average feature values for churn segments. For churn predictions at the secondary level for every account, the derivation of churn segments depends on the secondary level of the item selected in the side pane. For example, if an item has a secondary level of product category (office supplies), then only the items having office supplies as the product category are considered when deriving the average feature values for churn segments. This logic is applied to ensure a fair comparison of the item's feature values with the average values across low, medium, and high churn segments.

  In some cases, the average value of low, medium, or high churn segments is empty or not available because there are no items that belong to the corresponding churn segments based on the above definition.

  The interpretation of values under the average low, medium, and high columns is different for categorical features like country/region or industry. Because the notion of "average" feature value doesn't apply to categorical features, the values in these columns are the proportion of customers in low, medium, or high churn segments that have the same value of the categorical feature as compared to the item selected in the side panel.

### Tables

For the B2B scenario, the customer profile contains unified accounts, and the schema usually contains a subset of the attributes from the [Common Data Model definition of Account](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/account). An additional table, *UnifiedContact* is created if contact data is unified.

#### UnifiedContact

The *UnifiedContact* table contains unified information about a contact. Contacts are [individuals that are mapped to an account](data-unification-contacts.md) in a B2B scenario.

| Column                       | Type                | Description     |
| ---------------------------- | ------------------- | --------------- |
|  BirthDate            | DateTime       |  Date of birth of the contact               |
|  City                 | Text |  City of the contact address               |
|  ContactId            | Text |  ID of the contact profile               |
|  CountryOrRegion      | Text |  Country/Region of the contact address               |
|  CustomerId           | Text |  ID of the account the contact is mapped to               |
|  TableName            | Text |  Name of the table               |
|  FirstName            | Text |  First name of the contact               |
|  FK_AccountID         | Text |  GUID representing the unified account  |
|  FK_ContactToAccountID| Text |  Unified source value for the contact's associated account |
|  Gender               | Text |  Gender of the contact               |
|  Id                   | Text |  Deterministic GUID based on `Identifier`               |
|  Identifier           | Text |  Internal ID of the contact profile: `UnifiedContact|CustomerId|ContactId`               |
|  JobTitle             | Text |  Job title of the contact               |
|  LastName             | Text |  Last name of the contact               |
|  PostalCode           | Text |  ZIP code of the contact address               |
|  PrimaryEmail         | Text |  Email address of the contact               |
|  PrimaryPhone         | Text |  Telephone number of the contact               |
|  StateOrProvince      | Text |  State or province of the contact address               |
|  StreetAddress        | Text |  Street of the contact address               |
|  UnifiedContactId     | Unique identifier   |  GUID for the contact               |


[!INCLUDE [footer-include](../includes/footer-banner.md)]
