---
title: How to use ALM in asset library
description: Learn how to use ALM in the asset library to export files in a solution and import them into another organization. Follow the steps to preserve file references.
ms.date: 11/09/2026
ms.topic: how-to
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# How to use ALM in asset library

Use ALM in the asset library to move files between organizations with solutions. Add existing files to a solution, then export and import it to preserve the files and their references.

## Export and import asset library files with ALM

To use this feature, follow these steps:

1. Open the **Settings** menu :::image type="icon" source="media/settings-icon.png" border="false"::: at the top of the page and select **Advanced settings**.
1. In the **Solutions** tab, select the option to create a new solution.
1. After creating the solution, choose **Add existing**. A dropdown appears with all the entities that are solution aware.
    :::image type="content" source="media/add-assets-library.png" alt-text="Screenshot of the Add existing options for asset library files.":::
1. Select **File**. A dialog displays all existing files. Choose the files you want to export and save the changes.
1. Export the newly created solution.

These steps generate a .zip folder that you can later import into a different organization.

The imported files are added to the target organization and the links point correctly to the target organization.

## Preserve file references in emails and templates

Emails and templates already support ALM. If the files referenced in those emails and templates exist in the target organization, the references after the import process point to the target organization.

This feature ensures that even if you accidentally delete files in the source organization, your emails continue to function correctly in the target organization.

To enable this feature, follow these steps:

1. Create a solution containing all the files referenced in your emails and templates.
1. Import the created solution into the target organization.
1. Next, create a solution with emails and templates, and import it into the target organization. This step ensures that all your emails and templates have references pointing to the correct organization.

If you didn't follow these steps and imported a solution containing emails and templates referencing files without having the files in the target organization, nothing happens. The references still point to the original organization.

To fix this issue, follow these steps:

1. Create a solution containing all the files referenced in your emails and templates.
1. Import the created solution into the target organization.
1. Update the solution containing emails and templates.
