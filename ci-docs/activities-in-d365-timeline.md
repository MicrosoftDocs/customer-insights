---
title: "Display Customer Insights activities in Dynamics 365 timelines"
description: "Set up Customer Insights so that activities can be displayed on other Dynamics 365 apps." 
ms.date: 06/15/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: andtapia
ms.author:  andreatapia
ms.custom: bap-template
---

# Display Customer Insights activities in Dynamics 365 timelines

If you use Customer Insights and a supported Dynamics 365 app such as Dynamics 365 Sales, Marketing, and Customer Service, activity data from Customer Insights can display in a shared activity timeline for a given customer or account.

Once enabled by a Dynamics 365 administrator, sellers and representatives can view activities such as notes, posts, emails, and appointments as well as transactional and behavior data for a customer.

Customer Insights activities within the Dynamics 365 activity timeline can be filtered, searched, and updated dynamically.

## Prerequisites

- Customer Insights and the other Dynamics 365 apps operate on the same [Dataverse organization](customer-insights-dataverse.md).
- Account or contact data are ingested into Customer Insights through a [Microsoft Dataverse managed data lake](connect-dataverse-managed-lake.md). The data is then [unified](data-unification.md).
- [Account or contact activities are defined](activities.md).
- The Dynamics 365 Customer Insights Timeline Integration (*msdyn_CustomerInsightsTimelineIntegration*) solution is installed on the Power Apps environment.

## Enable the Dynamics 365 Customer Insights Timeline Integration

The setting Enable Customer Insights Timeline Integration (*msdyn_IsTimelineIntegrationEnabled*) is enabled through Power Apps. For more information, see [Adding an existing setting definition](/power-apps/maker/data-platform/create-edit-configure-settings#adding-an-existing-setting-definition).

The Customers Insights Timeline Connector (*msdyn_CustomerInsightsTimelineConnector*) is automatically attached to the Dynamics Timeline control on the main Contact and Account form. To attach the connector to the Dynamics Timeline control on any other Account or Contact form, see [Configure the custom connector for the timeline control](/power-apps/maker/model-driven-apps/custom-connectors-timeline-control#configure-the-custom-connector-for-the-timeline-control).