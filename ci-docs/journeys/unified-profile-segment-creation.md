---
title: Create segments using unified profiles and customer measures from Customer Insights - Data
description: Learn how to create segments using unified profiles and customer measures from Customer Insights - Data in Dynamics 365 Customer Insights - Journeys.
ms.date: 01/30/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create segments using unified profiles and customer measures from Customer Insights - Data

Customer Insights - Journeys lets you create highly personalized segments based on customers' unified profiles and customer measures from Customer Insights - Data. You can use these segments directly in Customer Insights - Journeys without having to use the Customer Insights - Data app to create unified profile-based segments. This ensures that all interaction data is captured against the contact, irrespective of whether you use the information from contacts or unified profiles.

When a Customer Insights - Journeys environment is [connected to](customer-insights-quickstart-guide.md) a Customer Insights - Data environment, unified profiles and customer measures are available when you create a segment of contacts. For example, you could create a segment of contacts called “Monthly grocery shoppers” that's based on location information from the contact table, the “Rewards member” property from unified profiles, and “MonthlyTotalSpend” from a customer measure (the latter two coming from Customer Insights - Data)

> [NOTE]
With Jan-2025 release, this option will only appear in CI-J applications where CustomerId backstamping (COLA stamping) with CI-D has been successfully set up and executed.

:::image type="content" source="media/unified-profile-segment-creation.png" alt-text="Screenshot showing unified profile segment creation." lightbox="media/unified-profile-segment-creation.png":::

## Creating measures

To learn how to create measures in Customer Insights – Data and what types of measures are available for use in Customer Insights - Journeys, see [Use calculated measures in Dataverse-based applications](../data/dataverse-measures.md).

> [!NOTE]
> While the user interface presents itself as one-to-many relationship, the current implementation in Customer Insights – Data only allows single dimension metrics, therefore, there will always be only one value returned. 
