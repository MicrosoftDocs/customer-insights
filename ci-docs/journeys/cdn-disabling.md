---
title: Impact of disabling CDN
description: Impact of disabling CDN in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/30/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Impact of disabling CDN

Dynamics 365 Customer Insights - Journeys uses Azure CDN (content delivery network) for caching image embedded in email, as well as lead generation forms and pages outside of the selected Azure geo to ensure performance of our service.

Dynamics 365 Customer Insights - Journeys may transfer customer data outside of the selected Azure geographic location when using the following features that use Azure CDN (content delivery network) to operate globally:
- [Asset library](upload-images-files.md)
- [Forms](real-time-marketing-form-overview.md)

> [!NOTE]
> Starting February 2024, we will add a feature switch in the product that will allow you to disable using CDN.
> 
> If you decide to not use CDN, you can still execute marketing campaigns without using such features by hosting your assets and forms in a content management system of your choice.

> [!IMPORTANT]
> If you decide not to use CDN, please refer to the list below to understand the impacted product features.

## Impacted product areas if CDN is disabled

- Assets library 
    - Will not be accessible.
- Forms 
    - You can view, edit, and create new forms; however, you’ll not be able to publish them.
    - The forms will not be rendered on the web page. This applies for both forms hosted as standalone page and forms embedded in web page using Javascript.
- Emails 
    - Editing or creating emails (In Email Editor):
        - Cannot utilize assets from the assets library. 
        - Cannot upload assets to the library.
        - Cannot add forms
    - Previously created email (In Email Editor):
        - Cannot render used assets, it will show broken links.
    - Previously sent emails (In customer inbox):
        - Your customers cannot see images, they will see broken links.
        - Your customers cannot download files, videos and documents.
        - Your customers cannot access forms.
- Live journeys:

If you opt-out while having a running journey
    - Your customers will receive the emails, but will not be able to see images nor download files, videos or documents.
    - Your customers will receive the emails, but will not be able to open and interact with forms.
- Email Templates
    - Assets in any email templates will not be accessible. 
    - Cannot upload assets. 
    - Previously created templates will not render assets.
- Content blocks
    - Assets in any content block will not be accessible. 
    - Cannot upload assets. 
    - Previously created content blocks will not render assets.
- Push Notifications
    - Cannot upload images. 
    - Previously created notifications will not render images.
- Contact timeline
    - Cannot preview images in sent emails. 
    - Cannot show information about forms.
- Analytics and insights 
    - Can't show information regarding filled forms. 
    - Any data of filled forms in all product areas won't be accessible.
    - Contact insights about forms won't be accessible.
