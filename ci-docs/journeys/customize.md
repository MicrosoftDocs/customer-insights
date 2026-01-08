---
title: Customize Dynamics 365 Customer Insights - Journeys
description: How to customize lists, forms, workflows, business processes, validations, and more in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/07/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customize Dynamics 365 Customer Insights - Journeys

This article explains how to customize lists, forms, workflows, business processes, validations, and more in Customer Insights - Journeys.

## Basic customizations

Model-driven apps in Dynamics 365 (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Customer Insights - Journeys, and Dynamics 365 Project Service Automation) provide rich possibilities for customization without coding. Customizers can add new fields to existing entities, add or hide fields in list or form views, design custom business processes and workflows, and much more—all while working in their web browser. Other types of customization include installing custom solutions from Microsoft Marketplace, such as a third-party text messaging solution for Customer Insights - Journeys. The system also provides APIs that enable developers to write code that implements even more advanced custom functionality and third-party integration.

> [!WARNING]
> Do not include sensitive information in your customized schema and display names. Schema and display names for fields, entities, relations, attributes, and other elements are displayed in various interfaces throughout the Customer Insights - Journeys application. They may also be referenced by other object definitions and get shared through various other channels. They may also appear in telemetry.

The techniques for customizing Dynamics 365 Customer Insights - Journeys are the same as those for customizing other model-driven apps in Dynamics 365. For complete details about how to customize model-driven apps in Dynamics 365, see the [Power Apps documentation](/powerapps/?panel=getstarted#pivot=home).

For details about customizations that apply only to the Customer Insights - Journeys app (but not other Dynamics 365 apps), see the following topics:

- [Create and customize marketing calendars](customize-marketing-calendars.md)
- [Create and customize template labels](customize-template-labels.md)

## Don't remove status-reason values used by go-live functionality

Entities that include [go-live functionality](go-live.md) provide a **Status reason** field that tracks the go-live status of each record. The field is an option set that must include the following values: **Draft**, **Live**, **Stopped**, "**Live, editable**", **Error**, **Going live**, and "**Stopping...**". Be sure not to delete any of these standard values. If you do, the entity will no longer be able to go live.

## Create a custom app that includes Customer Insights - Journeys solutions

> [!WARNING]
> To use entities, tables, operations, or components associated with a specific app like Sales or Service, you must be licensed for those apps. The license requirement applies regardless of whether you create a custom app to access the data.

Customizers and developers can create custom app modules that include any number of existing solutions, plus other custom elements, as needed. You can include 
Dynamics 365 Customer Insights - Journeys solutions in custom apps such as these, but the *Marketing email test send* entity won't be included automatically when you add the Marketing solution. As a result, your custom app won't support test sends of marketing emails by default. If you'd like to include this feature in your custom app, then you must add the *Marketing email test send* entity manually to your app after you add the Marketing solution.

More information: [Design model-driven apps by using the app designer](/powerapps/maker/model-driven-apps/design-custom-business-apps-using-app-designer)

## Advanced customization through coding

Advanced customization and integration with external systems is possible through code-based interactions with the system's various APIs. For details about writing code and developing for Dynamics 365 Customer Insights - Journeys and other model-driven apps in Dynamics 365, see the [developer documentation for Power Apps](/powerapps/?panel=developer#pivot=home).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
