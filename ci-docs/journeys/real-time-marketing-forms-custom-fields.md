---
title: "Preview: Create custom fields for marketing and event registration forms"
description: Custom mapped and unmapped fields for forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/03/2024
ms.topic: article
author: petrjantac
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Create custom fields for marketing and event registration forms

> [!IMPORTANT]
> A preview feature is a feature that is not complete but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

Custom unmapped fields allow you to easily gather additional information about your customers by creating any kind of question directly in the form editor without the need to create new custom attributes for your lead or contact entity. For example, you can create fields to ask, “What is your meal preference?” or create contest questions to increase your customer satisfaction and retention.

## Difference between mapped and unmapped fields

There are two general types of fields: mapped and unmapped. If you want to store the submitted value on Contact or Lead, use the mapped fields. If you don't want the submitted value to be stored on Contact or Lead, use the unmapped fields.

- **Mapped fields** are linked to an existing attribute of an entity. For example, the First Name field is linked to the firstname attribute of the Contact entity. When the form is submitted, the mapped fields update the corresponding Lead or Contact attribute. All contact and lead attributes (except some protected system fields) are available as fields in the form editor. If you create a new custom attribute of Lead or Contact, it is automatically available as a field in the form editor.
- **Unmapped fields** are not mapped to any attribute of any entity. These fields are typically used for one-off questions. Unmapped fields values are not stored in Contact or Lead entities. The submitted values are stored in the Form submission entity.