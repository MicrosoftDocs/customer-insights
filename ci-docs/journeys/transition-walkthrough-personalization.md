---
title: Transition personalization
description: Learn how to transition personalization from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 05/29/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition personalization

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Personalization in real-time journeys is accomplished differently than in outbound marketing. The differences are to achieve greater ease of use and additional capabilities that couldn't be achieved in outbound marketing (for example, conditional content without needing to use scripting). For email, the migration feature provided in the product automatically (see [Transition emails, journeys, and assets](transition-walkthrough-journeys.md)) moves most of the personalization from outbound marketing emails to real-time journeys emails except when equivalent personalization isn't currently supported in real-time journeys. 

## Guidance on specific capabilities

See below for guidance on specific capabilities that are currently unsupported or function differently in real-time journeys. For other capabilities not listed here, we don't have a published plan currently. It's recommended that you don't wait for these capabilities to complete your transition.

### 1. Import emails created in external editors

**Details**: Ability to create formatted emails in external emails along with personalization placeholders.
**Guidance**: HTML-based content that doesn’t include personalization can be imported. Personalization must be created within the email designer.

### 2. Option set for dynamic text

**Details**: Ability to use option sets in dynamic text (currently it only outputs numeric values). Option sets are supported in conditions.
**Guidance**: For an option set with few options, inline conditions can be used to output the desired verbose labels for the options. For larger option sets, add a calculated field that holds verbose labels for the options. Use this calculated field instead of the option set field.

[!INCLUDE [footer-include](./includes/footer-banner.md)]