---
title: Purchase a license directly from a trial
description: Learn how to a license to purchase a paid license directly within a Dynamics 365 Customer Insights trial.
ms.date: 07/23/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Purchase a license directly from a trial

You can now purchase a Dynamics 365 Customer Insights license directly from a trial. Tenant admins can directly purchase the Customer Insights environment SKUs (Dynamics 365 Customer Insights App or Dynamics 365 Customer Insights Attach) and convert the trial environment to a paid environment in one streamlined workflow.

This article explains who can purchase a license within the app, how they can purchase a license, and what happens after the purchase.

## Who can purchase a license from a trial?

From a trial, only tenant admins can enter the direct purchase flow.

## Purchase a license within a trial

To purchase a license within a Customer Insights trial, select **Buy Now** from the information banner at the top of the screen in your trial.

A modal window opens and shows you the appropriate license for your tenant based on existing licenses that are on the tenant. You see one of the following options:

- **Dynamics 365 Customer Insights license**: Entitles you to four application installs of Customer Insights - Journeys and four of Customer Insights - Data, 10,000 interacted people, and 100,000 unified people. You see this option if your company’s tenant has no pre-existing Dynamics 365 licenses.
- **Dynamics 365 Customer Insights Attach**: This is a discounted price Dynamics 365 Customer Insights license if your company’s tenant has a pre-existing Dynamics 365 license (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Supply Chain Management, Dynamics 365 Finance, Dynamics 365 Commerce).

> [!NOTE]
> The license shown depends on whether you already have another qualifying Dynamics 365 app with 10 or more users. For more information, see [Dynamics 365 Customer Insights licensing overview](marketing-license.md).

Next, enter your purchase information to finalize the transaction.

## What happens after the purchase

After the system processes your purchase, it returns to the trial page and informs you that your license is ready to activate. You have two options:

- To convert the existing trial environment to a paid instance using any available license on the tenant, select the **Activate** button.
- To create a new environment to apply the license to or to apply the license to an existing Dynamics 365 environment with other apps already installed, select the **Learn more** link.

> [!NOTE]
> If you don't have the required administrator user privileges to activate a license in the current environment, the system shows you a window that informs you that the license is ready to activate and to contact the system admin for the environment. To apply the license, the app administrator must assign you app admin rights or they can also activate the trial and apply the license. For more information, see [Manage user accounts, user licenses, and security roles](admin-users-licenses-roles.md).
>
> Alternatively, you can activate the license on a separate environment you create on which you are the app admin. For more information, see [Create and manage environments in the Power Platform admin center](/power-platform/admin/create-environment).

After you activate the license, your trial environment changes to a full production environment. This change means that the system moves the database environment to a production scale group and makes some other optimizations. This process can take 20 to 30 minutes to complete. The app might experience some downtime while the upgrade is in progress.

> [!IMPORTANT]
> - Your new Customer Insights license appears on your tenant instantly, but it can take up to 24 hours to replicate in the Power Platform admin center. 
> - Additionally, you experience some Customer Insights app downtime while your trial app is being upgraded. The downtime can last from 15 minutes to an hour.

## Manage your subscription

Go to the [Power Platform admin center](https://admin.microsoft.com/) to manage your subscription, limit, and control the purchase experience. Management capabilities depend on whether you have an administrator or user role.

In the admin center, *tenant admins* can:
- Disable purchase by product ID of any product.
- View all departmental purchases made in the organization.
- Cancel any departmental purchase and (optionally) move assigned users to an organization purchase.

For more information, see [Manage self-service purchases (Admin)](/microsoft-365/commerce/subscriptions/manage-self-service-purchases-admins).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
