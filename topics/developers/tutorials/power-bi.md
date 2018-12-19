---
layout: page
title: Power BI integration


---

Aria is a telemetry platform that captures events in real time. Although it provides some visualizations, their number is somewhat limited. On the other hand, the Power BI application offers a broad set of visualizations that you can choose from and customize as you wish. If you're a Power BI user looking for a real-time service that captures your telemetry and provides intelligent insights, you can use Aria's services and still export your data to Power BI with the data connector.

## Quickstart

1. Download the [Aria-PowerBI](https://ariamediahost.blob.core.windows.net/media/PowerBI/Aria-PowerBI.zip) zip file.

1. Unzip (extract) the `Power BI Desktop` folder from the zip file.

1. Move the `Power BI Desktop` folder to your `Documents` folder.
> **Note:** If you previously had a `Power BI Desktop` folder in your `Documents` folder, rename the old folder and make sure the new folder is named `Power BI Desktop`.

1. Start the Power BI Desktop application and Enable the **Custom data connectors** preview feature in Power BI Desktop under **File** > **Options and settings**.
> **Note:** If you get an **Uncertified connectors** dialog when you open Power BI Desktop, please refer to the **Uncertified connectors** section below.
{% img "how-to/power-bi/PreviewFeature.png" alt:"Preview feature" class:"img-responsive" %}

1. Restart the Power BI Desktop application.

## Connect to a project's cubes

> **Note**: In this section, you must have the Aria connector installed. If you don't have it installed, please refer to the **Quickstart** section above.

1. Select **Get data** from the **Getting started** dialog, or from the **Home** ribbon tab, and then select **More...**

1. You can find the data connector by searching for **Aria** in the search box or in the **Online services** group. Double-click it.
{% img "how-to/power-bi/GetData.png" alt:"Get data" class:"img-responsive" %}
 
1. A dialog appears to alert you that the connector is still under development. 
{% img "how-to/power-bi/ThirdPartyWarning.png" alt:"Third-party warning" class:"img-responsive" %}
    
1. Select  **Continue**. The  **Aria**  dialog box appears.

1. Copy your **Project ID** and paste it into the corresponding box. Select an **Interval** and **Granularity** from the drop-down menu. These fields are optional.
> **Note**: The granularity **must be less than or equal to the interval**.
{% img "how-to/power-bi/AriaDialog.png" alt:"Aria Dialog" class:"img-responsive" %}

1. Confirm that the cubes and dashboards from the project are working properly in the ARIA portal.

1. When prompted for credentials, sign into your Microsoft account, and allow Power BI to access your account. After you sign in, click **Connect**.
{% img "how-to/power-bi/Authentication.png" alt:"Authentication" class:"img-responsive" %}

1. Select the cubes and measures from which you would like to import data by clicking their checkboxes.
> **Note**: When you select a cube's measure table, **all of its data** will be imported, including every dimension and operation for that specific measure.
{% img "how-to/power-bi/Navigation.png" alt:"Navigator" class:"img-responsive" %}

1. Click **Load** to import your existing data into your Power BI project or **Edit** if you want to make changes to the data or metadata.

1. Now you can use your data to make visualizations in Power BI!

## Export dashboard data from Aria to Power BI

> **Note**: In this section, you must have the Aria connector installed. If you don't have it installed, please refer to the **Quickstart** section above.

1. Open the Aria dashboard.

1. Click **Build Power BI query** on the dashboard toolbar.
{% img "how-to/power-bi/Dashboard.png" alt:"Dashboard button" class:"img-responsive" %}

1. Select the layer you want to export from the dashboard's drop-down menu.
{% img "how-to/power-bi/LayerDropDown.png" alt:"Layer drop-down" class:"img-responsive" %}

1. A query similar to the following one will be copied to the clipboard.
    `=AriaDataConnector.GetCubeCSV("https://api.int.aria.ms/v4/tenants/29752ff24d7347dc97fbcee272d5de91/providers/Rta/cubes/8f13114a71984b96bb94a489159ecbf1/measures/Duration/series", "{""filters"":[{""dimension"":""Manufacturer"",""operation"":""in"",""values"":[""Apple"",""Google"",""Microsoft"",""Samsung""],""action"":""separate""}],""segments"":[],""transforms"":[{""type"":""anomalies"",""sensitivityIndex"":0.5}],""interval"":""2018-07-10T21:25:00Z/2018-07-10T22:30:00Z"",""granularity"":""PT5M"",""operations"":[""Average""]}")`

1. Open the Power BI Desktop application and select **Get data** from the **Getting started** dialog, or select **Blank query** from the **Home** ribbon tab.
{% img "how-to/power-bi/BlankQueryHome.png" alt:"Blank query" class:"img-responsive" %}

1. If you selected **Get data**, click either **All** or **Other** and then enter `blank query` in the search box. Double-click **Blank Query** in the right-hand pane. 
{% img "how-to/power-bi/GetDataBlankQuery.png" alt:"Blank query" class:"img-responsive" %}

1. Paste the query into the formula bar.
{% img "how-to/power-bi/FormulaBar.png" alt:"Formula bar" class:"img-responsive" %}

1. Click **Edit Credentials**, and then click **Sign in as a different user**. Enter your Microsoft credentials.
{% img "how-to/power-bi/Credentials.png" alt:"Edit credentials" class:"img-responsive" %}

1. Click **Connect**. The data will be imported as a table.
{% img "how-to/power-bi/SignIn.png" alt:"Sign in" class:"img-responsive" %}

1. The data type of the imported columns may not be the desired one. To adjust the data type, click the **ABC** icon next to the column title, or select **Detect Data Type** on the **Transform** tab.
{% img "how-to/power-bi/DataType.png" alt:"Data type" class:"img-responsive" %}

## Uncertified connectors

1. The following dialog box should appear. Click the **OK** button.
{% img "how-to/power-bi/UncertifiedConnectors.png" alt:"Uncertified" class:"img-responsive" %}

1. Enable the **Allow any extension** option under **File > Options and settings > Security > Data extensions**. 
{% img "how-to/power-bi/Options.png" alt:"Options" class:"img-responsive" %}

1. Return to the **Quickstart** section above or **Restart** the Power BI Desktop application.

## Questions

If you have any questions about Power BI, please refer to the [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/). 

If you have any questions or problems with the Aria Power BI Data Connector, please email [ariasupport@services.microsoft.com](mailto:ariasupport@services.microsoft.com).




