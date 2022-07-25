---
title: "Relationships between entities and entity paths"
description: "Create and manage relationships between entities from multiple data sources."
ms.date: 09/27/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: CadeSanthaMSFT
ms.author: cadesantha
manager: shellyha
searchScope: 
  - ci-semantic-mapping
  - ci-entities
  - ci-relationships
  - ci-activities
  - ci-activities-wizard
  - ci-measures
  - ci-segments
  - ci-segment-builder
  - ci-measure-builder
  - ci-measure-template
  - ci-permissions
  - customerInsights
---

# Relationships between entities and entity paths

Relationships connect entities and define a graph of your data when entities share a common identifier, a foreign key. This foreign key can be referenced from one entity to another. Connected entities enable the definition of segments and measures based on multiple data sources.

There are three types of relationships: 
- Non-editable system relationships are created by the system as part of the data unification process
- Non-editable inherited relationships are created automatically from ingesting data sources
- Editable custom relationships are created and configured by users

## Non-editable system relationships

During data unification, system relationships are created automatically based on intelligent matching. These relationships help relate the customer profile records with corresponding records. The following diagram illustrates the creation of three system-based relationships. The customer entity is matched with other entities to produce the unified *Customer* entity.

:::image type="content" source="media/relationships-entities-merge.png" alt-text="Diagram with relationship paths for the customer entity with three 1-n relationships.":::

- ***CustomerToContact* relationship** was created between the *Customer* entity and the *Contact* entity. The *Customer* entity gets the key field **Contact_contactID** to relate to the *Contact* entity key field **contactID**.
- ***CustomerToAccount* relationship** was created between the *Customer* entity and the *Account* entity. The *Customer* entity gets the key field **Account_accountID** to relate to the *Account* entity key field **accountID**.
- ***CustomerToWebAccount* relationship** was created between the *Customer* entity and the *WebAccount* entity. The *Customer* entity gets the key field **WebAccount_webaccountID** to relate to the *WebAccount* entity key field **webaccountID**.

## Non-editable inherited relationships

During the data ingestion process, the system checks data sources for existing relationships. If no relationship exists, the system automatically creates them. These relationships are also used in downstream processes.

## Create a custom relationship

Relationship consists of a *source entity* containing the foreign key and a *target entity* that the source entity's foreign key points to. 

1. Go to **Data** > **Relationships**.

2. Select **New relationship**.

3. In the **New relationship** pane, provide the following information:

   :::image type="content" source="media/relationship-add.png" alt-text="New relationship side pane with empty input fields.":::

   - **Relationship name**: Name that reflects the purpose of the relationship. Example: CustomerToSupportCase.
   - **Description**: Description of the relationship.
   - **Source entity**: Entity that is used as a source in the relationship. Example: SupportCase.
   - **Target entity**: Entity that is used as a target in the relationship. Example: Customer.
   - **Source cardinality**: Cardinality of the source entity. Cardinality describes the number of possible elements in a set. It always relates to the target cardinality. You can choose between **One** and **Many**. Only many-to-one and one-to-one relationships are supported.  
     - Many-to-one: Multiple source records can relate to one target record. Example: Multiple support cases from a single customer.
     - One-to-one: A single source record relates to a one target record. Example: One loyalty ID for a single customer.

     > [!NOTE]
     > Many-to-many relationships can be created using two many-to-one relationships and a linking entity, which connects the source entity and the target entity.

   - **Target cardinality**: Cardinality of the target entity records.
   - **Source key field**: Foreign key field in the source entity. Example: SupportCase uses  **CaseID** as the foreign key field.
   - **Target key field**: Key field of the target entity. Example: Customer uses  **CustomerID** as the key field.

4. Select **Save** to create the custom relationship.

## Set up account hierarchies

Environments that are configured to use business accounts as the primary target audience can configure account hierarchies for related business accounts. For example, a company that has separate business units.

Organizations create account hierarchies to better manage accounts and their relationships with each other. Customer Insights supports parent-child account hierarchies that already exist in ingested customer data. For example, accounts from Dynamics 365 Sales. These hierarchies can be configured on the **Relationships** page.

1. Go to **Data** > **Relationships**.
1. Select the **Account hierarchy** tab.
1. Select **New account hierarchy**.
1. In the **Account hierarchy** pane, provide a name for the hierarchy. The system creates a name for the output entity, but you can change it.
1. Select the entity that contains your account hierarchy. It's usually in the same entity that contains the accounts.
1. Select the **Account UID** and **Parent UID** from the selected entity.
1. Select **Save** to finalize the account hierarchy.

## Manage existing relationships

Go to the **Relationships** page to view all the relationships that have been created, their source entity, the target entity, and the cardinality.

:::image type="content" source="media/relationships-list.png" alt-text="List of relationships and options in the action bar of the Relationships page.":::

Use the **Filter by** or **Search relationships** options to locate a particular relationship. To see a network diagram of the existing relationships and their cardinality, select [**Visualizer**](#explore-the-relationship-visualizer).

Select a relationship to view available actions:
- **Edit**: Update properties of custom relationships in the edit pane and save changes.
- **Delete**: Delete custom relationships.
- **View**: View system-created and inherited relationships.

### Explore the relationship visualizer

The relationship visualizer shows a network diagram of the existing relationships between connected entities and their cardinality. It also visualizes the relationship path.

:::image type="content" source="media/relationship-visualizer.png" alt-text="Screenshot of the relationship visualizer network diagram with connections between related entities.":::

To customize the view, you can change the position of the boxes by dragging them on the canvas. Other options include: 
- **Export as image**: Save the current view as an image file.
- **Change to horizontal/vertical layout**: Change the alignment of the entities and relationships.
- **Edit**: Update properties of custom relationships in the edit pane and save changes.

## Relationship paths

A relationship path describes the entities that are connected with relationships between a source entity and a target entity. It's used when creating a segment or a measure that includes entities other than the unified profile entity and there are multiple options to reach the unified profile entity. Different relationship paths can yield different results.

For example, the entity *eCommerce_eCommercePurchases* has the following relationships to the unified profile *Customer* entity:

- eCommerce_eCommercePurchases > Customer
- eCommerce_eCommercePurchases > eCommerce_eCommerceContacts > POS_posPurchases > Customer
- eCommerce_eCommercePurchases > eCommerce_eCommerceContacts > POS_posPurchases > loyaltyScheme_loyCustomers > Customer

A relationship path determines which entities you can use when creating rules for measures or segments. Choosing the option with the longest relationship path will likely yield fewer results because the matching records need to be part of all entities. In this example, a customer has to have purchased goods through e-commerce(eCommerce_eCommercePurchases) at a point of sale(POS_posPurchases) and participate in our loyalty program (loyaltyScheme_loyCustomers). When choosing the first option, you'd likely get more results because customers only need to exist in one additional entity.

### Direct relationship

A relationship is classified as a **direct relationship** when a source entity relates to a target entity with only one relationship.

For example, if an activity entity called *eCommerce_eCommercePurchases* connects to a target entity *eCommerce_eCommerceContacts* entity through *ContactId* only, it's a direct relationship.

:::image type="content" source="media/direct_Relationship.png" alt-text="Source entity connects directly to target entity.":::

#### Multi-path relationship

A **multi-path relationship** is a special type of direct relationship that connects a source entity to more than one target entity.

For example, if an activity entity called *eCommerce_eCommercePurchases* relates to two target entities, both *eCommerce_eCommerceContacts* and *loyaltyScheme_loyCustomers*, it's a multi-path relationship.

:::image type="content" source="media/multi-path_relationship.png" alt-text="Source entity connects directly to more than one target entity through a multi-hop relationship.":::

### Indirect relationship

A relationship is classified as an **indirect relationship** when a source entity relates to one or more additional entities before relating to a target entity.

#### Multi-hop relationship

A **multi-hop relationship** is an *indirect relationship* that allows you to connect a source entity to a target entity through one or more other intermediary entities.

For example, if an activity entity called *eCommerce_eCommercePurchasesWest* connects to an intermediate entity called *eCommerce_eCommercePurchasesEast* and then connects to a target entity called *eCommerce_eCommerceContacts*, it's a multi-hop relationship.

:::image type="content" source="media/multi-hop_relationship.png" alt-text="Source entity connects directly to a target entity with an intermediate entity.":::

### Multi-hop, multi-path relationship

Multi-hop and multi-path relationships can be used together to create **multi-hop, multi-path relationships**. This special type combines the functions of **multi-hop** and **multi-path relationships**. It lets you connect to more than one target entity while using intermediate entities.

For example, if an activity entity called *eCommerce_eCommercePurchasesWest* connects to an intermediate entity called *eCommerce_eCommercePurchasesEast* and then connects to two target entities, both *eCommerce_eCommerceContacts* and *loyaltyScheme_loyCustomers*, it's a multi-hop, multi-path relationship.

:::image type="content" source="media/multi-hop_multi-path_relationship.png" alt-text="Source entity connects directly to one target entity and connects to another target entity through an intermediate entity.":::

## Next step

System and custom relationships are used to [create segments](segments.md) and [measures](measures.md) based on multiple data sources that are no longer siloed.

[!INCLUDE [footer-include](includes/footer-banner.md)]
