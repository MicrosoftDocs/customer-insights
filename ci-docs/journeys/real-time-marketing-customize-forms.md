---
title: Customize Customer Insights - Journeys forms
description: Learn how to customize form entity in Dynamics 365 Customer Insights - Journeys.
ms.date: 1/4/2024
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customize the form editor

The latest [form editor](../real-time-marketing-form-overview.md) simplifies the design process of a form or a simple landing page by providing more screen real estate for the design canvas. You can further tailor the form editor to suit your needs by implementing your own customizations.

The list of customizable form entities:

- Form (msdynmkt_marketingform)
- Form Submission (msdynmkt_marketingformsubmission)

Customizations made to the main form or customizations adding new fields to the Form Settings form *do not* require any action.

For example, you can extend the form editor, adding custom fields through Dataverse to streamline your business processes for higher efficiency. This allows you to add custom fields such as "Campaign" to your forms.

## Customizing form editor

Let's add "Campaign" field to your forms in this step-by-step guide.

