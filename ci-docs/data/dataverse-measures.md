---
title: Use calculated measures in Dataverse-based applications
description: Write one-dimensional measures to separate tables in Dataverse to use them in other applications.
ms.date: 02/27/2024
ms.topic: how-to
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: mhart
ms.custom: bap-template
---

# Use calculated measures in Customer Insights - Journeys and other Dataverse-based applications

Dynamics 365 Customer Insights lets you create highly personalized experiences for your customers by [using the unified profile of your customers in journeys](marketing-get-started.md). You can further augment these experiences with [customer measures](measures.md) to tailor journeys, deliver personalized offers, and content based on loyalty points, lifetime value, and other calculated measures. Further, you can use simple measures in Power Apps built on top of Microsoft Dataverse.

## Limitation

- Up to 10 million rows in a calculated measure. For more than 10 million rows, break up the measure into multiple parts.

## Create a calculated measure table

To create measures that the system stores as tables in Dataverse, ensure you meet these prerequisites:

- Use only one dimension for the measure. The dimension is *CustomerInsights.CustomerId* from the *Customer* table.
- Provide meaningful names for both your measure and the calculation. It helps to easily identify the table in Customer Insights - Journeys or in apps built with Power Apps.

1. [Create a new measure](measure-builder.md) with the **Build your own** option.
1. Set **Measure Type** to **Customer** and **Table**. Business measures don't support Dataverse tables.
   :::image type="content" source="media/measures-table-setting.svg" alt-text="Settings for a calculated measure that writes to a Dataverse table.":::
1. Run the measure and wait until it refreshed.

   To check the status, go to **Settings** > **System** and review the **Measures** and **Measures in Dataverse** sections. Depending on the number of customers and the data size that the measure is aggregated against, the process can take several minutes.

The system writes the measure to a Dataverse table with a relationship to the customer profile in the *Customer* table. You can now use the newly created measure table for customer journey orchestration or personalization in Customer Insights - Journeys or for forms or views in Power Apps.

> [!NOTE]
> If you're using the [Customer Card add-in](customer-card-add-in.md) and want a measure to show up there, continue to build measures of type Customer and Attribute.
> :::image type="content" source="media/measure-customer-attribute.svg" alt-text="Measure settings for a customer attribute that is used in the Customer Card add-in.":::

## Sample scenarios

The following list contains some inspiration for one-dimensional customer measures and how to use them in a customer journey:

- Use customer measures that measure metrics like lifetime spend in [journeys as a branch condition](../journeys/real-time-marketing-tile-reference.md#branching-the-customer-journey). For example: If the lifetime spend is greater than $ 500, route customers directly to tier 1 support.
- [Personalize email content](../journeys/real-time-marketing-personalization.md) based on lifetime spend. For example, email a discount offer based on an amount they spent.
- [Create a segment of contacts in Customer Insights - Journeys](../journeys/real-time-marketing-build-segments.md) based on the lifetime spend.
- Use the measure for a [form in Power Apps](/power-apps/maker/model-driven-apps/create-design-forms). For example: Create a page for your customer support team so they can see the lifetime spend of a customer when looking up customer details.

[!INCLUDE [footer-banner](includes/footer-banner.md)]
