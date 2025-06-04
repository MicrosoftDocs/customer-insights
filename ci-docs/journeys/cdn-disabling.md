---
title: Impact of disabling Azure CDN
description: Impact of disabling Azure CDN in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/04/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Impact of disabling Azure CDN

To ensure optimal performance, Customer Insights - Journeys uses Azure Content Delivery Network (CDN) to cache images embedded in email, lead generation forms, and pages. Customer Insights - Journeys may transfer customer data outside of the selected Azure geographic location when using the following features that utilize Azure CDN:
- [Asset library](upload-images-files.md)
- [Forms](real-time-marketing-form-overview.md)

Sensitive or private data, including CRM records and prefilled forms, are stored exclusively within the geographic region of the customer's environment. This data doesn't leave the region. However, certain types of publicly accessible digital assets may be temporarily cached outside the region. These include:
-	Images
-	Files
-	Videos
-	HTML forms (only if they're empty and not prefilled with user data)

These assets are cached using a CDN to improve performance. For example, if a contact in the United States accesses an image hosted in a European environment, the image may be temporarily cached on a United States-based CDN server.

If you decide not to use Azure CDN, you can still execute marketing campaigns by hosting assets and forms in a content management system (CMS) of your choice. You should be aware, however, that the [functionality listed below](cdn-disabling.md#impacted-feature-areas-if-azure-cdn-is-disabled) is impacted if you disable Azure CDN.

> [!NOTE]
> A feature switch allows you to disable Azure CDN.

## Impacted feature areas if Azure CDN is disabled

### Assets library
- Not accessible.

### Forms
- You can view, edit, and create new forms but you can't publish them.
- The forms can't render on the webpage. This applies to forms hosted as standalone pages and forms embedded in webpages using JavaScript.

### Editing or creating emails (in the email editor):
- Can't utilize assets from the asset library.
- Can't upload assets to the library.
- Can't add forms.

### Previously created emails (in the email editor):
- Can't render assets, assets show as broken links.

### Previously sent emails (in customer inboxes):
- Customers can't see images, they see broken links.
- Customers can't download files, videos, or documents.
- Customers can't access forms.

### Email templates
- Assets in any email templates won't be accessible. 
- Can't upload assets.
- Previously created templates won't render assets.

### Live journeys
If you opt out while a journey is running:
- Your customers receive the emails, but can't see images or download files, videos, or documents.
- Your customers receive the emails, but can't open and interact with forms.

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
