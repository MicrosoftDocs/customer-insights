---
title: "Power Apps connector (preview)"
description: "Connect with Power Apps and Power Automate."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Power Apps connector (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Bring unified customer profiles into your personalized apps with Microsoft Power Apps.

> [!TIP]
> We recommend using this option [to create apps with Dataverse data](/power-apps/maker/). It ensures you benefit from our [integration into Dataverse](integrate-d365-apps.md).

## Connect Power Apps and Dynamics 365 Customer Insights - Data

Customer Insights - Data is one of the many [available sources for data in Power Apps](/powerapps/maker/canvas-apps/working-with-data-sources).

Refer to the Power Apps documentation to learn how to [add a data connection to an app](/powerapps/maker/canvas-apps/add-data-connection). We recommend you also review [how Power Apps uses delegation to handle large datasets in Canvas apps](/powerapps/maker/canvas-apps/delegation-overview).

## Available tables

After adding Customer Insights - Data as a data connection, choose the following tables in Power Apps:

- **Customer**: to use data from the [unified customer profile](customer-profiles.md).
- **UnifiedActivity**: to display the [activity timeline](activities.md) in the app.

## Limitations

### Retrievable tables

You can only retrieve the **Customer**, **UnifiedActivity**, and **Segments** tables through the Power Apps connector. Other tables are shown because the underlying connector supports them through triggers in Power Automate.

You can do a maximum of 100 calls per 60 seconds. You can call the API endpoint multiple times by using the $skip parameter. [Learn more about the $skip parameter](/connectors/customerinsights/#get-items-from-a-table).

### Delegation

Delegation works for the **Customer** table and **UnifiedActivity** table.

- Delegation for **Customer** table: To use delegation for this table, the fields need to be indexed in [search & filter index](search-filter-index.md).  
- Delegation for **UnifiedActivity**: Delegation for this table only works for the fields **ActivityId** and **CustomerId**.  

For more information about delegation, go to [Power Apps delegable functions and operations](/powerapps/maker/canvas-apps/delegation-overview).

## Example gallery control

Optionally, add customer profiles to a [gallery control](/powerapps/maker/canvas-apps/add-gallery).

1. Add a **gallery** control to an app you're building.
  
   :::image type="content" source="media/connector-powerapps9.png" alt-text="Add a gallery element.":::

1. Select **Customer** as the data source for items.

   :::image type="content" source="media/choose-datasource-powerapps.png" alt-text="Select a data source.":::

1. Change the data panel on the right to select which field for the Customer table to show on the gallery.

1. If you want to show any field from the selected customer on the gallery, fill in the **Text** property of a label using **{Name_of_the_gallery}.Selected.{property_name}**  
    - For example: _Gallery1.Selected.address1_city_

1. To display the unified timeline for a customer, add a gallery element, and add the **Items** property using **Filter('UnifiedActivity', CustomerId = {Customer_Id})**  
    - For example: _Filter('UnifiedActivity', CustomerId = Gallery1.Selected.CustomerId)_

[!INCLUDE [footer-include](includes/footer-banner.md)]
