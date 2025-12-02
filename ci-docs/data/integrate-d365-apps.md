---
title: Automatically link Dynamics 365 apps to customer profiles
description: Learn how the Customer Insights - Data unified profile can be used with other Dynamics 365 applications.
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.topic: integration
ms.date: 12/02/2025
ms.custom: bap-template
---

# Automatically link Dynamics 365 apps to customer profiles

With automatic linking, you can use extended insights from the unified customer profile from Customer Insights - Data to work with your Dynamics 365 contacts, leads, and other customer tables. You can easily access data that is associated with a customer, including:

- Customer profile attributes, such as "loyalty tier"
- Customer measures, such as "Days since last claim"
- Customer activities that are calculated as a measure, such as "Total purchases" and "Number of purchases in the last four months"

## Examples

- A Dynamics 365 Sales admin easily links to a customer lifetime value (CLV) or lead score from Customer Insights - Data. The data then appears on a sales agent's **Leads** page and provides more details about a customer's interests, activity history, and insights.
- A Dynamics 365 Support admin updates their contact measures to show the number of support issues during the last month, the last year, and the lifetime for a customer.
- A Customer Insights – Journeys marketing manager uses the loyalty tier data to personalize a new product announcement.

## Requirements

- Dataverse source tables come from the Dataverse environment that Customer Insights - Data is linked to. Linking isn't supported for tables from other Dataverse environments.
- Dataverse source tables, such as the leads table, must be ingested into Customer Insights - Data through the [Microsoft Dataverse connector](connect-dataverse.md) (recommended) or the [Power Query Dataverse connector](connect-power-query.md). Don't change the names of the source tables.
- The primary key that is selected for each Dataverse table during the [Describe customer data step for unification](data-unification-map-tables.md) is the actual primary key for the table. For example, the standard primary keys for the contact and lead tables are `ContactId` and `LeadId`.
- Your Customer Insights - Data environment is set up for individual customers. Linking isn't supported for business (B2B) environments.

> [!NOTE]
> Automatic linking isn't supported when Customer Insights - Data output is configured to use your own Azure Data Lake Storage.

## Link to a customer profile

Every time unification is run, the customer profile table is written to Dataverse. If all the requirements are met, Customer Insights automatically updates the unified Dataverse source tables with links to the customer profile table. Source records in each Dataverse table that participated in unification are linked to their associated record in the customer profile table.

The task that performs the linking is named *CustomerId Backstamping Hydration*. To view the results from this task, go to **Settings** > **System**, and select the **Status** tab. When the task runs for the first time on a source table, it adds a lookup column and links each row by populating fields with the appropriate `CustomerID` value. The name of the lookup column is `Customer Profile`, and the schema name is `msdynci_lookupfield_customerprofile`. During subsequent runs, only rows that change are updated.

> [!TIP]
> We recommend [configuring filtering attributes](/powerapps-docs/powerapps-docs/developer/data-platform/best-practices/business-logic/include-filtering-attributes-plugin-registration.md) on your plugins and limiting them to only the field names relevant to your business logic. Avoid including fields such as `msdynci_lookupfield_customerprofile` if they aren’t needed. This helps prevent unintended plugin executions during backstamping, which can be especially important on the initial backstamping run when many contacts may be processed.

### CustomerId Backstamping Hydration task

- If the status of the *CustomerId Backstamping Hydration* task is *Skipped*, automatic linking wasn't enabled because not all the requirements were met.
- The task updates every row in the target table, updates the `LastModifiedOn` timestamp for the customer profile, and links records. If workflows such as triggers are associated with the update event on a table that you intend to link, disable the triggers before the first unification to prevent triggering on each record.
- The *InsightsAppsPlatform* (IAP) service account performs the linking. Logs might reference this service account as either *insightsappsplatform@onmicrosoft.com* or *#InsightsAppsPlatform*.

[!INCLUDE [footer-include](includes/footer-banner.md)]
