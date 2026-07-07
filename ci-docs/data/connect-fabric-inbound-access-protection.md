---
title: Connect to a workspace with inbound access protection enabled
description: Connect to Delta tables in a Microsoft Fabric OneLake lakehouse with inbound access protection enabled in  Dynamics 365 Customer Insights - Data.
ms.date: 07/06/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Connect to a workspace with inbound access protection enabled

Microsoft Fabric provides inbound access protection for organizations that need enhanced control over connection to a workspace. Use this article to connect Dynamics 365 Customer Insights - Data to a Microsoft Fabric OneLake workspace when **Inbound Access Protection** is enabled.

Inbound access protection helps secure Microsoft Fabric workspaces by restricting access from the public internet. When enabled, public endpoints are disabled and services like Customer Insights – Data must connect through a private link.

Learn more:

- [Limit inbound requests with inbound access protection](/fabric/onelake/onelake-manage-inbound-access)
- [Cross-tenant connections using workspace-level private links](/fabric/security/security-cross-tenant-communication)

When inbound access protection is on, public OneLake endpoints are blocked. To allow access, you must create and validate a workspace-level Private Link in Azure, then complete the data source connection in Customer Insights - Data.

## Prerequisites

- The Fabric tenant setting **Users can access data stored in OneLake with apps external to Fabric** is enabled. Learn more in [Enable external access to OneLake data](connect-fabric-onelake.md#enable-the-service-principal-in-the-fabric-tenant).

- The Customer Insights - Data service principal is granted the required permissions to the Fabric workspace. Learn more in [Add Customer Insights - Data service principal to the Fabric workspace](connect-fabric-onelake.md#add-customer-insights---data-service-principal-to-the-fabric-workspace).

- A Private Link service is created in Azure for the workspace, and you have access to that resource. Go to [Step 2: Set up and use workspace-level Private Links](/fabric/security/security-workspace-level-private-links-set-up?tabs=fabric-portal#step-2-create-the-private-link-service-in-azure).

- You or someone in your organization is ready to approve pending private endpoint connections in Azure.

## Create a Private Link for the workspace

Create a Private Link for the Fabric workspace in Customer Insights - Data, then ask your Azure admin to approve the pending private endpoint connections.

### Step 1: Create the workspace Private Link

1. In Customer Insights - Data, go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Microsoft Fabric OneLake**.

1. Select the **Enable Azure Private Link** checkbox.

   :::image type="content" source="media/connect-fabric-inbound-access-protection/fabric-onelake-private-link.png" alt-text="Screenshot of adding Fabric OneLake using a Private Link.":::

1. In the **Fabric workspace Private Link** dropdown, select the Fabric Private Link service resource in Azure that corresponds to the workspace. The Azure admin creates and names the Private Link service specifically for each workspace, so the name should be clearly associated with the workspace name.

1. Select **Create Private Link**.

### Step 2: Approve pending endpoint connections

An Azure admin must approve pending Private Link requests. Ask your Azure admin to:

1. Open the Azure portal.

1. Go to **Network Foundation**.

1. Select **Pending connections**.

1. Find the two pending private endpoint requests.

1. Approve both connections.

Users can't use the Private Link until you approve both endpoint connections.

### Step 3: Validate the Private Link

1. Return to the Fabric Private Link configuration page.

1. Select **Validate Private Link**.

1. Confirm validation succeeds.

> [!IMPORTANT]
> Changes can take several minutes to propagate after the endpoint approvals are completed. If validation initially fails, wait a few minutes and try again.

## Connect to your workspace in Customer Insights - Data

After the Private Link validates successfully, [Connect to Microsoft Fabric OneLake](connect-fabric-onelake.md) to ingest data from the workspace.

## Troubleshooting

### The Fabric workspace Private Link list is empty, or my workspace isn't listed

If you don't see an obvious Private Link service for the workspace, it's possible the Private Link service isn't created in Azure, or you don't have access to the resource. Contact your Azure admin to create the Private Link service or give you access as appropriate. Learn more in [Step 2: Create the Private Link service in Azure](/fabric/security/security-cross-tenant-communication).

### Private Link validation fails

Verify that:

- Both pending endpoint connections are approved.

- The approvals had sufficient time to propagate.

- The workspace Private Link is created successfully.

### The table list appears hung during refresh, or appears empty

An empty table list usually indicates that Customer Insights – Data doesn't have permission to access or read the contents of the workspace. Verify workspace permissions, external access settings, and that the Private Link is successfully validated.


[!INCLUDE [footer-include](includes/footer-banner.md)]
