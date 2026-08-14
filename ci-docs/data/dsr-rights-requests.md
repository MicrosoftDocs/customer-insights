---
title: Respond to Data Subject Rights (DSR) requests
description: Learn how to respond to Data Subject Requests with Dynamics 365 Customer Insights - Data.
ms.date: 05/03/2024
ms.topic: how-to
author: srivas15
ms.author: shsri
ms.reviewer: mhart
ms.custom: bap-template
---

# Respond to Data Subject Rights (DSR) requests

[!INCLUDE [gdpr-intro](~/../shared-content/shared/privacy-includes/gdpr-intro.md)]

[!INCLUDE [gdpr-dsr-delete-note](~/../shared-content/shared/privacy-includes/gdpr-dsr-delete-export-note.md)]

## Respond to data subject delete requests

The right to erasure, which is the removal of personal data from an organization’s customer data, is a key protection in many privacy laws and regulations. Removing personal data includes removing all personal data and system-generated logs, except audit log information.

### Manage data subject delete requests

Dynamics 365 Customer Insights - Data provides the following in-product experiences to delete personal data for a specific customer or user:

- **Manage delete requests for customer data**: Customer data comes from original external data sources. First, perform data delete requests in the original data source.
- **Manage delete requests for user data**: Customer Insights - Data creates data for application users. Perform all data delete requests in the application.

#### Manage requests to delete customer data

As an admin, remove customer data that you deleted in the data source. Verify that the data delete requests were performed in the original data source.

1. Sign in to Customer Insights - Data.

1. Go to **Data** > **Data sources**.

1. For each data source in the list that contains deleted customer data:
   1. Select the data source and then select **Refresh**.
   1. Check the status of the data source under **Status**.

   :::image type="content" source="media/data-sources.png" alt-text="Screenshot of the Data sources page showing the status of data sources for handling data delete requests for customer data.":::

1. After a successful data source refresh, run the downstream refreshes too, especially if you don't have a recurring full refresh scheduled.

   > [!IMPORTANT]
   > Static segments aren't included in a full refresh or downstream refreshes. To comply with the delete request for customer data, recreate the static segments with the refreshed source data.
   >
   > Inactive segments aren't refreshed (neither manually, nor a scheduled refresh, nor other refreshes). They have a **Status** listed as **Skipped**, which means that Customer Insights - Data didn't attempt to refresh them. If a segment was executed successfully before changing to an **Inactive** status, Customer Insights - Data created a table with the customer data. To comply with the delete request for customer data, either activate the segment and run it with the latest data *or* delete the segment.

#### Manage delete requests for user data

As an admin, delete application user data.

1. Sign in to Customer Insights - Data.

1. Go to **Settings** > **Permissions** and select the **Users** tab.

1. Select the checkbox for the users you want to delete.

1. Select **Remove**.

1. Confirm the deletion.

## Respond to data subject export requests

The right of data portability allows data subjects to request a copy of their personal data in a structured, common, electronic format that can be transmitted to another data controller.

### Manage export and view requests

Manage requests to export customer or user data.

#### Export customer data (tenant admin)

As a tenant administrator, export customer data.

1. Send an email to D365CI@microsoft.com specifying the customer’s email address in the request. The Customer Insights team sends an email to the registered tenant admin email address, asking for confirmation to export data.
1. Acknowledge the confirmation to export the data for the requested customer.
1. Receive the exported data through the tenant admin email address.

#### Export user data (tenant admin)

As a tenant administrator, export user data.

1. Send an email to D365CI@microsoft.com specifying the user’s email address in the request. The Customer Insights team sends an email to the registered tenant admin email address, asking for confirmation to export data.
1. Acknowledge the confirmation to export the data for the requested user.
1. Receive the exported data through the tenant admin email address.

## Data deletion handling

If data partitions and data snapshots are inactive for more than 30 days, the system refreshes data sources and replaces them with a new data partition and snapshot.

Not all data and snapshots are deleted. The most recent data partition and data snapshot are active because they're used in Customer Insights - Data. For the most recent data, it doesn't matter if the data sources weren't refreshed within the last 30 days.


[!INCLUDE [footer-include](includes/footer-banner.md)]
