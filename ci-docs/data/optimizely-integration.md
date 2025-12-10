---
title: No-code web personalization using Optimizely (preview)
description: Learn how to personalize web experiences with the Customer Insights - Data and Optimizely integration.
ms.date: 12/13/2024
ms.topic: how-to
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: mhart
ms.custom: bap-template
---

# No-code web personalization using Optimizely (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Personalizing the web experience for your visitors is critical to foster loyalty, increase engagement, enhance satisfaction, and drive higher conversion rates. This kind of customization often requires a team of web developers. But Optimizely's native integration with Customer Insights - Data empowers marketers to personalize your website for visitors, without developers and without having to understand code themselves.

The Optimizely integration allows Customer Insights - Data to share segments with Optimizely and create audiences in Optimizely that are based on those segments. You can use them in your web personalization campaigns or web experiments. Customer Insights identifies website visitors who are members of a segment and lets you provide a personalized web experience to them in real time.

For example, let's say you create a segment in Customer Insights - Data for high-value customers. This segment also shows up in Optimizely, making it easy to add a promotional banner to the home page that's only displayed to visitors who are part of the "high-value customers" segment.

You can also track user behavior for events that real-time tracking supports and for specific events in Optimizely: Campaign & Experiment.

Watch this brief video for an overview of the Optimizely integration with Customer Insights - Data.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=0374bff9-f481-4324-8237-ebbaaffaed27]

> [!TIP]
> Sign up to [request access to the preview version](https://forms.office.com/r/TJEE62xTD3) of the real-time personalization features and [read the blog about the announcement](https://cloudblogs.microsoft.com/dynamics365/?p=188733).

## Prerequisites

- Optimizely license and account for Web Experimentation. Learn more at [Optimizely Web Experimentation](https://www.optimizely.com/products/experiment/web-experimentation/).
- Customer Insights real-time tracking script added to your website. Learn more in [Set up real-time web personalization](real-time-web-personalization.md).
- Optimizely tracking script added to your website. Learn more at [Optimizely Web Experimentation JavaScript snippet](https://support.optimizely.com/hc/articles/4410284311565-Optimizely-Web-Experimentation-JavaScript-snippet).
- CookieID in Optimizely set to the Customer Insights cookie ID: `_msci`

## Connect to Optimizely

Connect to Optimizely in either of the following ways.

### Use the first run experience

Going through the first run experience creates a connection to Optimizely and exports all segments. You can edit the export and remove segments as you prefer.

1. In Customer Insights - Data, go to **Web tracking & personalization**.
1. Select **Set up** in the Optimizely tile.
1. Enter a name for the connection to Optimizely.
1. Enter an Optimizely API key. Learn more at [Personal access token](https://docs.developers.optimizely.com/web-experimentation/docs/personal-access-token).
1. Agree to the data privacy and compliance notice, and then select **Connect**.
1. Choose the Optimizely project you want to connect to.
1. Select **Save** or **Save and Run**.

You now have a connection to Optimizely and an export with all your segments. You can edit them like any other connection or export.

### Create the connection and export from scratch

Create a connection to Optimizely and export your segments manually. This connection can be shared with other users in Customer Insights. You can remove the connection at any time to discontinue the use of Optimizely.

#### Create the connection

1. In Customer Insights - Data, go to **Connections**.
1. Select **Add connection**, and then select **Optimizely**.
1. Enter a name for the connection.
1. Enter an Optimizely API key. Learn more at [Personal access token](https://docs.developers.optimizely.com/web-experimentation/docs/personal-access-token).
1. Agree to the data privacy and compliance notice, and then select **Save**.

#### Create an export and include the segments that you want to export to Optimizely

1. In Customer Insights - Data, go to **Exports**.
1. Create an export and choose the Optimizely connection you want to use. If you don't see a connection, create one or ask your administrator to create the connection and share it with you.
1. Name your export and provide the Optimizely Project ID.
1. To export the segments to Optimizely right away, select **Save and Run**. You can also schedule the export to run on system refresh.

## Known limitations

- In Optimizely, only 100 audiences or attributes can be created per project. If you have more than 100, the remaining audiences or attributes move to your audiences archive in Optimizely.
