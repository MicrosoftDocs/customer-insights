---
title: Application lifecycle management for digital assets
description: Describes how to use an application lifecycle management (ALM) for digital assets in Dynamics 365 Customer Insights - Journeys.
ms.date: 07/24/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Application lifecycle management for digital assets

Read this article to learn how to use application lifecycle management (ALM) for digital assets.

## Move digital assets between environments

When you use multiple Dynamics 365 environments for your application lifecycle management, ensure that you're migrating your production-ready digital assets between environments so your team can utilize them in your content.

You can learn more about copying and restoring environments in the [Copy or restore environments](/dynamics365/customer-insights/journeys/copy-or-restore#copy-a-customer-insights---journeys-environment-to-another-environment) article.

## Importing/exporting digital asset files

To import or export digital assets, follow these steps:

### Step 1: Prepare and export your files

1. In your source Customer Insights application, select the **Settings** gear in the top right corner.
1. Select **Advanced settings**, a **Power App** page opens.
    :::image type="content" source="media/alm-power-page.png" alt-text="Power app page." lightbox="media/alm-power-page.png":::
1. Select **Solutions** then select **New solution**.
    :::image type="content" source="media/alm-new-solution.png" alt-text="New solution within Power App." lightbox="media/alm-new-solution.png":::
    Choose a **Name**, select a **Publisher**, and then select **Create**.
1. After creating a new solution, go to **Add existing** > **More** > **Other** > **File**.  
    :::image type="content" source="media/alm-add-existing.png" alt-text="Other file for exporting digital assets." lightbox="media/alm-add-existing.png":::
    This opens all the files you have in your digital assets library.
1. Select the files you want to export and select **Add**.
1. Go back to **Solutions**, select the solution that you created, and select **Export solution**.
1. Select **Publish**.  
    :::image type="content" source="media/alm-publish.png" alt-text="Publish solution." lightbox="media/alm-publish.png":::
1. Once completed, select **Next**.
1. Select **Managed solution**, then select **Export**. Managed solutions are an ALM best practice and must be utilized for exporting. To learn more, see [Solution concepts](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions).
    :::image type="content" source="media/alm-export.png" alt-text="Export solution." lightbox="media/alm-export.png":::
1. To download your files, select **Download** in the pop-up.  
    :::image type="content" source="media/alm-download.png" alt-text="Download solution." lightbox="media/alm-download.png":::

### Step 2: Import your digital asset files to the target environment

You need to download a zip folder to import your digital asset files to the new environment.

1. Go to your target Customer Insights environment.
1. Select the **Settings** gear in the top right corner then select **Advanced settings**.
1. Select **Solutions**.
1. Select **Import solution**.  
    :::image type="content" source="media/alm-import.png" alt-text="Import solution." lightbox="media/alm-import.png":::
1. Select **Browse** and select the downloaded zip file, then select **Next**.
1. Select **Import**. After the import is completed, you can see all your selected digital assets with their URLs referencing the target environment.

## Import/export emails that have digital assets

If you want to export emails that have references to digital assets files from one environment to another and you want to have the links pointing to the new org, follow these steps:

1. First, import/export your digital assets files to the target environment.
1. Next, export another solution from the source environment for emails.
1. Import the solution to the new environment. During the import, all links within emails refer to the target environment that you’re using. We’ll update the reference of the files that already exist in the target environment.

If you export and then import a solution for emails without first exporting or importing a solution for digital assets files, all the links in your emails refer to the source environment. To fix the links:

1. Go to your target Customer Insights environment.
1. Select the **Settings** gear in the top right corner then select **Advanced settings**.
1. Select **Solutions**.
1. Update the version of the solution for emails.
1. Import the solution for emails again.

## FAQ

- *Can I add files and emails to the same solution and will that update the URLs of the files in the email?*
    
    No. You have first to move the digital asset files then the email.

- *Given that digital assets are a dependency on files, would the digital assets automatically be added to the solution if I add the email to the solution?*
    
    No. Moving emails that have digital assets won't move the digital assets files. It’s important to move first the digital asset files then the emails.

- *Can I delete digital assets from the source environment after migration?*
    
    It’s not possible to delete files from managed solutions. The reason is to ensure that your solution doesn’t have references to the deleted assets that leave you with orphan dependency. For example, emails that have a reference to digital asset. If you wish to delete digital assets, you have to delete the managed solution.

[!INCLUDE [footer-include](./includes/footer-banner.md)]