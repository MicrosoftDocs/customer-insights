---
title: Create conversational journeys
description: Conversational journeys in Dynamics 365 Customer Insights let you design voice call experiences using Contact Center integration. Learn how to set up and branch journeys.
ms.date: 05/29/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
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
> Conversational journeys work only with **contact-based** journeys.

## Using the Voice conversation tile and branching on its outcomes

To use the Voice conversation tile and branch on its outcomes:

1. When creating a journey, add an action and choose **Voice conversation**.

    :::image type="content" source="media/voice-conversation-tile.png" alt-text="Add an action and choose voice conversation." lightbox="media/voice-conversation-tile.png":::

1. Choose a **Proactive engagement**.

    :::image type="content" source="media/proactive-engagement-select.png" alt-text="2.	Choose a proactive engagement configuration." lightbox="media/proactive-engagement-select.png":::
    
1. After you select a proactive engagement, you must select:
    - The **compliance profile** you want to use.
    - The **Purpose**.
    - The **Topic** (if applicable).
    - A **Quiet time** option. You can always choose “Don’t apply quiet time to this message.”

    :::image type="content" source="media/voice-conversation-expanded.png" alt-text="Configure proactive engagement fields." lightbox="media/voice-conversation-expanded.png":::

1. To branch based on your proactive engagement outcomes, add a **Wait for trigger** action and choose a branch condition type of **Previous message gets an interaction**.

    :::image type="content" source="media/previous-message-interaction.png" alt-text="Add a Wait for trigger action and choose a branch condition type." lightbox="media/previous-message-interaction.png":::
    
1. In the branches, you can choose the following triggers:
    - **Voice call attempted**: Contact Center attempted to make the phone call to the contact. Be aware that a call attempted doesn't necessarily mean that the contact answered.
    - **Voice call not attempted**: Contact Center didn't attempt to make a phone call.
    - **Voice call blocked**: Customer Insights - Journeys blocked the call from being attempted and didn't send the request to Contact Center.

    :::image type="content" source="media/choose-triggers.png" alt-text="Choose a trigger." lightbox="media/choose-triggers.png":::

1. Add an **Attribute branch** action and choose **Branch on** “A voice call is attempted.”

    :::image type="content" source="media/attribute-voice-call.png" alt-text="Add an attribute branch on 'A voice call is attempted.'" lightbox="media/attribute-voice-call.png":::

1. In the attribute branches, choose which conditions you want to branch on. Within “Voice call attempted” you have default variables (**Disposition Codes** and **Result**) and variables based on how you set up your proactive engagement (for example, **Outcome**).

    :::image type="content" source="media/conversational-voice-condition.png" alt-text="Choose conditions for the attribute branch." lightbox="media/conversational-voice-condition.png":::

    Depending on your use case, you can choose any combination of these variables to design your branching logic.

    :::image type="content" source="media/attribute-voice-call-combination.png" alt-text="Select variable as condition on voice call results for attribute branch." lightbox="media/attribute-voice-call-combination.png":::

1. Once done, you can publish your journey.

## Voice consent and compliance profiles

In Customer Insights - Journeys, compliance profiles govern how you manage consent for outbound communications. Compliance profiles define the legal and regulatory framework for sending messages, like whether a message is transactional or promotional, and make sure you get and respect the right consent (opt-in or opt-out). When you set up a journey in Customer Insights - Journeys, select a compliance profile to link each message to a specific purpose and align with privacy laws.

You can also use a compliance profile to ensure your voice communications follow legal standards and customer preferences. The compliance profile lets you add features like unsubscribe links, quiet time enforcement, and consent tracking. These features help you avoid legal risks and keep customer trust. This is especially important for high-volume outreach, like autonomous agents or marketing campaigns, where you need to manage consent at scale.

Learn more about consent management:

- [Consent management overview - Understand compliance profiles, Purposes, and Topics](real-time-marketing-compliance-settings.md)
- [Evaluate consent for voice channel](real-time-marketing-email-text-consent.md#how-consent-is-respected-for-voice-channel-by-default)

## Quiet times and conversational voice

In Customer Insights - Journeys, quiet times are configurable time windows during in which outbound communications are suppressed to respect customer preferences and legal constraints. These settings are important for voice calls because they help ensure compliance with regulations like the Telecommunication Consumer Protection Act (TCPA), which restricts when businesses can contact individuals based on their local time zones.

Quiet times are useful because they prevent calls from being placed during inappropriate hours (for example, late at night or early morning), which could otherwise lead to customer dissatisfaction or legal penalties.

To learn about how to create and manage quiet times, see [Set quiet times to prevent messages from sending during unwanted hours](real-time-marketing-quiet-times.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]