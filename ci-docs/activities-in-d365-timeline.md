---
title: "Integrate Customer Insights activities with Dynamics 365 timelines"
description: "Set up Customer Insights so that activities can be displayed on other Dynamics 365 apps." 
ms.date: 06/15/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: andtapia
ms.author:  andreatapia
ms.custom: bap-template
---

# Integrate Customer Insights activities with Dynamics 365 timelines

If you use Customer Insights and another Dynamics 365 app such as Dynamics 365 Sales, Marketing, or Customer Service, you can integrate Customer Insights activity so that they display on Dynamics 365 activity timelines.

Once enabled by a Dynamics 365 administrator, sellers and representatives can view activities such as notes, posts, emails, and appointments as well as transactional and behavior data for a customer.

## Prerequisites

- Customer Insights and other Dynamics 365 apps operate on the same [Dataverse organization](customer-insights-dataverse.md).
- The Dynamics 365 Customer Insights Timeline Integration (*msdyn_CustomerInsightsTimelineIntegration*) solution is installed on the Power Apps environment. It is included with version 1.0.3.38 of the Dynamics 365 Customer Insights Base (*msdyn_CustomerInsightsAnchor*) solution. To check your version, go to Power Apps and select **Solutions**. For more information, see [Work with solutions](/power-apps/maker/data-platform/solutions-overview#search-and-filter-in-a-solution).
- Customer data is ingested into Customer Insights through a [Microsoft Dataverse managed data lake](connect-dataverse-managed-lake.md). The data is then [unified](data-unification.md).
- [Customer activities are defined](activities.md).
- An Admin role in Dynamics 365.

## Enable the Dynamics 365 Customer Insights Timeline Integration

1. Go to [Power Apps](https://powerapps.microsoft.com/).

1. Enable the setting **Enable Customer Insights Timeline Integration** (*msdyn_IsTimelineIntegrationEnabled*). For more information, see [Adding an existing setting definition](/power-apps/maker/data-platform/create-edit-configure-settings#adding-an-existing-setting-definition).

1. Attach the **Customers Insights Timeline Connector** (*msdyn_CustomerInsightsTimelineConnector*) to the Dynamics Timeline control on Account or Contact forms. For more information, see [Configure the custom connector for the timeline control](/power-apps/maker/model-driven-apps/custom-connectors-timeline-control#configure-the-custom-connector-for-the-timeline-control).

   > [!TIP]
   > By default, the connector is automatically attached to the Dynamics Timeline control on the main Contact and main Account forms.

[!INCLUDE [footer-include](includes/footer-banner.md)]
