---
title: "Export Customer Insights data to SFTP hosts"
description: "Learn how to configure the connection to an SFTP host."
ms.date: 06/05/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for SFTP (preview)

Use your customer data in third-party applications by exporting them to a Secure File Transfer Protocol(SFTP) host.

## Prerequisites

- Availability of a SFTP host and corresponding credentials.

## Connect to SFTP

1. Go to **Admin** > **Export destinations**.

1. Under **SFTP**, select **Set up**.

1. Give your destination a recognizable name in the **Display name** field.

1. Provide a **Username**, **Password** and **Hostname** for your SFTP account. Example: If your SFTP server's root folder is /root/folder, and you would like the data to be exported to /root/folder/ci_export_destination_folder, the the host should be sftp://<server_address>/ci_export_destination_folder".

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

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data via SFTP, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that the export destination meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
