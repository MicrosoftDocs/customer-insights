---
uid: developers/tutorials/metrics-create-metrics
title: Create metrics 
author: hakrou
description: Create metrics 
ms.author: hakrou
ms.date: 05/09/2019
ms.service: product-insights
ms.topic: conceptual
---
# Create metrics 

You can create metrics based on the signals you are receiving. Select a signal from one of your projects, then click Explore to define metrics. 

In the [sample project](https://pi.dynamics.com/teams/fe359446d26a4e4eb094e9c5fbe89f21/projects/dc7e179315a441f285d5fe77993bd72c/signals), select the vehicle_drive_end signal. You should see a list of signals coming through. Click Explore on the top right corner. 

Based on the signal you have selected, below are sample metrics you could create: 

- Total number of drives completed. To get this metric, simply select Signal count operation. 
- To see the total number of unique cars, select distinct count, then select the VIN property. This will give you a distinct count of VIN numbers presented in the incoming vehicle_drive_end signals. 
- To see average MPG for all completed drives, select the average operation, then choose the CurrentMileage property which represents MPG value for completed drives. Product Insights collects all CurrentMileage data reported, then works out the average value. 

For detailed instructions, see below. 

1. To create a metric, first verify that the **Project** and the **Signal** are correct. 
1. Decide which operation to use. Do you simply want a count of signals sent in? Do you want an average of some numeric value such as MPG? 
1. If you want 'average', specify which property is to be used. In this example, you can use CurrentMileage property. 



