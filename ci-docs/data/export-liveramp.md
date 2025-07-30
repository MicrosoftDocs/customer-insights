---
title: "Export segments to LiveRamp (preview)"
description: "Learn how to configure the connection and the export to LiveRamp."
ms.date: 11/15/2022
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: sfi-image-nochange
---

# Export segments to LiveRamp&reg; (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Activate your data in LiveRamp to connect with over 500 platforms across digital, social, and TVs. Work with your data in LiveRamp to target, suppress, and personalize ad campaigns.

## Prerequisites

- A LiveRamp subscription to use this connector. To get a subscription, [contact LiveRamp](https://liveramp.com/contact/) directly. [Learn more about LiveRamp Onboarding](https://liveramp.com/our-platform/data-onboarding/).

## Known limitations

- The LiveRamp export is using an SFTP export. SFTP destinations behind firewalls are currently not supported.
- If you use an SSH key for authentication, make sure you [create your private key](/azure/virtual-machines/linux/create-ssh-keys-detailed#basic-example) as PEM or SSH.COM format. If you are using Putty, convert your private key by exporting is as Open SSH. The following private key formats are supported:
  - RSA in OpenSSL PEM and ssh.com format
  - DSA in OpenSSL PEM and ssh.com format
  - ECDSA 256/384/521 in OpenSSL PEM format
  - ED25519 and RSA in OpenSSH key format
- The runtime of an export depends on your system performance. We recommend two CPU cores and 1 Gb of memory as minimal configuration of your server.
- Exporting tables with up to 100 million customer profiles can take 90 minutes when using the recommended minimal configuration of two CPU cores and 1 Gb of memory.
- The actual number of profiles (or data) you can export to LiveRamp depends on your subscription with LiveRamp.

## Set up connection to LiveRamp

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **LiveRamp**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Choose whether you want to authenticate through SSH or username/password for your connection and provide the necessary details.

1. After successful verification, review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the LiveRamp section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. In the **Connect data** field, select **Email**, **Name and address**, or **Phone** to send to LiveRamp for identity resolution.

   :::image type="content" source="media/export-liveramp-segments.png" alt-text="LiveRamp connector with attribute mapping.":::

1. Map the corresponding attributes from your *Customer* table for the selected key identifier.

1. Select **Add attribute** to map more attributes to send to LiveRamp.

   > [!TIP]
   > Sending more key identifier attributes to LiveRamp is likely to get you a higher match rate.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
