---
title: Give consent to use Copilot in Customer Insights - Data
description: As an admin, give consent to use all Copilot features in Customer Insights - Data
ms.date: 09/01/2023
ms.reviewer: v-wendysmith
ms.topic: conceptual
author: radsay01
ms.author: rsayyaparaju 
ms.custom: bap-template
---

# Give consent to use Copilot in Customer Insights - Data

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

There are three levels of consent to use generative AI copilot features in Customer Insights - Data. Consent is global for all users and all Copilot features in Customer Insights - Data.

- **Enable Copilot features powered by Azure OpenAI**: **On** indicates you agree to enable all Copilot features and acknowledge that AI-generated content should be reviewed. Default is **On**.

- **Allow cross-geography data flow for Copilot features**: **On** indicates you agree that data may be stored and processed outside of your geographic region, compliance boundary, or national cloud instance. Default is **On** for the United States and the European Union where Azure OpenAI is deployed. Default is **Off** for all other regions and if Azure OpenAI isn't deployed.

- **Allow data sharing for Copilot features**: **On** indicates you agree to allow Microsoft to capture and review inputs, outputs, and telemetry from Copilot features to improve Microsoft's models, features, and services.

A Dynamics 365 Customer Insights - Data admin role is required to change consent for opt-in and cross-geography levels. A Power Platform Admin Center administrator role is required to change data sharing consent.

1. Go to **Settings** > **System** and select the **Consent** tab.

   :::image type="content" source="media/copilot-settings-consent.svg" alt-text="Screenshot of the Consent tab in System Settings.":::

1. Toggle consent on or off.

[!INCLUDE [footer-include](includes/footer-banner.md)]
