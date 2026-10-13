---
title: Add a contactability grid control to custom forms
description: Learn how to add contactability grid control to custom forms.
ms.date: 10/13/2026
ms.topic: how-to
author: udag
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Add a contactability grid control to custom forms

This article explains how to add a contactability consent control to custom forms. Learn more: [View and manage consent records](real-time-marketing-email-text-consent.md#view-and-manage-consent-records).

1. Go to the [maker portal](https://make.powerapps.com/).
1. From the **Tables** menu, select the **Contact** or **Lead** table depending on which custom form you want to add the contactability grid control to.
1. Go to the **Forms** for the table and select the form where you want to add the control.
    > [!NOTE]
    > You may not have forms defined as a customization, but instead in your own solution. In that case, instead of selecting the **Tables** menu in step two, you should select the **Solutions** menu and then select your solution that contains the form.
1. From the list of components, add a new **1-column tab** to the layout of the form.
    :::image type="content" source="media/add-1-column-tab.png" alt-text="For the layout, add a section of one column tab":::
1. Select the **Expand this tab by default** and **Expand first component to full tab** options for this tab and name the tab "Communication."
    :::image type="content" source="media/expand-column-tab-to-full-display.png" alt-text="Expand column tab to full display":::
1. Add a **1-column section** component on this tab.
    :::image type="content" source="media/add-1-column-section.png" alt-text="Add a section of one column":::
1. Once added, expand the **More Components** section, and add the **ContactabilityGrid** control onto the new section.
    :::image type="content" source="media/select-contactability-grid.png" alt-text="Select the contactability grid by expanding the section":::
1. Once complete, the contactability consent control looks like this:
    :::image type="content" source="media/add-your-contact-points.png" alt-text="You can add your contact points":::
