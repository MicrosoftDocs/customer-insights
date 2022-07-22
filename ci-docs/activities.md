---
title: "Customer activities"
description: "Define customer activities and view them in a timeline on customer profiles." 
ms.date: 07/22/2022
ms.subservice: audience-insights
ms.reviewer: mhart
ms.topic: conceptual
author: CadeSanthaMSFT
ms.author: cadesantha
manager: shellyha
searchScope: 
  - ci-entities
  - ci-customer-card
  - ci-relationships
  - ci-activities
  - ci-activities-wizard
  - ci-measures
  - ci-segment-suggestions
  - customerInsight
---

# Customer activities

Customer activities are actions or events performed by customers. For example, transactions, support call duration, website reviews, purchases, or returns. These activities are contained in one or more data sources. With Customers Insights, consolidate your customer activities from these [data sources](data-sources.md) and associate them with customer profiles. These activities appear chronologically in a timeline on the customer profile. Include the timeline in Dynamics 365 apps with the [Customer Card add-in](customer-card-add-in.md) solution.

## Define an activity

An entity must have at least one attribute of type **Date** to be included in a customer timeline. The **Add activity** control is disabled if no such entity is found.

1. Go to **Data** > **Activities**.

1. Select **Add activity** to start the guided experience.

1. In the **Activity data** step, enter the following information:

   - **Activity name**: Name for your activity.
   - **Activity entity**: Entity that includes transactional or activity data.
   - **Primary key**: Field that uniquely identifies a record. It shouldn't contain any duplicate values, empty values, or missing values.

   :::image type="content" source="media/Activity_Wizard1.PNG" alt-text="Set up the activity data with name, entity, and primary key.":::

1. Select **Next**.

1. In the **Relationship** step, select **Add relationship** to connect your activity data to its corresponding customer record. This step visualizes the connection between entities.  

   - **Foreign key from entity**: Field in your activity entity that will be used to establish a relationship with another entity.
   - **To entity name**: Corresponding source customer entity with which your activity entity will be in relationship. You can only relate to source customer entities that are used in the data unification process.
   - **Relationship name**: Name identifying the relationship between entities. If a relationship between this activity entity and the selected source customer entity already exists, the relationship name is read-only.

   :::image type="content" source="media/Activity_Wizard2.PNG" alt-text="Define the entity relationship.":::

   > [!TIP]
   > In B-to-B environments, you can select between account entities and other entities. If you select an account entity, the relationship path is automatically set. For other entities, you have to define the relationship path over one or more intermediate entities until you reach an account entity.

1. Select **Apply** to create the relationship.

1. Select **Next**.

1. In the **Activity unification** step, choose the activity event and the start time of your activity.
   - **Required fields**
      - **Event activity**: Field that is the event for this activity.
      - **Timestamp**: Field that represents the start time of your activity.

   - **Optional fields**
      - **Additional detail**: Field with relevant information for this activity.
      - **Icon**: Icon that best represents this activity type.
      - **Web address**: Field containing a URL with information about this activity. For example, the transactional system that sources this activity. This URL can be any field from the data source, or it can be constructed as a new field using a Power Query transformation. The URL data will be stored in the *Unified Activity* entity, which can be consumed downstream using [APIs](apis.md).

   - **Show in timeline**
      - Choose if you what to show this activity in the timeline view on your customer profiles. Select **Yes** to show the activity in the timeline or **No** to hide it.

      :::image type="content" source="media/Activity_Wizard3.PNG" alt-text="Specify the customer activity data in a Unified Activity entity.":::

1. Select **Next** to choose the activity type, or select **Finish and review** to save the activity with the activity type set to **Other**.

1. In the **Activity Type** step, choose the activity type and optionally select if you want to semantically map some of the activity types for use in other areas of Customer Insights. Currently, *Feedback*, *Loyalty*, *SalesOrder*, *SalesOrderLine*, and *Subscription* activity types support semantics after agreeing to map the fields. If an activity type isn't relevant for the new activity, you can choose *Other* or *Create new* for a custom activity type.

1. Select **Next**.

1. In the **Review** step, verify your selections. Go back to any of the previous steps and update the information if necessary.

1. Select **Save activity** to apply your changes and select **Done** to go back to **Data** > **Activities**. The created activity displays.

1. After creating all your activities, select **Run** to process them.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Manage existing activities

Go to **Data** > **Activities** to view your saved activities, their source entity, the activity type, and if they are included in the customer timeline. You can sort the list of activities by any column or use the search box to find the activity you want to manage.

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

1. To remove filters, select **Clear filters** or select **Filter** and clear the filter checkbox.

> [!NOTE]
> Activity filters are removed when you leave a customer profile. You have to apply them each time you open a customer profile.

[!INCLUDE [footer-include](includes/footer-banner.md)]
