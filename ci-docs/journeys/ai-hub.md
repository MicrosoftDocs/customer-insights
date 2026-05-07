---
title: Introduction to AI Hub in Customer Insights – Journeys (preview)
description: AI Hub in Customer Insights – Journeys centralizes AI agent management. Learn how to enable, configure, and govern agents in your environment today.
ms.date: 05/07/2026
ms.topic: how-to
ms.collection: bap-ai-copilot
author: terezakirk
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
---

# Introduction to AI Hub in Customer Insights – Journeys (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]  

AI Hub is a centralized experience in Customer Insights – Journeys for managing AI agents and Copilot features at the environment level. To visit AI hub, navigate to **Settings** and select **AI Hub** in the left side navigation. AI Hub allows administrators to configure prerequisites, enable or disable agents, and set operational limits such as processing caps and follow-up thresholds.

AI Hub aligns with tenant-level governance defined in Copilot Hub in the Power Platform Admin Center, helping ensure compliance with organizational policies. By consolidating controls into a single location, AI Hub simplifies how administrators review, configure, and manage AI capabilities across the environment.

> [!NOTE]
> AI Hub control is available to the Admin user role by default. If you use custom roles and permissions and want to add specific permissions for agent settings, the entity is *msdynmkt_agentsettings*.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## How AI agents work in Dynamics 365 Customer Insights – Journeys

AI agents in Customer Insights – Journeys assist with creating and optimizing customer engagement by automating common tasks and applying data-driven decision making. Agents are available out of the box and consume Copilot credits.

Currently, there is one agent available:

- Journey Creation Agent

## Enable agents in Customer Insights – Journeys

To use AI agents in Customer Insights – Journeys, a tenant administrator must first enable AI agents at the tenant level in the Power Platform Admin Center.

To enable agents:

1. Go to **Power Platform Admin Center** > **Copilot** > **Settings**. Or, go to this URL: https://admin.powerplatform.microsoft.com/copilot/settings
1. Scroll to the **Dynamics 365 Customer Insights – Journeys** section.
1. Select **AI agents**.
1. Turn **Use AI agents** "On" for the selected environment or environment group.
1. **Save** the settings.

Once enabled at the tenant level, AI agents can be configured and managed within AI Hub in Customer Insights – Journeys. If AI agents aren't enabled in the Power Platform Admin Center, AI Hub displays a warning banner indicating that tenant-level permissions are required.

## Accepting prerequisites

After enabling AI agents in the Power Platform Admin Center, administrators must accept required prerequisites before agents can be used in Customer Insights – Journeys. The following prerequisites must be reviewed and accepted:

- Microsoft Copilot Studio capacity
- Move data across regions
- AI prompts

These prerequisites ensure that AI features operate within supported capacity, data handling, and compliance settings. Learn more: [Manage prerequisites in AI Hub](ai-hub-prerequisites.md).

## Setting up AI Agents

After all mandatory prerequisites are accepted, individual agents can be enabled in the  **Add and Manage Agents** section.

### Set up the Journey Creation Agent

The Journey Creation Agent translates user intent into a fully configured customer journey. Based on a described goal (for example, re-engagement, service notification, or event promotion), the agent generates the journey structure, including triggers, messaging steps, and flow logic. This reduces the need for manual configuration and enables users to create journeys without requiring detailed knowledge of journey design or technical setup. Learn more: [Journey Creation Agent in Customer Insights - Journeys](journey-creation-agent.md).

Steps to set up the Journey Creation Agent:

1. In **AI Hub**, select **Add and manage agents**.
1. Select **Add an agent** and choose **Journey Creation Agent**.
1. In the **Overview tab**, review how the agent works.
1. Complete the Journey Creation Agent-specific prerequisite: Anthropic integration (required). Learn more: [Allow external language models for generative responses](/power-platform/admin/allow-llm-generative-responses).
1. To control agent usage, configure *message consumption limits*. Learn more: [Manage capacity](/power-platform/admin/manage-copilot-studio-messages-capacity#manage-capacity).
1. To activate the agent, select **Enable**.

Once enabled, the Journey Creation Agent is available in the selected environment. To use it, go to **Real-time marketing** > **Journeys**.

## Disabling AI agents

Administrators can disable AI agents at any time at the environment or tenant level.

### Disable individual agents

To disable a specific agent:

1. In AI Hub, go to **Add and manage agents**.
1. Select the agent.
1. Set the agent status to **Disabled**.

Once disabled, the agent is no longer available for use in the selected environment.

### Disable all agents at the tenant level

If a tenant administrator disables AI agents in the **Power Platform Admin Center**:

- All active agents are **immediately disabled**.
- New agents can't be created or configured.

### Impact of prerequisites

If any mandatory prerequisite is no longer accepted in the Power Platform Admin Center:

- All enabled agents are *automatically disabled*.
- Agents remain unavailable until the prerequisite is accepted again.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
