---
title: Best practices for outbound segments in real-time journeys
description: Guidelines for using outbound marketing segments in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/19/2024
ms.topic: best-practice
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Best practices for outbound segments in real-time journeys

This article discusses caveats to consider when using outbound marketing segments in Customer Insights - Journeys.

## What happens in the background when using outbound segments in real-time journeys?

To run a real-time journey, you need to use a real-time journeys segment. When you use and outbound marketing segment, the app creates a copy of the segment and it to create a real-time journeys segment. This export takes time and you may run into issues if a journey runs before the export completes.

## When should you consider using an outbound marketing segment?

Typically, you should try to use real-time journeys-native segments in real-time journeys. You can use outbound marketing segments in real-time journeys when:

1. There's a segment query that you can't replicate in real-time journeys due to missing functionality. This circumstance will diminish over time as the real-time journeys functionality continues to develop feature parity and improvements on outbound marketing features.
1. It's used only as an audience segment. You shouldn't use outbound Marketing segments as exclusion segments. If an export is delayed, the journey might execute on more contacts than expected because the export hasn't completed.
1. The segment is less than 750,000 in size. For segments beyond this size, exports are unreliable.
1. The journey is ongoing. Using an outbound segment with a one-time journey might cause issues as it picks up the current members exactly when the journey runs. If the export isn't completed by then, you may end up with missing members.

## What should you keep in mind while scheduling a journey with outbound marketing segments?

If you're using outbound marketing segments, you should delay the start of your journey by at least a few hours after you create it. Ideally, the journey should start in four to six hours to allow enough time for the segment export. It takes approximately 60 minutes per 1 million members for the export to complete.

## Known limitations

After a journey runs, the **Journey insights** view shows links to the segments used. To make sure that the exported segment is always up to date, the app cleans up the exported real-time journeys segments three days after a journey completes its run (if the segment isn't used in any other journey).

The insights when an outbound marketing segment is used in a real-time journey aren't linked to the original outbound marketing segment. Additionally, the original outbound marketing segment isn't cleaned up. This issue will be addressed in a future bug fix.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
