---
uid: developers/tutorials/metrics-drill-down-to-instance
title: Drill down to instance level 
author: hakrou
description: Drill down to instance level 
ms.author: hakrou
ms.date: 05/09/2019
ms.service: product-insights
ms.topic: conceptual
---

# Drill down to instance level 

Using filters or splits, you can drill down to a single vehicle. 

Continuing from the [Fabrikam Go example](metrics-create-metrics), select filter from the Explore screen. Select the VIN property from the property dropdown. You should see Filter dialog box added in the Data pane. 

Click the pencil icon to edit filter properties. Select "is equal to", then enter a VIN value such as 3896R0REU0PGPLAW8. You should now only see results for the specific vehicle. 

Select the average operation from the Measure dropdown, and select the CurrentMileage property. This should give you the average MPG for the car. If you do not see any data, you can change the time window to search for more values sent from this car. 


