---
title: Override FLS attributes in Dynamics 365 Customer Insights
description: Learn how to override FLS attributes in Dynamics 365 Customer Insights - Journeys.
ms.date: 07/10/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Override FLS attributes in Dynamics 365 Customer Insights - Journeys

This article provides details about the impact of Field Level Security (FLS)-protected attributes in personalization, journey branching, real-time segmentation, and how to override FLS attributes.

FLS is a platform feature that allows you to restrict access to certain fields on dataverse entities such as contact, account, or lead. For example, you can use FLS to protect sensitive information from unauthorized users, such as Social Security number or salary. FLS is configured by creating field security profiles and adding users or teams to them.

By default, Customer Insights - Journeys prevents you from using FLS-protected attributes in the following scenarios:

- Content personalization: You can't define dynamic text or conditions that use FLS-protected attributes.
- Journey personalization/branching: You can't use FLS-protected attributes in conditions for journey branching or personalization.
- Real-time segmentation: You can't use FLS-protected attributes in filters or expressions for real-time segments.

Using [dataverse table data](/power-apps/maker/data-platform/entity-overview) with Customer Insights – Journeys, you can create and send personalized messages to your customers and branch journeys to automate sending personalized messages to large real-time audience segments. However, this also increases the risk of exposing sensitive data if everyone in your team can access and use FLS-protected fields in the messages. By default, Customer Insights – Journeys doesn't let everyone use FLS-protected fields in the messages in order to prevent privacy issues.

## Prerequisites to override FLS

You can override the FLS limitation and use FLS-protected attributes in personalization, journey branching, or real-time segmentation. This override is enabled by the product team.

Before you request to override FLS, complete these steps:

1. Identify all application/system users who should have access to FLS-protected attributes and add them to the respective FLS profiles. To find the details of security roles, refer to [manage user accounts, user licenses, and security roles](admin-users-licenses-roles.md#form-and-field-level-security).

1. Ensure that journey publishing is allowed only for FLS-enabled users. This step prevents accidental exposure of sensitive information by unauthorized users.

1. Review the details of how FLS works with the personnel tasked with ensuring security and privacy in your company. Sign off on the following information:

    *After the FLS override is in place, all journeys will be able to access the FLS-protected attributes even if they're published by users who aren't in the FLS profiles themselves. This is because Journeys runs in the application user context and not in the context of the publishing user.*

If you don't follow these steps, you may encounter serious issues, such as:

- Journeys/personalization won't work as expected. For example, empty emails may be sent, branching may behave wrongly, or Journeys crashing potentially.
- You may violate your data privacy and compliance policies by exposing FLS-protected data to unauthorized users.

## Override FLS

If you complete the prerequisites and accept the risks of overriding FLS, you can request to enable the FLS-protected attributes in Customer Insights – Journeys. To enable FLS-protected attributes, [contact the support team](/power-platform/admin/get-help-support#view-solutions-or-create-a-support-request) and provide the following information:

- Your org name and ID. For more information, see [find your organization ID and name](/power-platform/admin/get-help-support#view-solutions-or-create-a-support-request).
- Confirmation that you added all Customer Insights – Journeys application and system users to the FLS profiles.
- Confirmation of the following statement:  
    *Please enable FLS-Override for the above org(s). We have completed all prerequisite steps and required security/privacy reviews. Our company understands and accepts the risks associated with this change to our security model.*

Once you're notified that FLS is enabled, you can start using FLS-protected attributes in Customer Insights – Journeys.

For more information, see [submit a support request](/dynamics365/field-service/field-service-get-help).

## More information

- [Form and field level security](admin-users-licenses-roles.md#form-and-field-level-security)
- [Don't modify or remove marketing service users](admin-users-licenses-roles.md#dont-modify-or-remove-service-users).
