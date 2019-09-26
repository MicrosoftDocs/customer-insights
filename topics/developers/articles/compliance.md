---
uid: developers/articles/compliance
title: Compliance
author: ruthaisabokhae
description: Compliance
ms.author: ruthai
ms.date: 09/23/2019
ms.service: product-insights
ms.topic: conceptual
---

# GDPR/ Compliance 

## Background
The European Union’s General Data Protection Regulation (GDPR) that has been applied since May 25, 2018, gives significant rights to individuals with regards to their data. The GDPR is fundamentally about protecting and enabling the privacy rights of individuals. You can read more about the Microsoft commitment to security at the Microsoft Trust Center.

## Deleting and exporting signal data containing personal identifiable information (PII)
The following sections describe how to delete and export signal data that may contain PII.

### Overview
Dynamics 365 Product Insights is committed to helping our customers meet their GDPR requirements, such as the right to delete and export data that includes PII like user IDs, phone numbers, email addresses, etc. Team administrators are enabled to execute user requests regarding deleting or exporting their data, ensuring that Product Insights complies with GDPR requirements.
There is a two-step process to delete or export data:
1.	Tag signal properties that contain PII data.
2.	Delete/Export data associated with specific PII values (for example: a specific user ID).

### Tag signal properties
PII data is tagged on a **Signal property** level; therefore, it is necessary to first tag the signal properties being considered for deletion and export. 
To tag a signal property as containing PII, follow these steps.
1.	Navigate to the project that the signal belongs to.

![Project overview screenshot](ProjectOverview.PNG)
  
2.	Click on the signal you want to tag to get to the signal overview page.

[Insert screenshot: SignalOverview.png]
  

3.	Click on [...] and then edit to get to the **Update Property** window.

[Insert screenshot: SignalSettings.png]
 
4.	Inside the **Update Property** window, click on [...] in the upper right corner, and select the box “Contains PII." Click **Update** to save your changes.

[Insert screenshot: SignalTagging.png]

 > [!NOTE]
 > Every time the signal schema changes or a new signal is being created, it is recommended to evaluate the associated signal properties and tag/untag them as containing PII data, if necessary.

### Delete/Export tagged signal data
If all signal properties have been tagged appropriately as described in the previous step, a team administrator is then able to issue deletion requests against the tagged signal data from the **Team settings** page.

[Insert screenshot: TeamOverview.png]
 
#### Deletion
For deletion, you can enter a list of comma-separated values in the **Delete PII for the user IDs specified** box. These properties will then be compared with all tagged signal properties of all projects underneath the current team via exact string matching. 

[Insert screenshot: Deletion.png]
 
If a property value matches one of the provided values, then the associated signal will be permanently deleted. Due to the irreversibility of this action, you must confirm the deletion after clicking the delete button.

[Insert screenshot: ConfirmDeletion.png]
 
#### Export
The export process is identical to the deletion process when it comes to defining the signal property values in the **Export all PII contained in this team for user IDs specified** box. Additionally, it is necessary to provide an Azure Blob URL to specify the export destination. The Azure Blob URL also has to include a [Shared Access Signature (SAS)](https://docs.microsoft.com/azure/storage/common/storage-sas-overview) as part of the URL.

[Insert screenshot: Export.png]
 
After clicking **Export**, all signals of the current team that contain matching tagged properties will be exported in CSV format to the destination Blob.

##### Good Practices
* Avoid sending any signals that contain PII data.
* If you do need to send signals containing PII data, make sure to limit the number of signals and signal properties containing PII data as much as possible. Ideally, stick to only one signal that sends PII data.
* Make sure that as few people as possible have access to the sent PII data.
* For signals containing PII data, make sure that you set one property to emit a unique identifier that can easily be linked to a specific user (for example: a user ID). This makes it much easier to segregate data and export/delete the right data.
* Only tag one property per signal as containing PII data, ideally one that only contains a unique identifier
* Do not tag properties containing verbose values (for example: an entire request body). Product Insights uses exact string matching when deciding which signals to delete/export.

