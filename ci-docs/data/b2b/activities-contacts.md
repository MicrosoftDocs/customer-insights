---
title: Set up business contact activities
description: Define business contact activities in Customer Insights and map them to accounts and contacts. Follow this guide to display activities on customer timelines.
ms.date: 07/10/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.update-cycle: 1095-days
ms.custom: bap-template
---

# Set up business contact activities (preview)

[!INCLUDE [public-preview-banner](../includes/public-preview-banner.md)]

[!INCLUDE [b2b-note](../includes/b2b-note.md)]

Business contact activities are actions or events that business contacts perform. For example, these activities include transactions, support call duration, website reviews, purchases, or returns. One or more data sources contain these activities. By using Customer Insights, you can consolidate your contact activities from these data sources and associate them with customer profiles. These activities appear chronologically in a timeline on the customer profile. Include the timeline in Dynamics 365 apps by using the [Customer Insights - Data Timeline Integration](../activities-in-d365-timeline.md) or the [Customer Card Add-in](../customer-card-add-in.md) solution.

> [!TIP]
> In B2B environments, you can select between account tables and other tables. If you select an account table, the relationship path is automatically set. For other tables, define the relationship path over one or more intermediate tables until you reach an account table.

[!INCLUDE [public-preview-note](../includes/public-preview-note.md)]

## Prerequisites

- Add [data sources](../data-sources.md) that contain activities. Make sure each activity table has at least one field of type **Date** or **Datetime**.
- [Unify customer data into customer profiles](../data-unification.md).

## Define contact activities (preview)

For business accounts (B2B), use a *UnifiedContact* table to capture activities of contacts. You can see in the activity timeline for an account which contact was responsible for each activity. Most steps follow the customer activity mapping configuration.

> [!NOTE]
> To define contact-level activities, create a [*UnifiedContact*](data-unification-contacts.md) table.
>
> Each record in your activity data must have both **AccountID** and **ContactID** attributes.
  
1. Go to **Data** > **Activities**. Select **Configure activities**.

1. In the **Activity tables** step, select **Select tables** and choose the tables that have activity data. Select **Add**.

1. For each table, choose the following information:

   - **Activity type**: Choose from the semantic types, *Feedback*, *Loyalty*, *SalesOrder*, *SalesOrderLine*, and *Subscription*. If a semantic activity type isn't relevant for the new activity, choose a non-semantic type, *Other*, or *Create New* for a custom type.
   - **Primary key**: The primary key uniquely identifies a record. It shouldn't contain any duplicate values, empty values, or missing values.

   > [!NOTE]
   > The primary key for each row must remain consistent across data source refreshes. If a data source refresh changes the primary key for a row, the system deletes all old rows and inserts all new rows, which causes an increase in processing time.

1. Select **Next** for the **Activity fields** step.

1. For each table that has a semantic activity type, choose **Intelligent mapping** to use AI models for smart prediction of semantics, which saves time and accuracy. Intelligent mapping automatically determines the type of data in each column and maps it to the attributes.

1. Enter the following information for each table:

   - **Activity name**: Unique name for your activity.
   - **Timestamp**: Field that represents the start time or date of your activity.
   - **Event activity**: Field that is the event for this activity.
   - **Web address** (optional): Field containing a URL with information about this activity. For example, the transactional system that sources this activity. This URL can be any field from the data source, or it can be constructed as a new field using a Power Query transformation. The URL data is stored in the *Unified Activity* table, which can be consumed downstream by using [APIs](../apis.md).
   - **Additional detail** (optional): Field with relevant information for this activity.
   - **Show this activity in the timeline on your customer profile?**: **Yes** to show the activity in the timeline or **No** to hide it.
     > [!NOTE]
     > If you select **No** and hide the activity in the timeline view, the [Customer Insights - Data API](../apis.md) doesn't return the activity either.
   
   - **Map field types for your activity's attributes?**: **Yes** to help the system better understand the relevance of your activity data or **No** to not map.

1. If you chose **Yes** to map your field types, select the appropriate attributes to map your data. Required fields are determined by the selected activity type.

1. Select **Next**.

1. In the **Relationship** step, select **Add relationship** and create an indirect relationship between your activity source data to accounts, using your contact data as an intermediary table. For more information, see [direct and indirect relationship paths](../relationships.md#relationship-paths).

   - Example relationship for an activity called *Purchases*:
      - **Purchases Source Activity Data** > **Contact Data** on the attribute **ContactID**
      - **Contact Data** > **Account Data** on the attribute **AccountID**
     > [!NOTE]
     > You can't configure activities by using [inherited relationships](../relationships.md#non-editable-system-relationships).

   :::image type="content" source="media/Contact_Activities1.png" alt-text="Screenshot of an example relationship setup.":::

1. Select **Apply** to create the relationship, and then select **Next**.

1. In the **Review** step, verify your selections. Go back to any of the previous steps and update the information if necessary.

1. To save your changes, select **Save and close**. To save your changes and create the activities, select **Create activities**.

1. After creating the contact-level activities, you can see the information on your customer timeline.

   :::image type="content" source="media/Contact_Activities2.png" alt-text="Screenshot of the final result after configuring contact activities.":::

## Contact-level activity timeline filtering

After you configure and run a contact-level activity mapping, the activity timeline for your customers updates. It includes their IDs or names, depending on your *UnifiedContact* configuration, for the activities they acted on. You can filter activities by contacts in the timeline to see specific contacts that you're interested in. To see all activities that aren't assigned to a specific contact, select **Activities not mapped to a Contact**.

   :::image type="content" source="media/Contact_Activities3.png" alt-text="Screenshot of the filtering options available for Contact-level activities.":::

[!INCLUDE [footer-include](../includes/footer-banner.md)]
