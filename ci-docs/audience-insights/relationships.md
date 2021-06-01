---
title: "Relationships between entities and entity paths"
description: "Create and manage relationships between entities from multiple data sources."
ms.date: 06/01/2020
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: MichelleDevaney
ms.author: midevane
manager: shellyha
---

# Relationships between entities

Relationships help you connect entities and generate a graph of your data when entities share a common identifier (foreign key) that can be referenced from one entity to another. Connected entities enable the definition of segments and measures based on multiple data sources.

There are three types of relationships: 
- Non-editable system relationships, created by the system as part of the data unification process
- Non-editable inherited relationship, which are created automatically from ingesting data sources 
- Editable custom relationships, created and configured by users

## Non-editable system relationships

During the match and merge processes, system relationships are created behind the scenes based on intelligent matching. These relationships help relate the customer profile records with other corresponding entities' records. The following diagram illustrates the creation of three system-based relationships when the customer entity is matched with additional entities to produce the unified *Customer* entity.

:::image type="content" source="media/relationships-entities-merge.png" alt-text="Diagram with relationship paths for the customers entity with three 1-n relationships.":::

- ***CustomerToContact* relationship** was created between the *Customer* entity and the *Contact* entity. The *Customer* entity gets the key field **Contact_contactID** to relate to the *Contact* entity key field **contactID**.
- ***CustomerToAccount* relationship** was created between the *Customer* entity and the *Account* entity. The *Customer* entity gets the key field **Account_accountID** to relate to the *Account* entity key field **accountID**.
- ***CustomerToWebAccount* relationship** was created between the *Customer* entity and the *WebAccount* entity. The *Customer* entity gets the key field **WebAccount_webaccountID** to relate to the *WebAccount* entity key field **webaccountID**.

## Non-editable inherited relationships

During the data ingestion process, the system checks data sources for existing relationships. If no relationship exists, the system automatically creates them. These relationships are also used in downstream processes.

## Create a custom relationship

Relationship consists of a *source entity* containing the foreign key and a *target entity* that the source entity's foreign key points to. 

1. In audience insights, go to **Data** > **Relationships**.

2. Select **New relationship**.

3. In the **New relationship** pane, provide the following information:

   :::image type="content" source="media/relationship-add.png" alt-text="New relationship side pane with empty input fields.":::

   - **Relationship name**: Name that reflects the purpose of the relationship. Example: CustomerToSupportCase.
   - **Description**: Description of the relationship.
   - **Source entity**: Entity that is used as a source in the relationship. Example: SupportCase.
   - **Target entity**: Entity that is used as a target in the relationship. Example: Customer.
   - **Source cardinality**: Specify the cardinality of the source entity. Cardinality describes the number of possible elements in a set. It always relates to the target cardinality. You can choose between **One** and **Many**. Only many-to-one and one-to-one relationships are supported.  
     - Many-to-one: Multiple source records can relate to one target record. Example: Multiple support cases from a single customer.
     - One-to-one: A single source record relates to a one target record. Example: One loyalty ID for a single customer.

     > [!NOTE]
     > Many-to-many relationships can be created using two many-to-one relationships and a linking entity, which connects the source entity and the target entity.

   - **Target cardinality**: Select the cardinality of the target entity records. 
   - **Source key field**: The foreign key field in the source entity. Example: SupportCase could use CaseID as a foreign key field.
   - **Target key field**: The key field of the target entity. Example Customer could use the **CustomerID** key field.

4. Select **Save** to create the custom relationship.

## View relationships

The Relationships page lists all the relationships that have been created by the system or by a user. Each row represents a relationship which also includes details about the source entity, the target entity and the cardinality. 

:::image type="content" source="media/relationships-list.png" alt-text="List of relationships and options in the action bar of the Relationships page.":::

This page offers a set of options for existing and new relationships: 
- **New Relationship**: [Create a custom relationship](#create-a-custom-relationship).
- **Visualizer**: [Explore the relationship visualizer](#explore-the-relationship-visualizer) to see a network diagram of the existing relationships and their cardinality.
- **Filter by**: Choose the type of relationships to show in the list.
- **Search relationships**: Use a text-based search on properties of the relationships.

### Explore the relationship visualizer

The relationship visualizer shows a network diagram of the existing relationships between connected entities and their cardinality.

To customize the view, you can change the position of the boxes by dragging them on the canvas.

:::image type="content" source="media/relationship-visualizer.png" alt-text="Screenshot of the relationship visualizer network diagram with connections between related entities.":::

Available options: 
- **Export as image**: Save the current view as an image file.
- **Change to horizontal/vertical layout**: Change the alignment of the entities and relationships.
- **Edit**: Update properties of custom relationships in the edit pane and save changes.

## Manage existing relationships 

On the Relationships page, each relationship is represented by a row. 

Select a relationship and choose one of the following options: 
 
- **Edit**: Update properties of custom relationships in the edit pane and save changes.
- **Delete**: Delete custom relationships.
- **View**: View system-created and inherited relationships in a pane where you can change the details of the relationship. 

## Next step

System and custom relationships are used to [create segments](segments.md) based on multiple data sources that are no longer siloed.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
