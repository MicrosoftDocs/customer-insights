---
title: Introduction to AI Hub in Customer Insights – Journeys (preview)
description: Learn about agent capabilities in Customer Insights - Journeys and how to enable their use in your environment.
ms.date: 04/27/2026
ms.topic: how-to
author: terezakirk
ms.author: alfergus
search.audienceType: 
  - admin
---

# Introduction to AI Hub in Customer Insights – Journeys (preview)
AI Hub provides a centralized experience in Customer Insights – Journeys for managing AI agents and Copilot features at the environment level. To visit AI hub, navigate to Settings and select Ai Hub in the left-hans ide navigation. It enables administrators to configure prerequisites, enable or disable agents, and set operational limits such as processing caps and follow-up thresholds.
AI Hub aligns with tenant-level governance defined in Copilot Hub in Power Platform Admin Center, helping ensure compliance with organizational policies. By consolidating controls into a single location, it simplifies how administrators review, configure, and manage AI capabilities across the environment.
Note: AI Hub control is available to Admin user role by default. If you are using custom roles & permissions and want to add specific permissions for agent settings, the entity is msdynmkt_agentsettings. 

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## How AI Agents work in Dynamics 365 Customer Insights – Journeys
AI agents in Customer Insights – Journeys assist with creating and optimizing customer engagement by automating common tasks and applying data-driven decisioning. They are available out of the box and will consume Copilot credits. 
At present, there are two agents available: 
-	Journey Creation Agent 
-	Outreach Optimization Agent

## Enabling use of agents in Customer Insights – Journeys
To use AI agents in Customer Insights – Journeys, a tenant administrator must first enable AI agents at the tenant level in Power Platform Admin Center (PPAC).
1.	Go to *Power Platform Admin Center* > *Copilot* > *Settings*
https://admin.powerplatform.microsoft.com/copilot/settings
2.	Scroll to the *Dynamics 365 Customer Insights – Journeys* section.
3.	Select *AI agents*.
4.	Turn *Use AI agents* "On" for the selected environment or environment group.
5.	Save the settings.

Once enabled at the tenant level, AI agents can be configured and managed within *AI Hub* in Customer Insights – Journeys.

If AI agents are not enabled in PPAC, AI Hub displays a warning banner indicating that tenant-level permissions are required.

## Accepting prerequisites 
After enabling AI agents in Power Platform Admin Center, administrators must accept required prerequisites before agents can be used in Customer Insights – Journeys.
The following prerequisites must be reviewed and accepted:
-	Microsoft Copilot Studio capacity
-	Move data across regions
-	AI prompts

These prerequisites ensure that AI features operate within supported capacity, data handling, and compliance settings. [Learn more](ai-hub-prerequisites.md).

## Setting up AI Agents 
After all mandatory prerequisites are accepted, individual agents can be enabled in Add and Manage Agents section. 

### Set up Journey Creation Agent 
The Journey Creation Agent translates user intent into a fully configured customer journey. Based on a described goal (for example, re-engagement, service notification, or event promotion), the agent generates the journey structure, including triggers, messaging steps, and flow logic.
This reduces the need for manual configuration and enables users to create journeys without requiring detailed knowledge of journey design or technical setup. Learn more (link to JCA article)

Steps:
1.	In *AI Hub*, select *Add and manage agents*.
2.	Select *Add an agent* and choose *Journey Creation Agent*.
3.	In the *Overview tab*, review how the agent works.
4.	Complete the agent-specific prerequisite: 
o	Anthropic integration (required) -  [learn more](https://learn.microsoft.com/en-us/power-platform/admin/allow-llm-generative-responses)
5.	Configure *message consumption limits* to control agent usage - [learn more](https://learn.microsoft.com/en-us/power-platform/admin/manage-copilot-studio-messages-capacity#manage-capacity)
6.	Select *Enable* to activate the agent.

Once enabled, the Journey Creation Agent is available in the selected environment. To use it, go to *Real-time marketing* > *Journeys*.

### Set up Outreach Optimization Agent
The Outreach Optimization Agent improves how and when messages are delivered to customers. It analyzes engagement history and real-time signals to adjust message timing, frequency, and follow-up behavior.
Instead of relying on fixed schedules, the agent dynamically determines optimal send times and cadence, helping ensure that outreach is delivered when customers are more likely to engage. Learn more (Link to OOA article)

Steps: 
1.	In *AI Hub*, select *Add and manage agents*.
2.	Select *Add an agent* and choose *Outreach Optimization Agent*.
3.	In the *Overview tab*, review how the agent works.
4. Configure *message consumption limits* to control agent usage - [learn more](https://learn.microsoft.com/en-us/power-platform/admin/manage-copilot-studio-messages-capacity#manage-capacity)
5.	Select *Enable* to activate the agent.

Once enabled, the Outreach Optimization Agent can be applied within journeys to optimize message delivery and engagement.

## Disabling AI Agents
Administrators can disable AI agents at any time at the environment or tenant level.

### Disable individual agents
To disable a specific agent:
1.	In AI Hub, go to Add and manage agents.
2.	Select the agent.
3.	Set the agent status to *Disabled*.

Once disabled, the agent is no longer available for use in the selected environment.

### Disable all agents at the tenant level
If a tenant administrator disables AI agents in *Power Platform Admin Center (PPAC)*:
- All active agents are *immediately disabled*
-	New agents cannot be created or configured

### Impact of prerequisites
If any mandatory prerequisite is no longer accepted in PPAC:
-	All enabled agents are *automatically disabled*
-	Agents remain unavailable until the prerequisite is accepted again



