---
title: Download and use marketing analytics templates and sample reports for Power BI
description: Download and use Power BI templates and sample reports to create custom analytics reports for your Customer Insights - Journeys organization.
ms.date: 08/17/2023
ms.topic: how-to
author: cabeln
ms.author: cabeln
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing, evergreen
---

# Download and use marketing analytics templates and sample reports for Power BI

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

[!INCLUDE [marketing-trial-cta](.././includes/marketing-trial-cta.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](../transition-overview.md).

This article provides a gallery with links to downloads and details for each Microsoft Power BI template and sample report that's currently available for Dynamics 365 Customer Insights - Journeys. It also explains how to connect a downloaded template to your Dynamics 365 Customer Insights - Journeys instance. These resources help you produce custom analytics reports with Power BI for your Dynamics 365 Customer Insights - Journeys organization.

<a name="gallery"></a>

## Gallery: Download Power BI reports and templates

> [!TIP]
> Download your analytics reports and templates directly from our gallery&mdash;ready to use with Dynamics 365 Customer Insights - Journeys!

Choose from a growing number of marketing reports for easy download, and find the information to help you select the reports that fit your needs. Each template and report provides useful views, charts, and analytics. You can use the standard features of the Power BI Desktop to explore the data sources and analytical displays, and customize them to meet your own organization's requirements.

|Name  |Description  |Template  |Report  |
|---------|---------|---------|---------|
|[Generic template (framework and tools)](analytics-gallery-framework.md)|This report provides generic parameters, data sources, and query code you can use to query for any marketing data from Microsoft Dataverse and the interaction store.|[![Download template.](media/IconDownloadTemplate30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/PowerBI-Templates/PowerBI%20Template%20-%20Dynamics%20365%20for%20Marketing.pbit)|[![Download sample report](media/IconDownloadReport30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/pbx%20files/PowerBI%20Template%20-%20Dynamics%20365%20for%20Marketing.pbix)|
|[Basic leaderboard report (journeys and email marketing)](analytics-gallery-leaders.md)|Identify your most effective journeys and marketing messages.|[![Download template.](media/IconDownloadTemplate30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/PowerBI-Templates/MarketingAnalyzers%20-%20Journey%26Email%20Leaderboard.pbit)|[![Download sample report](media/IconDownloadReport30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/pbx%20files/MarketingAnalyzers%20-%20Journey%26Email%20Leaderboard.pbix)|
|[Email marketing report](analytics-gallery-email.md)|Deep-dive into your email marketing plans, activities, and interactions.|[![Download template.](media/IconDownloadTemplate30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/PowerBI-Templates/MarketingAnalyzers%20-%20Email%20Marketing.pbit)|[![Download sample report](media/IconDownloadReport30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/pbx%20files/MarketingAnalyzers%20-%20Email%20Marketing.pbix)|
|[Segmentation report](analytics-gallery-segments.md)|Analyze how segments are used in your marketing activities.|[![Download template.](media/IconDownloadTemplate30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/PowerBI-Templates/MarketingAnalyzers%20-%20Segmentation.pbit)|[![Download sample report](media/IconDownloadReport30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/pbx%20files/MarketingAnalyzers%20-%20Segmentation.pbix)|
|[Marketing program effectiveness](analytics-gallery-program.md)|Analyze the end-to-end effectiveness of your marketing programs, including automation, journeys, channels, lead generation, conversion, and revenue generation.|[![Download template.](media/IconDownloadTemplate30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/PowerBI-Templates/MarketingAnalyzers%20-%20Marketing%20Automation.pbit)|[![Download sample report](media/IconDownloadReport30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/pbx%20files/MarketingAnalyzers%20-%20Marketing%20Automation.pbix)|
|[Marketing reach analysis](analytics-gallery-reach.md)|Identify contacts and how you're reaching out to them. See all audiences reached in selected journeys, together with their related interactions.|[![Download template.](media/IconDownloadTemplate30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/PowerBI-Templates/MarketingAnalyzers%20-%20Customers%20Included%20In%20Journeys.pbit)|[![Download sample report](media/IconDownloadReport30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/pbx%20files/MarketingAnalyzers%20-%20Customers%20Included%20In%20Journeys.pbix)|
|[Marketing form submission report](analytics-gallery-forms.md)|Get an overview of the submission stream across all your marketing forms.|[![Download template.](media/IconDownloadTemplate30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/PowerBI-Templates/MarketingAnalyzers%20-%20Form%20Submissions.pbit)|[![Download sample report](media/IconDownloadReport30.png)](https://github.com/microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting/raw/master/pbx%20files/MarketingAnalyzers%20-%20Form%20Submissions.pbix)|

The source code for all of these reports is [available publicly on GitHub](https://github.com/Microsoft/Dynamics-365-for-Marketing---Power-BI-Reporting).

![A collage of various Power BI reports.](media/Overview-Hero1.png "A collage of various Power BI reports")

<a name="connect-dialog"></a>

## Connect a Power BI template to your Dynamics 365 Customer Insights - Journeys instance

After your Azure Blob storage is [set up and connected to Dynamics 365 Customer Insights - Journeys](../custom-analytics.md), you're ready to start working in Power BI to connect to your data sources and design your analytics.

1. If you haven't done so already, download the templates you need from the gallery.

1. Select a template and open it in Power BI Desktop. If you don't already have Power BI Desktop, you can download it for free from [https://powerbi.microsoft.com/desktop/](https://powerbi.microsoft.com/desktop/).

1. The first time you open a Power BI template, you'll be asked to specify connection strings and credentials to connect to both Azure Blob storage and to Dynamics 365 Customer Insights - Journeys.

    ![The connection dialog for connecting your Power BI template to the relevant data sources.](../media/custom-analytics-pbi-connect.png "The connection dialog for connecting your Power BI template to the relevant data sources")

    - To connect to the Dynamics 365 database, use the same user credentials that you use to sign in to Customer Insights - Journeys.
    - You can [find connection details for your Azure Blob storage](../custom-analytics.md#connect-blob) by using Azure Storage Explorer.
    - Specify how many days of interaction data that you want to load (counting back from today).

1. Select **Load** to load the template into Power BI.

    > [!NOTE]
    > If you see loading errors the first time you open a template, open the query editor, select a query that has been highlighted with a warning icon, and then select **Retry** on the notification message bar. Repeat for each query that shows a warning. After all queries have loaded, select **Close & Apply**.

    > [!IMPORTANT]
    > There is a **two hour** limit for Power BI report refresh. To prevent a timeout, we recommend keeping the data in your blob storage under these limits:
    > -	50,000 blobs in total
    > -	5GB of data in total


<!-- [kfm: this video is being edited and will be hosted elsewhere. Revive this section and update the embed when it's ready]

## A video guide to data available for marketing analytics

Watch [the following video](https://www.youtube.com/watch?v=pBrB1BohUrE)
for a quick overview of all the data that's available for your marketing analytics reports.<br/><br/>

> [!VIDEO https://www.youtube.com/embed/pBrB1BohUrE]
## Learn more

Here are some advanced resources for this topic:

- [Extracting Marketing Interactions in Dynamics 365 Marketing](https://community.dynamics.com/blogs/post/?postid=4e96ca1e-52ed-4ae4-9887-af8d6e563304)

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
