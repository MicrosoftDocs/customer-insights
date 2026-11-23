---
title: Use feature switches to enable or disable optional and preview features
description: Explore feature switches in Dynamics 365 Customer Insights - Journeys by category. Use the Preview features only filter to find preview options.
ms.date: 11/23/2026
ms.update-cycle: 180-days
ms.topic: article
author: udag
ms.author: colinbirkett
ms.reviewer: udag
ms.collection: bap-ai-copilot
ai-usage: ai-assisted
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Use feature switches to enable or disable optional and preview features

Feature switches let administrators turn optional and preview features on or off in Dynamics 365 Customer Insights - Journeys. Use the **Feature switches** page to enable or disable capabilities for your environment.

## Find and change feature switches

1. Go to **Settings** > **Overview** > **Feature switches**.
1. Find the switch you want to change. Use **Search switches** to search by name or description, select a category tab, or select **All** to browse the categories together.
1. To quickly find preview features, turn on **Preview features only**. Turn it off to include switches without a preview label again.
1. Set the feature switches to **On** or **Off** as needed.
1. Select **Save** to apply your feature setting changes.

The **Preview features only** toggle filters the displayed switches. It doesn't enable or disable features and doesn't require you to select **Save**.

The following tables follow the category order on the **Feature switches** page. Preview labels identify switches marked as preview on that page; the absence of a preview label isn't a statement of general availability.

> [!NOTE]
> Consult your legal or privacy counsel to determine the consent and tracking settings appropriate for your organization.

## Copilot

| Feature switch | Description |
|---|---|
| Global data sharing consent | Allow data sharing for Copilot features. |
| Global opt-in consent | [Consent to enable Copilot or Bing Search-powered features](https://go.microsoft.com/fwlink/?linkid=2255531). |
| AI tagging for images (preview) | [Enable AI-generated tags when you upload images to the asset library](upload-images-files.md). |

## Business units

| Feature switch | Description |
|---|---|
| Business unit scoping | [Enable business unit scoping for marketing processes in real-time journeys](real-time-marketing-business-units.md). |

## Compliance

| Feature switch | Description |
|---|---|
| One-click unsubscribe | Enable one-click unsubscribe for supported email clients, so recipients can unsubscribe from commercial emails without visiting a preference center. [Learn about one-click unsubscribe](one-click-unsubscribe.md). |
| Check contact consent in real-time journeys | Enable additional contact-attribute consent checks for email and tracking when the audience is contacts. These checks supplement contact point consent checks. [Learn about contact consent checks](real-time-marketing-compliance-settings.md). |
| Double opt-in | Enable double opt-in for real-time journeys. [Learn about double opt-in](real-time-marketing-double-opt-in.md). |

## Email editor

| Feature switch | Description |
|---|---|
| Litmus integration | Enable an optional third-party inbox-preview integration. Review the Litmus [terms of service](https://www.litmus.com/terms) and [privacy policy](https://www.litmus.com/privacy) before enabling the integration. |
| PowerFx personalization formulas (preview) | Let marketers use Power Fx expressions in email personalization placeholders. [Learn about Power Fx formulas](power-fx-dynamic-text.md). |
| Filter email templates by language | Enable a language dropdown when selecting email templates to show templates matching the selected language. When disabled, templates in all languages are available. |
| Easy email creation experience | [Enable content creation with in-place editing and an improved template gallery](real-time-marketing-email.md). |
| View in browser | [Enable adding a link to view emails in web browsers](view-email-in-browser.md). |
| Show exact copy of sent emails | Enable viewing exact copies of sent emails on the contact timeline. This feature applies to emails sent after you enable it; copies are available for one year. [Learn about viewing sent emails](view-previously-sent-emails.md). |
| Dynamic content blocks | Enable dynamic content blocks. Updates to a dynamic content block automatically appear in emails that include it when you send them. [Learn about dynamic content blocks](content-blocks.md#static-vs-dynamic-content-blocks). |

## Forms

| Feature switch | Description |
|---|---|
| Form capture | [Enable form capture in real-time journeys](real-time-marketing-form-capture.md). |
| Enable custom JavaScript in forms | Control custom JavaScript in forms. [Learn about custom JavaScript in forms](real-time-marketing-manage-forms.md#add-custom-javascript-to-your-form). |
| Enable table-less layouts in form editor | Use `<div>` containers instead of table-based layouts in the form editor. |

<a id="integration-feature-switches"></a>

## Integrations

| Feature switch | Description |
|---|---|
| Contact Center integration | Enable Dynamics 365 Contact Center integrations with Customer Insights - Journeys. [Learn about conversational journeys](conversational-journeys-overview.md). |
| Customer Voice integration | Enable Dynamics 365 Customer Voice integrations with Customer Insights - Journeys. |

## Lead management

| Feature switch | Description |
|---|---|
| Lead scoring | [Create a scoring model](real-time-marketing-create-lead-scoring-model.md) to identify the best leads, and [define qualification criteria](real-time-marketing-qualify-leads.md) for marketing qualified leads. |

## Orchestration

| Feature switch | Description |
|---|---|
| Send now | [Enable Send Now to send emails without building a journey](email-without-journey.md). |
| CC recipients for emails | Enable adding CC recipients to emails. [Learn how to add CC recipients to emails](real-time-marketing-add-cc-recipients.md). |
| Email deduplication | Prevent duplicate sends to a shared email address at an email tile in a segment-based journey. Deduplication doesn't span different email tiles or journeys. [Learn about email deduplication](email-deduplication.md). |
| Record creation | Enable the creation of Dataverse records from journeys. [Learn about creating records and activities](create-records-activities.md). |
| Ongoing journey reentry | Make reentry available for ongoing journeys. Members can reenter when they leave and rejoin the starting segment if the journey's rejoin option is enabled. |

## Personalization

| Feature switch | Description |
|---|---|
| Use protected fields in personalization | Allow protected columns or fields in personalization. Use with caution. [Learn about protected fields in personalization](overriding-fls-attributes.md). |

## Segmentation

| Feature switch | Description |
|---|---|
| Use protected fields in segments | Let segments use protected columns or fields in criteria for real-time journeys. Use with caution. [Learn about protected fields in segments](protected-fields.md). |
| Query edit | Edit a segment query directly in an editor. |
| Edit live segments used in live journeys (preview) | Let users change a segment that's used by a live journey without stopping the journey or creating a new journey version. [Learn about editing live segments](edit-live-segments.md). |
| Segment templates | Enable templates for creating segments, including custom segment templates. [Learn about segment templates](real-time-marketing-segment-templates.md). |

## Tracking

| Feature switch | Description |
|---|---|
| UTM tracking | Enable UTM (Urchin Tracking Module) parameters in email and text-message links where tracking is permitted, for source tracking in third-party tools such as Google Analytics. [Learn about UTM tracking](real-time-marketing-utm.md). |

## Other

| Feature switch | Description |
|---|---|
| Azure Content Delivery Network (CDN) | [Disable Azure Content Delivery Network (CDN) for Customer Insights - Journeys](cdn-disabling.md). |

> [!IMPORTANT]
> [!INCLUDE [cc_preview_features_definition](./includes/cc-preview-features-definition.md)]
> [!INCLUDE [cc_preview_features_no_MS_support](./includes/cc-preview-features-no-ms-support.md)]
