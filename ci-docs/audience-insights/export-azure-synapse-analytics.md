---
title: "Export Customer Insights data to Azure Synapse Analytics"
description: "Learn how to configure the connection to Azure Synapse Analytics."
ms.date: 03/15/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: stefanie-msft
ms.author: sthe
manager: shellyha
---

# Overview

You can now use your Customer Insights data within Azure Synapse Analytics. 

# Prerequisites

To configure the connection from Customer Insights to Azure Synapse Analytics and use your Customer Insights data within Azure Synapse Analytics, the following reprequisites must be met:

## Prerequisites in Customer Insights

* You have an Administrator role in Customer Insights

## Prerequisites in Azure 
* You have an active Azure Subscription
 
* On export storage, the first party app needs **Storage Blob Contributor** permissions. Learn more on [how to connect to an Azure Data Lake Storage Gen2 account with an Azure service principal for audience insights](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/connect-service-principal)

* On Synapse workspace, the first party app needs **Reader** permissions. Learn more on [How to set up access control for your Synapse workspace](https://docs.microsoft.com/en-us/azure/synapse-analytics/security/how-to-set-up-access-control) 

* On Synapse workspace api, the first party app needs **Admin** role assigned. Learn more on [How to set up access control for your Synapse workspace](https://docs.microsoft.com/en-us/azure/synapse-analytics/security/how-to-set-up-access-control) 

# Set up the connection to Azure Synapse Analytics from within Customer Insights

## Configure a connection
1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Azure Synapse Analytics** to configure the connection.


## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add export**.

1. ...

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 
