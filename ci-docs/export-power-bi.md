---
title: "Power BI connector (preview)"
description: "Learn how to use the Dynamics 365 Customer Insights connector in Power BI."
ms.date: 11/15/2022
ms.reviewer: mhart

ms.topic: how-to
author: Nils-2m
ms.author: nikeller
---

# Power BI connector (preview)

Create visualizations for your data with the Microsoft Power BI Desktop. Generate additional insights and build reports with your unified customer data.

## Prerequisites

- Unified customer profiles.
- The latest version of [Microsoft Power BI Desktop](https://powerbi.microsoft.com/desktop/) is installed on your computer. [Learn more about Power BI Desktop](/power-bi/desktop-what-is-desktop).

## Configure the connector for Power BI

1. In Power BI Desktop, select **File** > **Get Data**.

1. Select **See more** and search for **Dynamics 365 Customer Insights**

1. Select **Connect**.

1. **Sign in** with the same organizational account you use for Customer Insights and select **Connect**.
   > [!NOTE]
   > The account you indicate in this step is used to fetch data from Customer Insights and doesn't need to be the same you are signed in to Power BI. To reset the account that is used for data fetching, open Power BI and go to **File** > **Options** > **Settings** > **Data source settings**. In the list of data sources, select **Dynamics 365 Customer Insights Login** and select **Clear permissions**.  

1. In the **Navigator** dialog box, view the list of all environments you have access to. Expand an environment and open any of the folders. For example, open the **Segments** folder, to see all tables you can import.

1. Select the check boxes next to the tables to include and **Load**. You can select multiple tables from multiple environments.

   A loading dialog box displays while your tables are loaded. Once all of your selected tables have loaded, use the capabilities of Power BI to visualize the data.

## Large data sets

The Customer Insights connector for Power BI is designed to work for data sets that contain up to 1 million customer profiles. Importing larger data sets may work, but takes a long time and could time-out because of Power BI limitations. For more information, see [Power BI: Recommendations for large data sets](/power-bi/admin/service-premium-what-is#large-datasets).

### Work with a subset of data

Consider working with a subset of your data. For example, create [segments](segments.md) instead of exporting all customer records to Power BI.

> [!TIP]
> For troubleshooting information, go to [Microsoft Dynamics 365 Customer Insights troubleshooting](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights).

[!INCLUDE [footer-include](includes/footer-banner.md)]
