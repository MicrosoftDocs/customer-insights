---
title: "Export segments to Facebook Ads Manager"
description: "Learn how to configure the connection and export to Facebook Ads Manager."
ms.date: 09/29/2025
ms.reviewer: alfergus
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
---

# Export segments to Facebook Ads Manager

Export segments of unified customer profiles to Facebook Ads Manager to create campaigns on Facebook and Instagram.

## Prerequisites

- A [Facebook Ads account](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account) that includes a [Facebook Business account](https://business.facebook.com/).
- Admin privileges on the Facebook Ads account.
- A Facebook Ads custom audience ID. In Facebook Ads Manager, go to the audience page and set it to show the audience ID column in the table.
- The user setting up the connection in Dynamics 365 Customer Insights - Data accepts the Custom Audience Terms.

## Known limitations

- Export up to 10 million customer profiles to Facebook Ads Manager. This process can take up to 90 minutes.
- Only segments are supported.
- Facebook Ads integration doesn't support users with more than 25 ad accounts.
- Only the Facebook *customer list* type in [custom audiences](https://www.facebook.com/business/help/744354708981227?id=2469097953376494) is supported.
  > [!NOTE]
  > In some cases, you might see custom audiences of different types in the dropdown list. If you select a type other than *customer list*, the export fails.

## Set up connection to Facebook Ads Manager

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Facebook Ads Manager**.

1. Enter a recognizable name in the **Display name** field. The name and type of the connection describe the connection. Choose a name that explains the purpose and target of the connection.

1. [Allow contributors to use the connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Authenticate with Facebook Ads:

   1. Select **Continue with Facebook** to sign in to your Facebook Ads account.

   1. Allow the **ads_management** permission after you authenticate with Facebook.

   1. Select the **Facebook Ads Account** you want to use.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

### Refresh authentication for Facebook Ads connection

Authentication for a Facebook Ads connection is valid for 60 days, as enforced by Facebook. Refresh the authentication at any time.

1. Go to **Settings** > **Connections**.

1. Select the connection you want to reauthenticate from the list, and then select **Edit**.

1. Authenticate with Facebook Ads:

   1. Select **Continue with Facebook** to sign in to your Facebook Ads account.

   1. Allow the **ads_management** permission when prompted after you authenticate with Facebook.

1. Select **Save** to update the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Facebook Ads Manager section. Contact an admin if no connection is available.

1. Enter a name for the export.

1. Enter the **Facebook Ads custom audience ID**, which defines the audience this export updates. We show the Facebook Ads account name an1. In the **Connect data** field, select **Email**, **Name and address**, or **Phone** to send to Facebook Ads Manager. Map the corresponding attributes from your unified customer table for the selected key identifier.
   > [!TIP]
   > You get the best match if you select **Email** as the key identifier. Adding other identifiers can improve matching.le1. Select **Add attribute** to map more attributes to send to Facebook Ads Manager. Attributes from Facebook Ads Manager map to the following user-friendly names:
    **FN** = **First Name**, **LN** = **Last Name**, **FI** = **First Initial**, **PHONE** = **Phone**, **GEN** = **Gender**, **DOB** = **Date of birth**, **ST** = **State**, **CT** = **City**, **ZIP** = **Postal code / ZIP Code**, **COUNTRY** = **Country / Region**CT** = **City**, **ZIP** = **Postal code / ZIP Code**, **COUNTRY** = **Country / Region**

      > [!NOTE]
   > All personal data is sent as hashed values to Facebook.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
