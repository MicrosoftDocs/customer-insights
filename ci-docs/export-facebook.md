---
title: "Export segments to Facebook Ads Manager (preview) (contains video)"
description: "Learn how to configure the connection and export to Facebook Ads Manager."
ms.date: 04/15/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to Facebook Ads Manager (preview)

Export segments of unified customer profiles to Facebook Ads Manager to create campaigns on Facebook and Instagram.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWO1aN]

## Prerequisites

- A [Facebook Ads Account](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account) that includes a [Facebook Business Account](https://business.facebook.com/).
- Administrator privileges on the [Facebook Ads Account](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account).

## Known limitations

- Up to 10 million customer profiles per export to Facebook Ads Manager, which can take up to 90 minutes.
- Segments only.
- Facebook *customer list* type in [custom audiences](https://www.facebook.com/business/help/744354708981227?id=2469097953376494) only.
  > [!NOTE]
  > In some cases, you might see custom audiences of different types in the dropdown list. Selecting a different type other than *customer list* will result in a failing export.

## Set up connection to Facebook Ads Manager

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Facebook Ads Manager**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. [Allow contributors to use the connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Authenticate with Facebook Ads:

   1. Select **Continue with Facebook** to sign in to your Facebook Ads account.

   1. Allow the **ads_management** permission after authenticating with Facebook.

   1. Select the **Facebook Ads Account** that you want to work with.

   1. Select an **Existing custom audience** from the dropdown list or create a **New custom audience**.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Facebook Ads Manager section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. In the **Connect data** field, select **Email**, **Name and address**, or **Phone** to send to Facebook Ads Manager.

1. Map the corresponding attributes from your unified customer entity for the selected key identifier.
   > [!TIP]
   > The best chances for a match occur if you select **Email** as key identifier. Adding additional identifiers may improve the matching.

1. Select **Add attribute** to map more attributes to send to Facebook Ads Manager. Attributes from Facebook Ads Manager are mapping to the following user-friendly names:
    **FN** = **First Name**, **LN** = **Last Name**, **FI** = **First Initial**, **PHONE** = **Phone**, **GEN** = **Gender**, **DOB** = **Date of birth**, **ST** = **State**, **CT** = **City**, **ZIP** = **Postal code / ZIP Code**, **COUNTRY** = **Country / Region**

1. Select the segments you want to export.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

[!INCLUDE [footer-include](includes/footer-banner.md)]
