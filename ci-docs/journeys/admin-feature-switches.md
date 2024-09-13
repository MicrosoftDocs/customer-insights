---
title: Use feature switches to enable or disable optional and preview features
description: Learn how to use the feature switches page to enable or disable optional and preview features in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/13/2024
ms.topic: article
author: alfergus
ms.author: alfergus
ms.collection: bap-ai-copilot
---

# Use feature switches to enable or disable optional and preview features

Use the **Feature switches** page to enable or disable optional and preview features in Dynamics 365 Customer Insights - Journeys.

To enable or disable a feature, go to **Settings** > **settings** under Overview > **Feature switches** and set the various feature sliders to **On** or **Off** as needed. After you set the feature sliders, click **Save** in the upper right corner of the window.

The following tables list each available feature, preview status, and links for more information.

## Analytics

| Feature switch | Preview or production | Description |
|---|---|---|
| Marketing effectiveness analytics | Preview | [Understand the contribution of your marketing activities towards key milestones in your buyer's journey.](real-time-marketing-effectiveness.md)|

## Business units

| Feature switch | Preview or production | Description |
|---|---|---|
| Business unit scoping (outbound marketing) | Production | [Enable business unit scoping for marketing processes in outbound marketing.](business-units.md)|
| Business unit scoping (real-time journeys)|Production| [Enable business unit scoping for marketing processes in real-time journeys.](real-time-marketing-business-units.md) |

## Tracking

| Feature switch | Preview or production | Description |
|---|---|---|
| UTM tracking | Production | [Enable UTM values to be automatically added to every link in your messages. This allows source tracking within third-party tools like Google Analytics.](real-time-marketing-utm.md)|
| Bot protection | Production| [Filter out non-human click interactions.](bot-protection.md) |

## Event management

| Feature switch | Preview or production | Description |
|---|---|---|
| Event registration forms | Preview | [Enable marketing forms to submit event registrations.](event-forms.md)|
| Enable events creation in real-time journeys | Production | [Enable events creation in real-time marketing.](set-up-event.md)|
| Enable session level registration in real-time journeys| Production | [Enable session level registration in real-time journeys.](session-level-registration-outbound.md) |

## Customer journey

| Feature switch | Preview or production | Description |
|---|---|---|
| Updated customer journey designer | Production | [Enable the redesigned customer journey design workspace.](customer-journeys-create-automated-campaigns.md)|
| CC recipients for emails | Production | [Enable adding email CC recipients. Their interactions with sent emails (open, forward, unsubscribe) will be counted as a primary recipient interaction against quota and will affect your insights and analytics.](real-time-marketing-add-cc-recipients.md)|

## Email editor

| Feature switch | Preview or production | Description |
|---|---|---|
| Enhanced HTML controls | Preview | [Enable custom code markup and real-time HTML email editing.](email-creation-with-html-edits.md) |
| Live email editing with Link alias | Preview | [Enable editing personalization and conditional content in live email with link alias.](edit-email-in-live-journey.md) |
| Easy email creation experience | Production | [Enable easy content creation with in-place editing and an improved template gallery.](real-time-marketing-email.md)|
| Send now | Preview | [Enable Send Now to send emails without having to build a journey.](email-without-journey.md)|
| View in browser | Production | [Enable adding a link to view emails in web browsers.](view-email-in-browser.md) |

## Copilot

| Feature switch | Preview or production | Description |
|---|---|---|
| Global opt-in consent | Production | [Consent to enable Copilot and/or Bing Search-powered features.](https://go.microsoft.com/fwlink/?linkid=2255531) |
| Global data sharing consent | Production | Allows data sharing for Copilot features. |

## Library

| Feature switch | Preview or production | Description |
|---|---|---|
| AI tagging for images | Preview | [Enable AI-generated tags to be added when you upload images to the asset library.](upload-images-files.md) |

## Data sharing program

| Feature switch | Preview or production | Description |
|---|---|---|
| Azure Content Delivery Network (CDN) | Production | [Disable Azure Content Delivery Network (CDN) for Customer Insights - Journeys.](cdn-disabling.md) |

## Email sending

| Feature switch | Preview or production | Description |
|---|---|---|
| Email deduplication | Preview | [Disallows sending the same email more than once to an email address. This is a general setting that applies to all segment-based journeys.](email-deduplication.md) |
| One-click unsubscribe |Production | [Enable one-click unsubscribe for supported email clients. This feature allows recipients to unsubscribe from commercial email without visiting a preference center.](one-click-unsubscribe.md) |

## Contact timeline

| Feature switch | Preview or production | Description |
|---|---|---|
| Show exact copy of sent emails | Production| [Enable saving an exact copy of sent emails on contact timeline.](view-previously-sent-emails.md) |

## Forms

| Feature switch | Preview or production | Description |
|---|---|---|
| Form capture | Production | [Enable form capture in real-time journeys.](real-time-marketing-form-capture.md) |
| Enable custom JavaScript in forms |Production | [If disabled, custom JavaScript is automatically removed from real-time journey forms.](real-time-marketing-manage-forms.md#add-custom-javascript-to-your-form) |
| Form prefill | Preview | [Enable form prefill in real-time journeys.](form-prefill.md) |

## Journey

| Feature switch | Preview or production | Description |
|---|---|---|
| Lead and opportunity creation | Preview | [Enables the creation of leads and opportunities within journeys using built-in journey activities.](lead-generation-overview.md) |
| Tile entry and exit analytics | Preview | [View additional information on journey tiles, such as which customers entered a journey step, which customers have exited the journey, and why they exited the journey.](real-time-marketing-tile-reference.md) |

## Integrations

| Feature switch | Preview or production | Description |
|---|---|---|
| Customer Voice integration | Production | [Enable Dynamics 365 Customer Voice integrations with Customer Insights - Journeys.](customer-voice.md) |

## Compliance

| Feature switch | Preview or production | Description |
|---|---|---|
| Check contact consent in real-time journeys | Production| [Enable real-time journeys to use contact attributes to enforce consent in addition to contact point consent records.](real-time-marketing-compliance-settings.md) |
| Double opt-in | Preview| [Enable double opt-in functionality for real-time journeys. Forms created or modified after enabling this feature link to a compliance profile and inherit its double opt-in status.](real-time-marketing-double-opt-in.md) |

## Lead management

| Feature switch | Preview or production | Description |
|---|---|---|
| Lead scoring | Production| [Create scoring model to identify the best leads and define qualification criteria for marketing qualified leads.](set-up-lead-scoring.md) |

## Machine learning

| Feature switch | Preview or production | Description |
|---|---|---|
| Smart scheduler | Production | [Automatically select the best time to send an email message.](automated-scheduler.md) |

> [!IMPORTANT]
> [!INCLUDE [cc_preview_features_definition](./includes/cc-preview-features-definition.md)]
> [!INCLUDE [cc_preview_features_no_MS_support](./includes/cc-preview-features-no-ms-support.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
