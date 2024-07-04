---
title: How to use ALM in asset library
description: Describes how to use ALM in the asset library in Dynamics 365 Customer Insights - Journeys.
ms.date: 07/04/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

## Move Digital Assets between environments

When you use multiple Dynamics 365 environments for your application lifecycle management, you want to ensure that you are migrating your production ready digital assets between environments so your team can utilize them in your content.

You can now move digital assets between environments. Once you move your digital assets, all their references will be pointing to the target environment and your team can immediately use them.

You can learn more about the copy and restore of environments as it’s described in [Copy or restore environments - Dynamics 365 Customer Insights | Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/copy-or-restore#copy-a-customer-insights---journeys-environment-to-another-environment)

## Import/Export of Digital Assets files

To export/import DA, follow these steps

### Step 1: Prepare and export your files

1. In your source Customer Insights – Journeys application, click on the settings gear on the top right corner.
1. Click on Advanced Settings, a Power App page will open
1. Click on Solutions and select New solution
     Choose a Name, select a publisher, and then click Create
1. After creating a new solution. Click on Add existing -> more -> other -> file 
     This will open all the files you have in your Digital Assets library
1. Select the files you want to export and click Add
1. Go back to Solutions, select the solution that you created and click Export solution
1. Click on Publish. This will take few minutes.
    Once completed, click Next.

1. Select Managed solution, then click Export.  Managed solutions are ALM best practice and must be utilized for exporting. To learn more refer to this [Solution concepts - Power Platform | Microsoft Learn](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions)
1. Click on Download in the pop up to download your files.

### Step 2: Import your files to the target environment

You will have to use the download zip folder to import it to the new environment.

1. Go to your target Customer Insights – Journeys environment
1. Click on Advanced settings
1. Click on Solutions
1. click on Import solution
1. Browse and select the download zip file, then click Next
1. Click import After import is completed. You should be able to see all your selected digital assets with their URLs referencing to the target environment.

## Import/export emails that have Digital Assets

If you want to export emails that have references to Digital Assets files from one environment to another, and you want to have the links pointing to the new org, it’s important that you:

1. First import/export of Digital Assets files to target environment (steps above).
1. Then, similarly you have to export another solution from the source environment for emails and then import it to the new environment. During the import, all links within emails will refer to the target environment that you’re using. We’ll only update the reference of the files that already exist in the target environment.

If you export and then import a solution for emails without first export/import a solution for Digital Assets files, all the links in your Emails will be referring to the source environment. If you want to remediate that:

1. You must do steps 1 and 2 for digital assets files import/export,
1. Update the version of the solution for emails.
1. Import the solution for emails again.

Note, Digital Asset ALM support for content blocks is not yet supported, and it will be part of the July 2024 release.

## FAQ

1. Can I add files and emails to the same solution and will that update the URLs of the files in the email? No. You have first to move the Digital Asset files then the email.
1. Given that DAs are a dependency on files, would the DAs automatically be added to the solution if I add the email to the solution?  No. Moving emails that have Digital Assets will not move the Digital Assets files. It’s important to move first the Digital Asset files then the emails.
1. Can I delete Digital Assets from source environment after migration? It’s not possible to delete files from managed solutions. The reason is to ensure that your solution doesn’t have references to the deleted assets that will leave you with orphan dependency (e.g., emails that has a reference to digital asset). For that, if you wish to delete digital assets, you have to delete the managed solution.
