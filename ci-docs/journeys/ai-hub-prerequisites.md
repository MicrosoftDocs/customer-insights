---
title: Manage prerequisites in AI Hub (preview)
description: Manage AI Hub prerequisites in Customer Insights – Journeys to enable AI agents. Learn how to review and accept required settings in Power Platform Admin Center.
ms.date: 05/07/2026
ms.topic: how-to
ms.collection: bap-ai-copilot
author: terezakirk
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
---

# Manage prerequisites in AI Hub (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]  

Before you can use AI agents in Customer Insights – Journeys, administrators must review and accept a set of mandatory prerequisites. These prerequisites ensure that AI capabilities are enabled in a controlled and compliant manner, aligned with organizational policies for capacity, data handling, and AI usage.

Prerequisites are managed at the tenant level through the Power Platform Admin Center and are surfaced in AI Hub for review and acceptance. Until all required prerequisites are accepted, AI agents remain unavailable for configuration or use.

This article describes each prerequisite, explains its purpose, and provides guidance on how to review and accept it.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Prerequisites for AI agents

Before enabling AI agents in Customer Insights – Journeys, administrators must review and accept three required prerequisites. Each prerequisite defines conditions for capacity, data processing, and AI feature usage.

### 1. Microsoft Copilot Studio capacity

This prerequisite ensures that sufficient capacity is available to support AI agent operations.

AI capabilities in Dynamics 365 Customer Insights – Journeys support two billing models:

- **Prepaid capacity**: Uses Copilot Studio message pack subscriptions, which are a licensing option for Microsoft Copilot Studio that you purchase in advance.
- **Pay-as-you-go**: Charges for the actual number of messages consumed by agents during the month.

Learn more: [Copilot licensing](/microsoft-copilot-studio/billing-licensing).

#### Set up Microsoft Copilot Studio capacity

Before using AI agents, administrators must ensure that sufficient Copilot Studio capacity is allocated to the environment.
Capacity allocation is managed in the Power Platform Admin Center. Learn more: [Manage capacity](/power-platform/admin/manage-copilot-studio-messages-capacity#manage-capacity).

Steps to allocate capacity:

1. Sign in to the **Power Platform Admin Center**.
1. In the navigation pane, select **Licensing**.
1. Under **Products**, select **Copilot Studio**.
1. Open the **Summary** tab.
1. Complete one of the following actions:
    - Select **Manage capacity** from the **Prepaid capacity** card, *or*
    - Under the **Copilot Studio** section, select **Manage Copilot credits** or **Manage sessions**.
1. In the allocation panel:
    - Select the target **environment**.
    - Specify the number of **Copilot credits** to allocate.

### 2. Move data across regions

The AI agents in Dynamics 365 Customer Insights - Journeys use the same data processing and storage infrastructure as other Copilot features in Power Platform. This behavior means that the data that the agents use might be processed and stored in regions outside of the user's primary region, depending on the availability of services and infrastructure.

For more information about data residency and movement for Copilot features, see [Move data across regions for Copilots and generative AI features](/power-platform/admin/geographical-availability-copilot).

#### Enable move data across regions

To use AI agents that require cross-region processing, administrators must enable the **Move data across regions** prerequisite in Power Platform Admin Center. Learn more: [Turn on data movement, Bing search, Microsoft 365 services, and flex routing](/power-platform/admin/geographical-availability-copilot?tabs=new#turn-on-data-movement-bing-search-microsoft-365-services-and-flex-routing).

Steps to enable moving data across regions:

1. Sign into the **Power Platform Admin Center**.
1. In the navigation pane, select **Manage**.
1. Select **Environments**.
1. On the **Environments** page, select the target environment.
1. In the environment details page, locate the **Generative AI features** card and select **Edit**.
1. Review the terms of use.
1. Select the **Move data across regions** checkbox.
1. **Save** the changes.

### 3. AI prompts

This prerequisite governs how AI-generated prompts and inputs are processed. AI agents use prompts to interpret user intent and generate outputs. An AI prompt is a natural language instruction using a large language model (LLM) that allows you to perform tasks and helps you meet specific business needs. Learn more: [Enable or disable AI prompts in Power Platform and Copilot Studio](/ai-builder/administer#enable-or-disable-ai-prompts-in-power-platform-and-copilot-studio).

#### Enable AI prompts

Steps to enable AI prompts:

1. Sign into the **Power Platform admin center**.
1. In the admin center, select **Environments** > [*select an environment*] > **Settings** > **Product** > **Features**.
1. On the **Features** settings page under **AI Builder**, enable the **AI prompts** toggle.

If your environment is part of an environment group, you can also govern the AI prompts feature availability through the AI prompts environment group rule.

## Geographical availability and languages supported

AI agents in Customer Insights - Journeys are available in the geographical regions and languages listed in the [Copilot international availability report](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport).

[!INCLUDE [footer-include](./includes/footer-banner.md)]