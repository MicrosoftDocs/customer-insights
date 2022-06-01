---
title: "Export Customer Insights data to InMobi"
description: "Learn how to configure the connection and export to InMobi."
ms.date: 10/06/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segment list and other data to InMobi (preview)

Export segment lists or other data from your Customer Insights instance to [InMobi](https://www.inmobi.com/).

# Prerequisites
1. You have an [InMobi account](https://www.inmobi.com/) and Admin credentials
2. You have a Blob Storage account name and account key - [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage), as well as a container within your Blob storage account [Create a container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).
3. InMobi will create a direct connection to your Blob Storage, and configure an automatic import of your data to InMobi. Contact your InMobi representative to initiate the process. 

## Known limitations

1. For Azure Blob Storage you can choose between [Standard performance and Premium performance tier](/azure/storage/blobs/storage-blob-performance-tiers). If you choose the Premium performance tier, select the [premium block blobs as account type](/azure/storage/common/storage-account-overview#types-of-storage-accounts).



## Set up the connection to Blob Storage and configure an export

1. Follow the instructions to [setup a connection to your Blob Storage](/customer-insights-pr/blob/main/ci-docs/export-azure-blob-storage). 
2. Follow the instructions to [configure an export](https://github.com/MicrosoftDocs/customer-insights-pr/blob/main/ci-docs/export-azure-blob-storage.md#configure-an-export).



[!INCLUDE [footer-include](includes/footer-banner.md)]
