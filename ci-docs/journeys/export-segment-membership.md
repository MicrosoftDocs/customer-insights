---
title: Export segment membership for offline analysis
description: Learn about how to export segment membership in CSV format in Dynamics 365 Customer Insights - Journeys.
ms.date: 04/01/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Export segment membership for offline analysis

In Customer Insights – Journeys, marketers can export the members of a segment directly to Excel for offline analysis, reporting, or sharing. This feature lets marketers inspect audience data outside the Customer Insights – Journeys app while following organizational security policies.

## Export overview

Export up to 750,000 members from any static or dynamic segment. The exported file is in CSV format (.csv) and includes the following data for each segment member:
- Customer ID
- First Name
- Last Name
- Email address
- Phone number

This format ensures compatibility with downstream processes like data review, enrichment, or re-import into other systems.

> [!NOTE]
> Only the fields listed in the previous paragraph are included in the export. Additional attributes or custom fields aren't supported in the export file at this time.

## Security and permissions

Access to the **Export to Excel** capability is managed through security roles. A user needs the *Export Segment Members* privilege to perform this operation. This privilege is included in the following built-in security roles:
- *Marketing Manager (BU level) – Business*
- *Marketing Professional (BU level) – Business*
- *Marketing Manager – Business*
- *Marketing Professional – Business*

Additionally, users need *read access* to the segment they want to export. No write or modify permissions are required to run an export.

## How to export a segment

1. Go to **Segments** in the left navigation pane.
1. Select the segment you want to export.
1. On the command bar, choose **Export to Excel**.
1. The export is generated and downloaded automatically in .csv format.

If the button is disabled or dimmed:
- Check if the segment exceeds the 750,000-member limit.
- Make sure your security role has the necessary export privileges.

## Limitations

- Only segments with up to 750,000 members can be exported.
- The exported file includes only the five predefined columns listed above.
- Custom fields, segment attributes, and calculated metrics aren't included.
- Export is available only for users with the correct role-based security privileges and read access to the segment.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
