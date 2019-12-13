---
uid: developers/articles/user-content
title: Control lifecyle of user content and application usage data
author: ruthaisabokhae
description: Control lifecyle of user content and application usage data
ms.author: ruthai
ms.date: 09/30/2019
ms.service: product-insights
ms.topic: conceptual
---

# How to control the lifecyle of user content and application usage data
[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

## Overview
While using Product Insights, two different kinds of user related content will eventually be created: 

1. User content directly created by a specific user such as user settings, dashboards and charts.
2. Usage data, which is collected from users as part of Product Insights’ ongoing efforts to improve the product and give you the best experience.

The following sections describe how you can manage the lifecycle of your data.

## User content
When you use Product Insights, you create several documents such as dashboards, user settings, etc. All of the content you create can be viewed, modified and deleted through the [Product Insights User Interface](https://pi.dynamics.com/).

## Usage data
As soon as you start using Product Insights, we begin gathering your usage data. This data is handled in a secure way in our backend services and sent to locked down databases with restricted access control.   

There are two main reasons we collect usage data: 

* Product improvement 
* Customer support

Most of this data has a retention of less than 30 days and will automatically be deleted after that period. You can also trigger manual deleteting/exporting of the data we gather about your usage. The steps to manually delete/export this data varies with regards to the authentication mechanism employed when logging into the Product Insights portal. In addition to that, all your personal data will be deleted once you close your Azure Active Directory (AAD) or Microsoft Service (MSA) account.

### Azure Active Directory Accounts
Only AAD tenant admins can issue export/delete requests on behalf of the organization they manage. Please contact your AAD tenant admin to assist you. If you are an AAD tenant admin, please find detailed documentation on how to create export/delete requests [here](https://docs.microsoft.com/microsoft-365/compliance/gdpr-dsr-azure).

> [!NOTE] 
> Deletion requests for usage data are triggered by deleting the associated user from the AAD tenant.

### Microsoft Accounts
Go to the [Microsoft Account Privacy Dashboard](https://account.microsoft.com/privacy/) and log into your Microsoft account if you have not done so already. This is the main portal through which you can export and delete your usage data.

#### Deletion
To delete your usage data, navigate to **Activity history** and select **Apps and services** in the **Filter by data type** dropdown on the left handside menu.
![Select Apps and services](media/PrivacyPortal_marked.png)

On the right handside of your screen, you should now see an activity log of your Microsoft account with a list of all applications that have gathered data about your account (grouped by date). Delete individual entries by clicking **Clear** next to each entry or delete all entries by clicking **Clear activity** in the upper right hand corner.
![Select Clear or Clear activity](media/PrivacyPortal_deletion_marked.png)

#### Export
To export your usage data, navigate to **Download your data** and click on **CREATE NEW ARCHIVE**.
![Create New Archive](media/MsaExport_marked.png)

In the selection screen, mark the tick box next to **App & service usage JSON** and then click **Create archive**.
![Tick App & service usage JSON](media/MsaExportSelection.png)

After a few minutes your archive will be ready and you can download it by clicking **Download** next to it.
![Download Archive](media/MsaExportDownload_marked.png)

> [!NOTE]
 > Any archives you create will expire within 7 days.

For more information regarding Microsoft's commitment towards protecting your privacy, please read the [Microsoft Privacy Statement](https://privacy.microsoft.com/).
