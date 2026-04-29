---
title: Managing prerequisites in AI Hub (preview)
description: Learn how to review and accept mandatory prerequisites for the use of AI agents in Customer Insights - Journeys
ms.date: 04/27/2026
ms.topic: how-to
author: terezakirk
ms.author: alfergus
search.audienceType: 
  - admin
---
# Managing prerequisites in AI Hub (preview)
Before AI agents can be used in Customer Insights – Journeys, administrators must review and accept a set of mandatory prerequisites. These prerequisites ensure that AI capabilities are enabled in a controlled and compliant manner, aligned with organizational policies for capacity, data handling, and AI usage.
Prerequisites are managed at the tenant level through Power Platform Admin Center and are surfaced in AI Hub for review and acceptance. Until all required prerequisites are accepted, AI agents remain unavailable for configuration or use.

This article describes each prerequisite, explains its purpose, and provides guidance on how to review and accept them.
[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Prerequisites for AI agents
Before enabling AI agents in Customer Insights – Journeys, administrators must review and accept three required prerequisites. Each prerequisite defines conditions for capacity, data processing, and AI feature usage.

### Microsoft Copilot Studio capacity
This prerequisite ensures that sufficient capacity is available to support AI agent operations.

AI capabilities in Dynamics 365 Customer Insights – Journeys support two billing models: **prepaid capacity** and **pay-as-you-go**. The prepaid capacity model uses Copilot Studio message pack subscriptions, which are a licensing option for Microsoft Copilot Studio that you purchase in advance. The pay-as-you-go model charges for the actual number of messages consumed by agents during the month. Learn more in [Copilot licensing](https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing).

#### Set up Microsoft Copilot Studio capacity
Before using AI agents, administrators must ensure that sufficient Copilot Studio capacity is allocated to the environment.
Capacity allocation is managed in Power Platform Admin Center. [Learn more](https://learn.microsoft.com/en-us/power-platform/admin/manage-copilot-studio-messages-capacity#manage-capacity)

Steps:
1.	Sign in to **Power Platform Admin Center**.
2.	In the navigation pane, select **Licensing**.
3.	Under **Products**, select **Copilot Studio**.
4.	Open the **Summary** tab.
5.	Complete one of the following actions:
o	Select **Manage capacity** from the **Prepaid capacity** card
o	*or* under the **Copilot Studio** section, select **Manage Copilot credits** or **Manage sessions**
6.	In the allocation panel:
o	Select the target **environment**
o	Specify the number of **Copilot credits** to allocate

### Move data across regions
The AI agents in Dynamics 365 Customer Insights - Journeys use the same data processing and storage infrastructure as other Copilot features in Power Platform. This behavior means that the data that the agents use might be processed and stored in regions outside of the user's primary region, depending on the availability of services and infrastructure. For more information about data residency and movement for Copilot features, see [Move data across regions for Copilots and generative AI features](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/blob/main/power-platform/admin/geographical-availability-copilot).

#### Enable move data across regions
To use AI agents that require cross-region processing, administrators must enable the Move data across regions prerequisite in Power Platform Admin Center. [Learn more](https://learn.microsoft.com/en-us/power-platform/admin/geographical-availability-copilot?tabs=new#turn-on-data-movement-bing-search-microsoft-365-services-and-flex-routing)

Steps:
1.	Sign in to **Power Platform Admin Center**.
2.	In the navigation pane, select **Manage**.
3.	Select **Environments**.
4.	On the **Environments** page, select the target environment.
5.	In the environment details page, locate the **Generative AI features** card and select **Edit**.
6.	Review the terms of use.
7.	Select the **Move data across regions** checkbox.
8.	Save the changes.

### AI prompts
This prerequisite governs how AI-generated prompts and inputs are processed.
AI agents use prompts to interpret user intent and generate outputs. An AI prompt is a natural language instruction using a large language model which allows you to perform tasks and serve as a companion to help you meet specific business needs. [Learn more](https://learn.microsoft.com/en-us/ai-builder/administer#enable-or-disable-ai-prompts-in-power-platform-and-copilot-studio)

#### Enable AI Prompts 
Steps:
1.	Sign in to **Power Platform admin center**.
2.	In the admin center, select **Environments** > [*select an environment*] > **Settings** > **Product** > **Features**.
3.	On the **Features** settings page under **AI Builder**, enable the **AI prompts** toggle.

If your environment is part of an environment group, you can also govern AI prompts feature availability through the AI prompts environment group rule.

## Geographical availability and languages supported
AI agents in Dynamics 365 Customer Insights - Journeys are available in geographical regions and languages listed in the [Copilot international availability report](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport). 

