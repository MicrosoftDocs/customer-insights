---
title: "Business acounts overview in Customer Insights"
description: "Learn about business accounts (B2B) in Dynamics 365 Customer Insights" 
ms.date: 08/30/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author:  sstabbert
ms.custom: bap-template
---

# Business accounts overview in Customer Insights

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

With Dynamics 365 Customer Insights, business accounts (B2B) aren't supported. However, current customers with B2B data are still supported. This article describes information specific to B2B environments. For all other informtion related to Customer Insights, see [Dynamics 365 Customer Insights documentation.](../index.yml)

## Supported feature areas

- Activities: Support for [accounts](../activities.md) and related [contacts](activities-contacts.md) to create activities and show them in a timeline.
- [Relationships](../relationships.md): The activity wizard helps creating relationships between the tables so the account view can show all activities from contacts. Contacts can drill up to see contact view and [hierarchies](account-hierarchies.md) can be used for account activity aggregations.
- [Measures](../measures.md): Supports measures created from the [measure builder](measure-builder-b2b.md) with one calculation. An optional setting allows the roll-up for sub accounts when creating measures.
- [Segments](segments.md): Supports segments that are created from scratch with the [segment builder](segment-builder-b2b.md). Segments can be based on accounts or contacts.
- [Data ingestion](../data-sources.md)
- B2B data unification is very similar to B2C [data unification](../data-unification.md) but has an additional step to [unify contacts](data-unification-contacts.md) after account unification.
- [Enrichment](#enrichments): Some enrichment types are available only for business accounts.
- [Predictions and out-of-box models](../predictions.md): Transactional churn prediction contains additional steps for business accounts. Other predictions are only available for individual customers.
- [Activation and export](export-manage.md): Exports are available for business accounts. Some exports require extra configuration and contact information projected in the underlying segments to be valid for business accounts. See [Segment exports](#segment-exports) for more information.
- [System settings](../system.md) and [user management](../permissions.md): All features in this area are the same for business accounts.








## Environment

To create an environment, see [Create a new environment.](../create-environment.md) When creating the environment, select your business type:

**Choose your business**: Primary audience for the new environment: individual consumers (B2C) or [business accounts](work-with-business-accounts.md) (B2B). If your organization mainly does business with individuals, such as a retailer or a coffee shop, choose individual consumers. If your main audience is other companies, such as a car manufacturer or a paper company, choose business accounts.

## Dataverse storage capacity entitlement

A Customer Insights subscription entitles you to extra capacity for your organization's existing [Dataverse storage capacity](/power-platform/admin/capacity-storage). The added capacity depends on the number of profiles that your subscription uses.

For example, if you have a B2B subscription with 30,000 accounts, your total storage capacity is 45 GB (3 x 15 GB) database storage, and 60-GB file storage (3 x 20 GB).

## Customer profiles

On the **Customers** page, select a customer tile to view details for the selected customer. For business accounts, in addition to the customer profile, **Contacts for this customer** display. Each contact is shown with their fields. Empty fields are hidden. For more information, see [View customer profiles.](../customer-profiles.md)

## Enrichments

Go to **Data** > **Enrichment**. The **Discover** tab shows all supported enrichment options. You can create the following enrichments for B2B:

- [Account engagement data](enrichment-office.md) provided by Microsoft
- [Company data](enrichment-dnb.md) provided by Dun & Bradstreet
- [Company data](enrichment-leadspace.md) provided by Leadspace
- [Enhanced addresses](../enrichment-enhanced-addresses.md) provided by Microsoft
- [Enhanced company data](enrichment-enhanced-company-data.md) provided by Microsoft
- [Location data](../enrichment-azure-maps.md) provided by Microsoft Azure Maps
- [Location data](../enrichment-here.md) provided by HERE Technologies
- [SFTP custom data](../enrichment-SFTP-custom-import.md) through Secure File Transfer Protocol (SFTP)

For more information, see [data enrichment (preview) overview](../enrichment-hub.md)

## Power Apps

With a [Power Apps connector](../export-power-apps.md), you can choose the **UnifiedContact** table to display the contacts of a customer.

Delegation for **UnifiedContact** only works for the fields **ContactId** and **CustomerId**.

## Segment exports

You can export segment tables from Customer Insights. Segments are built on the *account* table or the *contact* table. To export account segments as is, the target system needs to support pure account segments. This is the case for [LinkedIn](../export-linkedin-ads.md) when you choose the **company** option while defining the export.

All other target systems require fields from the contact table.

With two segment types (contacts and accounts), Customer Insights automatically identifies which type of segments are eligible for export based on the target system. For example, for a contact-focused target system like Mailchimp, Customer Insights only allows you to choose contact segments to export.

When configuring the export, you select the included data fields, depending on the target system you are exporting data to.

### Limits on segment exports

- Third-party target systems may limit the number of customer profiles that you can export.
- For business accounts, you'll see the number of accounts or contacts depending on the segment. You will get a warning if the segment is too large. Exceeding the limits of the target systems results will skip the export.

## Tables

For the B2B scenario, the customer profile contains unified accounts, and the schema usually contains a subset of the attributes from the [Common Data Model definition of Account](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/account).

### UnifiedContact

A UnifiedContact contains unified information about a contact. Contacts are [individuals that are mapped to an account](data-unification-contacts.md) in a B-to-B scenario.

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





[!INCLUDE [footer-include](includes/footer-banner.md)]
