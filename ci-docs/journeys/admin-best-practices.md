---
title: Best practices for administration
description: Learn about best practices for Dynamics 365 Customer Insights - Journeys administration and management.
ms.date: 05/01/2024
ms.custom:
  - dyn365-admin
  - dyn365-marketing
ms.topic: best-practice
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Best practices for administration

Dynamics 365 Customer Insights - Journeys is a marketing-automation app that helps turn prospects into business relationships. The app is easy to use, works seamlessly with Dynamics 365 Sales, and has built-in business intelligence.

Customer Insights - Journeys is built on top of the Dynamics 365 platform. Environment-management operations are a standard feature of model-driven Dynamics 365 apps (Sales, Customer Service, Field Service, Customer Insights - Journeys, and Project Service Automation). Customer Insights - Journeys, however, has additional considerations to keep in mind.

This document discusses some of the key elements for managing Customer Insights - Journeys, focusing on the most common areas in which administrators have questions.

## Licensing model

Customer Insights - Journeys has a different licensing model than other Dynamics 365 applications. You can find more details about the Customer Insights - Journeys licensing model in the [license guidance article](license-setup.md) and in the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544&clcid=0x409). 

## Customer Insights - Journeys quota limits

As documented in [Quota management](quota-management.md), there are multiple types of marketing quotas. Here are some issues customers encounter regarding quotas:

- **You see a sudden drop in the Customer Insights - Journeys quota compared to the past or compared to what you have always paid for.** In such cases, validate that the Customer Insights - Journeys app and the marketing contact add-on pack subscription hasn't expired. Normally, if a subscription expires, the related quota associated with it also decreases.
- **You purchased marketing contact packs, but you do not see the packs reflected in the Quota Limits monitoring.** There could be multiple causes, but some common reasons are:
    1. *There are multiple channels through which you can purchase the Customer Insights - Journeys app and contact packs.* It might take time for the purchases to reflect in the quota limits. If the purchase doesn't reflect after 24 hours, you should open a support ticket to resolve the issue.
    1. *The offer used to purchase contact packs doesn't match the base offer of the Customer Insights - Journeys app.* This mismatch is normally the case in a non-web direct purchase channel. Check with your Microsoft contact counterpart for the purchase to validate that there isn't a purchase conflict. If no dependency issues are found and the purchase doesn't reflect after 24 hours, you should open a support ticket to resolve the issue.

## Environment strategy

The Customer Insights - Journeys app is built on top of the Dynamics 365 platform. Follow the environment and development strategy recommended by the Dynamics 365 platform when adopting Customer Insights - Journeys. You can find more details about
Dynamics 365 platform administration and environment strategy in this [Power
Platform Admin and Governance whitepaper](https://aka.ms/powerappsadminwhitepaper) [section: Platform architecture].

Customer Insights - Journeys customers often maintain a development environment, a test environment, and a prod environment. The various environments help to:

- Set up security boundaries and provide environments with flexibility for change management. For example, in a development environment, you might allow multiple customizations. But in prod, customizations are restricted to ensure a fully stable environment.
- Test upcoming features in a non-prod environment.
- Address DevOps issues without putting the prod environment at risk.

Depending on the environment and its usage, you might have different needs when deploying the Customer Insights - Journeys app. For information about deploying various environments, see the next section.

## Customer Insights - Journeys app types

Customer Insights - Journeys is composed of several components. Each Dynamics 365 environment requires a dedicated Customer Insights - Journeys app. Here are some of the common pitfalls (from a management perspective) that you might face when working with multiple Customer Insights - Journeys apps or environments:

- **Encountering an error about missing components when importing a custom solution build from a source environment containing a Customer Insights - Journeys app to a target environment that does not contain a Customer Insights - Journeys app, such as transitioning from QA to UAT.** In this scenario, you might believe that the source environment Customer Insights - Journeys solution is the cause of the problem. You might then try to remove or uninstall the Customer Insights - Journeys app from the source environment. Instead, deploy the solution-only Customer Insights - Journeys app on the target environment so that both the source and the target have the same level of solution level metadata.
- **Not noting that when a Customer Insights - Journeys environment is installed as solution-only, no Customer Insights - Journeys processes (such as customer journey or segmentation) will execute.** The solution-only environment only supports Customer Insights - Journeys entity availability and extensibility. If you require marketing process execution, the full Customer Insights - Journeys app should be installed.
- **Not following defined guidance (such as pre-req) when doing ALM operations (such as copy) on environments with the Customer Insights - Journeys app.** Refer to the next section for up-to-date guidance on ALM operations.

## Environment lifecycle operations

Customer Insights - Journeys supports most of the Dynamics 365 platform’s environment lifecycle management (ELO) capabilities such as copy, backup, and restore. Learn more about ELO capabilities in [Copy or restore environments](./copy-or-restore.md).

There are specifics to these operations, however, which you should adhere to when working with Customer Insights - Journeys. Some of the common pitfalls include:

- **Incorrectly assuming that ELO operations will move with the Customer Insights - Journeys apps from source to the target.**
- **Not preparing the source and target environments for the necessary ELO operation.**
- **Unnecessary uninstalling and reinstalling the Customer Insights - Journeys app in the source or target environments against the recommendations in the documentation.**

## Uninstallation

You can remove the Customer Insights - Journeys app from any Dynamics 365 environment where it's installed. While there are good reasons to uninstall the Customer Insights - Journeys app (such as dismantling a sandbox environment), there are situations where this operation is used incorrectly. The following scenarios outline some common situations where the uninstall operation is incorrectly used:

- **Once the Customer Insights - Journeys app is uninstalled, trying to also remove the Customer Insights - Journeys solutions from the environment.** The Customer Insights - Journeys app installs [many solutions on an environment](developer/marketing-solutions.md). You [don't need to remove the solutions](uninstall.md#uninstall-customer-insights---journeys-services) when uninstalling the Customer Insights - Journeys app. Removing the solutions requires special care and sequencing. Incorrect sequential removal of the solutions brings the environment into an undesired state. If you need to remove the solutions for valid business reasons (such as also removing the Customer Insights - Journeys metadata from the environment), you should open a support ticket to resolve the issue.

## Microsoft Dataverse vs CE deployment

Currently, Customer Insights - Journeys, like other Dynamics 365 model apps (Sales, Service, etc.), can only be deployed on CE environments (also known as orgs).

- [This documentation](/power-platform/admin/create-environment) describes how to add CE environments via purchase into a tenant on which Customer Insights - Journeys can be deployed.
- A CE environment could also be [provisioned via the Power Platform Admin Center with a CE DB](/power-platform/admin/create-environment). If you need to create a Customer Insights - Journeys template-based CE environment, you should open a support ticket to resolve the issue.

## Trials

See details about creating trials here: [Sign-up for trials](trial-signup.md). You can convert a trial app to a paid subscription using the in-app purchase process. Learn more: [Purchase a license directly from a Customer Insights - Journeys trial](direct-purchase.md).

## Data transfer

You can replicate Customer Insights - Journeys configurations and data across environments using the standard tools provided for Dynamics 365. More information is available in [Transfer data](transfer-data.md) and in [Transfer customizations](transfer-solution.md). The following are some of the common pitfalls when transferring data:

- **Using ELO operations instead of Import/Export when transferring selective data.**
- **Not following the transfer guidelines mentioned in the documentation such as having similar source and target versions of the Customer Insights - Journeys app.**

## Migrations

- **Tenant to tenant**: Customer Insights - Journeys supports [tenant to tenant migration within the same geo](/power-platform/admin/move-environment-tenant). There are, however, specific conditions to such migration that you must follow when provided as part of the support request.
- **Geo to geo**: The Customer Insights - Journeys app doesn't currently support migration between different tenant geographic locations (geo to geo).

## Geos (commercial clouds)

Customer Insights - Journeys is only available in certain geos. Refer to [the International availability guide](/dynamics365/get-started/availability) for Customer Insights - Journeys geo availability.

If your tenant is in a non-supported geo, you can't deploy Customer Insights - Journeys in that geo. The tenant must be enabled for multi-geo before deploying Customer Insights - Journeys in a supported geo. In this scenario, open a support request to check for feasibility.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
