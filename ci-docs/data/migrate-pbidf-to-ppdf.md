---
title: Migrate dataflows for Power Query-based data sources.
description: Learn how to upgrade dataflows when your Power Query data sources are upgraded.
ms.date: 09/09/2025
ms.reviewer: alfergus
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Migrate dataflows for Power Query-based data sources

To increase scalability, reliability, and performance, some Power Query-based data sources need to get updated. [Dataflows](/power-query/dataflows/understanding-differences-between-analytical-standard-dataflows) are cloud-based data preparation technologies that use Power Query to extract, transform, and load data. A system job scans for data sources that qualify for upgrade and migrates them as new dataflows.

## Prerequisites

- You have Administrator or Owner permissions in Dynamics 365 Customer Insights - Data.
- The Customer Insights - Data environment is connected a Dataverse environment.
- You have access to the credentials for the data source.

## How to update your data sources  

A notification in Customer Insights - Data indicates that there are data sources for which you need to take action.
We recommend following the steps for trial and sandbox environments before updating the data sources on the production environment.  

:::image type="content" source="media/migrade-data-sources.png" alt-text="Screenshot of a notification to migrate data sources. ":::

1. Sign in to Customer Insights - Data and open the environment to upgrade.

1. Go to **Data** > **Data sources**.  

1. In the list of data sources, the Power Query-based data sources show a **Credentials Required** status.

1. Edit the data source and enter the credentials without making changes to the query steps. Select **Next** then **Save**. The progress indicator for the data source shows in the status as **Upgrade pending**, **Upgrade in progress**, or **Successful**.

1. Power Query-based data sources can now refresh on their own schedule. For more information, see [Set the refresh frequency](/power-apps/maker/data-platform/create-and-use-dataflows#set-the-refresh-frequency).

After all the updated data sources have refreshed successfully, go to **Data** > **Unify** and select **Unify** > **Unify customer profiles and downstream dependencies** to run a full refresh.

If you run into issues, create a support ticket.  

## What to expect after the migration

Power Query data sources now refresh on their own schedule, independent from the system refresh of the environment.

Power Query data sources no longer appear as shared data sources. They show in the **Managed by you** section on **Data** > **Data sources**. Environment administrators can change ownership of the dataflow after the upgrade is complete in the Power Platform admin center.

A temporary data source with a similar name may show under **Administration** > **System** which gets removed by the system after a full successful refresh.

## Next steps

- [Connect to a Power Query data source](connect-power-query.md)
- [Data sources overview](data-sources.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]