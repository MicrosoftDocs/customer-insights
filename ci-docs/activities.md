---
title: "Customer or business contact activities"
description: "Define customer or business contact activities and view them in a timeline on customer profiles." 
ms.date: 11/16/2022
ms.subservice: audience-insights
ms.reviewer: v-wendysmith
ms.topic: conceptual
author: srivas15
ms.author:  shsri
manager: shellyha
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

Customer activities are actions or events performed by customers or business contacts. For example, transactions, support call duration, website reviews, purchases, or returns. These activities are contained in one or more data sources. With Customers Insights, consolidate your customer activities from these [data sources](data-sources.md) and associate them with customer profiles. These activities appear chronologically in a timeline on the customer profile. Include the timeline in Dynamics 365 apps with the [Customer Card add-in](customer-card-add-in.md) solution.

## Define a customer activity

A table must have at least one attribute of type **Date** to be included in a customer timeline. The **Add activity** control is disabled if no such table is found.

1. Go to **Data** > **Activities**.

1. Select **Add activity** to start the guided experience.

1. In the **Activity data** step, enter the following information:

   - **Activity name**: Select a name for your activity.
   - **Activity table**: Select a table that includes transactional or activity data.
   - **Primary key**: Select the field that uniquely identifies a record. It shouldn't contain any duplicate values, empty values, or missing values.

     > [!NOTE]
     > The Primary key for each row must remain consistent across data source refreshes. If the Primary key for a row is updated in a data source refresh, it creates duplicates in the output Activity table.

   :::image type="content" source="media/Activity_Wizard1.PNG" alt-text="Set up the activity data with name, table, and primary key.":::

1. Select **Next**.

1. In the **Relationship** step, select **Add relationship** to connect your activity data to its corresponding customer record. This step visualizes the connection between tables.  

   - **Foreign key**: Foreign field in your activity table that will be used to establish a relationship with another table.
   - **To table name**: Corresponding source customer table with which your activity table will be in relationship. You can only relate to source customer tables that are used in the data unification process.
   - **Relationship name**: If a relationship between this activity table and the selected source customer table already exists, the relationship name will be in read-only mode. If no such relationship exists, a new relationship will be created with the name you provide in this box.

   :::image type="content" source="media/Activity_Wizard2.PNG" alt-text="Define the table relationship.":::

   > [!TIP]
   > In B-to-B environments, you can select between account tables and other tables. If you select an account table, the relationship path is automatically set. For other tables, you have to define the relationship path over one or more intermediate tables until you reach an account table.

1. Select **Apply** to create the relationship.

1. Select **Next**.

1. In the **Activity unification** step, choose the activity event and the start time of your activity.
   - **Required fields**
      - **Event activity**: Field that is the event for this activity.
      - **Timestamp**: Field that represents the start time of your activity.

   - **Optional fields**
      - **Additional detail**: Field with relevant information for this activity.
      - **Icon**: Icon that best represents this activity type.
      - **Web address**: Field containing a URL with information about this activity. For example, the transactional system that sources this activity. This URL can be any field from the data source, or it can be constructed as a new field using a Power Query transformation. The URL data will be stored in the *Unified Activity* table, which can be consumed downstream using [APIs](apis.md).

   - **Show in timeline**
      - Choose if you what to show this activity in the timeline view on your customer profiles. Select **Yes** to show the activity in the timeline or **No** to hide it.
        > [!NOTE]
        > If you select **No** and hide the activity in the timeline view, the activity will not be returned by the [Customer Insights API](apis.md) either.

      :::image type="content" source="media/Activity_Wizard3.PNG" alt-text="Specify the customer activity data in a Unified Activity table.":::

1. Select **Next** to choose the activity type, or select **Finish and review** to save the activity with the activity type set to **Other**.

1. In the **Activity Type** step, choose the activity type and optionally select if you want to semantically map some of the activity types for use in other areas of Customer Insights. Currently, *Feedback*, *Loyalty*, *SalesOrder*, *SalesOrderLine*, and *Subscription* activity types support semantics after agreeing to map the fields. If an activity type isn't relevant for the new activity, you can choose *Other* or *Create new* for a custom activity type.

1. Select **Next**.

1. In the **Review** step, verify your selections. Go back to any of the previous steps and update the information if necessary.

1. Select **Save activity** to apply your changes and select **Done** to go back to **Data** > **Activities**. The created activity displays.

1. After creating all your activities, select **Run** to process them.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Manage existing customer activities

Go to **Data** > **Activities** to view your saved activities, their source table, the activity type, and if they are included in the customer timeline. You can sort the list of activities by any column or use the search box to find the activity you want to manage.

Select an activity to view available actions.

- **Edit** the activity to change it's configuration. The configuration opens on the review step. After changing the configuration, select **Save activity** and then select **Run** to process the changes.
- **Rename** the activity. Select **Save** to apply your changes.
- **Delete** the activity. To delete more than one activity at once, select the activities and then **Delete**. Confirm the deletion.

## View activity timelines on customer profiles

1. If you selected **Show in activity timeline** in the activity configuration, go to **Customers** and select a customer profile to view the customer's activities in the **Activity timeline** section.

   :::image type="content" source="media/Activity_Timeline1.PNG" alt-text="View configured activities in Customer Profiles.":::

1. To filter activities in the activity timeline:

   - Select one or more of the activity icons to refine your results to include the selected type(s) only.

     :::image type="content" source="media/Activity_Timeline2.PNG" alt-text="Filter activities by type using the icons.":::

   - Select **Filter** to open a filter panel to configure your timeline filters. Filter by *ActivityType* and/or *Date*. Select **Apply**.

     :::image type="content" source="media/Activity_Timeline3.PNG" alt-text="Use the filter panel to configure filter conditions.":::

> [!NOTE]
> Activity filters are removed when you leave a customer profile. You have to apply them each time you open a customer profile.

## Define a contact activity

For business accounts (B-to-B), use a *ContactProfile* table to capture activities of contacts. You can see in the activity timeline for an account which contact was responsible for each activity. Most steps follow the customer activity mapping configuration.

   > [!NOTE]
   > To define a contact-level activity, a *ContactProfile* table must be created, either as a [unified contact profile](data-unification-contacts.md) or through [semantic mapping](semantic-mappings.md#define-a-contactprofile-semantic-table-mapping).
   >
   > You must have both **AccountID** and **ContactID** attributes for each record within your activity data.
  
1. Go to **Data** > **Activities**.

1. Select **Add Activity**.

1. In the **Activity data** step, enter the following information:

   - **Activity name**: Select a name for your activity.
   - **Activity table**: Select a table that includes transactional or activity data.
   - **Primary key**: Select the field that uniquely identifies a record. It shouldn't contain any duplicate values, empty values, or missing values.

     > [!NOTE]
     > The Primary key for each row must remain consistent across data source refreshes. If the Primary key for a row is updated in a data source refresh, it creates duplicates in the output Activity table.

1. In the **Relationships** step, create an indirect relationship between your activity source data to accounts, using your contact data as an intermediary table. For more information, see [direct and indirect relationship paths](relationships.md#relationship-paths).
   - Example relationship for an activity called *Purchases*:
      - **Purchases Source Activity Data** > **Contact Data** on the attribute **ContactID**
      - **Contact Data** > **Account Data** on the attribute **AccountID**

   :::image type="content" source="media/Contact_Activities1.png" alt-text="Example relationship setup.":::

1. After setting up the relationship(s), select **Next** and complete your activity mapping configuration. For detailed steps on activity creation, see [define a customer activity](#define-a-customer-activity).

1. Run your activity mappings.

1. Your contact-level activities will now be visible on your customer timeline.

   :::image type="content" source="media/Contact_Activities2.png" alt-text="Final result after configuring contact activities":::

## Contact-level activity timeline filtering

After configuring a contact-level activity mapping and running it, the activity timeline for your customers will be updated. It includes their IDs or names, depending on your *ContactProfile* configuration, for the activities they acted on. You can filter activities by contacts in the timeline to see specific contacts that you are interested in. Additionally, you can see all activities that are not assigned to a specific contact by selecting **Activities not mapped to a Contact**.

   :::image type="content" source="media/Contact_Activities3.png" alt-text="Filtering options available for Contact-level activities.":::

[!INCLUDE [footer-include](includes/footer-banner.md)]
