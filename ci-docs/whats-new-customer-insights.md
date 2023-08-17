---
title: "What's new in Dynamics 365 Customer Insights"
description: "Information about new features, improvements, and bug fixes."
ms.date: 08/16/2023
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: skumm
---

# What's new in Dynamics 365 Customer Insights

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

We're excited to announce our newest updates! This article summarizes public preview features, general availability enhancements, and feature updates. To see the long-term feature plans, take a look at the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

We roll out updates on a region-by-region basis. So certain regions might see features before others. Unless specified differently, you don't need to take any action, we update the app automatically with no downtime.

> [!TIP]
> To submit and vote on feature requests and product suggestions, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=79a8c474-4e35-e911-a971-000d3a4f3343&forumName=Dynamics%20365%20Customer%20Insights).

## July 2023

### Identify and eliminate data quality issues effortlessly with Copilot

The data prep report reduces the time and effort encountered by turning your data into rich insights about your customers, such as segments, measures, and predictions. With actionable recommendations based on an AI-driven quality analysis, you can improve your data quality proactively. Analysts and business users can spend more time generating and using accurate insights and less time on data hygiene, empowering them to elevate customer experiences and optimize business outcomes.

- [Release plan](/dynamics365/release-plan/2023wave2/customer-insights/identify-eliminate-data-quality-issues-effortlessly-copilot)
- [Documentation](data-prep-overview.md)

### Address issues with environment status summary

The System Status page in Customer Insights is an indispensable tool for admins to keep a frequent tab to ensure all jobs are running smoothly. However, when there are errors/issues, the current process of checking through a large table of active jobs can be time-consuming and confusing, especially when there are complex relationships between jobs. Copilot in Customer Insights provides a simple, natural language summary of the environment, prominently highlighting the most important jobs tied to key activation events like exports. Armed with this summary, admins can focus on quickly taking the actions required.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/address-issues-environment-status-summary-copilot)
- [Documentation](system.md#environment-status-summary-preview)

### Monthly enhancements

[Marketing Contributor role](permissions.md#marketing-contributor-preview):

- can search for segments by name and only get results from their BU
- can filter by tags and tags honor BU.Tags created in a BU aren't visible and searchable in other BUs
- can customize the columns they see in their BU-specific view of the segment list
- can download a segment

### New blogs and scenario docs

- [Advanced unification scenario: Create unified customer profiles from functionally unrelated sources](https://community.dynamics.com/blogs/post/?postid=cbf1def2-2a94-4a4d-9535-0489e647157c)

- [Unlocking the power of Dynamics 365 Customer Insights: Best practices for data modelling and data quality](https://community.dynamics.com/blogs/post/?postid=988fae7a-3f37-ee11-bdf4-6045bdebe084)

- [Navigating the data platform landscape: Azure Synapse or Microsoft Fabric](https://community.dynamics.com/blogs/post/?postid=4c923e38-8738-ee11-bdf4-000d3a4e511f)

## June 2023

### Display Customer Insights activities in a Dynamics 365 activity timeline

A single view of all interactions enables a complete understanding of customer activity. With that context, sellers and representatives can create deeply personalized experiences for digital and nondigital channels. In Dynamics 365 Sales, Customer Service, and Marketing, users can see all Customer Insights activities in the unified activity timeline.

After a Dynamics 365 administrator enables the feature, sellers and representatives can view Customer Insights activities directly in the activity timeline. Dynamics 365 apps and Customer Insights must share a Dataverse instance.

Customer Insights activity data can appear within the same activity timeline already used today to add or view activities such as notes, posts, emails, and appointments. The unified activity timeline is available across *Accounts* and *Contacts*.

Customer Insights activities within the Dynamics 365 activity timeline can be filtered, searched, and updated dynamically.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/display-customer-insights-activities-dynamics-365-activity-timeline)
- [Documentation](activities-in-d365-timeline.md)

## May 2023

### Generate insights by asking questions in natural language with Copilot in Customer Insights

Copilot in Dynamics 365 Customer Insights is powered by AI to provide you with insights that answer your questions. In an easy and accelerated manner, you can have a dialogue with your data. Ask questions using natural language to explore, analyze, and understand customer segment sizes and preferences. Analysts and marketers can engage directly with customer data and discover new information that they may not have been aware of.

This feature democratizes access to insights, allowing analysts, marketers, and sellers to ask questions using conversational language and receive instant answers, without needing to have the knowledge of SQL programming. Copilot removes the barriers to getting a deeper understanding of customers, enabling users to speed up and scale the delivery of hyper-personalized experiences that customers expect.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/generate-insights-asking-questions-natural-language-copilot-customer-insights)
- [Documentation](dialog-with-data.md)

### Unify your B2B account and contact data into easy to work with related tables that also support commercial contacts with unknown accounts  

Get a 360-degree view of your B2B contacts by creating unified contact profiles. With this release, your B2B contacts can be unified just like accounts and customers in Dynamics 365 Customer Insights. The unified accounts table and unified contacts table share a simple relationship, allowing you to easily create segments of contacts that have specific account attributes. In addition, you can now identify and engage business contacts where the account is unknown, to discover and create new account relationships

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/gain-360-degree-view-b2b-contacts-leveraging-all-fields-unified-contacts)
- [Documentation](data-unification-contacts.md)

### Bring your custom prediction models from Azure Synapse Analytics into Dynamics 365 Customer Insights, using our Synapse pipeline integration

Now you can utilize your existing custom models in Synapse with routinely refreshed, high-quality unified customer and transaction data from Customer Insights to supercharge your next marketing or sales campaign.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/easily-connect-custom-prediction-models-guided-steps)
- [Documentation](custom-models.md)

### Get an enhanced experience for custom prediction models in Dynamics 365 Customer Insights with a user-friendly wizard

Users can easily and quickly bring custom prediction models from Azure Machine Learning or Azure Synapse Analytics into Customer Insights with a simple 5-step wizard that walks them through establishing a connection, addition of an AI/ML workflow, configuration of model parameters, setup of required data, and reviewing and running the model.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/connect-custom-machine-learning-models-azure-synapse-analytics)
- [Documentation](custom-models.md)

## April 2023

### Advanced application lifecycle management

We're enhancing our delete and reset environment capabilities to make them easier to work with at scale. For example, admins can delete or reset solutions associated with your environment.

Because Customer Insights environments are associated with a Dataverse environment, they're always in sync. Environment owners have access to these capabilities from the Power Platform admin center solutions page and can delegate these permissions.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/do-more-advanced-application-lifecycle-management)

## March 2023

### Generate insights in minutes with first run experience

> [!NOTE]
> [!INCLUDE [single-file-us-only](includes/single-file-us-only.md)]

This first run experience (FRE) feature helps you recognize the value of Dynamics 365 Customer Insights faster. Onboarding a new application can be time-consuming and tricky, leaving room for error and leaving you questioning the value it can bring. This feature saves you precious time and takes the guesswork out of setting up your data correctly the first time you use Customer Insights. It works in trial and paid environments and allows you to get valuable insights faster. Use those insights to fuel better customer experiences and drive a higher return on investment.

After an admin successfully provisions your initial Customer Insights environment, the FRE guides you through three easy steps:

1. Provide data: You're prompted to upload your data file (must be a CSV file containing more than 100 rows and 5 columns).
2. Get data checked: Use AI-driven models, your data is automatically validated and quality-checked—no manual configuration required.
3. Receive insights: Customer Insights identifies business value by deriving patterns and insights from your data file, such as segments and measures.

This FRE works with a single CSV file only. If you have multiple data files, or different data sources, [Customer Insights provides connections to a broad set of sources](data-sources.md).

- [Release plan](/dynamics365-release-plan/2022wave2/customer-insights/generate-insights-minutes-first-run-experience)
- [Documentation](data-sources-single.md) 

## January 2023

### Achieve business scenarios with application lifecycle management

Dynamics 365 Customer Insights starts supporting application and environment lifecycle management capabilities for common enterprise-grade requirements. For example, you can copy, reset, or delete your Customer Insights environments. Additionally, the system ensures your Customer Insights environment and the associated Dataverse environment are always in sync.

- [Release plan](/dynamics365-release-plan/2022wave2/customer-insights/achieve-business-scenarios-application-lifetime-management)
- [Documentation](create-environment.md#copy-the-environment-configuration)

<!--
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

 Data unification lets you unify once-disparate data sources into a single master dataset that provides a unified view of that data. Data can be unified on a single table or multiple tables. First, you [select tables and source fields](data-unification-map-tables.md), [remove duplicate records](data-unification-duplicates.md), specify rules for [matching conditions](data-unification-match-tables.md), and define which [fields to include in the unified customer profiles](data-unification-merge-tables.md).

For more information, see [Data unification overview](data-unification.md).

### Refreshed home page in Customer Insights

**Home** guides you through the configuration process for key features and provides an overview of segments, measures, and enrichment data. We've refreshed the experience to provide more relevant information at a glance.

For more information, see [Explore Customer Insights](home.md).

### Track usage of a segment

You can now [track the usage of a segment](segments-track-usage.md) in apps, which are based on the Dataverse organization that is connected with Customer Insights. For [Customer Insights segments used in customer journeys of Dynamics 365 Marketing](/dynamics365/marketing/real-time-marketing-ci-profile), the system informs you about the usage of that segment.

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

## March 2022 updates

The updates in March 2022 include new features, performance upgrades, and bug fixes.

### LiveRamp AbiliTec enrichment (Preview)

LiveRamp provides identity resolution and consolidation of customer data. You can map personal identifiers in your customer data to the AbiliTec identity graph and receive AbiliTec IDs. You can then use these IDs for better unification of your customer data.

For more information, see [Enrich customer profiles with identity data from LiveRamp (Preview)](enrichment-liveramp.md).

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

For more information, see [Predictions](predictions.md).

### New data source: Integration with Azure Synapse Analytics (Preview)

Azure Synapse Analytics is an enterprise analytics service that accelerates time to insights across data warehouses and big data systems.

Organizations that already use Azure Synapse Analytics can ingest that data to Customer Insights. 

For more information, see [Connect an Azure Synapse data source (Preview)](connect-synapse.md).

### LiveRamp enrichment (Preview)

LiveRamp provides identity resolution and consolidation of customer data. You can map personal identifiers in your customer data to the AbiliTec identity graph and receive AbiliTec IDs. You can then use these IDs for better unification of your customer data.

For more information, see [Enrich customer profiles with identity data from LiveRamp (Preview)](enrichment-liveramp.md).

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
-->

[!INCLUDE [footer-include](includes/footer-banner.md)]