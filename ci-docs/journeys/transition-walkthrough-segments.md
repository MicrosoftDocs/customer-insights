---
title: Migrate segments to real-time journeys
description: Learn how to use the Segment Migration Solution to migrate segments from outbound marketing to real-time journeys Dynamics 365 Customer Insights - Journeys.
ms.date: 06/05/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition segments to real-time journeys

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

You can use outbound marketing segments in real-time journeys, but it's best to rebuild the segments in real-time journeys for better performance and faster refresh cycles. Once outbound marketing is removed, segments created in outbound don't refresh and might not be available for use in real-time journeys. Migrate outbound segments using the [*Segment Migration Solution*](transition-walkthrough-segments.md#segment-migration-solution), or use [natural language and Copilot](real-time-marketing-natural-language-segments.md) to create real-time journeys segments.

> [!NOTE]
> The *Segment Migration Solution* isn't a comprehensive solution that migrates all outbound marketing segments to real-time journeys. It's provided to help you start segment migration. Read about the nuances of the *Segment Migration Solution* before using the tool.

Set aside time to migrate your most important segments to real-time journeys.

We've also increased the segmentation limits for real-time journeys to be better than outbound marketing, as shown in the [Service Limits and Fair Use Policy](fair-use-policy.md) page.

## Segment Migration Solution

Migrating segments from outbound marketing to real-time journeys can take time and effort. The *Segment Migration Solution* lets you move segments from outbound marketing to real-time journeys with an intuitive, clean interface for a simple migration experience.

The *Segment Migration Solution* is user friendly and has four screens that guide you through the migration process. It lets you move your most important segments from outbound marketing to real-time journeys instead of migrating everything at once. Here are some key features:

1. This is a Power Apps solution that you need to install. It's not integrated with the real-time journeys product.
1. To migrate segments, make sure you have *create* segment permissions in real-time journeys.
1. You can migrate up to 2,000 segments from outbound marketing to real-time journeys.
1. If you migrate a segment again, it replaces the previous version and doesn't count toward your quota.
1. Each migrated segment has the prefix “Migrated –“ to show it was moved using the *Segment Migration Solution*.

The *Segment Migration Solution* doesn't cover all outbound marketing segment migration needs. It's an initial resource to help you start migrating. Here are some limitations:

1. Migrated segments are created as drafts, no matter their state in outbound marketing. You can choose which segments to publish after migration.
1. You can't export outbound marketing segments with NULL definitions.
1. You can't export *Expired* segments from outbound marketing.
1. You can't migrate behavioral or interaction segments from outbound marketing to real-time journeys.
1. The solution doesn't support static segments with more than 100 members.
1. The solution doesn't support complex segments with multiple nested conditions.
1. The solution doesn't support segments that traverse entities (starting with an entity and going to contact).

## Install the Segment Migration Solution

1. Download the [managed solution zip](https://download.microsoft.com/download/a/b/a/abad6460-a4db-4c34-b36b-34a1b6508a5f/Segment%20Migration%20Tool.zip).
1. In the environment where you use this solution, go to the [Power Apps page](https://make.powerapps.com).
    1. Check that the org name at the top right matches the organization you're testing the solution for. If it doesn't, select the correct org.
1. Select **Solutions** in the left pane, then select **Import Solution** in the action ribbon at the top.
1. Follow the steps to select the shared zip solution file.
1. During the solution import, add the URL of the Customer Insights - Journeys app to your organization's URL.
    1. Copy the URL through the entire app ID. For example: `https://<organizationname>.crm.dynamics.com/main.aspx?appid=<appid>`
1. Select **Import**. Importing takes about two to three minutes. Don't exit the screen.
1. When the import finishes, you're ready to work with the *Segment Migration Solution*.

## Working with the Segment Migration Solution

To use the Segment Migration Solution:

1. Select the **Apps** button on the left navigation pane to open the catalog of **Apps** in your environment.
1. Hover over the **Segment Migration Tool App** to show the **Play** button.
1. Select the **Play** button to start the solution.

:::image type="content" source="media/solution-play-button.png" alt-text="Screenshot of the Play button for the Segment Migration Tool App." lightbox="media/solution-play-button.png":::

> [!NOTE]
> If you select the app name directly, you go to the editor, which isn't the intended action for this tool.

## Overview of each screen and its functionality

### Screen 1: Segment selection

On the left side, you see a list of all outbound marketing segments in the organization with an option for multi-select. This screen shows details about each segment, like the link to the segment in outbound marketing, date created, segment type, whether it has nesting, status, and whether it was previously migrated. There's also a toggle at the top to switch between migrated and nonmigrated segments.

On the right side, you see a list of segments that migrated to real-time journeys, along with links to those segments in real-time journeys. The right side is blank the first time you use the solution.

:::image type="content" source="media/solution-segment-selection.png" alt-text="Screenshot of segment selection in the Segment Migration Solution." lightbox="media/solution-segment-selection.png":::

Select the outbound segments you want to migrate, and then select **Transition Pre-check**. This step checks segment migration eligibility and lets you migrate only segments that pass validation.

## Screen 2: Prevalidation

In prevalidation, the solution checks segments for validity. Issues like behavioral interaction and multiple subsegments appear in the **limitations** section. The prevalidation plugin checks if the outbound marketing segment has all the components in the query that are needed to move it to real-time journeys. It also checks that all required mappings and configurations are complete.

The solution shows both segments that pass and fail validation, so you know exactly which segments migrate and which don't. You can review each segment before migration.

For segments that don't meet migration criteria, the **Response** column details why each segment fails migration checks. You can change the segment definition or recreate the segment manually in real-time journeys.

After validation, the solution shows a summary screen:

:::image type="content" source="media/solution-summary-screen.png" alt-text="Screenshot of the precheck summary screen in the Segment Migration Solution." lightbox="media/solution-summary-screen.png":::

Select the **Migrate** button to start recreating the segment in real-time journeys. The solution shows a dynamic progress tracker until all valid segments finish migration.

## Screen 3: Migration and execution confirmation

The solution checks if the query is empty and if the segment name is valid. If it finds any issues during real-time journeys segment creation, the **Response** column shows the reason for failure and the error message.

:::image type="content" source="media/solution-migration-confirmation.png" alt-text="Screenshot of the solution migration confirmation screen in the Segment Migration Solution." lightbox="media/solution-migration-confirmation.png":::

At this point, the segments that migrate successfully are in **Draft** state, and you decide if you want to publish them.

> [!NOTE]
> Because the segments are in **Draft** state, the solution can't check the membership of the segment. You can do this in the next screen after you publish the segments in real-time journeys.

On the next screen, select the segments you want to publish after migration.

## Screen 4: Publish

This screen lets you select migrated segments to publish. It lists up to 2,000 real-time journeys segments that successfully migrated. Select multiple segments to publish, or select all to publish every segment.

:::image type="content" source="media/solution-publish.png" alt-text="Screenshot of the segment publish screen in the Segment Migration Solution." lightbox="media/solution-publish.png":::

You see the count of segment members in outbound marketing and decide which segments to publish to a **Live** state in real-time journeys.

Follow these steps to transition your marketing efforts from outbound marketing to real-time journeys. This ensures continuity and lets you use the enhanced capabilities of real-time journeys.

## Known limitations of the Segment Migration Solution

1. Currently, users can't sort or search for the segments they want to migrate to outbound marketing.
1. Sometimes, users experience a bug when publishing the migrated segments in real-time journeys where, after selecting **Publish** on the final screen, there's an issue with rendering success. The segments are successfully migrated to real-time journeys and published, but users don't get that indication. You can verify this by selecting the **Home** button and seeing the segments show up in the real-time journeys **Segments** pane.

## Frequently asked questions about the Segment Migration Solution

### I have more than 2,000 segments that I want to migrate using this tool. What should I do?

Our telemetry shows that 99% of our customers have fewer than 2,000 outbound marketing segments, so this covers almost the entire customer base. For those with more than 2,000 segments, when moving from outbound marketing to real-time journeys, we ask that customers prioritize moving segments needed for real-time journeys. Evaluate segments created long ago that aren't used in journeys carefully before bringing them into real-time journeys.

### Why can't interaction or behavioral segments be moved from outbound marketing to real-time journeys using this tool?

The tool doesn't allow interaction or behavioral segments between outbound marketing and real-time journeys because interactions work differently in each, and there isn't a 1:1 mapping between all interactions.

### Why is this provided as a Power Apps solution file rather than being integrated into the product like other features?

The migration tool helps customers speed up migration from outbound marketing to real-time journeys. This one-time process doesn't need to reside in the product long term. So, we decided to share the solution file with customers to use as they move from outbound marketing to real-time journeys.

### You mention a "one-time process" above. Does that mean I have to do this in one iteration?

No. You can use this multiple times as long as the total number of segments being migrated is 2,000 or less.

### I'm not allowed to download this per my organization’s settings. What should I do?

If you don't have permissions, reach out to your admin for help with setting up the solution based on the provided instructions.

### My organization uses business unit scoping heavily. Is that part of the tool or can I see everything that was created for the org?

The Segment Migration Solution doesn't consider business unit scoping, so you can see all outbound marketing segments for the organization.

### I migrated a segment already and made some changes to the definition in outbound marketing. Do I need to migrate it again? Would that add to my quota?

No. If it's the same segment, we overwrite the previously migrated segment. This doesn't add to the quota as a different segment.

### Are there plans to improve the tool based on new features added to real-time journeys to close the gap to outbound marketing segmentation?

The focus is on closing feature gaps in real-time journeys compared to outbound marketing. While broader coverage is important, enhancements to the tool's coverage aren't currently prioritized.

### After the deprecation of outbound marketing, what happens to my segment templates?

Segment templates aren't removed, but marketers can't create new segments using outbound marketing segment templates. You can use the templates for lookup and refer to them while building real-time journeys segments. Segment templates aren't available in real-time journeys and aren't considered a blocking feature. If you want to use or recreate segment templates, save a segment as a template, create a copy, and use it (with or without changes) for a campaign.

### Will the removal of outbound marketing affect the usage of Customer Insights - Data segments in real-time journeys?

When outbound marketing is removed, you have two options to use Customer Insights - Data segments in real-time journeys:
1. **Use Customer Insights - Data segments directly in real-time journeys**: You can use existing Customer Insights - Data profile attributes and measures (in addition to Dataverse tables related to contacts) without extra work if [COLA Stamping] [unified-profile-segment-creation.md] is enabled. These are segments of profiles (not contacts), so you can only orchestrate on profiles.
1. **Create contact-based segments in real-time journeys directly with related tables in Dataverse**: You can build a contact segment in real-time journeys and use any related table in Dataverse like before, but you can't use any Customer Insights - Data information in the segment.

## Guidance on specific capabilities as you migrate from outbound marketing to real-time journeys

### Segment templates

- **Details**: Marketers can accelerate segment creation through templates.
- **Guidance**: There's no published roadmap for this capability. Create one or more segments to use as templates. Then, use the **Save as** option to create a copy for a campaign.

### Include or exclude up to 200,000 individual members in a static segment

- **Details**: Marketers can include or exclude up to 200,000 members while defining a static segment.
- **Guidance**: There's no published roadmap for this capability. Either:
  -  Use marketing lists to build a segment.
  -  Create a new attribute for the contacts in the segment, then create a query-based dynamic segment using the new attribute.

### View, copy, or paste segment definition query

- **Details**: Marketers can create new segments by copying and pasting segment definition queries from existing segments.
- **Guidance**: There's no published roadmap for this capability. Create a copy of the segment you want and edit the segment definition.

### Create a segment based on journey participation

- **Details**: Ability to create a segment that includes the audience that is participating in one or more specified journeys.
- **Guidance**: There's no published roadmap for this capability. Build segments using behavioral attributes specific to the journeys you want (for example, "email delivered" filtered for specific journeys using the *JourneyID* property).

### More than one level of nesting while building composite segments

- **Details**: Real-time journeys allow only one level of nesting when building composite segments.
- **Guidance**: There's no published roadmap for this capability. Use multiple segments to start or exit the journey and achieve the same outcome without a complex compound segment.

### Using Customer Insights - Data segments in Customer Insights - Journeys

- **Details**: Customer Insights - Data segments can be exported as segments of contacts in outbound marketing that become available in real-time journeys as well. 
- **Guidance**: When outbound marketing is removed, such exported segments will no longer be available for use in real-time journeys. You can use Customer Insights - Data segments in real-time journeys directly, though they'll be segments of Profiles (not segments of contacts), so journeys and messages need to use Profiles (instead of contacts). You can access profile attributes and measures from Customer Insights - Data for conditions and personalization. If the linking feature is enabled (see [Automatically link Dynamics 365 apps to customer profiles](/dynamics365/customer-insights/data/integrate-d365-apps)), then you can build segments of contacts in real-time journeys using profile attributes and measures.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
