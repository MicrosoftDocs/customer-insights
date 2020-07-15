---
uid: topics/derived-signals
title: Create and export derived signals
author: ruthaisabokhae
description: How to create and export derived signals
ms.author: ruthai
ms.date: 07/15/2020
ms.service: product-insights
ms.topic: conceptual


# Create and export derived signals

A derived signal is a virtual view of a base signal. These are generally used for scoping down a base signal for export, or for cleaning up a signal containing properties that aren't necessary for exposure or export.

Admins can define derived signals by removing and adding properties, as well as filtering events based on property values.

## Create a derived signal

There are three ways to create a derived signal from a base signal. Start by navigating to **Admin** -> **Data** -> **Signals**, then choose any one of the following options:

- Select **+ Add signals** and choose the **Create derived signal** option before proceeding with signal creation.
- Select **...** from the table row containing your desired base signal, then select **Create derived signal** from the dropdown menu.
- Select the name of your desired base signal to open a detailed view, then select **Create a derived signal** from the top menu.

## Modify a derived signal

Once created, you'll be taken to a detailed view of your new derived signal. This signal will contain all the same properties as your base signal by default.

### Add and remove properties

From the detailed view of your derived signal, select **Add and remove properties** to open the **Edit properties** pane. Use the checkboxes to indicate which properties you want to show and which ones you want to hide. Once you are done, select **Confirm**.

### Rename properties

From the detailed view of your derived signal, select the arrow next to a property, then select **Edit name** from the dropdown menu. Enter a new name and **Confirm**.

Renaming doesn't actually change the initial property. Instead, it creates a copy of the original with a new name, and then hides the original from view. If you want to access the original property, you can find it using the **Add and remove** properties menu.

## Filter properties

From the detailed view of your derived signal, select the arrow next to a property, then select **Add filters** from the dropdown menu.

Select **+ Add filter**, then choose an operation and a value. If you add multiple filters to a signal, they will be connected with a logical "AND" operator. Select **Confirm** when you are done.

If successful, you should see a filter icon appear next to the property's name in the detailed view.

## Export a derived signal

Signals, including derived signals, can be exported to external storage.

From the **Signals** page, select **...** next to the signal you want to export, then select **Export** from the dropdown menu. You will be guided through the five steps of export creation:

1. Name your export.
2. Select a signal for export, and an export cadence. The cadence informs how often an immutable folder with your signal's information will be created in Azure Data Lake Storage (ADLS).
3. Select the format for your export
4. Specify the ADLS location and your credentials.
5. Review and confirm your selections.

Once you've set up an export, it can be viewed by navigating to **Admin** -> **Data** -> **Exports**. Use the **...** selections on this page to edit or delete an existing export as desired.
