---
title: "What's new in Dynamics 365 Customer Insights - Data"
description: "Information about new features, improvements, and bug fixes."
ms.date: 11/10/2026
ms.topic: whats-new
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
---

# What's new in Dynamics 365 Customer Insights - Data

This article lists monthly release notes for Dynamics 365 Customer Insights - Data, including preview features, general availability updates, enhancements, and bug fixes. Visit the [AI at Work roadmap](https://aka.ms/AIatWorkroadmap) to discover upcoming capabilities, track rollout progress, and plan adoption.

Customer Insights - Data rolls out updates on a region-by-region basis. So certain regions might see features before others. Unless specified differently, you don't need to take any action. We update the app automatically with no downtime.

To submit and vote on **feature requests** and **product suggestions**, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=dfa5b83d-9e4c-e811-a956-000d3a1bef07&forumName=Dynamics%20365%20Marketing).

## November 2026

### General availability

#### Show or hide columns or tables from segment and measure builders

Administrators can control which columns or tables are visible in the segment and measure builders. This control helps reduce clutter and lets users focus on the data that's most relevant when creating segments and measures.

- [Docs](tables.md#show-or-hide-columns-or-tables-from-segment-and-measure-builders)

#### Business unit support and role-based access control

Administrators can control access to customer profiles, segments, and measures based on business units.

- [Docs](business-units-data-separation.md)

## October 2026

### General availability

#### Monitor your quota usage

Check how many unified profiles your organization is using for Customer Insights - Data compared to your limit.

- [Docs](quota-limits.md)

#### Web tracking and personalization

Web tracking and personalization in Customer Insights - Data is now generally available and includes new functionality.

- Track user activity on your website for known and unknown users in real-time.
- The system captures activity to Dataverse, so you can personalize your website content based on users' previous browsing activity on your site.
- New functionality includes optional query string tracking that you can use to attribute traffic to campaigns.
- New functionality includes optional IP tracking (first three octets).

> [!IMPORTANT]
> If you added the tracking script to your website before October 2026, you **must** update your website with the latest script to continue using tracking and personalization. Copy the script from Customer Insights - Data or Customer Insights - Journeys. Scripts are customized for your environment, so it's important to copy and use the production script in your production website. If your script contains `allowIpAddressCollection`, you have the latest script.

- [Docs](real-time-web-personalization-overview.md)

## September 2026

### General availability

#### Convert a data source to Microsoft Fabric OneLake

Convert an existing Azure Data Lake Delta tables data source to a Microsoft Fabric OneLake data source and keep the tables, mappings, and downstream dependencies in place.

- [Docs](convert-data-source-to-fabric-onelake.md)

## August 2026

### General availability

#### Data enrichments reach general availability

The following data enrichments reached general availability in August 2026:

- [Microsoft Brands and Interests enrichment](enrichment-microsoft.md)
- [Microsoft Enhanced addresses](enrichment-enhanced-addresses.md)

#### Target right audience based on signals from earlier campaigns

Access the interaction data captured by Customer Insights - Journeys and use it in Customer Insights - Data segments to include how customers responded to your campaign. This capability enables customer experience teams to combine the power of unified profiles with insights from Customer Insights - Journeys.

- [Docs](journeys-interaction-data-segments-measures.md)

## July 2026

### General availability

#### Connect to a Microsoft Fabric workspace with inbound access protection enabled

For organizations that require enhanced control over connections to a workspace, you can connect Dynamics 365 Customer Insights - Data to a Microsoft Fabric OneLake workspace with inbound access protection.

- [Docs](connect-fabric-inbound-access-protection.md)

### Public preview

#### Increase agent accuracy by grounding the agent in customer insights

Use the Customer Insights MCP Server to enrich your chat and agent workflows with unified customer data and AI-generated insights.

- [Docs](mcp-server-tools.md)

## May 2026

### General availability

#### Track and manage daily processing in the performance dashboard

The new performance dashboard gives you the ability to instantly see the overall end-to-end performance and operational status of Customer Insights - Data while allowing you to dive into task details when needed.

- [Docs](performance.md)

#### Reduce alert fatigue with noise-free notifications

Customer Insights - Data detects and self-corrects transient issues. ​This improved capability shows up in fewer emails sent to admins and in activity logs that distinguish between transient issues and permanent failures, allowing you to eliminate alerts to admins and on-call support staff for transient issues.

- [Docs](data-refresh-notifications.md)

### Public preview

#### Use Microsoft Fabric OneLake as a data source

Easily explore and select customer data stored in Fabric OneLake for processing in Customer Insights - Data. The OneLake connector reads directly from your OneLake data, eliminating the need to copy or stage data.

- [Docs](connect-fabric-onelake.md)

#### Target right audience based on signals from earlier campaigns

Access the interaction data captured by Customer Insights - Journeys and use it in Customer Insights - Data segments to include how customers responded to your campaign. This capability enables customer experience teams to combine the power of unified profiles with insights from Customer Insights - Journeys.

- [Docs](journeys-interaction-data-segments-measures.md)

## April 2026

### General availability

#### Easily select field values when working with segment conditions

Creating segments in Customer Insights - Data is now faster, easier, and more accurate. Customer Insights - Data allows you to select from a list of valid display names for field values, so you don't need to enter obscure codes or keep track of what data values are expected for each field.

- [Docs](segments-overview.md#segment-builder-tips)


[!INCLUDE [footer-include](includes/footer-banner.md)]
