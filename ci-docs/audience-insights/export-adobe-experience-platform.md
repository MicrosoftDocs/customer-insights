---
title: "Export Customer Insights data to Adobe Experience Platform"
description: "Learn how use audience insights segments in Adobe Experience Platform."
ms.date: 02/26/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: stefanie-msft
ms.author: antando
manager: shellyha
---

# Use Customer Insights segments in Adobe Experience Platform (preview)

As a user of audience insights for Dynamics 365 Customer Insights, you may have created segments to make your marketing campaigns more efficient by targeting relevant audiences. To use a segment from audience insights in Adobe Experience Platform and applications like Adobe Campaign Standard, you need to follow a few steps outlined in this article.

:::image type="content" source="media/AEP-flow.png" alt-text="Process diagram of the steps outlined in this article.":::

## Prerequisites

-   Dynamics 365 Customer Insights license
-   Adobe Experience Platform license
-   Adobe Campaign Standard license
-   Azure Blob Storage account

## Campaign Overview

To better understand how you can use segments from audience insights in Adobe Experience Platform, let’s look at a fictitious sample campaign.

Let’s assume that your company offers a monthly, subscription-based service to your customers in the United States. You want to identify customers whose subscriptions are due for renewal in the next eight days but haven't yet renewed their subscription. To keep these customers, you want to send them a promotional offer via email, using Adobe Experience Platform.

In this example, we want to run the promotional email campaign once. This article doesn’t cover the use-case of running the campaign more than once.

## Identify your target audience

In our scenario, we assume that the email addresses of the customers are available in audience insights and their promotional preferences were analyzed to identify members of the segment.

The [segment you defined in audience insights](segments.md) is called **ChurnProneCustomers** and you plan to send these customers the email promotion.

:::image type="content" source="media/churn-prone-customers-segment.png" alt-text="Screenshot of the segments page with the ChurnProneCustomers segment created.":::

The offer email that you want to send out will contain the first name, last name, and the subscription end date of the customer. It informs the customers about the discount they’ll get if they renew their subscription before it ends.

## Export your target audience

With our target audience identified, we can configure the export from audience insights to an Azure Blob Storage account.

1. In audience insights, go to **Admin** > **Export destinations**.

1. In the **Azure Blob Storage** tile, select **Set up**.

   :::image type="content" source="media/export-azure-blob-storage-tile.png" alt-text="Configuration tile for Azure Blob Storage.":::

1. Provide a **Display name** for this new export destination and then enter the **Account name**, **Account key**, and **Container** of the Azure Blob Storage account where you want to export the segment to.  
      
   :::image type="content" source="media/azure-blob-configuration.png" alt-text="Screenshot of the storage account configuration. "::: 

   - To learn more about how to find the Azure Blob storage account name and account key, see [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage).

   - To learn how to create a container, see [Create a container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).

1. Select **Next**.

1. Choose the segment that you want to export. In this example, it’s **ChurnProneCustomers**.

   :::image type="content" source="media/select-segment-churnpronecustomers.png" alt-text="Screenshot of the segment selection user interface with ChurnProneCustomers segment selected.":::

1. Select **Save**.

After saving the export destination, you find it on **Admin** > **Exports** > **My export destinations**.

:::image type="content" source="media/export-destination-azure-blob-storage.png" alt-text="Screenshot with list of exports and sample segment highlighted.":::

You can now [export the segment on demand](export-destinations.md#run-exports-on-demand). The export will also run with every [scheduled refresh](system.md).

> [!NOTE]
> Ensure that the number of records in the exported segment are within the allowed limit of your Adobe Campaign Standard license.

Exported data is stored in the Azure Blob storage container you configured above. The following folder path is automatically created in your container:

*%ContainerName%/CustomerInsights_%instanceID%/%ExportDestinationName%/%EntityName%/%Year%/%Month%/%Day%/%HHMM%/%EntityName%_%PartitionId%.csv*

Example: Dynamics365CustomerInsights/CustomerInsights_abcd1234-4312-11f4-93dc-24f72f43e7d5/BlobExport/ChurnSegmentDemo/2021/02/16/1433/ChurnProneCustomers_1.csv

The *model.json* for the exported entities resides at the *%ExportDestinationName%* level.

Example: Dynamics365CustomerInsights/CustomerInsights_abcd1234-4312-11f4-93dc-24f72f43e7d5/ChurnSegmentDemo/model.json

## Define Experience Data Model (XDM) in Adobe Experience Platform

Before the exported data from audience insights can be used within Adobe Experience Platform, we need to define the Experience Data Model schema and [configure the data for the Real-time Customer Profile](https://experienceleague.adobe.com/docs/experience-platform/profile/tutorials/dataset-configuration.html#tutorials).

Learn [what XDM is](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html) and understand the [basics of schema composition](https://experienceleague.adobe.com/docs/experience-platform/xdm/schema/composition.html#schema).

## Import data into Adobe Experience Platform

Now that everything is in place, we need to import the prepared audience data from audience insights into Adobe Experience Platform.

First, [create an Azure Blob Storage source connection](https://experienceleague.adobe.com/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/blob.html#getting-started).    

After defining the source connection, [configure a dataflow](https://experienceleague.adobe.com/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage.html#ui-tutorials) for a cloud storage batch connection to import the segment output from audience insights into Adobe Experience Platform.

## Create an audience in Adobe Campaign Standard

To send the email for this campaign, we will use Adobe Campaign Standard. After importing the data into Adobe Experience Platform, we need to [create an audience](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/get-started-profiles-and-audiences.html#permission) in Adobe Campaign Standard using the data in Adobe Experience Platform.

Learn how to [use segment builder](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/working-with-adobe-experience-platform/aep-using-segment-builder.html#building-a-segment) in Adobe Campaign Standard to define an audience based on the data in Adobe Experience Platform.

## Create and send the email using Adobe Campaign Standard

Create the email content and then [test and send](https://experienceleague.adobe.com/docs/campaign-standard/using/testing-and-sending/get-started-sending-messages.html#preparing-and-testing-messages) your email.

:::image type="content" source="media/contoso-sample-email.jpg" alt-text="Sample email with renewal offer from Adobe Campaign Standard.":::