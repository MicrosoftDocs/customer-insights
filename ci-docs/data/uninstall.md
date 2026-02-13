---
title: Uninstall or remove Customer Insights - Data
description: Learn how to remove Dynamics 365 Customer Insights - Data from an environment.
ms.date: 02/13/2026
ms.topic: how-to
author: dleblondMSFT
ms.author: dleblond
ms.reviewer: mhart
ms.custom: bap-template
---

# Uninstall or remove Customer Insights - Data

You can remove Customer Insights - Data from a Dynamics 365 environment. Removing Customer Insights - Data deletes the configuration and data associated with the instance.

> [!IMPORTANT]
> Removing Customer Insights - Data is a permanent action. All data, configurations, segments, measures, exports, and predictions associated with the instance are deleted and cannot be recovered.

## Prerequisites

- Admin role in Customer Insights - Data
- Admin role in the Power Platform environment
- No active exports or downstream dependencies that rely on Customer Insights - Data output

## Before you begin

Before removing Customer Insights - Data, assess the impact on your environment:

| Item | Impact of removal |
|------|-------------------|
| Unified customer profiles | Deleted from Dataverse |
| Segments and measures | Deleted; any downstream journeys or flows that reference them will fail |
| Configured data sources | Disconnected; source data in Azure Data Lake or Dataverse is not deleted |
| Exports | Stopped; destination systems retain previously exported data |
| Predictions and AI models | Deleted |
| Environment storage | Dataverse storage consumed by Customer Insights - Data tables is freed |

**Recommended steps before removal:**
1. Export any data you need to retain (customer profiles, segments, measures)
2. Deactivate all active exports
3. Notify users who depend on Customer Insights - Data outputs (for example, Power Automate flows, Power BI reports, Dynamics 365 journeys)

## Remove Customer Insights - Data

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
2. Select **Environments** and choose the environment from which you want to remove Customer Insights - Data.
3. Select **Resources** > **Dynamics 365 apps**.
4. Find **Dynamics 365 Customer Insights** in the list, select the **...** menu, and then select **Uninstall**.
5. Confirm the removal when prompted.
6. Wait for the uninstall process to complete. This can take several minutes.

## Verify removal

After the uninstall completes:

1. In the Power Platform admin center, verify that **Dynamics 365 Customer Insights** no longer appears under **Resources** > **Dynamics 365 apps** for the environment.
2. Verify that Customer Insights - Data tables (prefixed with `msdynci_`) have been removed from Dataverse by going to **Power Apps** > **Tables**.
3. Confirm that the Customer Insights - Data application URL for the environment no longer loads.

> [!NOTE]
> If some Customer Insights - Data solutions remain after uninstalling, you can remove them manually from the Power Platform admin center under **Solutions**. Contact [Support](https://admin.powerplatform.microsoft.com/support) if you encounter issues during manual solution removal.

## Reinstall Customer Insights - Data

If you need to reinstall Customer Insights - Data on the same or a different environment, follow the standard provisioning process. For more information, see [Create a Customer Insights - Data environment](create-environment.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
