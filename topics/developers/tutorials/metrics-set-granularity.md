---
uid: developers/tutorials/metrics-set-granularity
title: Set time granularity
author: hakrou
description: Set time granularity
ms.author: hakrou
ms.date: 05/09/2019
ms.service: product-insights
ms.topic: conceptual
---

# Set granularity 

Data on a chart is usually bound by time. For example, if you request the last 24 hours of data, grouped by hour, you will see 24 values graphed on a chart. 

You can change the date range and granularity. Granularity specifies how to group data. If you use a granularity of five minutes,  the data will be more detailed. If you use hourly or daily granularity, it will be easier to see trends, but you will probably lose details. 

![Sample chart for five minutes / one hour](../images/tutorials/Visualizations-Granularity.png)

Depending on your time range, granularity might chosen for you automatically for performance's sake. For example, if you want last week's data, default granularity is one hour and smaller granularities such as one and five minutes may be unavailable. 

![Sample chart for one week with granularity dropdown menu](../images/tutorials/Visualizations-GranularityScaleDown.png)
