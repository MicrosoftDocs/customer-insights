---
title: "What's new in Dynamics 365 Customer Insights - Data"
description: "Information about new features, improvements, and bug fixes."
ms.date: 06/03/2025
ms.topic: whats-new
author: colinbirkett
ms.author: colinbirkett
ms.reviewer: colinbirkett
---

# What's new in Dynamics 365 Customer Insights - Data

We're excited to announce our newest updates! This article summarizes public preview features, general availability enhancements, and feature updates. To see the long-term feature plans, take a look at the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

We roll out updates on a region-by-region basis. So certain regions might see features before others. Unless specified differently, you don't need to take any action, we update the app automatically with no downtime.

> [!TIP]
> To submit and vote on feature requests and product suggestions, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=79a8c474-4e35-e911-a971-000d3a4f3343&forumName=Dynamics%20365%20Customer%20Insights).

## June 2025

### Public preview

#### Filter rows from source data for better processing** 

Improve the quality of your unified customer profiles and insights by filtering out unwanted rows from your source data directly in Customer Insights - Data. Removing old or incomplete rows that don’t provide value allows Customer Insights - Data to create higher quality insights in less time and saves having to filter out unwanted data in downstream processes.

- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-data/filter-rows-columns-source-data-improved-processing)

:::image type="content" source="media/row-filtering.png" alt-text="Filter rows from source data for better processing." lightbox="media/row-filtering.png":::

## October 2024

### General availability

#### Use automation to manage segments and measures

As your Dynamics 365 Customer Insights usage increases, so does the number of segments and measures. Large numbers of segments and measures can result in longer system refresh times, which delay time-sensitive insights. 
Customer Insights now automatically deactivates segments and measures based on their usage to ensure your active segments and measures refresh faster. As an admin you get to control the retention period that applies and can support your organization to scale confidently.

- [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-data/use-automation-manage-segments-measures)
<!--- - [Docs](.md) -->

#### Accelerate time to insights with data in Delta Lake format

Your customer data updates constantly, with rapidly changing signals like online activities and mobile interactions. When a traditional data warehouse is used to generate customer insights, this leads to increased time to insight with each update while the volume of unprocessed signals keeps growing. Longer queues result in slow or stale insights. With native support for Delta Lake storage format in Customer Insights, you can now accelerate processing times even with a higher volume of fast-changing data updates. Get customer profiles and associated insights updated more frequently and react to customer engagements based on the most current information available. This empowers you to create the most relevant and personalized experiences for your customers and the most up-to-date and timely insights for your business users.

- [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-data/accelerate-time-insights-data-delta-lake-format)
<!--- - [Docs](.md) -->

## September 2024

### Public preview

#### Accelerate time to insights with data in Delta Lake format

Your data updates constantly, with rapidly changing signals like online activities and mobile interactions. When a traditional data warehouse is used to generate customer insights, this leads to increased time to insight with each update while the volume of unprocessed signals keeps growing. Longer queues result in slow or stale insights. With native support for Delta Lake storage format in Customer Insights, you can now accelerate processing times even with a higher volume of fast-changing data updates. You can get customer profiles and associated insights updated more frequently and react to customer engagements based on the most current information available. This empowers you to create the most relevant and personalized experiences for your customers and the most up-to-date and timely insights for your business users.

- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-data/accelerate-time-insights-data-delta-lake-format)
- [Docs](connect-delta-lake.md)

## June 2024

### General availability

#### Unlimited application installs now in Customer Insights

Limiting application installations creates unnecessary friction for customers wanting to install and use real-time journeys and Customer Insights – Data on their environments across different departments and geographies.

To reduce this friction, we're removing the limitations on [application installations for real-time journeys and Customer Insights - Data](../journeys/setup.md). This enhancement enables you to install and use Customer Insights - Journeys (real-time journeys) and Customer Insights - Data across all your departments and locations. By removing these obstacles, we enable you to fully tap into the power of Customer Insights.

- [Blog post](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/06/18/announcing-unlimited-application-installs-in-dynamics-365-customer-insights/)

### Public preview

#### Elevate customer experiences in real time

Customer Insights helps you collect web interactions in real time, enabling personalized experiences and a deeper understanding of your customers' needs and preferences.

This capability includes the following features:

**Real-time web tracking**: Ensure that your customer data is ingested in real time with a tracking script that can be added to your website. Capture high-intent signals such as "viewed pricing page," "added item to the cart," or "downloaded e-book" in real time.

**Real-time unknown profiles**: Capture web data from all your visitors even if they're not authenticated and let the system automatically create unknown profiles in real time.

**Real-time unknown-to-known**: Merge unknown profiles into known profiles in real time, so you can always have the 360-degree view of your customers.

**Real-time web personalization**: Leverage our APIs to read your customer data, including segment memberships, web events, or demographic data in real time to personalize the web experience for your visitors.

- [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-data/elevate-customer-experiences-real-time)
- [Docs](real-time-web-personalization-overview.md)

#### Personalize omnichannel experiences with no code using Optimizely

Customer Insights and Optimizely now unlock omnichannel personalization and experimentation capabilities, enabling marketers and citizen developers to personalize every customer touchpoint with no code or prior expertise required. By combining insights and segments from Customer Insights with Optimizely audiences, you can create experiences that are tailored to your customer's browsing activity, their loyalty, past engagement history, and other real-time signals. Moreover, you can continue the conversation or re-target your visitors by delivering the same consistent experience through customer journeys, based on which Optimizely treatment cohort the customer was part of.

- [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-data/personalize-omnichannel-experiences-no-code-using-optimizely)
- [Docs](optimizely-integration.md)

## April/May 2024

### General availability

#### Segments and measures limits increased

We have increased the limit for active segments and measures in Dynamics 365 Customer Insights – Data from 500 to 1000. You can now create and manage more campaigns using up to 1000 segments or measures based on your customer data and use them for targeted marketing, personalized experiences, or sales actions.  

- [Docs](service-limits.md)

### Public preview

#### Keep Facebook audiences in sync with a single connection

The exports feature in Dynamics 365 Customer Insights lets you choose which customer segments you want to synchronize with Facebook for targeted advertisements. That flexibility can also mean ongoing administration due to Facebook’s requirement to reauthenticate every 60 days.
With this release, managing your exports to Facebook becomes easier. Now, you can manage all your Facebook Ads exports through a single connection. This reduces your effort to managing one connection, regardless of the number of exports you've set up.

- [Docs](export-facebook.md)

## February/March 2024

### General availability features

#### Leverage customer insights in other business applications

Insights are available to your business users through their Dynamics 365 applications in the flow of their work. This enables numerous scenarios. For example:

- Marketing teams can personalize the experience of customers with segments and dynamic content based on their lifetime value, irrespective of where they are on the buying journeys and whether they're targeted as a lead or a contact.
- Sales and account reps can win more deals and foster stronger relationships, knowing every customer's interests, activity history, insights such as CLV or predictions such as propensity to buy - all accessible seamlessly in their contact or lead view.
- Service reps can provide personalized service knowing the customer's loyalty tier or prediction to churn.

:::image type="content" source="media/sales-ci-data.png" alt-text="Dynamics 365 Sales user interface with loyalty data from Customer Insights.":::

- [Release plan](/dynamics365/release-plan/2023wave2/customer-insights/empower-marketing-sales-service-users-customer-insights-right-within-their-business-applications)
- [Docs](integrate-d365-apps.md)

### New blog

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blog:

- [Dynamics 365 Customer Insights - Data: Inbound Data Batch Integration Patterns Introduction](https://community.dynamics.com/blogs/post/?postid=f32d115e-d9cb-ee11-92bd-000d3a7e795a)

## January 2024
<!--
### General availability features

#### Get insights by asking questions in natural language with Copilot in Customer Insights, now with general and global availability

Ask questions in natural language to have a dialog with your data to explore, assess, and better understand the profiles, behavior, and activity of your customers. Now with general availability and global availability across all geos and 23 supported languages to support enterprise and global customers. Get started today to democratize the power of your customer data platform (CDP) to everyone in your organization in a compliant and secure manner. Enable your end users to seamlessly access insights to make the best decisions in the moments that matter and provide deeply personalized experiences to your customers. For example, marketers can now use everyday words to understand the geographic distribution of loyalty program members and their recent transaction history to better cater customer lifetime value-focused campaigns and achieve higher campaign engagement.

- [Release plan](/dynamics365/release-plan/2023wave2/customer-insights/generate-insights-asking-questions-natural-language-copilot-customer-insights)
- [Docs](dialog-with-data.md)
-->
### Monthly enhancements

#### In-place upgrade of data sources to Delta format

If your data is already in Delta tables within the same storage container, you can update the connection on the Data Sources page. Update the folder and connection points to the folder that contains the same tables, but in the Delta format. Delta tables can significantly reduce the time to generate valuable insights from a data source. Also, if you're currently converting your Delta data into the common data model format to import it to Customer Insights – Data, Delta lake formatted tables help eliminate the processing and storage requirements to convert Delta data to common data model format.

#### Exports show most recent update

You can now track changes to exports with newly added columns that show details about when an export was last updated and by whom. This addition addresses user requests for more control over recent modifications. The **Last updated** column shows when an export was updated and the **Updated by** column lists the user who made the most recent change. These columns help foster team collaboration and accountability.

## December 2023

### General availability features

#### Personalize customer experiences using calculated metrics

You can already create highly personalized experiences for your customers when you use enriched profiles from Dynamics 365 Customer Insights - Data. Now, you can further personalize journeys and content by using calculated metrics (customer measures) such as lifetime value, total or average spend, total amount insured or number of policies, etc. With such calculated data available seamlessly, you're empowered to deliver experiences such as personalizing offers or level of service (for example, priority notification ahead of others).

- [Release plan](/dynamics365/release-plan/2023wave2/customer-insights/personalize-customer-experiences-using-calculated-metrics)
- [Docs](dataverse-measures.md)

### Public preview features

#### Use customer insights in other business applications

Insights are available to your business users through their Dynamics 365 applications in the flow of their work. This enables numerous scenarios. For example:

- Marketing teams can personalize the experience of customers with segments and dynamic content based on their lifetime value, irrespective of where they were on the buying journeys and whether they’re targeted as a lead or a contact.
- Sales and account reps can win more deals and foster stronger relationships, knowing every customer’s interests, activity history, insights such as CLV or predictions such as propensity to buy—all accessible seamlessly in their contact/lead view.
- Service reps can provide personalized service knowing the customer’s loyalty tier or prediction to churn.

## October 2023

### General availability features

#### Improved accuracy of the deduplication process

You might have customer data where a person has multiple records and has provided different emails and phone numbers over time, making it impossible to match all their records using a single rule. Because Customer Insights today can't combine customer records that were matched by different rules, the result can be the creation of separate profiles for that person, which fragments your view of the customer.

In a revisited deduplication process, the system now runs every deduplication rule against every customer record in a table. The match results from all the rules are then analyzed and match groups that share a common record are combined into a single match group. This process can identify and combine potentially long and complex chains of matching relationships, which result in the creation of unified customer profiles with unparalleled accuracy.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/improved-accuracy-deduplication-process)
- [Docs](data-unification-duplicates.md)

### Public preview

#### Receive task assistance from copilot based on docs

Setting up Customer Insights with all your data and managing it to stay healthy can be complex at times. Now, Copilot in Customer Insights assists you by providing timely guidance that adapts, depending on where you are in the configuration process. In addition to this guidance, you can also ask your own questions to help clarify concepts or understand what you need to do next to successfully configure your solution.

- [Release plan](/dynamics365/release-plan/2023wave2/customer-insights/receive-task-assistance-copilot-based-docs)
- [Docs](help-pane-copilot.md)

#### Seamlessly onboard customer data from your Delta Lake with no data integration

Data already prepared and stored in your Azure Data Lake storage in the Delta Lake format can be readily attached in Customer Insights without data movement and formatting. This accelerates the processing time and reduces operations management of intermediate processing and data preparation leading to more regular and current insights. As a result, organizations can obtain more frequent and up-to-date insights, allowing them to make informed decisions faster and adapt to changing business environments more effectively.

- [Release plan](/dynamics365/release-plan/2023wave2/customer-insights/seamlessly-onboard-customer-data-delta-lake-no-data-integration)
- [Docs](connect-delta-lake.md)

### Monthly enhancements

#### Simple customer measure

You can now create [customer measures](measures.md) with only one dimension and one calculation in that measure. The measure is available as a table in Dataverse for easy usage in Power Apps.

#### Enable configuring and running of exports for Business Units

Members of business units can now configure and run exports with a [Marketing contributor role](user-roles.md), limited to segments they have configured within their business unit. Administrators remain in control of which export destinations are available to other users by sharing the configured connections of export destinations.

#### Environment reset is now generally available

[Resetting an environment](manage-environments.md#reset-an-existing-environment) removes configurations and data from your Customer Insights - Data environment, restoring it to a new state that allows you to start fresh. Effectively, this is a quick way to uninstall and reinstall Customer Insights – Data from the application user interface.

## August/September 2023

### General availability features

#### Improved accuracy of the deduplication process

Customer Insights can now match and unify all the profile data for a specific customer, even if it requires several matching rules to identify all the customer’s records. Fully unified customer data ensures you can confidently use profiles to personalize the customer experience and make smarter decisions.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/improved-accuracy-deduplication-process)
- [Docs](data-unification-duplicates.md)

### Public preview

#### Build and refine segments quickly using everyday words with copilot

Effective segmentation, while a powerful tool for targeting the right audience, has traditionally required a thorough understanding of complex data models, database management and SQL (Structured Query Language). Segmentation assist, a copilot feature in Dynamics 365 Customer Insights, now makes it easy for marketing and CX teams to build and refine the rules that compose a segment using natural language, and immediately target them with customer journeys in Dynamics 365 Marketing or sync to ad/Martech platforms.

- [Release plan](/dynamics365/release-plan/2023wave2/customer-insights/build-segments-using-everyday-words-copilot-customer-insights)
- [Docs](segments-copilot.md)

### Monthly enhancements

#### Understand how various rules impact the number of members in your segment

Segments in Customer Insights - Data, now provides an "Inspection mode" toggle for segments. Enable this when creating or editing a segment to understand the contribution of each rule to the overall size of the segment, after a segment has been processed. Additionally, inspection mode also provides the cascading effect/contribution of each rule, thus giving you greater visibility and control to tweak the segment definition to match your marketing budget.

- [Docs](segments.md#view-segment-member-counts-preview)

## July 2023

### Identify and eliminate data quality issues effortlessly with Copilot

The data prep report reduces the time and effort encountered by turning your data into rich insights about your customers, such as segments, measures, and predictions. With actionable recommendations based on an AI-driven quality analysis, you can improve your data quality proactively. Analysts and business users can spend more time generating and using accurate insights and less time on data hygiene, empowering them to elevate customer experiences and optimize business outcomes.

- [Release plan](/dynamics365/release-plan/2023wave2/customer-insights/identify-eliminate-data-quality-issues-effortlessly-copilot)
- [Documentation](data-prep-overview.md)

### Address issues with environment status summary

The System Status page in Customer Insights - Data is an indispensable tool for admins to keep a frequent tab to ensure all jobs are running smoothly. However, when there are errors/issues, the current process of checking through a large table of active jobs can be time-consuming and confusing, especially when there are complex relationships between jobs. Copilot in Dynamics 365 Customer Insights provides a simple, natural language summary of the environment, prominently highlighting the most important jobs tied to key activation events like exports. With this summary, admins can focus on quickly taking the actions required.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/address-issues-environment-status-summary-copilot)
- [Documentation](system.md#environment-status-summary-preview)

### Monthly enhancements

[Marketing Contributor role](user-roles.md#marketing-contributor-preview):

- can search for segments by name and only get results from their business unit
- can filter by tags and tags honor business unit. Tags created in a business unit aren't visible and searchable in other business units
- can customize the columns they see in their business unit-specific view of the segment list
- can download a segment

### New blogs and scenario docs

- [Advanced unification scenario: Create unified customer profiles from functionally unrelated sources](https://community.dynamics.com/blogs/post/?postid=cbf1def2-2a94-4a4d-9535-0489e647157c)

- [Unlocking the power of Dynamics 365 Customer Insights: Best practices for data modeling and data quality](https://community.dynamics.com/blogs/post/?postid=988fae7a-3f37-ee11-bdf4-6045bdebe084)

- [Navigating the data platform landscape: Azure Synapse or Microsoft Fabric](https://community.dynamics.com/blogs/post/?postid=4c923e38-8738-ee11-bdf4-000d3a4e511f)

## June 2023

### Display activities in a Dynamics 365 activity timeline

A single view of all interactions enables a complete understanding of customer activity. With that context, sellers and representatives can create deeply personalized experiences for digital and nondigital channels. In Dynamics 365 Sales, Customer Service, and Customer Insights - Journeys, users can see all activities in the unified activity timeline.

After a Dynamics 365 administrator enables the feature, sellers and representatives can view activities directly in the activity timeline. Dynamics 365 apps and Customer Insights - Data must share a Dataverse environment.

Activity data can appear within the same activity timeline already used today to add or view activities such as notes, posts, emails, and appointments. The unified activity timeline is available across *Accounts* and *Contacts*.

Activities within the Dynamics 365 activity timeline can be filtered, searched, and updated dynamically.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/display-customer-insights-activities-dynamics-365-activity-timeline)
- [Documentation](activities-in-d365-timeline.md)

## May 2023

### Generate insights by asking questions in natural language with Copilot in Customer Insights - Data

Copilot in Dynamics 365 Customer Insights - Data is powered by AI to provide you with insights that answer your questions. In an easy and accelerated manner, you can have a dialogue with your data. Ask questions using natural language to explore, analyze, and understand customer segment sizes and preferences. Analysts and marketers can engage directly with customer data and discover new information that they might not have been aware of.

This feature democratizes access to insights, allowing analysts, marketers, and sellers to ask questions using conversational language and receive instant answers, without needing to have the knowledge of SQL programming. Copilot removes the barriers to getting a deeper understanding of customers, enabling users to speed up and scale the delivery of hyper-personalized experiences that customers expect.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/generate-insights-asking-questions-natural-language-copilot-customer-insights)
- [Documentation](dialog-with-data.md)

### Unify your B2B account and contact data into easy to work with related tables that also support commercial contacts with unknown accounts  

Get a 360-degree view of your B2B contacts by creating unified contact profiles. With this release, your B2B contacts can be unified just like accounts and customers. The unified accounts table and unified contacts table share a simple relationship, allowing you to easily create segments of contacts that have specific account attributes. In addition, you can now identify and engage business contacts where the account is unknown, to discover and create new account relationships.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/gain-360-degree-view-b2b-contacts-leveraging-all-fields-unified-contacts)
- [Documentation](b2b/data-unification-contacts.md)

### Bring your custom prediction models from Azure Synapse Analytics into Dynamics 365 Customer Insights - Data, using our Synapse pipeline integration

Now you can utilize your existing custom models in Synapse with routinely refreshed, high-quality unified customer and transaction data to supercharge your next marketing or sales campaign.

- [Release plan](/dynamics365/release-plan/2023wave1/customer-insights/easily-connect-custom-prediction-models-guided-steps)
- [Documentation](custom-models.md)

### Get an enhanced experience for custom prediction models in Dynamics 365 Customer Insights - Data with a user-friendly wizard

Users can easily and quickly bring custom prediction models from Azure Machine Learning or Azure Synapse Analytics into Customer Insights - Data with a simple 5-step wizard that walks them through establishing a connection, addition of an AI/ML workflow, configuration of model parameters, setup of required data, and reviewing and running the model.

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
> Currently, this feature is available for customers in the United States only.

This first run experience (FRE) feature helps you recognize the value of Dynamics 365 Customer Insights - Data faster. Onboarding a new application can be time-consuming and tricky, leaving room for error and leaving you questioning the value it can bring. This feature saves you precious time and takes the guesswork out of setting up your data correctly the first time you use Customer Insights - Data. It works in trial and paid environments and allows you to get valuable insights faster. Use those insights to fuel better customer experiences and drive a higher return on investment.

After an admin successfully creates your initial environment, the FRE guides you through three easy steps:

1. Provide data: You're prompted to upload your data file (must be a CSV file containing more than 100 rows and 5 columns).
2. Get data checked: Use AI-driven models, your data is automatically validated and quality-checked—no manual configuration required.
3. Receive insights: The system identifies business value by deriving patterns and insights from your data file, such as segments and measures.

This FRE works with a single CSV file only. If you have multiple data files, or different data sources, [Customer Insights - Data provides connections to a broad set of sources](data-sources.md).

- [Release plan](/dynamics365-release-plan/2022wave2/customer-insights/generate-insights-minutes-first-run-experience)

## January 2023

### Achieve business scenarios with application lifecycle management

Dynamics 365 Customer Insights - Data starts supporting application and environment lifecycle management capabilities for common enterprise-grade requirements. For example, you can copy, reset, or delete your Customer Insights - Data environments. Additionally, the system ensures your Customer Insights - Data environment and the associated Dataverse environment are always in sync.

- [Release plan](/dynamics365-release-plan/2022wave2/customer-insights/achieve-business-scenarios-application-lifetime-management)
- [Documentation](manage-environments.md#copy-the-environment-configuration-preview)

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
