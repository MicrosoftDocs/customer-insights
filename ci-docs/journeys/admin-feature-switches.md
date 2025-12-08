---
title: Use feature switches to enable or disable optional and preview features
description: Use feature switches to manage optional and preview features in Dynamics 365 Customer Insights - Journeys. Learn the steps to configure settings.
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.topic: article
author: alfergus
ms.author: colinbirkett
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Use feature switches to enable or disable optional and preview features

Quickly manage optional and preview features in Dynamics 365 Customer Insights - Journeys using the **Feature switches** page.

To enable or disable a feature, go to **Settings** > **Overview** > **Feature switches** and set the various feature sliders to **On** or **Off** as needed. After you set the feature sliders, select **Save** in the upper right corner of the window.

The following tables list each available feature, preview status, and links for more information.

## Segmentation

| Feature switch | Preview or production | Description |
|---|---|---|
| Use protected fields in segments | Production | Allow the use of protected columns/fields in segment criteria in real-time marketing. Use with caution. [Learn more](protected-fields.md). |
| Use system command bar | Preview | Utilize the system command bar to enhance the segmentation user experience. This feature enables customers to customize the ribbon and activates default CRM actions. |

## Business units

| Feature switch | Preview or production | Description |
|---|---|---|
| Business unit scoping (outbound marketing) | Production | [Enable business unit scoping for marketing processes in outbound marketing](business-units.md).|
| Business unit scoping (real-time journeys)|Production| [Enable business unit scoping for marketing processes in real-time journeys](real-time-marketing-business-units.md). |

## Tracking

| Feature switch | Preview or production | Description |
|---|---|---|
| UTM tracking | Production | [Enable UTM values to be automatically added to every link in your messages. This allows source tracking within third-party tools like Google Analytics](real-time-marketing-utm.md).|
| Bot protection | Production| [Filter out nonhuman click interactions](bot-protection.md). |

## Event management

| Feature switch | Preview or production | Description |
|---|---|---|
| Event registration forms | Preview | [Enable marketing forms to submit event registrations](event-forms.md).|
| Enable events creation in real-time journeys | Production | [Enable events creation in real-time marketing](set-up-event.md).|
| Enable session level registration in real-time journeys| Production | [Enable session level registration in real-time journeys](session-level-registration-outbound.md). |
| Waitlist in Real-time Journeys | Preview | Enable waitlist functionality for events/sessions, allowing attendees to join a waitlist if an event or a session is full. |

## Customer journey

| Feature switch | Preview or production | Description |
|---|---|---|
| Updated customer journey designer | Production | [Enable the redesigned customer journey design workspace](customer-journeys-create-automated-campaigns.md).|
| CC recipients for emails | Production | Enable adding email CC recipients. Their interactions with sent emails (open, forward, unsubscribe) will be counted as a primary recipient interaction against quota and will affect your insights and analytics. [Learn more](real-time-marketing-add-cc-recipients.md).|

## Email editor

| Feature switch | Preview or production | Description |
|---|---|---|
| Enhanced HTML controls | Preview | [Enable custom code markup and real-time HTML email editing](email-creation-with-html-edits.md). |
| Live email editing with Link alias | Preview | [Enable editing personalization and conditional content in live email with link alias](edit-email-in-live-journey.md). |
| Easy email creation experience | Production | [Enable easy content creation with in-place editing and an improved template gallery](real-time-marketing-email.md).|
| Send now | Preview | [Enable Send Now to send emails without having to build a journey](email-without-journey.md).|
| View in browser | Production | [Enable adding a link to view emails in web browsers](view-email-in-browser.md). |
| Email clickmap | Preview | Understand customers' interactions and gain insights into which links receive the most and least engagement based on your email design. |
| Litmus integration | Production | By enabling Litmus, you agree to the Litmus [terms of service](https://www.litmus.com/terms) and [privacy policy](https://www.litmus.com/privacy) Litmus is an external, third-party product made available to you on an optional trial basis. It is subject to the [terms of service](https://www.litmus.com/terms) set forth by Litmus. This is not a Microsoft product so you must provide consent before Litmus can be enabled. |

## Copilot

| Feature switch | Preview or production | Description |
|---|---|---|
| Global opt-in consent | Production | [Consent to enable Copilot and/or Bing Search-powered features](https://go.microsoft.com/fwlink/?linkid=2255531). |
| Global data sharing consent | Production | Allows data sharing for Copilot features. |

## Library

| Feature switch | Preview or production | Description |
|---|---|---|
| AI tagging for images | Preview | [Enable AI-generated tags to be added when you upload images to the asset library](upload-images-files.md). |

## Data sharing program

| Feature switch | Preview or production | Description |
|---|---|---|
| Azure Content Delivery Network (CDN) | Production | [Disable Azure Content Delivery Network (CDN) for Customer Insights - Journeys](cdn-disabling.md). |

## Email sending

| Feature switch | Preview or production | Description |
|---|---|---|
| Email deduplication | Preview | [Disallows sending the same email more than once to an email address. This is a general setting that applies to all segment-based journeys](email-deduplication.md). |
| One-click unsubscribe |Production | Enable one-click unsubscribe for supported email clients. This feature allows recipients to unsubscribe from commercial email without visiting a preference center. [Learn more](one-click-unsubscribe.md). |

## Contact timeline

| Feature switch | Preview or production | Description |
|---|---|---|
| Show exact copy of sent emails | Production| [Enable saving an exact copy of sent emails on contact timeline](view-previously-sent-emails.md). |

## Forms

| Feature switch | Preview or production | Description |
|---|---|---|
| Form capture | Production | [Enable form capture in real-time journeys](real-time-marketing-form-capture.md). |
| Enable custom JavaScript in forms |Production | [If disabled, custom JavaScript is automatically removed from real-time journey forms](real-time-marketing-manage-forms.md#add-custom-javascript-to-your-form). |
| Form prefill | Preview | Enable form prefill in real-time journeys [Learn more](form-prefill.md). |
| Enable table-less layouts in Form editor | Production |Use Div containers instead of table-based layouts in Form editor. |
| Custom unmapped fields | Production | Enable custom unmapped fields. |

## Journey

| Feature switch | Preview or production | Description |
|---|---|---|
| Lead and opportunity creation | Preview | [Enables the creation of leads and opportunities within journeys using built-in journey activities](lead-generation-overview.md). |
| Tile entry and exit analytics | Preview | View additional information on journey tiles, such as which customers entered a journey step, which customers have exited the journey, and why they exited the journey.[Learn more](add-action.md). |
| Wait for segment membership | Production | Enhances the "Wait for trigger" tile (also known as the if/then tile) to verify and pause until the audience becomes a member of the specified segment. |
| Ongoing journey re-entry | Production | Enables an enhancement for ongoing journeys to allow audience members to re-enter journeys when rejoining the segments. |

## Integrations

| Feature switch | Preview or production | Description |
|---|---|---|
| Customer Voice integration | Production | [Enable Dynamics 365 Customer Voice integrations with Customer Insights - Journeys](customer-voice.md). |
| Contact Center integration | Preview | Enable Dynamics 365 Contact Center integrations with Customer Insights - Journeys. [Learn more](conversational-journeys-overview.md) |

## Compliance

| Feature switch | Preview or production | Description |
|---|---|---|
| Check contact consent in real-time journeys | Production| [Enable real-time journeys to use contact attributes to enforce consent in addition to contact point consent records](real-time-marketing-compliance-settings.md). |
| Double opt-in | Preview| Enable double opt-in functionality for real-time journeys. Forms created or modified after enabling this feature link to a compliance profile and inherit its double opt-in status. [Learn more](real-time-marketing-double-opt-in.md). |

## Lead management

| Feature switch | Preview or production | Description |
|---|---|---|
| Lead scoring | Production| [Create scoring model to identify the best leads and define qualification criteria for marketing qualified leads](set-up-lead-scoring.md). |

## Machine learning

| Feature switch | Preview or production | Description |
|---|---|---|
| Smart scheduler | Production | [Automatically select the best time to send an email message](automated-scheduler.md). |

> [!IMPORTANT]
> [!INCLUDE [cc_preview_features_definition](./includes/cc-preview-features-definition.md)]
> [!INCLUDE [cc_preview_features_no_MS_support](./includes/cc-preview-features-no-ms-support.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
