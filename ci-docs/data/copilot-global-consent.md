---
title: Give consent to use Copilot in Customer Insights - Data
description: As an admin, give consent to use all Copilot features in Customer Insights - Data
ms.date: 11/12/2024
ms.update-cycle: 180-days
ms.reviewer: v-wendysmith
ms.topic: how-to
author: radsay01
ms.author: rsayyaparaju 
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# Give consent to use Copilot in Customer Insights - Data

There are three levels of consent to use generative AI Copilot features in Customer Insights - Data. Consent is global for all users and all Copilot features in Customer Insights - Data.

- **Enable Copilot features powered by Azure OpenAI**: **On** indicates you agree to enable all Copilot and/or Bing Search-powered features and acknowledge that AI-generated content should be reviewed. Default is **On**.

- **Allow cross-geography data flow for Copilot features**: **On** indicates you agree that data may be stored and processed outside of your geographic region, compliance boundary, or national cloud instance. If you're in a region where Azure OpenAI is deployed such as the United States and Switzerland, this field doesn't display (the default is **On** and can't be changed). Default is **Off** for all other regions where Azure OpenAI isn't deployed. To view where Azure OpenAI services are currently deployed, see [Azure products by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services&regions=all).

- **Allow data sharing for Copilot features**: **On** indicates you agree to allow Microsoft to capture and review inputs, outputs, and telemetry from Copilot features to improve Microsoft's models, features, and services. Customer Insights - Data only displays the consent and doesn't allow for edits; this consent must be provided in the [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/). Default is **Off**.

## Required roles to provide consent

- A Dynamics 365 Customer Insights - Data admin role is required to change consent for opt-in and cross-geography levels.

- A Power Platform Admin Center administrator role is required to [change data sharing consent](/power-platform/faqs-copilot-data-sharing).

## Give consent in Customer Insights - Data

1. Go to **Settings** > **System** and select the **Consent** tab.

   :::image type="content" source="media/copilot-settings-consent.svg" alt-text="Screenshot of the Consent tab in System Settings.":::

1. Enable or disable consent.

1. Select **Save**.

[!INCLUDE [copilot-availability](includes/copilot-availability.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
