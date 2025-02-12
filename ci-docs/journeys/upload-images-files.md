---
title: Upload, manage, and use images, files, and videos in online content
description: Find out how to efficiently upload, manage, and use images, files, and videos in Dynamics 365 Customer Insights - Journeys. Streamline your content creation.
ms.date: 11/22/2024
ms.topic: article
author: alfergus
ms.author: alfergus
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

Shareable assets are critical for meaningful and successful customer experiences. The files you use must be available publicly on the internet so your emails and pages can access and display them. The Dynamics 365 Customer Insights - Journeys library stores images, documents, and videos, hosting them publicly and providing an easy way to find and link to them while creating content. The library is shared across real-time and outbound marketing, making it easy to upload and use assets where you need them. 

> [!NOTE]
> The following file types are supported: AVI, CS, CSS, DOC, DOCX, EPUB,GIF, JPG, JPEG, MP3, MP4, MPEG, MPG, ODP, ODS, ODT, PDF, PNG, PPT, PPTX, PS, RTF, SVG, TAR, TGZ, TXT, WMV, XLS, XLSX, XML, ZIP
>
> You'll see an error message if you attempt to upload a file of an unsupported type.
>
> The maximum file size is:
> - 5MB for images
> - 32MB for documents
> - 128MB for videos
>
> Files are stored in your organization’s Microsoft Dataverse storage and count against your file storage capacity. For more information on Dataverse storage capacity, see [New Microsoft Dataverse storage capacity](/power-platform/admin/capacity-storage)

> [!TIP]
> As files are stored in the organization’s Microsoft Dataverse storage, ensure that the file types you want to use are not in the list of blocked files extension described at [System Settings General tab - Power Platform](/power-platform/admin/system-settings-dialog-box-general-tab) or the list of blocked MIME types described [here](/power-platform/admin/settings-privacy-security#mime-type-validation). Note that SVG files are in that list by default.  

## Upload files

You can create a collection of images, videos, and files for later use. To upload new files, go to **Customer Insights - Journeys > Assets > Library** and select **New**.

> [!div class="mx-imgBorder"]
> ![upload replace asset](media/upload-new-images-from-library.png "upload replace asset")

You can manually add **tags** when you upload a file so it’s easier to organize and find it later. Additionally, when you upload an image, AI tagging automatically creates additional tags describing your image. You can always delete or add tags as you see suitable.

## Edit assets

You can easily see and edit asset details in the side pane. Select the asset to rename, add tags and alt text, and copy the asset URL.

You can **replace** your assets with newer versions whenever needed. To replace an asset:

1. Select the image.
1. Select **Upload file** in the command bar.
1. Select a new image.
1. A new version of the asset appears in the asset library. If you open the asset, you can see the version number, but you can't view the previous versions.
> [!NOTE]
> The Asset Library utilizes a [Content Delivery Network (CDN)](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/cdn-disabling) to distribute content across multiple servers. When an asset is uploaded, each CDN caches its own version for up to 30 days. If you replace an asset with a newer version, the time it takes to update will vary across different CDNs, depending on their cache refresh cycles.
Since users access content from different CDNs, they may continue to see the previous version until the cache updates.
> To ensure the latest version is displayed consistently, we recommend uploading a new asset and updating the link in your message rather than replacing the existing asset.

## Find assets

Use the tabs to quickly switch between files categories such as images, videos, or documents. You can use the search bar at the top to search assets by name or use the filter to quickly find assets by tag.

## Use images in your content

To add an image, start by dragging an image element onto your design, which positions a placeholder. Then select the placeholder image to open the **Edit image** tab, where you can define the source, alt text, and link for the image. Select **Choose an image** > **Browse library** to find any image already uploaded to Customer Insights - Journeys.

> [!div class="mx-imgBorder"]
> ![browse images from asset library and use them](media/use-images-from-library.png "browse images from asset library and use them")

To find an image more quickly, try using the **Filter** search bar to look for specific keywords. If the image you need isn't there, select **+Upload** to add a new one.

Additionally, the Copilot assistant automatically identifies a selection of images from your library that best complement your content. Quickly and easily choose images that resonate with your audience without having to spend time searching for them.

When you add an image element to your content or need to [link to a file or video](/dynamics365/marketing/real-time-marketing-email#link-to-documents-and-videos-stored-in-the-asset-library), you can choose to use a file that already exists in your Customer Insights - Journeys app library or upload a new one. After you've uploaded a file in this way, it will also be available in the library for use in other content.

> [!IMPORTANT]
> The copilot assistant smart recommendation feature is currently in preview.

### See also

[Link to documents stored in the asset library](/dynamics365/marketing/real-time-marketing-email#link-to-documents-and-videos-stored-in-the-asset-library)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
