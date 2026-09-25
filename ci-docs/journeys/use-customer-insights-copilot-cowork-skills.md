---
title: Use Dynamics 365 Customer Insights skills in Copilot Cowork
description: Use Dynamics 365 Customer Insights skills in Copilot Cowork to retrieve customer profiles, apply consent rules, and validate campaigns. Explore capabilities.
ms.date: 09/23/2026
ms.update-cycle: 180-days
ms.topic: how-to
author: udag
ms.author: udag
ms.reviewer: udag
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Use Dynamics 365 Customer Insights skills in Copilot Cowork

Use Dynamics 365 Customer Insights skills in Copilot Cowork to retrieve customer data, apply consent rules, and review, draft, and validate marketing email and customer journeys in one place.

Every answer is grounded in live org data retrieved through the plugin's tools rather than in generic guidance, and write operations are gated: the plugin asks for explicit confirmation before it creates or changes a record, and it checks consent before it plans any outbound send.

For example, when you ask "Which segments is Maria Torres in, and what does the churn model predict for her?", Cowork resolves the unified customer profile for that name, retrieves only the segment memberships and model predictions you asked for, and reports the segment display names together with the model, its predicted values, and the horizon — labeling predictions as estimates rather than observed outcomes.

## Key capabilities

Resolve one customer, not a guess. The plugin identifies a single unified Customer Insights - Data profile from a Dataverse contact ID, a source-record ID and its source table, a customer name, or a unified profile ID you supply. When a name matches more than one profile, it presents the candidates and asks you to choose instead of picking the first match.

Retrieve only the view you asked for. Segments, measures, predictions, household or cluster membership, and the complete Customer 360 are separate reads. Asking for one section retrieves that section, so a routine question doesn't pull an entire profile.

Apply the same consent rules the runtime applies. The consent check evaluates a contact point, channel type, purpose, business unit, and optional topic, and returns the consent status together with the blocking reason. It enforces the same rules as the Customer Insights - Journeys runtime, so the verdict you see in chat is the verdict the platform would reach at send time.

Keep marketing content on brand and publishable. The plugin reads your org's brand profiles and recent sent emails before it reviews or drafts copy, then runs a publish-readiness validation covering the from address, company address, compliance profile, and unsubscribe surface.

Work within permissions already in place. All Dataverse access flows through the Dataverse MCP server using your delegated identity, so Cowork sees exactly the records you can see.

## Prerequisites

Before you use the plugin, confirm the following prerequisites:

- A Dynamics 365 Customer Insights environment — Data, Journeys, or both — that your account can access.

- The Dataverse MCP server enabled for that environment, because journey, segment, email, and consent records are read from and written to Dataverse.

- A Microsoft 365 Copilot license, which gives you access to Cowork.

- The appropriate Dynamics 365 Customer Insights license. The plugin is available to Cowork users, but only users licensed for Customer Insights can use it to reach Customer Insights data.

## Enable the plugin

1. In Microsoft 365 Copilot, select the **Cowork** tab.

1. Select **Customize**, and then select **Plugins**.
1. In the list of installed plugins, turn on the **Dynamics 365 Customer Insights** toggle.

    > [!NOTE]
    > If the Dynamics 365 Customer Insights plugin isn't visible, select **Show more** to see the complete list of installed plugins.  

1. Select the plugin to view its details, including the skills and tools it makes available.

1. Select the settings icon and then select the environment from the **Choose which environment to connect to** drop-down list.  
    Environment selection determines which Dynamics 365 environment your Cowork prompts run against. It matters when your teams work across several environments for different lines of business, regions, or use cases. It matters again because the plugin doesn't guess. If the intended environment is unclear, the plugin asks you to choose one rather than trying a request against a test, preproduction, and production connection in turn.

## Use skills in Cowork

When you submit a request, Cowork translates it into a sequence of smaller steps rather than treating the prompt as one opaque task. It identifies the intent, determines which system holds the data, and invokes the right skill and tool for each step. The Workspace panel shows that plan and its progress while the work runs.

Ask a question in natural language in the chat composer. For example, enter "Check whether I can email the Enterprise Renewals segment about the Q3 product update, then show me who is blocked and why." Cowork resolves the segment and its members from Dataverse, runs the consent check for that audience, channel and purpose, and reports the verdict with the blocking reason for each contact point that can't be mailed — before any send is planned.

## Example prompts

- Give me the complete Customer 360 for the profile behind contact ID 4a2f… — profile, segments, measures, predictions, and clusters.

- Which segments is this customer in, and what are their computed measures?

- Which household or cluster does this customer belong to, and who else is in it?

- How many members are in the VIP segment, and what is the criteria behind it?

- Can I send a promotional message to this contact? Show me the consent status and the blocking reason.

- Review this email draft against our brand profile and tell me whether it will publish.

- Why won't this email publish? List each blocker and how to fix it.

- Add this email to Customer Insights Journeys, and publish it.

- Create a three-step nurture journey that sends the welcome email after a form submission.

- Show me my active journeys and tell me why the onboarding journey stopped.

## Skills that Cowork uses

The Customer Insights plugin contributes three skills, each with a deliberate boundary so that a request lands in one workflow rather than being answered twice in different ways. Alongside them, Cowork continues to invoke its built-in skills — Word, Excel, PowerPoint, PDF, email, calendar, meetings, daily briefing, enterprise search, deep research, and adaptive cards — and any custom skills you install from your OneDrive.

| Skill | What it does | Typical request |
|----|----|----|
| Customer brief and value metrics | Resolves one unified Customer Insights - Data profile, then returns the segment memberships, computed measures, model predictions, household or cluster membership, or the complete Customer 360. Read-only. | "Show me everything we know about this customer." |
| Customer outreach | Resolves marketing segments and audiences in Customer Insights - Journeys, applies the consent gate, creates and publishes emails and customer journeys. | "Create a journey that emails this segment after a form submission." |
| Email content advisor | Reads the org's brand profiles and recently sent emails, reviews or drafts marketing email copy against them, and runs the publish-readiness check. | "Does this email match our brand, and will it publish?" |
