---
title: "Power BI connector (preview)"
description: "Learn how to use the Dynamics 365 Customer Insights connector in Power BI."
ms.date: 07/25/2022
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

1. In the **Navigator** dialog box, view the list of all environments you have access to. Expand an environment and open any of the folders (entities, measures, segments, enrichments). For example, open the **Entities** folder, to see all entities you can import.

   :::image type="content" source="media/power-bi-navigator.png" alt-text="Power BI Connector Navigator.":::

1. Select the check boxes next to the entities to include and **Load**. You can select multiple entities from multiple environments.

   A loading dialog box displays while your entities are loaded. Once all of your selected entities have loaded, use the capabilities of Power BI to visualize the data.

## Large data sets

The Customer Insights connector for Power BI is designed to work for data sets that contain up to 1 million customer profiles. Importing larger data sets may work, but takes a long time and could time-out because of Power BI limitations. For more information, see [Power BI: Recommendations for large data sets](/power-bi/admin/service-premium-what-is#large-datasets).

### Work with a subset of data

Consider working with a subset of your data. For example, create [segments](segments.md) instead of exporting all customer records to Power BI.

## Troubleshooting

### Customer Insights environment doesn't show in Power BI

Environments that have more than one [relationship](relationships.md) defined between two identical entities in Customer Insights will not be available in the Power BI connector.

Identify and remove the duplicated relationships.

1. Go to **Data** > **Relationships** on the environment you're missing in Power BI.
1. Identify duplicated relationships:
   - Check if there is more than one relationship defined between the same two entities.
   - Check if there is a relationship created between two entities that are both included in the unification process. There is an implicit relationship defined between all entities included in the unification process.
1. Remove any duplicate relationships identified.

After removal of the duplicated relationships, try to configure the Power BI connector again.

### Errors on date fields when loading entities in Power BI Desktop

When loading entities that contain fields with a date format like MM/DD/YYYY, you might encounter errors due to mismatched locale formats. This mismatch happens when your Power BI Desktop file is set to another locale than English (United States), because date fields in Customer Insights are saved in US format.

The Power BI Desktop file has a single locale setting, which is applied when retrieving data. To fix the date errors, [set the locale of the .BPI file](/power-bi/fundamentals/supported-languages-countries-regions#choose-the-language-or-locale-of-power-bi-desktop) to English (United States).

[!INCLUDE [footer-include](includes/footer-banner.md)]
