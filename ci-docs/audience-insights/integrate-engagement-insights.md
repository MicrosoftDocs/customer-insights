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

- Integrate Engagement insights SDK with your website. For more information, see 
- Exporting the refined web events requires access to an ADLS Gen 2 storage
    account that you would use for ingesting the web events data in Audience
    insights.

# Setting up Engagement insights

1.  Define Refined Web Events

    With the web page wired up with Engagement insights, now you can go to the
    workspace to define the Refined Events for integrating into Audience
    insights. \<\<fwlink\>\> overview.

    ![Graphical user interface, application Description automatically generated](media/b0751d1a46735d7509039a7dcdf4f16c.gif)

2.  Create Refined Event by selecting “New events”.

3.  Select a Base event and provide a meaningful name to the refined event.

    TIP: Specify the Name of the event that you would want to see as an Activity
    Name.

4.  Select the properties that you want to use to relate in the Audience
    insights.

    I have selected the following minimum required properties to setup an
    Activity to relate to a profile:

-   “Signal Action Name” which indicates the Activity Details i.e. Email
    Promotion.

-   “Signal User AuthId” which I can join back to the contact ids of my
    RetailCustomers entity in Audience insights.

-   “Signal Action View Uri” which I could use to map to the Web address, that I
    may chose to segment or create a measure on.

-   Signal Export Id is a pre-selected field that is a primary key for all the
    events that get captured.

-   Signal timestamp is a pre-selected field that will always be present to
    indicate when that event has happened and you will definitely need that on
    the activity timeline.

1.  Select the filters:

-   Note that I have filtered the Signal Action Name to “Email Promotion” to be
    laser focused on what activity I am setting up this export for. While you
    can skip the filtering, but that would not be a good choice, as you could
    end up bringing even a cursor up down or page up down as an event across 50+
    products.

-   Similarly, I have filtered the Signal View Title to be able to filter on the
    very specific page that I am interested to track.

## Export the Refined Web Events 

>   After the Refined Event is defined, now you can setup the export of data
>   that will be exported on an ongoing basis as the events are collected from
>   the web application. \<\<fwlink\>\> overview.

![](media/a2f368f4fbe2f2eaf5546b20aab622fd.gif)

>   Graphical user interface, application Description automatically generated

1.  Start with a New Export

2.  Select the Refined Events to export: here we select “StartPageClicks” as
    defined in the previous step.

3.  There is an option to select the file structure which indicates how the data
    will be stored.

4.  Next, Select “Common Data Model” as that’s what enables Audience insights to
    discover the event table as a data source.

5.  Provide an ADLS Gen 2 account storage location and account key to store the
    event data to be exported.

6.  Provide the folder path, also sometimes referred to as a container. If you
    want to create a sub folder in the container you can specify that as folder
    path. If a folder does not exist, the export will create one.

# Setting up Audience insights

## Ingest Events data from Engagement insights

>   Now that you have defined and setup the export of the Refined Event, you can
>   now discover it and integrate it with Audience insights. The first step here
>   is to setup as a data source.

![](media/54a1a821ed8ddb6aa25369d8f55d214d.gif)

>   Graphical user interface, application Description automatically generated

1.  In your existing environment, add a new Data Source.

2.  Select the import method as “Connect to a Common Data Model Folder” and name
    the data source.

3.  Provide the ADLS Gen 2 storage location that was setup at the time of export
    in Engagement insights.

4.  You should be able to see the default.cdm.json. You should be able to select
    the one for the events that you have configured for your scenario.

5.  You should see the event and as the entity and you can click Save.

    This completes the setup of the ingesting the Events Data.

    The data source will show as Refreshing on the Data Sources page. Since this
    is attaching a CDM folder, the refreshing state would not take long. Once
    the refreshing is complete, you can proceed to relating the events data as
    an Activity.

## Relate the Events data as an Activity of a Customer Profile

>   Now that the entity ingestion is complete, you should be able to configure
>   the events to the customer profile.

![](media/9e57473b5f0fb63bee52dca75c0668e2.png)

1.  You can add an Activity and select the newly created Entity.

2.  **Primary Key**: Signal.Export.id is a unique id that is always generated
    with every event record in Engagement insights. This property is not visible
    at the time of defining the event as it is system generated.

3.  **Timestamp:** Signal.Timestamp is the timestamp in the events property that
    you would select.

4.  **Event:** This is the Event name that you want to track, I have selected
    Signal.Name as that indicates my page_clicks event.

5.  **Web address:** This is the uri of the page that is for tracking.

6.  **Details:** This is the info that you want to associate with the event.
    Here I have selected Signal.Action.Name as that’s the property which
    indicates that the event is for Email Promotion.

7.  **Activity Type:** As this is a web activity, I have selected WebLog. This
    would be useful during the activation or when you are looking to filter for
    runing any AI/ML models or creating weblog based segments, etc.

8.  **Relationship:** This is the key part that will tie the data to the
    existing customer profile. As I mentioned at the time of defining the event
    properties, the Signal User Id is what user identifier was configured in the
    SDK to be collected and that relates to the user id in other data sources
    that are configured in Audience insights. So here we are configuring the
    relationship between Signal User Id and Retail Customers primary key which
    is CustomerRetailId defined in the Map during Unification.

    Once you save, this finishes the setup of the Activities, and then you can
    Run the activities.

>   Once the Activities have finished processing, you should be able to check
>   the Customers and can find that the Customer Card shows the activities from
>   Engagement insights.

![](media/4d7c2a8192b6bf534885bfe87909226e.png)

>   TIP: To find a customer id that has an Engagement insights activity, you can
>   check the Entities page and preview the data for UnifiedActivity entity. The
>   entity with ActivityTypeDisplay = WebLog will be the one with the
>   EngagementInsights activity as we just configured. You can copy the
>   customerid for one of those records and find that customer using the search
>   option on the Customers page.

# Next Steps

With this unified customer profile built with the data integrated from
Engagement insights with Audience insights, now you can further create more
powerful segments (\<\<fwlink\>\>), measures (\<\<fwlink\>\>) and predictions
(\<\<fwlink\>\>) to make a meaningful connection with your customers.
