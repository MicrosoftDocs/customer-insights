---
title: Known issues in Customer Insights - Journeys with mitigations
description: Learn about known issues in Customer Insights - Journeys, including limits for analytics, content, segments, and triggers. Find mitigations and workarounds.
ms.date: 10/05/2026
ms.topic: troubleshooting-known-issue
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Known issues in Customer Insights - Journeys with mitigations

This article lists known issues in Customer Insights - Journeys and provides mitigations to help you plan, configure, and troubleshoot journeys.

## Analytics

- Analytics for a journey can take up to 6-12 hours to show up.
- Occasionally, events are duplicated when saved in analytics. This duplication can lead to inconsistencies in reporting, such as customers appearing multiple times in the interaction details or remaining in a "processing" state well after the journey finishes.
- Some strings in the default Power BI aggregated analytics dashboards aren't localized.
- The default Power BI aggregated analytics dashboards don't support business units.
- If there's an email remote bounce, the contact or lead timeline might display two **email delivered** interactions for the same message with the same time stamp despite no message being delivered to the contact or lead email address. This behavior occurs because the second interaction is intended to "erase" the first one. However, the timeline doesn't currently handle this scenario.
- When you merge two contacts or leads, contact or lead insights show only interactions of the primary contact or lead.
- Unique values (for example, unique opens and clicks) in aggregated analytics dashboards might slightly deviate when compared to operational analytics. Key performance indicators (KPIs) in aggregated analytics are calculated once per day to ensure the highest possible accuracy. Operational analytics, designed for near real-time analysis, operate on demand by using faster calculation methods for unique values, which might be slightly less precise.

## Customer journeys

- Journey names can be up to 150 characters.
- Journey tiles that create branches can create up to 25 branches for a single tile. To create more branches, add a second branching tile to the **Other** branch of the first tile.
- Journeys with nested branches (a branching tile within the branch of another branching tile) have a maximum nested depth of eight branching conditions. To avoid nesting, consider consolidating branching logic or splitting the journey into separate journeys for large branches.
- Journeys with multiple complex conditions or large numbers of tiles can fail to publish. If retrying a journey publish doesn't succeed, consider splitting the journey into smaller journeys. You can also contact Microsoft Support to seek product support on this issue.
- A single journey instance can't run for more than 365 days. Once a participant starts a journey, that journey must end within that time frame or failures occur. If you need a journey longer than 365 days, consider splitting the journey into multiple journeys.
- A single wait tile can't wait for longer than 90 days. If you need a wait tile longer than 90 days, consider splitting the journey into multiple journeys.
- When you create a new journey version, only participants who enter the journey after you publish the version get the new journey version. In-progress journey participants remain on the journey version they started on. This condition affects the way analytics are shown across the journeys.
- Sometimes, journeys that have a large exclusion audience list, especially for a large segment that orchestrates the journey, encounter issues. In these cases, bring the exclusion list into the segment definition so that it can be processed better.
- When designing journeys with large segments, using a static Wait tile (for example, **Wait until September, 24 3:00 PM**) can cause delays in message delivery. To ensure smoother execution, consider using dynamic Wait conditions.
- Changing email links that are used for branching logic in live journeys might prevent participants from going down the correct path and isn't recommended.
- You can't edit one-time journeys with start dates that have already passed (even after copying them).
- You can only orchestrate segment-based journeys by using a single segment in Customer Insights - Journeys.
- You can't delete journeys once created and made live.
- The throughput of a journey varies depending on factors such as the complexity of your journey, the number of concurrent journeys that you run, the consumption patterns from other applications that you use, and the resource-intensive workloads that are being carried out. Learn more: [Service limits and fair use policy](fair-use-policy.md).

## Emails and content blocks

- Subject – 500 characters (including text to insert dynamic or conditional content) to 4,000 characters.
- Body – 1 MB (including all dynamic or conditional content).
- Marketers don't have the ability to align elements in the email editor.
- Marketers don't have the ability to put layouts inside layouts in the email editor.
- Marketers don't have the ability to create full-width layout emails.
- All content blocks, conditional content, lists, conditions, and other personalization don't have specific limits. However, they're stored within the email itself and therefore contribute to the size of the email and are subject to the email size limit.
- You insert content blocks into emails by copying. This condition has the following implications:
    - The same content block inserted multiple times in the same email are new and separate copies, and contribute to the email size.
    - Updating the original content block doesn't update emails that include those content blocks.
- The handlebar expression language for personalization syntax (for example, `{{contact.firstname}}`) isn't supported in real-time journeys. Define all personalization by using the user interface inside the designers for Email, SMS, or Push.

## Forms and pages

- If your embedded form isn't visible on external pages, ensure that the domain allows external form hosting. Most times, this restriction prevents customers from seeing the form on their website. You don't need to finish the domain authentication process to enable external form hosting for your domain. Learn more about [domain authentication](domain-authentication.md) Opens in a new window or tab.

## Lead scoring

- Parent contact scoring affects the time needed for scoring processing. Avoid parent contact scoring, especially if you have a large number of contacts.
- If you enable parent contact scoring, form submission interactions count twice in the lead scoring model.
- You can't use fields that have field-level security (FLS) enabled in lead scoring model conditions.

## Segments

- You can create a segment for up to 100,000,000 contacts.
- A segment-based journey works only when the size of the segment is under 10 million contacts. Any segment with a larger size fails to execute. To ensure that campaigns run effectively, break down the larger segments into multiple segments that use the same repeatable journey.
(1) This condition also applies to any trigger-based journeys that rely on segments in the journey flow.
- You can add up to 100 contacts to an inclusion or exclusion group as part of the segment definition. To get around this limit, create a separate segment of customers and use that segment in your main segment definition, thereby creating a compound segment.
- Relationship path suggestions in the segment builder are limited to five hops from the target table. To use a longer or more specific path, select **Custom path** and build it one relationship at a time. Custom paths can return to the target table - for example, contact > custom table > contact. Learn more: [Build segments in Customer Insights - Journeys](real-time-marketing-build-segments.md)
- You can't edit a segment that's being used in a live journey in Customer Insights - Journeys. To edit the segment, stop the journey, and then make the edits to the segments.
- The segment execution records table (`msdynmkt_segmentexecution`) stores execution history data for segments. The table is used for (1) rendering the "member count over time" graph in real-time journeys segments and (2) allowing journeys to determine when a segment was updated. Over time, the `msdynmkt_segmentexecution` table can grow significantly in size, impacting storage usage and performance. **Mitigation**: It's safe to delete `msdynmkt_segmentexecution` records. Before deleting anything, determine how much historical data you want to keep. It's recommended to retain at least the last three months of execution records, but retention decisions depend on your unique data policies and business needs.

## Triggers

- You can fire up to 100 custom triggers in an organization per day. This limit means you can execute up to 100 different types of custom triggers or trigger definitions. Each trigger can fire many times per day according to the fair usage policy. To increase the number of triggers for your organization, create a support ticket or contact your Microsoft representative.
- Define all attributes when you create custom triggers. If any attribute has a null value, the trigger fails and customers don't go through the journey. Currently, the system doesn't accept null values in a custom trigger. This condition results in a system failure and displays an error message at journey runtime.
- You can use Entity References in Custom or CDS triggers for up to five hops. You can't use any entity that's more than five hops away from the COLA entity as an attribute in a journey.
- When you use the **Marketing Form Submitted** standard trigger for your journey, ensure that the audience for the journey and the form are the same. Currently, the system doesn't display an error or warning when there's a mismatch, but the journey doesn't start.
- Currently, triggers also fire when you manually update a record in Dynamics 365 Dataverse. This condition can cause a contact to go through the journey based on the trigger even if they don't do anything to activate it.
- In rare instances, trigger-based journeys that use the if/then tile might encounter a delay in processing certain trigger events. In extreme situations, this delay could result in the event not being captured. While this occurrence is highly uncommon, the system continuously monitors and enhances the system to minimize any potential impact.
- Triggers can have at most 30 attributes. If the trigger has a table reference, the reference counts as one attribute toward the limit of 30. There's an additional limit of 1,024 on the number of columns from all such entity references.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
