---
title: Use Microsoft Teams for Dynamics 365 Customer Insights - Journeys online events
description: Learn how to create and host live events in Dynamics 365 Customer Insights - Journeys using Microsoft Teams as the streamed event provider.
ms.date: 02/04/2026
ms.topic: how-to
author: terezakirk
ms.author: terezakirk
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use Microsoft Teams for Dynamics 365 Customer Insights - Journeys online events

[!INCLUDE [azure-ad-to-microsoft-entra-id](./includes/azure-ad-to-microsoft-entra-id.md)]

[!INCLUDE [marketing-trial-cta](./includes/marketing-trial-cta.md)]

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=46b08db8-059a-40c7-928e-6b596f087907]

This article explains how to use Microsoft Teams as an online meeting provider for Customer Insights - Journeys events. Teams event functionality is incorporated directly into the Customer Insights - Journeys app, allowing you to use Teams meeting, webinars, Teams live events and Teams town hall for one/some to many online events.

For general information about setting up Microsoft Teams, refer to the [Microsoft Teams deployment overview](/microsoftteams/deploy-overview).

> [!NOTE]
> To use Microsoft Teams as an online event provider, you must have a [Microsoft 365 license](/office365/servicedescriptions/teams-service-description) that allows you access to the Teams service. If you don't have the correct license, you won't see the Teams webinar, Teams meeting, or Teams live event options as a part of the **Streaming provider** list.

## Create an online event

To create a Teams event, select **Event planning** in the Customer Insights - Journeys app area switcher, then select **Events** in the left navigation pane. Select **+New** in the top ribbon.

## Event streaming options

After you flip the **Do you want to stream this event** toggle to **Yes**, you have six streaming options: Teams meeting, Teams webinar, Teams live event, and then modernized set of options, Teams meeting v2, Teams webinar v2, and Teams town hall. This article explains the difference between the event types.

### Teams meetings, Teams webinars, and Teams live events

This set of online event options represents the legacy Teams experience. While still available to use, these options are gradually being phased out in favor of modernized integrations and new event types that are already available in Customer Insights - Journeys. As of February 2026, a new label "retiring" has been added to the legacy meeting type to highlight its life cycle. 

> [!IMPORTANT]
> Microsoft is retiring Teams live events and the associated Microsoft Graph APIs used to create Teams live events effective June 30, 2026 though Microsoft will honor all live events that are already scheduled through February 28, 2027. We encourage customers to migrate to Teams town halls, which offers an improved experience for large-scale digital and hybrid events. Teams town halls also provide comparable Graph APIs for programmatic creation, management, and integration of broadcast-style events. See the official Microsoft Teams announcement [here](https://go.microsoft.com/fwlink/?linkid=2347480)
> Microsoft honors all Teams Webinar and Teams Meeting that are already scheduled through February 28, 2027. For any events scheduled post this period, use Teams Webinar v2 or Teams Meeting v2.

1. **Teams meeting (retiring)**: Allows you to create an interactive online meeting experience where all attendees can share audio, video, or content. For more information, see [Meetings in Microsoft Teams](/microsoftteams/tutorial-meetings-in-teams).
1. **Teams webinar (retiring)**: Useful for conference keynotes or meetings where a few presenters are talking to a large audience. Webinars can support up to 1,000 attendees and support attendee registrations. For more information, see [Webinars in Microsoft Teams](/microsoftteams/plan-webinars)
1. **Teams live event (retiring)**: An extension of Teams meetings that enable you to schedule and produce events that stream to large online audiences. Teams live events are being replaced with Teams town halls and Teams will soon announce official removal date. For more information, see [Live Events in Microsoft Teams](https://support.microsoft.com/office/get-started-with-microsoft-teams-live-events-d077fec2-a058-483e-9ab5-1494afda578a)

### Teams meeting v2, Teams webinar v2, Teams town hall

The new generation of meeting types delivers the latest Microsoft Teams enhancements and features, powered by Graph API integration. These updates provide improved control over meeting options, enabling organizers to configure Teams settings directly within the Customer Insights – Journeys interface for a seamless experience.

#### Key differences

- Latest meeting types powered by the Teams Graph API
- Improved editing controls for set up of meeting options directly from the Teams user interface
- Ability to define coorganizers from Customer Insights - Journeys (coming in the February 2026 release)
- Improved attendance report with check-ins, check-out, and total attendance duration (coming in the February 2026 release)

1. **Teams meeting v2**: New version of the Teams meeting event that allows you to create an interactive online meeting experience where all attendees can share audio, video, or content. For more information, see [Use Microsoft Teams meetings v2 to create online meetings in Customer Insights - Journeys](teams-meeting-version-2.md)
1. **Teams webinar v2**: New version of Teams webinars that's useful for conference keynotes or meetings where a few presenters are talking to a large audience. Webinars can support up to 1,000 attendees and support attendee registrations. For more information, see [Use Microsoft Teams webinars v2 to host online events in Customer Insights - Journeys](teams-web-version-2.md)
1. **Teams town hall**: Teams town hall is a new feature designed to help organizations host large-scale, interactive virtual events directly within Microsoft Teams. For more information, see [Use Microsoft Teams town halls to host large-scale online events](teams-town-hall.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
