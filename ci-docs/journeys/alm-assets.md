---
title: How to use ALM in asset library
description: Describes how to use ALM in the asset library in Dynamics 365 Customer Insights - Journeys.
ms.date: 05/16/2024
ms.topic: how-to
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# How to use ALM in asset library

Files in the asset library now support application lifecycle management (ALM). This means that you can create a solution, add existing files to it, and then export the solution to import it into a target organization without the risk of losing valuable data.

## Steps to use import/export feature

To use this feature, you need to follow these steps:

1. Open the **Settings** menu ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") at the top of the page and select **Advanced settings**.
1. In the **Solutions** tab, select the option to create a new solution.
1. After creating the solution, choose **Add existing**. A dropdown appears with all the entities that are solution aware.
    :::image type="content" source="media/add-assets-library.png" alt-text="Add within asset library" :::
1. Select **File**. A dialog displaying all existing files. Choose the files you want to export and save the changes.
1. Export the newly created solution.

These steps generate a .zip folder that can be later imported into a different organization.

The imported files are added to the target organization and the links point correctly to the target organization.

## Notes for emails and templates

Emails and templates already support ALM. With the latest changes, if the files referenced in those emails and templates exist in the target organization, the references after the import process point to the target organization.

This feature ensures that even if you accidentally delete files in the source organization, your emails continue to function correctly in the target organization.

To enable this feature, follow these steps:

1. Create a solution containing all the files referenced in your emails and templates.
1. Import the created solution into the target organization.
1. Next, create a solution with emails and templates, and import it into the target organization. This ensures that all your emails and templates have references pointing to the correct organization.

If you didn’t follow these steps and imported a solution containing emails and templates referencing files without having the files in the target organization, nothing happens. The references still point to the original organization.

To fix this issue, follow these steps:

1. Create a solution containing all the files referenced in your emails and templates.
1. Import the created solution into the target organization.
1. Update the solution containing emails and templates.
