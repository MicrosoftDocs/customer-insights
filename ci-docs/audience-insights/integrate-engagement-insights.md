---
title: Integrate web data from engagement insights with audience insights
description: Bring web information about customers from engagement insights to audience insights. 
ms.date: 12/17/2020
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: mukeshpo
manager: shellyha
---

# Integrate web data from engagement insights with audience insights

Customers often do their day to day transactions online using web sites. The engagement insights capability in Dynamics 365 Customer Insights is a handy solution to integrate web data as a source. In addition to transactional, demographic, or behavioral data we can see activities on the web in unified customer profiles. We can use this profile to gain additional insights like segments, measures, or predictions for audience activation.

This article describes the steps to bring your customers’ web activity data from engagement insights into your existing audience insights environment.

In this example, we assume an environment that contains unified customer profiles. The profiles were unified with sources from surveys, retail sales, and a ticketing system. It also shows the related activities of the customers. 

We now want to know if a customer visits our web properties and understand their activities. Activities include, for example, visited websites or viewed product pages from a link received in an email.

## Prerequisites

To integrate data from engagement insights, a few prerequisites need to be met: 

- Integrate the engagement insights SDK with your website. For more information, see [Get started with the web SDK](../engagement-insights/instrument-website.md).
- Exporting web events from engagement insights requires access to an ADLS Gen 2 storage account that will be used to ingest the web events data to audience insights. For more information, see [Export events](../engagement-insights/export-events.md).

## Configure refined events in engagement insights

After an administrator instrumented a website with the engagement insights SDK, *base events* are gathered when a user views a web page or clicks somewhere. Base events tend to contain numerous details. Depending on your use case, you only need a subset of the data in a base event. Engagement insights let you create *refined events* that contain only the properties of a base event that you select.     

For more information, see [Create and modify refined events](../engagement-insights/refined-events.md).

Considerations when creating refined events: 

- Provide a meaningful name for the refined event. It's be used as an activity name in audience insights.
- Select at least the following properties to create an activity in audience insights: 
    - Signal.Action.Name - indicating the activity details
    - Signal.User.Id - used to map with the customer ID
    - Signal.View.Uri - used as a web address as a basis for segments or measures
    - Signal.Export.Id - to use as a primary key for events <!-- system generated, do we need to list?-->
    - Signal.Timestamp - to determine the date and time for the activity

Select the filters to focus on the events and pages that matter for your use case. In this example, we'll use the "Email promotion" action name.

## Export the Refined Web Events 

After defining the refined event is defined, you have to configure the export of the event data to an Azure Data Lake Storage, that can be set as a data source for ingestion in audience insights. Exports happen constantly as the events flow from the web property.

For more information, see [Export events](../engagement-insights/export-events.md).

## Ingest event data to audience insights

Now that you have defined the refined event and configured its export, we move on to ingesting the data to audience insights. You need to create a new data source based on a Common Data Model folder. Enter the details for the storage account you export the events to. In the *default.cdm.json* file, select the refined event to ingest and create the entity in audience insights.

For more information, see [Connect to a Common Data Model folder using an Azure Data Lake account](connect-common-data-model.md)


## Relate refined event data as an activity of a customer profile

After completing the entity ingestion, you can configure the activity for the customer profile.

For more information, see [Customer activities](activities.md).

:::image type="content" source="media/web-event-activity.png" alt-text="Activities page with expanded Edit activity pane and filled in fields.":::

Configure the new activity with the following mapping: 

- **Primary Key:** Signal.Export.Id, a unique ID that is available for every event record in engagement insights. This property is automatically generated.

- **Timestamp:** Signal.Timestamp in the event property.

- **Event:** Signal.Name, the event name that you want to track.

- **Web address:** Signal.View.Uri referring to the uri of the page that created the event.

- **Details:** Signal.Action.Name to represent the information to associate with the event. The selected property in this case indicates that the event is for email promotion.

- **Activity type:** In this example, we choose the exsting activity type WebLog. This selection is a useful filter option to run prediction models or create segments based on this activity type.

- **Set up relationship:** This important setting ties the activity to existing customer profiles. **Signal.User.Id** is the identifier configured in the SDK to be collected and that relates to the user ID in other data sources that are configured in audience insights. In this example, we configure the relationship between Signal.User.Id and RetailCustomers:CustomerRetailId, which is the primary key that was deinfed in the map step of the data unification process.


After processing the activities, you can review customer records and open a customer card to see activities from engagement insights in the timeline. 

> [!TIP]
> To find a customer id that has an engagement insights activity, go to **Entities** and preview the data for the UnifiedActivity entity. ActivityTypeDisplay = WebLog contain the engagement insights activity configured in the example above. Copy the customer ID for one of those records and for that ID on the **Customers** page.

## Next Steps

You can now create [segments](segments.md), [measures](measures.md), and [predictions](predictions.md) to make a meaningful connection with your customers.


[!INCLUDE[footer-include](../includes/footer-banner.md)]