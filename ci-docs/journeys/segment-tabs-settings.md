---
title: Tabs and settings for segments
description: Learn to navigate tabs and settings for segments in Dynamics 365 Customer Insights - Journeys to optimize your customer targeting.
ms.date: 12/02/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing, evergreen
---

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

# Tabs and settings for segments

Tabs are shown as a set of headings under the header, which shows the name of the segment. Select any of these headings to go to the relevant tab. Each tab is described briefly in the following subsections.

## The Definition tab

Use the **Definition** tab to establish the membership of the segment. For dynamic segments, you'll find a query builder here. For static segments, you'll select specific contacts one at a time.

## The Members tab

Use the **Members** tab to see which contacts are part of the segment. It typically takes a few minutes for the Members tab to populate after you go live with a segment.

## The General tab

The **General** tab provides a few basic settings and general information about the segment. Many of the values here are established when you first create the segment and then become read only. Some fields are only present if your application is configured to use them. All fields are read-only when the segment is live. The fields you see may include some or all of the following:

- **Name**: The name of the segment as it appears in the segment list and when selecting segments for a customer journey.
- **Created on**: The date the segment was created.
- **Segment Type**: Shows the segment type (dynamic or static). This is permanently established when you first create the segment.
- **External source**: For segments that are synced from an external source, such as Customer Insights, information about the external source is shown here.
- **External segment URL**: For segments that are synced from an external source, such as Customer Insights, the URL of the external source is shown here.
- **Time Zone**: Shows the time zone of the segment. This is the timezone that the segment uses to calculate dates relative to the current time. For example, if you choose the partial date operator "All contacts who registered for an event in the last three days," the three-day duration is calculated using the segment time zone.
- **Activation status**: Shows whether the segment is in a draft or live state. Only live segments are available for use in customer journeys. (This is also referred to as the **Status reason**.)
- **Owner**: Shows the name of the user who owns the segment.
- **Scope**: This setting only appears when business-unit scopes are enabled for your instance. When scopes are enabled, this can have a setting of **Business unit** or **Organization**, but only privileged users (such as managers or admins) will be able to change it. When set to **Business unit**, the segment only contains contacts that belong to the same business unit as the segment owner, even when the query would normally find more contacts than this. When set to **Organization**, the segment contains all contacts that match the query, regardless of who owns the contacts or the journey. When this feature is disabled, the segment behaves as though it were set to **Organization**. More information: [Use business units to control access to Customer Insights - Journeys records](business-units.md)
- **Description**: A description of the segment.
- **Members**: The number of contacts that are currently included in the segment.

## The Insights tab

The **Insights** tab shows segment members over time.

## The Related tab

Almost all types of entities in Customer Insights - Journeys include a **Related** tab. Use it to find records that are related to the currently open record. This "tab" is just a drop-down list where you can select the type of related records you'd like to see. On selecting a record type (entity), a new tab named for that entity is added to the page where you can see a list of the related records of the selected type. When you select a new entity from the Related tab, it replaces the one currently shown.

> [!NOTE]
> The **Related** tab for segments sometimes includes an entry for **Customer journeys**, but this entry only finds journeys where the current segment is a *suppression segment*. It doesn't find journeys that use the current segment as a target segment. The reason for this is that suppression segments are related directly to the customer journey entity, while target segments are linked to journeys less directly, through a tile configuration, and therefore aren't resolved in the **Related** tab.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
