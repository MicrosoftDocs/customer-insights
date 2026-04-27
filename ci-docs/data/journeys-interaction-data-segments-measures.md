---
title: Use Customer Insights - Journeys interaction data in segments and measures (preview)
description: Learn how to use Customer Insights - Journeys behavioral interaction data—such as email opens and link clicks—in Customer Insights - Data segments and measures.
ms.date: 04/27/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: alfergus
ms.service: customer-insights
ms.subservice: customer-insights-data
ms.custom: bap-template
---

# Use Customer Insights - Journeys interaction data in segments and measures (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Behavioral interaction data from Customer Insights - Journeys, such as emails opened, links clicked, and forms submitted, is automatically available in Customer Insights - Data for use in segments and measures. You can combine unified customer profiles with real campaign engagement signals to build more precise audiences and scoring models.

[Customer Insights - Journeys records a behavioral interaction](../journeys/real-time-marketing-redesigned-segment-builder.md) every time a customer engages with a marketing touchpoint - or fails to engage. The system captures these interactions across email, push notifications, text messages, forms, and events. Each interaction links to the contact or lead record that receives or triggers it.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Prerequisites

- [Deploy Customer Insights - Journeys and Customer Insights - Data](../journeys/setup.md) in the same environment.
- [Unify data](data-unification.md) that includes contacts or leads from Customer Insights - Journeys in unified Customer Profiles.

## Available interaction types

You can find Customer Insights - Journeys interaction data on the **Behavioral** tab in both the segment builder and the measure builder. The segment and measure builders only include interaction data linked to a unified **Customer Profile** in Customer Insights - Data. The builders don't include interactions associated with contacts or leads that aren't unified into a Customer Profile. To use contact- or lead-based interactions directly in journey branching and real-time targeting, use Customer Insights - Journeys.

The following interaction types are available:

**Email**
- Email Consent not given
- Email Blocked
- Email Bounced
- Email Delivered
- Email Link Clicked
- Email Opened
- Email Sent

**Push notifications**
- Push Notification Link Clicked
- Push Notification Not Sent
- Push Notification Opened
- Push Notification Sent

**Text messages**
- Text Message Bounced
- Text Message Delivered
- Text Message Link Clicked
- Text Message Not Sent
- Text Message Sent

**Events and forms**
- Marketing Event Check-in
- Event Registration Canceled
- Event Registration Created
- Form Submitted
- Form Visited

Each interaction type exposes fields you can use in conditions, such as Journey, Email, Email address, Email client, Timestamp, Profile ID, and Profile type. 

> [!NOTE]
> Interaction data refreshes on the Customer Insights - Data system refresh schedule, not in real time. Segments and measures that use interaction data reflect the state of interactions as of the last successful refresh.

## Use interaction data in a segment

Use the **Behavioral** tab in the segment builder to filter unified customer profiles based on how they responded - or didn't respond - to your campaigns.

1. Go to **Insights** > **Segments** and select **New** > **Build your own**.

1. Select **Edit details** to name your segment.

1. In the **Add to Rule 1** side panel, select the **Behavioral** tab.

   :::image type="content" source="media/journeys-interactions-behavioral-tab.png" alt-text="Screenshot of the Behavioral tab in the segment builder side panel, showing the full list of Customer Insights - Journeys interaction types including Email Opened, Email Sent, Form Submitted, and others.":::

1. Select an [interaction type](#available-interaction-types) to expand it and view its available fields or use the **Search** box at the top of the **Behavioral** tab to quickly find an interaction type or field by typing part of its name.

   > [!NOTE]
   > The search matches against the underlying field names, not the localized display names shown in the list. If you can't find an expected interaction type by its display name, try searching by a portion of its technical name, or select **Show display names** at the bottom of the panel to toggle between views.

1. Select a field or drag and drop it to add it to Rule 1.

1. Configure the condition - set the operator, value, and optionally a time window (for example, *Email Opened in the last 7 days*).

1. Add more conditions or rules as needed, and then select **Save** and **Run** to evaluate the segment.

### Scenario: Add the Email field from Email Opened to a rule

To filter customers by the specific email they opened, add the **Email** field from the **Email Opened** interaction type to your rule.

1. On the **Behavioral** tab, expand **Email Opened** by selecting it.

1. Select **Email** from the field list.

   The condition is added to Rule 1 on the canvas as
   `EmailOpened : CustomerInsightsJourneysInteractions.Email is equal to`.

   :::image type="content" source="media/journeys-scenario-email-added-to-rule.png" alt-text="Screenshot of the segment builder canvas showing Rule 1 with the condition 'EmailOpened: CustomerInsightsJourneysInteractions.Email is equal to', and the Email Opened interaction expanded in the side panel showing its available fields.":::

1. Use the value dropdown in the rule condition to select the specific email campaign to match.

### Example scenarios

- **Re-engagement:** Customers who received an email but didn't open it in the past 30 days - target them with a more compelling offer.
- **High-intent buyers:** Customers who clicked a product link in an email and also have a high lifetime value score from a predictive model.
- **Event attendees:** Customers who checked in to a marketing event in the past 90 days.
- **Non-responders:** Customers who were sent a push notification but it wasn't delivered - investigate delivery issues or update contact preferences.

## Use interaction data in a measure

Use the **Behavioral** tab in the measure builder to create calculated attributes based on interaction counts or aggregated values across your unified profiles.

1. Go to **Insights** > **Measures** and select **New** > **Build your own**.

1. Select **Add dimension** or begin adding conditions.

1. In the side panel, select the **Behavioral** tab.

1. Select an [interaction type](#available-interaction-types) and field to use as the basis for your aggregation
   (for example, count of *Email Opened* events per customer).

1. Configure aggregation type (count, sum, average, min, max) and optional filters or time windows.

1. Save and run the measure.

Use measures built on interaction data as attributes in segment conditions. This capability enables scenarios such as segmenting customers with more than five email opens in the last 60 days.

## Limitations

- **Batch only:** The system processes interaction data in batch with each system refresh. Segments and measures don't reflect interactions in real time. For real-time journey branching based on interactions, use Customer Insights - Journeys.
- **Profile-linked interactions only:** You can only access interactions linked to a unified Customer Profile. Interactions on contacts or leads that aren't yet unified don't appear. See the note at the top of this article.
- **Not surfaced in customer timeline:** Customer Insights - Journeys interaction data is intentionally not shown on the customer profile timeline in Customer Insights - Data. Use Customer Insights - Journeys contact insights for timeline views.
- **Ingestion time:** Depending on the volume of interaction data, the initial ingestion of interaction tables can take 30 minutes to several hours for large environments.

## Related information

- [Create and manage segments](segments.md)
- [Create and manage measures](measures.md)
- [Data unification overview](data-unification.md)
- [Improve targeting using interaction data in segments (Customer Insights - Journeys)](../journeys/real-time-marketing-redesigned-segment-builder.md)
- [Access and interpret analytics (Customer Insights - Journeys)](../journeys/real-time-marketing-analytics.md)
- [Use Customer Insights - Data profiles and segments in Customer Insights - Journeys](../journeys/real-time-marketing-ci-profile.md)
