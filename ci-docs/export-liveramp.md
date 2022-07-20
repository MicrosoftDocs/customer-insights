---
title: "Export segments to LiveRamp (preview)"
description: "Learn how to configure the connection and the export to LiveRamp."
ms.date: 07/06/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: kishorem-ms
ms.author: kishorem
manager: shellyha
---

# Export segments to LiveRamp&reg; (preview)

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
- Exporting entities with up to 100 million customer profiles can take 90 minutes when using the recommended minimal configuration of two CPU cores and 1 Gb of memory.
- The actual number of profiles (or data) you can export to LiveRamp depends on your subscription with LiveRamp.

## Set up connection to LiveRamp

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **LiveRamp**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Choose whether you want to authenticate through SSH or username/password for your connection and provide the necessary details. If you use an SSH key for authentication, make sure you [create your private key](/azure/virtual-machines/linux/create-ssh-keys-detailed#basic-example) as PEM or SSH.COM format. If you are using Putty, convert your private key by exporting is as Open SSH. The following private key formats are supported:
   - RSA in OpenSSL PEM and ssh.com format
   - DSA in OpenSSL PEM and ssh.com format
   - ECDSA 256/384/521 in OpenSSL PEM format
   - ED25519 and RSA in OpenSSH key format

1. Select **Verify** to test the connection to LiveRamp.

1. After successful verification, review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the LiveRamp section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. In the **Connect data** field, select **Email**, **Name and address**, or **Phone** to send to LiveRamp for identity resolution.

   :::image type="content" source="media/export-liveramp-segments.png" alt-text="LiveRamp connector with attribute mapping.":::

1. Map the corresponding attributes from your *Customer* entity for the selected key identifier.

1. Select **Add attribute** to map more attributes to send to LiveRamp.

   > [!TIP]
   > Sending more key identifier attributes to LiveRamp is likely to get you a higher match rate.

1. Select the segments you want to export.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

[!INCLUDE [footer-include](includes/footer-banner.md)]
