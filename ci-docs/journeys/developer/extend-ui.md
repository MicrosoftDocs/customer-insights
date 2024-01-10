---
title: Customize the Customer Insights - Journeys forms interface
description: Learn how to extend the Customer Insights - Journeys user interface to customize forms.
ms.date: 01/10/2023
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
---

# Customize the Customer Insights - Journeys forms interface

When customizing Customer Insights - Journeys forms or any Dataverse forms, you can choose between extending the form or copying (forking) the form. As discussed below, there are pros and cons to both approaches.

## Create a layer using a managed solution on top of an existing form

The benefit of creating a layer on top of an existing form is that you receive all new updates as they're shipped, at the risk of the form changing in a manner that's not desirable for you.

:::image type="content" source="../media/extend-journeys-forms.png" alt-text="Add existing form.":::

## Forking forms

> [!NOTE]
> Dynamics 365 Customer Insights - Journeys is still a relatively young product compared to the core Dataverse forms like contact, lead, account, etc. As such, changes are frequent and it might be hard to keep up.

The benefit of a copy of the form is that it never changes without your knowledge, but it can break without your knowledge. You need to constantly monitor for changes in the out-of-the-box form and continuously update your form to account for the newer changes.

Imagine a scenario where a new mandatory field is added to the out-of-box form that the backend validates. In the forked form scenario, such a marketing upgrade breaks your form.

Be mindful of form dependencies. When you fork a form without forking its dependencies (typically web resources handling onload, onsave, or onchange events), you're at risk that the dependencies will evolve in a manner that break your forked form.

## More information

- [Create, design, and edit forms](/dynamics365/customerengagement/on-premises/customize/create-design-forms)
- [Overview of working with solutions](/dynamics365/customerengagement/on-premises/customize/solutions-overview)