---
title: "New and upcoming features"
description: "Information about new features, improvements, and bug fixes."
ms.date: 11/04/2021
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

## October 2021 updates

The updates in October 2021 include a new features, performance upgrades, and bug fixes.

## B-to-B

Starting in October 2021, you can work with business accounts and their related contacts in Customer Insights. Before, the app was mostly tailored towards individual consumers. Several feature areas were updated to support B-to-B scenarios on top of a new environment type. 
For an overview on supported B-to-B features, see [Work with business accounts in audience insights](work-with-business-accounts.md).

The following sections highlight some of the key areas that were adapted to support business accounts and individual consumers.

### Export segments based on business accounts

All segment exports in audience insights are available in the context of business accounts. Most segment exports require extra configuration and [contact information projected](segment-builder.md#create-a-new-segment) in the underlying segments to be valid for business accounts. For more information, see [Export segments](export-destinations.md#export-segments).

### Use the LinkedIn Ads export with business accounts

The LinkedIn Ads export is now available for contact and company targeting in the context of business accounts. When selecting company targeting as your primary focus of the LinkedIn export, you can export segments built on business accounts without the need to project contact information. For more information, go to the docs about [LinkedIn Ads export](export-linkedin-ads.md) and the difference between [contact targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/contact-targeting) and [company targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/account-targeting). 

### Create measures based on business accounts and their hierarchy

The measure builder lets you create measures around business accounts and optionally use the hierarchy information. Hierarchy information is used to roll up a measure calculation across an account and all its related sub accounts. For example, you can create measures like total revenue for each group of business accounts identified by their hierarchy. For more information, see [Define and manage measures](measures.md).

### Create segments based on business accounts and their hierarchy

The segment builder enables you to create segments of business accounts that optionally include contact information for each account in a segment. If you have account hierarchy set up, you can use account hierarchy information in segment creation. For more information, see [Create a new segment](segment-builder.md#create-a-new-segment).

### Retain your business accounts with deep insights to their churn tendency

The customer churn prediction model now supports business accounts too. You can evaluate the risk of churn not just for an account but for a combination of an account and a product or service category that they buy from you. This addition helps you to understand if an account is more likely to stop buying from you in general or just for a certain category of goods or services. To further help you use this AI model, it also lists reasons why an account is likely to churn. For more information, see [Transaction churn prediction (preview)](predict-transactional-churn.md).

### See contacts of a business account in Customer view

If business accounts are mapped to related accounts, the Customer Insights app shows these related contacts as part of the customer details view. For more information, see [Customer profiles](customer-profiles.md).


## September 2021 updates

The updates in September 2021 include a new features, performance upgrades, and bug fixes.

### Activities

- **Activity timeline improvements**
  We have extended the filters for the activity timeline on customer profiles. Additionally, you can use the new filter pan to filter by activity type and by date. Dates can be filtered using different conditions. For more information, see [View activity timelines on customer profiles](activities.md#view-activity-timelines-on-customer-profiles).

### Relationships

- **Multi-hop relationship support**
  Use multi-hop relationships when configuring activities and defining relationships between entities. Multi-hop relationships use an intermediate entity to connect two entities. When configuring an activity, you can use a multi-hop relationship to connect your activity entity to an intermediate entity and then to a customer entity. You can combine multi-hop relationships with multi-path relationships. For more information, see [Multi-hop relationship](relationships.md#multi-hop-relationship).

- **Multi-path relationship support**
  Use multi-path relationships when configuring activities and defining relationships between entities. Multi-path relationships relate a source entity to more than one entity. When configuring an activity, you can use a multi-path relationship to connect your activity entity to more than one customer entity. You can combine multi-path relationships with multi-hop relationships. For more information, see [Multi-path relationship](relationships.md#multi-path-relationship).

## August 2021 updates

The updates in July and August 2021 include a new feature, performance upgrades, and bug fixes.

### Extensibility

- **Export segments to Klaviyo**
  We have extended our [export destinations to include Klaviyo](export-klaviyo.md). You can now export segments to crate campaigns, do email marketing, and use specific groups of customers with Klaviyo. 


## June 2021 updates

The updates in June 2021 include several features, performance upgrades, and bug fixes.

### Data ingestion

- **Improved data unification progress updates**
  You can now view more granular, improved dynamic status updates on the [data unification process](data-unification.md) steps. This feature lets you keep track of the detailed progress to understand the process flow and take action if any step needs attention.

### Extensibility

- **Export segments and other data to Salesforce Marketing Cloud**
  We have extended our export destinations to include [Salesforce Marketing Cloud](export-salesforce.md). You can now export segments and other types of data to Salesforce Marketing Cloud through a branded SFTP export. Data import can be fully automated in Salesforce and used to create more effective marketing campaigns.  
 
- **Export segments to ActiveCampaign**
  We have extended our export destinations to include [Active Campaign](export-active-campaign.md). You can now export segments to generate campaigns, run email marketing, and work with specific groups of customers in ActiveCampaign.
 
- **Export segments to Sendinblue**
  We have extended our export destinations to include [Sendinblue](export-sendinblue.md). You can now export segments to generate campaigns, run email marketing, and work with specific groups of customers with Sendinblue.
 
### UX updates 

- **New and enhanced Customers page and profile details page**
  We have redesigned the Customers page and the profile detail pages for improved user experience and better performance. These changes let you view, sort, search, and filter customers. Filters are now represented in the URL to share the search results with other users seamlessly. Search results can also be saved as a segment.    
  The details page for customer profiles now groups data in various subsections such as demographic data, IDs, and other profile attributes for improved readability. Other sections on the profile details page are now more interactive. For example, the activities section now allows filtering and sorting.


## May 2021 updates

The updates in May 2021 include several features, performance upgrades, and bug fixes.

### Data ingestion

- **View or modify metadata or entity definition when attaching data from your Azure Data Lake Storage**
  You can now view and edit metadata or entity definition in audience insights when attaching data from a Common Data Model folder in your Azure Data Lake Storage. This capability provides real-time feedback, model validation, and error checking. It allows you to edit both model.json and manifest.json seamlessly.

### Extensibility

- **Improved segment exports, custom schedule, and duplication**
  You can now [see all exports for a specific segment](export-destinations.md#view-exports-and-export-details) in a list. This new view helps to manage how a specific segment is used and adapt existing or create new exports.    
  You can [define custom refresh schedules](export-destinations.md#schedule-and-run-exports) for individual exports or several exports at once. Until now, all exports were run with every system refresh.    
  Rather than creating a new export from scratch, you can start based on an existing one to save some time.

- **Export segments to Microsoft Advertising**
  We have extended our export destinations to include Microsoft Advertising. Create Customer Match audiences on Microsoft Advertising with your unified customer profile data and use these audiences for your advertising campaigns. For more information, see [Export segments to Microsoft Advertising](export-microsoft-advertising.md).

- **Export segments to LinkedIn Ads**
  We have extended our export destinations to include LinkedIn Ads and enable you to unlock Contact Targeting as well as Company Targeting through LinkedIn by exporting your unified customer profile data. For more information, see [Export segments to LinkedIn Ads](export-linkedin-ads.md).


- **Export segments to Omnisend**
  We have extended our export destinations to include Omnisend. Use the segments created in audience insights to generate campaigns, provide email marketing, and use specific groups of customers with Omnisend. For more information, see [Export segments to Omnisend](export-omnisend.md)

### Predictions

- **Input Data Usability Report**
  The input data usability report provides a consolidated view of the errors and warnings that your out-of-box predictions may be generating. It also gives recommendations how to improve the model performance.    
  The report is available after a model has completed its training process. It's created for each model separately, regardless of whether it completed successfully or not.
  Currently, this feature is only available for the Transaction Churn model. For more information, see [Input data usability report](manage-predictions.md#input-data-usability-report).

### Relationships

- **Relationship visualizer**
  The relationship visualizer view allows you to see all existing relationships between entities and their cardinality. Relationships are now organized in groups: user created, system, and inherited relationships. You can also export a view as an image. For more information, see [View relationships](relationships.md#view-relationships). 

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
   We have extended our export destinations to include RollWorks. You can now export segments from Customer Insights to RollWorks audiences and use them as the baseline for your B-to-B advertising.    
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

  Admins can copy environment configurations to a new environment in the same organization. This feature extends the copy environment functionality for cases in which data sources based on a Microsoft Dataverse managed data lake or a Common Data Model folder are used.

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