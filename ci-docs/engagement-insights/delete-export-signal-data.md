---
title: Delete and export event data 
author: ruthaisabokhae
description: How to delete and export event data containing end user identifiable information (EUII)
ms.author: ruthai
ms.date: 08/11/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Delete and export event data

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## Background

The European Union’s General Data Protection Regulation (GDPR) that has been applied since May 25, 2018, gives significant rights to individuals with regard to their data. The GDPR is fundamentally about protecting and enabling the privacy rights of individuals. You can read more about Microsoft's commitment to security at the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

## Deleting and exporting event data containing personal identifiable information

The following sections describe how to delete and export event data that might contain end user identifiable information (EUII).

### Overview

Dynamics 365 Customer Insights engagement insights capability is committed to helping our customers meet their GDPR requirements, such as the right to delete and export data that includes personal information (like user IDs, phone numbers, and email addresses). Team administrators can implement user requests regarding the deleting or exporting of their personal data, ensuring that engagement insights capability complies with GDPR requirements.

To delete or export data:

1. Tag event properties that contain data with personal information.
2. Delete or export data associated with specific values (for example: a specified user ID).

### Tag and update event properties

EUII data is tagged on an event property level. You first need to tag the properties being considered for deletion or export.

To tag an event property as containing personal information, follow these steps:

1. Navigate to the project for the event.
  
1. Select the event you want to tag to reach the event's **Overview** page.

   ![Select event](media/SignalsOverview.png "Select event")
     
1. Select **...** and then select **Edit** to reach the **Update Property** window.

   ![Edit event](media/EditSignal.png "Edit event")

1. In the **Update Property** window, select **...** in the upper right corner, and then select the **Contains EUII** box. Select **Update** to save your changes.

   ![Save your changes](media/UpdateEvent.png "Save your changes")

   > [!NOTE]
   > Every time the event schema changes or a new event is created, it's recommended that you evaluate the associated event properties and tag or untag them as containing EUII data, if necessary.

### Delete or export tagged event data

For private preview, you can email delete requests to **[pirequest@microsoft.com](mailto:pirequest@microsoft.com)**. We are currently working on the functionality that enables you to delete tagged event data on your own. Stay tuned!

#### Good practices

* Try to avoid sending any events that contain EUII data.
* If you do need to send events containing EUII data, make sure to limit the number of events and event properties containing EUII data as much as possible. Ideally, limit yourself to one such event.
* Make sure that as few people as possible have access to the sent EUII data.
* For events containing EUII data, make sure that you set one property to emit a unique identifier that can easily be linked to a specific user (for example: a user ID). This makes it much easier to segregate data, and to export or delete the right data.
* Only tag one property per event as containing EUII data, ideally one that only contains a unique identifier.
* Do not tag properties containing verbose values (for example: an entire request body). Engagement insights capability uses exact string matching when deciding which events to delete or export.
