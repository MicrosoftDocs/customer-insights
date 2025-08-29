---
title: Transition settings from outbound marketing to real-time journeys
description: How setting up real-time journeys differs from outbound marketing setup in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/28/2025
ms.topic: install-set-up-deploy
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition settings from outbound marketing to real-time journeys

Before you transition to real-time journeys, make sure your core configurations are up to date. Some settings work differently between outbound marketing and real-time journeys. When you transition to real-time journeys, settings don't migrate automatically. Here's a summary of the key configurations to review and update.

## Email and content settings

| Setting | Outbound marketing | Real-time journeys |
|---|---|---|
| **Social media links** | Social media links are under **Default settings** > **Marketing email** > **Content settings**. | Social media links are managed under **Brand profiles** > **Social links**. Create separate profiles for each brand and assign unique social media links to each one. Learn more: [Brand profiles](brand-profiles.md).|
| **Email senders** | Email senders are under **Default settings** > **Marketing email**. | Email senders are configured under **Brand profiles** > **Senders**. Each brand profile can have multiple email senders assigned to it. For each sender, define: <br>- **From name**: The display name shown to recipients. <br>- **From email**: The email address used to send messages. <br>- **Reply-to email**: The address where replies are directed. <br>- **Default sender**: The primary sender used by default for the brand. |
| **Sending domains** | Sending domains are under **Default settings** > **Marketing email**. | Within each **brand profile**, you can configure multiple senders using the appropriate domain. One of these senders can be designated as the **default sender** for that brand, which is used automatically. |
| **Litmus integration** | Litmus integration is set under **Default settings** > **Marketing email**. | Turn on Litmus integration under **Feature switches** > **Email editor** > **Litmus integration**. |
| **Email deduplication** | Marketing email deduplication is under **Default settings** > **Global-level double opt-in**. | Email deduplication is configured under **Feature switches** > **Email deduplication**. |

## Journey settings

| Setting | Outbound marketing | Real-time journeys |
|---|---|---|
| **Journey time zone** | The default time zone is set under **Default settings** > **Customer journey**. | To set the default time zone, go to **Journey settings** > **General**. The default time zone applies to all your journeys. If needed, override it for a specific journey by updating the time zone directly in the journey. |

## Consent settings

| Setting | Outbound marketing | Real-time journeys |
|---|---|---|
| **Double opt-in** | Set double opt-in under **Default settings** > **Global-level double opt-in**. | To set up double opt-in, go to **Compliance profiles** > **Select a compliance profile** > **Double opt-in**. Choose the compliance profile where you want to enable double opt-in. |

[!INCLUDE [footer-include](./includes/footer-banner.md)]