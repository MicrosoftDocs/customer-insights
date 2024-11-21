---
title: "Export data to SFTP hosts (preview)"
description: "Learn how to configure the connection and export to an SFTP location."
ms.date: 04/03/2023
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export data to SFTP hosts (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Use your customer data in third-party applications by exporting them to a Secure File Transfer Protocol (SFTP) location.

[!INCLUDE [data-out-azure-synapse-link](includes/data-out-azure-synapse-link.md)]

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWO94X]

## Prerequisites

- Availability of an SFTP host and corresponding credentials.

## Known limitations

- SFTP destinations behind firewalls are currently not supported.
- The runtime of an export depends on your system performance. We recommend two CPU cores and 1 Gb of memory as minimal configuration of your server.
- This export works only for CSV formatted files.
- Up to 100 million customer profiles, which can take 90 minutes when using the recommended minimal configuration of two CPU cores and 1 Gb of memory.
- If you use an SSH key for authentication, make sure you [create your private key](/azure/virtual-machines/linux/create-ssh-keys-detailed#basic-example) as PEM or SSH.COM format. If you are using Putty, convert your private key by exporting is as Open SSH. The following private key formats are supported:
  - RSA in OpenSSL PEM and ssh.com format
  - DSA in OpenSSL PEM and ssh.com format
  - ECDSA 256/384/521 in OpenSSL PEM format
  - ED25519 and RSA in OpenSSH key format

## Set up connection to SFTP

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **SFTP**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Choose whether you want to authenticate through SSH or username/password for your connection and provide the necessary details. If you use an SSH key for authentication, make sure you [create your private key](/azure/virtual-machines/linux/create-ssh-keys-detailed#basic-example) as PEM or SSH.COM format. If you are using Putty, convert your private key by exporting is as Open SSH. The following private key formats are supported:
   - RSA in OpenSSL PEM and ssh.com format
   - DSA in OpenSSL PEM and ssh.com format
   - ECDSA 256/384/521 in OpenSSL PEM format
   - ED25519 and RSA in OpenSSH key format

1. Enter the **Hostname** and specify the **Export folder** on the FTP server. The export folder must be lowercase. The system is not case-sensitive and will create folder names in lowercase even if you use capital letters in the folder name.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the SFTP section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Choose if you want to export your data **Gzipped** or **Unzipped** and the **field delimiter** for the exported files.

1. Select the tables, for example segments, that you want to export.

1. Choose **Next** and determine if you want to send all fields in the selected tables. By default, all fields in your selected tables are exported. Clear the checkox next to the fields you don't want to export.

   > [!NOTE]
   > Each selected table is split into a maximum of five output files when exported.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

> [!TIP]
> Export of tables that contain a large amount of data can lead to multiple CSV files in the same folder for each export. Splitting exports happens for performance reasons to minimize the time it takes for an export to complete.

[!INCLUDE [footer-include](includes/footer-banner.md)]
