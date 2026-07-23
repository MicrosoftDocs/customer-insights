---
title: Browser and system requirements
description: Find the supported desktop and tablet browsers, screen readers, and email clients for Dynamics 365 Customer Insights - Journeys, plus browser setup steps.
ms.date: 07/22/2026
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Browser and system requirements

Dynamics 365 Customer Insights - Journeys is a cloud-based service that doesn't require special software other than an up-to-date web browser, though some restrictions apply. This article lists the devices, browsers, and browser settings you need to work with Dynamics 365 Customer Insights - Journeys.

In most cases, Dynamics 365 Customer Insights - Journeys supports the same browsers and mobile devices as other model-driven apps in Dynamics 365 (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Customer Insights - Journeys, and Dynamics 365 Project Service Automation). These are described in [Requirements/supported configurations](/power-platform/admin/online-requirements), though some Dynamics 365 Customer Insights - Journeys features may require slightly newer systems, and a few other exceptions apply, as specified in this article.

## Supported desktop browsers

The [desktop browser requirements](/power-platform/admin/web-application-requirements) for Dynamics 365 Customer Insights - Journeys are the same as those for other model-driven apps in Dynamics 365.

## Supported tablet browsers

You can use the following OS/browser combinations to work with Dynamics 365 Customer Insights - Journeys on a tablet:

- Apple iOS 11 (or higher) with the current Apple Safari browser
- Google Android 7 (or higher) with the current Google Chrome browser
- Microsoft surface tablets running any supported desktop browser

## Accessibility and screen reader support

Dynamics 365 Customer Insights - Journeys has been tested to work correctly with the following accessibility technologies:

- Microsoft Edge browser (current version) with Microsoft Narrator screen reader
- Google Chrome browser (current version) with NV Access NVDA screen reader
- Google Chrome browser (current version) with Freedom Scientific JAWS screen reader
- Google Android Talkback screen reader
- Apple iOS Voice Over screen reader

## Browser configuration

Regardless of which supported browser you use, configure your browser as follows so Dynamics 365 Customer Insights - Journeys works correctly:

- **Allow pop-up windows from Dynamics 365 Customer Insights - Journeys**<br>Configure your browser to allow all pop-up windows from your Dynamics 365 Customer Insights - Journeys domain (see your browser's documentation for instructions), since some features rely on them. Most modern web browsers block all pop-up windows by default. Some browsers alert you when they block a pop-up window, (for example by showing an icon in the address bar), but others don't.
- **Allow JavaScript from Dynamics 365 Customer Insights - Journeys**<br>Enable JavaScript for your browser, at least for your Dynamics 365 Customer Insights - Journeys domain, to use the app's interactive features. Most browsers enable JavaScript by default.
- **Allow cookies from Dynamics 365 Customer Insights - Journeys**<br>Enable cookies for your browser, at least for your Dynamics 365 Customer Insights - Journeys domain, so your sign-in and preferences work as expected. Most browsers enable cookies by default.

## Enable touch for Microsoft Edge browsers

If you're using Microsoft Edge on a touch device, such as a tablet, enable the touch-based drag-and-drop features by doing the following steps:

1. Run Microsoft Edge.
2. Type &quot;about:flags&quot; into the address bar and select Enter.
3. A page of local browser settings opens. Under Standards Preview, set Enable touch events to Always on.
4. Restart your browser.

## Supported email clients

Marketing emails you create and send with Dynamics 365 Customer Insights - Journeys, including all included templates, render correctly across a wide range of recipient email clients, though older clients typically support fewer formatting options. For a complete list of tested email clients, see [Tested email clients](email-templates.md#tested-clients).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
