---
title: Personalize your customers' web experience
description: Personalize your customers' web experience with Customer Insights - Data using APIs or Optimizely. Learn how to deliver relevant website content.
ms.date: 10/21/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: tozahalk
ms.custom:
  - bap-template
  - ci-data-web-tracking
  - ai-gen-docs-bap
  - ai-seo-date: 09/16/2026
ai-usage: ai-assisted
---

# Personalize your customers' web experience

Tracking tells you what visitors are interested in. Personalize your customers' web experience by changing banners, offers, recommended products, or entire pages based on each visitor. This article explains how to personalize with Optimizely or APIs so you can choose the approach that fits your needs:

- **Without code, by using Optimizely**: Your segments from Customer Insights - Data become audiences in Optimizely, and marketers change what those audiences see without involving developers. Choose this option if you already have Optimizely and want marketing to own the experience. Learn more in [Personalize the web experience without code by using Optimizely](#personalize-the-web-experience-without-code-by-using-optimizely).

- **With code, by using APIs**: Your development team queries Customer Insights - Data for a visitor's profile, segments, measures, and web interactions, and builds the experience however you like. Choose this if you need full control or don't use Optimizely. Learn more in [Personalize the web experience with code](#personalize-the-web-experience-with-code).

Both approaches read the same web tracking data, so you can start with one and add the other later.

## Personalize the web experience without code by using Optimizely

The Optimizely integration allows Customer Insights - Data to share segments with Optimizely and create matching audiences in Optimizely. Customer Insights - Data identifies which visitors belong to a segment, and Optimizely delivers the experience in real time.

For example, create a segment in Customer Insights - Data for high-value customers. This segment appears in Optimizely, where you can add a promotional banner to the home page that only those visitors see. You can also run experiments against those audiences, and track behavior for both web tracking events and Optimizely's own campaign and experiment events.

Watch this brief video for an overview of the Optimizely integration with Customer Insights - Data.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=0374bff9-f481-4324-8237-ebbaaffaed27]

### Prerequisites

- An Optimizely license and account for Web Experimentation. Learn more at [Optimizely Web Experimentation](https://www.optimizely.com/products/experiment/web-experimentation/).
- The Customer Insights - Data real-time tracking script added to your website. Learn more in [Set up web tracking and personalization](real-time-web-personalization.md).
- The Optimizely tracking script added to your website. Learn more at [Optimizely Web Experimentation JavaScript snippet](https://support.optimizely.com/hc/articles/4410284311565-Optimizely-Web-Experimentation-JavaScript-snippet).
- The CookieID in Optimizely must be set to the Customer Insights - Data cookie ID: `_msci`.

### Connect to Optimizely

Connect to Optimizely by using the first run experience, which creates a connection to Optimizely and exports all segments.

1. In Customer Insights - Data, go to **Web tracking & personalization**.
1. Select **Set up** in the Optimizely tile.
1. Enter a name for the connection.
1. Enter an Optimizely API key. Learn more at [Personal access token](https://docs.developers.optimizely.com/web-experimentation/docs/personal-access-token).
1. Agree to the data privacy and compliance notice, and then select **Connect**.
1. Choose the Optimizely project you want to connect to.
1. Select **Save** or **Save and Run**.

You can edit the export afterward and remove any segments you don't want shared.

To create the connection separately instead, go to **Connections**, select **Add connection** > **Optimizely**, name it, enter your API key, accept the notice, and save. You can share connections with other Customer Insights users, and remove them at any time to stop using Optimizely.

### Known limitations

- In Optimizely, you can create up to 100 audiences or attributes per project. If you exceed this limit, Optimizely moves the extra audiences or attributes to your audiences archive.

## Personalize the web experience with code

 Use APIs to personalize the web experience for your visitors. Query any of the [Customer Insights - Data APIs](dv-odata.md) to retrieve rich information about each customer, such as demographic information, web interactions, activities, segments, and measures.

Because the cookie IDs uniquely identify a known customer or an unknown visitor, you can use the cookie ID to query a profile. Retrieve the Customer Insights - Data web tracking cookie on the server side of your website. The Customer Insights - Data web tracking cookie is named `_msci` in the request.

For example, by using C#, you can find the cookie ID of the current visitor:

```csharp
string cookieId = Request.Cookies["_msci"]; // Customer Insights - Data cookie
```

Then, use the cookie as an identifier to query any of the Customer Insights - Data APIs.

## Related information

- [Web tracking and personalization overview](real-time-web-personalization-overview.md)
- [Scenarios for web tracking and personalization](real-time-web-personalization-scenarios.md)
- [Set up web tracking and personalization](real-time-web-personalization.md)