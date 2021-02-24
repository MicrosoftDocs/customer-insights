## Use Customer Insights segments in Adobe Experience Platform

As a user of audience insights for Dynamics 365 Customer Insights, you may have created segments to make your marketing campaigns more efficient by targeting relevant audiences. To use a segment from audience insights in Adobe Experience Platform and application like Adobe Campaign Standard, you need to follow a few steps outlined in this article.

![Graphical user interface, application Description automatically generated](media/61297cd989c77b0685000c4221c03a7e.png)

## Prerequisites

-   Dynamics 365 Customer Insights license
-   Adobe Experience Platform license
-   Adobe Campaign Standard license
-   Azure Blob Storage account

## Campaign Overview

To better understand how you can use segments from audience insights in Adobe Experience Platform, let’s look at a fictitious sample campaign.

Let’s assume that your company offers a monthly, subscription-based service to your customers in the United States. You want to identify customers whose subscriptions are due for renewal in the next 8 days but have not yet renewed their subscription. To retain these customers, you want to send them a promotional offer via email, using Adobe Experience Platform.

In this example, we want to run the promotional email campaign once. This article doesn’t cover the use-case of running the campaign more than once.

## Identify your target audience

In our scenario, we assume that the email addresses of the customers are available in audience insights and their promotional preferences were analyzed using the subscription churn prediction model to identify members of the segment.

The segment you defined in audience insights is called **ChurnProneCustomers** and you plan to send these customers the email promotion.

![Graphical user interface, application Description automatically generated](media/0964e3bd8079e1264cb49c3d19840971.png)

The offer email that you want to send out will contain the first name, last name, and the subscription end date of the customer. It informs the customers about the discount they’ll get if they renew their subscription before it ends.

## Export your target audience

With our target audience identified, we can configure the export from audience insights to an Azure Blob Storage account.

1. In audience insights, go to **Admin** > **Export destinations**.

1. In the **Azure Blob Storage** tile, select **Set up**.

   ![Graphical user interface, text, application, email Description automatically generated](media/e0ed35ef156f7a667b5680c9cefee63a.png)

1. Provide a **Display name** for this new export destination and then enter the **Account name**, **Account key** and **Container** of the Azure Blob Storage account where you want to export the segment to.  

   ![Graphical user interface, text, application, email Description automatically generated](media/75dd25e318d5105418c2f4c587e2e402.png)

   - To learn more about how to find the Azure Blob storage account name and account key, see [Manage storage account settings in the Azure portal](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage).
   - To learn how to create a container, see [Create a container](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).

1. Select **Next**.

1. Choose the segment that you want to export. In this example, it’s **ChurnProneCustomers**.

   ![Graphical user interface, text, application, email Description automatically generated](media/0adebaa6983b9b2eab0cb499554067a4.png)

1. Select **Save**.

After saving the export destination, you find it on **Admin** > **Exports** > **My export destinations**.

![Graphical user interface, text, application Description automatically generated](media/e85c303e147480b24f98d061a329a9a4.png)

This export destination is now enabled and will automatically export data during each data refresh run.

Exported data is stored in the Azure Blob storage container you configured above. The following folder path is automatically created in your container:

*%ContainerName%/CustomerInsights_%instanceID%/%ExportDestinationName%/%EntityName%/%Year%/%Month%/%Day%/%HHMM%/%EntityName%_%PartitionId%.csv*

Example: Dynamics365CustomerInsights/CustomerInsights_abcd1234-4312-11f4-93dc-24f72f43e7d5/BlobExport/ChurnSegmentDemo/2021/02/16/1433/ChurnProneCustomers_1.csv

The model.json for the exported entities will reside at the %ExportDestinationName% level.

Example: Dynamics365CustomerInsights/CustomerInsights_abcd1234-4312-11f4-93dc-24f72f43e7d5/ChurnSegmentDemo/model.json

## Define Experience Data Model (XDM) in Adobe Experience Platform

Before any of the data exported from Audience Insights can be used within Adobe Experience Platform, we would need to define the Experience Data Model schema.

Learn [what XDM is](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html?lang=en) and understand the [basics of schema composition](https://experienceleague.adobe.com/docs/experience-platform/xdm/schema/composition.html?lang=en#schema).

## Import data into Adobe Experience Platform

Now that we have everything setup, we would need to import the Audience Insights’ audience data, that we have prepared, into Adobe Experience Platform.

To begin, [create an Azure Blob source connection](https://experienceleague.adobe.com/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/blob.html?lang=en#getting-started) in the UI. Once you have the source connection defined, [configure a dataflow](https://experienceleague.adobe.com/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage.html?lang=en#ui-tutorials) for a cloud storage batch connection in the UI to import the Audience Insights’ segment output into Adobe Experience Platform.

## Create an audience in Adobe Campaign Standard

In order to send the email for this campaign, we will use Adobe Campaign Standard. Once the data is imported into Adobe Experience Platform, we would need to create an [audience](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/get-started-profiles-and-audiences.html?lang=en#permission) in Adobe Campaign Standard using the data present in Adobe Experience Platform.

Learn how to [use segment builder](https://experienceleague.adobe.com/docs/campaign-standard/using/profiles-and-audiences/working-with-adobe-experience-platform/aep-using-segment-builder.html?lang=en#building-a-segment) in Adobe Campaign Standard to define an audience based on the data present in Adobe Experience Platform.

## Create and send the email using Adobe Campaign Standard

Create the email content and then [test and send](https://experienceleague.adobe.com/docs/campaign-standard/using/testing-and-sending/get-started-sending-messages.html?lang=en#preparing-and-testing-messages) your email.

![Graphical user interface Description automatically generated](media/8f4abf66a452817d9f75a9b6444f7a96.jpg)
