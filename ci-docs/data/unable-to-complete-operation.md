---
title: Unable to complete the operation
description: Learn how to fix an operation that can't complete in Dynamics 365 Customer Insights - Data.
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.date: 12/08/2025
---
# Unable to complete the operation

This article provides a resolution for an issue where Customer Insights - Data can't complete a one-off operation.

## Symptoms

This error occurs when you try to run an operation, such as creating a new segment or performing unification, and the cache of the ingested source data isn't available. Customer Insights - Data persists ingested data only for a short period to support processing. If the data expires and you attempt one-off operations without refreshing, the system can’t complete the task.

> [!NOTE]
> A full system refresh avoids this issue because it refreshes all data sources before processing.

## Resolution

Refresh all data sources before retrying the operation. You can do this in two ways:

**Data source refresh**:

  1. Go to **Data** > **Data sources**.

  1. Select all sources and choose **Refresh**. Learn more in [data source refresh](data-sources-manage.md#refresh-data-sources).

**System refresh**:

  1. Go to **Settings** > **System** and select the **Schedule** tab.

  1. Schedule automatic refreshes of all your ingested data sources. Learn more in [system refresh](schedule-refresh.md).