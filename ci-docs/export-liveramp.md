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

## Prerequisites for a connection

- You need a LiveRamp subscription to use this connector.
- To get a subscription, [contact LiveRamp](https://liveramp.com/contact/) directly. [Learn more about LiveRamp Onboarding](https://liveramp.com/our-platform/data-onboarding/).

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

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **LiveRamp** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Choose whether you want to authenticate through SSH or username/password for your connection and provide the necessary details. If you use an SSH key for authentication, make sure you [create your private key](/azure/virtual-machines/linux/create-ssh-keys-detailed#basic-example) as PEM or SSH.COM format. If you are using Putty, convert your private key by exporting is as Open SSH. The following private key formats are supported:
   - RSA in OpenSSL PEM and ssh.com format
   - DSA in OpenSSL PEM and ssh.com format
   - ECDSA 256/384/521 in OpenSSL PEM format
   - ED25519 and RSA in OpenSSH key format

1. Provide your consent for **Data privacy and compliance** by selecting the **I agree** checkbox.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the LiveRamp section. If you don't see this section name, there are no connections of this type available to you.

1. In the **Choose your key identifier** field, select **Email**,  **Name and address**, or **Phone** to send to LiveRamp for identity resolution.
   > [!div class="mx-imgBorder"]
   > ![LiveRamp connector with attribute mapping.](media/export-liveramp-segments.png "LiveRamp connector with attribute mapping")

1. Map the corresponding attributes from your *Customer* entity for the selected key identifier.

1. Select **Add attribute** to map more attributes to send to LiveRamp.

   > [!TIP]
   > Sending more key identifier attributes to LiveRamp is likely to get you a higher match rate.

1. Select the segments you want to export to LiveRamp.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Liveramp, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Liveramp meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.

[!INCLUDE [footer-include](includes/footer-banner.md)]
