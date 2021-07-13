---
title: "Data Subject Rights (DSR) requests under GDPR | Microsoft Docs"
description: "Respond to Data Subject Requests for Dynamics 365 Customer Insights audience insights capability."
ms.date: 05/14/2020
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: wimohabb
manager: shellyha
---

# Data Subject Rights (DSR) requests under GDPR

## Responding to GDPR data subject delete requests for Dynamics 365 Customer Insights audience insights capability

The “right to erasure” by the removal of personal data from an organization’s customer data is a key protection in the General Data Protection Regulation (GDPR). Removing personal data includes removing all personal data and system-generated logs, except audit log information.

### Manage data subject delete requests

Audience insights offers the following in-product experiences to delete personal data for a specific customer or user:

- **Manage delete requests for customer data**: Customer data in Customer Insights is ingested from original data sources external to Customer Insights. All GDPR delete requests must be performed in the original data source.
- **Manage delete requests for Customer Insights user data**: Data for users is created by Customer Insights. All GDPR delete requests must be performed in Customer Insights.

#### Manage delete requests for customer data

A Customer Insights admin can follow these steps to remove customer data that was deleted in the data source:

1. Sign in to Dynamics 365 Customer Insights.
2. In audience insights, go to **Data** > **Data sources**
3. For each data source in the list that contains deleted customer data:
   1. Select (...) and then select **Refresh**.
   2. Check the status of the data source under **Status**. A check mark means the refresh was successful. A warning triangle means something went wrong. If a warning triangle is displayed, contact D365CI@microsoft.com.

> [!div class="mx-imgBorder"]
> ![Handling GDPR delete requests for customer data.](media/gdpr-data-sources.png "Handling GDPR delete requests for customer data")

#### Manage delete requests for user data

A Customer Insights admin can follow these steps to delete Customer Insights user data:

1. Sign in to Dynamics 365 Customer Insights.
2. In audience insights, go to **Admin** > **Permissions**.
3. Select the check box for the user you want to delete.
4. Select **Remove**.

> [!div class="mx-imgBorder"]
> ![Handling GDPR delete requests foruser data.](media/gdpr-permissions.png "Handling GDPR delete requests for user data")

## Responding to GDPR data subject export requests

As part of our commitment to partner with you on your journey to the General Data Protection Regulation (GDPR), we’ve developed documentation to help you prepare. This documentation describes steps you can take today to support GDPR compliance when using audience insights.

### Manage export and view requests

The right of data portability allows data subjects to request a copy of their personal data in an electronic format (a “structured, commonly used, machine readable, and interoperable format”) that can be transmitted to another data controller.

#### Export customer data (tenant admin)

A tenant administrator can follow these steps to export data:

1. Send an email to D365CI@microsoft.com specifying the customer’s email address in the request. The Customer Insights team will send an email to the registered tenant admin email address, asking for confirmation to export data.
2. Acknowledge the confirmation to export the data for the requested customer.
3. Receive the exported data through the tenant admin email address.

#### Export user data (tenant admin)

1. Send an email to D365CI@microsoft.com specifying the user’s email address in the request. The Customer Insights team will send an email to the registered tenant admin email address, asking for confirmation to export data.
2. Acknowledge the confirmation to export the data for the requested user.
3. Receive the exported data through the tenant admin email address.


[!INCLUDE[footer-include](../includes/footer-banner.md)]