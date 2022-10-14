---
title: "Relationships between tables and table paths"
description: "Create and manage relationships between tables from multiple data sources."
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

# Relationships between tables and table paths

Relationships connect tables and define a graph of your data when tables share a common identifier, a foreign key. This foreign key can be referenced from one table to another. Connected tables enable the definition of segments and measures based on multiple data sources.

There are three types of relationships: 
- Non-editable system relationships are created by the system as part of the data unification process
- Non-editable inherited relationships are created automatically from ingesting data sources
- Editable custom relationships are created and configured by users

## Non-editable system relationships

During data unification, system relationships are created automatically based on intelligent matching. These relationships help relate the customer profile records with corresponding records. The following diagram illustrates the creation of three system-based relationships. The customer table is matched with other tables to produce the unified *Customer* table.

:::image type="content" source="media/relationships-entities-merge.png" alt-text="Diagram with relationship paths for the customer table with three 1-n relationships.":::

- ***CustomerToContact* relationship** was created between the *Customer* table and the *Contact* table. The *Customer* table gets the key field **Contact_contactID** to relate to the *Contact* table key field **contactID**.
- ***CustomerToAccount* relationship** was created between the *Customer* table and the *Account* table. The *Customer* table gets the key field **Account_accountID** to relate to the *Account* table key field **accountID**.
- ***CustomerToWebAccount* relationship** was created between the *Customer* table and the *WebAccount* table. The *Customer* table gets the key field **WebAccount_webaccountID** to relate to the *WebAccount* table key field **webaccountID**.

## Non-editable inherited relationships

During the data ingestion process, the system checks data sources for existing relationships. If no relationship exists, the system automatically creates them. These relationships are also used in downstream processes.

## Create a custom relationship

Relationship consists of a *source table* containing the foreign key and a *target table* that the source table's foreign key points to. 

1. Go to **Data** > **Relationships**.

2. Select **New relationship**.

3. In the **New relationship** pane, provide the following information:

   :::image type="content" source="media/relationship-add.png" alt-text="New relationship side pane with empty input fields.":::

   - **Relationship name**: Name that reflects the purpose of the relationship. Example: CustomerToSupportCase.
   - **Description**: Description of the relationship.
   - **Source table**: Table that is used as a source in the relationship. Example: SupportCase.
   - **Target table**: Table that is used as a target in the relationship. Example: Customer.
   - **Source cardinality**: Cardinality of the source table. Cardinality describes the number of possible elements in a set. It always relates to the target cardinality. You can choose between **One** and **Many**. Only many-to-one and one-to-one relationships are supported.  
     - Many-to-one: Multiple source records can relate to one target record. Example: Multiple support cases from a single customer.
     - One-to-one: A single source record relates to a one target record. Example: One loyalty ID for a single customer.

     > [!NOTE]
     > Many-to-many relationships can be created using two many-to-one relationships and a linking table, which connects the source table and the target table.

   - **Target cardinality**: Cardinality of the target table records.
   - **Source key field**: Foreign key field in the source table. Example: SupportCase uses  **CaseID** as the foreign key field.
   - **Target key field**: Key field of the target table. Example: Customer uses  **CustomerID** as the key field.

4. Select **Save** to create the custom relationship.

## Set up account hierarchies

Environments that are configured to use business accounts as the primary target audience can configure account hierarchies for related business accounts. For example, a company that has separate business units.

Organizations create account hierarchies to better manage accounts and their relationships with each other. Customer Insights supports parent-child account hierarchies that already exist in ingested customer data. For example, accounts from Dynamics 365 Sales. These hierarchies can be configured on the **Relationships** page.

1. Go to **Data** > **Relationships**.
1. Select the **Account hierarchy** tab.
1. Select **New account hierarchy**.
1. In the **Account hierarchy** pane, provide a name for the hierarchy. The system creates a name for the output table, but you can change it.
1. Select the table that contains your account hierarchy. It's usually in the same table that contains the accounts.
1. Select the **Account UID** and **Parent UID** from the selected table.
1. Select **Save** to finalize the account hierarchy.

## Manage existing relationships

Go to the **Relationships** page to view all the relationships that have been created, their source table, the target table, and the cardinality.

:::image type="content" source="media/relationships-list.png" alt-text="List of relationships and options in the action bar of the Relationships page.":::

Use the **Filter by** or **Search relationships** options to locate a particular relationship. To see a network diagram of the existing relationships and their cardinality, select [**Visualizer**](#explore-the-relationship-visualizer).

Select a relationship to view available actions:
- **Edit**: Update properties of custom relationships in the edit pane and save changes.
- **Delete**: Delete custom relationships.
- **View**: View system-created and inherited relationships.

### Explore the relationship visualizer

The relationship visualizer shows a network diagram of the existing relationships between connected tables and their cardinality. It also visualizes the relationship path.

:::image type="content" source="media/relationship-visualizer.png" alt-text="Screenshot of the relationship visualizer network diagram with connections between related tables.":::

To customize the view, you can change the position of the boxes by dragging them on the canvas. Other options include: 
- **Export as image**: Save the current view as an image file.
- **Change to horizontal/vertical layout**: Change the alignment of the tables and relationships.
- **Edit**: Update properties of custom relationships in the edit pane and save changes.

## Relationship paths

A relationship path describes the tables that are connected with relationships between a source table and a target table. It's used when creating a segment or a measure that includes tables other than the unified profile table and there are multiple options to reach the unified profile table. Different relationship paths can yield different results.

For example, the table *eCommerce_eCommercePurchases* has the following relationships to the unified profile *Customer* table:

- eCommerce_eCommercePurchases > Customer
- eCommerce_eCommercePurchases > eCommerce_eCommerceContacts > POS_posPurchases > Customer
- eCommerce_eCommercePurchases > eCommerce_eCommerceContacts > POS_posPurchases > loyaltyScheme_loyCustomers > Customer

A relationship path determines which tables you can use when creating rules for measures or segments. Choosing the option with the longest relationship path will likely yield fewer results because the matching records need to be part of all tables. In this example, a customer has to have purchased goods through e-commerce(eCommerce_eCommercePurchases) at a point of sale(POS_posPurchases) and participate in our loyalty program (loyaltyScheme_loyCustomers). When choosing the first option, you'd likely get more results because customers only need to exist in one additional table.

### Direct relationship

A relationship is classified as a **direct relationship** when a source table relates to a target table with only one relationship.

For example, if an activity table called *eCommerce_eCommercePurchases* connects to a target table *eCommerce_eCommerceContacts* table through *ContactId* only, it's a direct relationship.

:::image type="content" source="media/direct_Relationship.png" alt-text="Source table connects directly to target table.":::

#### Multi-path relationship

A **multi-path relationship** is a special type of direct relationship that connects a source table to more than one target table.

For example, if an activity table called *eCommerce_eCommercePurchases* relates to two target tables, both *eCommerce_eCommerceContacts* and *loyaltyScheme_loyCustomers*, it's a multi-path relationship.

:::image type="content" source="media/multi-path_relationship.png" alt-text="Source table connects directly to more than one target table through a multi-hop relationship.":::

### Indirect relationship

A relationship is classified as an **indirect relationship** when a source table relates to one or more additional tables before relating to a target table.

#### Multi-hop relationship

A **multi-hop relationship** is an *indirect relationship* that allows you to connect a source table to a target table through one or more other intermediary tables.

For example, if an activity table called *eCommerce_eCommercePurchasesWest* connects to an intermediate table called *eCommerce_eCommercePurchasesEast* and then connects to a target table called *eCommerce_eCommerceContacts*, it's a multi-hop relationship.

:::image type="content" source="media/multi-hop_relationship.png" alt-text="Source table connects directly to a target table with an intermediate table.":::

### Multi-hop, multi-path relationship

Multi-hop and multi-path relationships can be used together to create **multi-hop, multi-path relationships**. This special type combines the functions of **multi-hop** and **multi-path relationships**. It lets you connect to more than one target table while using intermediate tables.

For example, if an activity table called *eCommerce_eCommercePurchasesWest* connects to an intermediate table called *eCommerce_eCommercePurchasesEast* and then connects to two target tables, both *eCommerce_eCommerceContacts* and *loyaltyScheme_loyCustomers*, it's a multi-hop, multi-path relationship.

:::image type="content" source="media/multi-hop_multi-path_relationship.png" alt-text="Source table connects directly to one target table and connects to another target table through an intermediate table.":::

## Next step

System and custom relationships are used to [create segments](segments.md) and [measures](measures.md) based on multiple data sources that are no longer siloed.

[!INCLUDE [footer-include](includes/footer-banner.md)]
