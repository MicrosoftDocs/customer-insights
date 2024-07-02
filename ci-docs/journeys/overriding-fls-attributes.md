---
title: Override FLS attributes in Dynamics 365 Customer Insights
description: Learn how to override FLS attributes in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/02/2024
ms.topic: article
author: cbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Override FLS attributes in Dynamics 365 Customer Insights

This article provides details about the impact of Field Level Security (FLS)-protected attributes in personalization, journey branching, and real-time segmentation, and how to override the FLS attributes.

FLS is a backend feature that allows you to restrict access to certain fields on dataverse entities such as contact, account, or lead. For example, you can use FLS to protect sensitive information from unauthorized users, like your Social Security number or salary. FLS is configured by creating field security profiles and adding users or teams to them.

By default, Customer Insights - Journeys prevents you from using FLS-protected attributes in the following scenarios:

- Content personalization: You can't define dynamic text that uses FLS-protected attributes.
- Journey personalization/branching: You can't use FLS-protected attributes in conditions for journey branching or personalization.
- Real-time segmentation: You can't use FLS-protected attributes in filters or expressions for real-time segments.

Using [Dataverse table data](/power-apps/maker/data-platform/entity-overview) with Customer Insights – Journeys, you can create and send personalized messages to your customers and branch journeys to automate sending personalized messages to large real-time audience segments. However, doing so also increases the risk of exposing sensitive data if everyone in your team can access and use FLS-protected fields in the messages. By default, Customer Insights – Journeys doesn't let everyone use FLS-protected fields in the messages in order to prevent privacy issues.

## Prerequisites to override FLS

You can override the FLS limitation and use FLS-protected attributes in personalization, journey branching, or real-time segmentation by completing the following instructions.

Before you request to override FLS, complete these steps:

1. Add all Customer Insights – Journeys application/system users to the respective FLS profiles, so that these users have access to the FLS-protected attributes. To find the names of the application users, refer to [Manage user accounts, user licenses, and security roles](admin-users-licenses-roles.md#form-and-field-level-security).
1. Understand the change to your security model and sign off on it. After you add the Customer Insights – Journeys application users to the FLS profiles, all Dynamics 365 users who can publish journeys are able to access the FLS-protected attributes, even if users aren't in the FLS profiles. Customer Insights – Journeys doesn't impersonate the user who publishes the journey. Instead, Customer Insights – Journeys uses the application user.  

If you don't follow these steps, you may encounter serious issues, such as:

- Journeys/personalization not working, empty emails being sent, branching behaving wrongly, and journeys crashing.
- You may violate your data privacy and compliance policies by exposing FLS-protected data to unauthorized users.

## Override FLS

If you complete the prerequisites and accept the risks of overriding FLS, you can request to enable the FLS-protected attributes in Customer Insights – Journeys. To enable the attributes for your organization, contact your support team.

To request to enable the FLS-protected attributes, contact the support team and provide the following information:

- Your org name.
- Confirmation that you added all Customer Insights – Journeys application/system users to the FLS profiles.
- Confirmation that you understand and accept the change to your security model and the potential risks of overriding FLS.

Once you've been notified that the FLS is enabled, you can start using FLS-protected attributes in Customer Insights – Journeys.

For more information, see [Submit a support request](/dynamics365/field-service/field-service-get-help).

## More information

- [Form and field level security](admin-users-licenses-roles.md#form-and-field-level-security)
- [Don't modify or remove marketing service users](admin-users-licenses-roles.md#dont-modify-or-remove-service-users).
