---
title: "Customer or business contact activities"
description: "Define customer or business contact activities and view them in a timeline on customer profiles." 
ms.date: 02/25/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: srivas15
ms.author:  shsri
ms.custom: bap-template
searchScope: 
  - ci-entities
  - ci-customer-card
  - ci-relationships
  - ci-activities
  - ci-activities-wizard
  - ci-measures
  - ci-segment-suggestions
  - customerInsights
---

# Customer or business contact activities

Customer activities are actions or events performed by customers or business contacts. For example, transactions, support call duration, website reviews, purchases, or returns. These activities are contained in one or more data sources. With Customers Insights, consolidate your customer activities from these data sources and associate them with customer profiles. These activities appear chronologically in a timeline on the customer profile. Include the timeline in Dynamics 365 apps with the [Customer Card add-in](customer-card-add-in.md) solution.

## Prerequisites

- Add [data sources](data-sources.md) that contain activities. Make sure each activity table has at least one field of type **Date** or **Datetime**.
- [Unify customer data into customer profiles](data-unification.md).

## Define customer activities

Customer Insights helps you with simple steps to define all activities at once.

1. Go to **Data** > **Activities**. Select **Configure activities**.

1. In the **Activity tables** step, **Select tables** and choose the tables that have activity data. Select **Add**.

1. For each table, choose the following information:

   - **Activity type**: Choose from the semantic types, *Feedback*, *Loyalty*, *SalesOrder*, *SalesOrderLine*, and *Subscription*. If a semantic activity type isn't relevant for the new activity, choose a non-semantic type, *Other*, or *Create New* for a custom type.
   - **Primary key**: The primary key uniquely identifies a record. It shouldn't contain any duplicate values, empty values, or missing values.

   > [!NOTE]
   > The Primary key for each row must remain consistent across data source refreshes. If a data source refresh changes the Primary key for a row, Customer Insights must delete all old rows and insert all new rows causing an increase in processing time.

   :::image type="content" source="media/Activity_Wizard1.PNG" alt-text="Set up the activity data with table and primary key.":::

1. Select **Next** for the **Activity fields** step.

1. For each table that has a semantic activity type, choose **Intelligent mapping** to use AI models to predict semantics, which saves time and improves accuracy. Intelligent mapping automatically determines the type of data in each column and maps it to the attributes.

1. Enter the following information for each table:

   - **Activity name**: Unique name for your activity.
   - **Timestamp**: Field that represents the start time or date of your activity.
   - **Event activity**: Field that is the event for this activity.
   - **Web address** (optional): Field containing a URL with information about this activity. For example, the transactional system that sources this activity. This URL can be any field from the data source, or it can be constructed as a new field using a Power Query transformation. The URL data will be stored in the *Unified Activity* table, which can be consumed downstream using [APIs](apis.md).
   - **Additional detail** (optional): Field with relevant information for this activity.
   - **Show this activity in the timeline on your customer profile**: **Yes** to show the activity in the timeline or **No** to hide it. Optionally, choose an icon to represent the activity on the timeline.
     > [!NOTE]
     > If you select **No** and hide the activity in the timeline view, the activity will not be returned by the [Customer Insights API](apis.md) either.
   - **Map field types for your activity's attributes?**: **Yes** to help the system better understand the relevance of your activity data or **No** do not map.

   :::image type="content" source="media/Activity_Wizard2.PNG" alt-text="Map the activity fields.":::

1. If you choose **Yes** to map your field types, select the appropriate attributes to map your data. Required fields are determined by the selected activity type.

1. Select **Next**.

1. In the **Relationship** step, select **Add relationship** and enter the following information for each table. This step connects your activity data to its corresponding customer record.  

   - **Foreign key**: Field in your activity table that will be used to establish a relationship with another table.
   - **To table name**: Corresponding source customer table with which your activity table will be in relationship. You can only relate to source customer tables that are used in the data unification process.
   - **Relationship name**: If a relationship between this activity table and the selected source customer table already exists, the relationship name will be in read-only mode. If no such relationship exists, a new relationship will be created with the name you provide in this box.

   > [!TIP]
   > In B-to-B environments, you can select between account tables and other tables. If you select an account table, the relationship path is automatically set. For other tables, you have to define the relationship path over one or more intermediate tables until you reach an account table.

1. Select **Apply** to create the relationship and then select **Next**.

1. In the **Review** step, verify your selections. Go back to any of the previous steps and update the information if necessary.

1. To save your changes, select **Save and close**. To save your changes and create the activities, select **Create activities**.

## Manage existing customer activities

Go to **Data** > **Activities** to view your saved activities, their source table, the activity type, and if they are included in the customer timeline. You can sort the list of activities by any column or use the search box to find an activity.

Select an activity to rename or delete the activity. To edit activities, select **Configure activities**.

## View activity timelines on customer profiles

1. If you selected **Show this activity in the timeline on your customer profile** in the activity configuration, go to **Customers** and select a customer profile to view the customer's activities in the **Activity timeline** section.

   :::image type="content" source="media/Activity_Timeline1.PNG" alt-text="View configured activities in Customer Profiles.":::

1. To filter activities in the activity timeline:

   - Select one or more of the activity icons to refine your results to include the selected type(s) only.

     :::image type="content" source="media/Activity_Timeline2.PNG" alt-text="Filter activities by type using the icons.":::

   - Select **Filter** to open a filter panel to configure your timeline filters. Filter by *ActivityType* and/or *Date*. Select **Apply**.

     :::image type="content" source="media/Activity_Timeline3.PNG" alt-text="Use the filter panel to configure filter conditions.":::

> [!NOTE]
> Activity filters are removed when you leave a customer profile. You have to apply them each time you open a customer profile.

## Define contact activities (preview)

For business accounts (B-to-B), use a *ContactProfile* table to capture activities of contacts. You can see in the activity timeline for an account which contact was responsible for each activity. Most steps follow the customer activity mapping configuration.

   > [!NOTE]
   > To define contact-level activities, a *ContactProfile* table must be created, either as a [unified contact profile](data-unification-contacts.md) or through [semantic mapping](semantic-mappings.md#define-a-contactprofile-semantic-entity-mapping).
   >
   > You must have both **AccountID** and **ContactID** attributes for each record within your activity data.
  
1. Go to **Data** > **Activities**. Select **Configure activities**.

1. In the **Activity tables** step, **Select tables** and choose the tables that have activity data. Select **Add**.

1. For each table, choose the following information:

   - **Activity type**: Choose from the semantic types, *Feedback*, *Loyalty*, *SalesOrder*, *SalesOrderLine*, and *Subscription*. If a semantic activity type isn't relevant for the new activity, choose a non-semantic type, *Other*, or *Create New* for a custom type.
   - **Primary key**: The primary key uniquely identifies a record. It shouldn't contain any duplicate values, empty values, or missing values.

   > [!NOTE]
   > The Primary key for each row must remain consistent across data source refreshes. If a data source refresh changes the Primary key for a row, Customer Insights must delete all old rows and insert all new rows causing an increase in processing time.

1. Select **Next** for the **Activity fields** step.

1. For each table that has a semantic activity type, choose **Intelligent mapping** to use AI models for smart prediction of semantics, saving time and accuracy. Intelligent mapping automatically determines the type of data in each column and maps it to the attributes.

1. Enter the following information for each table:

   - **Activity name**: Unique name for your activity.
   - **Timestamp**: Field that represents the start time or date of your activity.
   - **Event activity**: Field that is the event for this activity.
   - **Web address** (optional): Field containing a URL with information about this activity. For example, the transactional system that sources this activity. This URL can be any field from the data source, or it can be constructed as a new field using a Power Query transformation. The URL data will be stored in the *Unified Activity* table, which can be consumed downstream using [APIs](apis.md).
   - **Additional detail** (optional): Field with relevant information for this activity.
   - **Show this activity in the timeline on your customer profile**: **Yes** to show the activity in the timeline or **No** to hide it.
     > [!NOTE]
     > If you select **No** and hide the activity in the timeline view, the activity will not be returned by the [Customer Insights API](apis.md) either.
   - **Map field types for your activity's attributes?**: **Yes** to help the system better understand the relevance of your activity data or **No** do not map.

1. If you chose **Yes** to map your field types, select the appropriate attributes to map your data. Required fields are determined by the selected activity type.

1. Select **Next**.

1. In the **Relationship** step, select **Add relationship** and create an indirect relationship between your activity source data to accounts, using your contact data as an intermediary table. For more information, see [direct and indirect relationship paths](relationships.md#relationship-paths).
   - Example relationship for an activity called *Purchases*:
      - **Purchases Source Activity Data** > **Contact Data** on the attribute **ContactID**
      - **Contact Data** > **Account Data** on the attribute **AccountID**

   :::image type="content" source="media/Contact_Activities1.png" alt-text="Example relationship setup.":::

1. Select **Apply** to create the relationship and then select **Next**.

1. In the **Review** step, verify your selections. Go back to any of the previous steps and update the information if necessary.

1. To save your changes, select **Save and close**. To save your changes and create the activities, select **Create activities**.

1. After creating the contact-level activities, the information is visible on your customer timeline.

   :::image type="content" source="media/Contact_Activities2.png" alt-text="Final result after configuring contact activities":::

## Contact-level activity timeline filtering

After configuring a contact-level activity mapping and running it, the activity timeline for your customers will be updated. It includes their IDs or names, depending on your *ContactProfile* configuration, for the activities they acted on. You can filter activities by contacts in the timeline to see specific contacts that you are interested in. Additionally, you can see all activities that are not assigned to a specific contact by selecting **Activities not mapped to a Contact**.

   :::image type="content" source="media/Contact_Activities3.png" alt-text="Filtering options available for Contact-level activities.":::

[!INCLUDE [footer-include](includes/footer-banner.md)]
