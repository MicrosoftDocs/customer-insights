---
title: "Export segments to Adobe Campaign Standard (preview)"
description: "Learn how use Customer Insights - Data segments in Adobe Campaign Standard."
ms.date: 11/06/2024
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to Adobe Campaign Standard (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments that target relevant audiences to Adobe Campaign Standard.

:::image type="content" source="media/ACS-flow.png" alt-text="Process diagram of the steps outlined in this article.":::

## Prerequisites

- An Adobe Campaign Standard license to use Adobe Campaign.
- To setup the export in Customer insights the same prerequisites as for [Export to Azure Blob storage](export-azure-blob-storage.md) apply:
  - An [Azure Blob Storage account with a container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).
  - User who sets up the connection must have the permission to access the content of the container. For example, a [Blob Storage Contributor](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) role.
  - The [Customer Insights Service Principal](connect-service-principal.md) has write permissions on the container. For example, a [Blob Storage Contributor](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) role.

## Campaign overview

To better understand how you can use segments from Dynamics 365 Customer Insights - Data in Adobe Experience Platform, let’s look at a fictitious sample campaign.

Let’s assume that your company offers a monthly, subscription-based service to your customers in the United States. You want to identify customers whose subscriptions are due for renewal in the next eight days but haven't yet renewed their subscription. To keep these customers, you want to send them a promotional offer via email, using Adobe Campaign Standard.

In this example, we want to run the promotional email campaign once. This article doesn’t cover the use-case of running the campaign more than once. However, Customer Insights - Data and Adobe Campaign Standard can be configured to work for a recurring campaign scenario too.

## Identify your target audience

In our scenario, we assume that the email addresses of the customers are available in Customer Insights - Data and their promotional preferences were analyzed to identify members of the segment.

The [segment you defined in Customer Insights - Data](segments.md) is called **ChurnProneCustomers** and you plan to send these customers the email promotion.

:::image type="content" source="media/churn-prone-customers-segment.png" alt-text="Screenshot of the segments page with the ChurnProneCustomers segment created.":::

The offer email that you want to send out will contain the first name, last name, and the subscription end date of the customer. It informs the customers about the discount they’ll get if they renew their subscription before it ends.

## Export your target audience

### Set up connection to Adobe Campaign

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Adobe Campaign**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter **Subscription**, **Resource group**, **Storage account**, and **Container** for your Blob Storage account.

1. Optionally, if your storage account is behind a firewall, select **Enable Private Link**. For more information, go to [Private Links](private-link.md).

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

### Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Adobe Campaign section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Choose the segment that you want to export. In this example, it's **ChurnProneCustomers**.

   :::image type="content" source="media/select-segment-churnpronecustomers.png" alt-text="Screenshot of the segment selection user interface with ChurnProneCustomers segment selected.":::

1. Select **Next**.

1. Map the **Source** fields from the segment to the **Target** field names in the Adobe Campaign Standard profile schema.

   :::image type="content" source="media/ACS-field-mapping.png" alt-text="Field mapping for the Adobe Campaign Standard connector.":::

   If you want to add more attributes, select **Add attribute**. The target name can be different from the source field name so you can still map segment output from Customer Insights - Data to Adobe Campaign Standard if the fields don’t have the same name in the two systems.

   > [!NOTE]
   > Email address is used as an identity field but you can use any other identifier from the customer profile to map data to Adobe Campaign Standard.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

> [!NOTE]
> Ensure that the number of records in the exported segment are within the allowed limit of your Adobe Campaign Standard license.

Exported data is stored in the Azure Blob Storage container you configured above. The following folder path is automatically created in your container:
*%ContainerName%/CustomerInsights_%instanceID%/% exportdestination-name%_%segmentname%_%timestamp%.csv*

Example: Dynamics365CustomerInsights/CustomerInsights_abcd1234-4312-11f4-93dc-24f72f43e7d5/ChurnSegmentDemo_ChurnProneCustomers_1613059542.csv

## Configure Adobe Campaign Standard

Exported segments contain the columns you selected while configuring the export. This data can be used to [create profiles in Adobe Campaign Standard](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/managing-profiles/about-profiles.html#managing-profiles).

To use the segment in Adobe Campaign Standard, [extend the profile schema](https://experienceleague.adobe.com/docs/campaign-standard/using/developing/use-cases--extending-resources/extending-the-profile-resource-with-a-new-field.html#developing) in Adobe Campaign Standard to include two additional fields.

In our example, these fields are Segment Name and Segment Date. We will use these fields to identify the profiles in Adobe Campaign Standard we want to target for this campaign.

If there are no other records in Adobe Campaign Standard, other than what you are going to import, skip this step.

## Import data into Adobe Campaign Standard

Import the prepared audience data from Customer Insights into Adobe Campaign Standard to [create profiles using a workflow](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/managing-profiles/creating-profiles.html#profiles-and-audiences).

The import workflow in the image below has been configured to run every eight hours and look for exported segments (.csv file in Azure Blob Storage). The workflow extracts the .csv file content in a specified column order. This workflow has been built to perform basic error handling and ensure that each record has an email address before hydrating the data in Adobe Campaign Standard. The workflow also extracts the segment name from the filename before upserting into Adobe Campaign Standard profile data.

:::image type="content" source="media/ACS-import-workflow.png" alt-text="Screenshot of an import workflow in the Adobe Campaign Standard user interface.":::

## Retrieve the audience in Adobe Campaign Standard

Once the data is imported into Adobe Campaign Standard, [create a workflow](https://experienceleague.adobe.com/docs/campaign-standard/using/managing-processes-and-data/workflow-general-operation/building-a-workflow.html#managing-processes-and-data) and [query](https://experienceleague.adobe.com/docs/campaign-standard/using/managing-processes-and-data/targeting-activities/query.html#managing-processes-and-data) the customers based on the Segment Name and Segment Date to select profiles that were identified for our sample campaign.

## Create and send the email using Adobe Campaign Standard

Create the email content and then [test and send](https://experienceleague.adobe.com/docs/campaign-standard/using/testing-and-sending/get-started-sending-messages.html#preparing-and-testing-messages) your email.

:::image type="content" source="media/contoso-sample-email.jpg" alt-text="Sample email with renewal offer from Adobe Campaign Standard.":::

[!INCLUDE [footer-include](includes/footer-banner.md)]
