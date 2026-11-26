---
title: Customer Insights quickstart guide
description: Use Customer Insights to unify customer data, create a loyalty segment, and send personalized reward emails. Follow this quickstart to get started.
ms.date: 11/09/2026
ms.topic: quickstart
ai-usage: ai-assisted
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customer Insights quickstart guide

Use Customer Insights to unify customer and loyalty data, build a segment for customers with more than 1,000 points, and send a personalized reward email. This quickstart shows how to connect the apps and publish a loyalty reward journey.

Think of a scenario where a retail giant wants to reward customers who surpass a loyalty point threshold. Each purchase earns loyalty points that you can redeem for exclusive discounts and rewards. The retailer has heaps of information about what people buy, how often they shop, and what they like. They track product purchases and loyalty card usage, generating thousands of data points. Translating the data into action, however, involves navigating a maze of data sources, manually building segments, and initiating cumbersome communication processes.

Now, imagine if the retailer implemented Dynamics 365 Customer Insights. By using Customer Insights, you can process data automatically, so the store understands what customers like and how they shop. Customer Insights then allows customers to actively shape marketing campaigns, choosing how and where they interact with the brand. Dynamics 365 Customer Insights empowers the retailer and you to create personalized, targeted experiences.

This guide explores a step-by-step process to seamlessly integrate, analyze, and utilize customer information, crafting tailored experiences that resonate with individual preferences and behaviors.

## Prerequisites

Before you begin:

1. [Install Customer Insights - Data and Customer Insights - Journeys on the same Dataverse environment](setup.md), and [set up Customer Insights - Data](../data/get-started.md).
1. Verify that you have permissions to configure data in Customer Insights - Data and create emails and journeys in Customer Insights - Journeys. See [Customer Insights - Data permissions](../data/user-roles.md) and [Manage user accounts, user licenses, and security roles](admin-users-licenses-roles.md).
1. Configure the email channel and a compliance profile for your reward email. Verify that your test recipients meet the configured consent requirements. Segment membership alone doesn't grant permission to send a message. See [Create an email](real-time-marketing-email.md) and [Configure consent management controls](real-time-marketing-compliance-settings.md).
1. Use test customer records and email addresses you control before sending to a production audience.

### Connect the apps

Verify that Customer Insights - Data shares data with the Dataverse environment used by Customer Insights - Journeys. In Customer Insights - Journeys, check **Settings** > **Data management** > **Customer Insights - Data connector**.

The connection might be discovered automatically. If it isn't, complete the integration setup and select **Connect**. See [Use Customer Insights - Data profiles and segments in Customer Insights - Journeys](real-time-marketing-ci-profile.md).

Connecting the apps makes profiles and segments available to journeys, but it doesn't replace data ingestion, unification, or refresh processing. Before you send, confirm that the required profiles, measures, and segment membership are available.

## Procedure

Follow these five steps to build and validate the loyalty reward journey.

### Step 1: Import data into Customer Insights - Data

Create data sources for the customer and loyalty information you need. Choose a connector that fits where your data is stored. Not every connector requires a Power Query dataflow.

For example, import:

- Customer records from an e-commerce system, including a customer identifier, name, and email address.
- Loyalty records from a loyalty card system, including a customer identifier, loyalty status, and loyalty points.
- Purchase records, if you need transaction data to calculate loyalty points.

:::image type="content" source="media/add-data-source-name.png" alt-text="Screenshot of the field for naming a new data source.":::

> [!NOTE]
> Customer Insights - Data supports connectors such as Microsoft Fabric OneLake, Azure Data Lake Storage, Microsoft Dataverse, and Power Query. Delta format is the native processing format. Where possible, choose a connector that attaches to your data rather than copying it.

> Learn more: [Data sources overview](../data/data-sources.md).

:::image type="content" source="media/list-of-data-sources.png" alt-text="Screenshot of the list of created data sources.":::

After you create your data sources, review the imported tables and resolve data quality issues before unification.

### Step 2: Create unified profiles and set up relationships

Run the data unification process to create a single profile for each customer:

1. Select the tables and columns that contain customer profile information.
1. Define deduplication rules within each table.
1. Define matching conditions across tables using suitable identifiers, such as a customer ID, email address, or phone number.
1. Choose the columns to include or merge in the unified profile, and run unification.

Don't use changing values such as loyalty points or purchase history as customer identifiers. Keep purchase transactions in a related table rather than treating each purchase as a separate customer profile. [Set up relationships between tables](../data/relationships.md) to use transaction data in segments and measures.

For example, a unified profile for a customer named John Smith might look like this:

| **Attribute** | **Value** |
|---|---|
|     Name    |     John Smith    |
|     Email    |     john.smith@example.com    |
|     Phone    |     +1 234 567 8901    |
|     Address    |     123 Main Street, New York, NY 10001    |
|     Age    |     35    |
|     Loyalty   Status    |     Gold    |
|     Loyalty   Points    |     1500    |
|     Gender    |     Male    |
|     Purchase   History    |     Shoes, Jacket, Backpack    |

The purchase history in this example is a summary; keep individual transactions in the related purchase table.

Learn more: [Data unification overview](../data/data-unification.md). You can optionally [enrich your profiles](../data/enrichment-hub.md) after unification.

### Step 3: Create a loyalty segment and optional insights

Use the unified data to identify the customers who qualify for the reward:

- **Measures**: If your source already contains each customer's current loyalty balance, use that value directly. If you need to calculate points from transaction data, create a customer measure first. Learn more: [Create and manage measures](../data/measures.md).

    :::image type="content" source="media/create-measures.png" alt-text="Screenshot of the screen for creating customer measures.":::

- **Segments**: Create a segment in Customer Insights - Data with the condition Loyalty Points > 1,000. Use the profile attribute or the measure you prepared. In **Insights** > **Segments**, activate the segment if needed, refresh it, and check **Last refreshed** for a successful refresh. Confirm that the segment has the expected members. Learn more: [Create and manage segments](../data/segments.md).

    :::image type="content" source="media/create-segments.png" alt-text="Screenshot of the screen for creating customer segments.":::

- **Predictions (optional)**: Predictions aren't required for this reward journey. For a more advanced scenario, use a product recommendation model to suggest products based on purchase behavior and customers with similar purchase patterns. Review the model's data requirements before you configure it. Learn more: [Create and manage predictions](../data/predictions.md).

    :::image type="content" source="media/use-predictions.png" alt-text="Screenshot of the predictions screen for analyzing customer data.":::

### Step 4: Create a personalized email and a segment-based journey

Use the unified customer profiles and the segment you created in Customer Insights - Data:

If the segment isn't visible in Customer Insights - Journeys or has no members, verify data sharing and segment membership in Dataverse before you continue. See [Use segments in Customer Insights - Journeys](../data/segments.md#use-segments-in-customer-insights---journeys).

1. In Customer Insights - Journeys, go to **Settings** > **Customer engagement** > **Audience configuration**. For **Customer profile**, map the email address field to use for recipients. Customer profiles don't have default recipient fields. Learn more: [Select the audience source for journeys](real-time-marketing-audience-data.md).
1. Go to **Channels** > **Emails** and create the reward email. Configure its sender, subject, compliance profile, and purpose.
1. Add dynamic text through the personalization controls. Use **Customer Profile** as the audience data for this Customer Insights - Data segment, and select the name and loyalty points fields or measures. Configure default values where needed. Learn more: [Personalize content](real-time-marketing-personalization.md).
1. Preview and test the email with representative data, then mark it as **Ready to send**.
1. Go to **Engagement** > **Journeys**, select **+New journey**, and choose **Segment-based**. Select the Customer Insights - Data segment, choose the frequency and start time, and select **Create**. For a single reward send, use a one-time journey with a static audience.
1. Add a **Send an email** step and select the reward email.

For example, your email might read as follows after personalization:

> Hi John,
>
> Congratulations! You earned 1,500 loyalty points. To thank you, here's a 20% discount on your next purchase. Use the code LOYAL20 at checkout.
>
> Your friends at Contoso

This example shows the rendered message, not dynamic-text syntax to paste into the editor. Replace the sample offer with your own terms.

Learn more: [Create a segment-based journey](real-time-marketing-segment-based-journey.md).

> [!NOTE]
> Lead scoring models score leads, not unified customer profiles. Lead scoring isn't required for this loyalty reward journey. Learn more: [Create lead scoring models](real-time-marketing-create-lead-scoring-model.md).

### Step 5: Validate, publish, and monitor the journey

Before you send to a production audience:

1. Verify the segment membership, recipient email mapping, personalization values, and consent settings by using a test audience.
1. Confirm that Customer Insights - Data finishes refreshing the profiles and measures that the journey uses. Align journey quiet times with the refresh window, including time for data to finish writing to Dataverse. Updated segment membership alone doesn't mean that all profile and measure values are ready. See [Align quiet times with Customer Insights - Data refresh](coordinate-ci-data-refresh-with-quiet-times.md).
1. Review the journey configuration and start time, and then select **Publish** when you're ready to send.
1. Monitor delivery and engagement in the journey analytics. Review delivery failures or blocked messages before expanding the audience. See [Access and interpret analytics](real-time-marketing-analytics.md).

Customers finish the journey when they complete its steps. You don't need to add an end tile or manually set the journey status to **Completed**. Learn more: [End a journey](journey-end.md).

## Summary

You connected Customer Insights - Data and Customer Insights - Journeys, unified customer records, created a loyalty segment, and configured a personalized reward journey. Use the journey's delivery and engagement results to refine your audience and message.

## Next steps

- [Send a targeted email blast in Customer Insights - Journeys](real-time-marketing-email-get-started.md).
- [Boost event engagement with journeys](real-time-marketing-event-registration-journey.md).
- [Create segments by using unified profiles and customer measures](unified-profile-segment-creation.md).
