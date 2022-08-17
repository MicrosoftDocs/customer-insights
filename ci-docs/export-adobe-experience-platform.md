---
title: "Export segments to Adobe Experience Platform (preview)"
description: "Learn how to use Customer Insights segments in Adobe Experience Platform."
ms.date: 07/25/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: stefanie-msft
ms.author: antando
manager: shellyha
---

# Export segments to Adobe Experience Platform (preview)

Export segments that target relevant audiences to Adobe Experience Platform.

:::image type="content" source="media/AEP-flow.png" alt-text="Process diagram of the steps outlined in this article.":::

## Prerequisites

- An Adobe Experience Platform license.
- An Adobe Campaign Standard license.
- An [Azure Blob Storage account](/azure/storage/blobs/create-data-lake-storage-account) name and account key. To find the name and key, see [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage).
- An [Azure Blob Storage container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).

## Campaign Overview

To better understand how you can use segments from Customer Insights in Adobe Experience Platform, let’s look at a fictitious sample campaign.

Let’s assume that your company offers a monthly, subscription-based service to your customers in the United States. You want to identify customers whose subscriptions are due for renewal in the next eight days but haven't yet renewed their subscription. To keep these customers, you want to send them a promotional offer via email, using Adobe Experience Platform.

In this example, we want to run the promotional email campaign once. This article doesn’t cover the use-case of running the campaign more than once.

## Identify your target audience

In our scenario, we assume that the email addresses of the customers are available in Customer Insights and their promotional preferences were analyzed to identify members of the segment.

The [segment you defined in Customer Insights](segments.md) is called **ChurnProneCustomers** and you plan to send these customers the email promotion.

:::image type="content" source="media/churn-prone-customers-segment.png" alt-text="Screenshot of the segments page with the ChurnProneCustomers segment created.":::

The offer email that you want to send out will contain the first name, last name, and the subscription end date of the customer. It informs the customers about the discount they’ll get if they renew their subscription before it ends.

## Export your target audience

We'll configure the export from Customer Insights to an Azure Blob Storage account.

### Set up connection to Azure Blob Storage

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Azure Blob Storage**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter **Account name**, **Account key**, and **Container** for your Blob Storage account where you want to export the segment to.  

   :::image type="content" source="media/azure-blob-configuration.png" alt-text="Screenshot of the storage account configuration.":::

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

### Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Azure Blob Storage section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Choose the segment that you want to export. In this example, it’s **ChurnProneCustomers**.

   :::image type="content" source="media/select-segment-churnpronecustomers.png" alt-text="Screenshot of the segment selection user interface with ChurnProneCustomers segment selected.":::

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

> [!NOTE]
> Ensure that the number of records in the exported segment are within the allowed limit of your Adobe Campaign Standard license.

Exported data is stored in the Azure Blob Storage container you configured. The following folder paths are automatically created in your container:

- For source entities and entities generated by the system: 

  *%ContainerName%/CustomerInsights_%instanceID%/%ExportDestinationName%/%EntityName%/%Year%/%Month%/%Day%/%HHMM%/%EntityName%_%PartitionId%.csv*

  Example: Dynamics365CustomerInsights/CustomerInsights_abcd1234-4312-11f4-93dc-24f72f43e7d5/BlobExport/ChurnSegmentDemo/2021/02/16/1433/ChurnProneCustomers_1.csv

- The *model.json* for the exported entities resides at the *%ExportDestinationName%* level.

  Example: Dynamics365CustomerInsights/CustomerInsights_abcd1234-4312-11f4-93dc-24f72f43e7d5/ChurnSegmentDemo/model.json

## Define Experience Data Model (XDM) in Adobe Experience Platform

Before the exported data from Customer Insights can be used within Adobe Experience Platform, define the Experience Data Model schema and [configure the data for the Real-time Customer Profile](https://experienceleague.adobe.com/docs/experience-platform/profile/tutorials/dataset-configuration.html#tutorials).

Learn [what XDM is](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html) and understand the [basics of schema composition](https://experienceleague.adobe.com/docs/experience-platform/xdm/schema/composition.html#schema).

## Import data into Adobe Experience Platform

Import the prepared audience data from Customer Insights into Adobe Experience Platform.

1. [Create an Azure Blob Storage source connection](https://experienceleague.adobe.com/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/blob.html#getting-started).

1. [Configure a dataflow](https://experienceleague.adobe.com/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage.html#ui-tutorials) for a cloud storage batch connection to import the segment output from Customer Insights into Adobe Experience Platform.

## Create an audience in Adobe Campaign Standard

To send the email for this campaign, we'll use Adobe Campaign Standard.

1. [Create an audience](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/get-started-profiles-and-audiences.html#permission) in Adobe Campaign Standard using the data in Adobe Experience Platform.

1. [Use segment builder](https://experienceleague.adobe.com/docs/campaign-standard/using/integrating-with-adobe-cloud/adobe-experience-platform/audience-destinations/aep-using-segment-builder.html) in Adobe Campaign Standard to define an audience based on the data in Adobe Experience Platform.

## Create and send the email using Adobe Campaign Standard

Create the email content and then [test and send](https://experienceleague.adobe.com/docs/campaign-standard/using/testing-and-sending/get-started-sending-messages.html#preparing-and-testing-messages) your email.

:::image type="content" source="media/contoso-sample-email.jpg" alt-text="Sample email with renewal offer from Adobe Campaign Standard.":::

[!INCLUDE [footer-include](includes/footer-banner.md)]