---
title: "Semantic mappings (Preview)"
description: "Overview of semantic mappings and how to use them." 
ms.date: 09/20/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.reviewer: mhart
ms.topic: conceptual
author: CadeSanthaMSFT
ms.author: cadesantha
manager: shellyha
---

# Semantic Mappings

Semantic mappings allow you to map your non-activity data to pre-defined schemas, allowing Audience Insights to better understand your data attributes. Depending on the type of Semantic Mapping created and the data your provide, you will be able to enable new insights and features throughout Audience Insights. 

   > [!NOTE]
   > To map your activity data to pre-defined schemas, follow the steps outlined in the [activities](activities.md) documentation.

**Semantic mappings are currently enabled in B2B instances only**. There is currently one type of Semantic Mapping supported in Audience Insights: *ContactProfile*.

## Define a *ContactProfile* semantic entity mapping

1. In audience insights, go to **Data** > **Semantic mappings (preview)**.

1. Select **Add semantic mapping** to start the guided experience for the semantic mapping setup process.

1. In the **Entity data** step, set the values for the following fields:

   - **Semantic entity mapping name**: Select a name for your semantic entity mapping.
   - **Source Entity**: Select an entity that includes contact data.
   - **Primary key**: Select the field that uniquely identifies a contact record. It shouldn't contain any duplicate values, empty values, or missing values.

   :::image type="content" source="media/Semantic_Mapping_Wizard1.png" alt-text="Set up the semantic entity mapping with name, source entity, and primary key.":::

1. Select **Next** to go to the next step.

1. In the **Relationships** step, configure the details to connect your contact data to its corresponding account data. This step visualizes the connection between entities.  

   > [!Tip]
   > There are two types of relationship paths that can be implemented: **Direct relationships** and **Indirect relationships**.
   >   - Learn more about [direct and indirect relationship paths](relationships.md#relationship-paths)

   - **First**: Select **Add Relationship** to launch the relationship configuration steps.
   - **Second**: Select the attribute from your source entity that connects your contact entity to another entity.
   - **Third**: Select the entity to connect your contact entity to, either from the *Account entities* section or the *Intermediate entity* section. 
      - If you select an intermediate entity, you need to define a second relationship to connect to your target account entity.

   :::image type="content" source="media/Semantic_Mapping_Wizard2.png" alt-text="Select either an Account entity or an Intermediate entity.":::

   - **Fourth**: Name the defined relationship(s). If a relationship between your entities already exist, the relationship name will be in read-only mode. If no such relationship exists, a new relationship will be created with the name you provide in this box.
   - **Fifth**: Once you are finished configuring your relationship(s), select **Apply**. You will now see a visualization of your relationship(s) between your contact entity and your account entity.

   :::image type="content" source="media/Semantic_Mapping_Wizard3.png" alt-text="Click apply to confirm and apply relationship definition steps.":::

   > [!NOTE]
   > You are able to configure additional relationships between the contact entity and other account entities, utilizing intermediate entities as needed.
   >  :::image type="content" source="media/Semantic_Mapping_Wizard4.png" alt-text="Visualization of various relationships connect contact entities to account entities.":::

1. Once you are satisfied with your relationship configurations, select **Next** to go to the next step.

1. In the **Semantic type** step, start by selecting a **Semantic type**. Currently, there is one **Semantic Type** called *ContactProfile*.

1. Map your data to the *ContactProfile* **Semantic type** for the fields shown.
   - **Required Field**: *Contact ID*
   - **Optional Fields**: *First name*, *Last name*, *Birth date*, *Gender*, *Primary email*, and *Primary phone*

   :::image type="content" source="media/Semantic_Mapping_Wizard5.png" alt-text="Map your contact data attributes to the provided required and optional fields.":::

1. Select **Next** to go to the next step.

1. In the **Review** step, take a look at the configuration you have created for your **Semantic mapping**. To make changes to your configuration, select **Edit** for the corresponding section or select **Back** as many times as needed.

1. When you are satisfied with your configuration, select **Save** to save your new **Semantic mapping**.

   :::image type="content" source="media/Semantic_Mapping_Wizard6.png" alt-text="After confirming your configuration, select the save button.":::

1. After saving, you have the option of selecting **Run** to run the creation of your **Semantic mapping** or you can select **Close** to save your **Semantic mapping** without running it.

   :::image type="content" source="media/Semantic_Mapping_Wizard7.png" alt-text="Run your new semantic mapping or select close to run it at a later point.":::

1. To run a **Semantic mapping** at a later point, select the **Semantic mapping** of your choice and select **Refresh**.

> [!TIP]
> There are [six types of status](system.md#status-types) for tasks/processes. Additionally, most processes [depend on other downstream processes](system.md#refresh-policies). You can select the status of a process to see details on the progress of the entire job. After selecting **See details** for one of the job's tasks, you find additional information: processing time, the last processing date, and all errors and warnings associated with the task.

## Manage existing semantic mappings

On **Data** > **Semantic mappings (preview)**, you can view all your saved semantic mappings, and manage them. Each semantic mapping is represented by a row that includes details about the source entity, semantic type, mapping type, and status for that semantic mapping.

The following actions are available when you select a semantic mapping: 

- **Edit**: Opens the semantic mapping setup on the review step. You can change any or all of the current configuration from this step. After changing the configuration, select **Save** and then select **Run** to process the changes.

- **Refresh**: Regenerates the selected semantic mapping using the most up-to-date data from the respective entities utilized in the semantic mapping configuration.
> [!NOTE]
> Refreshing any given **Semantic mapping** will refresh all **Semantic mappings** of the same semantic type.

- **Rename**: Opens a dialog where you can enter a different name for the selected semantic mapping. Select **Save** to apply your changes.

- **Delete**: Opens a dialog to confirm the deletion of the selected semantic mapping. You can also delete more than one semantic mapping at once by selecting the semantic mappings and then selecting the delete icon. Select **Delete** to confirm the deletion.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
