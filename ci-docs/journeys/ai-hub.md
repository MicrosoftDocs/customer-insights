---
title: Introduction to AI Hub in Customer Insights – Journeys (preview)
description: AI Hub in Customer Insights – Journeys lets admins manage AI agents, prerequisites, and limits for an environment. Learn how to enable and govern these features.
ms.date: 07/09/2026
ms.update-cycle: 180-days
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

AI Hub is the settings area in Customer Insights – Journeys where administrators manage AI agents and Copilot features for an environment. To open AI Hub, go to **Settings** and select **AI Hub** in the left navigation. AI Hub lets administrators configure prerequisites, enable or disable agents, and set operational limits such as processing caps and follow-up thresholds.

AI Hub aligns with tenant-level governance defined in Copilot Hub in the Power Platform Admin Center, helping ensure compliance with organizational policies. By consolidating controls into a single location, AI Hub simplifies how administrators review, configure, and manage AI capabilities across the environment.

> [!NOTE]
> AI Hub is available to users with the **Admin** role by default. If you use custom roles and permissions, add agent settings permissions for the *msdynmkt_agentsettings* entity.

> [!IMPORTANT]
> AI Hub is available as part of the 1.1.65002.153 update. To use AI Hub, navigate to **Settings** > **Versions** and upgrade to 1.1.65002.153.
>
> If you're a customer in the North America (NAM) or Oceania (OCE) region, Journey Creation Agent will be available with the June 2026 update.


[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## How AI agents work in Dynamics 365 Customer Insights – Journeys

AI agents in Customer Insights – Journeys help create and optimize customer engagement by automating common tasks and applying data-driven decision-making. Agents are available out of the box and consume Copilot credits.

Currently, there are two agents available:

- Journey Creation Agent
- Outreach Optimization Agent

## Enable agents in Customer Insights – Journeys

To use AI agents in Customer Insights – Journeys, a tenant administrator must first enable AI agents at the tenant level in the Power Platform Admin Center.

To enable agents:

1. Go to **Power Platform Admin Center** > **Copilot** > **Settings**. Or, go to this URL: https://admin.powerplatform.microsoft.com/copilot/settings
1. Scroll to the **Dynamics 365 Customer Insights – Journeys** section.
1. Select **AI agents**.
1. Set **Use AI agents** to **On** for the selected environment or environment group.
1. **Save** the settings.

Once enabled at the tenant level, AI agents can be configured and managed within AI Hub in Customer Insights – Journeys. If AI agents aren't enabled in the Power Platform Admin Center, AI Hub displays a warning banner indicating that tenant-level permissions are required.

## Accept AI agent prerequisites

After enabling AI agents in the Power Platform Admin Center, administrators must accept required prerequisites before agents can be used in Customer Insights – Journeys. The following prerequisites must be reviewed and accepted:

- Microsoft Copilot Studio capacity
- Move data across regions
- AI prompts

These prerequisites ensure that AI features operate within supported capacity, data handling, and compliance settings. For more information, see [Manage prerequisites in AI Hub](ai-hub-prerequisites.md).

## Set up AI agents in AI Hub

After all required prerequisites are accepted, you can enable individual agents in **Add and manage agents**.

### Set up the Journey Creation Agent

The Journey Creation Agent translates user intent into a fully configured customer journey. Based on a described goal (for example, re-engagement, service notification, or event promotion), the agent generates the journey structure, including triggers, messaging steps, and flow logic. This reduces the need for manual configuration and lets users create journeys without detailed knowledge of journey design or technical setup. For more information, see [Journey Creation Agent in Customer Insights - Journeys](journey-creation-agent.md).

Steps to set up the Journey Creation Agent:

1. In **AI Hub**, select **Add and manage agents**.
1. Select **Add an agent** and choose **Journey Creation Agent**.
1. In the **Overview tab**, review how the agent works.
1. Complete the Journey Creation Agent prerequisite, Anthropic integration. For more information, see [Allow external language models for generative responses](/power-platform/admin/allow-llm-generative-responses).
1. To control agent usage, configure *message consumption limits*. For more information, see [Manage capacity](/power-platform/admin/manage-copilot-studio-messages-capacity#manage-capacity).
1. To activate the agent, select **Enable**.

Once enabled, the Journey Creation Agent is available in the selected environment. To use it, go to **Real-time marketing** > **Journeys**.

### Set up Outreach Optimization Agent

Outreach Optimization Agent improves how and when messages are delivered to customers. It analyzes engagement history and real-time signals to adjust message timing, frequency, and follow-up behavior. Instead of relying on fixed schedules, the agent dynamically determines optimal send times and cadence, helping ensure that outreach is delivered when customers are more likely to engage. For more information, see [Outreach Optimization Agent in Customer Insights - Journeys](outreach-optimization-agent.md).

Steps to set up Outreach Optimization Agent:

1. In **AI Hub**, select **Add and manage agents**.
1. Select **Add an agent** and choose **Outreach Optimization Agent**.
1. In the **Overview tab**, review how the agent works.
1. To control agent usage, configure *message consumption limits*. For more information, see [Manage capacity](/power-platform/admin/manage-copilot-studio-messages-capacity#manage-capacity).
1. To activate the agent, select **Enable**.

Once enabled, Outreach Optimization Agent can be applied within journeys to optimize message delivery and engagement.

## Disable AI agents

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
