---
title: "Configure the usage of customer data and consent preferences"
description: "Create consent rules and configure the default consent rules."
ms.date: 09/30/2021
ms.service: customer-insights
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Set consent data rules and apply consent preferences

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Define how customer data is used based on a customer's consent preferences. You can choose to include or exclude customer data from business activities that involve usage of customer data. For example, you can exclude customers form your product announcements if the they haven't given consent for marketing emails.

## Start the consent rules process

You have to [import consent data](import-consent-data.md) before your configure consent rules. 

Once consent data is in the system, go to the **Consent** page in the Consent Center and select **Set rules**.

:::image type="content" source="media/set-rules-control.png" alt-text="Consent page in Consent Center with control to set rules.":::

## Set up rules

Consent data rules will be available in audience insights where you can apply them as rules to individual segments or exports. In addition, you can assign these rules to purposes and subscriptions as default rules that automatically apply to all segments. The app guides you through the steps to complete to map the consent data. 

1. Go to **Consent** and select **Set rules**. The **Set consent data rules** process starts.

1. In the **Set up rules** step, create the first rule.
   :::image type="content" source="media/set-up-rules-step.png" alt-text="Set up rules step with available options."::: 
    1. Under **Select actions**, specify if you want to **Include** or **Exclude** contacts. 
    1. Under **Select data**, choose the purposes or subscriptions to apply the logic to. 
    1. Under **Select value(s)**, select the values to complete the rule.
    1. Optionally, select **Add a rule** to define more rules.

1. Select **Next**.

1. In the **Apply rules as default (optional)** step, choose which purposes and subscriptions to apply the rule to. These rules are then applied to segments in audience insights.
   :::image type="content" source="media/apply-rules-default.png" alt-text="Select the data the rules apply to by default. ":::

1. Select **Next**.

1. Review the configuration and select **Set rules** to complete the process. 

1. Select **Done** go complete the guided experience and enforce the mapping in business processes.
