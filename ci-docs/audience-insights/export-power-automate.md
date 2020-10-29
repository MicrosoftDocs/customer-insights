---
title: "Power Automate connector | Microsoft Docs"
description: "Create flows in Microsoft Power Automate from Dynamics 365 Customer Insights."
ms.date: 08/03/2020
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: philk
manager: shellyha
---

# Power Automate connector (preview)

Trigger specific events to occur automatically when your data changes and manage more complex flows directly in [Power Automate](https://flow.microsoft.com/).

## Power Automate triggers

You can use a variety of triggers that allow you to create flows to automate repetitive tasks, such as notifications or more advanced actions. 

- Trigger when a data source refresh fails. 
- Trigger when a data source refresh succeeds.
- Trigger when a threshold is crossed on a segment. The trigger is limited to crossing above the threshold.
- Trigger when a threshold is crossed on a business measure. The trigger is limited crossing above the threshold.
- Trigger when a full refresh of (data sources, segments, measures,...) is completed.
- Trigger when a refresh of the unification process (map, match, merge) is completed.

[Configure your triggers in Power Automate](https://flow.microsoft.com/connectors/shared_customerinsights/dynamics-365-customer-insights-connector/).

## Power Automate actions
The Power Automate connector provides other actions than the available triggers. For more information, see the [Dynamics 365 Customer Insights Connector](https://docs.microsoft.com/connectors/customerinsights/).

## Create a Power Automate flow in audience insights

1. In audience insights, go to **Admin** > **System**.

1. On the **System** page, select the **Status** tab.

1. In the **Data Sources** section, select **Flows** and select **Create a flow** from the dropdown list.
   > [!div class="mx-imgBorder"]
   > ![Power Automate connector showing Create a Flow action](media/power-automate-connector-create-flow.png "Power Automate connector showing Create a Flow action")

1. In Power Automate, select one of the available triggers to create your preferred flow. If you're creating your first flow, you'll need to authenticate with the Power Automate connector first.
