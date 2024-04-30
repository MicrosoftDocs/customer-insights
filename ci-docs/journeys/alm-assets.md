---
title: How to use ALM in assets library
description: Describes how to use ALM in assets library.
ms.date: 04/30/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# How to use ALM in Assets Library

Files in the Assets Library now support ALM. This means that you can create a solution, add existing files to it, and then export the solution to import it into a target organization without the risk of losing valuable data.

## Steps to use import/export feature

To utilize this feature, you need to follow these steps:

1. Navigate to the “Advanced Settings” section.
2. In the “Solutions” tab, select the option to create a new solution.
3. After creating the solution, choose “Add existing”. A dropdown will appear with all the entities that are solution aware.
4. Select “File”. A dialog will open, displaying all existing files. Choose the files you want to export and save the changes.
5. Export the newly created solution.

These steps will generate a zip folder that can be later imported into a different organization.

The imported files will be added to the target organization, and the links will point correctly to the target organization.

### Notes for emails and templates

Additionally, emails and templates already support ALM. With the latest changes, if the files referenced in those emails and templates exist in the target organization, the references after the import process will point to the target organization.

This ensures that even if you accidentally delete files in the source organization, your emails will continue to function correctly in the target organization.

To achieve this, follow this order:

1. Create a solution containing all the files referenced in your emails and templates.
2. Import the created solution into the target organization.
3. Next, create a solution with emails and templates, and import it into the target organization. This will ensure that all your emails and templates have references pointing to the correct organization.

If you didn’t follow these steps and imported a solution containing emails and templates referencing files without having the files in the target organization, nothing will happen. The references will still point to the original organization.

To rectify this, follow these steps:

1. Create a solution containing all the files referenced in your emails and templates.
2. Import the created solution into the target organization.
3. Update the solution containing emails/templates.
