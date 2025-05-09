---
title: Known issues for journeys
description: Learn about known issues related to real-time journeys functionality in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/29/2024
ms.topic: troubleshooting-known-issue
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Known issues for journeys

This article documents known issues related to real-time journeys functionality.

## Active journeys that were created on or before May 5, 2022 will stop working on July 1, 2024

Real-time journeys created on or before Thursday, May 5, 2022 use an internal component that is no longer supported. Newly created, copied, and versioned journeys use the latest, supported components. Outbound marketing journeys aren't impacted and don't require action.

If no action is taken, the impacted real-time journeys will stop working on or after July 1, 2024.

### Steps to avoid journey disruption

In Customer Insights – Journeys, go to the **Real-time journeys** area and navigate to **Engagement** > **Journeys**. Determine which of your journeys need to be republished by filtering your real-time journeys list view to "**Live**" and "**Completing**" journeys created "**on or before 5/5/2022**", then create a new version, or a copy, of these real-time journeys.

> [!NOTE]
> Creating a new version of the journey is recommended in order to keep the analytics for the journey scenario together under a single journey.

To create a new version of a journey (*recommended*):

- Open the journey and select the **Edit** action.
- Make any necessary changes to the journey. For example: modify the scheduled start time to a date or time in the future.  
    - This can be done by selecting the first tile in the journey and changing the **Schedule** > **Start** field.
- Select the **Publish** action.

Learn more about versioning: [Edit a live journey in Customer Insights - Journeys](real-time-marketing-edit-journey.md)

To create a new copy of the journey (*alternative*):

- Open the journey and select the **Create a copy** action.
- Make any necessary changes to the journey.
- **Save** the new copy of the journey.
- Open the original journey and **Stop** the journey.
- Open the new journey and **Publish** the new journey.
