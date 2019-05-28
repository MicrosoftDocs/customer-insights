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

A signal is data sent to Project Insights from a remote application or applications.
You may find it useful to generate sample signals and data for test purposes.

> [!VIDEO https://ariamediahost.blob.core.windows.net/media/videos/ProductInsights/CreateSampleSignals.mp4]

## Add a signal

1. Select a team from the left pane of the **Home** screen, such as "Autopilot".

1. Select a project from the team screen, such as "Command".

1. Select the **Define a Signal** button from the project screen. The **Add new signal** window will appear.

1. Fill the **Description** field with a description of the new signal. The **Display name** and **Actual name** fields
will fill automatically.

1. Select the new signal, in this case "Autopilot command". The **Signals** screen for the new
signal will appear.

## Add properties

1. Click the **Add** button in the **Properties** pane. The **Add new properties** window will appear.

1. Enter values for the **Display name** and **Actual name** fields of the property, and select a value from
the **Expected type** drop-down menu such as "string". Select **Add** when you are ready to proceed.

1. Repeat the previous step for as many properties as you wish to add, such as "command", "model", and "speed".

## Generate a sample signal

1. Select the **Generate** button. The **Generate test data** window will appear.

1. Enter example values for each of the properties, with an optional variation range for each.

|Property|Example value|Variation range|
|--------|-------------|---------------|
|command|start,stop|
|speed|100|40%|
|model|GEM, ATV, GoKart|

1. Click **Start** to generate data for the sample signal.
