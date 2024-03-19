---
title: Guidelines for using Outbound marketing segments in Customer Insights - Journeys
description: Guidelines for using Outbound marketing segments in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/19/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Guidelines for using Outbound marketing segments in Customer Insights - Journeys

While we allow using outbound marketing segments in Customer Insights - Journeys, there are certain caveats and considerations we must look at. 

## What happens in the background?

For running a Customer Insights - Journeys journey, we need a Customer Insights - Journeys segment. When an outbound marketing segment is used, we create a copy and export the outbound segment to create a Customer Insights - Journeys segment. This export takes time, and we may run into issues if a journey runs before the export completes. 

## When to consider using an Outbound marketing segment?

It's advised to use Customer Insights - Journeys segments in journeys. It's okay to use Outbound marketing segments in Customer Insights - Journeys when:
1. There's a segment query, which can't be replicated in Customer Insights - Journeys due to missing functionality. We're working on actively developing all functionalities supported in Outbound marketing to Customer Insights - Journeys and more.
1. It's used only as an audience segment. It's advised not to use Outbound Marketing segments as exclusion segments. In case an export is delayed, the journey might execute on more contacts than expected since the export may haven't completed. 
1. Segment is less than 750k in size. For a segment above this size, exports are unreliable.
1. It's recommended to use Outbound marketing segments with Ongoing Journey [Add link here]. Using it with One-time journey might cause issues as it picks up the current members exactly at the time when the journey runs. If the export isn't completed by then, we may end up missing members. 

## What to keep in mind while scheduling the journey?

It's recommended to schedule the journey a few hours (Recommended 4-6 hours. It takes approximately 60 mins per 1 million members for the export to complete.) In the future to give the export enough time to complete. 

## Known Limitations

After a journey runs, the journey Insights view shows links to the segments used. To make sure that the exported segment is always up to date, we clean up the exported Customer Insights - Journeys segments 3 days after a journey completes it's run if it isn't used in any other journey. 

The insights when an Outbound marketing segment is used in Customer Insights - Journeys won't be linked to the original Outbound marketing segment in this case. Note that the original Outbound marketing segment isn't cleaned up. We're working on fixing this issue from our end (Provide Bug ID here).
