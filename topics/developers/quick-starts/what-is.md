---
uid: developers/quick-starts/what-is
title: One minute introduction to Product Insights
author: hakrou
description: One minute introduction to Product Insights
ms.author: hakrou
ms.date: 04/24/2019
ms.service: product-insights
ms.topic: conceptual
---

# <a id="what_is"></a>Quickstart: setup to insights in five minutes 

This quickstart explains how to sign up with the Product Insights portal, create a sample organization and team, add members, generate and view sample signals, and configure dashboards for charts. 

## Product Insights overview

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RE2RZnI]

## Sign up for a Product Insights preview

Sign into Product Insights at [https://pi.dynamics.com](https://pi.dynamics.com). You may need to use an incognito window (Ctrl+Shift+N).
> [!NOTE]
> - An AAD (Azure Active Directory) account is required for the Product Insights preview. Contact [Jeff Hardie](email:jefhar@microsoft.com) to enable a preview for your AAD.
> - The Product Insights team may also provide a sample AAD account. Contact [Jeff Hardie](email:jefhar@microsoft.com) to request yours.
> - Previews are not available to MSA accounts (example: [sample@outlook.com](email:sample@outlook.com)) at this time.

## Create a team
1. Select **Create a team** in the center welcome tile, or **+New team** in the bottom left corner of the portal.
1. Type *Test_Team* in the **Name** field and text for **Description**. Select **Create** to commit the update.

	![Create a new team](../images/quick-starts/create-a-team.png)
  
## Add members
1. Select *Test_Team* from the left menu.  
1. Select **Members** and then **+Add Members** in the center pane.
1. Enter email addresses from your AAD for any new members you would like to have access, and then select **Role** under **Owner**. Select **Add** to commit the update.

	![Add new members](../images/quick-starts/add-members.png)

## Create a project 
1. Select **Projects** and then **+New project** in the center pane. 
1. Type *SampleProject* for TK and any other text for **Description**.  Select **Create** to commit the update.

	![Add new project](../images/quick-starts/add-project.png)
  
## Create data
Generate a new signal for the sample project by defining a schema with this tool.

### Define signal 
1. Select *SampleProject* from the center pane. 
1. Select **+Define a Signal**, and then type *SampleSignal* for TK and any other text for **Description**.  Select **Add** to commit the update.
1. Select *SampleSignal*, and then select **+Add** for each of the following properties:

|Display name | Expected type|
|-------------|--------------|
|command|String| 
|speed|Number  |
|model|String  |

4. Select **Save** on the top right of the toolbar.

### Generate data 
1. Select **Generate** on the top right of the toolbar, and then select **+Add** for each of the following properties:

|Property|Example value|Variation range|
|--------|-------------|---------------|
|command|start,stop|
|speed|100|40%|
|model|mazda, acura, bmw|

2. Select **Start** to begin generating data.

## Preview signals

1. Select **Explore** on the top right of the toolbar.  You will see the sample data you generated.
1. Toggle **Raw data** to view the data as a chart and begin exploring it. 

   ![Preview new signals](../images/quick-starts/preview-signal.png)
 
## Publish your metric to a dashboard

1. Select **Publish to new dashboard** on the top right of the toolbar. Leave the default name, and select **Publish** to commit the update.

![Create a dashboard](../images/quick-starts/create-a-dashboard.png)


> [!div class="nextstepaction"]
> [Next >>](who-uses.md)

