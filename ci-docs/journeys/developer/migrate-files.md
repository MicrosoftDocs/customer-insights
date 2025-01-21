---
title: Limitations on migrating files between outbound marketing environments
description: Learn about limitations on migrating files between outbound marketing environments and possible workarounds.
ms.date: 11/16/2023
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing
---

# Limitations on migrating files between outbound marketing environments

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](../transition-overview.md)

Out of the box, Dynamics 365 Customer Insights - Journeys doesn't provide tools to migrate files between environments. Any such tool would need to be built by a customer or partner and would revolve around calling Microsoft Dataverse APIs.

On a high level, the tool would fetch files from the source environment, download the metadata and content for each file, and then create the file in the target environment. On the source environment, metadata for files are stored in the **msdyncrm_file** entity. The **msdyncrm_blobcdnuri** field contains a URL to the file content.

> [!WARNING]
> The Customer Insights - Journeys app doesn't currently support migration between different tenant geographic locations (geo to geo). To install Customer Insights - Journeys again on the org in the target geo, you must have uninstalled Customer Insights - Journeys on the source geo before the geo migration. Be aware that when you uninstall Customer Insights - Journeys on the source geo, you lose all Marketing Services data.

## An example flow to clone files (digital assets) in Customer Insights - Journeys

> [!IMPORTANT]
> The following steps are a guideline on manually creating a flow to clone files in Dynamics 365 Customer Insights - Journeys. Implementation may vary based on the framework and language you are using.

The flow should start with a call to the **msdyncrm_UpsertFile** custom action using the following parameters:
- **InputFile**: String with a serialized JSON object with the following properties:
    - **msdyncrm_name**: Image (file) name
    - **msdyncrm_contenttype**: Content type
    - **msdyncrm_width**: Image width, in pixels
    - **msdyncrm_height**: Image height, in pixels

- **InputKeywords**: String with serialized JSON array with keywords. Each keyword is represented by the following JSON object:
    - **id**: Keyword record identifier (GUID)
    - **entityType**: Always "msdyncrm_keyword"
    - **name**: Value of the keyword

- The call returns properties required for uploading the file content. Of particular note:
    - **msdyncrm_bloburi**: URI to upload the content to
    - **msdyncrm_sastoken**: SAS token used for the upload (can be an empty string)
    - **msdyncrm_fileid**: ID of the newly created msdyncrm_file record

- A PUT call is made to an endpoint provided by **msdyncrm_bloburi** with the file content.

- After the upload is completed, an update to the **msdyncrm_file** record is performed to update **msdyncrm_rethumbnail** property to "true".

> [!NOTE]
> If you copy Customer Insights - Journeys emails from one environment to another and have images from the old environment in the emails, the images will be point to old environment CDN. This means that if you decide to uninstall Customer Insights - Journeys from the old environment or remove the files, the emails in the new environment will have broken images.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
