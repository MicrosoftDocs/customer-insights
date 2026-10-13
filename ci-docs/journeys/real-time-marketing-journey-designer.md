---
title: Customize the journey designer in Customer Insights - Journeys
description: Learn how to customize the journey designer in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/13/2026
ms.topic: get-started
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customize the journey designer in Customer Insights - Journeys

> [!IMPORTANT]
> To build an approval process in real-time journeys, see [Journey and email approval process in Customer Insights - Journeys](https://community.dynamics.com/blogs/post/?postid=e2f9169d-eef7-ee11-a73d-000d3ae2664e)

Customization of your customer journeys is now available in Dynamics 365 Customer Insights - Journeys. Not only can you use out-of-the-box Customer Insights - Journeys capabilities to engage customers, but you can also now create personalized, flexible, and efficient solutions through Power Apps to better tailor Customer Insights - Journeys to meet your specific business needs.

For example, you can extend the journey canvas, adding custom fields through Dataverse to streamline your business processes for higher efficiency. For example, you could add a custom "Campaign" field to your journeys to better manage your assets, collaborate with your team members, and give you more flexibility to create customized analytics reports.

Here's how you can achieve the above scenario by adding a campaign field in the new journey designer in Customer Insights - Journeys:

1. Go to [Power Apps](https://make.powerapps.com/) for the Customer Journeys - Insights environment and find the **Journey** table under **Dataverse** > **Tables**.

    :::image type="content" source="media/real-time-marketing-dataverse-tables.png" alt-text="dataverse tables":::

1. To access the new journey designer form, go to **Data experiences** > **Forms**.

    :::image type="content" source="media/real-time-marketing-data-experiences-forms.png" alt-text="data experiences forms":::

1. Choose **Main** under **Form type** to get started.

    :::image type="content" source="media/real-time-marketing-form-type.png" alt-text="form type":::

1. You should see a form designer that looks like the new journey creation experience under the **Design** tab. Navigate to the **Settings** tab in the new journey form.

    :::image type="content" source="media/real-time-marketing-new-journey-form.png" alt-text="new journey form":::

    > [!IMPORTANT]
    > The **Settings** tab may be hidden by default. To view hidden elements, enable the **Show hidden** switch at the bottom of the form designer.

1. Add the fields you want to show on the journey designer on the **Settings** tab. You can add sections to organize your fields. In this example, a section labeled *Campaign* is added to the form with a custom *Campaign* field.

    :::image type="content" source="media/real-time-marketing-new-journey-campaign.png" alt-text="new journey campaign":::

    > [!CAUTION]
    > Only sections and fields under **Settings** will show up in the **Other Settings** side pane in the journey designer. Other tabs added in the form designer aren't rendered in the journey designer.

1. The fields added on the **Settings** tab are visible in the **Other Settings** pane in the journey designer.

    :::image type="content" source="media/real-time-marketing-new-journey-campaign-custom-settings.png" alt-text="other settings journey designer":::
