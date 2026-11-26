---
title: Create segments using unified profiles and customer measures from Customer Insights - Data
description: Learn how to create segments using unified profiles and customer measures in Customer Insights - Journeys to personalize contact targeting. Get started.
ms.date: 11/09/2026
ms.topic: article
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: sfi-image-nochange
---

# Create segments using unified profiles and customer measures from Customer Insights - Data

Customer Insights - Journeys lets you create highly personalized segments based on customers' unified profiles and customer measures from Customer Insights - Data. You can use these segments directly in Customer Insights - Journeys without having to use the Customer Insights - Data app to create unified profile-based segments. This approach ensures that all interaction data is captured against the contact, irrespective of whether you use the information from contacts or unified profiles.

When a Customer Insights - Journeys environment is [connected to](customer-insights-quickstart-guide.md) a Customer Insights - Data environment, unified profiles and customer measures are available when you create a segment of contacts. For example, you could create a segment of contacts called "Monthly grocery shoppers" that is based on location information from the contact table, the “Rewards member” property from unified profiles, and “MonthlyTotalSpend” from a customer measure (the latter two coming from Customer Insights - Data).

> [!IMPORTANT]
> Following the January 2025 release, this option only appears in Customer Insights - Journeys applications where CustomerId backstamping (COLA stamping) with Customer Insights - Data has been successfully set up and executed.

:::image type="content" source="media/unified-profile-segment-creation.png" alt-text="Screenshot of unified profile segment creation.":::

## Create customer measures

To learn how to create measures in Customer Insights – Data and what types of measures are available for use in Customer Insights - Journeys, see [Use calculated measures in Dataverse-based applications](../data/dataverse-measures.md).

> [!NOTE]
> While the user interface presents itself as a one-to-many relationship, the current implementation in Customer Insights – Data only allows single-dimension metrics. Therefore, there is always only one value returned.
