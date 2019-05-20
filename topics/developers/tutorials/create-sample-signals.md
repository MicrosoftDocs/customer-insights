---
uid: developers/tutorials/create-sample-signals
title: Create sample signals
author: hakrou
description: Create sample signals
ms.author: hakrou
ms.date: 05/16/2019
ms.service: product-insights
ms.topic: conceptual
---

# Create sample signals

You may find it useful to generate sample signals and data for test purposes.
Creating sample signals is a simple procedure with Product Insights.

On the **Home** screen, select a team from the pane on the left, such as "Autopilot".

From the team screen, select a project, such as "Command".

On the project screen, select the **Define a Signal** button.

The **Add new signal** window will appear. The **Display name** and **Actual name** fields
for the signal will be filled automatically. You can fill the **Description** field with
a description of the new signal.

Select the new signal, in this case "Autopilot command". The **Signals** screen for the new
signal will appear.

Click the **Add** button in the **Properties** pane.

The **Add new properties** window will appear.
Enter values for the **Display name** and **Actual name** fields for the property, and select a value from
the **Expected type** drop-down menu such as "string". Click **Add** when you are ready to proceed.

Repeat the previous step for as many properties as you would like to add, such as 
"command", "model", and "speed".

Select the **Generate** button in the upper right corner.

The **Generate test data** window will appear.
Enter example values for each of the properties, with 
an optional variation range for each.
For example, for the property name "command", you might enter
"Start, Stop, Help", and for the property name "speed", you might enter 100,
with a variation range of 40%.
You might assign the "model" property the values "GEM, ATV, GoKart".

Click **Start** when you are ready to generate data for the sample signal.