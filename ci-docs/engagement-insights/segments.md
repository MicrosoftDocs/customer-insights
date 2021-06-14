---
title: View and create segments
description: How to create, edit, and delete segments and where to use them.
ms.reviewer: mhart
ms.author: jusali
author: jusali
ms.date: 06/09/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# View and create segments

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Segments allow you to identify subsets of visitors based on characteristics or website interactions. Segments let you apply filters and analyze those subsets. The analysis can help examine and respond to trends in your business. 

:::image type="content" source="media/segments-page.png" alt-text="Screenshot of the engagement insights application showing the list of existing segments in a workspace.":::

## View segments

1. Go to **Data** in the left navigation pane. 

1. Select the **Segments** tab to see a list of all segments in the workspace. 

## Create a segment

Segments consist of rules and conditions that are connected with logical operators. Conditions apply filters to a selected dimension. Every segment can use up to five dimensions.

The following example shows a segment with two conditions in a one rule. It filters all website events where the browser is Chrome and the operating systems are iOS or Android.

:::image type="content" source="media/segment-sample.png" alt-text="Example segments with two conditions in a rule to filter for website events.":::

This section describes how to create a *blank segment* from scratch.

1. Go to **Data** > **Segments**.

1. Select **New segment**.

1. In the **Resource library**, choose the attribute you want to filter by. Currently, you can only create segments based on dimensions.

1. Choose an operator and a value for the selected attribute. The following operations are supported.
   - **is**: requires an exact match to include values. Uses **equal to** for a single value or **any of** to include multiple values.
   - **is not**: requires an exact match to exclude values. Uses **equal to** for a single value or **any of** to include multiple values.
   - **starts with**: a string that the matching values start with.
   - **ends with**: a string the matching values ends with.
   - **contains**: a string contained in matching values.

1. To add more conditions to a group, you can use two logical operators. Projected attributes are factored in when using set operators.
   - **AND** operator: Both conditions must be met as part of the segmentation process. This option is most useful when you define conditions across different entities.
   - **OR** operator: Either one of the conditions needs to be met as part of the segmentation process. This option is most useful when you define multiple conditions for the same entity.

1. Select **Save** and name the segment. 

The segment will be listed on the Segments page and you can apply it to all reports and funnels in the workspace.

## Use a segment in a report or funnel

You can apply segments to a report or a funnel to filter them based on the conditions in the segment. However, you can't apply segments to the real-time usage report.

:::image type="content" source="media/segment-reports-filter.png" alt-text="A page views report with an expanded drop-down list to choose which segments to apply.":::

To apply a segment, open the report or funnel. Select **Add condition** and choose **Filter by segment**. Choose the segment from the list that you want to apply. The segment gets be applied to the report. If a chart doesn't support the segment, it shows an error.
 
You can apply *up to three segments* to a report or funnel.

## Edit a segment

1. Go to **Data** > **Segments**.
1. Select the segment in the list to open it. 
1. Change or add values as needed.
1. Select **Save** to apply your changes.

## Change the name of a segment

1. Go to **Data** > **Segments**.
1. In the segment list, select **More [...]**. 
1. From the drop-down list, choose **Edit name**.
1. Enter the new name and select **Rename**.

## Delete a segment

1. Go to **Data** > **Segments**.
1. In the segment list, select **More [...]**. 
1. From the drop-down list, choose **Delete**.
1. Select **Delete** to confirm.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
