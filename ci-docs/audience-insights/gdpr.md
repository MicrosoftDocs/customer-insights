---
title: "Data Subject Rights (DSR) requests under GDPR | Microsoft Docs"
description: "Respond to Data Subject Requests for Dynamics 365 Customer Insights."
ms.date: 09/01/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: conceptual
author: m-hartmann
ms.author: wimohabb
manager: shellyha
---

# Data Subject Rights (DSR) requests under GDPR

The European Union’s General Data Protection Regulation (GDPR) has been in effect since May 25, 2018. It gives significant rights to individuals regarding their data. The GDPR is about protecting and enabling the privacy rights of individuals. You can read more about Microsoft's commitment to security and compliance at the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

## Overview

The “right to erasure” by the removal of personal *End User Identifiable Information (EUII)* data from an organization’s customer data is a key protection of GDPR. Removing personal data includes removing all personal data and system-generated logs, except audit log information.

> [!NOTE]
> Microsoft is committed to helping customers meet their GDPR requirements. It includes the right to delete and export data that includes personal information such as user IDs, phone numbers, and email addresses. Administrators can implement user requests to delete or export personal data.

## Audience insights

Audience insights offers the following in-product experiences to delete personal data:

- **Manage delete requests for customer data**: Customer data in Customer Insights is ingested from original data sources external to Customer Insights. All GDPR delete requests must be performed in the original data source.
- **Manage delete requests for Customer Insights user data**: Data for users is created by Customer Insights. All GDPR delete requests must be performed in Customer Insights.

### Manage delete requests for customer data

A Customer Insights admin can follow these steps to remove customer data that was deleted in the data source:

1. In **audience insights**, go to **Data** > **Data sources**
1. For each data source in the list that contains deleted customer data:
   1. Select (...) and then select **Refresh**.
   1. Check the status of the data source under **Status**. A check mark means the refresh was successful. A warning triangle means something went wrong. If a warning triangle is displayed, contact D365CI@microsoft.com.

> [!div class="mx-imgBorder"]
> ![Handling GDPR delete requests for customer data.](media/gdpr-data-sources.png "Handling GDPR delete requests for customer data")

### Manage delete requests for user data

A Customer Insights admin can follow these steps to delete Customer Insights user data:

1. In **audience insights**, go to **Admin** > **Permissions**.
1. Select the check box for the user you want to delete.
1. Select **Remove**.

> [!div class="mx-imgBorder"]
> ![Handling GDPR delete requests foruser data.](media/gdpr-permissions.png "Handling GDPR delete requests for user data")

## Engagement insights

Engagement insights offers the following in-product experiences to tag and update event properties:

- **Tag and update event properties**: Personal data that is tagged on an event property level.
- **Delete or export tagged event data**: An environment admin can issue a deletion or export request against the tagged event data.
- **Delete or export events associated with end user IDs**: Events that contain matching tagged properties will be exported in CSV format to the export destination.

### Tag and update event properties

This includes personal data that is tagged on an event property level. First, tag the properties being considered for deletion or export.

To tag an event property as containing personal information, follow these steps:

1. In **engagement insights**, open the workspace containing the event.
1. Go to **Data** > **Events** to see the list of events in the selected workspace.
1. Select the event you want to tag.
1. Select **Edit properties** to open the pane listing all properties of the selected event.
1. Select **...** and then choose **Edit** to reach the **Update property** dialog.

   ![Edit event.](media/edit-event.png "Edit event")

1. In the **Update Property** window, choose **...** in the upper right corner, and then choose the **Contains EUII** box. Choose **Update** to save your changes.

   ![Save your changes.](media/update-property.png "Save your changes")

   > [!NOTE]
   > Every time the event schema changes or you create a new event, it's recommended that you evaluate the associated event properties and tag or untag them as containing personal data, if necessary.

### Delete or export tagged event data

If all event properties have been tagged appropriately as described in the previous step, an environment admin can issue a deletion or export request against the tagged event data.

To manage EUII deletion or export requests, follow these steps:

1. In **engagement insights**, go to **Admin** > **Environment** > **Settings**.
1. In the **Manage end user identifiable information (EUII)** section, select **Manage EUII**.

### Delete events associated with end user IDs

For deletion, in engagement insights you can enter a list of comma-separated user IDs in the **Delete end user identifiable information (EUII)** section. These IDs will then be compared with all tagged event properties of all projects in the current environment via exact string matching. 

If a property value matches one of the provided IDs, the associated event will be permanently deleted. Due to the irreversibility of this action, you must confirm the deletion after selecting **Delete**.

### Export events associated with end user IDs

The export process is identical to the deletion process above when it comes to defining event property values in the **Export end user identifiable information (EUII)** section. 

Also, you'll need to provide an **Azure blob storage URL** to specify the export destination. The Azure Blob URL must include a [Shared Access Signature (SAS)](/azure/storage/common/storage-sas-overview).

After selecting **Export**, all events of the current team that contain matching tagged properties will be exported in CSV format to the export destination.

### Good practices

* Try to avoid sending any events that contain personal data.
* If you need to send events containing EUII data, limit the number of events and event properties that contain EUII data. Ideally, limit yourself to one such event.
* Make sure that as few people as possible have access to the sent personal data.
* For events containing personal data, make sure that you set one property to emit a unique identifier that can easily be linked to a specific user (for example, a user ID). This makes it easier to segregate data and to export or delete the right data.
* Only tag one property per event as containing personal data. Ideally one that only contains a unique identifier.
* Do not tag properties containing verbose values (for example, an entire request body). Engagement insights capability uses exact string matching when deciding which events to delete or export.

### Respond to GDPR data subject export requests

As part of our commitment to partner with you on your journey to the General Data Protection Regulation (GDPR), we’ve developed documentation to help you prepare. This documentation describes steps you can take today to support GDPR compliance when using Customer Insights.

#### Manage export and view requests

The right of data portability allows data subjects to request a copy of their personal data in an electronic format (a “structured, commonly used, machine readable, and interoperable format”) that can be transmitted to another data controller.

#### Export customer data (tenant admin)

A tenant administrator can follow these steps to export data:

1. Send an email to D365CI@microsoft.com specifying the customer’s email address in the request. The Customer Insights team will send an email to the registered tenant admin email address, asking for confirmation to export data.
2. Acknowledge the confirmation to export the data for the requested customer.
3. Receive the exported data through the tenant admin email address.

#### Export user data (tenant admin)

1. Send an email to D365CI@microsoft.com specifying the user’s email address in the request. The Customer Insights team will send an email to the registered tenant admin email address, asking for confirmation to export data.
2. Acknowledge the confirmation to export the data for the requested user.
3. Receive the exported data through the tenant admin email address.



[!INCLUDE[footer-include](../includes/footer-banner.md)]