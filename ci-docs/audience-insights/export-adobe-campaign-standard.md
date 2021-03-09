---
title: "Export Customer Insights data to Adobe Campaign Standard"
description: "Learn how use audience insights segments in Adobe Campaign Standard."
ms.date: 02/26/2021
ms.reviewer: antando
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Use Customer Insights segments in Adobe Campaign Standard (preview)

As a user of audience insights for Dynamics 365 Customer Insights, you may have created segments to make your marketing campaigns more efficient by targeting relevant audiences. To use a segment from audience insights in Adobe Experience Platform and applications like Adobe Campaign Standard, you need to follow a few steps outlined in this article.

:::image type="content" source="media/ACS-flow.png" alt-text="Process diagram of the steps outlined in this article.":::

## Prerequisites

-   Dynamics 365 Customer Insights license
-   Adobe Campaign Standard license
-   Azure Blob Storage account

## Campaign Overview

To better understand how you can use segments from audience insights in Adobe Experience Platform, let’s look at a fictitious sample campaign.

Let’s assume that your company offers a monthly, subscription-based service to your customers in the United States. You want to identify customers whose subscriptions are due for renewal in the next eight days but haven't yet renewed their subscription. To keep these customers, you want to send them a promotional offer via email, using Adobe Campaign Standard.

In this example, we want to run the promotional email campaign once. This article doesn’t cover the use-case of running the campaign more than once. However, audience insights and Adobe Campaign Standard can be configured to work for a recurring campaign scenario too.

## Identify your target audience

In our scenario, we assume that the email addresses of the customers are available in audience insights and their promotional preferences were analyzed to identify members of the segment.

The [segment you defined in audience insights](segments.md) is called **ChurnProneCustomers** and you plan to send these customers the email promotion.

:::image type="content" source="media/churn-prone-customers-segment.png" alt-text="Screenshot of the segments page with the ChurnProneCustomers segment created.":::

The offer email that you want to send out will contain the first name, last name, and the subscription end date of the customer. It informs the customers about the discount they’ll get if they renew their subscription before it ends.

## Export your target audience

With our target audience identified, we can configure the export from audience insights to an Azure Blob Storage account.

1. In audience insights, go to **Admin** > **Export destinations**.

1. In the **Azure Blob Storage** tile, select **Set up**.

   :::image type="content" source="media/adobe-campaign-standard-tile.png" alt-text="Configuration tile for Adobe Campaign Standard.":::

1. Provide a **Display name** for this new export destination and then enter the **Account name**, **Account key**, and **Container** of the Azure Blob Storage account where you want to export the segment to.  
      
   :::image type="content" source="media/azure-blob-configuration.png" alt-text="Screenshot of the storage account configuration. "::: 

   - To learn more about how to find the Azure Blob storage account name and account key, see [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage).

   - To learn how to create a container, see [Create a container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).

1. Select **Next**.

1. Choose the segment that you want to export. In this example, it’s **ChurnProneCustomers**.

   :::image type="content" source="media/select-segment-churnpronecustomers.png" alt-text="Screenshot of the segment selection user interface with ChurnProneCustomers segment selected.":::

1. Select **Next**.

1. Now we map the **Source** fields from the audience insights segment to the **Target** field names in the Adobe Campaign Standard profile schema.

   :::image type="content" source="media/ACS-field-mapping.png" alt-text="Field mapping for the Adobe Campaign Standard connector.":::

   If you want to add more attributes, select **Add attribute**. The target name can be different from the source field name so you can still map segment output from audience insights to Adobe Campaign Standard if the fields don’t have the same name in the two systems.

   > [!NOTE]
   > Email address is used as an identity field but you can use any other identifier from your audience insights customer profile to map data to Adobe Campaign Standard.

1. Select **Save**.

After saving the export destination, you find it on **Admin** > **Exports** > **My export destinations**.

:::image type="content" source="media/export-destination-adobe-campaign-standard.png" alt-text="Screenshot with list of exports and sample segment highlighted.":::

You can now [export the segment on demand](export-destinations.md#export-data-on-demand). The export will also run with every [scheduled refresh](system.md).

> [!NOTE]
> Ensure that the number of records in the exported segment are within the allowed limit of your Adobe Campaign Standard license.

Exported data is stored in the Azure Blob storage container you configured above. The following folder path is automatically created in your container:

*%ContainerName%/CustomerInsights_%instanceID%/% exportdestination-name%_%segmentname%_%timestamp%.csv*

Example: Dynamics365CustomerInsights/CustomerInsights_abcd1234-4312-11f4-93dc-24f72f43e7d5/ChurnSegmentDemo_ChurnProneCustomers_1613059542.csv

## Configure Adobe Campaign Standard

When a segment from audience insights is exported, it contains the columns you selected while defining the export destination in the previous step. This data can be used to [create profiles in Adobe Campaign Standard](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/managing-profiles/about-profiles.html#managing-profiles).

To use the segment in Adobe Campaign Standard, we need to extend the profile schema in Adobe Campaign Standard to include two additional fields. Learn how to [extend the profile resource](https://experienceleague.adobe.com/docs/campaign-standard/using/developing/use-cases--extending-resources/extending-the-profile-resource-with-a-new-field.html#developing) with new fields in Adobe Campaign Standard.

In our example, these fields are *Segment Name and Segment Date (optional).*

We will use these fields to identify the profiles in Adobe Campaign Standard we want to target for this campaign.

If there are no other records in Adobe Campaign Standard, other than what you are going to import, you can skip this step.

## Import data into Adobe Campaign Standard

Now that everything is in place, we need to import the prepared audience data from audience insights into Adobe Campaign Standard to create profiles. Learn [how to import profiles in Adobe Campaign Standard](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/managing-profiles/creating-profiles.html#profiles-and-audiences) using a workflow.

The import workflow in the image below has been configured to run every 8 hours and looks for exported audience insights segments (.csv file in Azure Blob Storage). The workflow extracts the .csv file content in a specified column order. This workflow has been built to perform basic error handling and ensure that each record has an email address before hydrating the data in Adobe Campaign Standard. The workflow also extracts the segment name from the filename before upserting into ACS Profile data.

:::image type="content" source="media/ACS-import-workflow.png" alt-text="Screenshot of an import workflow in the Adobe Campaign Standard user interface.":::

## Retrieve the audience in Adobe Campaign Standard

Once the data is imported into Adobe Campaign Standard, you [can create a workflow](https://experienceleague.adobe.com/docs/campaign-standard/using/managing-processes-and-data/workflow-general-operation/building-a-workflow.html#managing-processes-and-data) and [query](https://experienceleague.adobe.com/docs/campaign-standard/using/managing-processes-and-data/targeting-activities/query.html#managing-processes-and-data) the customers based on the *Segment Name* and *Segment Date* to select profiles that were identified for our sample campaign.

## Create and send the email using Adobe Campaign Standard

Create the email content and then [test and send](https://experienceleague.adobe.com/docs/campaign-standard/using/testing-and-sending/get-started-sending-messages.html#preparing-and-testing-messages) your email.

:::image type="content" source="media/contoso-sample-email.jpg" alt-text="Sample email with renewal offer from Adobe Campaign Standard.":::