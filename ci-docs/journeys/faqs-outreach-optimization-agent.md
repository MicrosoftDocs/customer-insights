---
title: Responsible AI FAQs for Outreach Optimization Agent
description: Discover how to use Journey Creation Agent in Dynamics 365 Customer Insights - Journeys responsibly. These FAQs provide essential guidelines and best practices.
ms.date: 05/05/2025
ms.update-cycle: 180-days
ms.topic: faq
author: Joni-M
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom: 
  - transparency-note
---

# Responsible AI FAQs for Outreach Optimization Agent

This document provides frequently asked questions about the Outreach Optimization Agent in Dynamics 365 Customer Insights – Journeys.

## What is the Outreach Optimization Agent?

The Outreach Optimization Agent is an AI-powered orchestration agent designed to optimize when and how often customer communications are sent. It analyzes historical engagement data and real-time signals to create and adjust messaging plans that improve engagement while reducing message fatigue.

## What can Outreach Optimization Agent do?

Outreach Optimization Agent optimizes when and how often messages are sent within customer journeys.

Specifically, Outreach Optimization Agent can:

- Determine the best send time based on historical engagement signals
- Control message cadence and follow-up frequency to reduce customer fatigue
- Execute goal-driven follow-up strategies within predefined scenarios

Outreach Optimization Agent focuses on **execution and optimization of messaging plans**, not content creation.

## What is the intended use of Outreach Optimization Agent?

Outreach Optimization Agent is intended to be used within **Dynamics 365 Customer Insights – Journeys** to improve engagement outcomes while maintaining responsible, predictable behavior.

The intended use includes:

- Optimizing follow-up timing and cadence in goal-oriented journeys
- Reducing manual effort required to analyze engagement data and adjust journeys
- Scaling personalization of send-time and follow-up decisions across large audiences
- Supporting marketers and sellers with AI-assisted execution, while keeping humans in control of goals, content, and constraints

Outreach Optimization Agent is **not intended** to:

- Generate or modify message content
- Interpret free-text replies or infer sentiment
- Make decisions outside explicitly defined scenarios and limits

## How was Outreach Optimization Agent evaluated? What metrics are used to measure performance?

Outreach Optimization Agent is evaluated based on **goal-aligned engagement outcomes**, rather than open-ended optimization.

Evaluation focuses on metrics relevant to each supported scenario, such as:

- Click-through rates, registrations, or attendance in event-based journeys
- Reduction in unnecessary follow-ups and message fatigue
- Improved efficiency compared to static or manually configured journeys

Outreach Optimization Agent follows the same evaluation and validation practices used for Copilot Studio agents, including functional testing, scenario validation, and Responsible AI reviews.

## What are the limitations of Outreach Optimization Agent? How can users minimize the impact of Outreach Optimization Agent limitations when using the system?

Current limitations of Outreach Optimization Agent include:

- Email-only channel support
- No message content generation or rewriting
- No understanding of free-text replies, sentiment, or intent
- Operation limited to predefined scenarios with fixed goals and exit conditions

### Mitigations

Users can minimize the impact of these limitations by:

- Ensuring message content is high quality and appropriate before optimization
- Setting conservative limits on follow-ups and retries
- Using Outreach Optimization Agent in scenarios where quantitative engagement signals are meaningful
- Keeping human review and oversight for content and business decisions

## What operational factors and settings allow for effective and responsible use of Outreach Optimization Agent?

Effective and responsible use of Outreach Optimization Agent depends on the following operational controls:

- **Consent and compliance settings**: Outreach Optimization Agent respects contact point consent, quiet times, and channel permissions
- **Journey configuration**: Explicit goals, exit criteria, and scenario selection
- **Capacity and infrastructure**: Proper configuration of Copilot Studio capacity and required enablement from AI Hub
- **Human-in-the-loop controls**: Users retain ownership of content, goals, and journey design

[!INCLUDE [footer-include](./includes/footer-banner.md)]