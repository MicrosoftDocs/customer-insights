---
title: Data refresh notifications
description: Learn how data refresh notifications in Customer Insights - Data alert admins to permanent failures, suppress transient failures, and help you act fast.
ms.date: 04/23/2026
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: alfergus
ms.service: customer-insights
ms.subservice: customer-insights-data
ms.custom: bap-template
---

# Data refresh notifications

Data refresh notifications in Customer Insights - Data help environment admins identify permanent refresh failures without unnecessary alerts. This article explains what triggers a notification, how transient failures are suppressed, and how to respond when action is required.

## Failure types

When a refresh task fails, Customer Insights - Data automatically attempts to recover by retrying the failed step. Not every failure requires admin intervention - many failures are transient. The system detects a recoverable condition and retries successfully without any action on your part.

To reduce unnecessary alerts and avoid notifying admins for failures that resolve automatically, Customer Insights - Data classifies every failure as one of two types:

| Failure type | Description | Notification sent? |
|---|---|---|
| **Failed (retrying)** | The task failed but is being automatically retried. The system expects to recover without admin action. | No |
| **Failed (permanent)** | All retry attempts are exhausted, or the task timed out. Task timeouts always generate a notification. The failure or time out requires investigation. | Yes |

You can see the current failure classification for any task in the [system status view](system.md#view-system-status). Tasks actively being retried show a **Failed (retrying)** status. Tasks that permanently failed show **Failed (permanent)**. For a full description of all task statuses, see [Status definitions](system.md#status-definitions).

## Email notifications

The system sends email notifications to environment admins only when a permanent failure occurs. The following events can result in a permanent failure notification:

| Notification type | Trigger |
|---|---|
| Refresh failure | A data source, unification, segment, measure, or export task permanently fails after all retries are exhausted |
| Refresh failure | A task times out |
| Refresh skipped | A downstream process is skipped because an upstream task permanently failed |

Customer Insights - Data sends notifications to all users with the **Admin** role. The notification goes to the email address associated with each admin's account.

> [!TIP]
> If you previously received frequent failure alerts for jobs that appeared healthy the next time you checked, those alerts likely indicated transient failures. This update automatically suppresses those alerts.

## Respond to a permanent failure notification

When you receive a permanent failure notification, it means the system exhausted all automatic recovery options and the failure requires your attention.

1. Go to **Settings** > **System** and select the **Status** tab.

1. Find the failed task. Select its status to open the **Progress details** pane.

1. Review the error details and identify the root cause.

1. Take corrective action. For example:
   - For a **data source** failure: check connectivity, credentials, and source availability. Learn more in [Manage data sources](data-sources-manage.md).
   - For a **unification** failure: review your match and merge rules for configuration issues. Learn more in [Data unification overview](data-unification.md).
   - For a **segment or measure** failure: check for broken references or data quality issues. Learn more in [Work with segments](segments.md) and [Create and manage measures](measures.md).
   - For an **export** failure: verify the export destination connection is valid. Learn more in [Export destinations overview](export-destinations.md).

1. After resolving the root cause, trigger a manual refresh or wait for the next scheduled refresh to confirm the issue is resolved.

## Configure the refresh schedule

Permanent failures that occur repeatedly during scheduled refreshes can indicate a persistent issue with a data source or configuration. To adjust when refreshes run or to reduce the frequency of overnight alerts, see [Schedule system refresh](schedule-refresh.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
