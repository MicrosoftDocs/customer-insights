---
title: Data management settings 
description: Learn how to import, export, and clean data in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/25/2026
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Data management settings

This topic describes what you can do when working in the **Advanced Settings** > **Data Management** section of the **Settings** menu ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") at the top of the page.

<a name="import"></a>

## Import data and manage imports

Bring your customer and sales data quickly into your app by importing it. You can import data into most record types.

Dynamics 365 Customer Insights - Journeys processes imports in the background. After an import is completed, you can review which records were successfully imported, failed to be imported, or were partially imported. To fix the records that failed to be imported, export them into a separate file, fix them, and then try to import them again (if necessary, you can start over by deleting all records associated with the previous import).

Data can be imported from:

- Most list views
- The **Settings** ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") > **Advanced settings** > **Data management** > **Imports** settings page

When you import data while working in the **Settings** work area, you must select the entity you want to import to (such as a lead or contact).

More information: [Import data](import-data.md)

<a name="export"></a>

## Export data or templates

Present information to people who don't have access to Dynamics 365 Customer Insights - Journeys by exporting the data to an Excel workbook. You can export just the data from a list, or you can export a template.

When you export a template, a ready-made workbook with column headings matching the fields of the record is created for you. Templates are already formatted as expected by Dynamics 365, so they are easy to edit and reimport later.

Data and templates can be exported from:

- Most list views
- The **Settings** ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") > **Advanced settings** > **Data management** > **Imports** page

When you export data or templates while working in the **Settings** work area, you must select the entity you want to export (such as a lead or contact). You can also choose the view that will be used for exporting. If you don't choose a view, the default view is selected, and the data or template for all the columns in that view are exported.

More information: [Export data](export-data-word-excel.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
