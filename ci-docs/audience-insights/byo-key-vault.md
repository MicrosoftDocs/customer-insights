---
title: "Bring your own Azure Key Vault"
description: "Learn how to configure Customer Insights to use your own Key Vault."
ms.date: 20/09/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: Bernd Kiefer
ms.author: bkief
manager: sesilv
---

# Bring your own Azure Key Vault (Preview)

Linking a dedicated [Azure Key Vault](https://docs.microsoft.com/azure/key-vault/general/basic-concepts) to an environment enables organizations to meet their compliance requirements.
The dedicated Key Vault can be used to stage and bring in secrets from within the organizations compliance boundary into the environment which can then be used to [setup connections](https://docs.microsoft.com/dynamics365/customer-insights/audience-insights/connections) to third party systems.

## Link the Key Vault to the Environment

### Prerequisites

To configure the Key Vault in Audience Insights, the following prerequisites must be met:

* You have an active Azure Subscription.

* You have an [Administrator](permissions.md#adminstrator) role in Audience Insights. Learn more about [setting user permissions in audience insights](permissions.md#assign-roles-and-permissions).

* You have the [Contributor](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#contributor) and [User Access Administrator](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#user-access-administrator) role on the Key Vault or the Resource Group the Key Vault is belonging to. For more information, see [Add or remove Azure role assignments using the Azure portal](https://docs.microsoft.com/azure/role-based-access-control/role-assignments-portal).

* The Key Vault **must have** Firewall disabled.

* The Key Vault must reside in the same [Azure location](https://azure.microsoft.com/global-infrastructure/geographies/#overview) as the environment. The region of the environment can be found under `Admin > System >` Tab `About >`  `Region`

 Warning

If you don't have the **User Access Administrator** role on the Key Vault, the RBAC permissions for the Azure service principal for Customer Insights must be setup separatly. Please follow the steps in [Connect to an Azure Data Lake Storage account by using an Azure service principal](https://docs.microsoft.com/dynamics365/customer-insights/audience-insights/connect-service-principal) but do the action on the Key Vault which should be linked.

### Link a Key Vault to the Environment

1. Go to `Admin > System >` Tab `Security`.
1. Click on `Setup` on the Key Vault tile.
1. Pick a `Subscription`.
1. Pick a `Key Vault` from the drop down. If too many Key Vaults are showing up, a Resource Group can be selected to narrow down the search results.
1. Accept the `Data privacy and compliance` statement.
1. Click `Save`

The Key Vault tile shows now the details of the linked Key Vault like Name, Resource Group & Subscription. It is now ready to be used in the connection setup.
For details which permissions on the Key Vault are granted to Audience Insights see the section [Permissions granted on the Key Vault to Audience Insights](#)

## Use the Key Vault in the Connection setup

When [setting up connections](https://docs.microsoft.com/dynamics365/customer-insights/audience-insights/connections) to third party systems the secrets from the linked Key Vault can now be used to configure the connections.

1. Go to `Admin > Connections`.
1. Click `Add connection`.
1. For the supported connection types listed below a `Use Key Vault` toggle can be enabled when a Key Vault is linked.
1. Instead of entering the secret manually it can now instead be configured via picking the `secret name` which is pointing to the secret value in the Key Vault.

**TODO** - ADD SCREENSHOTS

## Supported Connection Types

The following [export](export-destinations.md) connections are supported.

* [ActiveCampaign](export-active-campaign.md)
* [Autopilot](export-autopilot.md)
* [DotDigital](export-dotdigital.md)
* [Google Ads](export-google-ads.md)
* [Klaviyo](export-klaviyo.md)
* [LiveRamp](export-liveramp.md)
* [Marketo](export-marketo)
* [Omnisend](export-omnisend.md)
* [Salesforce Marketing Cloud](export-salesforce.md)
* [Sendgrid](export-sendgrid.md)
* [Sendinblue](export-sendinblue.md)
* [SFTP](export-sftp.md)

For other export connections where the log in on the target system is required (for e.g. Mailchimp and others) the connection secrets are kept in the service.

## Permissions granted on the Key Vault to Audience Insights

If the Key Vault is linked to the Environment, Audience Insights will be granted following permissions on the Key Vault depending if [Vault access policy](https://docs.microsoft.com/azure/key-vault/general/assign-access-policy?tabs=azure-portal) or [Azure role-based access control](https://docs.microsoft.com/azure/key-vault/general/rbac-guide?tabs=azure-cli) is enabled.

### Vault access policy

| Type        | Permissions                                                                                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Key         | [Get Keys](https://docs.microsoft.com/rest/api/keyvault/get-keys), [Get Key](https://docs.microsoft.com/rest/api/keyvault/get-key)                                 |
| Secret      | [Get Secrets](https://docs.microsoft.com/rest/api/keyvault/get-secrets), [Get Secret](https://docs.microsoft.com/rest/api/keyvault/get-secret)                     |
| Certificate | [Get Certificates](https://docs.microsoft.com/rest/api/keyvault/get-certificates), [Get Certificate](https://docs.microsoft.com/rest/api/keyvault/get-certificate) |

This is the minimum to list and read during execution.

### Azure role-based access control

The well-known `Key Vault Reader` and `Key Vault Secrets User` roles will be added for Audience Insights. For details on the roles see [Azure built-in roles for Key Vault data plane operations](https://docs.microsoft.com/azure/key-vault/general/rbac-guide?tabs=azure-cli).

## Recommendations

* Use a separate or dedicated Key Vault which is having only the secrets required for Audience Insights. Read more about why [separate Key Vaults are recommended](https://docs.microsoft.com/azure/key-vault/general/best-practices#why-we-recommend-separate-key-vaults).

* Follow the [Best practices to use Key Vault](https://docs.microsoft.com/azure/key-vault/general/best-practices#turn-on-logging) in regards of Control Access, Backup, Audit and Recovery options

## FAQs

### Can Audience Insights write secrets or overwrite secrets into the Key Vault?

No. Audience Insights has only read and list permissions, see [granted Permissions](#permissions-granted-on-the-key-vault-to-audience-insights). It cannot add, delete or overwrite existing secrets in the Key Vault. That's also the reason why entering secrets in the UI is not possible when `Use Key Vault` toggle is enabled.

### Can i switch a Connection from using secrets from a linked Key Vault to a default setup?

No. Once you decide on Connection creation to configure it with a secret from a linked Key Vault it can't be switched back to a default Connection. In this case we recommend to create a separate connection and delete the old one if necessary.

### How can i revoke access for Audience Insights?

Depending on whether [Vault access policy](https://docs.microsoft.com/azure/key-vault/general/assign-access-policy?tabs=azure-portal) or [Azure role-based access control](https://docs.microsoft.com/azure/key-vault/general/rbac-guide?tabs=azure-cli) are enabled you need to remove the permissions for the Service Principal `0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff` with the name `Dynamics 365 AI for Customer Insights`. Be aware that all connections will become invalid and all scenarios using the connection will break.

### A secret got removed from the Key Vault which is used in a connection, what can i do?

Audience Insights will give you a message on the UI when a configured secret from the Key Vault is not accessible anymore. It is recommended to enable [soft-delete](https://docs.microsoft.com/azure/key-vault/general/soft-delete-overview) which gives you the option to restore secrets if they are accidentally removed.

### A connection does not work but my secret is in the Key Vault, what might be the cause?

Audience Insights will give you a message on the UI when it can't access the Key Vault and specify the reason which can be

* The permissions for the Audience Insights Service Principal got removed. In this case they need to be manually restored. See [Prerequisites](#prerequisites) and [Permissions granted on the Key Vault to Audience Insights](#permissions-granted-on-the-key-vault-to-audience-insights).

* The Firewall on the Key Vault is enabled. In this case the Firewall must be disabled to make the Key Vault accessible for Audience Insights again.