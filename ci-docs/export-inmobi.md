---
title: Export Customer Insights data to InMobi
description: Learn how to configure the connection and export to InMobi.
ms.date: 11/15/2022
ms.reviewer: mhart
ms.topic: how-to
author: pkieffer
ms.author: philk
---

# Export Customer Insights data to InMobi (preview)

Export segment lists or other data from your Customer Insights instance to [InMobi](https://www.inmobi.com/).

## Prerequisites

- An [InMobi account](https://www.inmobi.com/) and admin credentials.
- An [Azure Blob Storage account](/azure/storage/blobs/create-data-lake-storage-account) name and account key. To find the name and key, see [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage).
- An [Azure Blob Storage container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container) to export InMobi data to.
- InMobi will create a direct connection to your Blob Storage, and configure an automatic import of your data to InMobi. Contact your InMobi representative to initiate the process.

## Known limitations

- For Azure Blob Storage, choose between [Standard performance and Premium performance tier](/azure/storage/blobs/storage-blob-performance-tiers). If you choose the Premium performance tier, select the [premium block blobs as account type](/azure/storage/common/storage-account-overview#types-of-storage-accounts).

## Set up connection to Azure Blob Storage

[Set up a connection to your Azure Blob Storage](export-azure-blob-storage.md).

## Configure an export

[Configure an export](export-azure-blob-storage.md#configure-an-export).

[!INCLUDE [footer-include](includes/footer-banner.md)]
