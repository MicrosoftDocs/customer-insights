---
title: Overriding FLS Attributes in Dynamics Customer Insights
description: Learn how to override FLS attributes in Dynamics Customer Insights - Journeys.
ms.date: 06/02/2024
ms.topic: article
author: cbirkett
ms.author: cbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# How FLS attributes are handled in Dynamics 365 Customer Insights – Journeys

This is a  guide for customers who want to understand the impact of FLS-protected attributes in personalization, journey branching, and real-time segmentation.

## What is FLS and how does it affect Customer Insights - Journeys?

Field Level Security (FLS) is a backend feature that allows you to restrict access to certain fields on dataverse entities, such as contact, account, or lead. For example, you can use FLS to protect sensitive information like your Social Security number or salary from unauthorized users. FLS is configured by creating field security profiles and adding users or teams to them.

By default, Customer Insights - Journeys prevents you from using FLS-protected attributes in the following scenarios:

- Content personalization—You can't define dynamic text that uses FLS-protected attributes.
- Journey personalization/branching—You can't use FLS-protected attributes in conditions for journey branching or personalization.
- Real-time segmentation—You can't use FLS-protected attributes in filters or expressions for real-time segments.

With Customer Insights – Journeys, using [Dataverse table data](/power-apps/maker/data-platform/entity-overview) you can create and send personalized messages to your customers and branch journeys to automate sending personalized messages to large real-time audience segments. However, this action also increases the risk of exposing sensitive data if everyone in your team can access and use FLS-protected fields in the messages. By default, Customer Insights – Journeys doesn't let everyone use FLS-protected fields in the messages to prevent privacy issues.

## What are the prerequisites of overriding FLS?

Some customers might want to override the FLS limitation in CI-J and use FLS-protected attributes in personalization, journey branching, or real-time segmentation. This is possible with additional steps and considerations.

Before you request to override FLS, you need to do the following:

- Add all CI-J application/system users to the respective FLS profiles, so that these users have access to the FLS-protected attributes. You can find the names of the CI-J application users in [Manage user accounts, user licenses, and security roles](/ci-docs/journeys/admin-users-licenses-roles.md#form-and-field-level-security).
- Understand and accept the change to your security model and sign off on it. After you add the Customer Insights – Journeys application users to the FLS profiles, all Dynamics 365 users who can publish journeys are able to access the FLS-protected attributes even if users aren't in the FLS profiles themselves. Customer Insights – Journeys doesn't impersonate the user who publishes the journey. Instead, Customer Insights – Journeys uses the application user.  

If you don't follow these steps, you might encounter serious issues, such as:

- Journeys/personalization not working, empty emails being sent, branching behaving wrongly, and journeys crashing completely.
- You might violate your data privacy and compliance policies by exposing FLS-protected data to unauthorized users.

## How to override FLS?

If you have completed the prerequisites and accepted the risks of overriding FLS, you can request to enable the FLS-protected attributes in Customer Insights – Journeys. It can be enabled for your organization by the support team.

To request to enable the FLS-protected attributes, you need to contact the support team and provide the following information:

- Your org name.
- A confirmation that you have added all Customer Insights – Journeys application/system users to the FLS profiles.
- A confirmation that you understand and accept the change to your security model and the potential risks of overriding FLS.

You're notified when the FLS is enabled and you can start using FLS-protected attributes in Customer Insights – Journeys.

For more information, see [submit a support request](/dynamics365/field-service/field-service-get-help).

## More information

- [Form and field level security](/ci-docs/journeys/admin-users-licenses-roles.md#dont-modify-or-remove-marketing-service-users#form-and-field-level-security)
- [Don't modify or remove marketing service users](/ci-docs/journeys/admin-users-licenses-roles.md#dont-modify-or-remove-marketing-service-users).
