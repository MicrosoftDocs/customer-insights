---
title: View data reports
description: Use the available reports to see real-time activity on your site.
author: darrinw-docs
ms.reviewer: mhart
ms.author: darrinw
ms.date: 10/01/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# View reports

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A report is a collection of data visualizations, using the data collected through the SDK, that help you measure and understand user behavior. Dynamics 365 Customer Insights engagement insights include out-of-the-box (OOB) reports for web and mobile projects.  

## Web reports

You can access web reports under **Discover** in the left navigation pane.

:::image type="content" source="media/report-menu.png" alt-text="Navigation showing the list of available reports.":::

### Real-time usage report

The  **Real-time usage** report provides an overview of current activity on your site that automatically refreshes every minute. Use real-time usage to monitor the impact of marketing campaigns, press events, and other scenarios on your site's traffic.

### Key metrics reports

- **Page views** list the page views for individual pages along with the number of total page views over the selected time frame.

- **Visits** show information about the number of visits and the visit duration.

- **Visitors** inform about new and returning unique visitors to your site.

### Content reports

- **Links** show information about the number and type of clicks.

- **Exit pages** list the links that visitors clicked to exit your site.

### Traffic sources reports

- **Referrers** list the domains and URLs that referred visitors to your site.

- **Tracking codes** provide details about the tracking codes in the links that brought visitors to your site.

### Visitor profiles reports

- **Devices** list the physical devices that were used to access your site.

- **OS & browsers** provide insights into the operating systems and browsers that were running when accessing your site.

- **Locations** show information about visitors by country, region, and city.

- **Languages** list page views by the visitor's preferred languages.

## Mobile reports

Mobile reports are grouped in real-time usage, app, and user categories. You can access mobile reports under **Discover** in the left navigation pane.   

:::image type="content" source="media/mobile-reports.png" alt-text="User interface of engagement insights showing the real-time usage report that renders data in charts and lists.":::   

### Real-time usage

**Real-time usage** provides an overview of current activity in your mobile app that automatically refreshes every minute. Use real-time usage to monitor the number of users and sessions currently active in your app and the top screen views.

### App reports

- **Screen views** list screen views for individual screens in an app and the total number of screen views over a selected time frame. You can view screen views by screen name or by screen title.

- **Sessions** show information about the number of sessions and the session duration.

- **Return frequency** groups session counts by the number of days since the last session.

- **Users** show new and returning users in your mobile app.

- **Events** list all the events collected from your app, plus the total count for each event.

### User reports

- **App versions** list the versions of your mobile app in use by your user base.

- **Devices & OS versions** provide insights into which devices and operating systems are running your mobile app.

- **Locations** show information about app users by country, region, and city.

## Filter by time or date range

You can select the time frame or date range in a web or mobile report to focus on a value or time period. 

- To select a time frame, in the upper-right corner of the report view, select a value from the dropdown list of the report. You can also choose a **Fixed date range**. 

  :::image type="content" source="media/filter-by-time.png" alt-text="Filter by time or date range.":::   

- For most reports, select a value in a chart or list to filter the report.

> [!NOTE]
> Time range selection is disabled for a real-time usage report; the time range for a real-time usage report is “now.”


[!INCLUDE[footer-include](../includes/footer-banner.md)]
