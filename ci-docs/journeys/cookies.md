---
title: How the outbound marketing app uses cookies
description: Describes how cookies are set and used in outbound marketing.
ms.date: 09/20/2023
ms.topic: reference
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# How the outbound marketing app uses cookies

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Outbound marketing identifies website visitors using a technology called *cookies*. A cookie is a small file that's sent by a server and saved by your browser. Each time you visit a server for which a cookie is set, your browser submits that cookie value back to the server. In this way, the cookie can provide a unique visitor ID, which enables the server to return information that is unique to you. This is the technology that originally made the online shopping cart possible.

> [!IMPORTANT]
> Many countries/regions (including the European Union) require that you obtain consent before setting a cookie on a resident's machine. It is your organization's responsibility to be aware of, and conform to, all relevant laws and regulations in the markets where you operate, including when it comes to obtaining consent to set cookies. You can read more about the EU regulations at [ec.europa.eu/ipg/basics/legal/cookies/](https://ec.europa.eu/ipg/basics/legal/cookies/).
> 
> This page explains how outbound marketing can help your organization conform to these regulations.

Outbound marketing can generate a small piece of JavaScript code that reads and sets cookies on any page where you place the code. All you need to do to let outbound marketing record visits to a given page is include the script on that page.

A cookie identifies a single device/browser/account combination. If you use two different browsers (such as Mozilla Firefox and Internet Explorer on the same computer), each has its own cookie. Likewise, you have different cookies on each device that you use. Another user with their own account on your computer has yet other cookies. If a device gets deleted and reinstalled, all cookies will also be deleted. Nevertheless, outbound marketing attempts to resolve the actual marketing contact associated with each unique cookie ID.

Whenever a contact submits a marketing page, outbound marketing correlates the behavior-analysis cookie ID with the incoming contact data submitted with the marketing page form. In this way, the cookie ID is mapped to an outbound marketing contact ID, allowing the administrator to determine who has been browsing the site. The system applies its configured duplicated-detection method to determine whether incoming landing-page data should be mapped to an existing contact or to a new contact.

Outbound marketing sets three different types of cookies:

- **Long-term behavioral-analysis cookie**: This cookie is set and/or read on any webpage where you have placed an outbound marketing website behavioral-analysis script. The cookie enables outbound marketing to score leads based on their level of interaction with a given website. The cookie contains no personal information, but does uniquely identify a specific browser on a specific machine, and outbound marketing can use it to correlate this ID with an actual contact in the outbound marketing database. The cookie remains active for two years.
- **Short-term, single-visit cookie**: This cookie is also set and/or read on any webpage where you have placed an outbound marketing website behavioral-analysis script. By default, it expires after just 30 minutes. Outbound marketing uses it to group all page loads by a given visitor that is recorded by the same behavioral-analysis script and that occur within the configured time frame. The cookie considers all of these as part of a single &quot;visit&quot; to the website.
- **Event website**: The event website uses a session cookie to enable contacts to sign in and register for events. Additionally, the event website uses cookies to store the user's language.

> [!NOTE]
> The outbound marketing application also sets cookies to enable sign-in sessions and other technical features. These only affect direct users of outbound marketing (such as your internal marketing personnel), not the general public. Microsoft&#39;s standard privacy policy applies for these users.

## List of outbound marketing cookies

The table below lists the cookies used by outbound marketing and the purpose and properties.

| Cookie name | Is Essential | Purpose | First or third party | Properties | Function (Purpose detail) | Source URL/JS |
|---|---|---|---|---|---|---|
| 79f08280-5c63-4331-b04d-fb6f39afda51 | No | Behavior tracking | Third party | Persistent, secure, HttpOnly | Identifies end user(by browser).   We set this cookie when end user visits a marketing page or a select a link   (with tracking enabled). At some point of time, when a form is submitted by this end user, a new   contact/lead is created and we leverage the cookie available in the browser   to associate previous visits with the newly generated contact/lead. | This cookie is set by the   service. URL differs for each customer org. It can be seen in the tracking/form loader code: &lt;div class="d365-mkt-config" style="display:none" data-website-id="{websiteid}" data-hostname={GUID}.svc.dynamics.com&gt;&lt;/div&gt; |
| 319af4c0-e197-4de9-8a9b-fe98c8a2ca04 | No | Session tracking | Third party | Session, secure, HttpOnly | To find out how much time user spent on the page | This cookie is set by the   service. URL differs for each customer org. It can be seen in the   tracking/form loader code: &lt;div class="d365-mkt-config" style="display:none" data-website-id="{websiteid}" data-hostname=**"**{GUID }.svc.dynamics.com"&gt;&lt;/div&gt;
| msd365mkttr | No | Behavior tracking | First party | Persistent, client-side | This is being used for the same   purpose as the first cookie(79f08280-5c63-4331-b04d-fb6f39afda51). Only   difference is that this cookie is set on the customer domain. In   some cases, we're unable to access third party cookies (ex: safari OOB blocks) therefore we set this first party cookie to keep   functionality.| Set by the form loader or website tracking   script |
| msd365mkttrs | No | Session tracking | First party | Session, client-side | This cookie is similar to   (319af4c0-e197-4de9-8a9b-fe98c8a2ca04). Only difference is that it's a first   party cookie | Set by the form loader or   website tracking script |

## How to disable nonessential outbound marketing cookies

Outbound marketing provides a JavaScript API to help your organization conform with data regulations by disabling nonessential outbound marketing cookies. By defining the following function in your web pages, outbound marketing won't set nonessential cookies.

```
<script>
    function d365mktConfigureTracking() {
         return {Anonymize: true};
    }
</script>
```

> [!NOTE]
> Without the above code, outbound marketing *will* set non-essential cookies by default.

If you use a third-party system to handle consent such as a consent service or a cookie banner, you can instruct outbound marketing to set nonessential cookies with the following call:

```
MsCrmMkt.reconfigureTracking({Anonymize: false})
```

Without nonessential cookies, outbound marketing's tracking capabilities are limited. In some scenarios, users appear to be anonymous. For example, form submissions continue to work correctly as user identification is based on the submitted data not on cookies, but form prefill data won't work.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
