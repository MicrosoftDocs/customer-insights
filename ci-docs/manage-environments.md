---
title: "Manage environments"
description: Learn how to to manage existing Customer Insights environments as an admin.
ms.date: 08/15/2022
ms.topic: how-to
ms.reviewer: mhart
author: mukeshpo
ms.author: mukeshpo
searchScope: 
  - ci-system-about
  - customerInsights
---

# Manage environments

Administrators [create](create-environment.md) and manage environments. They can change some settings in existing environments. Business, type, region, storage option, and Dataverse settings are fixed after creating the environment. If you want to change these settings, [reset the environment](#reset-an-existing-environment-preview) or [create a new environment](create-environment.md).

## Edit an existing environment

Edit details of an existing environment such as the name or setting the default environment.

1. Select the **Environment** picker in the header of the app.

1. Select the **Edit** icon.

   :::image type="content" source="media/edit-environment.png" alt-text="Icon to edit the environment settings.":::

1. In the **Edit environment** pane, update the environment settings.

1. Select **Review and finish**, then **Update** to apply the changes.

## Change the owner of an environment

Several users can have admin permissions but only one user is the owner of an environment. By default, it's the admin who creates an environment initially. As an admin of an environment, you can assign ownership to another user with admin permissions.

1. Select the **Environment** picker in the header of the app.

1. Select the **Edit** icon.

1. In the **Edit environment** pane, go to the **Basic information** step.

1. In the **Change owner of environment** field, choose the new owner of the environment.  

1. Select **Review and finish**, then **Update** to apply the changes.

## Claim ownership of an environment

If the user account of the owner is deleted or suspended, the environment won't have an owner. Any admin user can claim the ownership and become the new owner. The owner admin can continue to own the environment or [change the ownership to another admin](#change-the-owner-of-an-environment).

To claim ownership, select the **Take ownership** button that shows at the top of every page in Customer Insights when the original owner left the organization.

## Reset an existing environment (preview)

As the owner of an environment, reset an environment to an empty state if you want to delete all configurations and remove the ingested data.

1. Select the **Environment** picker in the header of the app.

1. Select the environment you want to reset and select the vertical ellipsis (&vellip;).

1. Choose **Reset (preview)**.

   :::image type="content" source="media/reset-environment.png" alt-text="Control to reset an environment.":::

1. Choose whether you want to reset the entire environment, everything except the data sources, or anything that is configured on top of the unified customer profile.

1. To confirm, enter the environment name and select **Reset**.

## Delete an existing environment

As the owner of an environment, you can delete it.

> [!IMPORTANT]
> Deleting an environment does not remove the connection to a Dataverse environment. If you plan to connect the same Dataverse environment to a new Customer Insights environment in the future, you must [remove that connection to the Dataverse environment](customer-insights-dataverse.md#remove-an-existing-connection-to-a-dataverse-environment).

1. Select the **Environment** picker in the header of the app.

1. Select the environment you want to delete and select the vertical ellipsis (&vellip;). 

1. Choose **Delete**.

   :::image type="content" source="media/delete-environment.png" alt-text="Control to delete the environment.":::

1. To confirm the deletion, enter the environment name and select **Delete**.

[!INCLUDE [footer-include](includes/footer-banner.md)]
