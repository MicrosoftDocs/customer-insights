---
title: "Customer or contact activities"
description: "Define customer or business contact activities and view them in a timeline on customer profiles." 
ms.date: 05/23/2022
ms.subservice: audience-insights
ms.reviewer: v-wendysmith
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

# Customer or business contact activities

Combine customer or business contact activities from [various data sources](data-sources.md) in Dynamics 365 Customer Insights. Create a timeline that lists the activities chronologically. Include the timeline in Dynamics 365 apps with the [Customer Card add-in](customer-card-add-in.md) solution.

## Define a customer activity

Your data sources can include entities with transactional and activity data from multiple data sources. Identify these entities and select the activities you want to view on the customer's timeline. Choose the entity that includes your target activity or activities.

An entity must have at least one attribute of type **Date** to be included in a customer timeline and you can't add entities without **Date** fields. The **Add activity** control is disabled if no such entity is found.

1. Go to **Data** > **Activities**.

1. Select **Add activity** to start the guided experience for the activity setup process.

1. In the **Activity data** step, set the values for the following fields:

   - **Activity name**: Select a name for your activity.
   - **Entity**: Select an entity that includes transactional or activity data.
   - **Primary key**: Select the field that uniquely identifies a record. It shouldn't contain any duplicate values, empty values, or missing values.

   :::image type="content" source="media/Activity_Wizard1.PNG" alt-text="Set up the activity data with name, entity, and primary key.":::

1. Select **Next** to go to the next step.

1. In the **Relationship** step, configure the details to connect your activity data to its corresponding customer record. This step visualizes the connection between entities.  

   - **First**: Foreign field in your activity entity that will be used to establish a relationship with another entity.
   - **Second**: Corresponding source customer entity with which your activity entity will be in relationship. You can only relate to source customer entities that are used in the data unification process.
   - **Third**: If a relationship between this activity entity and the selected source customer entity already exists, the relationship name will be in read-only mode. If no such relationship exists, a new relationship will be created with the name you provide in this box.

   :::image type="content" source="media/Activity_Wizard2.PNG" alt-text="Define the entity relationship.":::

   > [!TIP]
   > In B-to-B environments, you can select between account entities and other entities. If you select an account entity, the relationship path is automatically set. For other entities, you have to define the relationship path over one or more intermediate entities until you reach an account entity.

1. Select **Next** to go to the next step. 

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

1. Select **Next** to move to the next step. You can select **Finish and review** to save the activity now with the activity type set to **Other**. 

1. In the **Activity Type** step, choose the activity type and optionally select if you want to semantically map some of the activity types for use in other areas of Customer Insights. Currently, *Feedback*, *Loyalty*, *SalesOrder*, *SalesOrderLine*, and *Subscription* activity types support semantics after agreeing to map the fields. If an activity type isn't relevant for the new activity, you can choose *Other* or *Create new* for a custom activity type.

1. Select **Next** to move to the next step. 

1. In the **Review** step, verify your selections. Go back to any of the previous steps and update the information if necessary.

   :::image type="content" source="media/Activity_Wizard5.PNG" alt-text="Review the specified fields for an activity.":::
   
1. Select **Save activity** to apply your changes and select **Done** to go back to **Data** > **Activities**. Here you see which activities are set to show in the timeline. 

1. On the **Activities** page, select **Run** to process the activity. 

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Manage existing customer activities

On **Data** > **Activities**, you can view all your saved activities, and manage them. Each activity is represented by a row that also includes details about the source, the entity, and the activity type.

The following actions are available when you select an activity. 

- **Edit**: Opens the activity setup on the review step. You can change any or all of the current configuration from this step. After changing the configuration, select **Save activity** and then select **Run** to process the changes.

- **Rename**: Opens a dialog where you can enter a different name for the selected activity. Select **Save** to apply your changes.

- **Delete**: Opens a dialog to confirm the deletion of the selected activity. You can also delete more than one activity at once by selecting the activities and then selecting the delete icon. Select **Delete** to confirm the deletion.

## View activity timelines on customer profiles

After you configured customer activities, select **Show in activity timeline** in the activity configuration to find all your customer's activities on their customer profile.

To open the timeline for a customer, go to **Customers** and choose the customer profile that you want to view.

If a customer has participated in a configured activity, you'll find it in the **Activity timeline** section.

:::image type="content" source="media/Activity_Timeline1.PNG" alt-text="View configured activities in Customer Profiles.":::

There are several ways to filter activities in the activity timeline:

- You can select one or many of the activity icons to refine your results to include the selected type(s) only.

  :::image type="content" source="media/Activity_Timeline2.PNG" alt-text="Filter activities by type using the icons.":::

- You can select **Filter** to open a filter panel to configure your timeline filters.

   1. You can filter by *ActivityType* and *Date*
   1. Select **Apply** to use the filters in the activity timeline.

   :::image type="content" source="media/Activity_Timeline3.PNG" alt-text="Use the filter panel to configure filter conditions.":::

To remove filters, select the **x** next to each filter applied to the timeline or select **Clear filters**.


> [!NOTE]
> Activity filters are removed when you leave a customer profile. You have to apply them each time you open on a customer profile.

## Use a ContactProfile entity to create contact-level activities

After creating a *ContactProfile* entity, you can capture activities of contacts. It enables you to see in the activity timeline for an account which contact was responsible for each activity. Most steps follow the typical activity mapping configuration.

   > [!NOTE]
   > For contact-level activities to work, you must have both **AccountID** and **ContactID** attributes for each record within your activity data.

**Prerequisite:**

The *ContactProfile* entity has been created, either as a [unified contact profile](data-unification-contacts.md) or through [semantic mapping](semantic-mappings.md#define-a-contactprofile-semantic-entity-mapping).

1. Go to **Data** > **Activities**.

1. Select **Add Activity** to create a new activity.

1. Name the activity, select the source activity entity, and select the primary key of the activity entity.

1. In the **Relationships** step, create an indirect relationship between your activity source data to accounts, using your contact data as an intermediary entity. For more information, see [direct and indirect relationship paths](relationships.md#relationship-paths).
   - Example relationship for an activity called *Purchases*:
      - **Purchases Source Activity Data** > **Contact Data** on the attribute **ContactID**
      - **Contact Data** > **Account Data** on the attribute **AccountID**

   :::image type="content" source="media/Contact_Activities1.png" alt-text="Example relationship setup.":::

1. After setting up the relationship(s), select **Next** and complete your activity mapping configuration. For detailed steps on activity creation, see [define an activity](activities.md).

1. Run your activity mappings.

1. Your contact-level activities will now be visible on your customer timeline.

   :::image type="content" source="media/Contact_Activities2.png" alt-text="Final result after configuring contact activities":::

### Contact-level activity timeline filtering

After configuring a contact-level activity mapping and running it, the activity timeline for your customers will be updated. It includes their IDs or names, depending on your *ContactProfile* configuration, for the activities they acted on. You can filter activities by contacts in the timeline to see specific contacts that you are interested in. Additionally, you can see all activities that are not assigned to a specific contact by selecting **Activities not mapped to a Contact**.

   :::image type="content" source="media/Contact_Activities3.png" alt-text="Filtering options available for Contact-level activities.":::

[!INCLUDE [footer-include](includes/footer-banner.md)]
