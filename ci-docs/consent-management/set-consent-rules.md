---
title: "Set up and apply consent data rules"
description: "With the consent management capability of Dynamics 365 Customer Insights, you can define how data is used based on a customer's consent preferences."
ms.date: 11/03/2021
ms.service: customer-insights
ms.subservice: consent-management
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Set consent data rules and apply consent preferences

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Define how customer data is used based on a customer's consent preferences. You can choose to include or exclude customer data from business activities that involve the usage of customer data. For example, you can exclude customers from your product announcements if they haven't given consent to receiving marketing emails.

## Start the consent rules setup process

First, [import consent data](import-consent-data.md) before you configure consent rules. 

Once consent data is in the system, go to the **Consent** page in the Consent Center, then select **Set rules**.

:::image type="content" source="media/set-rules-control.png" alt-text="Consent page in Consent Center with control to set rules.":::

## Set up rules

Consent data rules will be available in audience insights where you can apply them as rules to individual segments or exports. You can assign these as default rules to purposes and subscriptions that automatically apply to all segments. The app guides you through the steps to complete the mapping of consent data. 

1. In the Consent Center, go to **Data sources** and select **Set rules** to start the **Map consent data** process.

### Set rules

The first step defines if customers should be included or excluded based on their consent preferences. Every imported data source with consent data must be part of a rule mapping. For example, you've imported two consent data sources for product offers and company news, so you could have two rule mappings. One could include contacts that opted-in to the product offers and the other could exclude contacts that opted-out from company news.

1. In the **Set rules** step, create the first rule.
   :::image type="content" source="media/set-up-rules-step.png" alt-text="Set up rules step with available options."::: 
    1. Under **Select actions**, specify if you want to **Include** or **Exclude** contacts. 
    1. Under **Select data**, choose the purposes or subscriptions to apply the logic to. 
    1. Under **Select value(s)**, select the values to complete the rule.

1. Optionally, select **Add another mapping** to define more rules.

1. When you're finished defining rules, select **Next**.

### Apply rules as default (optional)

In this step, you can choose which purposes and subscriptions will have the rule mappings applied to all segments in audience insights. Rules for the imported consent data are automatically synced to audience insights. Administrators have to [activate the consent rules](../audience-insights/activate-consent.md) and can allow users to override the default selection.

1. In the **Apply rules as default (optional)** step, choose which purposes and/or subscriptions to apply the rule to by default. These rules are then applied to all segments in audience insights.

   :::image type="content" source="media/apply-rules-default.png" alt-text="Select the data the rules apply to by default. ":::

1. Select **Next**.

### Review and finish

1. Review the configuration and select **Set rules** to complete the process. 

1. If you've selected certain rules to apply by default, select **Activate consent rules in Customer Insights** to go to audience insights and [activate the default consent rules](../audience-insights/activate-consent.md). Otherwise, select **Done** to complete the guided experience and enforce the mapping in business processes.

## Activate rules in audience insights

Before the rules are applied to business processes through audience insights, an admin has to activate them. For more information, see [Activate consent rules](../audience-insights/activate-consent.md).
