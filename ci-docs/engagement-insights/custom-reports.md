---
title: About custom reports
description: Learn how to create and custom reports.
author: mochimochi016
ms.reviewer: mhart
ms.author: jefhar
ms.date: 10/01/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Create and edit custom reports

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

In addition to out-of-box (OOB) reports, you can build a custom report with chart and table visualizations to help you understand user behavior. This article explains how to create a report with the data you need using table and chart visualizations. For information about OOB reports, see [View reports](view-reports.md).

## Create a custom report

1. Go to **Analyze** > **Custom** to access the custom report list.

1. Select **New report** to start creating a custom report.

   :::image type="content" source="media/new-custom-report.png" alt-text="New custom reports.":::

1. Decide the type of report you want to build:

    - Select **Add visual** in the command bar to create a default table visualization.
    - Or, select a column, bar, line, area, pie, donut, or table visualization from the **Report editor** pane.

1. In the **Data** section of the **Visualization editor** pane, choose one of the available options (for example, page views) from the **Metrics** dropdown. You can also add **Dimensions** (for example, country) to show on the visualization. For more information, see [View and create metrics](metrics.md) and [View and create dimensions](dimensions.md).

   :::image type="content" source="media/page-views.png" alt-text="Choose a metric for your report.":::

1. Select the **Design** section of the **Visualization editor** pane to add **Title text** and toggle the **Title** on and off.  You can also change the visualization type by selecting another chart, such as **pie chart**.

1. To change the size and position of a visualization:
   - Select the visualization and then drag one of the corners or borders to adjust its size.
   - Select the visualization and move it to a new position. You can also use the arrow keys to change the position.
1. To add another visualization, select **Add visual** in the command bar.
1. After adding the visualizations you want for the report, select **Save** in the command bar.

1. Provide a name for the custom report and select **Save** to create it.
 
## Filter a custom report

You can select the time frame or date range in a custom report to focus on a value or time period.

To select a time frame, in the upper-right corner of the report view, select a value from the dropdown list of the report. You can also choose a **Fixed date range*.

:::image type="content" source="media/filter-time-date-range.png" alt-text="Filter by time or date range.":::

For most reports, select **+ Add condition**, to choose a dimension or segment to filter the report. For more information, see [View and create segments](segments.md).

## Edit a custom report

1. Go to **Analyze** > **Custom** to access the custom report list.

1. In the custom report list, select **More [...]** 

1. Choose **Edit name** to change the name of the report.

1. Select the name of the report and use the **+ Add visual** and **Edit** options to add, remove, reposition, or resize the visualizations.

1. To change the properties of a visualization, select the visual, select **...** and then **Edit visual**.

   :::image type="content" source="media/edit-visual-control.png" alt-text="Editing chart properties for custom reports.":::

1. After editing the report, select **Save** to apply your changes. 

## Delete a custom report

1. Go to **Analyze** > **Custom** to access the custom report list.

1. In the custom report list, select **...**

1. Choose **Delete** to remove the report.

1. Confirm your deletion to remove the report permanently.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
