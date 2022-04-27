---
title: "Manage users in the consent management capability"
description: "All users in an org that owns consent management can get access to the service. Admins add users and assign them the required permissions in Customer Insights."
ms.date: 04/27/2022

ms.subservice: consent-management
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Manage users and permissions

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

All administrators of audience insights have access to the consent management capability. They can add and remove other users and assign them the required permissions.

## Roles

- Reader
    - Is a view-only role that can see which consent data is imported and its associated summary analytics on the home page.

- Contributor
    - Can configure import of consent data.
    - Can configure consent rules.

- Admin: 
    - Has all permissions of the Contributor role.
    - Can set system settings.
    - Can manage users and permissions.
    - The first admin who enables the consent management capability in Customer Insights gets the Admin (Owner) role. This user can't be removed from the system.

## Add users

1. In Consent Center (preview), go to **Admin** > **Permissions**.
1. Select **Add users**
1. In the **Add users** pane, choose the **Role** and users to add. 
1. Select **Grant access**. 

## Remove users

1. In Consent Center (preview), go to **Admin** > **Permissions**.
1. Select the user you want to remove in the list.
1. Select **More options (...)** and choose **Remove user**
1. Confirm the removal to revoke access to the users.

## Change roles

1. In Consent Center (preview), go to **Admin** > **Permissions**.
1. Select the user you want to remove in the list.
1. Select **More options (...)** and choose **Remove user**
