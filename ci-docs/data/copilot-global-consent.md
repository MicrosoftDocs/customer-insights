---
title: Give consent to use Copilot in Customer Insights - Data
description: As an admin, give consent to use all Copilot features in Customer Insights - Data
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
ms.collection: bap-ai-copilot
---

# Give consent to use Copilot in Customer Insights - Data

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

> [!IMPORTANT]
> Copilot features in Customer Insights - Data are only available in environments in the United States and Switzerland regions. These features might become available in additional regions in future releases.

To use generative AI Copilot features in Customer Insights - Data, you need to give consent at three levels. Consent is global for all users and all Copilot features in Customer Insights - Data.

- **Enable Copilot features powered by Azure OpenAI**: Turn **On** to enable all Copilot and Bing Search-powered features and acknowledge that you should review AI-generated content. The default is **On**.

- **Allow cross-geography data flow for Copilot features**: Turn **On** to agree that data can be stored and processed outside of your geographic region, compliance boundary, or national cloud instance. If you're in a region where Azure OpenAI is deployed, such as the United States and Switzerland, this field doesn't display (the default is **On** and can't be changed). The default is **Off** for all other regions where Azure OpenAI isn't deployed. To view where Azure OpenAI services are currently deployed, see [Azure products by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services&regions=all).

- **Allow data sharing for Copilot features**: Turn **On** to allow Microsoft to capture and review inputs, outputs, and telemetry from Copilot features to improve Microsoft's models, features, and services. Customer Insights - Data only displays the consent and doesn't allow for edits; you must provide this consent in the [Power Platform admin center](https://admin.powerplatform.microsoft.com/). The default is **Off**.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Required roles to provide consent

- You need the Dynamics 365 Customer Insights - Data admin role to change consent for opt-in and cross-geography levels.

- You need a Power Platform admin center administrator role to [change data sharing consent](/power-platform/faqs-copilot-data-sharing).

## Give consent in Customer Insights - Data

1. Go to **Settings** > **System** and select the **Consent** tab.

   :::image type="content" source="media/copilot-settings-consent.svg" alt-text="Screenshot of the Consent tab in System Settings.":::

1. Enable or disable consent.

1. Select **Save**.

[!INCLUDE [copilot-availability](includes/copilot-availability.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
