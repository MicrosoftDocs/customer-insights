---
title: Filter cities by selected country in Customer Insights - Journeys forms
description: Discover how to create country and city lookups, populate the values and set up relationship using forms in Dynamics 365 Customer Insights - Journeys. Learn more now!
ms.date: 08/15/2025
ms.update-cycle: 180-days
ms.topic: how-to
author: petrjantac
ms.author: colinbirkett
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Filter cities by selected country in Customer Insights - Journeys forms

Filtering the list of cities based on the selected country is a powerful way to simplify form interactions and improve data accuracy. Instead of overwhelming users with long, irrelevant dropdowns, this approach ensures they only see city options that match their chosen country—making the form faster to complete and easier to understand. This is especially valuable in scenarios like lead routing, where selecting the correct location ensures submissions reach the right team. In this guide, you learn how to set up this filtering using lookup fields and relationships between data tables.

:::image type="content" source="media/cascading-form-fields.gif" alt-text="Cascading form fields." lightbox="media/cascading-form-fields.gif":::

Filtered lookup fields feature is available for both marketing and event registration form types.

To enable filtered lookup fields in your form—such as showing only cities that match the selected country—follow these setup steps:

1. **Create a new Solution**, which helps you organize all related components (custom tables, relationships, forms, views, and scripts) in one place, making it easier to manage, deploy, and maintain.
1. **Create custom entities for Country and City**, as the default fields (address1_country and address1_city) are simple text fields and don't support filtering. **Establish a relationship** between the Country and City entities. This relationship is required for filtering to work.
1. **Populate the Country and City entities** with relevant data to ensure meaningful lookup options.
1. **Link the custom Country and City** entities to the **Contact** and/or **Lead** entities so they can be used in forms.
1. **Add read permission** for the **Marketing Services User Extensible Role** to access Country and City entities.
1. **Create a new marketing form** and add Country and City fields

Once these steps are complete, the new Country and City fields appear in the **form editor** as lookup fields, enabling dynamic filtering.

## 1. Create a new Solution

1. Go to **Power Apps**.
1. Navigate to Solutions in the left-hand menu.
1. Select **+ New Solution**.
1. Enter a name (for example, LocationLookupFiltering), publisher, and version.
1. Select **Create**.

Once your solution is created, you can add all the components from the following steps—custom entities, relationships, form customizations, and filtering logic—into this solution for better structure and portability.

> [!TIP]
> Get more information about the benefits of using [Solutions](https://learn.microsoft.com/power-apps/maker/data-platform/create-solution) for customizations and understand how to create them.

## 2. Create Custom Entities for Country and City and establish relationship

1. In your Solution in Power Apps, select **+ New** and select **Table**.
1. You can import XLSX files with the list of countries to simplify the process or you can build the table from scratch.
1. Name the table **Country**.
1. Add a Primary Column (for example, Country Name) of type Text.
1. Optionally, add other columns like Country Code or Region if needed.
1. Create another table named **City**.
1. Add a Primary Column (for example, City Name) of type Text.
1. Add a **Lookup Column that references the Country table**. This establishes the relationship needed for filtering.
    - Name it Country Lookup.
    - Set the related table to Country.
1. Select **Save and exit** to publish the tables.

:::image type="content" source="media/power-apps-country-city-relationship.png" alt-text="Create Country and City tables." lightbox="media/power-apps-country-city-relationship.png":::

> [!TIP]
> You can [learn more](https://learn.microsoft.com/power-apps/maker/data-platform/create-edit-entities-portal) about creating custom tables in Power Apps.

## 3. Populate the City and Country entities with data

- Use **Excel import**, **Power Automate**, or **manual entry in Power Apps** to add records to both tables.
- Ensure each City record is linked to the correct Country via the lookup field.

:::image type="content" source="media/power-apps-country-city.png" alt-text="Populate data for City table." lightbox="media/power-apps-country-city.png":::

> [!TIP]
> There are various ways to [import data](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-import-export).

## 4. Link Custom Country and City Entities to Contact and/or Lead Entities

To use your newly created Country and City lookup fields in forms for Contact or Lead records, you need to establish relationships between these entities.

**Add Lookup Fields to Contact or Lead**
    1. In your Solution in Power Apps, **Add existing Table** to add the Contact or Lead table into your Solution.
    1. Navigate to the Columns section and select **+ Add Column**.
    1. Choose Data Type: Lookup.
    1. For the Related Table, select Country.
    1. Name the column (for example, Preferred Country or simply Country).
    1. Repeat the process to add a City lookup column, selecting City as the related table.
**Save and Publish**
After adding both lookup columns, select **Save and exit** and **Publish All Customizations** to make the changes available in the form editor.

:::image type="content" source="media/power-apps-add-country-contact.png" alt-text="Link Country lookup to Contact entity." lightbox="media/power-apps-add-country-contact.png":::

> [!TIP]
> You can enable the Country lookups for the combined Lead & Contact audience by creating a mapping between Contact -> Country and Lead -> Country. The same applies for City lookup. [Learn more about mapping](real-time-marketing-form-global-settings.md#lead-contact-mapping).

## 5. Add read permission for the service user

To ensure that users visiting your form can see the options listed in the Country and City lookup fields, you need to grant read access to these entities through the appropriate security role.

1. Go to the **Power Platform Admin Center**.
1. Select the environment where your form and entities are located.
1. Go to Settings > Users + Permissions > Security Roles.
1. Find and open the **Marketing Services User Extensible Role**.
1. Locate the Country and City entities (your custom tables).
1. Set the **Read** permission to **Organization** level for both entities.
1. Select **Save** to apply the changes.

:::image type="content" source="media/power-platform-country.png" alt-text="Set up value filtering." lightbox="media/power-platform-country.png":::

[Learn more](https://learn.microsoft.com/power-platform/admin/security-roles-privileges) about security roles.

## 6. Create a new marketing form

1. Create a new marketing or event registration form.
1. The Country and City fields are now available in the list of fields in the right pane.
1. Add Country and City lookup fields to your form. Ensure both lookup fields are properly configured.
1. Select the **City** field and use the **Filter values** button to define the filtering.
    :::image type="content" source="media/real-time-marketing-form-filter-values.png" alt-text="Select City as filter." lightbox="media/real-time-marketing-form-filter-values.png":::
1. In the filtering configuration window, select **Country** as the field for **Based on answer to**—this defines which lookup field acts as the filter input. Then, select **Country** under **Show values for** to specify the relationship that connects the Country and City entities and enables the filtering logic.
    :::image type="content" source="media/real-time-marketing-filter-cities-by-country.png" alt-text="Select relationship for filtering." lightbox="media/real-time-marketing-filter-cities-by-country.png":::
1. **Publish** and test your form.

**The setup is complete!** Your form offers a streamlined and intelligent experience—showing users only the most relevant options based on their selections. This not only improves data quality and reduces errors, but also makes the form faster and more intuitive to complete. You're now ready to deliver a professional, user-friendly solution that enhances both customer satisfaction and operational efficiency.

[!INCLUDE [footer-include](./includes/footer-banner.md)]