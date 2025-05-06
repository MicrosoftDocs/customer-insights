---
title: "Relationships between tables and table paths"
description: "Create and manage relationships between tables from multiple data sources."
ms.date: 01/22/2025
ms.reviewer: mhart
ms.topic: article
author: srivas15
ms.author:  shsri
ms.custom: bap-template
---

# Relationships between tables and table paths

Customer data is often spread across multiple tables. It's critical for this data to be connected to each other so you can leverage it for your scenarios. For example, you have a table for users, orders, order details, and products. Let's say you want a segment of all users who placed an order recently. To create this segment, you can't use the *Users* table alone, but would need the *Orders* table and the *Users* table. Your *Users* and *Orders* table must be linked to each other with a key like **userId**. Relationships in Customer Insights - Data let you link your tables together, enabling you to use all of your data across segments and measures and other Customer Insights - Data processes.

Relationships define a graph of your data when tables share a common identifier, a foreign key. This foreign key can be referenced from one table to another. A relationship consists of a *source table* containing the foreign key and a *target table* that the source table's foreign key points to.

There are three types of relationships: 
- Non-editable system relationships are created by the system as part of the data unification process
- Non-editable inherited relationships are created automatically from ingesting data sources
- Editable custom relationships are created and configured by users

## Non-editable system relationships

During data unification, system relationships are created automatically based on intelligent matching. These relationships help relate the customer profile records with corresponding records. The following diagram illustrates the creation of three system-based relationships. The customer table is matched with other tables to produce the unified *Customer* table.

:::image type="content" source="media/relationships-tables-merge.png" alt-text="Diagram with relationship paths for the customer table with three 1-n relationships.":::

- ***CustomerToContact* relationship** was created between the *Customer* table and the *Contact* table. The *Customer* table gets the key field **Contact_contactID** to relate to the *Contact* table key field **contactID**.
- ***CustomerToAccount* relationship** was created between the *Customer* table and the *Account* table. The *Customer* table gets the key field **Account_accountID** to relate to the *Account* table key field **accountID**.
- ***CustomerToWebAccount* relationship** was created between the *Customer* table and the *WebAccount* table. The *Customer* table gets the key field **WebAccount_webaccountID** to relate to the *WebAccount* table key field **webaccountID**.

## Non-editable inherited relationships

During the data ingestion process, the system checks data sources for existing relationships. If no relationship exists, the system automatically creates them. These relationships are also used in downstream processes.

## Create a custom relationship

Custom relationships allow you to connect two tables that can then be used together in downstream segments and measures. 

For example, you want to build a segment of all customers who purchased coffee from a store in New York. Your data is stored in three tables:
- loyaltyContacts: contains a list of all customers. Columns include LoyaltyId and FullName.
- Purchases: contains purchase history of all customers. Columns include Timestamp, LoyaltyId, PurchasePrice, and StoreId.
- Stores: contains more details about each store. Columns include StoreId, StoreSize, and StoreLocation.
For this example, create a custom relationship between Purchases and Stores as a many (purchases) to one (stores) relationship on the StoreId column. Once established, you can create the required segment by adding a filter on the StoreLocation column in the Stores table.

1. Go to **Data** > **Tables**.

1. Select the **Relationships** tab.

1. Select **New relationship**.

1. In the **New relationship** pane, provide the following information:

   :::image type="content" source="media/relationship-add.png" alt-text="New relationship side pane with empty input fields.":::

   - **Relationship name**: Name that reflects the purpose of the relationship. Relationship names are case sensitive. Example: PurchasesToStores.
   - **Description**: Description of the relationship.
   - **Source table**: Table that is used as a source in the relationship. Example: Purchases.
   - **Target table**: Table that is used as a target in the relationship. Example: Stores.
   - **Source cardinality**: Cardinality of the source table. Cardinality describes the number of possible elements in a set. It always relates to the target cardinality. You can choose between **One** and **Many**. Only many-to-one and one-to-one relationships are supported.
     - Many-to-one: Multiple source records can relate to one target record. Example: Multiple purchases from a single store.
     - One-to-one: A single source record relates to a one target record.

     > [!NOTE]
     > Many-to-many relationships can be created using two many-to-one relationships and a linking table, which connects the source table and the target table.

   - **Target cardinality**: Cardinality of the target table records.
   - **Source key field**: Foreign key field in the source table. Example: StoreId
   - **Target key field**: Key field of the target table. Example: StoreId

1. Select **Save** to create the custom relationship.

## Manage existing relationships

Go to **Data** > **Tables** and the **Relationships** tab to view all the relationships that have been created, their source table, the target table, and the cardinality.

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

A relationship path determines which tables you can use when creating rules for measures or segments. Choosing the option with the longest relationship path will likely yield fewer results because the matching records need to be part of all tables. In this example, a customer has to have purchased goods through e-commerce(eCommerce_eCommercePurchases) at a point of sale(POS_posPurchases) and participate in our loyalty program (loyaltyScheme_loyCustomers). When choosing the first option, you'd likely get more results because customers only need to exist in one other table.

### Direct relationship

A relationship is classified as a **direct relationship** when a source table relates to a target table with only one relationship.

For example, if an activity table called *eCommerce_eCommercePurchases* connects to a target table *eCommerce_eCommerceContacts* table through *ContactId* only, it's a direct relationship.

:::image type="content" source="media/direct_Relationship.png" alt-text="Source table connects directly to target table.":::

#### Multi-path relationship

A **multi-path relationship** is a special type of direct relationship that connects a source table to more than one target table.

For example, if an activity table called *eCommerce_eCommercePurchases* relates to two target tables, both *eCommerce_eCommerceContacts* and *loyaltyScheme_loyCustomers*, it's a multi-path relationship.

:::image type="content" source="media/multi-path_relationship.png" alt-text="Source table connects directly to more than one target table through a multi-hop relationship.":::

### Indirect relationship

A relationship is classified as an **indirect relationship** when a source table relates to one or more other tables before relating to a target table.

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
