---
title: "Export segments to LinkedIn Ads (preview)"
description: "Learn how to configure the connection and export to LinkedIn Ads."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to LinkedIn Ads (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to LinkedIn Ads to create matched audiences. Use the matched audiences for company targeting and contact targeting.

## Prerequisites

- A [LinkedIn Campaign Manager account](https://business.linkedin.com/marketing-solutions/ads) and corresponding administrator credentials.
- A [LinkedIn Campaign Manager Account ID](https://www.linkedin.com/help/lms/answer/a424270).
- [Configured segments](segments.md).
- The exported segments need at least one specific field depending whether you choose [contact targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/contact-targeting) or [company targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/account-targeting) on LinkedIn. The possible fields are listed in the **Data matching** step when [configuring the export](#configure-an-export).

## Known limitations

- Up to 100,000 customer profiles per export to LinkedIn Ads, which can take up to 10 minutes to complete.
- Segments only. A segment must contain at least 300 unique profiles.

## Set up connection to LinkedIn Ads

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **LinkedIn Ads**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your LinkedIn Campaign Manager Account ID.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Authenticate with LinkedIn** and provide your admin credentials for LinkedIn Campaign Manager.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the LinkedIn Ads section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Choose whether you want to export data to do [contact targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/contact-targeting) or [company targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/account-targeting) on LinkedIn.

1. In the **Data matching** section, for contact targeting, select at least one field that represents a customer's email address, Apple Ad ID, Google Ad ID, Google User ID, or first and last name. If you choose company targeting, select at least one field that represents a company name, email domain, LinkedIn page URL, Stock symbol, or Website.

1. Optionally, add fields to further define your export. Select **Add attribute** to map these fields.

   > [!NOTE]
   > All personal data is sent as a hashed value to LinkedIn.

1. Select the segments you want to export. The matched audiences in LinkedIn Campaign Manager will automatically be created with the name of the segments that you selected to export. Each segment will result in a separate matched audience.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
