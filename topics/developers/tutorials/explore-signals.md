---
uid: developers/tutorials/explore-signals
title: Explore signals
author: ruthaisabokhae
description: Explore signals 
ms.author: ruthai
ms.date: 05/16/2019
ms.service: product-insights
ms.topic: conceptual
---

# Explore signals

You can select the **Explore** button on the **Signals** page
to analyze and discover every aspect of a Product Insights signal.
Product Insights displays a wide variety of data related to the signal, 
as explained below.

* **Properties**: The **Properties** pane lists the various properties of a signal and their values: key/value pairs sent inside the signal.
  For example, the **vehicle_drive_end** signal might list the **CurrentMileage** and
  **CurrentLocalDrivingConditions** properties, among many others.
  Each property is associated with a **Type**, and **First seen** and **Last seen** values.
* **Type**: The type of a property represents the kind of information it contains (either **Number** (double), **String**, or an enumerated type).
  For example, **CurrentMileage** has **Number** for a type, and **VehicleModel** is a **String**.
* **First seen** and **Last seen** contain the first and last date and time the property was noticed in the signal and assigned a value.
  For example, the last time **CurrentMileage** was calculated was probably during the last time the vehicle was driven.
* Charts: The **Signal volume** graph describes how many signals reached Product Insights over a period of time.
* The **Suggested Charts** pane displays what the system suggests may be meaningful metrics.