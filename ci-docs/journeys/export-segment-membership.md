---
title: Export segment membership for offline analysis
description: Export segment membership to a CSV file in Customer Insights - Journeys. Choose columns with a view and include contact or lead IDs for offline analysis. Learn how.
ms.date: 10/09/2026
ms.topic: how-to
author: udag
ms.author: udag
ai-usage: ai-assisted
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Export segment membership for offline analysis

Export segment membership to a CSV file for offline analysis, reporting, or sharing in Customer Insights - Journeys. Learn how to choose exported columns and include contact or lead IDs while following organizational security policies.

## Export overview

Export up to 750,000 members from any static or dynamic segment that targets contacts or leads. The exported file is in CSV format (.csv). Its columns come from the view selected in **Column set from** on the segment's **Members and Insights** tab, so you choose what's exported by choosing a contact or lead view. The export includes every column in the view, including custom columns and columns from related tables. You can also include each member's contact or lead ID. For more information, see [Include contact or lead IDs in the export](#include-contact-or-lead-ids-in-the-export).

This format ensures compatibility with downstream processes like data review, enrichment, or re-import into other systems.

## Security and permissions

Security roles manage access to the **Export members** capability. A user needs the *Export Segment Members* privilege to perform this operation. The following built-in security roles include this privilege:

- *Marketing Manager (BU level) - Business*
- *Marketing Professional (BU level) - Business*
- *Marketing Manager - Business*
- *Marketing Professional - Business*
- *System Administrator*

Additionally, users need read and write access to the segment they want to export.

## How to export a segment

1. Go to **Segments** in the left navigation pane.
1. Open the segment you want to export. The segment must be in **Ready to use** or **Live with warnings** status.
1. Select the **Members and Insights** tab.
1. In **Column set from** above the member list, select the view whose columns you want to export. Each option shows the view name followed by its columns.
1. On the command bar, select **Export members**.

The export is generated and the .csv file downloads automatically.

> [!IMPORTANT]
> Select **Export members** while the **Members and Insights** tab is open. If you export from the **Design** tab, the file contains only the default columns (ID, first name, last name, email, and phone number), regardless of the view you selected.

The view you select isn't saved with the segment. When you reopen the segment, **Column set from** shows the default view again, so check it before each export.

If **Export members** is disabled or dimmed:  

- Make sure the segment is in **Ready to use** or **Live with warnings** status.  
- Check that the segment has at least one member and no more than 750,000 members.  
- Make sure your security role has the *Export Segment Members* privilege and that you have write access to the segment.  

## Include contact or lead IDs in the export

To match exported members with records in Dataverse or another system, show the contact or lead ID in the member list before you export. The ID is the unique identifier (GUID) of each contact or lead record.

1. Open a segment that's in **Ready to use** or **Live with warnings** status and select the **Members and Insights** tab.
1. Above the member list, select **More options** (**⋮**), and then select **Show Contact ID**. For a lead-based segment, select **Show Lead ID**.

    A column with each member's ID appears in the member list.

    :::image type="content" source="media/export-segment-members-show-contact-id.png" alt-text="Screenshot of a segment member list showing contact IDs and the More options menu.":::

1. On the command bar, select **Export members**. The exported file includes the ID column.

The ID column stays visible in your browser until you hide it. To remove it, select **More options** (**⋮**) > **Hide Contact ID** or **Hide Lead ID**.

## Limitations

- You can export only segments with up to 750,000 members.
- You can export only segments that target contacts or leads.
- The exported file includes the columns from the view selected in **Column set from** and, if shown, the contact or lead ID. Export from the **Members and Insights** tab to get these columns.
- Export is available only for users with the *Export Segment Members* privilege and read and write access to the segment.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
