---
uid: developers/quick-starts/2_create-own-metric
title: Create your metric
author: ruthaisabokhae
description: Create your own metric
ms.author: ruthai
ms.date: 05/14/2019
ms.service: product-insights
ms.topic: conceptual
---

# Create metrics   

In this article, you will learn how to build metrics from signals in seconds.  Metrics are measurements extracted from signals. Browse the signals that are being sent, select a signal of interest, then drill down to choose a specific property for a meaningful metric. 

For this example, the **vehicle_drive_end** signal is sent after a vehicle completes a trip, and the signal contains the MPGe value for the whole trip. This property determines average MPGe values for different vehicle fuel types.

To find this signal, refer to the previous section, [View signals](1_view-signals). 

1. Select **Explore** at the top right corner of the screen to open the chart editor. 

![Open the chart editor from the signals page](../images/quick-starts/create-metrics-1-vehicle_drive_end.png)

2. Turn off **raw data**. Select **vehicle_drive_end** in the **Signal** menu. 

![Turn off raw data](../images/quick-starts/create-metrics-2-rawdata-off.png)

3. Select **Average** from the **Operation** menu.
4. Select **CurrentMileage** from the **Property** menu. This is what the vehicles reported as their MPGe for each trip. After these steps, you will see the chart showing the average MPGe for all vehicles and all trips.

![Set up your metric](../images/quick-starts/create-metrics-3-vehicle_drive_end-explore.png)

So far this MPG value is for all types of vehicles. To see MPG values for different vehicle fuel types such as electric or gasoline, you need to add splits. 

5. Click **Split** from the top left corner of the chart, and select *VehicleFuelType*

![Add a split](../images/quick-starts/create-metrics-4-add-split.png)

Now you will see multiple lines representing average MPG for each fuel type.

7. Select **Publish** at the top right corner of the chart to publish the metric.  That means this metric (MPG per city type) will appear on the list of metrics and be available to other users. Your colleagues can then comment on the metric and create their own metrics and charts based on your metric.

![Add a split](../images/quick-starts/create-metrics-5-publish.png)

*For electric vehicles, the value is *MPGe - miles per gallon gasoline equivalent

> [!div class="nextstepaction"]
> [Get insights >>](3_get-insights.md)
