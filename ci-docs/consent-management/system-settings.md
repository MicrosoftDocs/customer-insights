---
title: "Specify system settings for consent management"
description: "Set the language and local settings for the consent management capability of Dynamics 365 Customer Insights."
ms.date: 11/12/2021
ms.service: customer-insights
ms.subservice: consent-management
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# System settings in Consent Center (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

The [consent management capability](overview.md) in Dynamics 365 Customer Insights lets you configure some system settings for your environments. 

:::image type="content" source="media/system-settings.png" alt-text="Excerpt of the system settings view.":::

## Change the language

During public preview, the app is only available in English and French. More languages are added when the capability is generally available. 

To change the language, [update your language settings in Customer Insights](../audience-insights/system.md#update-the-settings).

## Stop using the consent management capability

After an admin has provisioned the consent management capability, it's automatically available in the linked Customer Insights environment. Currently, you can't remove consent management from your environment once it's provisioned. 

However, there are some workarounds that an admin can use to stop enforcing consent rules and hence disable the functionality related to consent management. 

1. In audience insights, go to System > Consent (preview). 

1. Select the checkbox to allow overrides. 

1. Allow overrides for all existing segments. 

1. In the **Enable consent checks** section, set the toggle to **Off**.

-OR- 

1. In audience insights, go to System > Consent (preview). 

1. In the **Enable consent checks** section, set the toggle to **Off**. 

1. Remove all default consent rules.
