---
uid: developers/tutorials/metrics-choose-visualizations
title: Choose visualizations
author: hakrou
description: Choose visualizations
ms.author: hakrou
ms.date: 05/09/2019
ms.service: product-insights
ms.topic: conceptual
---

# Choose visualizations  

Product Insights has many visualization options. By default, data will be displayed in a table. A row represents a single signal. When the Raw data option is turned off, a line chart is typically displayed. 

* Line

See values change over time. Simplest option.

![Visualizations: line](../images/tutorials/Visualizations-Line.png)

* Area - 
Stacked: vehicle_drive_end, Sum operation, CurrentTripDistance

![Visualizations: stacked](../images/tutorials/Visualizations-Stacked.png)

Then add a split on VehicleFuelType 

Switch to %stacked to what percentage of trips each fuel type is. 

![Visualizations: %stacked](../images/tutorials/Visualizations-Stacked100.png)

Good to see how much each segment takes is over time. 

* Column 

Bar charts. To see total breakdown, switch to "all"  

(Continuing from previous example), switch to Column, then change "Five minutes" to All  

Then switch granularity to "hour"  

![Visualizations: column](../images/tutorials/Visualizations-Column.png)

* Pie 

Removes time as a dimension. Good to see distribution.

![Visualizations: pie](../images/tutorials/Visualizations-Pie.png)

* Scatter 

Does not force a trend. Good for a general picture. 

![Visualizations: scatter](../images/tutorials/Visualizations-Scatter.png)

* Table 

Good for seeing raw data. 

![Visualizations: table](../images/tutorials/Visualizations-Table.png)
