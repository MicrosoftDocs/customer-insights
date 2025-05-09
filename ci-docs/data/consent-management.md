---
title: Use customer consent
description: "Honor you customers' consent preferences in Customer Insights by importing consent data."
ms.date: 06/19/2024
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert 
ms.author: sstabbert
---
# Use customer consent

Dynamics 365 Customer Insights helps you honor your customers’ consent requests by importing and storing their preferences as part of the unified customer profiles.

If consent data is stored separately from your customer profiles, [add your consent data as a new data source](#import-and-unify-consent-data). The data source that contains the consent data is added to the data unification process. Successful unification of consent data and customer profiles then leads to unified customer profiles that contain the consent information. For customer profiles that already contain consent information, go directly to the [use consent data](#use-consent-data) section.

## Prerequisites

The following information must be available in your source data to unify consent data with other customer profiles:

- A key to match the consent information to user profiles in Customer Insights - Data. For example, an email address or a phone number.
- Consent value to determine the status of the customer's consent.

Consent data can be unified from a single table or multiple tables as long as a customer is represented as a single row in each table.

## Example 1 - Consent data in a single table

|Consent ID |Email |Newsletter consent  |Product update consent  |
|---------|---------|---------|---------|
|1    |  holly@contoso.com       |  True       | True       |
|2    |  frank@contoso.com       |  True       | False      |

## Example 2 - Consent data in separate tables

|Consent ID  |Email  | Newsletter consent  |
|---------|---------|----------|
|1    |  holly@contoso.com       |  True       |
|2    |  frank@contoso.com       |  True       |

|Consent ID   |Email  | Product update consent  |
|---------|---------|---------|
|1    |  holly@contoso.com       |  True       |
|2    |  frank@contoso.com       |  False      |

## Import and unify consent data

Import consent data the same way that you ingest other data sources to Customer Insights - Data. For more information about supported data sources and how to import them, see [Data sources overview](data-sources.md).

For more information about unifying your data sources, see [Data unification overview](data-unification.md).

## Use consent data

Once your consent data is part of your unified customer profiles, you can use it in Customer Insights - Data. For example, create a segment with a rule to ensure you honor your customers’ privacy and data protection preferences. Rules supporting consent preferences are used to exclude users from a segment based on profile attributes. Add a rule to a segment that excludes customer profiles that didn't provide consent to contact.

In example 1, a segment could contain this rule: `Newsletter consent value=True`. This configuration results in a segment that honors contact preferences to send a newsletter.

For more information about building segments, see [Create segments](segment-builder.md).

Once the segment is created, you can use one of the many [export options](export-manage.md) to use the segment in other applications.

[!INCLUDE [footer-include](includes/footer-banner.md)]
