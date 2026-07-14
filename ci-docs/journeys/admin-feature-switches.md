---
title: Use feature switches to enable or disable optional and preview features
description: Feature switches for Dynamics 365 Customer Insights - Journeys are listed by category, with preview or production status and links for more details.
ms.date: 07/09/2026
ms.update-cycle: 180-days
ms.topic: article
author: alfergus
ms.author: colinbirkett
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Use feature switches to enable or disable optional and preview features

Feature switches are settings that let administrators turn optional and preview features on or off in Dynamics 365 Customer Insights - Journeys without waiting for a full release update. Use the **Feature switches** page to quickly enable or disable these features for your environment.

To enable or disable a feature, go to **Settings** > **Overview** > **Feature switches** and set the various feature sliders to **On** or **Off** as needed. After you set the feature sliders, select **Save** in the upper right corner of the window.

The following tables list each available feature switch, organized by area, along with its preview or production status and a link to more information.

## Segmentation feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Use protected fields in segments | Production | Let segments use protected columns/fields in criteria for real-time marketing. Use with caution. [Learn about protected fields in segments](protected-fields.md). |
| Use system command bar | Preview | Use the system command bar to improve the segmentation experience. This feature lets you customize the ribbon and use default customer relationship management (CRM) actions. |

## Business unit feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Business unit scoping (real-time journeys) | Production | [Enable business unit scoping for marketing processes in real-time journeys](real-time-marketing-business-units.md). |

## Tracking feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| UTM tracking | Production | [Enable UTM (Urchin Tracking Module) parameters to be automatically added to every link in your messages. This allows source tracking within third-party tools like Google Analytics](real-time-marketing-utm.md).|
| Bot protection | Production | [Filter out nonhuman click interactions](bot-protection.md). |

## Event management feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Event registration forms | Preview | [Enable marketing forms to submit event registrations](event-forms.md).|
| Enable events creation in real-time journeys | Production | [Enable events creation in real-time marketing](set-up-event.md).|
| Enable session level registration in real-time journeys | Production | [Enable session level registration in real-time journeys](real-time-journeys-event-session.md). |
| Waitlist in Real-time Journeys | Preview | Enable waitlist functionality for events/sessions, allowing attendees to join a waitlist if an event or a session is full. |

## Customer journey feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Updated customer journey designer | Production | [Enable the redesigned customer journey design workspace](customer-journeys-create-automated-campaigns.md).|
| CC recipients for emails | Production | Enable adding email CC recipients. Their interactions with sent emails (open, forward, unsubscribe) will be counted as a primary recipient interaction against quota and will affect your insights and analytics. [Learn how to add CC recipients to emails](real-time-marketing-add-cc-recipients.md).|

## Email editor feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Enhanced HTML controls | Preview | [Enable custom code markup and real-time HTML email editing](email-creation-with-html-edits.md). |
| Live email editing with Link alias | Preview | [Enable editing personalization and conditional content in live email with link alias](edit-email-in-live-journey.md). |
| Easy email creation experience | Production | [Enable easy content creation with in-place editing and an improved template gallery](real-time-marketing-email.md).|
| Send now | Preview | [Enable Send Now to send emails without having to build a journey](email-without-journey.md).|
| View in browser | Production | [Enable adding a link to view emails in web browsers](view-email-in-browser.md). |
| Email clickmap | Preview | Understand customers' interactions and gain insights into which links receive the most and least engagement based on your email design. |
| Litmus integration | Production | By enabling Litmus, you agree to the Litmus [terms of service](https://www.litmus.com/terms) and [privacy policy](https://www.litmus.com/privacy). Litmus is an external, third-party product made available to you on an optional trial basis. It is subject to the [terms of service](https://www.litmus.com/terms) set forth by Litmus. This is not a Microsoft product, so you need to give consent before turning on Litmus. |

## Copilot feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Global opt-in consent | Production | [Consent to enable Copilot and/or Bing Search-powered features](https://go.microsoft.com/fwlink/?linkid=2255531). |
| Global data sharing consent | Production | Allows data sharing for Copilot features. |

## Library feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| AI tagging for images | Preview | [Enable AI-generated tags to be added when you upload images to the asset library](upload-images-files.md). |

## Data sharing program feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Azure Content Delivery Network (CDN) | Production | [Disable Azure Content Delivery Network (CDN) for Customer Insights - Journeys](cdn-disabling.md). |

## Email sending feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Email deduplication | Preview | [Prevents sending the same email more than once to an email address. This general setting applies to all segment-based journeys](email-deduplication.md). |
| One-click unsubscribe | Production | Enable one-click unsubscribe for supported email clients. This feature allows recipients to unsubscribe from commercial emails without visiting a preference center. [Learn about one-click unsubscribe](one-click-unsubscribe.md). |

## Contact timeline feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Show exact copy of sent emails | Production | [Enable saving an exact copy of sent emails on contact timeline](view-previously-sent-emails.md). |

## Forms feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Form capture | Production | [Enable form capture in real-time journeys](real-time-marketing-form-capture.md). |
| Enable custom JavaScript in forms | Production | [If disabled, custom JavaScript is automatically removed from real-time journey forms](real-time-marketing-manage-forms.md#add-custom-javascript-to-your-form). |
| Form prefill | Preview | Enable form prefill in real-time journeys. [Learn about form prefill](form-prefill.md). |
| Enable table-less layouts in form editor | Production | Use `<div>` containers instead of table-based layouts in the form editor. Existing forms are automatically converted to the table-less layout when edited. |
| Custom unmapped fields | Production | Enable custom unmapped fields. |

## Journey feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Lead and opportunity creation | Preview | [Lets journeys create leads and opportunities by using built-in journey activities](lead-generation-overview.md). |
| Tile entry and exit analytics | Preview | View additional information on journey tiles, such as which customers entered a journey step, which customers have exited the journey, and why they exited the journey. [Learn about journey tile actions](add-action.md). |
| Wait for segment membership | Production | Enhances the "Wait for trigger" tile (also known as the if/then tile) to verify and pause until the audience becomes a member of the specified segment. |
| Ongoing journey re-entry | Production | Lets audience members re-enter ongoing journeys when they rejoin the segments. |

## Integration feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Customer Voice integration | Production | [Enable Dynamics 365 Customer Voice integrations with Customer Insights - Journeys](customer-voice.md). |
| Contact Center integration | Preview | Enable Dynamics 365 Contact Center integrations with Customer Insights - Journeys. [Learn about conversational journeys](conversational-journeys-overview.md). |

## Compliance feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Check contact consent in real-time journeys | Production | [Enable real-time journeys to use contact attributes to enforce consent in addition to contact point consent records](real-time-marketing-compliance-settings.md). |
| Double opt-in | Preview | Enable double opt-in functionality for real-time journeys. Forms created or modified after enabling this feature link to a compliance profile and inherit its double opt-in status. [Learn about double opt-in](real-time-marketing-double-opt-in.md). |

## Lead management feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Lead scoring | Production | [Create scoring model to identify the best leads and define qualification criteria for marketing qualified leads](set-up-lead-scoring.md). |

## Machine learning feature switches

| Feature switch | Preview or production | Description |
|---|---|---|
| Smart scheduler | Production | [Automatically select the best time to send an email message](automated-scheduler.md). |

> [!IMPORTANT]
> [!INCLUDE [cc_preview_features_definition](./includes/cc-preview-features-definition.md)]
> [!INCLUDE [cc_preview_features_no_MS_support](./includes/cc-preview-features-no-ms-support.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
