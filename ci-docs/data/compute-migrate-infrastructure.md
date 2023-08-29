---
title: Recreate your private links for the upgrade to the new compute infrastructure
description: Learn how to update the private links for the upgrade of the compute infrastructure
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: mamihail
ms.author: mamihail
ms.custom: bap-template
ROBOTS: NOINDEX
---

# Recreate your private links for the upgrade to the new compute infrastructure

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 Customer Insights - Data is upgrading the compute infrastructure to newer technology, designed to increase the reliability and performance of the big data computation. The new solution requires access to customer storage protected by private networks and firewalls through Azure Private Links. Existing private links are not transferable to the new infrastructure.

A notification in the application indicates if you have private links you need to recreate.

:::image type="content" source="media/compute-migration-notification-CI.png" alt-text="Screenshot of a notification to update private links in Customer Insights.":::

> [!IMPORTANT]
> The due date for creating the required private links is September 1, 2023. If the private links are not recreated by this date, errors occur when performing operations such as data ingestion, segment refreshing, measures, activities, and other tasks.

## Prerequisites

- Customer Insights - Data role: Administrator
- Azure built-in role: [Storage Account Contributor](/azure/role-based-access-control/built-in-roles#storage-account-contributor)
- Permissions for custom Azure role: [Microsoft.Storage/storageAccounts/read and Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action](/azure/role-based-access-control/resource-provider-operations#microsoftstorage)

## Update your private links

1. Sign in to Customer Insights - Data and open the environment to upgrade.

1. [Recreate the private links](private-link.md#set-up-a-private-link-directly-from-the-private-links-page-in-customer-insights---data) for all the used storage that are protected by private links.

   :::image type="content" source="media/compute-migration-create-private-links-CI.png" alt-text="Screenshot of creating private links in Customer Insights. ":::

## Approve the Private Links in the Azure portal

After configuring the Private Links between Customer Insights and your virtual network protected storage, four Private Links show on the **Private Links** tab with a status of **Pending**.

[Approve the Private Links](private-link.md#approve-your-private-link-in-the-azure-portal).

It's important to approve all four private links for each storage.

After recreating the private links, all jobs should continue to run normally. At the due date, we'll perform the migration of the environments on the new compute infrastructure.

