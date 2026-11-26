---
title: Respond to Data Subject Rights (DSR) requests
description: Manage Data Subject Rights (DSR) requests in Customer Insights - Data by deleting customer records, removing users, and exporting data. 
ms.date: 11/11/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
ai-usage: ai-assisted
---

# Respond to Data Subject Rights (DSR) requests

[!INCLUDE [gdpr-intro](~/../shared-content/shared/privacy-includes/gdpr-intro.md)]

[!INCLUDE [gdpr-dsr-delete-note](~/../shared-content/shared/privacy-includes/gdpr-dsr-delete-export-note.md)]

## Respond to data subject delete requests

The right to erasure, which is the removal of personal data from an organization’s customer data, is a key protection in many privacy laws and regulations. Removing personal data includes removing all personal data and system-generated logs, except audit log information.

Dynamics 365 Customer Insights - Data provides the following in-product experiences to delete personal data for a specific customer or user:

- [**Manage delete requests for customer data**](#manage-requests-to-delete-customer-data): Customer data comes from original external data sources. First, perform data delete requests in the original data source.
- [**Manage delete requests for user data**](#manage-delete-requests-for-user-data): Customer Insights - Data creates data for application users. Perform all data delete requests in the application.

### Manage requests to delete customer data

As an admin, remove customer data that you deleted in the data source. Verify that the data delete requests were performed in the original data source.

1. Sign in to Customer Insights - Data.

1. Go to **Data** > **Data sources**.

1. For each data source in the list that contains deleted customer data:
   1. Select the data source and then select **Refresh**.
   1. Check the status of the data source under **Status**.

   :::image type="content" source="media/dsr-data-sources.png" alt-text="Screenshot of the Data sources page showing the status of data sources for handling data delete requests for customer data.":::

1. After a successful data source refresh, run the downstream refreshes too, especially if you don't have a recurring full refresh scheduled.

   > [!IMPORTANT]
   > Static segments aren't included in a full refresh or downstream refreshes. To comply with the delete request for customer data, recreate the static segments with the refreshed source data.
   >
   > Inactive segments aren't refreshed (neither manually, nor a scheduled refresh, nor other refreshes). They have a **Status** listed as **Skipped**, which means that Customer Insights - Data didn't attempt to refresh them. If a segment was executed successfully before changing to an **Inactive** status, Customer Insights - Data created a table with the customer data. To comply with the delete request for customer data, either activate the segment and run it with the latest data *or* delete the segment.

### Manage delete requests for user data

As an admin, delete application user data.

1. Sign in to Customer Insights - Data.

1. Go to **Settings** > **Permissions** and select the **Users** tab.

1. Select the checkbox for the users you want to delete.

1. Select **Remove**.

1. Confirm the deletion.

## Delete web tracking and personalization data

As a Dataverse administrator handling an approved deletion request, use the following procedure to delete web tracking and personalization data before deleting customer profiles or their identity links. For a tracking-only request, retain known customer profiles and their source-derived identity keys.

### Identify the tables and relationships

Include the following Dataverse tables in the request scope.

| Logical table name | Data to include |
|---|---|
| `msdynci_personalizationview` | Page views. |
| `msdynci_personalizationaction` | Clicks and other tracked actions. |
| `msdynci_personalizationuser` | Stored user events associating cookie IDs with customer identifiers. |
| `msdynci_personalizationcookie` | Cookie records and their identity-key links. |
| `msdynci_alternatekey` | Cookie-based tracking keys. Source-derived keys follow the ordinary customer-data deletion process. |
| `msdynci_customerprofile` | Associated unknown profiles. Known profiles follow the ordinary customer-data deletion process. |

On `msdynci_customerprofile`, `msdynci_webpersonalization_isunknown` is `true` for an unknown profile and `false` for a known profile.

```text
Customer profile
  |
  +-- Alternate key(s)              matched by msdynci_customerid
        |
        +-- Cookie(s)               linked by msdynci_lookupfield_alternatekey
              |
              +-- Page views        msdynci_personalizationview
              +-- Actions           msdynci_personalizationaction
              +-- User events       msdynci_personalizationuser
```

Events link to their cookie through `msdynci_personalizationcookiereference` and carry its ID in `msdynci_userlocalid`. One customer can have multiple keys and cookies across browsers and devices.

### Collect identities and records

Complete the inventory before deleting any links.

1. For a known customer, start with the unified customer ID. Retrieve its alternate keys, then every linked cookie, not only the cookie from the customer's current browser.
2. For an unknown visitor, start with their supplied cookie IDs and follow the keys to the unknown profile.
3. Collect the identifiers used to associate tracking activity with the customer, including relevant source-record IDs. Query `msdynci_personalizationuser` by these identifiers in `msdynci_userauthid`. Add the cookie IDs returned in `msdynci_userlocalid` to the inventory.
4. For every collected cookie ID, retrieve its Dataverse views, actions, and user events.
5. Follow every `@odata.nextLink` until you've retrieved all pages. Save each row's entity set, primary-key value, and `partitionid` before deleting any links.

Use the applicable entry point in steps 1 and 2. A cookie that was never linked to the customer can't be identified from their profile alone. Use identifiers confirmed to belong to the approved subject, together with their source entity and source system. Reconcile each returned cookie with the deletion scope before proceeding.

Example GET paths, relative to `/api/data/v9.2/`:

```text
msdynci_alternatekeys?$filter=msdynci_customerid eq '<customer-id>'
msdynci_personalizationcookies?$filter=_msdynci_lookupfield_alternatekey_value eq <key-guid>
msdynci_personalizationviews?$filter=msdynci_userlocalid eq '<cookie-id>'
msdynci_personalizationactions?$filter=msdynci_userlocalid eq '<cookie-id>'
msdynci_personalizationusers?$filter=msdynci_userlocalid eq '<cookie-id>'
msdynci_personalizationusers?$filter=msdynci_userauthid eq '<customer-identifier>'
```

### Delete tracking records in dependency order

Use supported Dataverse DELETE operations in this order:

1. Delete the scoped views, actions, and user events.
2. Delete their cookie records.
3. Delete cookie-based tracking alternate-key records. Retain source-derived keys until the ordinary customer-data deletion step.
4. Delete associated unknown customer profiles after confirming that `msdynci_webpersonalization_isunknown` is `true`. Retain known profiles (`false`) until the ordinary customer-data deletion step, if that step is in the request scope.

Resolve entity-set and primary-key names from `EntityDefinitions`. For partitioned elastic-table rows, use each saved record ID and partition ID:

```text
DELETE <entity-set>(<primary-key-name>=<record-guid>,partitionid='<partition-id>')
```

For more information, see [Dataverse elastic-table operations](/power-apps/developer/data-platform/use-elastic-tables).

Don't rely on cascading deletion. Deleting a profile, identity link, or cookie doesn't automatically delete the related tracking events. Confirm the scope before removing identity links shared with other records.

### Synchronize and refresh downstream data

Allow the Dataverse deletions to synchronize. Then refresh the affected web-event data source, unification, and profile hydration, in that order.

Identify copies in the data lake, exports, or connected systems and apply their supported deletion procedures. Record the results.

Don't rely on retention expiry alone. Dataverse time-to-live (TTL) expiry doesn't remove copies already synchronized through Synapse Link.

### Verify completion

Rerun the Dataverse inventory queries, following every `@odata.nextLink`. Confirm that the scoped cookies, events, cookie-based tracking keys, and applicable unknown profiles are absent. Verify that unrelated records remain and that a tracking-only request retains known profiles and their source-derived keys.

After unification and profile hydration, verify that `msdynci_webpersonalization_webactivityreference` and `msdynci_webpersonalization_webactivityreference_alternate` on retained known profiles no longer contain the deleted cookie IDs. Use the refresh path rather than manually updating these fields.

Verify removal from ingested data and relevant downstream systems. If the customer also withdraws tracking consent, update your website's consent handling to prevent new collection. Clearing browser cookies alone doesn't delete historical records.

### Complete customer-data deletion if requested

If the approved request also covers the customer's source data and known profile, delete the source records through their approved procedures. Then follow [Manage requests to delete customer data](#manage-requests-to-delete-customer-data). Refresh the affected data sources, unification, activities, measures, segments, and hydrated outputs. Verify removal of the known profile, remaining subject-specific identity mappings, and derived customer data.

For a tracking-only request, don't delete the known profile or its source-derived identity keys.

## Respond to data subject export requests

The right of data portability allows data subjects to request a copy of their personal data in a structured, common, electronic format that can be transmitted to another data controller. Manage requests to export customer or user data.

### Export customer data (tenant admin)

As a tenant administrator, export customer data.

1. Send an email to D365CI@microsoft.com specifying the customer’s email address in the request. The Customer Insights team sends an email to the registered tenant admin email address, asking for confirmation to export data.
1. Acknowledge the confirmation to export the data for the requested customer.
1. Receive the exported data through the tenant admin email address.

### Export user data (tenant admin)

As a tenant administrator, export user data.

1. Send an email to D365CI@microsoft.com specifying the user’s email address in the request. The Customer Insights team sends an email to the registered tenant admin email address, asking for confirmation to export data.
1. Acknowledge the confirmation to export the data for the requested user.
1. Receive the exported data through the tenant admin email address.

### Include web tracking and personalization data in an export request

For web tracking and personalization data, use the [identity-discovery steps](#collect-identities-and-records) to identify the customer's unified profile ID and all associated browser cookie IDs that you can identify. Include these identifiers in your [email export request](#export-customer-data-tenant-admin) through D365CI@microsoft.com. If the visitor has no known customer profile, provide the available cookie IDs. Don't perform the deletion steps when preparing an export request.

Include retained page views, actions, authentication events, and associated cookie and identity records in the requested scope. A cookie that was never linked to a known customer can't be identified from that customer's profile alone.

The [Dataverse APIs for web personalization](dv-odata.md#web-personalization) describe how to retrieve profile and activity data by cookie identifier. A profile row alone doesn't contain all related tracking records.

## Data deletion handling

If data partitions and data snapshots are inactive for more than 30 days, the system refreshes data sources and replaces them with a new data partition and snapshot.

Not all data and snapshots are deleted. The most recent data partition and data snapshot are active because they're used in Customer Insights - Data. For the most recent data, it doesn't matter if the data sources weren't refreshed within the last 30 days.

### Retention of system-generated logs

Customer Insights - Data automatically deletes sensitive identifiers and sensitive data from system-generated logs after 30 days. The service retains anonymized or redacted logs for a longer period for pattern analysis.


[!INCLUDE [footer-include](includes/footer-banner.md)]
