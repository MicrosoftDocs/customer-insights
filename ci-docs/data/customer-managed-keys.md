---
title: Customer-managed keys in Dynamics 365 Customer Insights - Data
description: Manage your encryption of data at rest with customer-managed keys.
ms.date: 02/06/2024
ms.reviewer: mhart
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Customer-managed keys in Dynamics 365 Customer Insights - Data

Customer-managed keys (CMK) are encryption keys that you manage, rather than Microsoft. These keys give you more control over the security of your data. For example, with customer-managed keys, you can rotate or swap the encryption key on demand. You can also prevent access to your data by revoking key access at any time. All customer data stored in Power Platform is already encrypted at-rest with strong Microsoft-managed encryption keys by default, but Power Platform also provides the option to enable a customer-managed encryption key to increase data protection.

Customer Insights - Data builds on features of Power Platform to support CMK for data at-rest. It shares a limitation with Power Platform: When you set up connections for exports or enrichments, the authentication tokens are encrypted with a Microsoft-managed key. For more information, see [Manage your customer-managed encryption key](/power-platform/admin/customer-managed-key).

## Use a customer-managed key in Customer Insights - Data

Enable CMK in Power Platform for the environment that hosts your Customer Insights installation. For more information, see [Create encryption key and grant access](/power-platform/admin/customer-managed-key#create-encryption-key-and-grant-access). Consider implications of using CMK and [understand the potential risk when you manage your key](/power-platform/admin/customer-managed-key#understand-the-potential-risk-when-you-manage-your-key).

> [!NOTE]
> The connection settings for export and enrichments will continue to be encrypted with a Microsoft-managed key. Consider using your [own Azure key vault to encrypt the connection settings](use-azure-key-vault.md) for the supported exports.

If your Customer Insights environment is configured to use your own Azure Data Lake Storage, you can configure your data lake to use customer-managed keys too. For more information, see [Customer-managed keys for Azure Storage encryption](/azure/storage/common/customer-managed-keys-overview).

### See also

- [Connections (preview) overview](connections.md)
- [Bring your own Azure key vault (preview)](use-azure-key-vault.md)
- [Security overview](security-overview.md)
