---
title: How to
description: Learn more about additional capabilities in Conversational journeys.
ms.date: 05/13/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# How to

To use conversational journeys you have to enable the feature switch Contact Center integration under the Integrations section. For more information, see [Use feature switches to enable or disable optional and preview features](admin-feature-switches.md#integrations).

Once enabled, Customer Insights Journeys will auto detect your Contact Center in the same environment.

The integration with Contact Center allows you to create conversational journeys by selecting a <!-- [proactive engagement](LINK) --> from Contact Center and design your journey based on its outcomes.

> [!NOTE]
> Conversational journeys work only with **Contact** based journeys.

## Using Conversational voice call tile and branch on its outcomes

To use Conversational voice call tile and branch on its outcomes:

1. When creating a journey, you can add an action and choose **Voice conversation**
    
1. Choose a **proactive engagement**  
    
1. Once you select a Proactive engagement, you must select:
    -   The **compliance profile** you want to use
    -   **Purpose**
    -   **Topic** (if applicable)
    -   **Quite time** option. You can always choose “Don’t apply quiet time to this message”

1. To branch based on your proactive engagement outcomes, add a **Wait for trigger** action and choose a branch condition type of “**Previous message gets an interaction”**.
    
1. In the branches, you can choose the following triggers:
    -   **Voice call attempted**: It means that Contact Center had attempted to make the phone call to the Contact. Please be aware that a call attempted does not necessarily mean that the Contact had answered.
    -   **Voice call not attempted**: It means that Contact Center did not attempt to make a phone call.
    -   **Voice call blocked**: It means that Customer Insights Journeys blocked the call from being attempted and did not send the request to Contact Center.

1. Add **Attribute branch** action, and choose **Branch on** “A voice call is attempted”  

1. In the attribute branches you can choose what conditions you want to branch on.  
    Within “Voice call attempted” you'll have default variables: **Disposition Codes** and **Result**, and variables based on how you set up your proactive engagement (for example, Outcome).

    Up to your use case, you can choose any combination of these variables to design your branching logic.  

1. Once done, you can publish your journey.

## Voice consent and compliance profiles

In Dynamics 365 Customer Insights - Journeys, a compliance profile are the hubs that govern how consent is managed for outbound communications. It defines the legal and regulatory framework under which messages are sent—such as whether a message is considered transactional or promotional—and ensures that appropriate consent (opt-in or opt-out) is obtained and respected. When setting up a journey in CIJ, selecting a compliance profile allows you to associate each message with a specific purpose, aligning with privacy laws.

You need a compliance profile to ensure that your voice communications adhere to legal standards and customer preferences. It enables features like unsubscribe links, quiet time enforcement, and consent tracking, which are critical for avoiding legal risks and maintaining customer trust. This is especially important in scenarios involving high-volume outreach, such as autonomous agents or marketing campaigns, where managing consent at scale is essential

To learn about how to create and manage compliance profiles, see [Consent management overview](real-time-marketing-compliance-settings.md).

## Quiet times and conversational voice

In Dynamics 365 Customer Insights - Journeys, quiet times are configurable time windows during which outbound communications are suppressed to respect customer preferences and legal constraints. These settings are important for voice calls because they help ensure compliance with regulations like the Telecommunication Consumer Protection Act (TCPA), which restricts when businesses can contact individuals based on their local time zones.

Quiet times are useful because they prevent calls from being placed during inappropriate hours (for example, late at night or early morning), which could otherwise lead to customer dissatisfaction or legal penalties.

To learn about how to create and manage quiet times, see [Set quiet times to prevent messages from sending during unwanted hours](real-time-marketing-quiet-times.md)
