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

Product Insights has many visualization options. By default, data will be displayed in a table with a row representing a single signal. When the raw data option is turned off, a line chart is typically displayed. 

* Line

Line charts display data as a series of points connected by straight lines. They are useful to visualize data over time (usually represented by the x axis). Line charts are the simplest option.

![Visualizations: line](../images/tutorials/Visualizations-Line.png)

* Area

Area charts are graphs based on line charts, with highlighted areas beneath the lines. Area charts are usually intended to compare the quantities they represent.

Stacked area charts represent cumulative totals over time, with greater values arranged above lesser ones, and each value in the stack of values highlighted or colored in a different way.

TK: Stacked: vehicle_drive_end, Sum operation, CurrentTripDistance

![Visualizations: stacked](../images/tutorials/Visualizations-Stacked.png)

Then add a split on VehicleFuelType

%Stacked area charts represent percentage values as proportions of the entire stack of values at a specific point in time. They are useful to understand how much of the whole each segment takes over time.

**Example**: Switch to %stacked area charts to learn what percentage of trips each fuel type contributes.

![Visualizations: %stacked](../images/tutorials/Visualizations-Stacked100.png)

* Column 

Column charts or bar charts show data in different categories with values represented by their heights or lengths. For example, the x axis of a bar chart might represent various models of automobile, with the y axis representing their MPGe values.

TK: Bar charts. To see a total breakdown by fuel type, switch to **All**.

**Example**: Continuing from the previous example, switch the chart type to **Column**, then change "Five minutes" to **All**, and **Granularity** to "hour".

![Visualizations: column](../images/tutorials/Visualizations-Column.png)

* Pie

Pie charts are circular graphs divided into slices like a pie. The area of each slice is proportional to the fraction represented of the total. Time is not represented as one of the dimensions of the graph. Pie charts are useful to see the distribution of various elements.

![Visualizations: pie](../images/tutorials/Visualizations-Pie.png)

* Scatter 

Scatter charts graph data sets as collections of points with one variable along the x axis and another along the y axis. They are good for obtaining a general picture, because they do not force a trend on the data. 

![Visualizations: scatter](../images/tutorials/Visualizations-Scatter.png)

* Table 

Tables are collections of data arranged into columns and rows. They are useful for understanding raw data. 

![Visualizations: table](../images/tutorials/Visualizations-Table.png)
