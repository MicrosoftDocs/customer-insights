---
title: "Export Customer Insights data to SFTP hosts | Microsoft Docs"
description: "Learn how to configure the connection to an SFTP host."
ms.date: 06/05/2020
ms.reviewer: philk
ms.service: dynamics-365-ai
ms.topic: "get-started-article"
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for SFTP (preview)

Use your customer data in third-party applications by exporting them to a Secure FTP (SFTP) host.

## Prerequisites

- Availability of a SFTP host and corresponding credentials.

## Connect to SFTP

1. Go to **Admin** > **Export destinations**.

1. Under **SFTP**, select **Set up**.

1. Give your destination a recognizable name in the **Display name** field.

1. Provide a **Username**, **Password** and **Hostname** (example.com:1234/folderpath) for your SFTP account.

1. Select **Verify** to test the connection.

1. After successful verification, choose if you want to export your data **Zipped** or **Unzipped**, and select the **field delimiter** for the exported files.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Next** to start configuring the export.

## Configure the connection

1. Select the **customer attributes** you want to export. You can export one or multiple attributes.

1. Select **Next**.

1. Select the segments you want to export.

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).
