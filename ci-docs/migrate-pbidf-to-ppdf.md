---
title: Migrate dataflows for Power Query-based data sources.
description: 
ms.date: 06/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.custom: bap-template
---

# Migrate dataflows for Power Query-based data sources

To increase scalability, reliability, and performance, some Power Query-based data sources need to get updated. [Dataflows](/power-query/dataflows/understanding-differences-between-analytical-standard-dataflows) are cloud-based data preparation technologies that use Power Query to extract, transform, and load data. A system job scans for data sources with analytical dataflows and migrates them to standard dataflows.

## Prerequisites

- You have Administrator or Owner permissions in Customer Insights.
- The Customer Insights environment is connected a Dataverse environment.
- You have access to the credentials for the data source.

## How to update your data sources  

A notification in Customer Insights indicates that there are data sources for which you need to take action.
We recommend following the steps for trial and sandbox environments before updating the data sources on the production environment.  

:::image type="content" source="media/migrade-data-sources.png" alt-text="Screenshot of a notificaiton to migrate data sources. ":::

1. Sign in to Customer Insights and open the environment to upgrade.

1. Go to **Data** > **Data sources**.  

1. In the list of data sources, the Power Query-based data sources show a **Credentials Required** status.

1. Edit the data source and enter the credentials without making changes to the query steps. Select **Next** then **Save**. The progress indicator for the data source shows in the status as **Upgrade pending**, **Upgrade in progress**, or **Successful**.

1. Power Query-based data sources can now refresh on their own schedule. Set up the refresh schedule for the data source.

After all the updated data sources have refreshed successfully, go to **Data** > **Unify** and select **Unify** > **Unify customer profiles and downstream dependencies** to run a full refresh.

If you run into issues, create a support ticket.  

## What to expect after the migration

Power Query data sources now refresh on their own schedule, independent from the system refresh of the environment.

Power Query data sources no longer appear as shared data sources. They show in the **Managed by you** section on **Data** > **Data sources**. You can change ownership of the data source after the upgrade is complete.

A temporary data source with a similar name may show under **Administration** > **System** which gets removed by the system after a full successful refresh.
