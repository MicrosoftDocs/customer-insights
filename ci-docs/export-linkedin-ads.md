---
title: "Export segments to LinkedIn Ads (preview)"
description: "Learn how to configure the connection and export to LinkedIn Ads."
ms.date: 10/08/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to LinkedIn Ads (preview)

Export segments of unified customer profiles to LinkedIn Ads to create matched audiences. Use the matched audiences for company targeting and contact targeting.

## Prerequisites

- A [LinkedIn Campaign Manager account](https://business.linkedin.com/marketing-solutions/ads) and corresponding administrator credentials.
- A [LinkedIn Campaign Manager Account ID](https://www.linkedin.com/help/lms/answer/a424270).
- [Configured segments](segments.md) in Customer Insights.
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Up to 100,000 customer profiles per export to LinkedIn Ads, which can take up to 10 minutes to complete.
- Segments only. A segment must contain at least 300 unique profiles.

## Set up connection to LinkedIn Ads

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **LinkedIn Ads**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your LinkedIn Campaign Manager Account ID.

1. Select **I agree** to confirm the [Data privacy and compliance](#data-privacy-and-compliance).

1. Select **Connect** to initialize the connection.

1. Select **Authenticate with LinkedIn** and provide your admin credentials for LinkedIn Campaign Manager.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to LinkedIn Ads, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that LinkedIn Ads meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to stop the use of this functionality.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the LinkedIn Ads section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. Choose whether you want to export data to do [contact targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/contact-targeting) or [company targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/account-targeting) on LinkedIn.

1. In the **Data matching** section, for contact targeting, select at least one field that represents a customer's email address, Apple Ad ID, Google Ad ID, Google User ID, or first and last name. If you choose company targeting, select at least one field that represents a company name, email domain, LinkedIn page URL, Stock symbol, or Website.

1. Optionally, add fields to further define your export. Select **Add attribute** to map these fields.

1. Select the segments you want to export. The matched audiences in LinkedIn Campaign Manager will automatically be created with the name of the segments that you selected to export. Each segment will result in a separate matched audience.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).
