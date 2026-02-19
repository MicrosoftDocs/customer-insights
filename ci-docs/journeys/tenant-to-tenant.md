---
title: Migrate Dynamics 365 Customer Insights - Journeys between tenants
description: Discover how to set up your environment for a tenant-to-tenant migration to start the transfer process between tenants.
ms.date: 02/19/2026
ms.topic: upgrade-and-migration-article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Migrate Dynamics 365 Customer Insights - Journeys between tenants

Migrating a Customer Insights - Journeys environment between tenants requires assistance from our technical support team. To request tenant to tenant migration within the same Azure geographic location (geo), [contact technical support](/power-platform/admin/get-help-support) and submit a support request.

> [!NOTE]
> When you're migrating a Customer Insights - Journeys environment between tenants, the support team advises you about pre-migration and post-migration steps. Familiarize yourself with the [Customer Insights - Journeys app status after migration](#customer-insights---journeys-app-status-after-migration) to determine if migration is a good fit for your environment.

> [!WARNING]
> The Customer Insights - Journeys app doesn't currently support migration between different tenant geographic locations (geo to geo).

## Customer Insights - Journeys app status after migration

After tenant to tenant migration, the Customer Insights - Journeys environment will be in the following state:

- The Customer Insights - Journeys app is upgraded to the latest version that's available at the time of migration.
- All Customer Insights - Journeys-related settings and customizations from your source environment are present on the migrated environment.
- All records that were live on the source environment (such as customer journeys, emails, lead-scoring records, and more) revert to the draft state on the migrated environment.
- Interaction data from your source environment (such as email clicks or website visits) isn't available to the migrated environment. Most insights data is initialized. You can freely generate new interaction data on the migrated environment without affecting your source environment.
- Content assets uploaded to your source environment (such as images used in emails and landing pages) aren't available on the migrated environment. If you go live on the migrated environment with an email or page that was previously published on the source environment, the published design shows defunct links.
- If outbound marketing is required, you must follow the request process to enable it, which can be found in the [Transition overview article](transition-overview.md#guidance-for-existing-customers-currently-using-outbound-marketing). 
- Other aspects of the org state not specific to Customer Insights - Journeys align with the [general tenant to tenant migration norms](/power-platform/admin/move-environment-tenant).
- When migrating a Customer Insights - Journeys environment between tenants, interaction data (such as email clicks), analytics data (such as journey analytics), and Customer Voice data *isn't* migrated.
- Migrating a Customer Insights - Journeys environment between tenants with Customer Insights - Data connected is unsupported at this time. If attempted, the connection to Customer Insights - Data will be broken and will need to be reset.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
