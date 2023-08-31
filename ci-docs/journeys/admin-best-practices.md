---
title: Best practices for administration
description: Learn about best practices for Dynamics 365 Customer Insights - Journeys administration and management.
ms.date: 08/22/2022
ms.custom:
  - dyn365-admin
  - dyn365-marketing
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Best practices for administration

[!INCLUDE[consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

Dynamics 365 Customer Insights - Journeys is a marketing-automation app that helps turn prospects into business relationships. The app is easy to use, works seamlessly with Dynamics 365 Sales, and has built-in business intelligence.

Customer Insights - Journeys is built on top of the Dynamics 365 platform. Environment-management operations are a standard feature of model-driven Dynamics 365 apps (Sales, Customer Service, Field Service, Customer Insights - Journeys, and Project Service Automation). Customer Insights - Journeys, however, has additional considerations to keep in mind.

This document discusses some of the key elements for managing Customer Insights - Journeys, focusing on the most common areas in which administrators have questions.

## Licensing model

Dynamics 365 Customer Insights - Journeys has a different licensing model than other Dynamics 365 applications. You can find more details about the Customer Insights - Journeys licensing model in [How to purchase](purchase.md#how-to-purchase-dynamics-365-marketing) and [Customer Insights - Journeys contacts purchase](setup-troubleshooting.yml#how-is-customer-insights---journeys-licensed-), as well as in the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544&clcid=0x409). Some important aspects of Customer Insights - Journeys’s licensing model are:

- You don't purchase user licenses of Customer Insights - Journeys. You purchase the Customer Insights - Journeys app and bundles of marketing contacts.
- One Customer Insights - Journeys app license permits deployment on only one Dynamics 365 environment. The environment could be a sandbox or production. Deploying on multiple Dynamics 365 environments requires multiple Customer Insights - Journeys app licenses.
- Customer Insights - Journeys is available in multiple variants with different pricing for production and non-production usage.

## Customer Insights - Journeys quota limits

As documented in [Quota management](quota-management.md), there are multiple types of marketing quotas. Here are some issues customers encounter regarding quotas:

- **You see a sudden drop in the Customer Insights - Journeys quota compared to the past or compared to what you have always paid for.** In such cases, validate that the Customer Insights - Journeys app and the marketing contact add-on pack subscription hasn't expired. Normally, if a subscription expires, the related quota associated with it also decreases.
- **You purchased marketing contact packs, but you do not see the packs reflected in the Quota Limits monitoring.** There could be multiple causes, but some common reasons are:
    1. *There are multiple channels through which you can purchase the Customer Insights - Journeys app and contact packs.* It might take time for the purchases to reflect in the quota limits. If the purchase doesn't reflect after 24 hours, you should open a support ticket to resolve the issue.
    1. *The offer used to purchase contact packs doesn't match the base offer of the Customer Insights - Journeys app.* This mismatch is normally the case in a non-web direct purchase channel. Check with your Microsoft contact counterpart for the purchase to validate that there isn't a purchase conflict. If no dependency issues are found and the purchase doesn't reflect after 24 hours, you should open a support ticket to resolve the issue.

## Environment strategy

The Dynamics 365 Customer Insights - Journeys app is built on top of the Dynamics 365 platform. Follow the environment and development strategy recommended by the Dynamics 365 platform when adopting Customer Insights - Journeys. You can find more details about
Dynamics 365 platform administration and environment strategy in this [Power
Platform Admin and Governance whitepaper](https://aka.ms/powerappsadminwhitepaper) [section: Platform architecture].

Customer Insights - Journeys customers often maintain a development environment, a test environment, and a prod environment. The various environments help to:

- Set up security boundaries and provide environments with flexibility for change management. For example, in a development environment, you might allow multiple customizations. But in prod, customizations are restricted to ensure a fully stable environment.
- Test upcoming features in a non-prod environment.
- Address DevOps issues without putting the prod environment at risk.

Depending on the environment and its usage, you might have different needs when deploying the Customer Insights - Journeys app. For information about deploying various environments, see the next section.

## Customer Insights - Journeys app types

Dynamics 365 Customer Insights - Journeys is composed of several components. Each Dynamics 365 environment requires a dedicated Customer Insights - Journeys app. In other words, if you want multiple Customer Insights - Journeys environments, you need to purchase multiple Customer Insights - Journeys app licenses. Many times, you might not want to buy additional Customer Insights - Journeys app licenses but still want to follow the best practices of having a dev, test, and prod setup. In such cases, there's another option.

Customer Insights - Journeys offers a solution-only license. The solution-only license doesn't support Customer Insights - Journeys processes such as segmentation and email sending. It does support, however, Customer Insights - Journeys metadata such as marketing entities that you can use for extensibility purposes. The solution-only license also allows you to enable ALM operations across your environments. Learn more about the solution-only license in [Purchase and set up Dynamics 365 Customer Insights - Journeys](purchase.md#how-to-purchase-dynamics-365-marketing).

Here are some of the common pitfalls (from a management perspective) that you might face when working with multiple Customer Insights - Journeys apps/environments:

- **Encountering an error about missing components when importing a custom solution build from a source environment containing a Customer Insights - Journeys app to a target environment that does not contain a Customer Insights - Journeys app, such as transitioning from QA to UAT.** In this scenario, you might believe that the source environment Customer Insights - Journeys solution is the cause of the problem. You might then try to remove or uninstall the Customer Insights - Journeys app from the source environment. Instead, deploy the solution-only Customer Insights - Journeys app on the target environment so that both the source and the target have the same level of solution level metadata.
- **Uninstalling and reinstalling the Customer Insights - Journeys app from one environment to another, hoping to reuse one Customer Insights - Journeys app for multiple Dynamics 365 environments.** This is incorrect and most of the time results in broken systems.
- **Not noting that when a Customer Insights - Journeys environment is installed as solution-only, no Customer Insights - Journeys processes (such as customer journey or segmentation) will execute.** The solution-only environment only supports Customer Insights - Journeys entity availability and extensibility. If you require marketing process execution, the full Customer Insights - Journeys app should be installed.
- **Not following defined guidance (such as pre-req) when doing ALM operations (such as copy) on environments with the Customer Insights - Journeys app.** Refer to the next section for up-to-date guidance on ALM operations.

## ALM operations

Dynamics 365 Customer Insights - Journeys supports most of the Dynamics 365 platform’s application lifecycle management (ALM) capabilities such as copy, backup, and restore. Learn more about ALM capabilities in [Manage Customer Insights - Journeys environments](./manage-marketing-environments.md).

There are specifics to these operations, however, which you should adhere to when working with Customer Insights - Journeys. Some of the common pitfalls include:

- **Incorrectly assuming that ALM operations will move with the Customer Insights - Journeys apps from source to the target.**
- **Not preparing the source and target environments for the necessary ALM operation.**
- **Unnecessary uninstalling and reinstalling the Customer Insights - Journeys app in the source or target environments against the recommendations in the documentation.**

## Uninstallation

You can remove the Customer Insights - Journeys app from any Dynamics 365 environment where it's installed. While there are good reasons to uninstall the Customer Insights - Journeys app (such as dismantling a sandbox environment), there are situations where this operation is used incorrectly. The following scenarios outline some common situations where the uninstall operation is incorrectly used:

- **Trying to use one Customer Insights - Journeys license for multi-use on multiple environments instead of doing a fresh install.** For information about installing Customer Insights - Journeys on more than one environment, refer to the Environment Strategy and Customer Insights - Journeys app type sections for additional guidance and options. The Customer Insights - Journeys uninstall process has [particular requirements and implications](uninstall-marketing.md).
- **Once the Customer Insights - Journeys app is uninstalled, trying to also remove the Customer Insights - Journeys solutions from the environment.** The Customer Insights - Journeys app installs [many solutions on an environment](developer/marketing-solutions.md). You [don't need to remove the solutions](uninstall-marketing.md#uninstall-customer-insights---journeys-services) when uninstalling the Customer Insights - Journeys app. Removing the solutions requires special care and sequencing. Incorrect sequential removal of the solutions brings the environment into an undesired state. If you need to remove the solutions for valid business reasons (such as also removing the Customer Insights - Journeys metadata from the environment), you should open a support ticket to resolve the issue.

## Microsoft Dataverse vs CE deployment

Currently, Dynamics 365 Customer Insights - Journeys, like other Dynamics 365 model apps (Sales, Service, etc.), can only be deployed on CE environments (also known as orgs).

- [This documentation](/power-platform/admin/create-environment) describes how to add CE environments via purchase into a tenant on which Customer Insights - Journeys can be deployed.

- A CE environment could also be [provisioned via the Power Platform Admin Center with a CE DB](/power-platform/admin/create-environment). If you need to create a Customer Insights - Journeys template-based CE environment, you should open a support ticket to resolve the issue.

## Trials

Dynamics 365 Customer Insights - Journeys trial apps have special behavior. Customer Insights - Journeys trial apps can only be installed on Dynamics 365 trial environments, which are automatically provided as part of the Customer Insights - Journeys Trial sign-up process. Unlike paid environments, these environments can't be created manually. Similarly, paid Customer Insights - Journeys apps (sandbox or prod) can't be deployed on trial environments.

You can convert a trial app to a paid subscription using the in-app purchase process. Learn more: [Purchase a license directly from a Customer Insights - Journeys trial](direct-purchase.md).

## Data transfer

You can replicate Dynamics 365 Customer Insights - Journeys configurations and data across environments using the standard tools provided for Dynamics 365. More information is available in [Transfer data](transfer-data.md) and in [Transfer customizations](transfer-solution.md). The following are some of the common pitfalls when transferring data:

- **Using ALM operations instead of Import/Export when transferring selective data.**
- **Not following the transfer guidelines mentioned in the documentation such as having similar source and target versions of the Customer Insights - Journeys app.**

## Migrations

- **Tenant to tenant**:* Dynamics 365 Customer Insights - Journeys supports [tenant to tenant migration within the same geo](/power-platform/admin/move-environment-tenant). There are, however, specific conditions to such migration that you must follow when provided as part of the support request.
- **Geo to geo**: The Customer Insights - Journeys app doesn't currently support migration between different tenant geographic locations (geo to geo).

## Geos (commercial clouds)

Dynamics 365 Customer Insights - Journeys is only available in certain geos. Refer to [the International availability guide](/dynamics365/get-started/availability) for Customer Insights - Journeys geo availability.

If your tenant is in a non-supported geo, you can't deploy Customer Insights - Journeys in that geo. The tenant must be enabled for multi-geo before deploying Customer Insights - Journeys in a supported geo. In this scenario, open a support request to check for feasibility.

[!INCLUDE[footer-include](./includes/footer-banner.md)]