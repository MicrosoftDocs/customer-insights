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

You can drill down to a single vehicle with filters and splits. 

Continuing from the [Fabrikam Go example](metrics-create-metrics), select **Filter** from the **Explore** screen. Select the **VIN** property from the **Property** menu. You should now see the **Filter** dialog box in the **Data** pane. 

Click the pencil icon to edit filter properties. Select **is equal to**, and then enter a VIN value such as 3896R0REU0PGPLAW8. You should now only see results for that specific vehicle. 

Select the **average** operation from the **Measure** menu, and then select the **CurrentMileage** property. This will show the average MPGe for the car. If you do not see any data, you can change the time window to search for more values sent from this car. 


