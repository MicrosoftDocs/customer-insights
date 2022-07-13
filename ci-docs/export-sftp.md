---
title: "Export data to SFTP hosts (preview) (contains video)"
description: "Learn how to configure the connection and export to an SFTP location."
ms.date: 06/09/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export data to SFTP hosts (preview)

Use your customer data in third-party applications by exporting them to a Secure File Transfer Protocol (SFTP) location.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWO94X]

## Prerequisites

- Availability of an SFTP host and corresponding credentials.

## Known limitations

- SFTP destinations behind firewalls are currently not supported.
- The runtime of an export depends on your system performance. We recommend two CPU cores and 1 Gb of memory as minimal configuration of your server.
- Up to 100 million customer profiles, which can take 90 minutes when using the recommended minimal configuration of two CPU cores and 1 Gb of memory.

## Set up connection to SFTP

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **SFTP**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Choose how to connect, either username and password or SSH key.
   - **Username and password**: Provide a **Username**, **Password**, **Hostname**, and **Export folder** for your SFTP account
   - **SSH key**: Provide a **Username**, **Private key**, **Passphrase**, **Hostname**, and **Export folder** for your SFTP account.

1. Select **Verify** to test the connection.

1. Select **I agree** to confirm the [Data privacy and compliance](#data-privacy-and-compliance).

1. Select **Save** to complete the connection.

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data via SFTP, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that the export destination meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the SFTP section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. Choose if you want to export your data **Gzipped** or **Unzipped** and the **field delimiter** for the exported files.

1. Select the entities, for example segments, that you want to export.

   > [!NOTE]
   > Each selected entity will be split into a maximum of five output files when exported.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

> [!TIP]
> Export of entities that contain a large amount of data can lead to multiple CSV files in the same folder for each export. Splitting exports happens for performance reasons to minimize the time it takes for an export to complete.

[!INCLUDE [footer-include](includes/footer-banner.md)]
