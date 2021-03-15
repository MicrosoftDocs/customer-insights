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

# Prerequisites

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
