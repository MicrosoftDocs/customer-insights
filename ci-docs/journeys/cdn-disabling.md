---
title: Impact of disabling CDN
description: Impact of disabling CDN in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/04/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Impact of disabling CDN

To ensure optimal performance, Dynamics 365 Customer Insights - Journeys uses Azure CDN (content delivery network) to cache images embedded in email, lead generation forms, and pages outside of the selected Azure geo. Customer Insights - Journeys may transfer customer data outside of the selected Azure geographic location when using the following features that use Azure CDN to operate globally:
- [Asset library](upload-images-files.md)
- [Forms](real-time-marketing-form-overview.md)

> [!NOTE]
> Starting February 2024, a feature switch will be added that will allow you to disable using the CDN.
> 
> If you decide to not use the CDN, you can still execute marketing campaigns without using such features by hosting your assets and forms in a content management system of your choice.

> [!IMPORTANT]
> If you decide not to use the CDN, refer to the list below to understand the impacted features.

## Impacted feature areas if the CDN is disabled

### Assets library
- Won't be accessible.

### Forms
- You can view, edit, and create new forms; however, you won't be able to publish them.
- The forms won't be rendered on the web page. This applies to forms hosted as standalone pages and forms embedded in web pages using JavaScript.

### Emails
- Editing or creating emails (in the email editor):
    - Can't utilize assets from the asset library.
    - Can't upload assets to the library.
    - Can't add forms.
- Previously created emails (in the email editor):
    - Can't render used assets; used assets show broken links.
- Previously sent emails (in customer inboxes):
    - Customers can't see images, they'll see broken links.
    - Customers can't download files, videos, or documents.
    - Customers can't access forms.

### Live journeys
If you opt out while a journey is running:
- Your customers will receive the emails, but won't be able to see images or download files, videos, or documents.
- Your customers will receive the emails, but won't be able to open and interact with forms.

### Email templates
- Assets in any email templates won't be accessible. 
- Can't upload assets.
- Previously created templates won't render assets.

### Content blocks
- Assets in any content block won't be accessible. 
- Can't upload assets.
- Previously created content blocks won't render assets.

### Push notifications
- Can't upload images. 
- Previously created notifications won't render images.

### Contact timeline
- Can't preview images in sent emails. 
- Can't show information about forms.

### Analytics and insights 
- Can't show information regarding filled forms. 
- Any data of filled forms in all product areas won't be accessible.
- Contact insights about forms won't be accessible.
