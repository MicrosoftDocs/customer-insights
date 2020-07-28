---
uid: topics/derived-signals
title: Create and export derived signals
author: ruthaisabokhae
description: How to create and export derived signals
ms.author: ruthai
ms.date: 07/27/2020
ms.service: product-insights
ms.topic: conceptual
---

# Create and export derived signals

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

A derived signal is a virtual view of a base signal. These are generally used for scoping down a base signal for export, or for cleaning up a signal containing properties that aren't necessary for exposure or export.

Admins can define derived signals by removing and adding properties, as well as filtering events based on property values.

## Create a derived signal

There are three ways to create a derived signal from a base signal. Start by navigating to **Admin** > **Data** > **Signals**, then choose any one of the following options:

- Select **+ Add signals** and choose **Create derived signal**.
- Select **...** from the table row containing a base signal, then select **Create derived signal** from the dropdown menu.
- Select the a base signal to open a detailed view, then select **Create a derived signal** from the top menu.

## Modify a derived signal

Once created, you'll be taken to a detailed view of your new derived signal. This signal will have the same properties as your base signal by default.

### Add and remove properties

From the detailed view of your derived signal, select **Add and remove properties** to open the **Edit properties** pane. Use the checkboxes to indicate which properties you want to show and which ones you want to hide. Select **Confirm** to apply your selection.

### Rename properties

From the detailed view of your derived signal, select the arrow next to a property, then select **Edit name** from the dropdown menu. Enter a new name and select **Confirm** to apply your changes.

> [!TIP]
> Renaming doesn't change the initial property. Instead, it creates a copy of the original with a new name, and then hides the original from view. If you want to access the original property, you can find it using the **Add and remove** properties menu.

## Filter properties

From the detailed view of your derived signal, select the arrow next to a property, then select **Add filters** from the dropdown menu.

Select **+ Add filter** and choose an operation and a value. If you add multiple filters to a signal, they will be connected with a logical "AND" operator. Select **Confirm** to apply the filters.

You'll see a filter icon next to the property's name in the detailed view if filters are successfully added.

## Export a derived signal

Signals, including derived signals, can be exported to an external storage.

From the **Signals** page, select **...** next to the signal you want to export and select **Export** from the dropdown menu. You will be guided through the five steps of export creation:

1. Provide a **Name** for the export.
2. Select a signal for export, and an export cadence. The cadence informs how often an immutable folder with your signal's information will be created in Azure Data Lake Storage (ADLS).
3. Select the format for your export
4. Specify the ADLS location and your credentials.
5. Review and confirm your selections.

Once you've set up an export, it can be viewed by navigating to **Admin** > **Data** > **Exports**. Use the **...** selections on this page to edit or delete an existing export as desired.
