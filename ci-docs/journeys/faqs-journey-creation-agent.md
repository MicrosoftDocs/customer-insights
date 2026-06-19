---
title: Responsible AI FAQs for Journey Creation Agent
description: Discover how to use Journey Creation Agent in Dynamics 365 Customer Insights - Journeys responsibly. These FAQs provide essential guidelines and best practices.
ms.date: 06/19/2025
ms.update-cycle: 180-days
ms.topic: faq
author: cmenesatti-m
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom: 
  - transparency-note
---

# Responsible AI FAQs for Journey Creation Agent

These responsible AI FAQs describe the AI impact of Journey Creation Agent feature in Dynamics 365 Customer Insights - Journeys.

## What is Journey Creation Agent?

Journey Creation Agent is an AI-powered assistant in Dynamics 365 Customer Insights - Journeys that helps marketers design and build customer journeys through natural language conversation. Instead of manually configuring each step on the journey canvas, you describe your marketing goal in plain language and the agent scaffolds the journey flow, timing, and branching logic on your behalf.

The agent draws on your existing Dynamics 365 data—segments, custom triggers, compliance profiles, and content assets—to propose a journey grounded in your actual environment. Nothing goes live until you review and explicitly publish the journey.

## What can Journey Creation Agent do?

Journey Creation Agent can:

- **Scaffold multi-step journeys** from a natural language description, including entry conditions, communication steps, wait periods, if/then branches, and exit conditions.
- **Orchestrate across channels** including email, SMS, push notifications, and custom channels.
- **Reference your Dynamics 365 data** to ground the proposed journey in your actual segments, triggers, and content assets.
- **Ask clarifying questions** to resolve ambiguity in your prompt before generating a proposal, for example, confirming the target segment, preferred timing, or journey type.
- **Iterate conversationally** allowing you to request structural changes (add or remove steps, adjust timing, change branching logic, swap content assignments) through follow-up messages.
- **Output an editable canvas** so every element the agent adds can be reviewed, modified, or removed before the journey is published.
- **Integrate with the broader agent suite** working alongside Outreach Optimization Agent for send-time optimization.

Journey Creation Agent doesn't create segments, write content, or publish journeys without explicit human review and approval.

## What is the intended use of Journey Creation Agent?

Journey Creation Agent is intended to reduce the time and expertise required to build well-structured customer journeys. It's designed for marketers who want to translate a campaign goal into a functioning journey quickly, and for teams that want a consistent starting structure based on best practices.

The feature isn't a replacement for human judgment. It's designed to accelerate the creation workflow while keeping a human in the loop at every decision point—the agent proposes, the marketer reviews and approves.

## How was Journey Creation Agent evaluated? What metrics are used to measure performance?

The agent was evaluated for each use case using curated datasets and quality metrics using a suite of golden scenarios that represent real-world marketing journey creation tasks.

**Comprehensive and accurate execution**

*Covers everything you need*: Ensures the agent includes all critical steps and information you expect, leaving nothing out.

*Correct steps and details*: Builds journeys that include all the required steps, follow your instructions, and match your expectations.

**Proactive communication**

*Asks about any missing details*: Requests additional information if needed to complete your journey, rather than guessing or omitting details.

**Efficiency and responsiveness**

*Quick responses*: Aims to reply and implement updates within a few minutes each time you request changes.

**Journey structure**

*Starts in the right place*: Initiates the journey with the correct group or trigger, according to your specifications.

*Handles branches and choices*: Incorporates all desired paths and decision points in your journey, ensuring they function as expected.

*Sets the right timing*: Configures delays and scheduling based on your instructions, so every step occurs in the intended order.

*Stops when goals are met*: Ends the journey appropriately when a customer achieves the defined goal, such as making a purchase.

*Uses the right template*: Starts from your chosen template and only makes changes as you direct.

## What are the limitations of Journey Creation Agent? How can users minimize the impact of these limitations?

**The agent doesn't create segments or content.** Journey Creation Agent scaffolds journey structure only. It references segments and content assets that already exist in your environment. If the required assets don't exist, the agent may leave placeholder steps, reference the wrong asset, or ask you to create the assets before proceeding. Create all segments, triggers, and content assets before starting an agent conversation to get the best results.

**The agent interprets your prompt, not your intent.** The quality of the proposed journey depends on how clearly the goal is described. Ambiguous or incomplete prompts may result in a journey structure that doesn't match your expectations. Use follow-up messages to refine the proposal, or start a new conversation with a more detailed description. Including the exact names of your segments and triggers in the prompt improves accuracy.

**The agent may not support all journey configurations.** Complex branching scenarios, highly customized exit conditions, or advanced journey settings may not be fully represented in the agent's output. Review the generated canvas carefully and make manual edits where the agent's output doesn't capture your requirements.

**The agent requires pre-existing channel configuration.** If a channel (such as SMS or push notifications) isn't configured in your environment, the agent can't add steps for that channel. Configure channels before using the agent for multi-channel journeys.

**Content must be in *Ready to send state* to publish.** The agent may propose a journey that references content in *Draft* state. The journey can't be published until all referenced content is marked as *Ready to send*. Review content status before publishing.

**Custom triggers must be published.** Journeys that use custom triggers as entry conditions or branch conditions can't be published until those triggers are published and have active integration code. Verify trigger status before publishing.

**The agent is subject to prompt processing limits.** Long or complex prompts may exceed processing limits and cause the agent to return an error. If this occurs, simplify your prompt or break the journey description into smaller parts and refine the proposal conversationally.

**Personally identifiable information (PII) in prompts may be blocked.** Don't include customer names, email addresses, phone numbers, or other PII in your journey description. Use segment names and trigger names instead.

**Feature availability varies by region and license.** Journey Creation Agent requires a Dynamics 365 Customer Insights - Journeys license, may not be available in all regions, and may require you to allow data movement across regions. See the [Dynamics 365 Customer Insights - Journeys feature availability by region](https://releaseplans.microsoft.com/availability-reports/?report=featuregeoreport) report for details.

## What operational factors and settings allow for effective and responsible use of Journey Creation Agent?

**Access and permissions.** Journey Creation Agent is available to users with the Marketing Manager or Marketing Professional role (or an equivalent role with sufficient permission). Administrators control feature availability through AI Hub settings in Customer Insights - Journeys. Confirm that Journey Creation Agent is enabled before use.

**Human review is required before publishing.** Every journey proposed by the agent must be reviewed on the canvas before it can go live. Use the "Review and publish" option to review the journey entry, each step, branches, and exit conditions. Verify that content assignments are correct and that all content is in *Ready to send* state. Nothing the agent creates is visible to your customers until you explicitly publish it.

**Write effective prompts.** The more specific your description, the more accurate the proposal. Effective prompts include:

- The goal of the journey (for example, re-engage contacts who haven't opened an email in 90 days).
- The target audience, using the exact name of the segment or trigger.
- Preferred channels and timing (for example, send an email on Day 0, a follow-up SMS on Day 3).
- Any branching logic or exit conditions (for example, stop the journey if the contact makes a purchase).

**Iterate through conversation.** If the initial proposal doesn't match your requirements, use follow-up messages to request specific changes rather than starting over. You can ask the agent to adjust timing, add or remove steps, change branching conditions, swap content assignments, or change the journey type.

**Verify all referenced assets before publishing.** Confirm that segments are populated, triggers are published, and all content is in *Ready to send* state. Check that any custom triggers used in the journey have active integration code.

**Use the canvas for final adjustments.** The agent's output is a starting point, not a finished journey. The canvas editor gives you full control to add steps, remove steps, modify branch conditions, adjust wait periods, and set or update the journey goal. Use the canvas to address any gaps or inaccuracies before publishing.

## Which languages are supported by Journey Creation Agent?

Journey Creation Agent supports English.

## See also

- [Journey Creation Agent in Customer Insights - Journeys](journey-creation-agent.md)
- [Responsible AI FAQ for Customer Insights - Journeys](responsible-ai-overview.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
