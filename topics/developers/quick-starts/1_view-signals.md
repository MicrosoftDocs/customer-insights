---
uid: developers/quick-starts/1_view-signals
title: View signals
author: ruthaisabokhae
description: View signals
ms.author: ruthai
ms.date: 09/30/2019
ms.service: product-insights
ms.topic: conceptual
layout: LandingPage
---

# Send signals 

Signals are data sent to Project Insights from remote applications. You can find and explore a continuous flow of data from a variety of sources such as products, websites, and mobile applications.    

You can send signals using a variety of ways:  

1. Using Product Insights [SDKs](https://review.docs.microsoft.com/en-us/dynamics365/product-insights/developers/dev-resources/?branch=master).  
2. Exploring our [samples](www.microsoft.com).  
3. Simulating sample signals for test purposes (follow instructions below).  


## Simulate sample signals
Watch this video to learn how to similate signals.  

>[!VIDEO https://youtube.com/embed/8oehlTygiEk]  


### Add a signal

1. Select a team from the left pane of the Home screen, such as **insert name**.

1. Select a project from the team screen, such as **insert name**.

1. Select the **Define a Signal** button from the project screen. The **Add new** signal window will appear.

1. Enter a name for the new signal into the Display name field (in this case, **insert name**). Enter any text into **Description**. The **Display name** field will fill automatically.

1. Select the new signal. The Signals screen will appear.

### Add properties

1. Select the **Add** button in the Properties pane. The **Add new** properties window will appear.

1. Enter values for the **Display name** field of the property, and select a value from
the **Expected type** drop-down menu such as **String**. Select **Add** when you're ready to proceed.

1. Repeat the previous step for as many properties as you wish to add, such as **insert name**, **insert name**, and **insert name**.

### Generate a sample signal

1. Select the **Generate** button. The **Generate test data** window will appear.

2. Enter sample values for each of the properties, with an optional **variation range** for each.

|Property|Example value|Variation range|
|--------|-------------|---------------|
|command|start,stop|
|speed|100|40%|
|model|GEM, ATV, GoKart|

3. Click **Start** to generate data for the sample signal.
