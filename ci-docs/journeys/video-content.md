---
title: Create a video library and add videos to your designs
description: How to set up a video library and add those videos to marketing emails and pages in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/23/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Create a video library and add videos to your designs

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Use Dynamics 365 Customer Insights - Journeys to store information about each of the videos that you use in your marketing initiatives and then include those videos in your emails and pages by adding a video design element that references a video from your video library.

For each video you add to your library, you'll specify a name, video URL, embed code, and thumbnail URL. The library won't contain the video itself, just these references to it, so you'll need to host your video somewhere else, such as on one of the major video platforms like YouTube or Vimeo.

When you add a video to one of your designs, the designer will automatically use the settings it needs for the type of design you are creating. For pages, the designer will embed the video, so visitors can play it without leaving the page. Most email clients don't support embedded videos, so for emails the designer will embed the thumbnail image and link it to the video URL so contacts can select the thumbnail to open the video in a new browser tab.

## Add a video to your library

To add a video to your library in Customer Insights - Journeys:

1. Go to **Outbound marketing** > **Marketing content** > **Videos** to open a page that shows a list of all videos already in your library.

1. Select a listed video to edit it or select **New** on the command bar to create a new one.

1. The **Video** form opens. Make the following settings:

    - **Name**: Assign a name to the video that will make it easy for you and other users to recognize.
    - **Owner**: This is the user who owns this video record, which can sometimes affect who can view and/or edit it. It defaults to the user who creates the record.
    - **Video URL**: Specify the URL that will open the video in a browser. This link will be used to link to the video from its thumbnail image when you use it in an email message.
    - **Video thumbnail URL**: Specify the URL of a still image that represents the video. This image will be embedded and linked to the video URL when you place the video in an email design. Most video hosting platforms make this URL available publicly&mdash;see the documentation for your video hosting service if you don't know how to find it. You could instead create your own thumbnails and host them in your [Dynamics 365 Customer Insights - Journeys files library](upload-images-files.md) or elsewhere if you prefer.
    - **Video embed URL**: Specify the code required to embed the image on a web page. This code will be used when you place the video on a marketing page so visitors can watch it right there without leaving the page. Most video hosting platforms will provide this code for you&mdash;see the documentation for your video hosting service if you don't know how to find it.

1. Select **Save** in the toolbar to save your work.

## View, delete, or edit your videos

To work with your existing videos, go to **Outbound marketing** > **Marketing content** > **Videos**. This opens a standard list view, where you can create, edit, or delete videos using check boxes and buttons in the command bar. Select any listed video to view or edit it. The settings here are the same as those described in the previous section.

## Use a video in a design

To add a video from your video library to the design of a marketing email or marketing page:

1. Open or create an [email message](email-design.md) or [marketing page](create-deploy-marketing-pages.md).
2. Drag a video element from the **Elements** panel to the appropriate location in your design.
3. Select the new video element. In the **Edit video** panel, select **Choose a video** to find and select the video from your library that you want to include here. Alternatively, you can insert a video from a URL. To improve accessibility, you can add an alt text description for the video.
4. Continue working with your design and eventually go live when you are ready to start using it.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
