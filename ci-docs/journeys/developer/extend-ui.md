---
title: Customize the Customer Insights - Journeys forms interface
description: Customize Customer Insights - Journeys forms with a managed solution layer to receive automatic updates, or fork a copy for full control and manual maintenance.
ms.date: 07/10/2026
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
---

# Customize the Customer Insights - Journeys forms interface

Customer Insights - Journeys forms are Dataverse forms, so you can customize them the same way you customize any Dataverse form. When you customize Customer Insights - Journeys forms or any other Dataverse forms, you can choose between extending the form (adding a layer on top of it) or copying (forking) the form. Each approach has its own pros and cons, described in the following sections.

## Create a layer using a managed solution on top of an existing form

The benefit of creating a layer on top of an existing form is that you receive all new updates as they're shipped, at the risk that the form might change in a way you don't want.

:::image type="content" source="../media/extend-journeys-forms.png" alt-text="Screenshot of adding an existing form as a managed solution layer in Dataverse.":::

## Create a copy (fork) of a form

> [!NOTE]
> Dynamics 365 Customer Insights - Journeys is still a relatively young product compared to core Dataverse forms such as contact, lead, and account. As such, changes are frequent and it might be hard to keep up.

The benefit of a copy of the form is that it never changes without your knowledge, but it can also break without your knowledge. To keep your forked form working, monitor the out-of-the-box form for changes and update your forked form to account for those changes.

Imagine a scenario where a new mandatory field is added to the out-of-the-box form that the backend validates. In the forked form scenario, such an upgrade breaks your form.

Be mindful of form dependencies. When you fork a form without forking its dependencies (typically web resources handling onload, onsave, or onchange events), you risk the dependencies evolving in a way that breaks your forked form.

## More information

- [Create, design, and edit forms](/dynamics365/customerengagement/on-premises/customize/create-design-forms)
- [Overview of working with solutions](/dynamics365/customerengagement/on-premises/customize/solutions-overview)