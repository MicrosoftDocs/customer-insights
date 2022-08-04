---
title: Configure security settings
description: Learn about security settings in Dynamics 365 Customer Insights.
ms.date: 08/02/2022

ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: mhart
manager: shellyha
---

# Configure security settings

Manage API keys, access customer data, and set up an Azure Private Link.

## Manage API keys

View and manage the keys to use the [Customer Insights APIs](apis.md) with the data in your environment.

1. Go to **System** > **Security** and select the **APIs** tab.

1. If API access to the environment has not been set up, select **Enable**. Or, to block API access to the environment, select **Disable** and confirm.

1. Manage the primary and secondary API keys:

   1. To show the primary or secondary API key, select the **Show** symbol.

   1. To copy the primary or secondary API key, select the **Copy** symbol.

   1. To create new primary and secondary API keys, select **Regenerate primary** or **Regenerate secondary**.

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

1. In Customer Insights, go to **Admin** > **Security** and select the **Private Links** tab.

1. Select **Add Private Link**.

   The **Add Private Link** pane lists storage accounts from your tenant that you’ve got permissions to see.

1. Select the subscription, resource group, and storage account.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save**.

1. Go to your Data Lake Storage account and open the link presented on the screen.

1. Approve the Private Link.


[!INCLUDE [footer-include](includes/footer-banner.md)]
