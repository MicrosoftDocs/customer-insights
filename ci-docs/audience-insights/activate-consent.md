---
title: "Activate consent rules for segments in audience insights"
description: "Steps to link consent data and activate consent checks in audience insights."
ms.date: 10/30/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Activate consent rules

[Consent Center (preview)](../consent-management/overview.md) helps you to harmonize consent data from various sources. Use the unified *Consent* entity to apply default consent checks. After importing consent data in Consent Center and configuring the rules for the imported consent data, the *Consent* entity is automatically synced to audience insights.

## Enable consent checks

With consent data imported to Consent Center (preview) and rules set up, you can enable consent checks in audience insights. 

:::image type="content" source="../consent-management/media/enable-consent-checks-audience-insights.png" alt-text="Consent tab in audience insights settings with activated consent data.":::

1. In audience insights, go to **Admin** > **System**.

1. Select the **Consent (preview)** tab.

1. In the **Enable consent checks** section, set the toggle for the area you want to enable to **On**.

1. Select the **Allow override of default consent rules** checkbox to enable admins to remove the enforced consent checks when they work in the selected area. In the dropdown menu, select where you want to allow overrides.    
For example, if you allow overrides for [segments](segments.md), users can freely create new segments in audience insights. These segments might include customers who didn't give consent to have their data used. Those customers would be filtered from the segment if the default consent check is enforced. 

1. In the **Link consent to customer profiles** section, choose the attribute that is used as an identifier to link consent data to customer data. It's likely a phone number or an email address. 

1. Select **Save** to apply your settings.
