---
title: Automatically link Dynamics 365 apps to customer profiles
description: Learn how the Customer Insights - Data unified profile can be used with other Dynamics 365 applications.
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.topic: conceptual
ms.date: 06/13/2024
ms.custom: bap-template
---

# Automatically link Dynamics 365 apps to customer profiles

Automatic linking lets you work with your Dynamics 365 contacts, leads, and other customer tables with extended insights from the unified customer profile from Customer Insights - Data. You can easily access data associated with a customer including:

- Customer profile attributes such as "loyalty tier"
- Customer measures such as "Days since last claim"
- Customer activities calculated as a measure, such as "Total purchases" and "Number of purchases in the last four months"

## Examples

- A Dynamics 365 Sales admin easily links to a customer lifetime value (CLV) or lead score from Customer Insights - Data. A Sales agent sees the data on their **Leads** page, providing more details about their customer’s interests, activity history, and insights.
- A Dynamics 365 Support admin updates their contact measures showing the number of support issues in the last month, year, and lifetime for a customer.
- A Customer Insights – Journeys marketing manager uses the loyalty tier data to personalize a new product announcement.

## Requirements

- Microsoft Dataverse source tables come from the Dataverse environment Customer Insights - Data links to. Linking isn't supported for tables from other Dataverse environments.
- Dataverse source tables, such as the leads table, must be ingested into Customer Insights - Data through the [Microsoft Dataverse connector (recommended)](connect-dataverse.md) or the [Power Query Dataverse connector](connect-power-query.md). Don't change the names of the source tables.
- The primary key selected on the [Describe customer data step for unification](data-unification-map-tables.md) for each Dataverse table is the actual primary key for the table. For example, the standard contact and lead tables primary keys are *ContactId* and *LeadId*.
- Your Customer Insights - Data environment is set up for individual customers. Linking isn't supported for business (B2B) environments.

> [!NOTE]
> Customer Insights - Data environments configured to write output to a private data lake aren't supported.

## Link to customer profile

Every time unification is run, the customer profile table is written to Dataverse. If all requirements are met, Customer Insights automatically updates the unified Dataverse source tables with links to the customer profile table. Source records in each Dataverse table that participated in unification are linked to their associated record in the customer profile table.

The task that performs the linking is called **CustomerId Backstamping Hydration**. To see the results from the task, go to **Settings** > **System** and select the **Status** tab. When the task runs for the first time on a source table, it adds a Lookup column and populates fields with the appropriate CustomerID to link each row. The Lookup column name is **Customer Profile** and the Schema name is **msdynci_lookupfield_customerprofile**. On subsequent runs, only rows that change are updated.

### CustomerId Backstamping Hydration task

- If the status of the **CustomerId Backstamping Hydration** task is **Skipped**, it indicates that not all requirements were met to enable automatic linking.
- The task updates every row in the target table, updates the LastModifiedOn timestamp for the customer profile, and links records. If you have workflows such as triggers associated with the Update event on a table you intend to link, disable the triggers before the first unification to avoid triggering on each record.
- The *InsightsAppsPlatform* (IAP) service account performs the linking. Logs might reference the *InsightsAppsPlatform* service account as either *insightsappsplatform@onmicrosoft.com* or *#InsightsAppsPlatform*.

[!INCLUDE [footer-include](includes/footer-banner.md)]
