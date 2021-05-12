---
title: "New and upcoming features"
description: "Information about new features, improvements, and bug fixes."
ms.date: 05/06/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: midevane
manager: shellyha
---

# What's new in the audience insights capability of Dynamics 365 Customer Insights

[!INCLUDE [cc-data-platform-banner](../includes/cc-data-platform-banner.md)]

We're excited to announce our newest updates! This article summarizes public preview features, general availability enhancements, and feature updates. To see the long-term feature plans, take a look at the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

We roll out updates on a region-by-region basis. So certain regions might see features before others. Unless specified differently, you don't need to take any action and we'll update the app automatically with no downtime.

> [!TIP]
> To submit and vote on feature requests and product suggestions, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=79a8c474-4e35-e911-a971-000d3a4f3343&forumName=Dynamics%20365%20Customer%20Insights).

## April 2021 updates

The updates in April 2021 include several features, performance upgrades, and bug fixes.

### Data unification
 
- **Enhanced merge experience for data unification**    
  
   We now have an enhanced user experience in the merge configuration of the data unification process. The changes include intuitive ordering of the merged fields and detailed statistics on combined and singleton fields.

- **Entity reordering and configure all source records into the Customer entity**  
      
   You can now reorder and remove entities from an existing conflation plan in the data unification process. It gives flexibility to reorder the entities in the match process according to business needs. Additionally, we enable include all non-matched records into the final *Customer* entity, which lets them define their customer profile dataset definition.

### Enrichments

 - **New enrichment: Enhanced addresses**    
  
   We're excited to introduce a new enrichment to enhance addresses in your customer data. Addresses in your data can be unstructured, incomplete, or incorrect. This feature uses Microsoft's models to normalize and enrich your addresses into the Common Data Model format for better accuracy and insights.
 
   For more information, see [Enrichment of customer profiles with enhanced addresses](enrichment-enhanced-addresses.md).

- **Guided configuration experience for enrichments**    
  
   We revisited the configuration experience for enrichments with a simple, guided experience. You now have a clear step-by-step process for creating and editing enrichments.
 
   Additionally, we separated the configuration of connections for third-party enrichments to enable the same connection to be used by multiple enrichments. Only administrators can configure new connections, but the created connections are available to both administrators and contributors.    

   For more information, see [Connections overview](connections.md).

- **Multiple enrichments of the same type**    
  
   We now allow users to create and manage multiple enrichments of the same enrichment type. For example, you can now create two separate address enrichments to enrich two different customer segments. Limits apply on how many enrichments of the same type can be created and vary depending on the enrichment type.
  
   For more information, see [Enrichment for customer profiles](enrichment-hub.md).

## March 2021 updates

The updates in March 2021 include several features, performance upgrades, and bug fixes.

### Activities

- **Activity wizard and semantic types**

   We have improved and updated our activity mapping experience to guide and simplify the creation of activity mapping. In this new experience, users get a guided experience to help completing of each step of the process. At the activity mapping step, in addition to choosing from many activity types, the user can choose to semantically map data for *Subscription* and/or *SalesOrderLine* to industry standard schemas, which can be used for downstream consumption.   

   For more information, see [Customer activities](activities.md).

### Data ingestion

- **Connect to on-premises data sources using Power Platform dataflows and gateways**
  We are pleased to announce the preview of Power Platform dataflows and on-premises connectivity using gateways in Customer Insights with an associated Power Platform or Dataverse environment. Any new data sources created in a Customer Insights environment with a linked Dataverse environment will default to Power Platform dataflows bringing in the on-premises data connectivity and a rich set of connectors and transformation capabilities.

### Extensibility

- **Exports organized in connections and exports**
  We have changed the name of the **Export destinations** page to **Connections** and added a separate page for **Exports**. As part of this update, we'll transition existing exports into pairs of a connection and an export using that connection. Administrators now have more clarity over outgoing data on the **Connections** page. All user roles have access to the **Exports** page, but only administrators can choose to allow contributors to edit specific exports with shared connections.     
  For more information, see [Connections overview](connections.md) and [Exports overview](export-destinations.md).

- **Export segments to Campaign Monitor**
   We have extended our export destinations to include Campaign Monitor. You can now export segments from Customer Insights to Campaign Monitor lists and use them as the baseline for your marketing campaigns.    
   For more information, see [Export to Campaign Monitor](export-campaign-monitor.md).

- **Export segments to Constant Contact**
   We have extended our export destinations to include Constant Contact. You can now export segments from Customer Insights to Constant Contact lists and use them as the baseline for your marketing campaigns.   
   For more information, see [Export to Constant Contact](export-constant-contact.md).

- **Export segments to RollWorks**
   We have extended our export destinations to include RollWorks. You can now export segments from Customer Insights to RollWorks audiences and use them as the baseline for your B2B advertising.    
   For more information, see [Export to RollWorks ](export-rollworks.md).

- **Export segments to Snapchat**
   We have extended our export destinations to include Snapchat. You can now export segments from Customer Insights to Snapchat audiences and use them as the baseline for your advertising.     
   For more information, see [Export to Snapchat](export-snapchat.md).

### Predictions

- **Use product filters in predictive product recommendations**
   We have added the capability to use product filters in our product recommendation model. You can now create a prediction that uses only a subset of your products.    
   For more information, see [Configure product filters](predict-product-recommendation.md#configure-product-filters).

- **Create segments from model predictions**
  We have added a quick way to create segments using the results of a prediction model. From the model results page, you can easily create a new segment by selecting the new **Create segment** option.    
  For more information, see [Create a segment based on a prediction model](prediction-based-segment.md).

- **Explanations for product recommendations**
   We have added information explaining the key factors learned by the AI model to generate product recommendations and the degree to which those factors contribute towards the product recommendations. This information is added to the model results screen.    
   For more information, see [Review a prediction status and results](predict-product-recommendation.md#review-a-prediction-status-and-results).

## February 2021 updates

The updates in February 2021 include several features, performance upgrades, and bug fixes.

#### Extensibility

- **Export segments to AdRoll**

  We have extended our export destinations to include AdRoll. You can now export segments from Customer Insights to AdRoll audiences and use them as the baseline for your advertising. For more information, see [Connector for AdRoll](export-adroll.md).

#### Segments
 
- **Duplicate a segment**
  
  To create a new segment based on an existing one, you can now duplicate a segment and edit the duplicated segment to refine it further. 

- **Add additional attributes to a segment**

  You can now include attributes in your segment output, even if these attributes are not part of the customer profile. For example, include subscription IDs in a segment even though it is part of the subscription entity that has a M:1 relation with the customer entity. As long as the attribute belongs to an entity related to the customer entity you can now include these attributes.  

#### Predictions

- **Create predictive product recommendations**

  Understanding what customers are interested in purchasing is one of the first steps needed to improve business revenue and build customer loyalty through personalization and engagement. Providing recommendations for products that aren’t aligned to your customer’s interests can create a sense of disconnect between the customer and your business, and ultimately limit the overall potential revenue and experience for a customer. 

  Using your own data, you can now create predictions for what products your customers are likely to purchase in the future. For more information, see [Product recommendation prediction](predict-product-recommendation.md).

#### System administration

- **Copy environment support more types of data sources**

  Admins can copy environment configurations to a new environment in the same organization. This feature extends the copy environment functionality for cases in which data sources based on a Common Data Service data lake or a Common Data Model folder are used.

## January 2021 updates

The updates in January 2021 include several features, performance upgrades, and bug fixes.

#### Extensibility

- **Extended functionality and enhanced performance for SFTP export**
  You can now export all output entities from Customer Insights to an SFTP host. Previously, export was limited to segment entities. 
  Additionally, the performance of the SFTP export allows more data volume in less time, depending on the performance of your SFTP host.    
  For more information, see [Connector for SFTP (preview)](export-sftp.md).  

#### Segments

- **Machine learning powered suggested segments to improve metrics**
  There's a new way do discover and create segments. The system uses an AI model to suggest segments that can help improve a KPI (measure) you are already tracking. We show the extent of influence of attributes that you select on a measure or another primary attribute. This information helps finding potential segments that present opportunities.    
  For more information, see [Suggested segments (preview)](suggested-segments.md).

#### Data unification

- **Enhanced match experience**
  In the data unification area, the match experience was updated. It lets you configure and view the match rules, including detailed stats to further explain how matching works. There are options to disable a match rule so it's no longer active while retaining the configuration, drag and drop match rules, and more.
  For more information, see [Match entities](match-entities.md).

- **Deduplication output from the match process is available as an entity**
  Deduplication process output from the match process is now written into a separate entity for further analysis. This entity consists of the fields used in the deduplication process and the winner record and the corresponding alternate records that get merged with the winner record.
  For more information, see [Deduplication output as an entity](match-entities.md#deduplication-output-as-an-entity).

#### System administration

- **Seamlessly share data to Microsoft Dataverse**
  You can now share Customer Insights output with Microsoft Dataverse applications using the Microsoft Dataverse Managed Data Lake. Once you associate a Dataverse environment with Customer Insights, you get the option to enable data sharing.
  For more information, see [Manage environments](manage-environments.md).




[!INCLUDE[footer-include](../includes/footer-banner.md)]