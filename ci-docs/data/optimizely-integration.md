---
title: No-code web personalization using Optimizely
description: Integrate Customer Insights - Data with Optimizely to personalize web experiences.
ms.date: 12/11/2023
ms.topic: how-to
author: philk
ms.author: philk
ms.reviewer: mhart
ms.custom: bap-template
---

# No-code web personalization using Optimizely

The Optimizely integration in Customer Insights - Data allows you to share segment membership information from Customer Insights with Optimizely. The system creates audiences in Optimizely based on the segments in Customer Insights – Data and you can use them in your web personalization campaigns or web experiments.

Customer Insights identifies website visitors who are members of a segment and let you provide a personalized web experience to these visitors in real-time. You can also track user behavior for events that real-time tracking supports and specific events in Optimizely: Campaign & Experiment.

## Prerequisites

- Optimizely license and account for Optimizely Web Experimentation.
- Real-time tracking script added to your website. [add link]
- Optimizely tracking script added to your website.
- CookieID in Optimizely set to the Customer Insights cookie ID: _msci.
- SetUserID to enable unknown to known flows. [Learn how to setup unknown to known user tracking](unknow-to-known.md).

<!-- is that the right link? --> 

## Connect to Optimizely

There are two ways to connect to Optimizely.

### Use the first run experience for Real-time & personalization

Going through the first run experience creates a connection to Optimizely and an export that includes all segments. You can edit the export and remove segments as you prefer.

1. Go to **Real time & Personalization**
2. Select **Advanced** and select **Setup on Optimizely**.
3. Enter a name.
4. [Provide Optimizely API key](https://docs.developers.optimizely.com/web-experimentation/docs/personal-access-token).
5. Select **Connect**.
6. Choose your Optimizely project you want to connect to.
7. Select **Save** or **Save and Run** to finalize the setup.

You now have a connection and an an export with all your segments to Optimizely set up. You can edit them like any other connection or export.

### Create the connection and export from scratch

Create a connection to Optimizely. This connection can be shared with other users in Customer Insights, and you can remove the connection at any time to discontinue the use of Optimizely.

#### Create connection

1. Go to **Connections**
1. Select **Add connection** and choose **Optimizely**.
1. Provide a name for the connection.
1. [Provide Optimizely API key](https://docs.developers.optimizely.com/web-experimentation/docs/personal-access-token).
1. Accept the legal disclaimer and select **Save**.

#### Create an export and include the segments that you want to export to Optimizely

1. Go to Exports. 
1. Create an export and choose the the Optimizely connection you want to use. If you don't see a connection, either create one or or ask your Admin to create the connection and share it with you.
1. Name to your export, and [provide the Optimizely Project ID](https://app.optimizely.com/v2/projects/1234567890/audiences).
1. Select **Save and Run** to export the segments to Optimizely right away, or schedule the export to run on system refresh.

## Example

Marketers across organizations strive to personalize the web experience of their customers. Web personalization often requires visitor tracking and knowledge about personalizing your website through APIs. Until today, organizations had to rely on web developers and designers to provide personalized omnichannel experiences to their customers.

With Customer Insights, Marketing teams can achieve that more efficiently and with minimal engagement of their web developers. Using the integration of Customer Insights – Data and Optimizely organizations can build truly personalized experiences throughout a customer journey.

## Known limitations

- In Optimizely only 100 audiences or attributes can be created per project. If you have more than 100 audiences, then the exceeding amount will be pushed to your audiences archive in Optimizely.