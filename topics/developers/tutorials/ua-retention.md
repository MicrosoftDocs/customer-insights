---
layout: page
title: Retention metrics

---

Aria's device retention metrics enable teams to identify usage patterns once an app has been installed on a device, providing data points to gauge both stickiness and user churn. Retention metrics are automatically generated for your application when you instrument your app using the Aria Session event.

## Definitions

Metric       | Description              |
---------------|------------------------|
Daily device retention | Measures the percentage of returning devices per day over a 28 day window. The cohort is all devices on which the app was first used on a given day (Day 0).
Weekly device retention | Measures the percentage of returning devices per week over a 12 week window. The cohort is all devices on which the app was first used in a given week (Week 0).
Monthly device retention | Measures the percentage of returning devices per month over a 12 month window. The cohort is all devices on which the app was first used in a given month (Month 0).
1, 7, 14 and 28 day retention | 1, 7, 14 and 28 day retention rendered as a time series over a specified time range.
{: .table .table-striped }

## Analysis

The daily return rate metric captures the percentage of returning devices over a specified window, following first-time launch of an app (which is considered Day 0). For example, in the table below, all devices on which the app was launched for the first time on November 26th would fall within the same cohort; the return rate on each subsequent day of the 14 day window is calculated as a ratio of the active devices on a given day divided by the size of this cohort.

{% img "how-to/user-analytics/retention-table.png" alt:"Retention table" class:"img-responsive" %}

In addition to the device retention table, Aria also provides an out of the box chart rendering 1, 7, 14 and 28 day device retention as a time series.  This enables you to visualize the change in industry standard retention metrics for your app over time.  In this chart, the 7 day retention for November 23 (Day 0) would be the number of returning devices on November 30 ('Day 7').

{% img "how-to/user-analytics/retention-chart.png" alt:"Retention chart" class:"img-responsive" %}

By setting the time range to weekly, you can view the weekly device retention or return rate metric.  This view captures the percentage of returning devices over a 12 week window, following the first-time launch of an app (Week 0). For example, all devices on which the app was launched for the first time in the week November 21 - 27 would fall within the same cohort; the return rate on each subsequent week of the 12-week window is calculated as a ratio of the active devices in a given week divided by the size of this cohort.  Aria aligns the weekly retention chart to the fiscal week, that is, Saturday through Friday.

Similarly, you can set the time range to monthly and view the monthly device retention metric over a 12 month window.  Aria aligns the monthly retention chart to the calendar month, in other words, January, February, and so on.
