---
title: Work with Customer Insights - Data and Microsoft Dataverse
description: Learn how to connect Customer Insights and Microsoft Dataverse and understand the output tables that are exported to Dataverse.
ms.date: 09/01/2023
ms.topic: conceptual
author: kishorem
ms.author: kishorem
ms.custom: bap-template
---

# Work with Customer Insights - Data and Microsoft Dataverse

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 Customer Insights - Data makes its output tables available in [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro). This integration enables easy data sharing and custom development through a low code/no code approach. The output tables are available as tables in a Dataverse environment. You can use the data for any other application based on Dataverse tables. These tables enable scenarios like automated workflows through Power Automate or building apps with Power Apps.

You can also [ingest data from on-premises data sources using Power Platform dataflows and gateways](connect-power-query.md#add-data-from-on-premises-data-sources) into your Dataverse environment.

## Prerequisites

- Customer Insights and Dataverse environments must be hosted in the same region.
- A global administrator role set up in the Dataverse environment. Verify if this [Dataverse environment is associated](/power-platform/admin/control-user-access#associate-a-security-group-with-a-dataverse-environment) to certain security groups and make sure you're added to those security groups.
- A Common Data Service/Dataverse [license is assigned](/power-platform/admin/create-users#to-assign-a-license) to you to get Read-Write access mode. Unlicensed administrators get Administrative access mode only.
- No other Customer Insights - Data environment already associated with the Dataverse environment you want to connect. Learn how to [remove an existing connection to a Dataverse environment](#remove-an-existing-connection-to-a-dataverse-environment).
- A Microsoft Dataverse environment connected to a single storage account if you configure the environment to [use your Azure Data Lake Storage](own-data-lake-storage.md).

## Dataverse storage capacity entitlement

A Customer Insights - Data subscription entitles you to extra capacity for your organization's existing [Dataverse storage capacity](/power-platform/admin/capacity-storage). The added capacity depends on the number of profiles that your subscription uses.

**Example:**

Assuming you get 15-GB database storage and 20-GB file storage per 100,000 customer profiles. If your subscription includes 300,000 customer profiles, your total storage capacity is 45 GB (3 x 15 GB) database storage and 60-GB file storage (3 x 20 GB).

Log capacity isn't incremental and fixed for your organization.

For more information about the detailed capacity entitlements, see [Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/?LinkId=866544).

## Connect a Dataverse environment to Customer Insights - Data

The **Microsoft Dataverse** step lets you connect Customer Insights - Data with your Dataverse environment while [creating an environment](create-environment.md).





## Output tables in Dataverse

Some output tables are available in Dataverse. For more information, see [Customer Insights - Data tables in Dataverse](tables.md#customer-insights---data-tables-in-dataverse).


