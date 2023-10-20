---
title: Give consent to use Copilot in Customer Insights - Journeys
description: As an admin, give consent to use all Copilot features in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/19/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Give consent to use Copilot in Customer Insights - Journeys

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

There are three levels of consent to use generative AI Copilot features in Customer Insights - Journeys. Consent is global for all users and all Copilot features in Customer Insights - Journeys.
- **Global Opt-in consent**: **On** indicates you agree to enable all Copilot and/or Bing Search-powered features and acknowledge that AI-generated content should be reviewed before use. Default is **On**.
- **Global cross-geography data flow consent**: On indicates you agree that data may be stored and processed outside of your geographic region, compliance boundary, or national cloud instance. If you're in a region where Azure OpenAI is deployed such as the United States and Switzerland, this field doesn't display (the default is **On** and can't be changed). Default is **Off** for all other regions where Azure OpenAI isn't deployed.
- **Global data sharing consent**: **On** indicates you agree to allow Microsoft to capture and review inputs, and outputs from Copilot features to improve Microsoft's models, features, and services. Default is **Off**.

## Required roles to provide consent

- A Dynamics 365 Customer Insights - Journey admin role is required to change consent for opt-in and cross-geography levels.

## Give consent in Customer Insights - Journeys

1. Go to **Settings > Feature switches**, and then go to the **Copilot** section.

> [!div class="mx-imgBorder"]
> ![Enable/Disable copilot functionality](media/copilot-consent-options.png "Enable/Disable copilot functionality")

2. Enable or disable consent.
3. Select **Save**.

[!INCLUDE [footer-include](includes/footer-banner.md)]