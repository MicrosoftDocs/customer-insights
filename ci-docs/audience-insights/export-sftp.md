---
title: "Export Customer Insights data to SFTP hosts"
description: "Learn how to configure the connection and export to an SFTP location."
ms.date: 03/03/2021
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Export segment lists and other data to SFTP (preview)

Use your customer data in third-party applications by exporting them to a Secure File Transfer Protocol (SFTP) location.

## Prerequisites for connection

- Availability of an SFTP host and corresponding credentials.

## Known limitations

- The runtime of an export depends on your system performance. We recommend two CPU cores and 1 Gb of memory as minimal configuration of your server. 
- Exporting entities with up to 100 million customer profiles can take 90 minutes when using the recommended minimal configuration of two CPU cores and 1 Gb of memory. 

## Set up connection to SFTP

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **SFTP** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide a **Username**, **Password**, **Hostname**, and **Export folder** for your SFTP account.

1. Select **Verify** to test the connection.

1. Choose if you want to export your data **Gzipped** or **Unzipped** and the **field delimiter** for the exported files.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the SFTP section. If you don't see this section name, there are no connections of this type available to you.

1. Select the entities, for example segments, you want to export.

   > [!NOTE]
   > Each selected entity will be split up into up to five output files when exported. 

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-export-on-demand). 

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data via SFTP, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that the export destination meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
