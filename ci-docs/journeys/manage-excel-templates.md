---
title: Create and deploy Excel templates
description: Create Excel templates that you can use to export, format, and share data from multiple records in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/21/2023
ms.topic: install-set-up-deploy
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create and deploy Excel templates

Microsoft Excel provides powerful ways to analyze and present your Dynamics 365 data. With Excel templates, you can easily create and share your customized analysis with others in your organization.

You can use Excel templates for:

- Sales forecasting
- Pipeline management
- Leads scoring
- Territory planning
- And much more…

Try out the Excel templates included with Dynamics 365 to get a quick view of what kind of analysis is possible. The Pipeline Management template is shown here:

![An example of an Excel template.](media/excel-template.png "An example of an Excel template")

Templates display information from the view defined for a record type (entity). There are four steps for creating an Excel template.

![The process for creating an Excel template.](media/excel-template-process-ill.png "The process for creating an Excel template")

## Step 1: Create a new template from existing data

1. Sign in to Dynamics 365 as a user with the System Administrator role.

1. Open the **Settings** menu ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") at the top of the page and select **Advanced settings**.

1. The advanced settings area opens in a new browser tab. Note that this area uses a horizontal navigator at the top of the page instead of a side navigator. Navigate to **Settings** > **Business** > **Templates**.

1. On the next screen, select **Document Templates**, then choose **+ New** in the top ribbon.

1. Select **Excel Template**, and then select an entity to which the template applies. The template will use data from this entity. The views you can select in the next field depend on the entity you select.

    > [!div class="mx-imgBorder"]
    > ![Choose which type of template to create.](media/create-template-type2.png "Choose which type of template to create")

1. The view defines the query used to display records and the columns or fields that are shown.

1. Select **Download File**.

1. You can customize (as detailed in the steps below) and upload the template by selecting **Upload**. To upload the template later, select the **X** icon in the upper right of the modal window.

1. To upload the template after you customize the data, go to the list of templates, and then select **Upload Template**. More information: [Step 3: Upload the template and share with others](#step-3-upload-the-template-and-share-with-others)

## Step 2: Customize the data in Excel

Open the newly created template in Excel to customize the data.

![A newly created Excel template.](media/excel-new-template.png "A newly created Excel template")

Let's walk through a simple example of customizing an Excel template by using Dynamics 365 sample data:

1. Select **Enable Editing** to allow customization of the Excel workbook.

2. Add a new column, and name it "Expected Revenue".

    ![Adding a column to an Excel template.](media/excel-new-column.png "Adding a column to an Excel template")

3. Create a formula for expected revenue. Don't refer to cells by using their addresses; define and use names instead.

    ![Create a formula based on column names.](media/excel-formula.png "Create a formula based on column names")

4. Create a pivot table and chart.

5. Place user-added content above or to the right of the existing data table. This prevents the content from being overwritten if you add new data in Dynamics 365 later and you create a new Excel template. More information: [Best practices and considerations for using Excel templates](#best-practices-and-considerations-for-using-excel-templates)

    ![A customized Excel template.](media/excel-graph.png "A customized Excel template")

6. Save the workbook.

You're now ready to upload the Excel template into Dynamics 365.

## Step 3: Upload the template and share with others

When you have your Excel template customized the way you want, you can upload it into Dynamics 365.

> [!NOTE]
> Users in your organization can see the templates available to them by selecting **Excel Templates** on the command bar in the list of records.

To upload the Excel template into Dynamics 365:

1. Open the **Settings** menu ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") at the top of the page and select **Advanced settings**.

1. Navigate to **Settings** > **Business** > **Templates**.

1. On the next screen, select **Document Templates**, then choose **Upload Template** in the top ribbon.

1. Find and upload the file.

    > [!div class="mx-imgBorder"]
    > ![Upload Template dialog.](media/excel-upload-template2.png "Upload Template dialog")

1. Select **Upload**. You'll see the summary of the file you're uploading.

1. Select the **X** icon in the upper right of the top ribbon to close the information screen.

<a name="best-practices-and-considerations-for-using-excel-templates"></a>

## Best practices and considerations for using Excel templates

Here are some things you need to be aware of to create and make the best use of Excel templates in Dynamics 365:

- **Test your Excel templates**  
  Excel has lots of features. It's a good idea to test your customizations to see that all Excel features work as expected in your templates.
- **Data in templates and privacy concerns**  
  By default, pivot chart data is not updated when a workbook is opened. This can create a security issue if certain pivot chart data should not be seen by users who have insufficient permissions. Consider the following scenario:
  - A Dynamics 365 Customer Insights - Journeys administrator creates a template where the view contains sensitive data in a pivot chart, which is uploaded into Customer Insights - Journeys.
  - A salesperson who should not have access to the sensitive data in the pivot charts uses the template to create an Excel file to do data analysis.

  As a result, the salesperson might be able to see the pivot chart data as uploaded by the Customer Insights - Journeys administrator, including access to views for which the salesperson does not have permissions.
  > [!IMPORTANT]
  > Sensitive data should not be included in pivot tables and pivot charts.
  > 
  > [!NOTE]
  > iOS does not support updating pivot data and pivot charts when using the Microsoft Excel app on iOS devices.
- **Set pivot chart data to automatically refresh**  
  By default, pivot chart data is not automatically refreshed when you open the workbook. Other types of charts are updated automatically. In Excel, right-click the pivot chart, and then select **PivotChart Options** > **Refresh data** when opening the file.
  ![Pivot table options in Excel.](media/excel-pivot-options-ill.png "Set pivot chart data to be automatically refreshed")
- **Placing new data**  
  If you want to add content to the Excel template, place your data above or to the right side of the existing data. A second option is to place your new content on a second sheet.
- **Excel templates with images might cause an error**  

If you attempt to view Customer Insights - Journeys data by using an Excel template that has an image saved in it, you might see the following message: "An error occurred while attempting to save your workbook. As a result, the workbook was not saved." Try removing the image from the template and reloading the template into Customer Insights - Journeys.
- **Excel templates and Office Mobile app in Windows 8.1**  
  Excel templates will not open on Windows 8.1 devices with the Windows 8.1 Mobile app. You'll get the following error message: "We've recovered as much of your document as we could, but you can't edit it. Try to open and repair the document on your PC to fix the problem." This is a known issue.
- **Use table column names and range names in formulas**  
  When you create Excel formulas, don't use column titles or cell numbers. Instead, use the table column names, and define names for cells or cell ranges.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
