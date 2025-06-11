---
title: Setup changes in real-time journeys
description: How setting up real-time journeys differs from outbound marketing setup in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/16/2023
ms.topic: install-set-up-deploy
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Setup changes in real-time journeys

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

A difference from outbound marketing that's immediately noticeable when setting up real-time journeys is that it's no longer necessary to specify a Power Pages instance. Outbound marketing relies on Power Pages to host content like landing pages and event portals. The real-time journeys module provides a self-hosting option that doesn't rely on Power Pages.

This doesn't mean that real-time journeys can't work with Power Pages as a publishing option for forms. The real-time journeys module has been decoupled from Power Pages because not every customer is able to use Power Pages. Some customers even have another content management system in place. For these customers, decoupling from Power Pages offers more flexibility in form publishing. Learn more: [Transition marketing pages and forms](transition-walkthrough-forms.md)

Due to the lack of Power Pages requirement, the event management module also works differently from outbound marketing. Learn more: [Transition event management](transition-walkthrough-events.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
