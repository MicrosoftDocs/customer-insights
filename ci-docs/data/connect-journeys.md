---
title: Connect Customer Insights - Data to Customer Insights - Journeys
description: Learn how to connect Customer Insights - Data and Customer Insights - Journeys to use unified customer profiles and segments in journeys.
ms.date: 02/13/2026
ms.topic: how-to
author: dleblondMSFT
ms.author: dleblond
ms.reviewer: mhart
ms.custom: bap-template
---

# Connect Customer Insights - Data to Customer Insights - Journeys

Use unified customer profiles and segments from Customer Insights - Data in Customer Insights - Journeys to create targeted, personalized customer journeys.

## Prerequisites

- Both applications must be installed on the **same Dataverse environment**
- The environment must have both Customer Insights - Data and Customer Insights - Journeys licenses assigned
- You must have Admin role in both applications
- Customer Insights - Data must have completed initial setup (at least one data source ingested and unification configured)

## Verify the connection

1. In Customer Insights - Journeys, go to **Settings** > **Data management** > **Customer Insights connector**.
2. You should see your Customer Insights - Data instance listed. If not:
   - Verify both apps are on the same environment (check the environment URL).
   - Verify licenses in **Power Platform Admin Center** > **Environments** > [your environment] > **Resources**.

## Enable Dataverse data sharing

For Customer Insights - Data segments and profiles to be available in Customer Insights - Journeys, Dataverse data sharing must be enabled.

1. In Customer Insights - Data, go to **Settings** > **Data sharing**.
2. Enable **Dataverse data sharing** if it isn't already enabled.
3. Run a full refresh to sync data to Dataverse.

## Common issues

| Problem | Cause | Solution |
|---------|-------|----------|
| "There was a problem setting up the Customer Insights - Data connection" | Customer Insights - Data not provisioned on the same environment | Provision Customer Insights - Data on the same Dataverse environment as Journeys |
| Customer Insights connector works in UAT but not Production | Different environments or license assignments | Verify Production has the same setup as UAT |
| Trigger-based journey not sending emails | Using Customer Insights - Journeys feature, not Customer Insights - Data | Verify you're configuring in the correct application |
| Cannot see Customer Insights - Data segments in Journeys | Dataverse sync disabled or segment not active | Enable Dataverse data sharing; activate and refresh the segment |
| Segment shows 0 members in Journeys | Segment hasn't synced to Dataverse yet | Wait for the next scheduled refresh to complete |

## See also

- [Use segments in Customer Insights - Journeys](segments.md#use-segments-in-customer-insights---journeys)
- [Create and manage segments](segments.md)
- [Exports overview](export-destinations.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
