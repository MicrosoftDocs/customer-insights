---
title: "Power Automate connector (preview) | Microsoft Docs"
description: "Create flows in Microsoft Power Automate from Dynamics 365 Customer Insights."
ms.date: 07/25/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: pkieffer
ms.author: philk
manager: shellyha
---

# Power Automate connector (preview)

Trigger specific events to occur automatically when your data changes and manage more complex flows directly in [Microsoft Power Automate](https://flow.microsoft.com/).

## Known limitations

- A maximum of 100 calls per 60 seconds. Use the [$skip parameter](/connectors/customerinsights/#get-items-from-an-entity) to call the API endpoint multiple times.

## Power Automate triggers

Use triggers to create cloud flows and automate repetitive tasks, such as notifications or more advanced actions. Use triggers when:

- A data source refresh fails.
- A data source refresh succeeds.
- A threshold is crossed on a segment. The trigger is limited to crossing above the threshold.
- A threshold is crossed on a business measure. Only business measures without a dimension are supported. The trigger is limited to crossing above the threshold.
- A full scheduled refresh is completed. This trigger doesn't work for manually started refreshes.
- A refresh of the unification process is completed.

[Configure your triggers in Power Automate.](https://flow.microsoft.com/connectors/shared_customerinsights/dynamics-365-customer-insights-connector/)

## Power Automate actions

The Power Automate connector provides other actions than the available triggers. For more information, see the [Dynamics 365 Customer Insights Connector](/connectors/customerinsights/).

## Create a Power Automate flow

1. Go to **Settings** > **Connections**.

1. On the **Power Automate** tile, select **Set up**.

1. The Customer Insights Connector (preview) in Power Automate opens. **Sign in** to Power Automate.

1. Choose one of the available triggers and add more steps to your new flow. For more information, see [Create a cloud flow in Power Automate](/power-automate/get-started-logic-flow).

Examples of how to use flows: 
- Post a message to a Microsoft Teams channel if a data source refresh fails. 
- Send an email to the data owners when a threshold on a segment is crossed.

[!INCLUDE [footer-include](includes/footer-banner.md)]
