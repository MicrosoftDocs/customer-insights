---
title: Use Customer Insights - Journeys interaction data in segments and measures
description: Learn how to use Customer Insights - Journeys behavioral interaction data in Customer Insights - Data segments and measures.
ms.date: 11/25/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: udag
ms.service: dynamics-365-customer-insights
ms.subservice: dynamics-365-customer-insights-data
ms.custom: bap-template
ai-usage: ai-assisted
---

# Use Customer Insights - Journeys interaction data in segments and measures

Behavioral interaction data from Customer Insights - Journeys, such as emails opened, links clicked, and forms submitted, is automatically available in Customer Insights - Data for use in segments and measures. You can combine unified customer profiles with real campaign engagement signals to build more precise audiences and scoring models.

[Customer Insights - Journeys records a behavioral interaction](../journeys/real-time-marketing-redesigned-segment-builder.md) every time a customer engages or doesn't engage with a marketing touchpoint. The system captures these interactions across email, push notifications, text messages, forms, and events. You can view the interaction data in tables under **System** on the **Tables** page. The system shows only tables that contain data.

## Prerequisites

- [Deploy Customer Insights - Journeys and Customer Insights - Data](../journeys/setup.md) in the same environment.
- [Unify data](data-unification.md) into unified customer profiles.

## Available interaction types

You can find Customer Insights - Journeys interaction data on the **Behavioral** tab in both the segment builder and the measure builder. The default relationship links the interaction's **ProfileId** to **Customer.CustomerProfileId** for CustomerProfile interactions. For other profile types, see [Use interactions recorded against other profile types](#use-interactions-recorded-against-other-profile-types).

The following interaction types are available across channels:

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

Each interaction type includes fields that you can use in conditions, such as Journey, Email, Email address, Email client, Timestamp, Profile ID, and Profile type.

> [!NOTE]
> Interaction data refreshes on the Customer Insights - Data system refresh schedule, not in real time. Segments and measures that use interaction data reflect the state of interactions as of the last successful refresh.

## Use interaction data in a segment

Use the **Behavioral** tab in the segment builder to filter unified customer profiles based on how they responded or didn't respond to your campaigns.

1. Go to **Insights** > **Segments** and select **New** > **Build your own**.

1. Select **Edit details** to name your segment.

1. In the **Add to Rule 1** side panel, select the **Behavioral** tab.

   :::image type="content" source="media/journeys-interactions-behavioral-tab.png" alt-text="Screenshot of the Behavioral tab in the segment builder side panel, showing the full list of Customer Insights - Journeys interaction types such as Email Opened, Email Sent, Form Submitted, and others.":::

1. Select an [interaction type](#available-interaction-types) to expand it and view its available fields, or use the **Search** box at the top of the **Behavioral** tab to find an interaction type or field by typing part of its name.

   > [!NOTE]
   > The search matches against the underlying field names, not the localized display names shown in the list. If you can't find an expected interaction type by its display name, try searching by a portion of its technical name, or select **Show display names** at the bottom of the panel to toggle between views.

1. Select a field, or drag it to Rule 1.

1. Configure the condition: set the operator, value, and optionally a time window (for example, *Email Opened in the last 7 days*).

1. Add more conditions or rules as needed, and then select **Save** and **Run** to evaluate the segment.

### Scenario: Add the Email field from Email Opened to a rule

To filter customers by the specific email they opened, add the **Email** field from the **Email Opened** interaction type to your rule.

1. On the **Behavioral** tab, expand **Email Opened**.

1. Select **Email** from the field list.

   The condition is added to Rule 1 on the canvas as:
   `EmailOpened : CustomerInsightsJourneysInteractions.Email is equal to`.

1. To select the specific email campaign to match, use the value dropdown in the rule condition.

   :::image type="content" source="media/journeys-scenario-email-choices.png" alt-text="Screenshot of the segment builder canvas showing Rule 1 with the condition 'EmailOpened: CustomerInsightsJourneysInteractions.Email is equal to', and the Email Opened interaction expanded in the side panel showing its available fields.":::

### Example scenarios

- **Re-engagement**: Customers who received an email but didn't open it in the past 30 days. Target them with a more compelling offer.
- **High-intent buyers**: Customers who clicked a product link in an email and also have a high lifetime value score from a predictive model.
- **Event attendees**: Customers who checked in to a marketing event in the past 90 days.
- **Non-responders**: Customers who were sent a push notification but it wasn't delivered. Investigate delivery issues or update contact preferences.

## Use interaction data in a measure

Use the **Behavioral** tab in the measure builder to create calculated attributes based on interaction counts or aggregated values across your unified profiles.

1. Go to **Insights** > **Measures** and select **New** > **Build your own**.

1. Select **Add dimension**, or start adding conditions directly in the builder.

1. In the side panel, select the **Behavioral** tab.

1. Select an [interaction type](#available-interaction-types) and field to use as the basis for your aggregation (for example, the count of *Email Opened* events per customer).

1. Configure the aggregation type (count, sum, average, min, max) and optional filters or time windows.

1. Save and run the measure.

Use measures built on interaction data as attributes in segment conditions. This capability enables scenarios such as segmenting customers with more than five email opens in the last 60 days.

## Limitations

- **Batch only**: The system processes interaction data in batch with each system refresh. Segments and measures don't reflect interactions in real time. For real-time journey branching based on interactions, use Customer Insights - Journeys.
- **Profile-linked interactions only**: Customer-based results include interactions that match a unified Customer Profile through the selected relationship.
- **Not surfaced in customer timeline**: Customer Insights - Journeys interaction data isn't shown on the customer profile timeline in Customer Insights - Data. Use Customer Insights - Journeys contact insights to view timeline data.
- **Ingestion time**: Initial ingestion can take 30 minutes to several hours for large environments, depending on data volume.
- **Segments and measures**: Behavioral interaction data from Customer Insights - Journeys is only available in segments and measures.

## Use interactions recorded against other profile types

The default relationship supports CustomerProfile IDs. For another profile type, such as Contact or Lead, configure a path that maps the interaction's `ProfileId` to Customer through the correct identifier.

| Profile type | `ProfileType` value | Identifier to match |
| --- | --- | --- |
| CustomerProfile | `msdynci_customerprofile` | `Customer.CustomerProfileId`, through the default system relationship |
| Contact | `contact` | The Contact identifier that maps to Customer |
| Lead | `lead` | The Lead identifier that maps to Customer |

Use the existing relationship and filter controls to configure this path.

### Example: Customers who opened an email sent to Contacts

Suppose a journey targets Contacts. You want a segment of unified customers who opened a specific email in the last 30 days.

For this example:

- The Contact table comes from the same Dataverse environment as the interactions.
- You ingest that table into Customer Insights - Data and include it in unification.
- A valid relationship maps its Contact IDs to Customer.

These contact-specific prerequisites apply to this example, not to the default CustomerProfile flow.

### Set up the relationship

1. Go to **Data** > **Tables** > **Relationships**.

1. Inspect the existing relationship from the ingested Contact table to Customer.

1. If the interaction-to-Contact relationship is missing, select **New relationship**.

1. Create a many-to-one relationship from **EmailOpened.ProfileId** to the Contact primary key, such as **Contact.contactid**.

1. Save the relationship. Leave the system CustomerProfile relationship unchanged.

The complete path is:

```text
EmailOpened.ProfileId -> Contact.contactid -> Customer
```

Use the actual table and key names in your environment. If Customer already exposes the correct Contact identifier, a direct relationship to that field is another option. Don't assume that the field is named `contactid`.

> [!IMPORTANT]
> Check which source IDs the path preserves. Several contacts can unify into one customer. A join to one retained Contact ID can miss other contacts' interactions. Duplicate matches can increase measure counts.

For more information, see [Relationships between tables and table paths](relationships.md).

### Use the Contact path in a segment

1. Create a customer segment and select a field from **Behavioral** > **Email Opened**.

1. Select the email to match.

1. In the same interaction rule, add **Profile type is equal to `contact`** and the required **Timestamp** condition. Combine these conditions with **AND**.

1. Select **Set relationship path** and choose the Contact-based path, not the system CustomerProfile path.

1. Save and run the segment.

The result contains unified customers reached through matching Contact interactions. It doesn't change the segment's audience to Contact records.

### Reuse the relationship in a measure

1. Create a customer measure that counts **ProfileId** in **Email Opened**, grouped by **CustomerId**.

1. In **Filter**, add **Profile type is equal to `contact`**, the email condition, and the required Timestamp condition.

1. In **Relationship path**, choose the same Contact-based path.

1. Save and run the measure.

Two matching email-open records for a Contact that maps once to a customer contribute a count of two. The explicit filter excludes records with another `ProfileType`.

The system stores the relationship once for that interaction table and can reuse it. Each saved segment or measure stores its own selected path and conditions. Another table, such as Email Sent, needs its own interaction relationship.

### Lead and other profile types

For lead interactions, use `ProfileType = lead` and a relationship to the correct lead identifier, such as **Lead.leadid**. That path must reach Customer.

For other supported profile types, verify the stored `ProfileType` value and the meaning of `ProfileId`. Then select the matching relationship path and add the corresponding condition.

## Related content

- [Create and manage segments](segments.md)
- [Create and manage measures](measures.md)
- [Data unification overview](data-unification.md)
- [Improve targeting using interaction data in segments (Customer Insights - Journeys)](../journeys/real-time-marketing-redesigned-segment-builder.md)
- [Access and interpret analytics (Customer Insights - Journeys)](../journeys/real-time-marketing-analytics.md)
- [Use Customer Insights - Data profiles and segments in Customer Insights - Journeys](../journeys/real-time-marketing-ci-profile.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
