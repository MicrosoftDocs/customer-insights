---
title: Filter cities by selected country/region in Customer Insights - Journeys forms
description: 'Customer Insights - Journeys forms: Filter city options by country/region for faster, more accurate submissions. Learn how to set up filtered lookups.'
ms.date: 08/26/2025
ms.update-cycle: 180-days
ms.topic: how-to
author: petrjantac
ms.author: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:08/26/2025
---

# Filter cities by selected country/region in Customer Insights - Journeys forms

Filtering the list of cities based on the selected country/region is a powerful way to simplify form interactions and improve data accuracy. Instead of overwhelming users with long, irrelevant dropdowns, this approach ensures they only see city options that match their chosen country/region—making the form faster to complete and easier to understand. This is especially valuable in scenarios like lead routing, where selecting the correct location ensures submissions reach the right team. In this guide, you learn how to set up this filtering using lookup fields and relationships between data tables.

The filtered lookup fields feature is available for marketing and event registration forms.

## Set up filtered lookup fields

Set up filtered lookup fields in your form, like showing only cities that match the selected country/region, by following these steps. Each step is explained in detail later in this article.

1. **Create a new solution** to organize all related components (custom tables, relationships, forms, views, and scripts) in one place. This approach makes it easier to manage, deploy, and maintain your work.
1. **Create custom entities for country/region and city** because the default fields (`address1_country` and `address1_city`) are simple text fields and can't support filtering. **Establish a relationship** between the country/region and city entities. This relationship lets filtering work.
1. **Populate the country/region and city entities** with relevant data so lookup options are meaningful.
1. **Link the custom country/region and city** entities to contact or lead entities so you can use them in forms.
1. **Add read permission** for the **Marketing Services User Extensible Role** so it can access the country/region and city entities.
1. **Create a new marketing form** and add country/region and city fields.

After you finish these steps, the new country/region and city fields appear in the **form editor** as lookup fields, letting you use dynamic filtering.

### 1. Create a new solution

1. Go to [**Power Apps**](https://make.powerapps.com/).
1. Navigate to **Solutions** in the left-hand menu.
1. Select **+New Solution**.
1. Enter a name (for example, `LocationLookupFiltering`), publisher, and version.
1. Select **Create**.

Once your solution is created, you can add all the components from the following steps (custom entities, relationships, form customizations, and filtering logic) into the solution for better structure and portability.

> [!TIP]
> Learn more about the benefits of using solutions for customizations and understand how to create them: [Create a solution](/power-apps/maker/data-platform/create-solution).

### 2. Create custom entities for country/region and city and establish a relationship

1. In your solution in Power Apps, select **+New** and select **Table**.
1. You can import XLSX files with the list of countries to simplify the process or you can build the table from scratch.
1. Name the table **Country/region**.
1. Add a primary column (for example, "Country/region Name") of type **Text**.
1. Optionally, add other columns like "Country/region Code" or "Region" if needed.
1. Create another table named **City**.
1. Add a primary column (for example, "City Name") of type **Text**.
1. Add a lookup column that references the Country/region table. This step creates the relationship needed for filtering.
1. Select **Save and exit** to publish the tables.

:::image type="content" source="media/power-apps-country-city-relationship.png" alt-text="Create Country/region and City tables." lightbox="media/power-apps-country-city-relationship.png":::

> [!TIP]
> Learn more about creating custom tables in Power Apps: [Create and edit tables using Power Apps](/power-apps/maker/data-platform/create-edit-entities-portal).

### 3. Populate the city and country/region entities with data

- Use **Excel import**, **Power Automate**, or **manual entry in Power Apps** to add records to both tables.
- Make sure each city record links to the correct country/region using the lookup field.

:::image type="content" source="media/power-apps-country-city.png" alt-text="Populate data for City table." lightbox="media/power-apps-country-city.png":::

> [!TIP]
> Learn more about the various ways to import data: [Import data from Excel and export data to CSV](/power-apps/maker/data-platform/data-platform-import-export).

### 4. Link custom country/region and city entities to contact or lead entities

To use your new country/region and city lookup fields in forms for contact or lead records, establish relationships between the entities.

1. **Add lookup fields to contact or lead**
    1. In your solution in Power Apps, select **Add existing Table** to add the contact or lead table to your solution.
    1. Navigate to the **Columns** section and select **+Add Column**.
    1. Choose data type **Lookup**.
    1. For the **Related Table**, select **Country/region**.
    1. Name the column (for example, "Preferred Country/region" or "Country/region").
    1. Repeat the process to add a "City" lookup column. Select "City" as the related table.
1. **Save and publish**: After you add both lookup columns, select **Save and exit**, then select **Publish All Customizations** to make the changes available in the form editor.

:::image type="content" source="media/power-apps-add-country-contact.png" alt-text="Link Country/region lookup to Contact entity." lightbox="media/power-apps-add-country-contact.png":::

> [!TIP]
> Enable the country/region lookups for the combined Lead & Contact audience by creating a mapping between **Contact** > **Country/region** and **Lead** > **Country/region**. The same applies for city lookup. Learn more about mapping: [Lead-Contact Mapping](real-time-marketing-form-global-settings.md#lead-contact-mapping).

### 5. Add read permission for the service user

To make sure users visiting your form can see the options in the country/region and city lookup fields, grant read access to the entities through the appropriate security role.

1. Go to the [**Power Platform Admin Center**](https://admin.powerplatform.microsoft.com).
1. Select the environment where your form and entities are located.
1. Go to **Settings** > **Users + Permissions** > **Security Roles**.
1. Find and open the **Marketing Services User Extensible Role**.
1. Locate the "Country/region" and "City" entities (your custom tables).
1. Set the **Read** permission to **Organization** level for both entities.
1. Select **Save** to apply the changes.

:::image type="content" source="media/power-platform-country.png" alt-text="Set up value filtering." lightbox="media/power-platform-country.png":::

Learn more about security roles in [Security roles and privileges](/power-platform/admin/security-roles-privileges).

### 6. Create a new marketing form

1. Create a new marketing or event registration form.
1. The "Country/region" and "City" fields are now available in the list of fields in the right pane.
1. Add "Country/region" and "City" lookup fields to your form. Make sure both lookup fields are properly configured.
1. Select the **City** field and use the **Filter values** button to set up the filtering.
1. In the filtering configuration window, select **Country/region** as the field for **Based on answer to**—this choice sets which lookup field acts as the filter input. Then, select **Country/region** under **Show values for** to specify the relationship that connects the Country/region and City entities and lets the filtering logic work.
1. **Publish** and test your form.

You're done setting up! Your form now shows users only the most relevant options based on their selections. This approach improves data quality, reduces errors, and makes the form faster and easier to complete. You're ready to deliver a professional, user-friendly solution that helps customer satisfaction and operational efficiency.

[!INCLUDE [footer-include](./includes/footer-banner.md)]