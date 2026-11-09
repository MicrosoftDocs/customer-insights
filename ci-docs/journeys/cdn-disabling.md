---
title: Impact of disabling Azure CDN
description: Learn how disabling Azure CDN affects assets, forms, emails, and live journeys in Customer Insights - Journeys. Review the impact before opting out.
ms.date: 11/09/2026
ms.topic: article
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Impact of disabling Azure CDN

Disabling Azure CDN affects images embedded in Customer Insights - Journeys emails, lead generation forms, and pages. Azure Content Delivery Network (CDN) caches these images to improve performance. Customer Insights - Journeys can transfer customer data outside the selected Azure geographic location when you use the following features that use Azure CDN:
- [Asset library](upload-images-files.md)
- [Forms](real-time-marketing-form-overview.md)

Sensitive or private data, including CRM records and prefilled forms, is stored exclusively within the geographic region of the customer's environment. This data doesn't leave the region. But certain types of publicly accessible digital assets can be temporarily cached outside the region. These assets include:
-	Images
-	Files
-	Videos
-	HTML forms (only if they're empty and not prefilled with user data)

The system caches these assets by using a CDN to improve performance. For example, if a contact in the United States accesses an image hosted in a European environment, the image can be temporarily cached on a United States-based CDN server.

If you decide not to use Azure CDN, you can still run marketing campaigns by hosting assets and forms in a content management system (CMS) of your choice. However, the following functionality is affected if you disable Azure CDN: [Impacted feature areas](cdn-disabling.md#impacted-feature-areas-if-azure-cdn-is-disabled).

> [!NOTE]
> A feature switch lets you disable Azure CDN.

## Impacted feature areas if Azure CDN is disabled

### Assets library
- You can't access the assets library.

### Forms
- You can view, edit, and create new forms, but you can't publish them.
- Forms don't render on the webpage. This restriction applies to forms hosted as standalone pages and forms embedded in webpages by using JavaScript.

### Email creation and editing in the email editor
- You can't use assets from the asset library.
- You can't upload assets to the library.
- You can't add forms.

### Previously created emails (in the email editor)
- Assets don't render; they show as broken links.

### Previously sent emails (in customer inboxes)
- Customers can't see images; they see broken links.
- Customers can't download files, videos, or documents.
- Customers can't use forms.

### Email templates
- Assets in any email template aren't accessible.
- You can't upload assets.
- Previously created templates don't render assets.

### Live journeys
If you opt out while a journey is running:
- Customers receive the emails, but can't see images or download files, videos, or documents.
- Customers receive the emails, but can't open or interact with forms.

### Content blocks
- Assets in any content block aren't accessible.
- You can't upload assets.
- Previously created content blocks don't render assets.

### Push notifications
- You can't upload images.
- Previously created notifications don't render images.

### Contact timeline
- You can't preview images in sent emails.
- You can't show information about forms.

### Analytics and insights
- You can't show information about filled forms.
- You can't access data from filled forms in all product areas.
- You can't access contact insights about forms.
