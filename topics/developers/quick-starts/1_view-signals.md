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

Signals are data sent to Project Insights from remote applications. You can find and explore a continuous flow of data from a variety of sources, such as products, websites, and mobile applications.    

You can send signals using a variety of ways:  

1. Create a team using the instructions found [here](create-a-team.md).
1. Using Product Insights [SDKs](../dev-resources/index.md).  
1. Exploring our [samples](explore-samples.md).  
1. Simulating sample signals for test purposes (follow instructions below).  


## Simulate sample signals

Watch to learn how to simulate signals. 

>[!VIDEO https://youtube.com/embed/nZc5a8uNE-8]


### Add a signal

1. Select a team from the left pane of the Home screen, such as **Smart Dishwashers**.

1. Select a project from the team screen, such as **2000 Series**.

1. Select the **Add New Signal** button from the project screen. The **Add Signals** window will appear.

1. Select **Define a Signal."

1. Select **Add** button. The signal will now appear on the list.

1. Enter a name for the new signal into the **Display name** field (in this case, **Sample Signal**). Enter any text into **Description**. 

1. Select the new signal. The **Signals** screen will appear.

### Add properties

1. Select the **Add Property** button, and the **Add Property** window will appear. 

1. Enter values for the **DetergentConsumption** field of the property, and select a value type from the **Expected type** drop-down menu, such as **Number**. Select **Add** when you're ready to proceed. 

1. Repeat the previous step for as many properties as you wish to add, such as **Firmware**, **Model**, and **WaterConsumptiom**.

### Generate a sample signal

1. Select the **Simulate** button. The **Generate test data** window will appear.

2. Enter sample values for each of the properties, with a **variation range** for each.

|Property|Example value|Variation range|
|--------|-------------|---------------|
|Model|V30, V40, V50, V60|
|Firmware|F1, F2, F3|
|DetergentConsumption|100|25%|
|WaterConsumption|8000|35%|


3. Click **Start** to generate data for the sample signal.
