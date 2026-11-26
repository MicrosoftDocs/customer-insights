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

Tracking helps you understand what visitors are interested in. Personalize your customers' web experience by changing banners, offers, recommended products, or entire pages based on each visitor's interests and behavior. This article explains how to personalize with Optimizely or APIs so you can choose the approach that fits your needs:

- **Without code, by using Optimizely**: Your segments from Customer Insights - Data become audiences in Optimizely, and marketers can change what those audiences see without involving developers. Choose this option if you already use Optimizely and want your marketing team to manage the experience. Learn more in [Personalize the web experience without code by using Optimizely](#personalize-the-web-experience-without-code-by-using-optimizely).

- **With code, by using APIs**: Your development team queries Customer Insights - Data for a visitor's profile, segments, measures, and web interactions, and builds a customized experience. Choose this option if you need full control or don't use Optimizely. Learn more in [Personalize the web experience with code](#personalize-the-web-experience-with-code).

Both approaches read the same web tracking data, so you can start with one and add the other later.

## Personalize the web experience without code by using Optimizely

The Optimizely integration lets Customer Insights - Data share segments with Optimizely and create matching audiences. Customer Insights - Data identifies which visitors belong to a segment, and Optimizely delivers the experience in real time.

For example, create a segment in Customer Insights - Data for high-value customers. This segment appears in Optimizely, where you can add a promotional banner to the home page that only those visitors see. You can also run experiments with those audiences and track behavior for both web tracking events and Optimizely campaign and experiment events.

Watch this brief video for an overview of the Optimizely integration with Customer Insights - Data.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=0374bff9-f481-4324-8237-ebbaaffaed27]

### Prerequisites

- An Optimizely license and account for Web Experimentation. Learn more at [Optimizely Web Experimentation](https://www.optimizely.com/products/experiment/web-experimentation/).
- The Customer Insights - Data real-time tracking script added to your website. Learn more in [Set up web tracking and personalization](real-time-web-personalization.md).
- The Optimizely tracking script added to your website. Learn more at [Optimizely Web Experimentation JavaScript snippet](https://support.optimizely.com/hc/articles/4410284311565-Optimizely-Web-Experimentation-JavaScript-snippet).
- Set the cookie ID in Optimizely to the Customer Insights - Data cookie ID, `_msci`.

### Connect to Optimizely

Connect to Optimizely by using the first-run experience. This process creates a connection to Optimizely and exports all segments.

1. In Customer Insights - Data, go to **Web tracking & personalization**.
1. Select **Set up** in the Optimizely tile.
1. Enter a name for the connection.
1. Enter an Optimizely API key. Learn more at [Personal access token](https://docs.developers.optimizely.com/web-experimentation/docs/personal-access-token).
1. Agree to the data privacy and compliance notice, and then select **Connect**.
1. Choose the Optimizely project you want to connect to.
1. Select **Save** or **Save and Run**.

You can edit the export afterward and remove any segments you don't want shared.

To create the connection separately, go to **Connections**, select **Add connection** > **Optimizely**, enter a name and your API key, accept the notice, and select **Save**. You can share connections with other Customer Insights users and remove them at any time to stop using Optimizely.

### Known limitations

- In Optimizely, you can create up to 100 audiences or attributes per project. If you exceed this limit, Optimizely moves extra audiences or attributes to your audiences archive.

## Personalize the web experience with code

Use APIs to personalize your visitors' web experience. Query any of the [Customer Insights - Data APIs](dv-odata.md) to retrieve information about each customer, such as demographic information, web interactions, activities, segments, and measures.

Because a cookie ID uniquely identifies a known customer or an unknown visitor, you can use it to query the visitor's profile. Retrieve the Customer Insights - Data web tracking cookie from your website's server. The Customer Insights - Data web tracking cookie in the request is named `_msci`.

For example, use C# to retrieve the current visitor's cookie ID:

```csharp
string cookieId = Request.Cookies["_msci"]; // Customer Insights - Data cookie
```

Then, use the cookie ID as an identifier to query any of the Customer Insights - Data APIs.

## Related information

- [Web tracking and personalization overview](real-time-web-personalization-overview.md)
- [Scenarios for web tracking and personalization](real-time-web-personalization-scenarios.md)
- [Set up web tracking and personalization](real-time-web-personalization.md)
