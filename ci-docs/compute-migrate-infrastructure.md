---
title: Recreate the private links for the upgrade of the new compute infrastructure
description: Learn how to update the private links for the upgrade of the compute infrastructure
ms.date: 13/07/2023
ms.reviewer: mhart
ms.topic: how-to
author: mamihail
ms.author: mamihail
ms.custom: bap-template
---

# Recreate the private links for the upgrade of the new compute infrastructure

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics Customer Insights is upgrading the compute infrastructure to newer technology, aiming to increase the reliability and performance of the big data computation we do for our customers. The new solution needs to obtain access to customer storage protected by private networks and firewalls, through Private Links. The private links created historically in the Customer Insights for security reasons are not transferable to the new infrastructure.

## Required action

 Recreate the private links for the customer storages used in Customer Insights 

## Prerequisites

- Customer Insights: Administrator
- Azure built-in role: Storage Account Contributor
- Permissions for custom Azure role: Microsoft.Storage/storageAccounts/read and Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action

## How to update your private links 

A notification in Customer Insights indicates that there are private links for which you need to take action.

:::image type="content" source="media/compute-migration-create-private-links.png" alt-text="Screenshot of a notification to update private links. ":::

1. Sign in to Customer Insights and open the environment to upgrade.

1. Go to **Settings** > **Permissions**  and select the  **Private links** tab.  

1. Recreate the private links for all the used storages that are protected by private links 

1. Click Add Private Link button.

 - The Add Private Link pane lists storage accounts in your tenant that you can see.

 - Select the subscription, resource group, and storage account.

 - Review the data privacy and compliance and select I agree.

 - Select Save.

:::image type="content" source="media/compute-migration-create-private-links-CI.png" alt-text="Screenshot of a notification to update private links. ":::

1. Approve the Private Links in the Azure portal

After configuring the Private Links between Customer Insights and your virtual network protected storage, four Private Links show on the Private Links tab in Customer Insights with a status of Pending.

- In the Azure portal, go to your Data Lake Storage account, and select Networking > Private endpoints connections to see the four new Private Links.

:::image type="content" source="media/compute-migration-create-private-links-pending.png" alt-text="Screenshot of a notification to update private links. ":::

- Select all and click Approve.

:::image type="content" source="media/compute-migration-create-private-links-approve.png" alt-text="Screenshot of a notification to update private links. ":::

- In Customer Insights, go to Settings > Permissions and select the Private Links tab. The Private Links in Customer Insights now show the status Approved.

:::image type="content" source="media/compute-migration-create-private-links-CI-approved.png" alt-text="Screenshot of a notification to update private links. ":::

It's important to approve all four private links for each storage. 


## What to expect after the recreating the private links

All the jobs should continue to run normally.

At the due date we will perform the migration of the instances on the new compute infrastucture. 

