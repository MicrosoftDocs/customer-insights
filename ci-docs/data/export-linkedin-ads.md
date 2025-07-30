---
title: "Export segments to LinkedIn Ads (preview)"
description: "Learn how to configure the connection and export to LinkedIn Ads."
ms.date: 07/17/2025
ms.reviewer: alfergus
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to LinkedIn Ads (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to LinkedIn Ads to create matched audiences. Use matched audiences for company targeting and contact targeting.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Prerequisites

- A [LinkedIn Campaign Manager account](https://business.linkedin.com/marketing-solutions/ads) and corresponding admin credentials.
- A [LinkedIn Campaign Manager Account ID](https://www.linkedin.com/help/lms/answer/a424270).
- [Configured segments](segments.md).
- Exported segments need at least one specific field, depending on whether you choose [contact targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/contact-targeting) or [company targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/account-targeting) on LinkedIn. Possible fields are listed in the **Data matching** step when [configuring the export](#configure-an-export).

## Known limitations

- Export up to 100,000 customer profiles to LinkedIn Ads at a time. This process can take up to 10 minutes.
- Export segments only. Each segment must have at least 300 unique profiles.

## Set up connection to LinkedIn Ads

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection**, then choose **LinkedIn Ads**.

1. Enter a recognizable name in the **Display name** field. The name and type describe the connection. Pick a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, only admins can use it. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your LinkedIn Campaign Manager Account ID.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) information, then select **I agree**.

1. Select **Connect** to set up the connection.

1. Select **Authenticate with LinkedIn**, then enter your admin credentials for LinkedIn Campaign Manager.

1. Select **Add yourself as export user**, then enter your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to finish setting up the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the LinkedIn Ads section. Contact your admin if no connection is available.

1. Enter a name for the export.

1. Choose whether to export data for [contact targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/contact-targeting) or [company targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/account-targeting) on LinkedIn.

1. In the **Data matching** section, for contact targeting, select at least one field that represents a customer's email address, Apple Ad ID, Google Ad ID, Google User ID, or first and last name. If you choose company targeting, select at least one field that represents a company name, email domain, LinkedIn page URL, stock symbol, or website.

1. Optionally, add fields to further define your export. Select **Add attribute** to map the fields.

   > [!NOTE]
   > All personal data is sent as a hashed value to LinkedIn.

1. Select the segments to export. LinkedIn Campaign Manager automatically creates matched audiences with the names of the segments you select. Each segment results in a separate matched audience.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
