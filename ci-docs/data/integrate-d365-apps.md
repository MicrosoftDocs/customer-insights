---
title: Integrate with Dynamics 365 applications (preview)
description: Learn how Customer Insights - Data can be used with other Dynamics 365 applications
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.topic: conceptual
ms.date: 12/07/2023
ms.custom: bap-template
---

# Integrate with Dynamics 365 applications (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 customers can access more data and insights made available by the unified customer profile while working with a contact or lead. When unification is run, Customer Insights – Data creates a relationship from each contact or lead to the associated customer profile table by creating a standard Microsoft Dataverse lookup column called CustomerID that links the records. From this link, you can view the details of a contact or lead and easily access the extended information and insights for that contact or lead from Customer Insights – Data.

To link contacts or leads to a unified customer profile, the contact or lead tables must be imported to Customer Insights – Data through the [Microsoft Dataverse connector](connect-dataverse.md) or the [Power Query Dataverse connector](connect-power-query.md) and [unified.](data-unification.md) Other data connector types will be supported in the upcoming months. When unification runs, a relationship is created between the Dataverse tables that were unified and the customer profile table. Contacts, leads, and other Dataverse records can natively reference their associated unified customer profile using the Dataverse relationship. In addition, the customer profile table provides relationships to [measures](measures.md) tables, making measures easily accessible.

Examples of using this native linking include:

- A sales team member viewing a lead can see additional information from the unified profile such as the customer lifetime value, lifetime purchases, churn risk, and other data. The team member can make better decisions on which leads to pursue and has access to data to help foster stronger relationships, knowing their customer’s interests, activity history, and insights. All of this information is accessible seamlessly in their contact/lead view.

- A marketing team can personalize email communications and thoughtfully branch a journey based on data in the unified profile, providing a distinct journey experience for customers based on data not previously available in Dynamics 365.

- Service reps can provide personalized service knowing the customer’s loyalty tier or prediction to churn.

## Requirements

- Source tables, such as the contact table, must be ingested directly from the default Dataverse environment, through the [Microsoft Dataverse connector](connect-dataverse.md) or the [Power Query Dataverse connector.](connect-power-query.md)
- Only source tables from Dataverse that are included in unification can be linked to the customer profile.
- On the [Describe customer data step for unification](data-unification-map-tables.md), the source table's primary key must correspond to the table's actual primary key. For example, the standard contact and lead tables primary keys are *ContactId* and *LeadId*.

> [!NOTE]
> Customer Insights - Data environments configured to write output to a private data lake aren't supported.

## Native linking task

The task that updates the Dataverse tables with a link to the customer profile is called **CustomerId Backstamping Hydration**. To see the results from the task, go to **Settings** > **System** and select the **Status** tab. The taks is under **Dataverse Hydration**. The status can be Successful, Failed, or Skipped. This task runs asynchronously and doesn't block or delay any other task.

When the status is **Skipped**, the status details may show "Error: Linking of Dataverse tables to the CustomerProfile table is skipped." or "Error: The backstamping job is skipped. It only runs when unification setup contains tables that are ingested to Customer Insights from the same Dataverse organization that was configured or selected during instance creation."

In Dataverse, the source table such as the Contact table, is updated by the *InsightsAppsPlatform* (IAP) service account. This is the service account that is used to create the Lookup column and write the appropriate foreign key value to that column for each row. Only the value in the lookup column is updated. The first time this job runs, it updates every row. Subsequent runs only update changed or new rows.

[!INCLUDE [footer-include](includes/footer-banner.md)]
