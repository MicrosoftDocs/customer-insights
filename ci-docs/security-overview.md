---
title: "Security settings in Dynamics 365 Customer Insights"
description: "Learn about security settings in Dynamics 365 Customer Insights."
ms.date: 06/03/2022

ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: mhart
manager: shellyha
---

# Security overview page

The **Security** page lists options to configure user permissions and features that help make Dynamics 365 Customer Insights more secure. Only administrators can access this page. 

Go to **Admin** > **Security** to configure the settings.

The **Security** page includes the following tabs:
- [Users](#users-tab)
- [APIs](#apis-tab)
- [Key Vault](#key-vault-tab)

## Users tab

Access to Customer Insights is restricted to users in your organization that were added to the application by an admin. The **Users** tab lets you manage user access and their permissions. For more information, see [User permissions](permissions.md).

## APIs tab

View and manage the keys to use the [Customer Insights APIs](apis.md) with the data of your environment.

You can create new primary and secondary keys by selecting **Regenerate primary** or **Regenerate secondary**. 

To block API access to the environment, select **Disable**. If APIs are disabled, you can select **Enable** to grant access again.

## Key Vault tab

The **Key Vault** tab lets you link and manage your own [Azure key vault](/azure/key-vault/general/basic-concepts) to the environment.
The dedicated key vault can be used to stage and use secrets in an organization's compliance boundary. Customer Insights can use the secrets in Azure Key Vault to [set up connections](connections.md) to third-party systems.

For more information, see [Bring your own Azure key vault](use-azure-key-vault.md).

## Securely access customer data in Customer Insights by using Customer Lockbox in Power Platform (preview)

Customer Insights is leveraging the Power Platform Customer Lockbox capability. Customer Lockbox provides an interface to review and approve (or reject) data access requests in the rare occasion when data access to customer data is needed to resolve a support case. To use this feature, Customer Insights must have an existing connection to a Microsoft Dataverse environment in your tenant.

For more details about Customer Lockbox, see the [summary](/power-platform/admin/about-lockbox#summary) of Power Platform Customer Lockbox. The article also describes the [workflow] (/power-platform/admin/about-lockbox#workflow) and the required [setup](/power-platform/admin/about-lockbox#enable-the-lockbox-policy) to enable Customer Lockbox.

> [!IMPORTANT]
> Global administrators for Power Platform or Power Platform administrators can approve Customer Lockbox requests issued for Customer Insights.

[!INCLUDE [footer-include](includes/footer-banner.md)]
