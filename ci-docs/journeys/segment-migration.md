---
title: Migrate segments to real-time journeys
description: Learn how to use the Segment Migration Solution to migrate segments from outbound marketing to real-time journeys Dynamics 365 Customer Insights - Journeys.
ms.date: 02/11/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Migrate segments to real-time journeys

The outbound marketing module [will be removed from Customer Insights - Journeys](transition-overview.md) by June 2025. To avoid business continuity issues, all outbound marketing users must transition to real-time journeys before this date. Segmentation continues to be one of the most widely used features in outbound marketing, with users creating a large number of segments that are being used either in real-time marketing or outbound marketing journeys. It's now essential for existing users of outbound marketing segments to migrate to real-time marketing segments. To aid this transition, we've created the *Segment Migration Solution*.

## Segment Migration Solution purpose

Migrating segments from outbound marketing to real-time marketing can be time-consuming and operationally heavy. The *Segment Migration Solution* helps users migrate their segments from outbound marketing to real-time marketing with an intuitive solution that has a clean interface, allowing for a seamless and straightforward migration experience.

The *Segment Migration Solution* is user-friendly, featuring four distinct screens that guide users through the migration process. It helps users migrate their most important segments from outbound marketing to real-time marketing rather than carrying out mass migration. Here are some key points about the *Segment Migration Solution* features:

1. This is a Power Apps solution that needs to be installed and isn't integrated within the real-time marketing product.
1. To complete a successful migration, users of this tool must ensure that they have *create* segment permissions in real-time marketing.
1. The solution allows users to migrate a maximum of 2,000 segments from outbound marketing to real-time marketing.
1. Previously migrated segments are replaced when they're migrated again and don't count toward the overall quota.
1. Each migrated segment contains the prefix “Migrated –“ to indicate that it was migrated using the *Segment Migration Solution*.

The *Segment Migration Solution* isn't designed to address all outbound marketing segment migration requirements comprehensively. Instead, it serves as an initial resource to support users in starting their migration journey. The tool's limitations are outlined below:

1. Migrated segments are created in a draft state regardless of their actual state in outbound marketing. Users can choose which segments to publish post migration.
1. Exporting outbound marketing segments with NULL definitions isn't supported.
1. Exporting *Expired* segments in outbound marketing isn't supported.
1. Behavioral and interaction segment migration from outbound marketing to real-time marketing isn't supported.
1. Static segments that have more than 100 members aren't supported by the solution.
1. Complex segments that contain multiple nested conditions aren't supported by the solution.
1. Segments that contain traversal of entities (starting with an entity and navigating to contact) aren't supported by the solution.

## Install the Segment Migration Solution

1. Download the [managed solution zip](https://download.microsoft.com/download/a/b/a/abad6460-a4db-4c34-b36b-34a1b6508a5f/Segment%20Migration%20Tool.zip).
1. For the environment where this solution is used, go to the [Power Apps page](https://make.powerapps.com).
    1. Ensure the org name on the top right of the screen matches the organization you're testing the solution for. If there's a discrepancy, select the correct org.
1. Select **Solutions** on the left pane, then select **Import Solution** on the action ribbon at the top.
1. Follow the steps to select the shared zip solution file.
1. During the solution import, append the URL of the Customer Insights - Journeys app to your organization's URL.
    1. Ensure you copy the URL through the entire app-ID. For example: `https://<organizationname>.crm.dynamics.com/main.aspx?appid=<appid>`
1. Select **Import**. This takes about two to three minutes to import. Don't exit the screen.
1. Once done, you're ready to work with the *Segment Migration Solution*.

## Working with the Segment Migration Solution

Find the **Segment Migration Tool App** in the catalog of **Apps** in your environment by selecting the **Apps** button on the left navigation pane. Hover over the app to find the **Play** button. Select the **Play** button to start using the solution.

:::image type="content" source="media/solution-play-button.png" alt-text="Screenshot of the solution play button." lightbox="media/solution-play-button.png":::

> [!NOTE]
> Directly selecting the app name takes you to the editor, which isn't the intended action for this tool.

## Overview of each screen and its functionality

### Screen 1: Segment selection

On the left side, you see a list of all outbound marketing segments in the organization along with an option for multi-select. This screen includes details on the attributes of the segment such as the link to the segment in outbound marketing, date created, segment type, whether it contains nesting, status, and whether it was previously migrated. It also contains a toggle on top to switch between migrated and nonmigrated segments.

On the right side, there's a list of segments that were successfully migrated to real-time marketing along with the links to those segments in real-time marketing. When you use the solution for the first time, the right side is blank.

:::image type="content" source="media/solution-segment-selection.png" alt-text="Screenshot of segment selection in the Segment Migration Solution." lightbox="media/solution-segment-selection.png":::

Select a list of outbound segments to migrate and then select **Transition Pre-check**. This helps validate segment migration eligibility and allows only segments that pass the validation to be migrated.

## Screen 2: Prevalidation

In prevalidation, segments are checked for validity. Issues such as behavioral interaction and multiple sub–segments are highlighted in the **limitations** section. The pre–validation plugin checks if the outbound marketing segment has all the components intact in the query that are required to move it to real-time marketing. It also ensures that all required mappings and configurations are completed.

Segments that pass the validation (and those that fail the validation) are shown so that you know exactly which segments won't be migrated and which ones will. This gives you the option to review the segment before final migration.

For the segments that don't meet the criteria for migration, the reasons why the segment failed migration checks are detailed in the **Response** column. This allows you to either modify the underlying segment definition or recreate the segment manually in real-time marketing.

Once validation is complete, a summary screen is shown:

:::image type="content" source="media/solution-summary-screen.png" alt-text="Screenshot of the precheck summary screen in the Segment Migration Solution." lightbox="media/solution-summary-screen.png":::

When you select the **Migrate** button on this screen, the solution starts the process of recreating the segment in real-time marketing while showing a dynamic tracker of the progress until all valid segments complete migration.

## Screen 3: Migration and execution confirmation

Another set of checks is performed to see if the query is empty and if the segment name is valid. If any issues are caught during real-time marketing segment creation, the **Response** column provides the reason for failure and the error message.

:::image type="content" source="media/solution-migration-confirmation.png" alt-text="Screenshot of the solution migration confirmation screen in the Segment Migration Solution." lightbox="media/solution-migration-confirmation.png":::

At this time, the segments that have successfully migrated are in **Draft** state, and you can decide if you want to publish them.

> [!NOTE]
> Given that the segments are in **Draft** state, the solution doesn't have the ability to check for the membership of the segment. This can be done in the next screen once the segments are published in real-time marketing.

In the next screen, select the segments you want to publish after migration.

## Screen 4: Publish

This screen lets you select the migrated segments you want to publish. Here, we list all the real-time marketing segments that have successfully migrated (up to 2,000) and then let you multi-select the segments you want to publish or select all to publish everything.

:::image type="content" source="media/solution-publish.png" alt-text="Screenshot of the segment publish screen in the Segment Migration Solution." lightbox="media/solution-publish.png":::

Here, you can see the count of the segment members in outbound marketing and decide which of these you want to publish to a **Live** state in real-time marketing.

By following these steps, you can seamlessly transition your marketing efforts from outbound marketing to real-time marketing, ensuring continuity and applying the enhanced capabilities of real-time marketing.

## Known limitation of the Segment Migration Solution

1. Currently, users can't sort or search for the segments they want to migrate to outbound marketing.
1. Sometimes, users experience a bug when publishing the migrated segments in real-time marketing where, after selecting **Publish** on the final screen, there's an issue with rendering success. The segments are successfully migrated to real-time marketing and published, but users don't get that indication. You can verify this by selecting the **Home** button and seeing the segments show up in the real-time marketing **Segments** pane.

## Frequently asked questions

### I have more than 2,000 segments that I want to migrate using this tool. What should I do?

Our telemetry shows that 99% of our customers have fewer than 2,000 outbound marketing segments, so this covers almost the entire customer base. For those with more than 2,000 segments, when moving from outbound marketing to real-time marketing, we ask that customers prioritize moving segments needed for real-time marketing. Evaluate segments created long ago that aren't used in journeys carefully before bringing them into real-time marketing.

### Why can't interaction or behavioral segments be moved from outbound marketing to real-time marketing using this tool?

The tool doesn't allow interaction or behavioral segments between outbound marketing and real-time marketing because interactions work differently in each, and there isn't a 1:1 mapping between all interactions.

### Why is this provided as a Power Apps solution file rather than being integrated into the product like other features?

The migration tool helps customers speed up migration from outbound marketing to real-time marketing. This one-time process doesn't need to reside in the product long term. So, we decided to share the solution file with customers to use as they move from outbound marketing to real-time marketing.


### You mention a "one-time process" above. Does that mean I have to do this in one iteration?

No. You can use this multiple times as long as the total number of segments being migrated is 2,000 or less.

### I'm not allowed to download this per my organization’s settings. What should I do?

If you don't have permissions, reach out to your admin for help with setting up the solution based on the provided instructions.

### My organization uses business unit scoping heavily. Is that part of the tool or can I see everything that was created for the org?

The Segment Migration Solution doesn't consider business unit scoping, so you can see all outbound marketing segments for the organization.

### I migrated a segment already and made some changes to the definition in outbound marketing. Do I need to migrate it again? Would that add to my quota?

No. If it's the same segment, we overwrite the previously migrated segment. This doesn't add to the quota as a different segment.

### Are there plans to improve the tool based on new features added to real-time marketing to close the gap to outbound marketing segmentation?

Our focus is on closing the feature gaps in real-time marketing compared to outbound marketing. While we recognize the importance of broader coverage, we can't currently prioritize enhancements to the tool's coverage.

[!INCLUDE [footer-include](./includes/footer-banner.md)]