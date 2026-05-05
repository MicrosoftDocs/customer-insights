---
title: Journey Creation Agent in Customer Insights - Journeys (preview)
description: Build customer journeys faster with Journey Creation Agent. Describe your goal in plain language and let AI scaffold steps, timing, and branching logic for you.
ms.date: 05/04/2026
ms.topic: how-to
ms.collection: bap-ai-copilot
author: cmenesatti-m
ms.author: alfergus
ms.reviewer: alfergus
---

# Journey Creation Agent in Customer Insights - Journeys (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]  

Journey Creation Agent is an AI-powered assistant in Dynamics 365 Customer Insights - Journeys that lets you build customer journey structures through natural language conversation. Instead of manually configuring each step, you describe your marketing goal in plain language, and the agent builds the journey flow, timing, and branching logic for you.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Key benefits

- **Faster journey creation**: Reduce the time to build a journey structure from hours to minutes by describing your goal conversationally rather than configuring each element manually.
- **Lower barrier to entry**: Business users who don't have deep platform expertise can build journeys without relying on a Marketing Operations specialist for every request.
- **Consistent structure**: The agent applies journey best practices for timing, branching logic, and multi-channel sequencing based on your goal and existing assets.
- **Human oversight built in**: Review and modify the proposed journey structure before activating it. You stay in control at every step.

## What is Journey Creation Agent?

Marketing teams often spend a significant portion of their time on the tactical mechanics of building journeys — selecting triggers, configuring wait steps, setting up branches, and arranging channel touchpoints in the right order. This work requires familiarity with the journey canvas and can create a bottleneck when non-technical team members need to execute campaigns.

Journey Creation Agent addresses this by letting you have a conversation about what you want to accomplish. You describe your campaign goal, your target audience, and your timeline, and the agent proposes a complete journey structure using your existing segments and content assets. You can then review the proposal, refine it through follow-up prompts, and publish when you're ready.

The agent works best when you have segments already defined in Customer Insights - Data and email, SMS, or push notification content prepared or in draft state. It assembles those assets into a logical journey flow — it does not create segments or write content for you in this release.

> [!IMPORTANT]
> Journey Creation Agent replaces the previously released Journey Copilot for journey creation.

## Key capabilities

### Natural language journey scaffolding

Describe your journey in conversational language and the agent proposes a journey structure with steps, timing, and branching logic. You can ask follow-up questions or request changes before accepting the proposal.

### Multi-channel orchestration

The agent structures journeys across email, SMS, push notification and custom channels. It arranges touchpoints in a logical sequence and can set up if/then branches so different contacts receive the right message based on their behavior — for example, sending an SMS only to contacts who did not open the initial email.

### Journey preview and human approval

Before you publish, the agent presents a visual preview of the proposed journey. You can ask the agent for modifications or move to journey designer to review every step, modify the structure, swap in different content, or adjust timing. Nothing goes live until you approve it.

### Dynamics 365 data grounding

The agent works with your existing Customer Insights - Journeys configuration. It references your segments, triggers, and content when generating journey proposals, so the output is based on assets that already exist in your environment.

### Integration with the Microsoft ecosystem

Journey Creation Agent connects with other Dynamics 365 applications. You can describe journeys that start from events in Dynamics 365 Sales — such as when an opportunity is created or stalls — or from Dynamics 365 Customer Service events, such as when a case is resolved. This lets marketing and sales teams coordinate touchpoints without manual handoffs.

## Prerequisites

Before you use Journey Creation Agent, make sure you have:

- Enable Journey Creation Agent via **AI Hub**

> [!NOTE]
> Journey Creation Agent leverages Anthropic’s models. Please ensure your tenant is opted in via the Microsoft 365 admin center and Microsoft Power Platform admin center (PPAC) to allow Anthropic to be used. [Anthropic as a subprocessor for Microsoft Online Services | Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor)

- **Permissions**: Marketing Manager or Marketing Professional role, or equivalent permissions to create and publish journeys

> [!TIP]
> The agent assembles journeys from your existing assets. Having your content ready before starting the conversation makes the experience faster and more productive. You can also build the journey structure first and assign content afterward on the journey canvas.

## Integration with other features

Journey Creation Agent integrates with the following Dynamics 365 Customer Insights - Journeys features and applications:

- **Customer Insights - Data**: Uses unified contact and lead profiles and pre-built segments to define your journey audience.
- **Dynamics 365 Sales**: Journeys can be triggered by sales milestones such as opportunity creation, stalled deals, or won/lost outcomes, enabling coordinated sales-marketing outreach.
- **Dynamics 365 Customer Service**: Journeys can start from service events such as case creation or resolution, supporting post-service follow-up and customer retention scenarios.
- **Message Optimization Agent**: Works alongside the Journey Creation Agent to optimize send times and test message variants after the journey is live.

> [!IMPORTANT]
> Integration with Dynamics 365 Sales and Customer Service requires that those applications are part of your Dynamics 365 deployment and that the relevant connections are configured by your administrator.

## Create a journey with Journey Creation Agent

Journey Creation Agent lets you describe a journey in plain language and receive a proposed journey structure — including steps, timing, branching logic, and content assignments — ready for your review.

### Start a conversation with Journey Creation Agent

1. In Customer Insights - Journeys, go to **Journeys** in the left navigation.
1. Select **New journey**, then choose **Journey Creation Agent (preview)**.

### Describe your journey

In the agent conversation panel, type a description of what you want to accomplish. Be as specific as you like — the agent asks clarifying questions if it needs more information.

**Examples of effective prompts:**

- Create a 30-day re-engagement journey for contacts who haven't opened an email in 90 days. Start with the “We miss you” email and then send the “re-engagement” SMS if there's no response.
- Create a welcome journey that starts when a new contact is added to /Segment and sends onboarding emails over the first 10 days.
- Send an invite to /Segment for /Event. If they don’t register send a weekly reminder until a week before the event.

> [!TIP]
> Use the exact names of segments, triggers and content in your prompt. You can use / to search and identify any asset you want to use. Including your goal, audience, timeline, and preferred channels in your initial message produces a more complete first proposal. You can always refine the details in follow-up messages.

> [!TIP]
> There are a few out-of-the-box prompts to help you get started. Make sure to edit them to fit your process and the journey you want to build.

### Answer the agent's clarifying questions

The agent may ask follow-up questions to make the journey structure more accurate. Common questions include:

- Should the journey start on a specific date, immediately when a contact qualifies, or when a trigger event occurs?
- Are there specific content assets you want to use, or should the agent suggest options?

Select your answers from the options provided, or type a response in natural language.

> [!TIP]
> If you refresh the page while on this experience.

### Review the proposed journey structure

After you provide the necessary details, the agent presents a proposed journey. The proposal includes:

- **Journey type**: Segment-based or trigger-based
- **Steps**: Each email, SMS, and push notification touchpoint with suggested content assignments from your library
- **Wait periods**: Time delays between steps
- **Branching logic**: If/then conditions based on contact behavior, such as email opens or link clicks
- **Entry and exit conditions**: How contacts enter and leave the journey

![Screenshot of the Journey Creation Agent panel showing a proposed journey with a step-by-step outline and content assignments](Image)

Review each section of the proposal in the agent panel. If any part does not match your intent, use follow-up messages to refine it before opening the canvas.

### Refine the journey through conversation

You can request changes by typing follow-up messages in the agent panel. Changes are reflected in the updated proposal immediately.

**Examples of refinement prompts:**

- "Change the wait between step 2 and step 3 to three days instead of one."
- "Add a condition after the first email — if the contact clicks the link, skip the second email and go straight to the final step."
- "Replace the content assigned to step 1 with the 'Spring Campaign Welcome' email."
- "Make this journey trigger-based, starting when a new lead is created in Dynamics 365 Sales."

Continue refining until the proposed structure matches your requirements.

> [!NOTE]
> The agent works with segments and content assets that already exist in your Customer Insights - Journeys environment. If a segment or content asset you want to use does not yet exist, create it first, then return to the agent conversation.

### Open the journey in the journey designer

When the proposed structure looks right, select **Review and refine** in the agent panel. The journey opens on the standard journey canvas with all proposed steps, conditions, and content assignments populated.

You can modify any part of the agent-generated journey using the standard [journey designer](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/journeys-overview):

- **Add a step**: Select the plus sign (**+**) between any two steps on the canvas.
- **Remove a step**: Select the step, then select **Delete** in the step settings pane.
- **Change a condition**: Select the branching tile and update the condition in the settings pane.
- **Adjust a wait period**: Select the wait step and change the duration in the settings pane.

When the journey structure is correct you can publish the journey as you usually would.

## Troubleshoot Journey Creation Agent

### Journey Creation Agent option is not available

The **Journey Creation Agent (preview)** option does not appear when you select **New journey**.

**Possible causes and resolutions**:

- **Feature not enabled**: Your administrator may need to enable Journey Creation Agent in your environment. Contact your administrator and ask them to verify that the feature is turned on in **AI Hub**.
- **Insufficient permissions**: You need Marketing Manager or Marketing Professional role, or equivalent permissions that include journey creation rights. Contact your administrator to verify your role assignment.
- **Unsupported region**: The Journey Creation Agent may not be available in all regions at release. Check the [Dynamics 365 Customer Insights - Journeys feature availability by region](real-time-marketing-feature-availability.md) article for current availability.

### The agent does not recognize my segment, trigger or content assets

You refer to a specific segment or content asset in your conversation, but the agent says it cannot find it or assigns different content.

**Possible causes and resolutions**:

- **Asset not yet saved**: If you recently created a segment or content asset, wait a few minutes for it to become available, then try again.
- **Permissions**: You can only use segments and content assets that your user account has permission to access. Contact your administrator to verify access.

### The agent references a segment or trigger I didn't mention

The generated journey uses a segment or trigger that doesn't match what you described.

**Resolutions**:

- The agent may have matched a similarly named asset in your environment. Review the entry settings and replace the segment or trigger with the correct one.
- If no matching asset exists for what you described, the agent may fall back to an empty action for you to refine.

### The proposed journey does not match my description

The agent's proposal includes steps, channels, or timing that do not reflect what you described. The agent generates a journey, but some steps or channels you mentioned in your prompt are absent.

**Resolutions**:

- Confirm the channels and assets you mentioned exist in your environment. If you referenced a channel not yet configured (for example, push notifications when no push app is set up), the agent may omit those steps.
- Use follow-up messages in the agent conversation panel to correct specific elements. Be explicit about what needs to change.
- Add the missing steps manually using the journey designer. Select the plus sign (**+**) at the right position on the canvas and configure the step.

If the proposal continues to diverge significantly from your intent, try starting a new conversation with a more detailed initial description. Using / to select the right message, segment etc will also improve the journey proposed.

### The agent conversation is unresponsive or produces an error

The agent panel does not respond to your messages, shows a loading spinner for an extended time, or displays an error message.

**Possible causes and resolutions**:

- **Prompt contains restricted content**: Prompts that contain personally identifiable information (PII) or sensitive data may be blocked. Describe your audience in general terms rather than including specific customer details.
- **Temporary service issue**: Wait a moment and try sending your message again.
- **Session timeout**: If your session has been idle for an extended period, refresh the page and start a new conversation. Note that refreshing will discard the current proposal — if the proposal was already transferred to the journey builder by selecting **Review and refine**, your work is preserved.

If the issue persists, contact Microsoft Support with details about the error message displayed and the steps you took before the error occurred.

## Related information

- [Customer Insights - Journeys overview](real-time-marketing-overview.md)
- [Edit a live journey](real-time-marketing-edit-journey.md)
- [Journey analytics](real-time-marketing-analytics.md)