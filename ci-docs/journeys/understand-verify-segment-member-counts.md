---
title: Understand and verify segment member counts
description: Learn why segment member counts differ in Dynamics 365 Customer Insights - Journeys, how to resolve mismatches, and verify accurate results.
ms.date: 09/08/2026
ms.topic: article
author: udag
ms.author: udag
ms.reviewer: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: sfi-image-nochange
---

# Understand and verify segment member counts

Segment member counts can be higher or lower than expected in Customer Insights - Journeys. This article explains how to compare preview and evaluated counts, identify the following common causes of mismatches, and verify that segment membership is working as intended.

- The preview estimate differs from the evaluated segment.
- Segment logic unintentionally excludes records.
- Related-table joins behave differently than expected.
- Business unit permissions affect visibility.
- Consent filtering removes contacts.
- Data synchronization hasn't completed.
- Unsupported data types are used in conditions.

Understanding these factors can help you identify the source of the mismatch and validate that your segment is working as intended.

## Compare preview and evaluated segment member counts

When you create a segment, the preview estimate is based on a sample of the data. The evaluated segment, however, is based on the entire dataset. This means that the preview estimate may not always match the evaluated segment count. To verify the correct counts, use the following methods:

- **Preview estimate versus evaluated membership**: The segment builder preview provides an estimate and sample members for quick validation. Large or complex segments might not return an accurate preview. Compare against the refreshed segment results rather than the preview. For more information, see [Build segments in Customer Insights - Journeys](real-time-marketing-build-segments.md#previewing-segment-members-and-size-estimate)  
- **Where to find the complete member list**: The segment details page shows only a preview of matching members. To validate counts, review the evaluated segment membership or export the results. Inspection mode shows member counts for individual rules and rule combinations. Use these counts to quickly identify which rules add or remove members. For more information, see [View segment member counts](../data/segments.md#view-segment-member-counts-preview)

## Resolve fewer members than expected

If your segment returns fewer members than expected, check the following factors to identify the cause of the discrepancy:

- **Conditions and operators**: When you combine multiple conditions, the segment logic can become more restrictive than expected. For example, if you combine two conditions with an AND operator, the segment includes only records that satisfy both conditions. Verify the conditions independently to ensure they're correct before combining them.  
- **Exclusions**: Exclusion segments override inclusions. A contact can match an inclusion rule but still be removed because it appears in an exclusion group. This condition commonly causes unexpectedly low counts.  
- **Related-table grouping and paths**: When segments use related tables, you might assume all related records must match a condition. Depending on grouping and relationships, the query can become more restrictive than expected. This condition usually causes complex segment issues.  
- **Business unit scope**: Business unit visibility and permissions can affect static segment matching. The segment definition process might not include records that exist in Dataverse if they aren't visible.  
- **Data synchronization**: A record might satisfy the conditions but isn't available for evaluation because synchronization or processing hasn't completed. Historical support investigations identified synchronization delays and metadata synchronization issues as common causes of count discrepancies.  
- **Consent criteria**: Modern segments can filter based on compliance profiles, purposes, topics, and channels. You might expect all matching contacts to appear, but consent evaluation can remove contacts from membership calculations. Segment counts can therefore differ from attribute-only filters.  

## Resolve more members than expected

If your segment returns more members than expected, check the following factors to identify the cause of the discrepancy:

- **Group operators**: OR groups and UNION operations typically increase counts. Customers often build logic that says:
    Industry = Financial Services
    OR Country/Region = USA
    when they intended both conditions to be true. The result is a much larger audience.  
- **Related-table grouping and paths**: Incorrect grouping across related tables can broaden results and include records that customers didn't expect.  
- **Static inclusions**: Imported CSV lists and manually included members can increase counts beyond the expected dynamic query results. A single CSV row can also match multiple Dataverse records, increasing membership.  
- **Consent criteria**: Customers may compare against older segments that use previous consent logic. New consent-based segments can evaluate membership differently, producing unexpected counts.  

## Verify segment membership results

After resolving the discrepancy, verify the result by checking the segment membership against a known sample record. If the sample record is included in the segment, you can be confident that the segment is working as intended. If the sample record is excluded, review the segment logic and conditions to ensure they are correct. If you still encounter issues, contact Microsoft support for further assistance.

## Related information

- [Build segments in Customer Insights - Journeys](real-time-marketing-build-segments.md)  
- [View segment member counts](../data/segments.md#view-segment-member-counts-preview)
