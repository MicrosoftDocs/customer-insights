---
title: "Export segments to Facebook Ads Manager (preview) (contains video)"
description: "Learn how to configure the connection and export to Facebook Ads Manager."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: pkieffer
ms.author: philk
---

# Export segments to Facebook Ads Manager (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to Facebook Ads Manager to create campaigns on Facebook and Instagram.

## Prerequisites

- A [Facebook Ads Account](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account) that includes a [Facebook Business Account](https://business.facebook.com/).
- Administrator privileges on the [Facebook Ads Account](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account).
- Custom Audience Terms need to be accepted by the user setting up the connection in Dynamics 365 Customer Insights - Data.

## Known limitations

- Up to 10 million customer profiles per export to Facebook Ads Manager, which can take up to 90 minutes.
- Segments only.
- Facebook Ads integration doesn't support users with more than 25 ad accounts.
- Facebook *customer list* type in [custom audiences](https://www.facebook.com/business/help/744354708981227?id=2469097953376494) only.
  > [!NOTE]
  > In some cases, you might see custom audiences of different types in the dropdown list. If you select a different type other than *customer list*, the export fails.

## Set up connection to Facebook Ads Manager

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Facebook Ads Manager**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. [Allow contributors to use the connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Authenticate with Facebook Ads:

   1. Select **Continue with Facebook** to sign in to your Facebook Ads account.

   1. Allow the **ads_management** permission after authenticating with Facebook.

   1. Select the **Facebook Ads Account** that you want to work with.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Facebook Ads Manager section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Enter the **Facebook Ads custom audience ID**, this defines which audience this export will update. You can see the audience ID in Facebook ads manager on the audience page, then choose columns and choose to display it in the table.

1. In the **Connect data** field, select **Email**, **Name and address**, or **Phone** to send to Facebook Ads Manager.

1. Map the corresponding attributes from your unified customer table for the selected key identifier.
   > [!TIP]
   > The best chances for a match occur if you select **Email** as key identifier. Adding additional identifiers may improve the matching.

1. Select **Add attribute** to map more attributes to send to Facebook Ads Manager. Attributes from Facebook Ads Manager are mapping to the following user-friendly names:
    **FN** = **First Name**, **LN** = **Last Name**, **FI** = **First Initial**, **PHONE** = **Phone**, **GEN** = **Gender**, **DOB** = **Date of birth**, **ST** = **State**, **CT** = **City**, **ZIP** = **Postal code / ZIP Code**, **COUNTRY** = **Country / Region**

   > [!NOTE]
   > All personal data is sent as a hashed value to Facebook.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
