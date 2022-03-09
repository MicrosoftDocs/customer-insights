---
title: "Select source fields for data unification"
description: "The first step in the unification process is selecting entities, attributes, primary keys, and semantic types to map data to the unified customer profile."
ms.date: 03/08/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: adkuppa
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-map
  - ci-match
  - customerInsights
---

# Map entities and attributes for data unification

The first step in customer or account unification is selecting the entities and attributes within your datasets that you want to unify.

> [!NOTE]
> For individual consumers (B-C), the unification process involves customers. For business accounts, this part of the unification process involves accounts. Screen titles indicate whether it is customers or accounts.

1. Go to **Data** > **Unify**.

1. For Source fields, select **Get started**.

1. Select the customer data **Entities** to combine into a customer profile.

1. For each entity, identify the columns you want to combine and reconcile. These columns are called *Attributes*. You can select the required attributes individually from an entity or include all attributes from an entity by selecting the **Include all fields** checkbox on the entity level. You can search on keywords across all attributes and entities to select the required attributes you want to map.

   <!--- Insert screenshot --->

   In this example, we're adding the **eCommerceContacts** and **loyCustomers** entities. By choosing these entities, you can derive insights on which of the online business customers are loyalty program members.

1. Select **Apply** to confirm your selections. The selected entities and attributes display.

## Select primary key and semantic type for attributes

<!--- Insert screenshot --->

1. Choose the **Primary key** for each entity. The primary key is an attribute unique to the entity. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.

1. For each attribute, choose a semantic type that best describes that attribute, such as name, city, or email address.

   > [!NOTE]
   > One field should map to the semantic type Person.FullName to populate the customer name in customer card. Otherwise, the customer cards will appear nameless.

   1. To use AI models for smart prediction of semantics, save time and improve accuracy, turn on **Intelligent mapping**. Intelligent mapping highlights AI-based semantics recommendation in the **Type** field. You can select any semantic type from the available list of options and override the suggested selection.
  
   1. To change an attribute type identified by the system, add a custom semantic type. Select the type field for an attribute, and type your custom semantic type name.

   1. To add an attribute thant contains a URL to profile images or logos, select the entity and field that contains the URL. In the **Type** input field, enter the following:
      - For a person: Person.ProfileImage
      - For an organization: Organization.LogoImage

   1. For an organization (preview) attribute, enter the attribute type "Organization.Name".

1. For attributes where a semantic type is automatically identified, review these attributes and types as they'll be used to combine your entities. These attributes are listed under **Review mapped fields**.

1. For attributes that aren't automatically mapped to a semantic type, select a semantic type field, or enter your custom attribute-type name. These attributes are listed under **Define the data in the unmapped fields**.

1. Click **Next**. Go to [Remove duplicates](remove-duplicates.md).

[!INCLUDE[footer-include](../includes/footer-banner.md)]
