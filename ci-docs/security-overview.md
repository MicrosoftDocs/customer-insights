---
title: Configure security settings
description: Learn about security settings in Dynamics 365 Customer Insights.
ms.date: 08/02/2022

ms.topic: conceptual
author: m-hartmann
ms.author: mhart
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

In Customers Insights you can create private links in the following ways:

   1. When creating a new Customer Insights environment for which you would like to [Use your own Azure Data Lake Storage account](own-data-lake-storage.md) that is protected by your virtual network.
   1. When creating a [data source](connect-common-data-model.md) for which the data is stored in your protected account.
   1. Directly from the **Admin** > **Security** > **Private Links** page in Customer Insights.

Regardless of the method you use to create the private link, it will show up under the **Admin** > **Security** > **Private Links** tab in Customer Insights.

### Setup a Private Link when creating a Customer Insights environment

When creating a [Customer Insights Environment](create-environment.md) that connects to your virtual network protected storage you need to select the **Enable Azure Private Link** option.

   :::image type="content" source="media/Private-Endpoint-Creation.png" alt-text="Private endpoint creation.":::

Afterwards select the **Create Private Link** option that will initiate the private link creation process. In order to proceed, you will need to [Approve the private links](#approve-your-private-link-in-azure-portal) in Azure Portal.

Once all links were approved proceed with the environment creation by selecting **Validate Private Link**.
Upon successful validation you can continue configuring your new environment.

### Setup a Private Link when creating a Data Source

When creating a [Data Source](connect-common-data-model.md) that needs to connect to a storage protected by a virtual network, follow the same steps as described under [Setting up a private link when creating a Customer Insights environment](#setup-a-private-link-when-creating-a-customer-insights-environment).

### Setup a Private Link directly from the Private Links page in Customer Insights

1. In Customer Insights, go to **Admin** > **Security** and select the **Private Links** tab.

1. Select **Add Private Link**.

   The **Add Private Link** pane lists storage accounts from your tenant that you’ve got permissions to see.

1. Select the subscription, resource group, and storage account.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save**.

## Approve your private link in Azure Portal

1. After configuring the private link between Customer Insights and your virtual network protected storage you will notice 4 private links on the **Private Links** tab in Customer Insights. The status of these links should be **Pending**.

1. In Azure Portal, go to your Data Lake Storage account, go to **Networking** > **Private endpoints connections**.

1. You will see the 4 new private links that were just created through your action in Customer Insights.

1. In order to finalize the setup, you will need to approve all private links.

    Note: For easy identification, consider adding a description when approving the links.

    :::image type="content" source="media/Private-Endpoint-Approval.png" alt-text="Description for the private endpoint approval step.":::

1. The private links will now show as **Approved** in Customer Insights.

1. You can now go ahead and configure [Data Sources](connect-common-data-model.md) that are linked to your protected storage.

## Delete az Azure Private link

1. In Customer Insights, go to **Admin** > **Security** and select the **Private Links** tab.

1. Select the storage account name for which you would like to delete the private links.

1. Select **Delete**.

[!INCLUDE [footer-include](includes/footer-banner.md)]
