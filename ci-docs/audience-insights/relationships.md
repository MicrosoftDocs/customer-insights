---
title: "Relationships between entities and entity paths"
description: "Create and manage relationships between entities from multiple data sources."
ms.date: 04/14/2020
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
---

# Relationships between entities

Relationships help you connect entities and generate a graph of your data when entities share a common identifier (foreign key) that can be referenced from one entity to another. Connected entities enable you to define segments and measures based on multiple data sources.

There are three types of relationships. 
1.	Non-editable system relationships, which are created automatically as part of the unification process
2.	Non-editable inherited relationship, which are created automatically from data sources 
3.	Editable custom relationships, created and configured by users.

## Non-editable system relationships, which are created automatically as part of the unification process

During the match and merge processes, system relationships are created behind the scenes based on intelligent matching. These relationships help relate the Customer Profile records with other corresponding entities' records. The following diagram illustrates the creation of three system relationships when the customer entity is matched with additional entities to produce the final Customer Profile entity.

> [!div class="mx-imgBorder"]
> ![Relationship creation](media/Relationships1.png "Relationship creation")

- ***CustomerToContact* relationship** was created between the Customer entity and the Contact entity. The Customer entity gets the key field **Contact_contactId** to relate to the Contact entity key field **contactId**.
- ***CustomerToAccount* relationship** was created between the Customer entity and the Account entity. The Customer entity gets the key field **Account_accountId** to relate to the Account entity key field **accountId**.
- ***CustomerToWebAccount* relationship** was created between the Customer entity and the WebAccount entity. The Customer entity gets the key field **WebAccount_webaccountId** to relate to the WebAccount entity key field **webaccountId**.

## Non-editable inherited relationship, which are created automatically from data sources 

During the ingestion process, a check is done on the data sources to see if relationships already exist, if they do then they are created behind the scenes so that users do not have to recreate them. They can also be used in downstream processes.

The next section will outline how to create custom relationships.


## Create a custom relationship

Define custom relationships on the **Relationships** page. Each relationship consists of a Source entity (the entity that holds the foreign key) and a Target entity (the entity that the source entity's foreign key points to).

1. In audience insights, go to **Data** > **Relationships**.

2. Select **New relationship**.

3. In the **New relationship** pane, provide the following information:

   > [!div class="mx-imgBorder"]
   > ![Enter relationship details](media/Relationship2.png "Enter relationship details")

   - **Relationship name**: Name that reflects the purpose of the relationship (for example, **AccountWebLogs**).
   - **Description**: Description of the relationship.
   - **Source entity**: Select the entity that is used as a source in the relationship (for example, WebLog).
   - **Cardinality**: Select the cardinality of the source entity records. For example, "many" means that multiple Weblog records are related to one WebAccount.
   - **Source key field**: This represents the foreign key field in the source entity. For example, WebLog has the **accountId** foreign key field.
   - **Target entity**: Select the entity that is used as a target in the relationship (for example, WebAccount).
   - **Target cardinality**: Select the cardinality of the target entity records. For example, "one" means that multiple Weblog records are related to one WebAccount.
   - **Target key field**: This field represents the key field of target entity. For example, WebAccount has the **accountId** key field.

> [!NOTE]
> Only many-to-one and one-to-one relationships are supported. Many-to-many relationships can be created using two many-to-one relationships and a link entity (an entity that is used to connect the source entity and the target entity).

## View relationships
The Relationships page, presents a view of all the relationships that have been set up. Each relationship is represented by a row which also includes details about the source, the entity and the cardinality. 

   > [!div class="mx-imgBorder"]
   > ![View relationships](media/Relationship3.png "View relationships")


The following actions are available from this page
1.**New Relationship**: described earlier
2.	**Visualizer**: selecting this will show a visual view of how the relationships are set up including cardinality. The boxes can be dragged around the screen or organize the view. 
   > [!div class="mx-imgBorder"]
   > ![Visualizer](media/Relationship4.png "Visualizer")

•	The following actions are available from this view
o	**Export as image**: selecting this allows you to export the view as an image
o	**Change to horizontal**: selecting this will change the view
o	**Edit**: If this is user created custom relationship then clicking on the edit circle will highlight the primary and foreign keys and present the edit panel from which edits can be made and saved updating the visual too

   > [!div class="mx-imgBorder"]
   > ![Edit](media/Relationship5.png "Edit")

3.	**Filter by**: selecting this will provide the user with options to see some, many or all of the relationships

## Manage existing relationships 
On the Relationships page, you can view all your saved relationships, and manage them. Each relationship is represented by a row which also includes details about the source, the entity and the cardinality. 
The following actions are available 

1.	**Edit**: This is available for user created custom relationship and will open a side panel where you can change the details of the relationship 
   > [!div class="mx-imgBorder"]
   > ![Edit_existing](media/Relationship6.png "Edit existing")

2.	**Delete**: This is available for user created custom relationship and this will open a pop to reconfirm you would like to delete the relationship. You can also choose to delete more than one activity at once, by selecting all the activities and clicking the delete icon. 
   > [!div class="mx-imgBorder"]
   > ![Delete](media/Relationship7.png "Delete")

3.	**View**: This is available for system and inherited relationships and will open a side panel where you can change the details of the relationship 
   > [!div class="mx-imgBorder"]
   > ![View](media/Relationship8.png "View")


## Next step

System and custom relationships are used to create segments based on multiple data sources that are no longer siloed. For more information, see [Segments](segments.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]
