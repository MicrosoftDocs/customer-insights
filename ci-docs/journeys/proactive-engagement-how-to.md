---
title: Create conversational journeys
description: Conversational journeys in Dynamics 365 Customer Insights let you design voice call experiences using Contact Center integration. Learn how to set up and branch journeys.
ms.date: 05/07/2026
ms.topic: article
author: vinayd-msft
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:05/27/2025
---

# Create conversational journeys

To use conversational journeys, enable the **Contact Center integration** feature switch under the **Integrations** section. For more information, see [Use feature switches to enable or disable optional and preview features](admin-feature-switches.md#integrations).

After you enable the feature, Customer Insights - Journeys automatically detects Dynamics 365 Contact Center if it's in the same environment.

The integration with Contact Center lets you create conversational journeys by selecting a [proactive engagement](proactive-engagement-concepts.md#proactive-engagement) from Contact Center and designing your journey based on its outcomes.

> [!IMPORTANT]
> Conversational journeys can only be **contact-based** journeys. You can't use leads or customer profiles as a conversational journeys audience.

Here's a short video that demonstrates how to create a conversational journey for the text message (SMS) channel.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=4dde461b-35a8-420b-8a02-90aff1001c7e]

## Use a voice or text messaging (SMS) conversation step and branch on its outcomes

To use a voice or text conversation step and branch on its outcomes:

1. When creating a journey, add an action, then choose one of the available AI powered-conversation actions.

    :::image type="content" source="media\ai-powered-conversation-steps.png" alt-text="Add an action and choose voice conversation." lightbox="media/ai-powered-conversation-steps.png":::

1. Choose a **Proactive engagement**.

    | For voice | For text messaging (SMS) |
    |---|---|
    | :::image type="content" source="media/proactive-engagement-select.png" alt-text="Choose a proactive engagement configuration for voice." lightbox="media/proactive-engagement-select.png"::: | :::image type="content" source="media/proactive-engagement-select-for-sms.png" alt-text="Choose a proactive engagement configuration for text messaging." lightbox="media/proactive-engagement-select-for-sms.png"::: |

1. Configure the channel-specific settings:

    | For voice | For text messaging (SMS) |
    |---|---|
    |    - Select the **compliance profile** you want to use. <BR>    - Select the **Purpose** (and the **Topic**, if applicable). <BR>    - Select a **Quiet time** option. You can always choose "Don't apply quiet time to this message."|    - Select an existing text message (or create a new one) used as the first message to initiate the conversation. <BR>    - There's no option to select **Compliance profile**, it's selected on the text message itself. <BR>    - Select a **Quiet time** option. You can always choose "Don't apply quiet time to this message." |
    |     :::image type="content" source="media/voice-conversation-expanded.png" alt-text="Configure proactive engagement fields for voice." lightbox="media/voice-conversation-expanded.png"::: |     :::image type="content" source="media/sms-conversation-expanded.png" alt-text="Configure proactive engagement fields for SMS." lightbox="media/sms-conversation-expanded.png"::: |

1. Create branches to take action based on conversation outcomes. (Learn more about taking action based on outcomes in the next section.)

After you're done, publish your journey.

## Take action after a conversation

A voice or text message (SMS) conversation can have many more nuanced outcomes or results than simple "success" or "failed." For example, a voice call may get a busy signal or a text message failed because the phone number isn't for a mobile device. There are other cases where a connection was established but a conversation didn't take place or was interrupted, or needed to be handed off to a human agent.

You may need to check up to three different variables to understand what happened and how to take the appropriate actions:

- **Disposition codes**: These values are set by the service representative to classify the result of voice or SMS conversations they handled and are configured in Contact Center (see [Configure disposition codes](/dynamics365/contact-center/administer/configure-disposition-codes)).
- **Result**: These are the outcomes returned by Contact Center for a proactive engagement request. See [Outcomes for proactive engagement](/dynamics365/contact-center/administer/proactive-engagement-outcomes) for list of values returned and their meaning.
- **Attributes**: These are data values set by the AI agent and are valid only for connected calls and SMS conversations where the AI agent has an active conversation. These attributes are configured in Contact Center (see [Send data back from AI agent to Dynamics 365 Contact Center](/dynamics365/contact-center/administer/configure-agentS-for-ai-led-proactive-engagement#send-data-back-from-ai-agent-to-dynamics-365-contact-center)).

### Branching after a voice conversation

1. Add a **Wait for trigger** action after the voice conversation step and choose the **Previous message gets an interaction** branch condition type.

    :::image type="content" source="media/previous-message-interaction.png" alt-text="Screenshot of setting the previous message gets an interaction condition type." lightbox="media/previous-message-interaction.png":::

1. In the branches, choose one of the following triggers:

    - **Voice call attempted**: Contact Center attempted to establish a conversation. If the attempt failed, it was for a reason that's temporary in nature (for example, reached voice mail), so, a retry after sometime may succeed.
    - **Voice call not attempted**: Contact Center was unable to establish a conversation for reasons that aren't likely to change (for example, bad phone number), so, a retry later won't help. Switching to a different channel (for example, email) should be considered.
    - **Voice call blocked**: The journey didn't send a request to Contact Center (for example, we don't have consent to contact them or no allowed contact windows were available due to quiet time settings).

    :::image type="content" source="media/choose-triggers.png" alt-text="Choose a trigger." lightbox="media/choose-triggers.png":::

1. Add an **Attribute branch** action and choose **Branch on** “A voice call is attempted.”

    :::image type="content" source="media/attribute-voice-call.png" alt-text="Add an attribute branch on 'A voice call is attempted.'" lightbox="media/attribute-voice-call.png":::

1. In the attribute branches, choose which conditions you want to branch on. Within “Voice call attempted” there are default variables (**Disposition Codes** and **Result**) and variables based on how you set up your proactive engagement (for example, **Outcome**).

    :::image type="content" source="media/conversational-voice-condition.png" alt-text="Choose conditions for the attribute branch." lightbox="media/conversational-voice-condition.png":::

1. Depending on your use case, you can choose any combination of these variables to design your branching logic.

    :::image type="content" source="media/attribute-voice-call-combination.png" alt-text="Select variable as condition on voice call results for attribute branch." lightbox="media/attribute-voice-call-combination.png":::

### Branch after a text message (SMS) conversation

Select the **create branches** link within the text message conversation action. This creates the entire branching structure for you.

:::image type="content" source="media/previous-message-interaction-sms.png" alt-text="Screenshot of branching structure creation." lightbox="media/previous-message-interaction-sms.png":::

The branching structure is a two-step branching (this is the same structure as described in the voice conversation section above). The first step checks if the conversation has a valid outcome or if it timed out. The conversation result path has an attribute condition step where you can set up additional branches based on specific conditions. Some examples include:

- A branch where the conversation completed successfully, for example, (Result = Conversation Closed).
- A branch where the conversation didn't occur and a retry might help, for example, (Result = Response Timeout).
- A branch where the conversation didn't occur and a retry won't likely help (so you should switch to another communication channel or take alternative actions), for example, (Return code = Conversation Cancelled).

Here's an example of specific branch conditions where the AI agent sets attribute "FavoriteColor" to what it determines the recipient's choice is after a conversation:

:::image type="content" source="media/conversational-text-branching.png" alt-text="Setting up branch condition after an SMS conversation." lightbox="media/conversational-text-branching.png":::

## Consent and compliance profiles

In Customer Insights - Journeys, compliance profiles govern how you manage consent for outbound communications. Voice conversations have separate compliance profiles, whereas Contact Center-based text message (SMS) conversations use the same profiles meant for normal text messages (SMS). Compliance profiles define the legal and regulatory framework for sending messages, like whether a message is transactional or promotional, and make sure you get and respect the right consent (opt-in or opt-out). When you set up a journey in Customer Insights - Journeys, select a compliance profile to link each message to a specific purpose and align with privacy laws.

You can also use a compliance profile to ensure your voice and text messaging (SMS) conversations follow legal requirements and customer preferences. The compliance profile lets you add features like unsubscribe links, quiet time enforcement, and consent tracking. These features help you avoid legal risks and keep customer trust. This is especially important for high-volume outreach, like autonomous agents or marketing campaigns, where you need to manage consent at scale.

Learn more about consent management:

- [Consent management overview - Understand compliance profiles, Purposes, and Topics](real-time-marketing-compliance-settings.md)
- [Evaluate consent for voice channel](real-time-marketing-email-text-consent.md#how-consent-is-respected-for-voice-channel-by-default)

## Quiet times settings

In Customer Insights - Journeys, quiet times are configurable time windows during in which outbound communications are suppressed to respect customer preferences and legal constraints. These settings are even more important for voice calls because they help ensure compliance with regulations like the Telecommunication Consumer Protection Act (TCPA), which restricts when businesses can contact individuals based on their local time zones.

Quiet times are useful because they prevent calls from being placed during inappropriate hours (for example, late at night or early morning), which could otherwise lead to customer dissatisfaction or legal penalties.

To learn about how to create and manage quiet times, see [Set quiet times to prevent messages from sending during unwanted hours](real-time-marketing-quiet-times.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]