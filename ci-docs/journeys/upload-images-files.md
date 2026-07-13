---
title: Upload, manage, and use images, files, and videos in online content
description: Customer Insights - Journeys lets you upload images, files, and videos, manage asset details, and use stored assets in emails, forms, and pages.
ms.date: 07/09/2026
ms.update-cycle: 180-days
ms.topic: article
author: cmenesatti-m
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Upload, manage, and use images, files, and videos in online content

> [!IMPORTANT]
> Dynamics 365 Customer Insights - Journeys may transfer customer data outside of the selected Azure geographic location when using the following features that use Azure CDN (content delivery network) to operate globally:
> -	[Asset library](upload-images-files.md)
> -	[Forms](real-time-marketing-form-overview.md)
>
> You can still execute marketing campaigns without using such features by hosting your assets and forms in a content management system of your choice.
>
> Sensitive or private data, including customer relationship management (CRM) records and prefilled forms, is stored exclusively within the geographic region of the customer's environment. This data doesn't leave the region. But certain types of publicly accessible digital assets can be temporarily cached outside the region. These include:
> -	Images
> -	Files
> -	Videos
> -	HTML forms (only if they're empty and not prefilled with user data)
> 
> These assets are cached using a CDN to improve performance. For example, if a contact in the United States accesses an image hosted in a European environment, the image can be temporarily cached on a United States-based CDN server. Only assets that are publicly available through a URL (shared on a website or form) are eligible for CDN caching.

The Customer Insights - Journeys asset library stores publicly hosted images, documents, and videos that you can upload once and reuse in emails, forms, pages, and other online content. Assets must be available publicly on the internet so your content can access and display them.

> [!NOTE]
> The following file types are supported: AVI, CS, CSS, DOC, DOCX, EPUB, GIF, ICS, JPG, JPEG, MP3, MP4, MPEG, MPG, ODP, ODS, ODT, PDF, PNG, PPT, PPTX, PS, RTF, SVG, TAR, TGZ, TXT, VCF, WMV, XLS, XLSX, XML, ZIP
>
> You see an error message if you attempt to upload a file of an unsupported type.
>
> The maximum file size is:
> - 5 MB for images
> - 32 MB for documents
> - 128 MB for videos
>
> Files are stored in your organization's Microsoft Dataverse storage and count against your file storage capacity. For more information on Dataverse storage capacity, see [New Microsoft Dataverse storage capacity](/power-platform/admin/capacity-storage)

> [!TIP]
> Because files are stored in the organization's Microsoft Dataverse storage, make sure the file types you want to use aren't in the list of blocked file extensions described in [System Settings General tab - Power Platform](/power-platform/admin/system-settings-dialog-box-general-tab) or the list of [blocked MIME types](/power-platform/admin/settings-privacy-security#mime-type-validation). SVG files are in that list by default.

## Upload files

You can create a collection of images, videos, and files for later use. To upload new files, go to **Customer Insights - Journeys > Assets > Library** and select **New**.

:::image type="content" source="media/upload-new-images-from-library.png" alt-text="Screenshot of the Customer Insights - Journeys asset library with the New button selected to upload assets." lightbox="media/upload-new-images-from-library.png":::

You can manually add **tags** when you upload a file so it's easier to organize and find later. When you upload an image, AI tagging also creates additional tags that describe the image. You can always delete or add tags as needed.

## Edit assets

You can easily see and edit asset details in the side pane. Select the asset to rename, add tags and alt text, and copy the asset URL.

You can **replace** your assets with newer versions whenever needed. To replace an asset:

1. Select the image.
1. Select **Upload file** in the command bar.
1. Select a new image.
1. A new version of the asset appears in the asset library. If you open the asset, you can see the version number, but you can't view the previous versions.

> [!TIP]
> The asset library uses a [Content Delivery Network (CDN)](cdn-disabling.md) to distribute content across multiple servers. When an asset is uploaded, each CDN caches its own version for up to 30 days. If you replace an asset with a newer version, the time it takes to update varies across CDNs based on their cache refresh cycles. Because users access content from different CDNs, they may continue to see the previous asset version until the cache updates. To show the latest version consistently, we recommend uploading a new asset and updating the link in your message instead of replacing the existing asset.

## Find assets

Use the tabs to quickly switch between file categories such as images, videos, or documents. You can use the search bar at the top to search assets by name or use the filter to quickly find assets by tag.

## Use images in your content

To add an image, start by dragging an image element onto your design, which positions a placeholder. Then select the placeholder image to open the **Edit image** tab, where you can define the source, alt text, and link for the image. Select **Choose an image** > **Browse library** to find any image already uploaded to Customer Insights - Journeys.

:::image type="content" source="media/use-images-from-library.png" alt-text="Screenshot of the Edit image pane with Browse library selected to choose an uploaded image." lightbox="media/use-images-from-library.png":::

To find an image more quickly, try using the **Filter** search bar to look for specific keywords. If the image you need isn't there, select **+Upload** to add a new one.

The Copilot assistant can also identify images from your library that best complement your content, so you spend less time searching for them.

When you add an image element to your content or need to [link to a file or video](/dynamics365/marketing/real-time-marketing-email#link-to-documents-and-videos-stored-in-the-asset-library), you can choose to use a file that already exists in your Customer Insights - Journeys app library or upload a new one. After you've uploaded a file in this way, it will also be available in the library for use in other content.

> [!IMPORTANT]
> The Copilot assistant smart recommendation feature is currently in preview.

## Troubleshoot image, file, and video issues

You may encounter the following error message: `Error occurred when processing image. Reason: Create image record for solution-aware entity failed for objectid ...`

This error is expected and occurs because unmanaged customizations are blocked. To resolve the error:

1. Go to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. Select the environment experiencing the issue.
1. Go to **Settings**.
1. Select **Features**.
1. Disable the **Block unmanaged customizations** option.

## See also

[Link to documents stored in the asset library](/dynamics365/marketing/real-time-marketing-email#link-to-documents-and-videos-stored-in-the-asset-library)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
