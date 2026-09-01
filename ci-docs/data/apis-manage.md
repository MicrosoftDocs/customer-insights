---
title: Manage Customer Insights - Data APIs
description: Manage API keys in Dynamics 365 Customer Insights - Data to enable or block environment access. Review API calls, data transfer, and operations.
ms.date: 08/31/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom:
 - ai-gen-docs-bap
 - ai-seo-date: 08/31/2026
ai-usage: ai-assisted
---

# Manage Customer Insights - Data APIs

[!INCLUDE [api-deprecate](./includes/api-deprecate.md)]

Set up the keys to use the Dynamics 365 Customer Insights - Data APIs and view the API usage.

## Manage API keys

View and manage the keys to use the [Customer Insights - Data APIs](apis.md) with the data in your environment.

1. Go to **Settings** > **Permissions** and select the **APIs** tab.

1. To set up API access to the environment, select **Enable**. To block API access to the environment, select **Disable**, and confirm.

1. Manage the primary and secondary API keys:

   1. To show the primary or secondary API key, select the **Show** symbol.

   1. To copy the primary or secondary API key, select the **Copy** symbol.

   1. To create new primary or secondary API keys, select **Regenerate primary** or **Regenerate secondary**.

## View API usage

View details about the real-time Customer Insights - Data API usage and see which events happened in a given time frame.

1. Go to **Settings** > **System** and select the **API usage** tab.

1. **Select a time frame** to view.

   The **API usage** page contains three sections:

   - **API calls** - a chart that visualizes the aggregated number of calls to the API in the selected time frame.
   - **Data transfer** - a chart that shows the amount of data that was transferred through the API in the selected time frame.
   - **Operations** - a table with rows for each available API operation and details about the usage of the operations. Select an operation name to go to [the API reference](https://developer.ci.ai.dynamics.com/api-details#api=CustomerInsights&operation=Get-all-instances).

[!INCLUDE [footer-include](includes/footer-banner.md)]
