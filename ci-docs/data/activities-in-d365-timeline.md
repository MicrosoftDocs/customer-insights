---
title: "Show activities with Dynamics 365 timelines"
description: "Set up Customer Insights so that activities can be displayed on other Dynamics 365 apps." 
ms.date: 09/01/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: andtapia
ms.author:  andreatapia
ms.custom: bap-template
---

# Show activities with Dynamics 365 timelines

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

If you use Dynamics 365 Customer Insights - Data and other Dynamics 365 apps such as Dynamics 365 Sales, Customer Insights - Journeys, or Customer Service, you can integrate activities so that they display on Dynamics 365 activity timelines.

Once enabled by a Dynamics 365 administrator, sellers and representatives can view activities such as notes, posts, emails, and appointments as well as transactional and behavioral data for a customer. They can search and filter activity records within the shared timeline.

## Prerequisites

- Customer Insights - Data and your other Dynamics 365 apps operate on the same Dataverse environment.
- The Dynamics 365 Customer Insights - Data Timeline Integration (*msdyn_CustomerInsightsTimelineIntegration*) solution is installed on the Power Apps environment. It's included with version 1.0.3.38 of the Dynamics 365 Customer Insights - Data Base (*msdyn_CustomerInsightsAnchor*) solution. To check your version, go to Power Apps and select **Solutions**. For more information, see [Work with solutions](/power-apps/maker/data-platform/solutions-overview#search-and-filter-in-a-solution).
- Contact or account data is imported through a [Microsoft Dataverse managed data lake](connect-dataverse.md). The data is then [unified](data-unification.md).
- [Customer activities are defined](activities.md). These activities are stored in Dataverse in the *UnifiedActivity* table.

## Enable the Dynamics 365 Customer Insights - Data Timeline Integration

1. Go to [Power Apps](https://powerapps.microsoft.com/).

1. Enable the setting **Enable Customer Insights Timeline Integration** (*msdyn_IsTimelineIntegrationEnabled*). For more information, see [Adding an existing setting definition](/power-apps/maker/data-platform/create-edit-configure-settings#adding-an-existing-setting-definition).

1. Attach the **Customer Insights - Data Timeline Connector** (*msdyn_CustomerInsightsTimelineConnector*) to the Dynamics Timeline control on Account or Contact forms. For more information, see [Configure the custom connector for the timeline control](/power-apps/maker/model-driven-apps/custom-connectors-timeline-control#configure-the-custom-connector-for-the-timeline-control).

   > [!TIP]
   > By default, the connector is automatically attached to the Dynamics Timeline control on the main Contact and main Account forms.

[!INCLUDE [footer-include](includes/footer-banner.md)]
