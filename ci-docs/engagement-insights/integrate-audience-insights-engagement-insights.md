---
title: Create a link between audience insights and engagement insights
description: Create an active link between audience insights and engagement insights to enable bidirectional sharing of data.
ms.date: 09/08/2021
ms.service: customer-insights
ms.topic: conceptual
author: mkisel
ms.author: mkisel
ms.reviewer: mhart
manager: shellyha
---

# Create a link between audience insights and engagement insights

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

The integration between engagement insights and audience insights links environments from both capabilities, and enables data to be shared bidirectionally between them.

Use unified profiles and segments from audience insights for more analysis options in engagement insights. Export events that have a high business value from engagement insights. Use these events to add data to unified profiles in audience insights.

## Prerequisites

- Audience insights profiles must be stored in an Azure Data Lake Storage account that you own, or in a [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro.md)&ndash;managed data lake. 

- You need administrator permissions for both the engagement insights and audience insights environments.

- Linked environments must be in the same geographical region.

> [!NOTE]
> - If your audience insights subscription is a trial, which uses an audience insights internally managed data lake, contact [pirequest@microsoft.com](mailto:pirequest@microsoft.com) for assistance. 
> - If your audience insights environment uses your own Azure Data Lake Storage to store data, you need to add an engagement insights Azure service principal to your storage account. For details, go to [Connect to an Azure Data Lake Storage account with an Azure service principal for audience insights](../audience-insights/connect-service-principal.md). 
> - Your audience insights environment should have an associated Dataverse environment. And if that environment is also using Dataverse for data storage, make sure you check the **Enable data sharing** option in audience insights. For more information, see [Create and configure a paid environment in audience insights](../audience-insights/get-started-paid.md).

## Create an environment link

You can create an environment link by updating the **Admin** > **Environment** settings in engagement insights.

**To establish an active link between audience insights and engagement insights**

1. On the **Environment admin** page, select the **Link environments** tab.

    :::image type="content" source="media/integrate1.png" alt-text="Set up an environment.":::

1. Select **Setup environments** in the upper-left corner or at the bottom of the screen.

     :::image type="content" source="media/integrate2.png" alt-text="Select an audience insights environment.":::

1. Select an audience insights environment, and then select ***Next** to finish. Now you can select optional features for the linked environments.
 
## Enable audience insights unified profiles attributes and segments

After linking environments, you can select optional features for the linked environments. These features enable unified profile attributes and segments from audience insights for interactive analysis on customer data.

**To analyze web data in engagement insights**

1. On the **Environment admin** page, turn on the **Share data from audience insights with engagement insights** toggle, and then select **Next**.

    :::image type="content" source="media/integrate4.png" alt-text="Select features.":::

1. Select the attributes of the unified profiles that will become dimensions in engagement insights. (Not all attributes are useful dimensions. For example, it's not likely that you'd need **First name** or **Last name** as an attribute for analysis of your website events.)

    :::image type="content" source="media/integrate5.png" alt-text="Curate dimensions.":::

   >[!NOTE]
   > All audience insights profile attributes that represent identifiers (such as **ID** and **alternate ID**) are filtered out of the available attributes and become dimensions in engagement insights.

1. When you're done selecting attributes, select **Next**.
1. Add users who can view the audience insights profile dimensions and segments in engagement insights.

    :::image type="content" source="media/integrate6.png" alt-text="Manage access to customer data.":::

   > [!IMPORTANT]
   > If you don't explicitly add users in this step, the data will be hidden from users in engagement insights.

1. Review your selection, and then select **Finish**.

    :::image type="content" source="media/integrate7.png" alt-text="Review customer data settings.":::

## Export refined events to audience insights

After you create a link between environments, you can export refined events from engagement insights to audience insights and ingest them as a new data source. 

For more information, go to [Integrate web data from engagement insights with audience insights](../audience-insights/integrate-engagement-insights.md).

<!--
## Share engagement insights refined events with audience insights

After you create a link between environments, a new option becomes available for you to share [refined events](refined-events.md) with audience insights.

Consider the following when creating refined events for audience insights: 

- Provide a meaningful name for the refined event. It will be used as an activity name in audience insights.
- Select at least the following properties to create an activity in audience insights: 
    - Signal.Action.Name indicates the activity details.
    - Signal.User.Id maps with the customer ID.
    - Signal.View.Uri is a web address as a basis for segments or measures.
    - Signal.Export.Id is a primary key for events.
    - Signal.Timestamp determines the date and time for the activity.

To share refined events:

1. From the engagement insights menu, select **Data** and then select the **Events** tab.
2. On the **Action** menu, select **Share as activity**.

    :::image type="content" source="media/integrate8.png" alt-text="Data shared events settings.":::

3. You can view and stop actively shared events on the **Export and Sharing** tab.
4. -- per Michael K, we need a mock here (Mukesh needs to update to reflect what happens in AUI once a user shares a refined event (i.e. no longer AUI, data wrangler needs to go discover data in the storage, the shared event is available as a DS and entity, correct?)

### Attach refined events shared as activities to unified profiles in audience insights

You can bring customer web activity data from engagement insights into audience insights. In addition to transactional, demographic, or behavioral data, you can view activities on the web in unified customer profiles. You can then use these profiles to get insights such as segments, measures, and predictions for audience activation.

Follow the steps in [data unification](../audience-insights/data-unification.md) to map, match, and merge website authentication information to unified profiles in audience insights.

You can also share refined events that are now available in audience insights, identified as data sources and entities. 

Next, you can relate event data from engagement insights as unified activities in customer profiles.

### Relate refined event data as an activity of a customer profile

After unifying the data, you can configure the activity for the customer profile. For more information, go to [Customer activities](../audience-insights/activities.md).

:::image type="content" source="media/web-event-activity.png" alt-text="Activities page with expanded Edit activity pane.":::

Next, configure the new activity by using mapping elements: 

- **Primary Key**: Signal.Export.Id, a unique ID that is available for every event record in engagement insights. This property is automatically generated.

- **Timestamp**: Signal.Timestamp in the event property.

- **Event**: Signal.Name, the event name that you want to track.

- **Web address**: Signal.View.Uri that refers to the URI of the page that created the event.

- **Details**: Signal.Action.Name to represent the information to associate with the event. The selected property in this case indicates that the event is for email promotion.

- **Activity type**: In this example, we choose the existing activity type WebLog. This selection is a useful filter option to run prediction models or create segments based on this activity type.

- **Set up relationship**: This important setting ties the activity to existing customer profiles. **Signal.User.Id** is the identifier configured in the SDK to be collected. It relates to the user ID in other data sources that are configured in audience insights. 

This example configures the relationship between Signal.User.Id and RetailCustomers:CustomerRetailId, which is the primary key that was identified in the map step of the data unification process.

After processing the activities, you can review customer records and open a customer card to see activities from engagement insights in the timeline. 

> [!TIP]
> To find a customer ID that has an engagement insights activity, go to **Entities** and preview the data for the UnifiedActivity entity. **ActivityTypeDisplay = WebLog** contains the engagement insights activity configured in the preceding example. Copy the customer ID for one of those records and search<!--note from editor: Edit okay? I couldn't quite follow this.-- > for that ID on the **Customers** page.

--> 

[!INCLUDE[footer-include](../includes/footer-banner.md)]
