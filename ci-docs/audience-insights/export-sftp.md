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

1. Provide a **Username**, **Password**, **Hostname**, and **Export folder** for your SFTP account. Example: If your SFTP server's root folder is /root/folder, and you would like the data to be exported to /root/folder/ci_export_destination_folder, the the host should be sftp://<server_address>/ci_export_destination_folder".

1. Select **Verify** to test the connection.

1. After successful verification, choose if you want to export your data **Gzipped** or **Unzipped**, and select the **field delimiter** for the exported files.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Next** to start configuring the export.

## Configure the export

1. Select the entities such as segments you want to export.

**Note:** each selected entity will be split into up to 5 output files when exported. 

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).

## Known limitations ##

- The runtime of an export is dependent on your system performance. We recommend 2 CPU cores and 1Gb memory as minimal configuration of your server for optimal results. 
- Exporting entities containing up to 100 million customer profiles can take up to 90 minutes when using the recommended minimal configuration of 2 CPU cores and 1Gb memory. 

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data via SFTP, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that the export destination meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
