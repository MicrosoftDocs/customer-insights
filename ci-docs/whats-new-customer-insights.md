---
title: "What's new in Dynamics 365 Customer Insights"
description: "Information about new features, improvements, and bug fixes."
ms.date: 08/31/2022
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: skumm
manager: shellyha
---

# What's new in Dynamics 365 Customer Insights

We're excited to announce our newest updates! This article summarizes public preview features, general availability enhancements, and feature updates. To see the long-term feature plans, take a look at the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

We roll out updates on a region-by-region basis. So certain regions might see features before others. Unless specified differently, you don't need to take any action, we'll update the app automatically with no downtime.

> [!TIP]
> To submit and vote on feature requests and product suggestions, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=79a8c474-4e35-e911-a971-000d3a4f3343&forumName=Dynamics%20365%20Customer%20Insights).

## September 2022 updates

The updates in September 2022 include new features, performance upgrades, and bug fixes.

### Export data to HubSpot

Export segments of unified customer profiles to HubSpot and use them for email marketing.

For more information, see [Export segments to HubSpot](export-hubspot.md).

### Remove a unified field or table from data unification

You can remove fields and tables from the data unification process.

For more information, see [Remove a unified field](data-unification-update.md#remove-a-unified-field).

### Manage unknown customer profiles

Memorable personalization depends on the richness and completeness of your customer data and Customer Insights helps you achieve these goals. You can manage customer profiles for users for which you don't have any information other than an ID.

For more information, see [Manage unknown profiles with Customer Insights](manage-unknown-profiles.md).

## August 2022 updates

The updates in August 2022 include new features, performance upgrades, and bug fixes.

### Contact unification in B-to-B environments

B-to-B environments in Customer Insights now support an enhanced data unification experience.

You can now unify contacts in addition to accounts to get a full view of your business contacts. Unified contacts are associated with unified accounts and are now listed on the customer cards. 

For more information, see [Create a unified contact profile](data-unification-contacts.md).

### Create and export of segments based on unified contacts

Thanks to the new contact unification, you can create segments of contacts using criteria from either contacts, accounts, or both. These segments can be exported for activation in other services.

For more information, see [Exports overview](export-destinations.md).

### Deployment regions aligned with Microsoft Dataverse

When creating a new Customer Insights environment, you can select the region where you would like the service to be deployed and hosted. We have updated the region selection to align with Microsoft Dataverse and the Power Platform.

You can now easily select the same region as your existing Microsoft Dataverse environment or your Azure Data Lake storage account (if you choose that option), subject to availability of Customer Insights in that region.

For more information, see [Create a new environment](create-environment.md) and [Product availability by geography](https://dynamics.microsoft.com/availability-reports/).

## July 2022 updates

The updates in July 2022 include new features, performance upgrades, and bug fixes.

### Export to MoEngage

Export segments of unified customer profiles to MoEngage and use them for email marketing in MoEngage.

For more information, see [Export segments to MoEngage](export-moengage.md).

### SSH support for SFTP-based exports

Choose whether you want to authenticate through SSH or username/password for connections to SFTP export destinations.

For more information, see [Export data to SFTP hosts](export-sftp.md).

### Personalize experiences with data about known and unknown users

Managing customer data isn't a new challenge but it's increasingly becoming more difficult as users navigate the various digital channels brands offer. A user who is known (authenticated) in one channel becomes unknown (unauthenticated) in another if not signed in. The problem often is that unauthenticated (unknown) users don't have a common ID. It could be used to associate meaningful profiles attributes and generate unified customer profiles. Customer Insights helps solve this problem by ingesting data from tracking methods on your source systems.

For more information, see [Personalize your experiences with data about known and unknown users](unknown-to-known.md).

## June 2022 updates

The updates in June 2022 include new features, performance upgrades, and bug fixes.

### Updated user experience for data sources and data ingestion

Importing data from a wide range of data sources is the foundation to consolidating your customer data in Dynamics 365 Customer Insights. We've revisited the user experience for the import and connection of data sources. This update aims to make it easier for you to ingest data to Customer Insights.

For more information, see [Data sources overview](data-sources.md).

### Export to InMobi

InMobi helps brands understand, identify, engage, and acquire consumers. You can export segments and other data to the InMobi service via Azure Blob Storage accounts.

For more information, see [Export to InMobi (preview)](export-inmobi.md)

### Lockbox support in Customer Insights

Customer Lockbox provides an interface to review and approve (or reject) data access requests. These requests occur when data access to customer data is needed to resolve a support case.

For more information, see [Securely access customer data with Customer Lockbox (Preview)](security-overview.md#securely-access-customer-data-with-customer-lockbox-preview).

### Connect to your data using Azure Private Link

Azure Private Link lets Customer Insights connect to your Azure Data Lake Storage account over a private endpoint in your virtual network. For data in a storage account, which isn't exposed to the public internet, Private Link enables the connection to that restricted network.

For more information, see [Use Private Link in Customer Insights](security-overview.md#set-up-an-azure-private-link).

## May 2022 updates

The updates in May 2022 include new features, performance upgrades, and bug fixes.

### Updated data unification experience

 Data unification lets you unify once-disparate data sources into a single master dataset that provides a unified view of that data. Data can be unified on a single table or multiple tables. First, you [select tables and source fields](map-entities.md), [remove duplicate records](remove-duplicates.md), specify rules for [matching conditions](match-entities.md), and define which [fields to include in the unified customer profiles](merge-entities.md).

For more information, see [Data unification overview](data-unification.md).

### Refreshed home page in Customer Insights

**Home** guides you through the configuration process for key features and provides an overview of segments, measures, and enrichment data. We've refreshed the experience to provide more relevant information at a glance.

For more information, see [Explore Customer Insights](home.md).

### Track usage of a segment

You can now [track the usage of a segment](segments.md#track-usage-of-a-segment) in apps, which are based on the Dataverse organization that is connected with Customer Insights. For [Customer Insights segments used in customer journeys of Dynamics 365 Marketing](/dynamics365/marketing/real-time-marketing-ci-profile), the system informs you about the usage of that segment.

### Export to Criteo

Criteo is an online platform that helps users manage digital advertising. You can now export segments of unified customer profiles to generate campaigns, provide email marketing and use specific groups of customers with Criteo.

For more information, see [Export segments to Criteo (preview)](export-criteo.md).

### Refined documentation structure for environment creation

We've revisited the help docs related to the creation and management of environments in Customer Insights. The articles are now grouped under the Environments node in the table of contents. The restructured articles provide more guidance for the different ways to set up environments and have a clearer structure. If you have feedback to share, let us know via the controls towards the end of the help articles.

For more information, see [How to: Create a new environment](create-environment.md).

## April 2022 updates

The updates in April 2022 include new features, performance upgrades, and bug fixes.

### Dun & Bradstreet enrichment (Preview)

Dun & Bradstreet provides commercial data, analytics, and insights for businesses. It enables customers with unified customer profiles for companies to enrich their data. Enrichments include attributes such as DUNS number, company size, location, industry, and more.

For more information, see [Enrichment of company profiles with Dun & Bradstreet (Preview)](enrichment-dnb.md).

### Define the measure type when creating a new measure

You can now distinguish between measures for individual profiles and measures across your entire business. While business measures show on the home page of Customer Insights, customer measures are exposed on the detailed customer views.

For more information, see [Use measure builder to create measures from scratch](measure-builder.md).

### Consolidation of Customer Insights documentation

We've revisited our documentation articles and removed mentions of engagement insights and audience insights capabilities. Moving forward, we'll refer consistently to the product name Customer Insights when we write about the core features of the application. This change also leads to significant restructuring of the table of contents, the URL structure, and the file paths in the underlying documentation repository. All your bookmarks or existing links continue to work and redirect to the updated URLs.

If you want to let us know how you perceive that change or spot something not working as expected, tell us by [submitting feedback for this page](https://github.com/MicrosoftDocs/customer-insights/issues/new?title=&body=%0A%0A%5BEnter%20feedback%20here%5D%0A%0A%0A---%0A%23%23%23%23%20Document%20Details%0A%0A%E2%9A%A0%20*Do%20not%20edit%20this%20section.%20It%20is%20required%20for%20docs.microsoft.com%20%E2%9E%9F%20GitHub%20issue%20linking.*%0A%0A*%20ID%3A%20d323ba46-f96e-1972-bc52-9b88f7d9cdfa%0A*%20Version%20Independent%20ID%3A%20d323ba46-f96e-1972-bc52-9b88f7d9cdfa%0A*%20Content%3A%20%5BNew%20and%20upcoming%20features%20-%20Dynamics%20365%20Customer%20Insights%5D(https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fdynamics365%2Fcustomer-insights%2Fwhats-new-customer-insights)%0A*%20Content%20Source%3A%20%5Bci-docs%2Fwhats-new-customer-insights.md%5D(https%3A%2F%2Fgithub.com%2FMicrosoftDocs%2Fcustomer-insights%2Fblob%2Fmain%2Fci-docs%2Fwhats-new-customer-insights.md)%0A*%20Service%3A%20**customer-insights**%0A*%20Sub-service%3A%20**audience-insights**%0A*%20GitHub%20Login%3A%20%40m-hartmann%0A*%20Microsoft%20Alias%3A%20**mhart**).

## March 2022 updates

The updates in March 2022 include new features, performance upgrades, and bug fixes.

### LiveRamp AbiliTec enrichment (Preview)

LiveRamp provides idtable resolution and consolidation of customer data. You can map personal identifiers in your customer data to the AbiliTec idtable graph and receive AbiliTec IDs. You can then use these IDs for better unification of your customer data.

For more information, see [Enrich customer profiles with idtable data from LiveRamp (Preview)](enrichment-liveramp.md).

### Organize segments and measures with tags and filters

If your organization maintains lots of segments or measures, finding the right one can sometimes feel challenging. This new feature lets you organize lists using tags and columns. It helps to find data quickly and easily and customize the views.

For more information, see [Work with tags and columns](work-with-tags-columns.md).

### Enable data sharing with Dataverse when using your own storage account

If your environment uses Azure Data Lake Storage to store Customer Insights data, data sharing with Microsoft Dataverse needs some extra configuration.
Earlier, you could only enable data sharing with Dataverse when your data was stored in our managed data lake.

For more information, see [Enable data sharing with Dataverse from your own Azure Data Lake Storage (Preview)](customer-insights-dataverse.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview).

### New export destinations: Iterable and Braze

We’re continuing to expand our ecosystem of export destinations with new connections. You can now export segments to Iterable and Braze to use their activation services.

For more information, see [Export segments to Iterable (preview)](export-iterable.md) and [Export segments to Braze (preview)](export-braze.md).

### Improvements to Marketo and Google Ads export

Changing APIs in connected services lead to updates for connectors to run reliably and smoothly. We’ve released some updates for the exports to Marketo and Google Ads services:

- Google Ads: The new version of the Google Ads export connector simplifies the authentication experience and now lets you create new Google Ads audiences automatically. 
- Marketo: The new version of the Marketo export connector provides support for the Marketo ID, enabling you to avoid data duplication, update existing records, and create new records in Marketo. 

## February 2022 updates

The updates in February 2022 include new features, performance upgrades, and bug fixes.

### General availability for prediction models

Out-of-the-box prediction models, including **subscription churn**, **transactional churn**, and **customer lifetime value (CLV)** become generally available as a part of Customer Insights. 

For more information, see [Predictions overview](predictions-overview.md).

### New data source: Integration with Azure Synapse Analytics (Preview)

Azure Synapse Analytics is an enterprise analytics service that accelerates time to insights across data warehouses and big data systems.

Organizations that already use Azure Synapse Analytics can ingest that data to Customer Insights. 

For more information, see [Connect an Azure Synapse data source (Preview)](connect-synapse.md).

### LiveRamp enrichment (Preview)

LiveRamp provides idtable resolution and consolidation of customer data. You can map personal identifiers in your customer data to the AbiliTec idtable graph and receive AbiliTec IDs. You can then use these IDs for better unification of your customer data.

For more information, see [Enrich customer profiles with idtable data from LiveRamp (Preview)](enrichment-liveramp.md).

### Enrichment for data sources (Preview)

Use data from sources like Microsoft and other partners to enrich your customer data before data unification. Data source enrichments help produce higher data completeness and quality that can help achieve better results once you unify your data.

For more information, see [Enrichment for data sources (Preview)](data-sources-enrichment.md).

### Change owner of environment

While several users can have admin permissions in Customer Insights, only one user is the owner of an environment. An improved experience lets you change owners of an environment and claim ownership if a former owner left the organization. 

For more information, see [Change the owner of an environment](manage-environments.md#change-the-owner-of-an-environment).

### Data preparation process lists corruption reason for corrupted records

Data preparation now shows the reason for corruption for all fields with corrupted data. The information is provided at the individual record level for easy identification.

For more information, see [Corrupt data sources](data-sources.md#corrupt-data-sources).

### End of preview for reporting features in the engagement insights capability

The Dynamics 365 Customer Insights engagement insights capability preview ended February 15, 2022.  
This change means the Customer Insights trial experience no longer includes the ability to create funnels nor other reporting functionality.

We invite you to explore and evaluate the many other features of [Customer Insights](https://dynamics.microsoft.com/ai/customer-insights/), the Microsoft customer data platform (CDP).    
 
For a transition period, existing preview participants still have access to some preview capabilities and functionality:

- Get code to instrument a web site or mobile app 
- See events and event properties 
- Enhance unified profiles with ingested and refined events to benefit from the full value of their customer data
  
During the transition period, captured events are still streamed to the connected Data Lake. Once this functionality is turned off, data sharing will stop, and no new events are sent to the connected storage.
Contact your Microsoft Account team directly if you have questions about the end of the capability preview. Your Account team will keep you up to date on coming launches. 

## January 2022 updates

The updates in January 2022 include new features, performance upgrades, and bug fixes.

### Sentiment analysis of your customer’s feedback

Customer Insights provides a new AI-powered feature to synthesize customer sentiment and identify specific business aspects as opportunities for targeted improvements. By analyzing the written feedback of your customers, you can get accurate insights at low cost. Sentiment analysis powered by Natural Language Processing (NLP) models that generate two derived insights for each customer ID. A sentiment score (of –5 to 5) and list of applicable business aspects. 

For more information, see [Analyze sentiment in customer feedback (Preview)](sentiment-analysis.md).


[!INCLUDE [footer-include](includes/footer-banner.md)]