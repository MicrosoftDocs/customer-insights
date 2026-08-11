---
title: Export segments to Braze (preview)
description: Export segments to Braze from Dynamics 365 Customer Insights - Data. Learn how to set up the connection and map customer IDs and emails.
ms.date: 08/11/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom:
 - ai-gen-docs-bap
 - ai-seo-date: 08/11/2026
ai-usage: ai-assisted
---

# Export segments to Braze (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to Braze and use them for marketing campaigns and customer engagement activities.

## Prerequisites

- A [Braze account](https://www.braze.com/) and corresponding administrator credentials.
- A [Braze API key](https://www.braze.com/docs/api/basics/).
- Your [Braze REST Endpoint Hostname](https://www.braze.com/docs/api/basics/#api-definitions).
- [Segments in Braze including their segment identifier](https://www.braze.com/docs/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment).
- [Segments](segments.md) in Customer Insights.
- Unified customer profiles in the exported segments contain a field representing an email address and a Braze customer ID.

## Known limitations

- You can export up to 1 million customer profiles to Braze, which can take up to 40 minutes to complete. The number of customer profiles that you can export to Braze depends on your contract with Braze.

## Set up connection to Braze

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Braze**.

1. Enter a recognizable name for your connection in the **Display name** field. The name and the type of the connection describe this connection. Choose a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, only administrators can use it. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your [Braze API key](https://www.braze.com/docs/api/basics/).

1. Provide your [Braze REST Endpoint Hostname](https://www.braze.com/docs/api/basics/#api-definitions) in the format `rest.iad-03.braze.com`.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Braze section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Enter the segment identifier ID of the segment in Braze where you want to export your data. You can find the segment identifier ID for a segment in Braze in the segment details page at the bottom in the **API Identifier** section.

1. In the **Data matching** section:
   - In the **Braze customer ID** field, select the field that represents the [User ID of a record in Braze](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention).
     - Mapping the User ID of Braze to the Braze customer ID field in Customer Insights - Data results in updating existing records in Braze when exporting.
     - Mapping a different ID field that doesn't represent the User ID of a record in Braze, or an empty field results in creating records in Braze when exporting.
   - In the **Email** field, select the field that represents a customer's email address.

   You can choose more, optional fields for matching data.

1. Select the tables or segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
