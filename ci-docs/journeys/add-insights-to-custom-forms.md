---
title: Add (customized) contact or lead insights to custom forms
description: Learn how to add customized contact or lead insights to custom forms Dynamics 365 Customer Insights - Journeys.
ms.date: 10/07/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Add (customized) contact or lead insights to custom forms

> [!NOTE]
> If you’re not familiar with editing forms using the form designer, follow the instructions here: [Create, edit, or configure forms using the form designer](/power-apps/maker/model-driven-apps/create-and-edit-forms)

To add the **Insights** tab to custom forms:

1. Open the form editor where you want to have the control placed.
1. Add a new tab to that form.
1. Make sure to check the "Expand first component to full tab" checkbox.
    
    :::image type="content" source="media/add-insights-expand-tab.png" alt-text="Screenshot showing Expand first component to full tab checkbox.":::
1. Select the **Components** section on the left side then select **Get more components**.
    
    :::image type="content" source="media/add-insights-get-more-components.png" alt-text="Screenshot showing Get more components link.":::

1. In the side panel that opens, search for "InsightsControl."
    
    :::image type="content" source="media/add-insights-insights-control.png" alt-text="Screenshot showing InsightsControl component.":::

1. Select the “InsightsControl” component then select **Add**.
1. The control now appears under the **More components** section. You can now add the control to the form.
1. Fill out the **Custom configuration** property. This is the web resource name (including extension) that's loaded to display the widgets. The “CC_filter” property shouldn't be used. Here are the default insights configurations:
    - **Contact**: ContactInsights.msdynmkt_InsightsConfig.json
    - **Lead**: LeadInsights.msdynmkt_InsightsConfig.json
    
    :::image type="content" source="media/add-insights-static-value.png" alt-text="Screenshot showing the Static value field.":::

1. Save changes and publish all customizations.

## Customize the layout

> [!NOTE]
> - The preferred way to customize the layout is to clone an existing configuration and customize the JSON according to user needs.
> - Using widgets not listed in "Available widgets" for a given entity results in unpredictable errors.
> - For more information about web resources, see [Create or edit model-driven app web resources to extend an app](/power-apps/maker/model-driven-apps/create-edit-web-resources)

Insights configuration is a JSON file specifying a layout of widgets on a page. It's meant to be used as a full-page control in a form.

To create a JSON file with layout definition:

1. Use one of the existing configurations as the base by querying its **web resource**. Consult the appropriate section to find out about the available web resources. After downloading the web resource, you can make the modifications. *Don't modify* properties other than the ones specified below:
    - **layout** > **gridConfiguration** > **responsiveBreakpoints**: These values specify the name and breakpoint at which the grid placement override is applied.
    - **pages**: This specifies the pages available for navigation. The first page is always the first, main visible page. Other pages can be navigated to by using InsightsNavigationControl.
    - **compoundWidgets**: The definition of content for each separate card on the layout. Consult the layout JSON description section for more detailed information.
1. After making changes, save the file on your local drive with a ".js" extension.
1. In the admin portal (**Settings** ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") > **Advanced settings**), go to **Solutions** and select the solution that the web resource should belong to.
    
    :::image type="content" source="media/add-insights-admin-portal.png" alt-text="Screenshot showing the admin portal.":::

1. Upload the file. In the custom control configuration, make sure to use the value of the “Name” field (including the solution prefix).

[!INCLUDE [footer-include](./includes/footer-banner.md)]