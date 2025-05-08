---
title: Use segments from Dynamics 365 Customer Insights - Data
description: Learn how to integrate Dynamics 365 Customer Insights - Journeys with Dynamics 365 Customer Insights - Data so you can share data and segments between the two systems.
ms.date: 08/18/2023
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use segments from Dynamics 365 Customer Insights - Data 

Dynamics 365 Customer Insights - Data applies artificial intelligence to analyze rich pools of customer data collected from across other apps like Dynamics 365 Sales, Service, and Customer Insights - Journeys. Its standard functionality generates powerful analytical displays for each contact, which makes the information easy to understand and use. The integrated solution can:

- Load data from Dynamics 365 Customer Insights - Journeys into Customer Insights - Data and combine it with customer data from other sources.
- Apply data cleansing, enrichment, fuzzy matching, and more.
- Use segments created by Customer Insights - Data to target journeys in Dynamics 365 Customer Insights - Journeys.

For complete details, see the [Customer Insights - Data documentation](/dynamics365/customer-insights/overview).

## Prerequisites

Dynamics 365 Customer Insights - Data is a separate product from Dynamics 365 Customer Insights - Journeys. To use the features described in this topic, you must already have a Customer Insights - Data instance available before you can integrate it with Dynamics 365 Customer Insights - Journeys. You can use either a trial or a production license of Customer Insights - Data while to try out the integration, but must eventually purchase a full license if you decide to continue using it.

## Overview: Working with Customer Insights - Data segments in Customer Insights - Journeys

Read this section for an overview of how to work with segments shared between Customer Insights - Data and Customer Insights - Journeys. See the later sections in this topic for detailed instructions.

### Connect Customer Insights - Data to Customer Insights - Journeys to grant access to your contact records

Customer Insights - Data has its own database for holding contact records and other information, and its own tools for working with that information, including tools for creating segments. That means that Customer Insights - Data requires access to your Customer Insights - Journeys database to enable it to work with your marketing contacts. You set this up by adding your Customer Insights - Journeys instance as a data source in Customer Insights - Data.

For complete instructions, see [Add a data source](/dynamics365/customer-insights/data-sources#add-a-data-source) in the Customer Insights - Data documentation.

### Export Customer Insights - Data segments to get them into Customer Insights - Journeys

You bring Customer Insights - Data segments into Customer Insights - Journeys by exporting them. The systems can communicate directly, so once the connection is set up, you'll be able to export segments with just a few clicks in Customer Insights - Data. You set this up by adding your Customer Insights - Journeys instance as an export destination in Customer Insights - Data.

See the later sections of this topic for details about how to set this up.

<a name="refresh"></a>

### Customer Insights - Data segments in Customer Insights - Journeys are mirrored and refreshed periodically

You can configure the frequency of automatic refreshes for Customer Insights - Data segments by changing your system preferences in Customer Insights - Data. For more information, see the [Schedule tab](/dynamics365/customer-insights/audience-insights/system#schedule-tab) topic in the Customer Insights - Data documentation. You can also re-export manually at any time.

Each time a segment in Customer Insights - Journeys is refreshed by Customer Insights - Data, it completely replaces that segment on the Customer Insights - Journeys side. It doesn't do an incremental update, so any customization you have made to the segment using the Customer Insights - Journeys tools will be overwritten.

Even if the segment is live in Customer Insights - Journeys, Customer Insights - Data will still be able to refresh it without stopping the segment.

### Customer Insights - Data segments look like static segments in Customer Insights - Journeys

Segments exported from Customer Insights - Data to Customer Insights - Journeys look like static segments. In Customer Insights - Journeys, you'll be able to see which contacts are in the segment, but not the logical rules used to create the segment in Customer Insights - Data. To modify the query criteria for these segments, you must work in Customer Insights - Data and then allow the systems to sync.

> [!NOTE]
> Static segments in Customer Insights - Journeys look different from segments in Customer Insights - Data. In Customer Insights - Journeys, the **Designer** tab for draft segments displays a list of all contacts in your database, and uses checkboxes to indicate whether or not each listed contact is a member of that segment. For live segments, Customer Insights - Journeys also provides a **Members** tab, which shows only the contacts that are members of the segment. In Customer Insights - Data, you'll just see a list of contacts that are part of the segment.

### Customer Insights - Data segments won't create new contacts in Customer Insights - Journeys

When you export a segment to Dynamics 365 Customer Insights - Journeys, the resulting segment will only contain contacts already in Customer Insights - Journeys that match incoming contact IDs from the Customer Insights - Data segment. Contacts in Customer Insights - Data that have IDs that aren't present in Customer Insights - Journeys (possibly because they came from another data source) will be ignored, so new contacts won't be created in Customer Insights - Journeys.

### Customer Insights - Data segments show details on the General tab in Customer Insights - Journeys

One way to tell whether a segment in Customer Insights - Journeys is being managed by Customer Insights - Data is to open the segment and go to its **General** tab. The following fields here indicate that the segment comes from Customer Insights - Data and provide information about the integration:

- **External source**: Shows a value of "Customer Insights" for segments that came from Customer Insights - Data. This field is blank for segments defined natively in Dynamics 365 Customer Insights - Journeys.
- **External Segment URL**: Shows the URL of the Customer Insights - Data instance where the segment came from. Select the globe button at the edge of this field to open the URL. This field is blank for segments defined natively in Dynamics 365 Customer Insights - Journeys.
- **Description** Shows the date and time the segment was last refreshed by being exported or re-exported from Customer Insights - Data. This field is either blank or holds custom descriptive text for segments defined natively in Dynamics 365 Customer Insights - Journeys.

![A segment from Customer Insights - Data.](media/ci-exported-segment-details.png "A segment from Customer Insights - Data")

### You must go live with your Customer Insights - Data segments to use them in Customer Insights - Journeys

When a new segment arrives in Customer Insights - Journeys from Customer Insights - Data, it will be in the draft state. To use it with a customer journey, you must go live, just as with segments created natively in Customer Insights - Journeys.

Once a segment is live in Customer Insights - Journeys, Customer Insights - Data will still be able to refresh it without stopping the segment.

### Don't edit Customer Insights - Data segments in Customer Insights - Journeys

Though you can use the native tools in Customer Insights - Journeys to add and remove contacts for a segment exported from Customer Insights - Data, you shouldn't do so. Your changes will be overwritten the next time Customer Insights - Data refreshes the segment. Instead, work directly in Customer Insights - Data if you need to modify its exported segments.

## Bring your Customer Insights - Journeys contacts into Customer Insights - Data

To make your Customer Insights - Journeys contacts available in Customer Insights - Data, you must set Customer Insights - Data to use your Customer Insights - Journeys database up as a data source. From Customer Insights - Data, use the **Microsoft Dataverse** data source type to connect to Customer Insights - Journeys and sign in using your usual Customer Insights - Journeys credentials.

![The Common Data Service connector in Customer Insights - Data.](media/ci-data-source-dataverse.png "The Dataverse data source in Customer Insights - Data")

For complete instructions, see [Import data from Dataverse to Customer Insights - Data](/dynamics365/customer-insights/connect-dataverse-managed-lake).

Once your Customer Insights - Journeys instance is connected as a data source, you'll probably also need to _unify_ the data with your Customer Insights - Data customers. For details about this, see the [Data unification](/dynamics365/customer-insights/data-unification) topic in the Customer Insights - Data documentation.

Once the data source is set up, it will continue to work and refresh automatically. Usually, you'll only need to do this once.

## Set your Customer Insights - Journeys app as an export destination in Customer Insights - Data

To make the segments you create in Customer Insights - Data available in Dynamics 365 Customer Insights - Journeys, you must set up your Customer Insights - Journeys instance as an export destination in Customer Insights - Data. You only have to do this once.

To configure your Dynamics 365 Customer Insights - Journeys instance as an export destination in Customer Insights - Data:

1. Sign into Customer Insights - Data.
1. Go to **Data** > **Export destinations**.
1. Select **Add destination** on the command bar.
1. The **Edit destination** dialog opens. Make the following settings:
   - **Type**: Select **Dynamics 365 Customer Insights - Journeys (Segments)**.
   - **Server address**: Enter the full domain name for your Dynamics 365 Customer Insights - Journeys instance.
   - **Server admin account**: Select **Sign in** to open a pop-up window where you can sign into your Dynamics 365 Customer Insights - Journeys instance. Sign in using an account with admin privileges on the Customer Insights - Journeys instance.
   - **Indicate which Customer Insights - Data field matches the Dynamics 365 Contact ID**: Select the field in Customer Insights - Data that stores contact IDs of contacts in Customer Insights - Journeys. Unless you've customized this, you should usually select **ContactId**.
   - **Display name**: Enter a name for this destination as you'd like it to appear in the destinations list in Customer Insights - Data.

    ![The Edit Destination dialog in Customer Insights - Data.](media/ci-edit-destination.png "The Edit Destination dialog in Customer Insights - Data")

1. Select **Next** to continue to the **Select segments to export** page. If you have any segments available in Customer Insights - Data, they are listed here. Mark the checkbox for each segment you'd like to export to Customer Insights - Journeys right away. You can also do this later if you prefer, or if you haven't created your segments yet.

    ![The Select Segments dialog in Customer Insights - Data.](media/ci-select-segments.png "The Select Segments dialog in Customer Insights - Data")

    > [!NOTE]
    > The segment list includes all currently defined segments, including **Draft** and **Inactive** segments. Though you are able to select draft and inactive segments here, these segments won't be exported to Dynamics 365 Customer Insights - Journeys.

1. Select **Save** to save your export destination.

## Configure a Customer Insights - Data segment to export to Customer Insights - Journeys

Any time you create a new segment for export, or decide you want to start exporting an existing segment, add that segment to the appropriate export destination to make it available in the Customer Insights - Journeys Instance it connects to. Once you have enabled export for a segment, it will continue to [refresh periodically](#refresh) until you [remove it](#edit-remove) from that export destination.

To export a new Customer Insights - Data segment to a Customer Insights - Journeys instance:

1. Sign in to Customer Insights - Data.
1. Go to **Segments**.
1. Find the segment you want to start exporting, select the **Expand all actions** button (which looks like three vertical dots) to open the action menu. Then open the **Add to** menu and select the export destination that you want to add the segment to. 

    ![Chose an export destination for a segment.](media/ci-export-segment.png "Chose an export destination for a segment")

    > [!NOTE]
    > The **Add to** menu only shows destinations that the current segment isn't already exporting to.

    > [!NOTE]
    > The segment list includes all currently defined segments, including **Draft** and **Inactive** segments. Though you are able to add draft and inactive segments to an export destination, these segments won't be exported to Dynamics 365 Customer Insights - Journeys.

<a name="edit-remove"></a>

## Edit the selection of Customer Insights - Data segments being exported to Customer Insights - Journeys

You can edit the list of Customer Insights - Data segments being exported to any destination, both to add or remove segments being exported and refreshed there. To do so:

1. Sign into Customer Insights - Data.
1. Go to **Admin** > **Export destinations**.
1. Find the destination you want to edit, select the **Actions** button (which looks like three vertical dots) to open the actions menu, and then select **Edit** from the actions menu.
1. The **Edit destination** dialog opens, showing your destination setup.
1. Select **Next** to continue to the **Select segments to export** page. All of the segments currently available in Customer Insights - Data are listed here. Select the check box for each segment you'd like to export and clear the check box for each segment you want to stop exporting.
1. Select **Save** to save your changes.

> [!NOTE]
> If you remove a segment from the export list, then that segment will no longer be refreshed by Customer Insights - Data, but the last exported versions will still remain available in Dynamics 365 Customer Insights - Journeys.

## Manually refresh integrated segments

Although your segments will automatically refresh a few times a day based on your [refresh schedule](/dynamics365/ai/customer-insights/pm-settings) in Customer Insights - Data, you can manually refresh your segments at any time. To do so:

1. Sign into Customer Insights - Data.
1. Go to **Data** > **Export destinations**.
1. Select the **Export** button at the top of the destinations list. This will trigger an export to all available destinations.

<!--    ![Manually export to a destination.](media/ci-export-destination.png "Manually export to a destination") -->

[!INCLUDE [footer-include](./includes/footer-banner.md)]
