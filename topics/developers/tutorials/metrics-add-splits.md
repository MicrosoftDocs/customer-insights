---
uid: developers/tutorials/metrics-add-splits
title: Add splits to your metric 
author: hakrou
description: Add splits to your metric 
ms.author: hakrou
ms.date: 05/09/2019
ms.service: product-insights
ms.topic: conceptual
---
# Add splits to your metric 

Splitting a metric enables breaking it down into reported categories. For example, you can add the following split operations to [the metrics previously established](metrics-create-metrics): 

- Add a split to the "total number of drives completed metric" by selecting **Split** and then **VehicleType**. Now you can see the total number of drives for every vehicle type such as SUV, Sports, Minivan, and Sedan. 

    ![Total no of drives completed by vehicletype](../images/tutorials/add-split-vehicletype.png)

- Add a split to the "distinct count of VINs" metric by selecting **Split** and then **CityType**. Now you can see the total number of unique vehicles reporting in, divided into the types of their locations. 

    ![Total no of unique cars by city type](../images/tutorials/add-split-citytype.png)

- Add a split to the average MPGe metric by selecting **VehicleFuelType**. Now you can see average MPGe values for gas, electric, and hybrid vehicles.

    ![Avg MPGe for all completed drives by vehicle fuel type](../images/tutorials/add-split-vehiclefueltype.png)
