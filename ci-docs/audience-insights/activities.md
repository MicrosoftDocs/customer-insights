---
title: "Customer activities"
description: "Define customer activities and view them in customer timeline." 
ms.date: 10/13/2020
ms.service: customer-insights
ms.subservice: audience-insights
ms.reviewer: adkuppa
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Customer activities

Combine customer activities from [various data sources](data-sources.md) in Dynamics 365 Customer Insights to create a customer timeline that lists the activities in chronological order. You can include the timeline in customer engagement apps in Dynamics 365 via the [Customer Card add-in](customer-card-add-in.md), or in a Power BI dashboard.

## Define an activity

Your data sources include entities with transactional and activity data from multiple data sources. Identify these entities and select the activities you want to view on the customer's timeline. Choose the entity that includes your target activity or activities.

1. In audience insights, go to **Data** > **Activities**.

1. Select **Add activity**. Here you will be presented with a wizard which will step you through the activity set up process

   > [!NOTE]
   > An entity must have at least one attribute of type **Date** to be included in a customer timeline and you can't add entities without **Date** fields. The **Add activity** control is disabled if no such entity is found.

1. In the **Add data** wizard page, set the values for the following fields:

   - **Activity name**: Select a name for your activity.
   - **Entity**: Select an entity that includes transactional or activity data.
   - **Primary key**: Select the field that uniquely identifies a record. It shouldn't contain any duplicate values, empty values, or missing values.

 > [!div class="mx-imgBorder"]
   > ![Activity_Wizard1](media/Activity_Wizard1.png "Define the entity relationship")

1. Select **Next** to move to the next step in the wizard

1. In the **Relationship** wizard page, configure the details to connect your activity data to its corresponding customer. This page now visually shows the connection between entities.  

   - **First**: Select the foreign field  in your activity entity that will be used to establish a relationship with another entity.
   - **Second**: Select the corresponding source customer entity with which your activity entity will be in relationship. You can relate to only those source customer entities that are used  in the data unification process.
   - **Third**: If a relationship between this activity entity and the selected source customer entity already exists, the relationship name will be in read-only mode. If there no such relationship exists, a new relationship will be created with the name provided here.

 > [!div class="mx-imgBorder"]
   > ![Activity_Wizard2](media/Activity_Wizard2.png "Define the entity relationship")

1. Select **Next** to move to the next step in the wizard. 

1. in the **Activity unification** wizard page, here you can select the activity event and the start time of your activity. You can also choose to have the activity detail included in your timeline.  

   - **Event activity**: Select the field that is the event for this activity
   - **Timestamp**: Select the field that represents the start time of your activity.
   - If you toggle **Yes** to the ‘show this information in the timeline’ question, you will be prompted to add additional information that will be shown in the Example timeline view panel
             - **Additional detail**: Optionally, select the field that is relevant for this activity 
             - **Icon**: Optionally, select the icon that best represents this activity
             - **Web address**: Select the field that represents a URL providing additional information about this activity. For example, the transactional system that sources this activity. This URL can be any field from the data source, or it can be constructed as a new field using a Power Query transformation. This URL data will be stored in the Unified Activity entity, which can be consumed downstream using APIs

 > [!div class="mx-imgBorder"]
   > ![Activity_Wizard3](media/Activity_Wizard3.png "Define the entity relationship")

1. Select **Next** to move to the next step in the wizard or select **Finish and review** if you are complete. If you choose to select **Finish and review**, then your activity type will be defaulted to **Other**. 

1. In the **Activity Type** wizard page, here you can select the activity type and optionally select if you would like to semantically map some of the activity types for use in other areas in the product. Currently Subscription & SalesOrderLine types can be semantically mapped. If an activity type is not relevant to your type, you can choose ‘other’ or choose ‘create new’ for a custom activity type. 

   - **Activity Type**: Select the one the best represents your type. 
             - 1.	If you select Type = Subscription  or SalesOrderLine, then a consent question will appear. If you select **Yes** to allow activity details to be semantically mapped, then additional fields will appear which will need to filled in
                  - **Additional fields**: select the fields relevant to this activity. This will show those 
                  - If you select Type = Create new, you will be asked to give it a unique Activity type name
                  - If you select any other Type, no additional information is needed

 > [!div class="mx-imgBorder"]
   > ![Activity_Wizard4](media/Activity_Wizard4.png "Define the entity relationship")

1. Select **Next** to move to the next step in the wizard. 

1. In this last step you can review what you have selected. From here to you go back to any of the wizard pages and update. If you are happy with your selection then you can continue 

 > [!div class="mx-imgBorder"]
   > ![Activity_Wizard5](media/Activity_Wizard5.png "Define the entity relationship")
   
1. Select **Save activity** to apply your changes and select **Done** to exti to the actitives page. Here you will also see which activities you have chosen to show in the timeline. 

 > [!div class="mx-imgBorder"]
   > ![Activity_Wizard6](media/Activity_Wizard6.png "Define the entity relationship")
   
 > [!div class="mx-imgBorder"]
   > ![Activity_Wizard7](media/Activity_Wizard7.png "Define the entity relationship")

1. On the **Activities** page, select **Run**. 

> [!TIP]
> There are [six types of status](system.md#status-types) for tasks/processes. Additionally, most processes [depend on other downstream processes](system.md#refresh-policies). You can select the status of a process to see details on the progress of the entire job. After selecting **See details** for one of the job's tasks, you find additional information: processing time, the last processing date, and all errors and warnings associated with the task.


## Manage exisiting activities

On the Activities page, you can view all your saved activities, and manage them. Each activity is represented by a row which also includes details about the source, the entity and the activity type.

 
   > ![Activity_Wizard8](media/Activity_Wizard8.png "Define the entity relationship")

The following actions are available when you select an activity. 

1. **Edit**: this will open the activity wizard on the review step, from here you can select to edit any or all of current activity configuration. Once changes are made,  click Save Activity and then click Run.

> [!div class="mx-imgBorder"]
   > ![Activity_Wizard9](media/Activity_Wizard9.png "Define the entity relationship")

1. **Rename**: this will open a pop up dialog where you can choose to enter a different name for you activity. Click **Save**

> [!div class="mx-imgBorder"]
   > ![Activity_Wizard10](media/Activity_Wizard10.png "Define the entity relationship")
   

1. **Delete**: this will open a pop to reconfirm you would like to delete that activity. You can also choose to delete more than one activity at once, by selecting all the activities and clicking the delete icon. Confirm you deletion by clicking **Delete**

> [!div class="mx-imgBorder"]
   > ![Activity_Wizard11](media/Activity_Wizard11.png "Define the entity relationship")
   
  


[!INCLUDE[footer-include](../includes/footer-banner.md)]
