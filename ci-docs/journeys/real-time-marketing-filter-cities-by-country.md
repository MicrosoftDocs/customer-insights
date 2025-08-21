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

Filtering the list of cities based on the selected country is a powerful way to simplify form interactions and improve data accuracy. Instead of overwhelming users with long, irrelevant dropdowns, this approach ensures they only see city options that match their chosen country—making the form faster to complete and easier to understand. This is especially valuable in scenarios like lead routing, where selecting the correct location ensures submissions reach the right team. In this guide, you'll learn how to set up this filtering using lookup fields and relationships between data tables.

To enable filtered lookup fields in your form—such as showing only cities that match the selected country—follow these setup steps:

1. **Create custom entities for Country and City**, as the default fields (address1_country and address1_city) are simple text . fields and do not support filtering. **Establish a relationship** between the Country and City entities. This relationship is required for filtering to work.
1. **Populate the Country and City entities** with relevant data to ensure meaningful lookup options.
1. **Link the custom Country and City** entities to the **Contact** and/or **Lead** entities so they can be used in forms.
1. **Add read permission** for the service user.
1. **Create a new marketing form** and add Country and City fields

Once these steps are complete, the new Country and City fields will appear in the **form editor** as lookup fields, enabling dynamic filtering.

## 1. Create Custom Entities for Country and City and establish relationship

1. Go to Power Apps and navigate to **Tables**.
1. Click **+ New Table**.
1. Name the table **Country**.
1. Add a Primary Column (e.g., Country Name) of type Text.
1. Optionally, add other columns like Country Code or Region if needed.
1. Create another table named **City**.
1. Add a Primary Column (e.g., City Name) of type Text.
1. Add a **Lookup Column that references the Country table**. This establishes the relationship needed for filtering.
    - Name it Country Lookup.
    - Set the related table to Country.
1. Save and publish the tables.

[Learn more](https://learn.microsoft.com/power-apps/maker/data-platform/create-edit-entities-portal) about creating custom tables in Power Apps.

## 2. Populate the City and Country entities with data

- Use **Excel import**, **Power Automate**, or manual entry to add records to both tables.
- Ensure each City record is linked to the correct Country via the lookup field.

[Learn more](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-import-export) about data import.

## 3. Link Custom Country and City Entities to Contact and/or Lead Entities

To use your newly created Country and City lookup fields in forms for Contact or Lead records, you need to establish relationships between these entities.

**Add Lookup Fields to Contact or Lead**
    1. In Power Apps, go to Tables and open the Contact or Lead table.
    1. Navigate to the Columns section and click + Add Column.
    1. Choose Data Type: Lookup.
    1. For the Related Table, select Country.
    1. Name the column (e.g., Preferred Country or simply Country).
    1. Repeat the process to add a City lookup column, selecting City as the related table.
**Save and Publish**
After adding both lookup columns, click **Save Table** and Publish All Customizations to make the changes available in the form editor.

## 4. Add read permission for the service user

To ensure that users visiting your form can see the options in the Country and City lookup fields, you need to grant read access to these entities through the appropriate security role.

1. Go to the Power Platform Admin Center.
1. Select the environment where your form and entities are located.
1. Go to Settings > Users + Permissions > Security Roles.
1. Find and open the Marketing Services User Extensible Role.
1. Locate the Country and City entities (your custom tables).
1. Set the Read permission to Organization level for both entities.
1. Click Save to apply the changes.

[Learn more](https://learn.microsoft.com/power-platform/admin/security-roles-privileges) about security roles.

## 5. Create a new marketing form

1. Create a new marketing form.
1. The Country and City fields are now available in the list of fields in the right pane.
1. Add Country and City fields to your form.
1. Select City field and use the Filter values button to define the filtering by Country.

:::image type="content" source="media/real-time-marketing-form-filter-values.png" alt-text="Set up value filtering." lightbox="media/real-time-marketing-form-filter-values.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]