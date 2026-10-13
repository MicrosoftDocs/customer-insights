---
title: Personalize triggers using conditions
description: Learn how to personalize triggers using attributes from tables one hop away in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/13/2026
ms.topic: article
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Personalize triggers using conditions

You can deliver more personalized experiences by accessing a rich set of trigger data for defining the journey entry/exit criteria, conditions/branches, and wait for branches. When you add any of these elements to the journey, you can use data attributes not only from the trigger’s core entity/table, but also from entities/tables directly related to those attributes.

For example, let’s create a journey to nurture new opportunities (using the “Opportunity created” trigger).

In the **Choose a trigger** dialogue, select the **Opportunity created** trigger.

:::image type="content" source="media/real-time-marketing-tile-choose-trigger.png" alt-text="Choose a trigger screenshot.":::

Then, select **+Add condition** and search for the **budget** attribute from the Opportunity table.

:::image type="content" source="media/real-time-marketing-tile-budget.png" alt-text="Select the budget attribute.":::

This enables you to create [journey variations](real-time-marketing-edit-journey.md) for opportunities that are more likely to buy.

:::image type="content" source="media/real-time-marketing-tile-will-buy.png" alt-text="Create a variation based on the attribute.":::
