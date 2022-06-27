---
title: Export Customer Insights data to InMobi
description: Learn how to configure the connection and export to InMobi.
ms.date: 06/27/2022
ms.reviewer: mhart
ms.subservice: audience-insights
ms.topic: how-to
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segment list and other data to InMobi (preview)

Export segment lists or other data from your Customer Insights instance to [InMobi](https://www.inmobi.com/).

## Prerequisites

1. You have an [InMobi account](https://www.inmobi.com/) and admin credentials.
1. You have an Azure Blob storage account name and the corresponding account key. For more information, see [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage). There's a container in the storage account to export inMobi data to. For more information, see [Create a container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).
1. InMobi will create a direct connection to your Blob Storage, and configure an automatic import of your data to InMobi. Contact your InMobi representative to initiate the process.

## Known limitations

1. For Azure Blob Storage, you can choose between [Standard performance and Premium performance tier](/azure/storage/blobs/storage-blob-performance-tiers). If you choose the Premium performance tier, select the [premium block blobs as account type](/azure/storage/common/storage-account-overview#types-of-storage-accounts).

## Set up the connection to Azure Blob Storage and configure an export

1. Follow the instructions to [setup a connection to your Azure Blob Storage](export-azure-blob-storage.md).
2. Follow the instructions to [configure an export](export-azure-blob-storage.md#configure-an-export).

[!INCLUDE [footer-include](includes/footer-banner.md)]
