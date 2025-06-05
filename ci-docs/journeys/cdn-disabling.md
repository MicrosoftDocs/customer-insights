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

To ensure optimal performance, Customer Insights - Journeys uses Azure Content Delivery Network (CDN) to cache images embedded in email, lead generation forms, and pages. Customer Insights - Journeys can transfer customer data outside the selected Azure geographic location when you use the following features that use Azure CDN:
- [Asset library](upload-images-files.md)
- [Forms](real-time-marketing-form-overview.md)

Sensitive or private data, including CRM records and prefilled forms, is stored exclusively within the geographic region of the customer's environment. This data doesn't leave the region. But certain types of publicly accessible digital assets can be temporarily cached outside the region. These include:
-	Images
-	Files
-	Videos
-	HTML forms (only if they're empty and not prefilled with user data)

These assets are cached using a CDN to improve performance. For example, if a contact in the United States accesses an image hosted in a European environment, the image can be temporarily cached on a United States-based CDN server.

If you decide not to use Azure CDN, you can still run marketing campaigns by hosting assets and forms in a content management system (CMS) of your choice. However, the [functionality listed below](cdn-disabling.md#impacted-feature-areas-if-azure-cdn-is-disabled) is affected if you disable Azure CDN.

> [!NOTE]
> A feature switch lets you disable Azure CDN.

## Impacted feature areas if Azure CDN is disabled

### Assets library
- Can't access the assets library.

### Forms
- View, edit, and create new forms, but you can't publish them.
- Forms don't render on the webpage. This applies to forms hosted as standalone pages and forms embedded in webpages using JavaScript.

### Editing or creating emails (in the email editor)
- Can't use assets from the asset library.
- Can't upload assets to the library.
- Can't add forms.

### Previously created emails (in the email editor)
- Assets don't render; they show as broken links.

### Previously sent emails (in customer inboxes)
- Customers can't see images; they see broken links.
- Customers can't download files, videos, or documents.
- Customers can't use forms.

### Email templates
- Assets in any email template aren't accessible.
- Can't upload assets.
- Previously created templates don't render assets.

### Live journeys
If you opt out while a journey is running:
- Customers receive the emails, but can't see images or download files, videos, or documents.
- Customers receive the emails, but can't open or interact with forms.

### Content blocks
- Assets in any content block aren't accessible.
- Can't upload assets.
- Previously created content blocks don't render assets.

### Push notifications
- Can't upload images.
- Previously created notifications don't render images.

### Contact timeline
- Can't preview images in sent emails. 
- Can't show information about forms.

### Analytics and insights
- Can't show information about filled forms.
- Data from filled forms in all product areas isn't accessible.
- Contact insights about forms aren't accessible.
