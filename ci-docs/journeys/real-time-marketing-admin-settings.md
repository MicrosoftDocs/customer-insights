---
title: Customer Insights - Journeys administrator settings
description: Learn about administrator settings required for Dynamics 365 Customer Insights - Journeys.
ms.date: 08/05/2025
ms.topic: article
author: alfergus
ms.author: alfergus
ms.reviewer: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customer Insights - Journeys administrator settings

This article describes administrator settings required for Customer Insights - Journeys features.

## Journeys

Customer Insights - Journeys utilizes a Power Automate connector to publish journeys. To ensure Customer Insights - Journeys's functionality, the *shared_d365marketingforapps* connector is required to be categorized in the **Business** data group within your data policy. [Data policies](/power-platform/admin/wp-data-loss-prevention) are an administrator-level feature from Power Platform that prevent misuse or abuse of company data by restricting usage of Power Platform connectors or combinations of connectors.

The **Business** categorization allows business data to be shared with Power Automate. The connector doesn't allow sharing or storage of any personal data. The data policy setting for the connector can only be set by an administrator.

> [!NOTE]
> Customer Insights - Journeys previous used a connector called Dynamics 365 Marketing (the ID was *shared_dynamics365marketing*). Journeys now use the native connector, which is called Dynamics 365 Marketing V2 (the ID is *shared_d365marketingforapps*). To ensure proper functionality, make sure you are using the most recent native connector.

> [!IMPORTANT]
> The Customer Insights - Journeys connector is only available to be used directly by the Customer Insights - Journeys product and cannot be used by any user or service outside of the product. The connector is visible in the data policy connectors list to allow you to enable Customer Insights - Journeys to work when you have explicit data policies configured.

Learn more about connector settings and data policies: [Connector classification](/power-platform/admin/dlp-connector-classification).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
