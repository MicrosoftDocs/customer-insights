---
title: Security settings in Customer Insights
description: Learn about security settings in Dynamics 365 Customer Insights.
ms.date: 05/27/2022

ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: mhart
manager: shellyha
---

# Security settings in Customer Insights

The **Security** page lists options to configure user permissions and features that help make Dynamics 365 Customer Insights more secure. Only administrators can access this page.

Go to **Admin** > **Security** to configure the settings.

The **Security** page includes the following tabs:

- [Users](#users-tab)
- [APIs](#apis-tab)
- [Private Links](#private-links-tab)
- [Key Vault](#key-vault-tab)

## Users tab

Access to Customer Insights is restricted to users in your organization that were added to the application by an admin. The **Users** tab lets you manage user access and their permissions. For more information, see [User permissions](permissions.md).

## APIs tab

View and manage the keys to use the [Customer Insights APIs](apis.md) with the data of your environment.

You can create new primary and secondary keys by selecting **Regenerate primary** or **Regenerate secondary**. 

To block API access to the environment, select **Disable**. If APIs are disabled, you can select **Enable** to grant access again.

## Private Links tab

[Azure Private Link](/azure/private-link/private-link-overview) lets Customer Insights connect to your Azure Data Lake Storage account over a private endpoint in your virtual network. For data in a storage account, which isn't exposed to the public internet, Private Link enables the connection to that restricted network.

> [!IMPORTANT]
> Minimum role requirement to set up a Private Link connection:
>
> - Customer Insights: Administrator
> - Azure built-in role: [Storage Account Contributor](/azure/role-based-access-control/built-in-roles#storage-account-contributor)
> - Permissions for custom Azure role: [Microsoft.Storage/storageAccounts/read and Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action](/azure/role-based-access-control/resource-provider-operations#microsoftstorage)
>

Setting up Private Link in Customer Insights is a two-step process. First, you initiate the creation of a Private Link from **Admin** > **Security** > **Private Links** in Customer Insights. The **Add Private Link** pane lists storage accounts from your tenant that you’ve got permissions to see. Select the storage account and provide consent to create the Private Link.

Next, you need to approve the Private Link on the Data Lake Storage account side. Open the link presented on screen to approve the new Private Link.

## Key Vault tab

The **Key Vault** tab lets you link and manage your own [Azure key vault](/azure/key-vault/general/basic-concepts) to the environment.
The dedicated key vault can be used to stage and use secrets in an organization's compliance boundary. Customer Insights can use the secrets in Azure Key Vault to [set up connections](connections.md) to third-party systems.

For more information, see [Bring your own Azure key vault](use-azure-key-vault.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
