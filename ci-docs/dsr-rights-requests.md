---
title: "Data Subject Rights (DSR) requests under GDPR | Microsoft Docs"
description: "Respond to Data Subject Requests for Dynamics 365 Customer Insights."
ms.date: 08/31/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: wimohabb
manager: shellyha
---

# Data Subject Rights (DSR) requests under GDPR

The European Union’s General Data Protection Regulation (GDPR) has been in effect since May 25, 2018. It gives significant rights to individuals regarding their data. The GDPR is about protecting and enabling the privacy rights of individuals. Read more about Microsoft's commitment to security and compliance at the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

We're committed to helping our customers meet their GDPR requirements. It includes the right to delete or export data that includes personal information such as user IDs, phone numbers, and email addresses. Administrators can implement user requests to delete or export personal data.

## Responding to GDPR data subject delete requests for Customer Insights

The “right to erasure” by the removal of personal data from an organization’s customer data is a key protection in the General Data Protection Regulation (GDPR). Removing personal data includes removing all personal data and system-generated logs, except audit log information.

### Manage data subject delete requests

Customer Insights offers the following in-product experiences to delete personal data for a specific customer or user:

- **Manage delete requests for customer data**: Customer data in Customer Insights is ingested from original data sources external to Customer Insights. Perform GDPR delete requests in the original data source first.
- **Manage delete requests for Customer Insights user data**: Data for users is created by Customer Insights. Perform all GDPR delete requests in Customer Insights.

#### Manage requests to delete customer data

As a Customer Insights admin, remove Customer Insights customer data that was deleted in the data source. Verify the GDPR delete requests were performed in the original data source.

1. Sign in to Dynamics 365 Customer Insights.

1. Go to **Data** > **Data sources**.

1. For each data source in the list that contains deleted customer data:
   1. Select the data source and then select **Refresh**.
   1. Check the status of the data source under **Status**. A check mark means the refresh was successful. A warning triangle means something went wrong. If a warning triangle is displayed, contact D365CI@microsoft.com.

   :::image type="content" source="media/gdpr-data-sources.png" alt-text="Handling GDPR delete requests for customer data.":::

1. After a successful data sources refresh, run the downstream refreshes too. Especially, if you don't have a recurring full refresh of Customer Insights scheduled.

   > [!IMPORTANT]
   > Static segments are not included in a full refresh or running downstream refreshes after a delete request. To ensure that customer data is removed from static segments too, recreate the static segments with the refreshed source data.

#### Manage delete requests for user data

As a Customer Insights admin, delete Customer Insights user data.

1. Sign in to Dynamics 365 Customer Insights.

1. Go to **Settings** > **Permissions** > and select the **Users** tab.

1. Select the check box for the users you want to delete.

1. Select **Remove**.

1. Confirm the deletion.

## Responding to GDPR data subject export requests

The right of data portability allows data subjects to request a copy of their personal data in an electronic format (a “structured, commonly used, machine readable, and interoperable format”) that can be transmitted to another data controller.

### Manage export and view requests

Manage requests to export customer or user data.

#### Export customer data (tenant admin)

As a tenant administrator, export customer data.

1. Send an email to D365CI@microsoft.com specifying the customer’s email address in the request. The Customer Insights team will send an email to the registered tenant admin email address, asking for confirmation to export data.
2. Acknowledge the confirmation to export the data for the requested customer.
3. Receive the exported data through the tenant admin email address.

#### Export user data (tenant admin)

As a tenant administrator, export user data.

1. Send an email to D365CI@microsoft.com specifying the user’s email address in the request. The Customer Insights team sends an email to the registered tenant admin email address, asking for confirmation to export data.
1. Acknowledge the confirmation to export the data for the requested user.
1. Receive the exported data through the tenant admin email address.

## Data deletion handling in Dynamics 365 Customer Insights

Data is deleted (data partitions and data snapshots) if the data partitions and data snapshots are inactive for more than 30 days, meaning they have been replaced by a new data partition and snapshot through a refresh of data sources.

Not all data and snapshots are deleted. The most recent data partition and data snapshot are active because they're used in Customer Insights. For the most recent data, it doesn't matter if the data sources weren't refreshed within the last 30 days.

[!INCLUDE [footer-include](includes/footer-banner.md)]
