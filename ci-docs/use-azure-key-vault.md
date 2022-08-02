---
title: "Bring your own Azure key vault (preview)"
description: "Learn how to configure Customer Insights to use your own Azure key vault to manage secrets."
ms.date: 08/02/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: brndkfr
ms.author: bkief
manager: shellyha
searchScope: 
  - ci-system-security
  - customerInsights
---

# Bring your own Azure key vault (preview)

Linking a dedicated [Azure key vault](/azure/key-vault/general/basic-concepts) to a Customer Insights environment helps organizations to meet compliance requirements. For more information, see [Bring your own Azure key vault](use-azure-key-vault.md).

## Link the key vault to the Customer Insights environment

Set up the dedicated key vault to stage and use secrets in an organization's compliance boundary.

### Prerequisites

- An active Azure subscription.

- An [Administrator](permissions.md#admin) role in Customer Insights. Learn more about [user permissions in Customer Insights](permissions.md#assign-roles-and-permissions).

- [Contributor](/azure/role-based-access-control/built-in-roles#contributor) and [User Access Administrator](/azure/role-based-access-control/built-in-roles#user-access-administrator) roles on the key vault or the resource group the key vault belongs to. For more information, go to [Add or remove Azure role assignments using the Azure portal](/azure/role-based-access-control/role-assignments-portal). If you don't have the User Access Administrator role on the key vault, set up the role-based access control permissions for the Azure service principal for Dynamics 365 Customer Insights separately. Follow the steps to [use an Azure service principal](connect-service-principal.md) for the key vault that should be linked.

- Key vault must have Key Vault firewall **disabled**.

- Key vault is in the same [Azure location](https://azure.microsoft.com/global-infrastructure/geographies/#overview) as the Customer Insights environment. The region of the environment in Customer Insights is listed under **Admin** > **System** > **About** > **Region**.

### Recommendations

- Use a separate or dedicated key vault that contains only the secrets required for Customer Insights. Read more about why [separate key vaults are recommended](/azure/key-vault/general/best-practices#why-we-recommend-separate-key-vaults).

- Follow the [best practices to use Key Vault](/azure/key-vault/general/best-practices#turn-on-logging) for control access, backup, audit, and recovery options.

### Link a key vault to the environment

1. Go to **Admin** > **Security**, and then select the **Key Vault** tab.
1. On the **Key Vault** tile, select **Setup**.
1. Choose a **Subscription**.
1. Choose a key vault from the **Key Vault** dropdown list. If too many key vaults are available, select a resource group to limit the search results.
1. Review the [Data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.
1. Select **Save**.

The **Key Vault** tile shows the linked key vault name, subscription, and resource group. It's ready to be used in the connection setup.
For details about which permissions on the key vault are granted to Customer Insights, go to [Permissions granted on the key vault](#permissions-granted-on-the-key-vault).

## Use the key vault in the connection setup

When [setting up connections](connections.md) to third-party systems, the secrets from the linked Key Vault can be used to configure the connections.

1. Go to **Admin** > **Connections**.
1. Select **Add connection**.
1. For the supported connection types, a **Use Key Vault** toggle is available if you linked a key vault.
1. Instead of entering the secret manually, choose the secret name that points to the secret value in the key vault.

   :::image type="content" source="media/use-key-vault-secret.png" alt-text="Connection pane with an SFTP connection that uses a Key Vault secret.":::
1. To create the connection, select **Save**.

## Supported connection types

The following [export](export-destinations.md) connections are supported:

* [ActiveCampaign](export-active-campaign.md)
* [Autopilot](export-autopilot.md)
* [DotDigital](export-dotdigital.md)
* [Google Ads](export-google-ads.md)
* [Klaviyo](export-klaviyo.md)
* [LiveRamp](export-liveramp.md)
* [Marketo](export-marketo.md)
* [Omnisend](export-omnisend.md)
* [Salesforce Marketing Cloud](export-salesforce.md)
* [Sendgrid](export-sendgrid.md)
* [Sendinblue](export-sendinblue.md)
* [SFTP](export-sftp.md)

## Permissions granted on the key vault

The following permissions are granted to Customer Insights on a linked key vault if either [Key Vault access policy](/azure/key-vault/general/assign-access-policy?tabs=azure-portal) or [Azure role-based access control](/azure/key-vault/general/rbac-guide?tabs=azure-cli) is enabled.

### Key Vault access policy

| Type        | Permissions          |
| ----------- | -------------------- |
| Key         | [Get Keys](/rest/api/keyvault/keys/get-keys/get-keys), [Get Key](/rest/api/keyvault/keys/get-key/get-key)                                 |
| Secret      | [Get Secrets](/rest/api/keyvault/secrets/get-secrets/get-secrets), [Get Secret](/rest/api/keyvault/secrets/get-secret/get-secret)                     |
| Certificate | [Get Certificates](/rest/api/keyvault/certificates/get-certificates/get-certificates), [Get Certificate](/rest/api/keyvault/certificates/get-certificate/get-certificate) |

The preceding values are the minimum to list and read during execution.

### Azure role-based access control

The [Key Vault Reader and Key Vault Secrets User roles](/azure/key-vault/general/rbac-guide?tabs=azure-cli) will be added for Customer Insights.

## Frequently asked questions

### Can Customer Insights write secrets or overwrite secrets into the key vault?

No. Only the read and list permissions outlined in [granted permissions](#permissions-granted-on-the-key-vault) are granted to Customer Insights. The system can't add, delete, or overwrite secrets in the key vault. That's also the reason why you can't enter credentials when a connection uses Key Vault.

### Can I change a connection from using Key Vault secrets to default authentication?

No. You can't change back to a default connection after you've configured it by using a secret from a linked key vault. Create a separate connection, and delete the old one if you don't need it anymore.

### How can I revoke access to a key vault for Customer Insights?

If the [Key Vault access policy](/azure/key-vault/general/assign-access-policy?tabs=azure-portal) or [Azure role-based access control](/azure/key-vault/general/rbac-guide?tabs=azure-cli) is enabled, remove the permissions for the service principal `0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff` with the name `Dynamics 365 AI for Customer Insights`. All connections that use the key vault will stop working.

### A secret that's used in a connection got removed from the key vault. What can I do?

A notification appears in Customer Insights when a configured secret from the key vault isn't accessible anymore. Enable [soft-delete](/azure/key-vault/general/soft-delete-overview) on the key vault to restore secrets if they're accidentally removed.

### A connection doesn't work, but my secret is in the key vault. What might be the cause?

A notification appears in Customer Insights when it can't access the key vault. The cause might be:

- The permissions for the Customer Insights service principal got removed. They need to be manually restored.

- The firewall on the key vault is enabled. The firewall must be disabled to make the key vault accessible for Customer Insights again.
