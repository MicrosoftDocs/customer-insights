---
title: Engagement insights availability regions
description: Learn more about the regions and geos that engagement insights is deployed.
author: mkisel11
ms.reviewer: mhart
ms.author: mkisel
ms.date: 07/15/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: article
ms.manager: shellyha
---

# Regional availability for engagement insights

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Engagement insights, a capability of Dynamics 365 Customer Insights gradually introduces additional regions where customers can choose to store their data. Administrators can choose a region when they [create a new environment](manage-environments-workspaces.md#create-an-environment). If an organization is sets up engagement insights for the very first time, they choose the region while going through the [guided first-run experience](quickstart.md). Subsequently, every new environment allows choosing the designated region the data will be stored in.

During public preview, there are 2 geographies: USA and Europe. Users can choose between the West US region and the North Europe region.

An organization can maintain environments in different regions. For example, Environment A stores data in West US and Environment B in North Europe.

> [!TIP]
> After choosing a region during environment creation, you won't be able to change that setting. To change the region, an environment admin has to [delete the environment](manage-environments-workspaces.md#delete-an-environment) and create a new environment with the updated region setting.

