---
title: "Connections to other services from Customer Insights."
description: "Share data to other services."
ms.date: 02/15/2021
ms.reviewer: nikeller
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connections (preview) overview

Connections are the key to enable data sharing from Customer Insights. Each connection establishes data sharing with a specific service. Connections are the foundation to [configure exports](export-destinations.md). The same connection can be used by multiple times. For example, one connection to Dynamics 365 Marketing works for multiple exports.
 
Only administrators can configure new connection but the can grant access to contributors for exisiting connections. Administrators control where data can go, contributors define the payload and frequency fitting their needs. For more information, see [Allow contributors to use a connection for exports](#allow-contributors-to-use-a-connection-for-exports).

Go to **Admin** > **Connections** to create and view connections.

The **Connections** tab shows you all active connections. The list shows a row for each connection. 

Get a quick overview, description, and find out what you can do with each extensibility option on the **Discover** tab.

## Add a new connection

To add connections, you need to have [administrator permissions](permissions.md). If you connect to other Microsoft services, we assume both services are in the same organization.

1. Go to **Admin** > **Connections (preview)**.

1. Go to the **Connections** tab.

1. Select **Add connection** to create a new connection. Choose from the drop-down menu what type of connection you want to create.

1. In the **Set up connection** pane provide the required details. 
   1. The **Display name** and the type of the connection describe a connection when using it to create exports. We recommend choosing a name which explains the purpose and target of this connection.
   1. The exact fields depend on what service you are connecting to. You can learn about details of a specific connection type in the article about the target service.

1. To create the connection select **Save**.

You can also select **Set up** on a tile on the **Discover** tab.

### Allow contributors to use a connection for exports

When setting up or editing a connection you choose which users are allowed to use this specific connection to define [exports](export-destinations.md). By default a connection is available to users with an administrator role. You can change this setting under **Choose who can use this connection** and allow users with contributor role to use this connection.
Connections
- Contributors won't be able to view or edit the connection. They will only see the display name and its type when creating an export..
- By sharing a connection you allow contributors to use a connection. Contributors will see shared connections when they set up exports. They can manage every export using this specific connection.
- You can change this setting while keeping the exports defined by contributors.

## Edit a connection

1. Select the vertical ellipsis for the connection you want to edit.

1. Select **Edit**.

1. Change the values you want to update and select **Save**.

## Remove a connection

If the connection you are removing is used by exports, you first need to disconnect or remove these exports. The remove dialog will guide you to these exports. 
Disconnected exports become inactive. You re-activate them by adding another connection to them on the [Exports](export-destinations.md) page.

1. Select the vertical ellipsis for the connection you want to edit.

1. Select **Remove** from the dropdown menu. A confirmation dialog will appear.

   1. If there are exports using this connection you will see a corresponding message. Activate the button on the message to see these exports in the **Exports** page.
   1. The Exports page will be filtered for the connection you tried to remove. You can choose to either remove or disconnect these exports to be able to remove the connection.
   1. To disconnect any export administrators have access to the **Disconnect** action. This action is available for individual and multiple selected exports.
   1. By disconnection you keep the export config, but it won't be run until another connection is added to it.
   1. Once no export is using this connection navigate to **Connections** page and activate **Remove** again.

1. In the dialog window review the list of affected elements. To confirm the deletion select **Remove**.

