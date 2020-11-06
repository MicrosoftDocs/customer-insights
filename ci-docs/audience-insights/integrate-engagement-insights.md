---
title: Integrate web data from engagement insights with audience insights.
description: Bring web information about customers to fomr engagement insights to audience insights. 
ms.date: 11/06/2020
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: mukeshpo
manager: shellyha
---

# Integrate web data from engagement insights with audience insights

With customers doing their day to day transactions often online, it's helpful to use the engagement insights capability and integrate web data as a source. In addition to transactional, demographic, or behavioral data we can see activities on the web in a unfied customer profile. We can use this profile to gain additional insights like segments, measures, or predictions for audience activation.

This article describes the steps to bring your customers’ web activity data from engagement insights into your existing audience insights environment.

For this example, we assume an environment that contains customer profiles that were unified with sources from surveys, retail sales, and a ticketing system. It also shows the activities that the customer has performed. 

We now want to know if a customer visits our web properties and understand their activities, such as visiting a website or viewing a product page thru a link that was sent in email.

![](media/b25feeac3fc13186fe2c8bed65930da5.png)


## Prerequisities

To integrate data from engagment insights, a few prerequisites need to be met: 

- Integrate the engagement insights SDK with your website. For more information, see [Get started with the web SDK](../engagement-insights/instrument-website.md).
- Exporting web events from engagement insights requires access to an ADLS Gen 2 storage account that will be used to ingest the web events data to audience
    insights. For more information, see [Export events](../engagement-insights/export-events.md).

## Configure refined events in engagement insights

After instrumenting a website with the engagement insights SDK, *base events* are gathered when a user views a web page or does an action by clicking a property. Base events tend to contain a lot of detais. Depending on your use case, you only need a subset of the data in a base event. Engagement insights lets you create *refined events* that contain only the properties of a base event that you select.     

For more information, see [Create and modify refined events](../engagement-insights/refined-events.md).

Considerations when creating refined events: 

- Provide a meaningful name for the refined event. It's be used as an activity name in audience insights.
- Select at least the following properties to create an activity in audience insights: 
    - Signal.Action.Name - indicating the activity details
    - Signal.User.AuthId - used to map with the customer ID
    - Signal.Action.View.Uri - used as a web address as a basis for segments or measures
    - Signal.Export.Id - to use as a primary key for events <!-- system generated, do we need to list?-->
    - Signal.Timestap - to determine the date and time for the actvity

Select the filters to focus on the events and pages that matter for your use case. In this example, we'll use the "Email promotion" action name.

## Export the Refined Web Events 

After defining the refined event is defined, you have to configure the export of the event data. Exports happen constantly as the events flow from the web property.

For more information, see [Export events](../engagement-insights/export-events.md).

## Ingest event data to audience insights

Now that you have defined the refined event and configured its export, we move on to ingesting the data to audience insights. First, you need to create a new data sources based on a Common Data Model folder. Enter the details for the storage account you export the events to. In the default.cdm.json file, select the refined event to ingest and create the entity in audience insights.

For more information, see [Connect to a Common Data Model folder using an Azure Data Lake account](connect-common-data-model.md)


## Relate refined event data as an activity of a customer profile

After completing the entity ingestion, you can configure the activity for the customer profile.

For more information, see [Customer activities](activities.md).

Configure the new activity with the following mapping: 

- **Primary Key:** Signal.Export.Id, a unique id that is available for every event record in engagement insights. This property is automatically generated.

- **Timestamp:** Signal.Timestamp in the event property.

- **Event:** Signal.Action.Name, the event name that you want to track.

- **Web address:** Signal.Action.View.Uri referring to the uri of the page that created the event.

6.  **Details:** This is the info that you want to associate with the event. Here I have selected Signal.Action.Name as that’s the property which indicates that the event is for Email Promotion.

7.  **Activity Type:** As this is a web activity, I have selected WebLog. This would be useful during the activation or when you are looking to filter for runing any AI/ML models or creating weblog based segments, etc.

8.  **Relationship:** This is the key part that will tie the data to the existing customer profile. As I mentioned at the time of defining the event properties, the Signal User Id is what user identifier was configured in the SDK to be collected and that relates to the user id in other data sources that are configured in Audience insights. So here we are configuring the relationship between Signal User Id and Retail Customers primary key which is CustomerRetailId defined in the Map during Unification.

    Once you save, this finishes the setup of the Activities, and then you can Run the activities.

>   Once the Activities have finished processing, you should be able to check
>   the Customers and can find that the Customer Card shows the activities from
>   Engagement insights.


>   TIP: To find a customer id that has an Engagement insights activity, you can
>   check the Entities page and preview the data for UnifiedActivity entity. The
>   entity with ActivityTypeDisplay = WebLog will be the one with the
>   EngagementInsights activity as we just configured. You can copy the
>   customerid for one of those records and find that customer using the search
>   option on the Customers page.

## Next Steps

With this unified customer profile built with the data integrated from
Engagement insights with Audience insights, now you can further create more
powerful segments (\<\<fwlink\>\>), measures (\<\<fwlink\>\>) and predictions
(\<\<fwlink\>\>) to make a meaningful connection with your customers.
