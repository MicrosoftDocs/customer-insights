---
title: Journeys overview
description: Learn how to create automated campaigns with real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/10/2025
ms.topic: overview
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:02/04/2025
---

# Journeys overview

Dynamics 365 Customer Insights - Journeys helps you visualize and automate the journey that your customers take as they engage with your product or services. A simple customer journey might include a short interaction, such as a single email campaign where you send them product or service information and include a link to your website for more information. A complex journey might include the full process from discovery, through nurturing, and on to identifying qualified leads.

## Trigger-based vs segment-based

There are two types of journeys:

1. [Trigger-based journeys](real-time-marketing-trigger-based-journey.md) that react to customer action (for example, filling out a form or registering for an event).
1. [Segment-based journeys](real-time-marketing-segment-based-journey.md) that target customers that share certain attributes (for example, loyalty club members in the state of Washington).

## Journey templates

You can create templates to make it easier for anyone to start with a pre-existing journey that represents common customer journey patterns for your business. Create a journey template by building a journey and selecting **Save as template**.

## The journey life cycle

All journeys have a life cycle: they're created and then published, once published they complete or can be stopped. A journey moves through these stages or states as shown in the diagram below:

:::image type="content" source="media/journeys-overview-states.png" alt-text="Stages of real-time journeys diagram." lightbox="media/journeys-overview-states.png":::

Legend:

1. Automatic transition to the next state when required system actions are complete.
Automatic transition to “Completing” when the journey stops accepting new customers, the journey has expired, or a new version is published.
1. Automatic transition to “Completed” when all customers in the journey have completed their journey.
1. Automatic transition to “Live” when the scheduled start time is reached.

## Details of journey states

The following table shows additional details about journey states and the transitions between them.

| State      | Definition                                                                 | User actions                                                                 |
|------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Draft**      | When a journey is created in the journey designer and saved, it’s in Draft state. | You can edit and update the journey as needed in this state. The journey isn’t active, and no customer can participate in this state. <br> **Publish:** Moves the journey to the Publishing state. <br> **Copy:** Makes a copy of the journey (the copy is a new journey in Draft state). |
| **Publishing** | An intermediate state when Publish is selected. The journey is validated and if errors are found, it reverts to Draft state. If everything is okay, the journey moves to the Live state. | No user actions are possible in this state. |
| **Live**       | The journey is Live (or running). A trigger-based journey accepts and reacts to triggers and lets customers who raised the trigger enter the journey. A segment-based journey processes the segment and lets the members enter the journey. (A journey may be Live and still not let new customers enter if the scheduled start time of the journey isn't yet reached.) | **Edit:** Goes into the Live edit state where the journey can be edited. <br> **Stop:** Stops the journey. <br> **Copy:** Makes a copy of the journey (the copy is a new journey in Draft state). |
| **Completing** | A journey in this state doesn’t allow new customers to enter but lets the current customers already in the journey finish. This state is reached for many reasons, such as when it’s past the journey’s scheduled end time, the journey has finished all its recurrences (for a repeating journey), all members of the segments have entered the journey (for a one-time segment-based journey), etc. | No user actions are possible in this state. |
| **Completed**  | The journey has finished its run. This state is reached when all eligible customers have completed their journey. | **Copy:** Makes a copy of the journey (the copy is a new journey in Draft state). |
| **Stopping**   | The journey is being stopped. No new customers are accepted, and current customers are being removed from the journey. As this action might take some time, it’s possible that some customers might still complete their journeys before the journey is stopped. | When there’s a backlog of messages due to high volume, those messages are deleted immediately and aren’t sent. This greatly reduces but doesn't always prevent messages from being delivered (some messages might have already been sent to the intermediate providers who will still deliver those messages even though the journey has been stopped). <br> No user actions are possible in this state. NOTE: If you have edited a published journey for any reason and generated new versions you must stop each version individually.|
| **Stopped**    | The journey has stopped. No new customers are accepted and there are no customers in the journey. | **Copy:** Makes a copy of the journey (the copy is a new journey in Draft state). |
| **Live, editing** | A new journey version is available that can be edited. The current version of the journey is still live and accepting customers or you can stop it to ensure the audience that has already entered the journey does not proceed through any remaining steps. You must stop each version of the journey separately. | **Publish:** Publishes the new version of the journey. The previous version of the journey moves to the Completing state to let anyone who has already entered finish the journey unless you explicitly 'Stop' that version. All new customers are accepted in the new version. <br> **(Discard):** The new version is discarded and focus returns to the current version of the journey that’s still Live. |

## Journey audit history

To enable journey audit history, go to the Power Apps [maker portal](https://make.powerapps.com) using CRMToolbox and enable the Audit History Extractor.