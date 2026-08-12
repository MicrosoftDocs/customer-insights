---
title: Power BI connector (preview)
description: Use Power BI for Dynamics 365 Customer Insights to visualize unified customer profiles. Learn how to configure the connector and load tables into Power BI.
ms.date: 08/11/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom:
 - ai-gen-docs-bap
 - ai-seo-date: 08/11/2026
ai-usage: ai-assisted
---

# Power BI connector (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Create visualizations for your data with Microsoft Power BI Desktop. Generate more insights and build reports with your unified customer data.

> [!TIP]
> Use one of the default options [to use Power BI with Dataverse data](/power-apps/maker/data-platform/use-powerbi-dataverse). You benefit from our [integration into Dataverse](integrate-d365-apps.md).
> You can access insights in Microsoft Fabric by using the [Dataverse link to Fabric and Microsoft OneLake](/power-apps/maker/data-platform/azure-synapse-link-view-in-fabric).

## Prerequisites

- Unified customer profiles.
- The latest version of [Microsoft Power BI Desktop](https://powerbi.microsoft.com/desktop/) installed on your computer. [Learn more about Power BI Desktop](/power-bi/desktop-what-is-desktop).

## Configure the connector for Power BI

1. In Power BI Desktop, select **File** > **Get Data**.

1. Select **See more** and search for **Dynamics 365 Customer Insights**.

1. Select **Connect**.

1. **Sign in** with the same organizational account you use for Customer Insights - Data and select **Connect**.
   > [!NOTE]
   > The account you provide in this step fetches data from Customer Insights - Data and doesn't need to be the same account you use to sign in to Power BI. To reset the account used for data fetching, open Power BI and go to **File** > **Options** > **Settings** > **Data source settings**. In the list of data sources, select **Dynamics 365 Customer Insights Login** and select **Clear permissions**.  

1. In the **Navigator** dialog box, view the list of all environments you have access to. Expand an environment and open any of the folders. For example, open the **Segments** folder to see all tables you can import.

1. Select the check boxes next to the tables to include and **Load**. You can select multiple tables from multiple environments.

   A loading dialog box displays while Power BI loads your tables. Once all of your selected tables load, use the capabilities of Power BI to visualize the data.

## Large data sets

The Customer Insights - Data connector for Power BI works with data sets that contain up to 1 million rows in the table. Importing larger data sets might work, but it takes a long time and could time out because of Power BI limitations. For more information, see [Power BI: Recommendations for large data sets](/power-bi/admin/service-premium-what-is#large-datasets).

### Work with a subset of data

Consider working with a subset of your data. For example, create [segments](segments.md) instead of exporting all customer records to Power BI.

> [!TIP]
> For troubleshooting information, see [Microsoft Dynamics 365 Customer Insights - Data troubleshooting](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights).

[!INCLUDE [footer-include](includes/footer-banner.md)]
