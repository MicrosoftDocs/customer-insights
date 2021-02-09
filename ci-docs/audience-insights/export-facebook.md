---
title: "Export Customer Insights data to Facebook Ads Manager"
description: "Learn how to configure the connection and export to Facebook Ads Manager."
ms.date: 06/05/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Export segments list to Facebook Ads Manager (preview)

Export segments of unified customer profiles to Facebook Ads Manager to create campaigns on Facebook and Instagram.

## Prerequisites for connection

- You need to have a [**Facebook Ad Account**](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account) which includes a [**Facebook Business Account**](https://business.facebook.com/).
- You need to be an administrator on the [**Facebook Ad Account**](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account).

## Known limitations

- Up to 10 million customer profile per export to Facebook Ads Manager.
- Export to Facebook Ads Manager is limited to segments.
- Exporting segments with a total of 10 million profiles can take up to 90 minutes to complete.

## Set up connection to Facebook Ads Manager

1. Go to **Admin** > **Connections**.

1. Select **Add connection** in command bar, choose **Facebook Ads Manager** from drop down menu. This opens the set up form for this connection.

1. Give your connection a recognizable name in the **Display name** field.

1. Choose who can use this connection. If you take no action the default will be **Administrators**. [Learn more about allowing contributors to use a connection](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Authenticate with Facebook Ads: 

   1. Select **Continue with Facebook** to sign in to your Facebook Ad Account.

   1. Allow the **ads_management** permission after authenticating with Facebook.

   1. Select the **Facebook Ads Account** that you want to work with.

   1. Select an **Existing custom audience** from the drop-down list or create a **New custom audience**. For more information, see [**Audiences in Facebook Ads Manager**](https://www.facebook.com/business/help/744354708981227?id=2469097953376494).

1. Review the **Data privacy and compliance**. To confirm it, select **I agree**.

1. Select **Save** to confirm this connection setup.

## Configure an export

You can configure this export if you have access to a connection of this type. [Learn about permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export select **Add destination** in command bar. 

1. Open menu for **Connection for export** and pick a connection from section **Facebook Ads Manager**. If you don't see this section name, then there are no connections of this type available to you.

1. In the **Choose your key identifier field**, select **Email**, **Name and address**, or **Phone** to send to Facebook Ads Manager. 

1. Give your connection a recognizable name in the **Display name** field.

1. Map the corresponding attributes from your unified customer entity for the selected key identifier.
   > [TIP]
   > The best chances for a match occur if you select **Email** as key identifier. Adding additional identifiers may improve the matching.

1. Select **Add attribute** to map additional attributes to send to Facebook Ads Manager. Attributes from Facebook Ads Manager are mapping to the following user friendly names: 
    **FN** = **First Name**, **LN** = **Last Name**, **FI** = **First Initial**, **PHONE** = **Phone**, **GEN** = **Gender**, **DOB** = **Date of birth**, **ST** = **State**, **CT** = **City**, **ZIP** = **Postal code / Zip code**, **COUNTRY** = **Country / Region**

1. Select the segments you want to export.

1. Select **Save**.

Note that saving an export does not trigger the export. See below on how to run this export on demand.

## Running an export

The export run with every [scheduled refresh](system.md#schedule-tab). 
You can choose to run an [export data on demand](export-destinations.md). 

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Facebook Ads Manager, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Facebook Ads meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
