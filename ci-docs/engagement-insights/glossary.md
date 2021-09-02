---
title: Customer insights glossary of terms
description: Glossary of terms and concepts for Customer Insights and capabilities.
author: mochimochi016
ms.reviewer: mhart
ms.author: jefhar
ms.date: 08/31/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Customer insights glossary of terms

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This topic defines selected terms that appear in Dynamics 365 Customer Insights, its capabilities, and in the supporting documentation.

## Activity data

Customers' activity data that is ingested to Customer Insights. Examples of activity data include transactions, support call duration, purchases, and returns. For tracking of demographic segments, activity data gets analyzed for recency, frequency, and monetary value (and duration).

## Affinity 

Affinities are customer preferences for brands and interests across various demographic
segments (defined by age, gender, or location).The online search volume for a brand or interest determines how much affinity a demographic segment,compared to other segments, has to that brand or interest.

## Attribute

Attributes are custom semantic types that you set during the data unification process. You can only specify attributes that exist in Customer Profile entities that you've created. Attribiutes that aren't automatically mapped to a semantic type are grouped as unmapped fields.

## Base event

A base event is a set of data representing activity on a website, such as a page view or click. See also *refined event*.

## Connections

Connections are used to configure third-party enrichments, which admins set up with credentials and provides consent for data transfers. See also *enrichment*.

## Custom model

Custom models let you create and manage workflows based on Azure Machine Learning models.

## Data ingestion

Data ingestion is the process of connecting to a data source. After ingesting the
data, you can unify and take action on it.

## Dimensions

Dimensions are attributes of events that can describe, filter, or group data. For example, you can select *operating system (OS)*, *browser*, or *page name* as a dimension in a report. See also *attribute* and *event*.

## Enrichment (of data)

Data enrichment refers to the process of appending or enhancing collected data with relevant context obtained from additional sources.

## Entity 

An entity in Customer Insights contains activity data. For example, the *UnifiedActivity* entity contains data for a specific activity. The entity that you choose as your primary entity serves as the basis for your unified profiles dataset.

## Environment

 An environment is a space that can contain one or more workspaces. You can use an environment to manage your workspaces and connections to Customer Insights audience insights capability. See also *workspace*.

## Event

An event represents user behavior in digital analytics. An event records when a user views a page (view event) or interacts with content (action event). Activity data from your website is captured as *base events*. For reporting, you can decide the properties of the data that you want display. This virtual view of the data is called a *refined event*. 

## Funnel report

A funnel report collects information about the *steps* that occur during a customer journey through your website or mobile app, and provides data to inform decisions and identify areas for optimization. For example, you can create a funnel report to identify paths your customers take before they make a purchase, to identify areas for process improvements.

## Member

A member of a workspace is a user who can access a workspace. Members can have roles, which allow the user to manage the workspace, its data, and view reports. Currently, *Owner* is the only role available in engagement insights capability.

## Metric

A metric is a quantifiable measurement of data used to track or assess a process. Page views and average time spent on site are examples of relevant metrics.

## Prediction

Predictions help you better understand what customers are interested in purchasing. They can also help organizations improve business revenue and build customer loyalty through personalization and engagement. For example, using your own data, you can create predictions for what products your customers are likely to purchase in the future.

## Real-time usage

Real-time usage provides an overview of current activity in your mobile app that automatically refreshes every minute. Use real-time usage to monitor the number of users and sessions currently active in your app and the top screen views.


## Refined event

A refined event is a virtual view of a base event filtered by specific properties of the data. Use refined events to simplify a base event for export or to remove properties from an event that aren't necessary for exposure or export. See also *base event*.

## Relationships

Relationships connect entities to define a graph of your data when entities share a common identifier, or a foreign key. You can reference foreign keys from one entity to another. Relationship-connected entities enable you to define segments and measures based on multiple data sources.

## Report

A report is a collection of data visualizations that help you measure and understand user behavior. Engagement insights capability includes several predefined reports for web projects. You can also create custom reports. 

## Return frequency

Return frequency groups user session counts by the number of days since the user's last session.

## Screen view

Screen views list screen views for individual screens in an app and thetotal number of screen views. You can view screen views by screen name or by screen title.

## Segment

A segment is a set of specific demographic characteristics (such as defined by age, gender, location, and so on). For example, you can map fields from your unified customer entity to define the demographic segment you want the system to use for enriching your customer data.

## Unification (of data)

The data unification process lets you unify once-disparate data sources into a single master dataset that provides a unified view of your customers. After setting up data sources, you can unify the data in three mandatory steps: Map, Match,and Merge.

## Visitor

A visitor is a customer who visits your website or mobile app. Visits refers to visitor information, including the number of visits and the visit duration, to inform you about new and individual and returning visitors to your site.

## Workspace

A workspace is where you store and manage events and reports. You can also view user activity in real time. When you create a workspace, you select the type of data you will send to the workspace.



[!INCLUDE[footer-include](../includes/footer-banner.md)]