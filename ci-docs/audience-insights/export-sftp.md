---
title: "Export Customer Insights data to SFTP hosts"
description: "Learn how to configure the connection to an SFTP host."
ms.date: 01/27/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: phkieffer
ms.author: philk
manager: shellyha
---

# Connector for SFTP (preview)

Use your customer data in third-party applications by exporting them to a Secure File Transfer Protocol (SFTP) host.

## Prerequisites

- Availability of an SFTP host and corresponding credentials.

## Connect to SFTP

1. Go to **Admin** > **Export destinations**.

1. Under **SFTP**, select **Set up**.

1. Give your destination a recognizable name in the **Display name** field.

1. Provide a **Username**, **Password**, **Hostname**, and **Export folder** for your SFTP account.

1. Select **Verify** to test the connection.

1. After successful verification, choose if you want to export your data **Gzipped** or **Unzipped**, and select the **field delimiter** for the exported files.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Next** to start configuring the export.

## Configure the export

1. Select the entities, for example segments, you want to export.

   > [!NOTE]
   > Each selected entity will be up to five output files when exported. 

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).

## Known limitations

- The runtime of an export depends on your system performance. We recommend two CPU cores and 1 Gb of memory as minimal configuration of your server. 
- Exporting entities with up to 100 million customer profiles can take 90 minutes when using the recommended minimal configuration of two CPU cores and 1 Gb of memory. 

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data via SFTP, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that the export destination meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.


[!INCLUDE[footer-include](../includes/footer-banner.md)]