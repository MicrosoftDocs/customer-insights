---
title: "Export Customer Insights data to Facebook Ads Manager"
description: "Learn how to configure the connection to Facebook Ads Manager."
ms.date: 06/05/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for Facebook Ads Manager (preview)

Export segments of unified customer profiles to Facebook Ads Manager to create campaigns on Facebook and Instagram.

## Prerequisites

- You need to have a [**Facebook Ad Account**](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account) which includes a [**Facebook Business Account**](https://business.facebook.com/).
- You need to be an administrator on the [**Facebook Ad Account**](https://www.facebook.com/business/learn/lessons/step-by-step-ads-manager-account).

## Connect to Facebook Ads Manager

1. Go to **Admin** > **Export destinations**.

1. Under **Facebook Ads Manager**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

1. Select **Continue with Facebook** to sign in to your Facebook Ad Account.

1. Allow the **ads_management** permission after authenticating with Facebook.

1. Select the **Facebook Ads Account** that you want to work with.

1. Select an **Existing custom audience** from the drop-down list or create a **New custom audience**. For more information, see [**Audiences in Facebook Ads Manager**](https://www.facebook.com/business/help/744354708981227?id=2469097953376494).

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Next** to configure the export.

## Configure the connector

1. In the **Choose your key identifier field**, select **Email**, **Name and address**, or **Phone** to send to Facebook Ads Manager.

1. Map the corresponding attributes from your unified customer entity for the selected key identifier.
   > [TIP]
   > The best chances for a match occur if you select **Email** as key identifier. Adding additional identifiers may improve the matching.

1. Select **Add attribute** to map additional attributes to send to Facebook Ads Manager. Attributes from Facebook Ads Manager are mapping to the following user friendly names: 
    **FN** = **First Name**, **LN** = **Last Name**, **FI** = **First Initial**, **PHONE** = **Phone**, **GEN** = **Gender**, **DOB** = **Date of birth**, **ST** = **State**, **CT** = **City**, **ZIP** = **Postal code / Zip code**, **COUNTRY** = **Country / Region**

1. Select the segments you want to export.

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Facebook Ads Manager, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Facebook Ads meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
