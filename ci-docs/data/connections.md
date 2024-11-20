---
title: "Connections (preview) overview"
description: "Connections to other services from Customer Insights - Data."
ms.date: 12/21/2023
ms.reviewer: mhart
ms.topic: overview
author: Scott-Stabbert
ms.author: sstabbert
---

# Connections (preview) overview

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Connections are the key to enable data sharing to and from Dynamics 365 Customer Insights - Data. Each connection establishes data sharing with a specific service. Use connections to [configure non-Microsoft enrichments](enrichment-manage.md) and [configure exports](export-manage.md). The same connection can be used multiple times. For example, one connection to Dynamics 365 Customer Insights - Journeys works for multiple exports and one Leadspace connection can be used for several enrichments.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Export connections

Only administrators can configure new connections, but they can [grant access to contributors](#allow-contributors-to-use-a-connection-for-exports) to use existing connections. Administrators control where data can go, contributors define the payload and frequency fitting their needs.

## Enrichment connections

Only administrators can configure new connections, but the created connections are always available to both administrators and contributors. Administrators manage credentials and give consent to data transfers. Administrators and contributors can use the connections for enrichments.

## Add a new connection

### Prerequisites

- [Administrator permissions](user-roles.md#admin)
- Other Microsoft services, if any, are in the same organization

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose the type of connection you want to create. Or, go to the **Discover** tab and select **Set up** on a connection tile.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Enter the required details. The exact fields depend on what service you're connecting to. For details of a specific connection type, refer to the article about the target service.

1. If you [use your own Key Vault](use-azure-key-vault.md) to store secrets, activate **Use Key Vault** and choose the secret from the list.

1. Review the data privacy and compliance and select **I agree**.

1. Select **Save** to create the connection.

### Data privacy and compliance

When you enable Customer Insights - Data to transmit data to third parties or other Microsoft products, you allow transfer of data (including personal data) outside of Customer Insights. Microsoft transfers such data at your instruction, but you're responsible for obtaining consent to use any data and ensuring that the third party meets any privacy or security obligations you might have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

An administrator can remove the connection at any time to discontinue use of the functionality.

## Allow contributors to use a connection for exports

When setting up or editing an export connection, choose which users are allowed to use this specific connection to define [exports](export-manage.md). By default, a connection is available to users with an administrator role. Change the **Choose who can use this connection** setting to allow users with contributor role to use this connection.

- Contributors can't view or edit the connection. They only see the display name and its type when creating an export.
- By sharing a connection, you allow contributors to use a connection. Contributors see shared connections when they set up exports. They can manage every export that uses this specific connection.
- You can change this setting while keeping the existing exports.

## Manage existing connections

1. Go to **Settings** > **Connections**.

1. Select the **Enrichment** or **Exports** tab to view a list of enrichment or export connections, the connection type, when it was created, and who has access. You can sort the list of connections by any column.

1. Select the connection to view available actions.

   - **Edit** the connection.
   - [**Remove**](#remove-a-connection) a connection.

### Remove a connection

If the connection you're removing is used by enrichments or exports, first detach or remove them. The remove dialog guides you to the relevant enrichments or exports.

> [!TIP]
> Deactivated enrichments and detached exports become inactive. You reactivate them by adding another connection to them on the [Enrichments](enrichment-manage.md) or [Exports](export-manage.md) page.

1. Go to **Settings** > **Connections**.

1. Select the **Enrichment** or **Exports** tab.

1. Select the connection you want to remove.

1. Select **Remove** from the dropdown menu. A confirmation dialog appears.

   1. If there are enrichments or exports using this connection, select the button to see what's using the connection.
      - **Exports:** Choose to either **Remove** the export or **Detach the connection**. Detaching the connection keeps the export config, but it doesn't run until another connection is added to it.
      - **Enrichments:** Choose to either **Delete** or **Deactivate** the enrichments.
   1. Once the connection has no more dependencies, go back to **Settings** > **Connections** and try removing the connection again.

1. To confirm the deletion, select **Remove**.

## Set up connections with secrets managed by your own Key Vault

Some connections need secrets like API keys or passwords. Some connections support secrets stored in your own Key Vault. Learn more about supported connections and how to set up on [your own Key Vault](use-azure-key-vault.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
