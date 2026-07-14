---
title: Give consent to use Copilot in Customer Insights - Journeys
description: Copilot consent in Customer Insights - Journeys controls AI feature access, cross-geography data flow, and data sharing. Learn which settings admins manage.
ms.date: 07/09/2026
ms.update-cycle: 180-days
ms.topic: how-to
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Give consent to use Copilot in Customer Insights - Journeys

Copilot consent in Customer Insights - Journeys controls whether generative AI features are available and how related data is handled. These settings apply to all users and most Copilot features in Customer Insights - Journeys.

Copilot for model-driven apps is controlled separately in [Power Platform admin center settings for Copilot in model-driven apps](/power-apps/maker/model-driven-apps/add-ai-copilot).

You can review the three Customer Insights - Journeys consent settings at **Settings** > **Feature switches** > **Copilot**:
- **Global Opt-in consent**: **On** indicates you agree to enable all Copilot and/or Bing Search-powered features and acknowledge that AI-generated content should be reviewed before use. Default is **On**.
- **Global cross-geography data flow consent**: **On** indicates that you agree that data may be stored and processed outside of your geographic region, compliance boundary, or national cloud instance. If you're in a region where Azure OpenAI is deployed such as the United States and Switzerland, this field doesn't display (the default is **On** and can't be changed). Default is **Off** for all other regions where Azure OpenAI isn't deployed.
- **Global data sharing consent**: **On** indicates that you agree to allow Microsoft to capture and review inputs and outputs from Copilot features to improve Microsoft's models, features, and services. Default is **Off**.

## Roles required to change Copilot consent

A Dynamics 365 Customer Insights - Journeys admin role is required to change the opt-in and cross-geography consent levels.

## Give consent in Customer Insights - Journeys

1. Go to **Settings > Feature switches**, and then go to the **Copilot** section.

    :::image type="content" source="media/copilot-consent-options.png" alt-text="Screenshot of the Copilot settings page in Customer Insights - Journeys, showing the consent options in Feature switches." lightbox="media/copilot-consent-options.png":::

1. Enable or disable consent.
1. Select **Save**.

[!INCLUDE [footer-include](includes/footer-banner.md)]
