---
title: "Track usage of a segment"
description: "Track the usage of a segment in other apps."
ms.date: 11/28/2022
ms.topic: concept
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-customers-page
  - ci-enrichment-details
  - ci-segments
  - ci-segment-details
  - customerInsights
---

# Track usage of a segment

If you use segments in apps which are based on the same Microsoft Dataverse organization that is connected with Customer Insights, you can track the usage of a segment. For [Customer Insights segments used in customer journeys of Dynamics 365 Marketing](/dynamics365/marketing/real-time-marketing-ci-profile), the system informs you about the usage of that segment.

When editing a segment that is being used within the Customer Insights environment, or in a customer journey in Marketing, a banner in the [segment builder](segment-builder.md) informs you about the dependencies. Inspect the dependency details directly from the banner or by selecting **Usage** in the segment builder.

The **Segment usage** pane shows the details about the usage of this segment in Dataverse-based apps. For segments used in customer journeys, you’ll find a link to inspect the journey in Marketing where this segment is used. If you have permissions to access the Marketing app, view more details there.

:::image type="content" source="media/segment-usage-pane.png" alt-text="Side pane with details of the segment usage in the segment builder.":::

The system informs you about the usage of a tracked segment when you try to delete it. If the segment you're about to delete is used in a customer journey in Marketing, that journey will stop for all users in the segment. If the journey is part of a marketing campaign, the deletion will affect that campaign itself. However, you can still delete the segment despite the warnings.

:::image type="content" source="media/segment-usage-delete.png" alt-text="Dialog box to confirm segment deletion when a segment is used in a Dataverse application.":::

## Supported apps

Usage is currently tracked in the following Dataverse-based apps:

- [Customer journeys in Dynamics 365 Marketing](/dynamics365/marketing/real-time-marketing-ci-profile)

[!INCLUDE [footer-include](includes/footer-banner.md)]
