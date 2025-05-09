---
title: "Export segments to Microsoft Advertising (preview)"
description: "Learn how to configure the connection and export to Microsoft Advertising."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to Microsoft Advertising (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export Dynamics 365 Customer Insights - Data segments to Microsoft Advertising to create Customer Match audiences. Use these audiences for your ad campaigns.

## Prerequisites

- A [Microsoft Advertising account](https://ads.microsoft.com/) and corresponding administrator credentials.
- A Microsoft Advertising Customer ID and Account ID. You can find the Customer ID (`cid`) and Account ID (`aid`) in the parameters of the URL when you're signed in to Microsoft Advertising.
- The [Customer Match](https://help.ads.microsoft.com/#apex/ads/en/56921/1) prerequisites are fulfilled and the terms of use are accepted. 
- [Configured custom audiences](https://help.ads.microsoft.com/#apex/ads/en/56720/1) in Microsoft Advertising.
- [Configured segments](segments.md) in Customer Insights - Data.
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Up to 500,000 customer profiles per export to Microsoft Advertising, which can take up to 10 minutes.
- Segments only.

## Set up connection to Microsoft Advertising

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Microsoft Advertising**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. The default is administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter the **Microsoft Advertising Customer ID**.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Authenticate with Microsoft Advertising** and provide your admin credentials for Microsoft Advertising.

1. Select **Add yourself as export user** and provide your Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Microsoft Advertising section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Provide the Microsoft Advertising custom audience ID to which you want to export your Customer Insights segments. For more information, see [Microsoft Advertising custom audience](https://help.ads.microsoft.com/#apex/ads/en/56720/1). 

1. In the **Data matching** section, in the **Email** field, select the field with a customer's email address.

   > [!NOTE]
   > All personal data is sent as a hashed value to Microsoft Advertising.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
