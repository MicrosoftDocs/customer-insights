---
title: Set up an Azure Private Link
description: Learn how to set up an Azure Private Link to connect your Data Lake Storage.
ms.date: 10/29/2024
ms.topic: how-to
author: AndreaAczel
ms.author: anaczel
ms.reviewer: mhart
ms.custom: bap-template
---

# Set up an Azure Private Link

[Azure Private Link](/azure/private-link/private-link-overview) lets Dynamics 365 Customer Insights - Data connect to your Azure Data Lake Storage account over a private endpoint in your virtual network. For data in a storage account, which isn't exposed to the public internet, Private Link enables the connection to that restricted network.

> [!NOTE]
> Customer Insights - Data is migrating from Azure Private Link to managed identities for Azure resources. During the migration, you might set up connections using Azure Private Link or managed identities. When setting up a connection to you Azure storage container, **Enable private link** indicates you'll use Private Link. This article explains the set up process. **This storage account is behind a firewall** indicates you'll use managed identities. Go to [Set up managed identities](managed-identities.md).

There are three scenarios where Customer Insights - Data can be configured to connect to firewall-protected Azure storage containers:

- Output storage that can be configured at setup to use your own Azure data lake.
- Data sources that read from an Azure data lake storage (Common Data Models (CDM) or Delta tables).
- Exports that write to an Azure data lake.

## Prerequisites

- Minimum role requirement to set up a Private Link connection:
  - Customer Insights - Data: Administrator
  - Azure built-in role: [Storage Account Contributor](/azure/role-based-access-control/built-in-roles#storage-account-contributor)
  - Permissions for custom Azure role: [Microsoft.Storage/storageAccounts/read and Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action](/azure/role-based-access-control/resource-provider-operations#microsoftstorage)

## Set up a Private Link when creating a Customer Insights - Data environment

When creating a [Customer Insights - Data environment](create-environment.md) that connects to your virtual network protected storage:

1. Select **Enable Azure Private Link**.

1. Select **Create Private Link** to initiate the creation process.

1. [Approve the Private Link](#approve-your-private-link-in-the-azure-portal) in the Azure portal.

1. Once all links are approved, select **Validate Private Link**. Upon successful validation, you can continue configuring your new environment.

## Set up a Private Link when creating a data source

When creating an [Azure Data Lake Storage data source](connect-common-data-model.md) that needs to connect to a storage protected by a virtual network, follow the same steps as described under [Setting up a private link when creating a Customer Insights - Data environment](#set-up-a-private-link-when-creating-a-customer-insights---data-environment).

## Set up a Private Link directly from the Private Links page in Customer Insights - Data

1. In Customer Insights - Data, go to **Settings** > **Permissions** and select the **Private Links** tab.

1. Select **Add Private Link**.

   The **Add Private Link** pane lists storage accounts in your tenant that you can see.

1. Select the subscription, resource group, and storage account.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save**.

## Approve your Private Link in the Azure portal

After configuring the Private Link between Customer Insights - Data and your virtual network protected storage, four Private Links show on the **Private Links** tab in Customer Insights - Data with a status of **Pending**.

1. In the Azure portal, go to your Data Lake Storage account, and select **Networking** > **Private endpoints connections** to see the four new Private Links.

1. Select **Yes** to approve them.

   > [!TIP]
   > For easy identification, consider adding a description when approving the Private Links.

    :::image type="content" source="media/Private-Endpoint-Approval.png" alt-text="Description for the private endpoint approval step.":::

1. In Customer Insights - Data, go to **Settings** > **Permissions** and select the **Private Links** tab. The Private Links now show the status **Approved**.

1. Continue to add your [data sources](connect-common-data-model.md) that are linked to your protected storage.

## Delete an Azure Private link

1. In Customer Insights - Data, go to **Settings** > **Permissions** and select the **Private Links** tab.

1. Select the storage account name for which you would like to delete the Private Links.

1. Select **Delete**.

[!INCLUDE [footer-include](includes/footer-banner.md)]