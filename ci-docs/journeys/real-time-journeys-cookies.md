---
title: How the real-time journeys app uses cookies
description: Understand the deployment and management of cookies in real-time journeys for personalized customer interactions.
ms.date: 12/13/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:12/13/2024
---

# How the real-time journeys app uses cookies

Real-time journeys identifies website visitors using a technology called cookies. Cookies are small text files that are placed on your device by websites you visit or applications you use. Cookies are widely used to make websites work more efficiently, enhance the user experience, and provide data to website or application owners.

Our product uses cookies to help you understand customer behavior and provide personalized experiences to your customers.

> [!IMPORTANT]
> Many countries and regions (including the European Union) require that you get consent before setting a cookie on a user's machine. It's your organization's responsibility to be aware of, and conform to, all relevant laws and regulations in the markets where you operate, including consent to set cookies. Read more about the EU regulations: [Cookies and similar technologies](https://commission.europa.eu/resources-partners/europa-web-guide/design-content-and-development/privacy-security-and-legal-notices/cookies-and-similar-technologies_en).

## How cookies are deployed

Real-time journeys can generate a small piece of JavaScript code that reads and sets cookies on any webpage where you place the code. All you need to do to let real-time journeys record website visits and website link clicks to a given page is include the script on that page.

A cookie identifies a single device/browser/account combination. If you use two different browsers (such as Microsoft Edge and Mozilla Firefox on the same computer), each has its own cookie. Likewise, you have different cookies on each device that you use. Another user with their own account on your computer has yet other cookies. If a device gets deleted and reinstalled, all cookies are also deleted. Nevertheless, real-time journeys attempts to resolve the actual marketing profile (contact, lead) associated with each unique cookie ID.

Whenever a profile (contact, lead, Customer Insights - Data profile) visits a webpage, real-time journeys correlates the behavior-analysis cookie ID with the available profile data. In this way, the cookie ID is mapped to a real-time journeys profile ID, allowing the administrator to determine who has been browsing the site.

## Cookies set by real-time journeys

**Long-term behavioral-analysis cookie**: This cookie is set and/or read on any webpage where you have placed a real-time journeys website behavioral-analysis script. The cookie enables real-time journeys to collect end user events based on their level of interaction with a given website. The cookie contains no personal information, but does uniquely identify a specific browser on a specific machine. Real-time journeys can use the cookie to correlate this ID with an actual profile in the real-time journeys database. The cookie remains active for one year.

## List of real-time journeys cookies

The following table lists the cookies used by real-time journeys and the purpose and properties.

| Cookie name             | Is essential | Purpose           | First or third party | Properties              | Function (purpose detail)                                                                                                                                                                                                                                                                                                                   | Source URL/JS |
|-------------------------|--------------|-------------------|----------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| msdynci_trackingContext | No           | Behavior tracking | First party          | Persistent, client-side | This cookie tracks web behavior, such as page visits and clicks, over a 365-day period. It associates this behavior with a known user profile within Customer Insights Journeys to enable orchestration of personalized experiences tailored to user behavior and preferences, as well as analysis of end-user web interactions in reports. | Set by the website tracking script.              |

## How to disable nonessential real-time journeys marketing cookies

Real-time journeys provides a JavaScript API to help your organization conform with data regulations by disabling nonessential real-time journeys cookies. By defining the following function in your web pages, real-time journeys won't set nonessential cookies.

```
<script>
    function disableCookiesUsage() {
         return true;
    }
</script>
```

> [!NOTE]
> Without the above code, real-time journeys will set non-essential cookies by default.

If you use a third-party system to handle consent, such as a consent service or a cookie banner, you can instruct real-time journeys to set nonessential cookies with the following call:

```
function disableCookiesUsage() {
     return false;
 }
```

Without nonessential cookies, real-time journeys's web tracking capabilities are limited and you can't orchestrate personalized experience to your customers.

[!INCLUDE [footer-include](./includes/footer-banner.md)]