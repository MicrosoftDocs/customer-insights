---
title: Create a link between audience insights and engagement insights
description: Create an active link between audience insights and engagement insights to enable bi-directional sharing of data.
ms.date: 07/22/2021
ms.service: customer-insights
ms.topic: conceptual
author: mkisel
ms.author: mkisel
ms.reviewer: mhart
manager: shellyha
---

# Create a link between audience insights and engagement insights

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Engagement and audience insights integration delivers an easy linkage between environments, enabling bi-directional sharing of data between audience insights and engagement insights. 

You can use unified profiles and segment data from audience insights for analysis of behavioral web activities in engagement insights. You can also share events that have a high business value from engagement insights and enrich unified profiles stored in audience insights.

## Prerequisites

For the self-service enablement of this feature to work properly, the source of the audience insights profiles is to be stored in an Azure Data Lake Storage (ADLS gen 2) account owned by a customer or in a [Dataverse](/powerapps/maker/data-platform/data-platform-intro.md) managed lake. 

To link environments, you need administrator permissions for both engagement insights and audience insights environments.

Linked environments must have the same type (production or sandbox) and the same geographical region.

> [!NOTE]
> - If your audience insights subscription is a trial, which uses an audience insights internal managed data lake, contact [pirequest@microsoft.com](mailto:pirequest@microsoft.com) for assistance. 
> - If your audience insights environment uses your own Azure Data Lake Storage to store data, you need to add an engagement insights Azure service principal to your storage account. For details, see [Connect to an Azure Data Lake Storage Gen2 account with an Azure service principal for audience insights](../audience-insights/connect-service-principal.md). 

## Create an environment link

You can create an environment link by updating the **Admin > Environment** settings in engagement insights.

To establish an active link between audience insights and engagement insights:

1. Navigate to the **Enviromment admin** page, then go to the **Link environments** tab.

   ![Setup environment](media/integrate1.png "Setup environment")

2. Select **Setup environments** at the top left or bottom link on the screen.

   ![Select audience insights environment](media/integrate2.png "Select audience insights environment")

2. Select an audience insights environment, and then **Next** to finish. Now you can select optional features for the linked environments.
 
## Enable audience insights unified profiles attributes and segments

After creating a link between environments, a new option becomes available to select optional features in the linked environments. These features enable unified profile attributes and segments from audience insights to perform interactive analysis on customer data.

To analyze web data in engagement insights: 

1. In the **Enviromment admin** page, change the toggle for **Share data from audience insights with engagement insights** to the enabled position, then select **Next**.

   ![Select features](media/integrate4.png "Select features")

2. Select the attributes of the unified profiles that will become dimensions in engagement insights. (Not all attributes are useful dimensions. For example, it’s not likely that you would need “First name” or “Last name” as an attribute for analysis of your website events.)

   ![Curate dimensions](media/integrate5.png "Curate dimensions")

3. When you're done selecting attributes, click **Next**.
4. Add users who can view the audience insights profile dimensions and segments in engagement insights.

   ![Manage access to customer data](media/integrate6.png "Manage access to customer data")

  > [!IMPORTANT]
  > If you do not explicitly add users in this step, the data will be hidden from users in engagement insights.

5. Review your selection and click **Finish**.

   ![Review customer data settings](media/integrate7.png "Review customer data settings")

<!--
## Share engagement insights refined events with audience insights

Once you create a link between environments, a new option becomes available to share [refined events](refined-events.md) with audience insights.

Considerations when creating refined events for audience insights: 

- Provide a meaningful name for the refined event. It will be used as an activity name in audience insights.
- Select at least the following properties to create an activity in audience insights: 
    - Signal.Action.Name – indicates the activity details.
    - Signal.User.Id – used to map with the customer ID.
    - Signal.View.Uri – used as a web address as a basis for segments or measures.
    - Signal.Export.Id – used as a primary key for events.
    - Signal.Timestamp – determines the date and time for the activity.

To share refined events:

1. From the engagement insights menu, select **Data** and then **Events** tab.
2. From the **Action** menu, select **Share as activity**.

   ![Data shared events settings](media/integrate8.png "Data shared events settings")

3. You can view and stop actively shared events in the **Export and Sharing** tab.
4. -- per Michael K, we need a mock here (Mukesh needs to update to reflect what happens in AUI once a user shares a refined event (i.e. no longer AUI, data wrangler needs to go discover data in the storage, the shared event is available as a DS and entity, correct?)

### Attach refined events shared as activities to unified profiles in audience insights

You can bring customer web activity data from engagement insights into audience insights. In addition to transactional, demographic, or behavioral data, you can view activities on the web in unified customer profiles. You can then use these profiles to get insights, such as segments, measures, and predictions for audience activation.

Follow the steps in [data unification](../audience-insights/data-unification.md) to map, match, and merge website authentication information to unified profiles in audience insights.

You can also share refined events that are now available in audience insights, identified as data sources and entities. 

Next, you can relate event data from engagement insights as unified activities in customer profiles.

### Relate refined event data as an activity of a customer profile

After unifying the data, you can configure the activity for the customer profile. For more information, see [Customer activities](../audience-insights/activities.md).

![Activities page with expanded Edit activity pane](media/web-event-activity.png "Activities page with expanded Edit activity pane")

Next configure the new activity with mapping elements: 

- **Primary Key**: Signal.Export.Id, a unique ID that is available for every event record in engagement insights. This property is automatically generated.

- **Timestamp**: Signal.Timestamp in the event property.

- **Event**: Signal.Name, the event name that you want to track.

- **Web address**: Signal.View.Uri referring to the URI of the page that created the event.

- **Details**: Signal.Action.Name to represent the information to associate with the event. The selected property in this case indicates that the event is for email promotion.

- **Activity type**: In this example, we choose the existing activity type WebLog. This selection is a useful filter option to run prediction models or create segments based on this activity type.

- **Set up relationship**: This important setting ties the activity to existing customer profiles. **Signal.User.Id** is the identifier configured in the SDK to be collected and that relates to the user ID in other data sources that are configured in audience insights. 

This example configures the relationship between Signal.User.Id and RetailCustomers:CustomerRetailId, which is the primary key that was identified in the map step of the data unification process.

After processing the activities, you can review customer records and open a customer card to see activities from engagement insights in the timeline. 

> [!TIP]
> To find a customer ID that has an engagement insights activity, go to **Entities** and preview the data for the UnifiedActivity entity. *ActivityTypeDisplay = WebLog* contains the engagement insights activity configured in the example above. Copy the customer ID for one of those records and for that ID on the **Customers** page.

--> 

[!INCLUDE[footer-include](../includes/footer-banner.md)]
