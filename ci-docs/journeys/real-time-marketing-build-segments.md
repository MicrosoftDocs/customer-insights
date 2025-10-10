---
title: Build segments in Customer Insights - Journeys 
description: Learn how to build segments to use in real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/09/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: sfi-image-nochange
---

# Build segments in Customer Insights - Journeys

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=a1240d08-395b-4041-ba4f-853a32afaea3]

Improve marketing return on investment by targeting the right audience. Build segments directly in Dynamics 365 Customer Insights - Journeys with the powerful, easy-to-use logic builder that doesn't require specialized knowledge of complex data structures or logical operators. Preview the estimated segment size and membership before you mark your segment as "Ready to use" in customer journeys.

When building segments, you can choose to target contacts, leads, or unified profiles from Customer Insights - Data.

> [!NOTE]
> To target unified profiles, install Customer Insights - Journeys and Customer Insights - Data on the same environment.

## Create a demographic segment targeting leads

You can now create dynamic segments targeting leads directly without having to connect it to a parent contact.

To target leads directly, go to **Customer Insights - Journeys** > **Audience** > **Segments** and select **+ New Segment** in the top toolbar. You can then name the new segment and select **Lead** under the **Select a target audience** dropdown. After you select the **Create** button, you'll be taken directly to the segment builder where you can create and save your segment.

> [!div class="mx-imgBorder"]
> ![Create a segment to target leads.](media/real-time-marketing-build-segment-create.png "Create a segment to target leads")

In the right pane of the segment builder, you can search for attributes to add to the builder canvas.

**Example:** Qualifying leads that are scheduled for a follow-up in the next seven days:

> [!div class="mx-imgBorder"]
> ![Search for attributes.](media/real-time-marketing-build-segment-attribute.png "Search for attributes")

## Create demographic segment using related tables

In addition to having a segment return its targeting entity (such as contacts or leads), you can also build more complex queries that reference other tables (such as Event Registration or Account) to further enrich your segment definition. You can even reference customer measures from Customer Insights - Data when targeting unified profiles.

> [!NOTE]
> To reference customer measures, Customer Insights - Journeys and Customer Insights - Data must be installed on the same environment.

When adding an attribute that relates to a different table, you can search for the attribute and then define how the two tables are related based on your segment definition. To add an attribute from a related table, you must enable **Track changes** in the related table. For new or existing tables, **Track changes** can be checked from the table properties.

>[!Note]
> Virtual tables aren't supported in real-time journeys segmentation. The real-time journeys segment designer doesn't show virtual tables in the "Add tables" dialog.

**Example:** Leads whose parent accounts are in the Consumer Services industry.

Search for "industry" on the right-side pane and select the **+** button to the right of the item in the table you want. You'll see all possible combinations of how the Lead and Account tables are related.

> [!div class="mx-imgBorder"]
> ![Search for related tables.](media/real-time-marketing-build-segment-industry.png "Search for related tables")

Select "Account > **Lead**" for the relationship path, then select the **Next** button. Next, set the path between the Lead and Account tables to be "Parent Account for lead" according to the segment definition, then select the **Set Path** button.

> [!div class="mx-imgBorder"]
> ![Set the path between the Lead and Account tables.](media/real-time-marketing-build-segment-path.png "Set the path between the Lead and Account tables")

## Previewing segment members and size estimate

When you're satisfied with your segment definition, select **Refresh** on the bottom toolbar to quickly check if you are on the right track to creating your segment. This gives you an estimated size of how many members are in the segment.

To see a list of the first set of segment members the app fetched based on your definition, select **View sample of included members** on the bottom toolbar. This gives you an estimate of who is in this segment.

> [!div class="mx-imgBorder"]
> ![View sample of included segment members.](media/real-time-marketing-build-segment-members.png "View sample of included segment members")

## Add a subgroup to your segment

**Example:** Leads with company size of more than 10,000 employees, whose parent accounts are in either the Consumer Services or Financial Services industry.

You can choose your attribute to be added to a new subgroup. To do this, search for the attribute, then select the name of the attribute item from the results. A contextual menu pops up that allows you to add the item to a new or existing subgroup.

> [!div class="mx-imgBorder"]
> ![Add a subgroup.](media/real-time-marketing-segment-builder-subgroup.png "Add a subgroup")

To include members from either subgroup, select the **or** subgroup operator.

> [!div class="mx-imgBorder"]
> ![Use the or operator.](media/real-time-marketing-segment-builder-or.png "Use the or operator")

## Add a new group to a segment (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

**Example**: Let’s say you want to create a query for leads with a company size of more than 10,000 employees whose parent accounts are in the Consumer Services or Financial Services industries, **but not** leads with a budget of less than $20,000.

To create the segment from the above example, create a new segment in Customer Insights - Journeys for leads whose company size is 10,001 or more. Open the **Elements** pane by selecting the top icon on the menu on the right side of the window. Then, go to the **Attributes** tab and search for the **Budget Amount** attribute. Select the icon to the left of the attribute name from the results list. A contextual menu appears, allowing you to add the attribute to an existing or new group.

> [!div class="mx-imgBorder"]
> ![add a new group to a segment](media/real-time-marketing-add-a-new-group.png "add a new group to a segment")

In the above example, the attribute was added to a new group (Group 2). To create the segment you want, select the operator button between the groups.

> [!div class="mx-imgBorder"]
> ![select your operator between groups](media/real-time-marketing-select-your-operator-between-groups.png "select your operator between groups")

> [!Note]
> Calculated and Formula Dataverse table fields aren't supported in real-time journeys segmentation. The segmentation backend doesn't receive an update signal when a Calculated or a Formula field is updated. This is by design, as values of Calculated and Formula fields aren't persisted anywhere, they're just calculated on the fly. To address this, the app now shows Calculated and Formula fields as **disabled** in the real-time journeys segment designer (with an appropriate tooltip).

> [!TIP]
> While adding nested segments to the segment definition, you can view the details of the underlying segment by selecting the **View segment** hyperlink when hovering over the desired segment. To use keyboard controls to view the segment, press the "K" key while focus is on the desired segment. This action opens a dialog displaying the segment details.
> :::image type="content" source="media/segment-details.png" alt-text="Screenshot showing link to view segment details." lightbox="media/segment-details.png":::

## Use CSV files to define static segment membership lists for up to 2,000,000 members

You can define segment membership by matching a list of contacts or leads from a CSV file to contacts or leads in Dataverse. The real-time journeys segment builder matches email addresses with already existing contacts or leads in Dataverse, which you can then include in the segment definition as a static list.

### Prerequisites

- The segment must be saved before adding static members.

### How to use a CSV file to add static members

1. Create a new contact or lead-based segment.
1. Select the **+ Add a new group** dropdown, then select **Upload CSV**. You can also drag and drop a CSV file onto the segment builder.
1. The CSV file must have a column with the header `emailaddress1` that contains email addresses for matching contact or lead records in Dataverse.
    - When using a CSV file, all contact or lead records in Dataverse with a matching email address are included in the list. Multiple records with the same email address aren't deduplicated.
1. You can also manually select members from Dataverse using the standard contact or leads grid view. To launch the standard Dataverse grid view, go to **Manual select** > **Select members** > **Add members**.
    > [!NOTE]
    > The grid view is limited to browser cache sizes for displaying available contacts or leads. You can only select as many contacts or leads at a time as the cache will display.
1. Each static member group defined either by a CSV file or by manually selecting from the contact or leads grid can contain up to 200,000 members. You can have a maximum of 10 groups, for a total of 2,000,000 possible static members. You can then add dynamic query criteria for additional members to be included when they meet the query criteria.
    > [!TIP]
    > Segment definitions can include static lists and dynamic criteria in the same definition.

### Guidance for using CSV files for static segments

- The "Not found" list includes rows in the CSV for which there are no matching records in Dataverse. You can download this list and follow the steps to upload them into Dataverse using the contact or leads list view CSV upload feature to create the records in Dataverse. You can then retry the matching to have them included in the segment definition.
- The number of records found in the CSV file shows the number of rows in the CSV file that match one or more contact or lead records in Dataverse. If multiple records match the same email address in the CSV, the member count of the static list can be larger than the number of records found in the CSV. For example, one row in the CSV with `email@email.com` might match three contact records with the same email address. The member count shows the number of contact or lead records in the segment, while the "found" count shows the number of CSV rows that match one or more contact or lead records.
- For static snapshots, contacts or leads that the segment builder has permissions to see in Dataverse either by teams or business unit scoping permissions are found and included in the segment definition. For dynamic queries, any matching contacts or leads, regardless of the business unit that the segment author belongs to while defining the segment, are included in the segment at run time.

### Augment with the segment builder API

The segment builder API powers the user interface (UI), so anything you do through the UI, you can do programmatically using the API. Use the API to augment a segment you build using the UI. Learn more: [Create a Customer Insights - Journeys segment using the Web API](real-time-marketing-api-segment.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
