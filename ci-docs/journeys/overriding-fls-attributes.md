---
title: Override field-level security attributes
description: Learn how to override field-level security attributes in Dynamics 365 Customer Insights - Journeys.
ms.date: 07/30/2025
ms.topic: how-to
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Override field-level security attributes

This article provides details about the impact of field-level security (FLS)-protected attributes in personalization, journey branching, real-time segmentation, and how to override FLS attributes.

FLS is a platform feature that allows you to restrict access to certain fields on Dataverse entities such as contact, account, or lead. For example, you can use FLS to protect sensitive information from unauthorized users, such as Social Security number or salary. FLS is configured by creating field security profiles and adding users or teams to them.

By default, Customer Insights - Journeys prevents you from using FLS-protected attributes in the following scenarios:

- Content personalization: You can't define dynamic text or conditions that use FLS-protected attributes.
- Journey personalization/branching: You can't use FLS-protected attributes in conditions for journey branching or personalization.
- Real-time segmentation: You can't use FLS-protected attributes in filters or expressions for real-time segments.

Using [Dataverse table data](/power-apps/maker/data-platform/entity-overview) with Customer Insights – Journeys, you can create and send personalized messages to your customers and branch journeys to automate sending personalized messages to large real-time audience segments. However, this also increases the risk of exposing sensitive data if everyone in your team can access and use FLS-protected fields in the messages. By default, to prevent privacy issues, Customer Insights – Journeys doesn't let everyone use FLS-protected fields in the messages.

## Prerequisites for overriding FLS

You can override the FLS limitation and use FLS-protected attributes in personalization, journey branching, or real-time segmentation using feature switches in the **Settings** > **Feature switches** area. However, before changing the feature switches, you must carefully consider security and privacy issues and obtain the appropriate approvals. Before overriding FLS:

1. Identify all application and system users who need access to FLS-protected attributes and add them to the respective FLS profiles. To learn about the details of security roles, see [Manage user accounts, user licenses, and security roles](admin-users-licenses-roles.md#form-and-field-level-security).

1. Next, add the various service users mentioned in [Customer Insights - Journeys service users](admin-users-licenses-roles.md#form-and-field-level-security) to the respective FLS profiles.
  > [!IMPORTANT]
  > If you miss this step, FLS-protected fields are rendered as “null” during internal system evaluations, leading to errors that are difficult to diagnose.
  
1. Ensure that journey publishing is allowed *only* for FLS-enabled users. This step prevents accidental exposure of sensitive information by unauthorized users.

1. Review the details of how FLS works and the changes you have made or plan to make with the personnel tasked with ensuring security and privacy in your company. Get their sign-off on the following statement:

    *After the FLS override is in place, all journeys will be able to access the FLS-protected attributes even if they're published by users who aren't in the FLS profiles themselves. This is because Customer Insights - Journeys runs in the application user context and not in the context of the publishing user.*

If you don't follow these steps, you may encounter serious issues, such as:

- Journeys or personalization not working as expected. For example, empty emails may be sent, branching may behave wrongly, or Customer Insights - Journeys may crash.
- You may violate your data privacy and compliance policies by exposing FLS-protected data to unauthorized users.

## Set the feature switches to override FLS

If you complete the prerequisites and accept the risks of overriding FLS, you can enable the following feature switches on the **Settings** > **Feature switches** page: 
- To override FLS in journeys and personalization, enable the “Use protected fields in personalization” feature switch in the “Personalization” group. You are asked to acknowledge the risks, and your user ID is recorded (and displayed) for audit purposes.
- To override FLS in segmentation, enable the "Use protected fields in segments" feature switch in the "Segmentation" group. Learn more: [Add protected fields in segment criteria](protected-fields.md).

## More information

- [Form and field level security](admin-users-licenses-roles.md#form-and-field-level-security)
- [Don't modify or remove marketing service users](admin-users-licenses-roles.md#dont-modify-or-remove-service-users).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
