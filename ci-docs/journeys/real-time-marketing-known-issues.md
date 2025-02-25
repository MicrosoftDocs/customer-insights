---
title: Known issues in Customer Insights - Journeys with mitigations
description: Learn about known issues in Customer Insights - Journeys and how to work around them.
ms.date: 01/30/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Known issues in Customer Insights - Journeys with mitigations

As we continue to work on Customer Insights - Journeys and refine the experience, we've become aware of some outstanding issues for you to bear in mind. These issues are summarized in this article.

## Analytics

- Analytics for a journey can take up to 6-12 hours to show up.
- Occasionally events are dropped before they can get to analytics. This can cause issues in the analytics reporting where customers are shown to be in a ‘processing’ state much after a journey has been completed. We're working on a solution to improve this.
- Some strings in the out-of-the-box Power BI aggregated analytics dashboards aren’t localized.
- Business units aren't supported in the out-of-the-box Power BI aggregated analytics dashboards.
- If there's an email remote bounce, the contact/lead timeline might display two "email delivered" interactions for the same message with the same time stamp despite no message being delivered to the contact/lead email address. This is because the second interaction is intended to "erase" the first one. However, this isn't currently being handled in the timeline.
- When two contacts or leads are merged, only interactions of the primary contact or lead will be visible in contact/lead insights.
- There might be cases where unique values (for example, unique opens and clicks) in aggregated analytics dashboards have a slight deviation when compared to operational analytics. KPIs in aggregated analytics are calculated once per day to ensure the highest possible accuracy. Operational analytics, designed for near real-time analysis, operate on demand utilizing faster calculation methods for unique values, which may be slightly less precise.

## Customer journeys

- Journey names can be up to 300 characters.
- Journeys tiles that create branches can create up to 25 branches for a single tile. To create more branches, add a second branching tile to the “Other” branch of the first tile.
- Journeys with nested branches (a branching tile within the branch of another branching tile) have a maximum nested depth of eight branching conditions. To avoid nesting, limits consolidate branching logic or consider splitting the journey into separate journeys for large branches.
- Journeys with multiple complex conditions or large amounts of tiles can fail to publish. If retrying a journey publish doesn’t succeed, consider splitting the journey into smaller journeys. You can also reach out to MS Support to seek product support on this.
- A single journey instance can't run for more than 365 days. Once a participant starts a journey, that journey must end within that time frame or failures occur. If a journey longer than 365 days is needed, consider splitting the journey into multiple journeys.
- A single wait tile can't wait for longer than 90 days. If a longer than 90-day wait tile is needed, consider splitting the journey into multiple journeys.
- When a new journey version is created, only participants who enter the journey after the version has been published will get the new journey version. In-progress journey participants remain on the journey version they started on. This impacts the way analytics are shown across the journeys as well.
- Sometimes, journeys that have a large exclusion audience list, especially for a large segment that orchestrates the journey, will encounter issues. In these cases, it's better to bring the exclusion list into the segment definition so that it can be processed better.
- Changing email links that are used for branching logic in live journeys may prevent participants from going down the correct path and isn't recommended.
- One-time journeys with start dates that have already passed can't be edited (even after being copied).
- Orchestration of segment-based journeys can only be done using a single segment in Customer Insights - Journeys.
- Today, you can't delete journeys once created and made live.
- The throughput of a journey varies depending on a few factors such as the complexity of your journey, the number of concurrent journeys that you run, the consumption patterns from other applications that you use, and the resource-intensive workloads that are being carried out. Read the [Service Limits and Fair Usage policy document](fair-use-policy.md#customer-insights---journeys-real-time-journeys) Opens in a new window or tab for more guidance.

## Emails and content blocks

- Subject – 500 characters (including text to insert dynamic/conditional content) to 4000 characters.
- Body – 1 MB (including all dynamic/conditional content).
- Marketers lack the ability to align elements in the email editor.
- Marketers lack the ability to put layouts inside layouts in the email editor.
- Marketers lack the ability to create full-width layout emails.
- All content blocks, conditional content, lists, and conditions, and other personalization don't have specific limits. However, they're stored within the Email itself and therefore contribute to the size of the email and are therefore subject to the email size limit.
- Content blocks are inserted into emails by copying. This has the following implications:
    - The same content block inserted multiple times in the same email are new and separate copies (and contribute to the email size).
    - Updating the original content block doesn't update emails that include those content blocks
- The handlebar expression language for personalization syntax (for example, {{contact.firstname}}) isn't supported in real-time. All personalization must be defined using the UI inside the designers for Email, SMS, or Push. Workaround: Use the [Email import tool](real-time-marketing-import-email-to-real-time.md) Opens in a new window or tab in real-time to copy outbound emails. The tool will automatically migrate personalization expressions.

## Forms and pages

- Customer Insights - Journeys forms can update only one entity (typically a Lead or Contact). Targeting a single entity makes the form configuration and maintenance easier and it allows you to build properly targeted journeys.
- If your embedded form isn't visible on external pages, ensure that the domain allows external form hosting. Most times, this is the reason why customers aren't able to see the form on their website. You don't need to finish the domain authentication process to enable external form hosting for your domain. Learn more about [domain authentication](domain-authentication.md) Opens in a new window or tab.
- In Customer Insights - Journeys, users may encounter an issue where they can't view the form within Power Pages Studio. This particular situation arises when building a complex marketing website with multiple pages, requiring navigation and user authentication capabilities. To address this challenge, Power Pages Studio emerges as the optimal solution. To embed a Customer Insights - Journeys marketing form into a website constructed using Power Pages Studio, some modifications to the source code are necessary. Specifically, the addition of a JavaScript code snippet is essential to facilitate the seamless integration of the Marketing form. It's important to note that within Power Pages Studio, the form won't be visible during the editing process. However, once the page goes live and is accessible to the public, the form becomes visible and fully functional on the website. This capability enhances the user experience and ensures the successful implementation of RTM strategies within the marketing website.

## Lead scoring

- Parent contact scoring affects the time needed for scoring processing. We recommend avoiding parent contact scoring, especially if you have a large number of contacts.

## Segments

- A segment can be created for up to 100,000,000 contacts.
- A segment-based journey will only work when the size of the segment is under 10M contacts. Any segment with a larger size fails to execute. To ensure that campaigns can run effectively, break down the larger segments into multiple segments that can use the same repeatable journey.
(1) This is also true for any trigger-based journeys that rely on segments in the journey flow.
- There's a limit of 100 contacts that can be added to an inclusion/exclusion group as part of the segment definition. To get around this, you can create a separate segment of customers and use that segment in your master segment definition thereby creating a compound segment.
- Today, users can't edit a segment that is being used in a live journey in Customer Insights - Journeys. To be able to edit the segment, stop the journey, and then make the edits to the segments.

## Triggers

- Today, there's a limit of 100 custom triggers that can be fired in an org per day. To increase this for your organization, create a support ticket or reach out to your Microsoft Representative, and we can work with you to support your use case.
- When defining custom triggers, ensure that all attributes are defined. Any attribute that has a null value causes the trigger to fail leading to the customers not going through the journey. Today, we don't have the ability to allow null values to be passed in a custom, which then results in a System Failure as the error message at journey runtime.
- Usage of Entity References in Custom or CDS triggers is limited to five hops. Any entity that is more than 5 hops away from the COLA entity, can't be used as an attribute in a journey.
- When using the "Marketing Form Submitted" standard trigger for your journey care should be taken to ensure that the audience for the journey and the form are the same. Today, we don't display an error or warning when there's a mismatch, but the journey won't start leading to customer confusion.
- Today, triggers also fire when a record is manually updated in Dynamics 365 Dataverse. This can cause a contact to go through the journey based on the trigger even if they don't do anything to activate it.
- Today, for trigger-based journeys that use the if/then tile, you can sometimes lose about 1% of all trigger events due to a slight delay in our system catching them.
- Triggers can have at most 30 attributes. If the trigger has a table reference, then such a reference is counted as one attribute toward the limit of 30. There's an additional limit of 1,024 on the number of columns from all such entity references.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
