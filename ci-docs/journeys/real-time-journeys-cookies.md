---
title: How real-time journeys uses cookies
description: Learn how real-time journeys cookies track website activity and help associate visits with contacts or leads. Explore cookie behavior and consent controls.
ms.date: 11/24/2026
ms.topic: article
author: udag
ms.author: colinbirkett
ai-usage: ai-assisted
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:12/13/2024
---

# How real-time journeys use cookies

Real-time journeys use cookies to record website visits and link clicks and help associate activity with known contacts or leads. This article explains how those cookies are deployed and how to control nonessential cookies.

Dynamics 365 Customer Insights - Journeys uses cookies to help you understand customer behavior and provide personalized experiences to your customers.

> [!IMPORTANT]
> Many countries and regions (including the European Union) require that you get consent before setting a cookie on a user's machine. It's your organization's responsibility to be aware of, and conform to, all relevant laws and regulations in the markets where you operate, including consent to set cookies. For more information about EU regulations, see [Cookies and similar technologies](https://commission.europa.eu/resources-partners/europa-web-guide/design-content-and-development/privacy-security-and-legal-notices/cookies-and-similar-technologies_en).
>
> This information isn't legal advice. Consult your own privacy counsel about your consent design.

## How real-time journeys deploy cookies

Real-time journeys can generate a small piece of JavaScript code that reads and sets cookies on any webpage where you place the code. All you need to do is include the script on the webpage to let real-time journeys record website visits and link clicks for that webpage.

A cookie identifies a single device/browser/account combination. If you use two different browsers (such as Microsoft Edge and Mozilla Firefox on the same computer), each browser has its own cookie. Likewise, you have different cookies on each device that you use. Another user with their own account on your computer has another set of cookies. If a device gets deleted and reinstalled, all cookies are also deleted. Nevertheless, real-time journeys attempts to resolve the actual marketing profile (contact, lead) associated with each unique cookie ID.

For supported web tracking scenarios, Customer Insights - Journeys associates website activity with known contacts or leads through a tracked message link or a marketing or event registration form submission. See [Personalize messages with web interaction data](interaction-journey-decision.md).

## Cookies set by real-time journeys

[!INCLUDE [web-tracking-identifiers](~/../ci-shared/web-tracking-identifiers.md)]

## List of real-time journeys cookies

[!INCLUDE [web-tracking-visitor-cookie](~/../ci-shared/web-tracking-visitor-cookie.md)]

Reading an existing `_msci` cookie on an ordinary visit doesn't renew its expiry.

### Journeys attribution cookies

Customer Insights - Journeys uses the following cookies to associate website activity with known contacts or leads. Not every cookie is created on every visit.

| Cookie name | Is essential | Purpose | First or third party | Properties | Function (purpose detail) | When set |
|-------------|--------------|---------|----------------------|------------|---------------------------|----------|
| `msdynci_trackingContext` | No | Behavior tracking | First party | Persistent, client-side; configured expiry of 365 days when written. | Stores the tracking context used to associate website activity with a known contact or lead. | The website tracking script initializes with a tracking context in the URL from a tracked Customer Insights - Journeys message link, and cookie usage is permitted. |
| `msdynmkt_formsubmissionid` | No | Behavior tracking | First party | Persistent, client-side; configured expiry of 365 days when written. | Associates subsequent website activity with the contact or lead resolved by a marketing or event registration form submission. A submission can create, match, or update a record according to the [matching settings](real-time-marketing-manage-forms.md#form-settings). | The form loader receives a successful submission response containing a submission ID, with **Web tracking** enabled for the marketing or event registration form and cookie usage permitted. |

A new tracked link or successful submission can write the corresponding attribution cookie again.

[!INCLUDE [web-tracking-browser-storage](~/../ci-shared/web-tracking-browser-storage.md)]

## How to disable nonessential real-time journeys marketing cookies

For marketing and event registration forms, also define the function before the form loader initializes.

[!INCLUDE [web-tracking-cookie-controls](~/../ci-shared/web-tracking-cookie-controls.md)]

Account for tracking scripts loaded by marketing or event registration forms as well as scripts installed separately. A tracking context supplied in a Customer Insights - Journeys message link can still be used in memory when cookies are refused.

Website cookie permission is separate from the compliance profile's **Tracking** purpose. See [Configure tracking consent](real-time-marketing-tracking-consent.md) for Customer Insights - Journeys consent enforcement.
