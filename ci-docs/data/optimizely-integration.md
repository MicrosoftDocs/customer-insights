---
title: No-code web personalization using Optimizely (preview)
description: Personalize web experiences with the Customer Insights - Data and Optimizely integration.
ms.date: 05/02/2024
ms.topic: how-to
author: philk
ms.author: philk
ms.reviewer: mhart
ms.custom: bap-template
---

# No-code web personalization using Optimizely (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Personalizing the web experience for your visitors is critical to foster loyalty, increase engagement, enhance satisfaction, and drive higher conversion rates. However, personalizing the website often requires a team of web developers working with the marketing teams to make changes to the website based on the latest business logic and integrating the APIs. But with Optimizely's native integration with Customer Insights - Data, marketers are empowered to personalize the web experience for their visitors in a no-code way. 

The Optimizely integration in Customer Insights - Data allows you to share segments from Customer Insights with Optimizely. The system creates audiences in Optimizely based on the segments in Customer Insights – Data and you can use them in your web personalization campaigns or web experiments. For example, let's say you create a segment in Customer Insights - Data for 'high value customers', this segment will also show up in Optimizely - now you can add a promotional banner to the homepage that will only be displayed to the visitors that are part of the 'high value customers' segment. 

Customer Insights identifies website visitors who are members of a segment and lets you provide a personalized web experience to these visitors in real-time. You can also track user behavior for events that real-time tracking supports and specific events in Optimizely: Campaign & Experiment.

> [!TIP]
> Sign up to [request access to the preview version](https://forms.office.com/r/6NK6uj6f7f) of the real-time personalization features and [read the blog about the annoucement](https://cloudblogs.microsoft.com/dynamics365/?p=188733).

<!--video when live https://go.microsoft.com/fwlink/?linkid=2260871 -->

## Prerequisites

- Optimizely license and account for [Optimizely Web Experimentation](https://www.optimizely.com/products/experiment/web-experimentation/).
- [Customer Insights real-time tracking script](real-time-web-personalization.md) added to your website.
- [Optimizely tracking script](https://support.optimizely.com/hc/articles/4410284311565-Optimizely-Web-Experimentation-JavaScript-snippet) added to your website.
- CookieID in Optimizely set to the Customer Insights cookie ID: `_msci`.

## Connect to Optimizely

There are two ways to connect to Optimizely.

### Use the first run experience

Going through the first run experience creates a connection to Optimizely and an export that includes all segments. You can edit the export and remove segments as you prefer.

1. Go to **Real time & Personalization**.
1. Select **Advanced** and select **Setup on Optimizely**.
1. Enter a name.
1. [Provide an Optimizely API key](https://docs.developers.optimizely.com/web-experimentation/docs/personal-access-token).
1. Select **Connect**.
1. Choose your Optimizely project you want to connect to.
1. Select **Save** or **Save and Run** to finalize the setup.

You now have a connection and an export with all your segments to Optimizely set up. You can edit them like any other connection or export.

### Create the connection and export from scratch

Create a connection to Optimizely. This connection can be shared with other users in Customer Insights, and you can remove the connection at any time to discontinue the use of Optimizely.

#### Create connection

1. Go to **Connections**.
1. Select **Add connection** and choose **Optimizely**.
1. Provide a name for the connection.
1. [Provide Optimizely API key](https://docs.developers.optimizely.com/web-experimentation/docs/personal-access-token).
1. Accept the legal disclaimer and select **Save**.

#### Create an export and include the segments that you want to export to Optimizely

1. Go to **Exports**.
1. Create an export and choose the Optimizely connection you want to use. If you don't see a connection, create one or ask your administrator to create the connection and share it with you.
1. Name to your export and [provide the Optimizely Project ID](https://app.optimizely.com/v2/projects/1234567890/audiences).
1. Select **Save and Run** to export the segments to Optimizely right away, or schedule the export to run on system refresh.

## Known limitations

- In Optimizely only 100 audiences or attributes can be created per project. If you have more than 100 audiences, the exceeding amount moves to your audiences archive in Optimizely.
