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

When customizing Customer Insights - Journeys forms or any Dataverse forms, you can choose between extending the form or copying form. There are pros and cons with both approaches.

## Creating a layer using a managed solution on top of an existing form

The benefit of creating layer on top of existing form is you'll get all new updates as they're shipped, at the risk of form changing in a manner that is not desirable for you.

:::image type="content" source="media/extend-journeys-forms.png" alt-text="Add existing form.":::

## Forking forms

> [!NOTE]
> Dynamics 365 Customer Insights - Journeys is still relatively young product compared to core dataverse forms - say like contact / lead / account / etc. - so changes are frequent and it might be hard to keep up. 

The benefit of a copy of the form is that it will never change without your knowledge - but it can break without your knowledge. You'll need to constantly monitor for changes in the out of box form and continuously update your form with those newer changes.
Imagine scenario like adding new mandatory field to the out-of-box form that is validated by backend - in forked form scenario such marketing upgrade will break your form.
Be mindful about form dependencies - when you fork a form without forking its depednencies (typically web resources handling onload / onsave / onchange events) you're in a risk that those will evolve in a manner that will break your forked form.

## More informations 

- [Creating and design dataverse froms](/dynamics365/customerengagement/on-premises/customize/create-design-forms)
- [Working with solutions](/dynamics365/customerengagement/on-premises/customize/solutions-overview)


