---
title: "Export data to Salesforce Marketing Cloud (preview)"
description: "Learn how to configure the connection and export to Salesforce Marketing Cloud."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export data to Salesforce Marketing Cloud (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Use your customer data in Salesforce Marketing Cloud by exporting them through a Secure File Transfer Protocol (SFTP) location.

## Prerequisites

- An [SFTP host for Salesforce Marketing Cloud](https://help.salesforce.com/articleView?id=sf.mc_es_configure_enhanced_ftp.htm&type=5) and corresponding admin credentials.

## Set up connection to Salesforce Marketing Cloud

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Salesforce Marketing Cloud**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide a **Username**, **Password**, **Hostname**, and **Export folder** for your SFTP account.

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

   > [!NOTE]
   > Each selected table will be split into a maximum of five output files when exported.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

## Import data from Dynamics 365 Customer Insights - Data from SFTP location to Salesforce Marketing Cloud

1. Create [data extensions in Salesforce Marketing Cloud](https://help.salesforce.com/articleView?id=sf.mc_es_create_data_extension.htm&type=5) to import the data file from Customer Insights - Data from the SFTP location.

2. [Import the data from the SFTP location](https://help.salesforce.com/articleView?id=sf.mc_es_import_data_extension_classic.htm&type=5) into the Salesforce Marketing Cloud data extension.

3. Set up the automation to import the data into the data extensions. Learn more about [file drop automations and scheduled automations](https://help.salesforce.com/articleView?id=sf.mc_as_triggered_automations.htm&type=5).

   Define a [file drop automation](https://help.salesforce.com/articleView?id=sf.mc_as_define_a_triggered_automation.htm&type=5) or a  [scheduled automation](https://help.salesforce.com/articleView?id=sf.mc_as_define_a_scheduled_automation.htm&type=5).

Here's an example of [an automation with SFTP](https://help.salesforce.com/articleView?id=sf.mc_as_ftp_and_triggered_automation_scenario.htm&type=5).

[!INCLUDE [footer-include](includes/footer-banner.md)]
