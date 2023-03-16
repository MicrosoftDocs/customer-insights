---
title: Configure security settings
description: Learn about security settings in Dynamics 365 Customer Insights.
ms.date: 02/28/2023

ms.topic: conceptual
author: AndreaAczel
ms.author: anaczel
ms.reviewer: mhart
---

# Configure security settings

Manage API keys, access customer data, and set up an Azure Private Link.

## Manage API keys

View and manage the keys to use the [Customer Insights APIs](apis.md) with the data in your environment.

1. Go to **Admin** > **Security** and select the **APIs** tab.

1. If API access to the environment has not been set up, select **Enable**. Or, to block API access to the environment, select **Disable** and confirm.

1. Manage the primary and secondary API keys:

   1. To show the primary or secondary API key, select the **Show** symbol.

   1. To copy the primary or secondary API key, select the **Copy** symbol.

   1. To create new primary or secondary API keys, select **Regenerate primary** or **Regenerate secondary**.

## Securely access customer data with Customer Lockbox (Preview)

Customer Insights uses the Power Platform Customer Lockbox capability. Customer Lockbox provides an interface to review and approve (or reject) data access requests. These requests occur when data access to customer data is needed to resolve a support case. To use this feature, Customer Insights must have an existing connection to a Microsoft Dataverse environment in your tenant.

For more information about Customer Lockbox, see the [summary](/power-platform/admin/about-lockbox#summary) of Power Platform Customer Lockbox. The article also describes the [workflow](/power-platform/admin/about-lockbox#workflow) and the required [setup](/power-platform/admin/about-lockbox#enable-the-lockbox-policy) to enable Customer Lockbox.

> [!IMPORTANT]
> Global administrators for Power Platform or Power Platform administrators can approve Customer Lockbox requests issued for Customer Insights.

## Set up an Azure Private Link

[Azure Private Link](/azure/private-link/private-link-overview) lets Customer Insights connect to your Azure Data Lake Storage account over a private endpoint in your virtual network. For data in a storage account, which isn't exposed to the public internet, Private Link enables the connection to that restricted network.

> [!IMPORTANT]
> Minimum role requirement to set up a Private Link connection:
>
> - Customer Insights: Administrator
> - Azure built-in role: [Storage Account Contributor](/azure/role-based-access-control/built-in-roles#storage-account-contributor)
> - Permissions for custom Azure role: [Microsoft.Storage/storageAccounts/read and Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action](/azure/role-based-access-control/resource-provider-operations#microsoftstorage)
>
> Special cases which require creating the Private Link:
> - A Private Link between Customer Insights and the storage account needs to be created even if the storage is accessible from Public Internet but it already has at least a Private Link.

In Customers Insights you can create private links in the following ways:

   - When creating a new Customer Insights environment for which you would like to [Use your own Azure Data Lake Storage account](own-data-lake-storage.md) that is protected by your virtual network.
   - When creating a [data source](connect-common-data-model.md) for which the data is stored in your protected account.
   - Directly from the **Admin** > **Security** > **Private Links** page in Customer Insights.

Regardless of the method you use to create the Private Link, it shows under the **Admin** > **Security** > **Private Links** tab in Customer Insights.

### Set up a Private Link when creating a Customer Insights environment

When creating a [Customer Insights environment](create-environment.md) that connects to your virtual network protected storage:

1. Select **Enable Azure Private Link**.

   :::image type="content" source="media/Private-Endpoint-Creation.png" alt-text="Private endpoint creation.":::

1. Select **Create Private Link** to initiate the creation process. 

1. [Approve the Private Link](#approve-your-private-link-in-the-azure-portal) in the Azure portal.

1. Once all links are approved, select **Validate Private Link**. Upon successful validation, you can continue configuring your new environment.

### Set up a Private Link when creating a data source

When creating an [Azure Data Lake Storage data source](connect-common-data-model.md) that needs to connect to a storage protected by a virtual network, follow the same steps as described under [Setting up a private link when creating a Customer Insights environment](#set-up-a-private-link-when-creating-a-customer-insights-environment).

### Set up a Private Link directly from the Private Links page in Customer Insights

1. In Customer Insights, go to **Admin** > **Security** and select the **Private Links** tab.

1. Select **Add Private Link**.

   The **Add Private Link** pane lists storage accounts in your tenant that you can see.

1. Select the subscription, resource group, and storage account.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save**.

## Approve your Private Link in the Azure portal

After configuring the Private Link between Customer Insights and your virtual network protected storage, four Private Links show on the **Private Links** tab in Customer Insights with a status of **Pending**.

1. In the Azure portal, go to your Data Lake Storage account, and select **Networking** > **Private endpoints connections** to see the four new Private Links.

1. Select **Yes** to approve them.

   > [!TIP]
   > For easy identification, consider adding a description when approving the Private Links.

    :::image type="content" source="media/Private-Endpoint-Approval.png" alt-text="Description for the private endpoint approval step.":::

1. In Customer Insights, go to **Admin** > **Security** and select the **Private Links** tab. The Private Links in Customer Insights now show the status **Approved**. 

1. Continue to add your [data sources](connect-common-data-model.md) that are linked to your protected storage.

## Delete an Azure Private link

1. In Customer Insights, go to **Admin** > **Security** and select the **Private Links** tab.

1. Select the storage account name for which you would like to delete the Private Links.

1. Select **Delete**.

[!INCLUDE [footer-include](includes/footer-banner.md)]
