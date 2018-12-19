---
layout: page
title: New device metrics

---

Aria offers daily, weekly and monthly new device metrics out of the box, both in aggregate and split by standard dimensions.  Aria identifies a new device based on first-time launch after an app has been installed.

## Definitions

Metric       | Description              |
---------------|------------------------|
Daily new devices (DND) | Measures the number of unique devices (not previously seen) with at least one app session for the specified day.
Monthly New Devices (MND) | Measures the number of unique devices (not previously seen) with at least one app session for the specified calendar month.
Weekly New Devices (WND) | Measures the number of unique devices (not previously seen) with at least one app session for this fiscal week (that is, from Saturday to Friday).
{: .table .table-striped }

## Identifying Devices

A device identifier is automatically collected from a given platform and always reported by the Aria telemetry library; no code is required to generate out of the box metrics on new devices. 

The Aria SDK caches the first launch time on the device and sends this value with each session event.  When computing the new device metric, Aria determines if a device is new for the selected time interval (day, week, or month) by applying a custom function for Current Time - First Launch Time.   The first launch time value cached by the Aria SDK persists across application upgrades and OS upgrades, but not if the application is reinstalled.

To calculate distinct devices, Aria applies the [HyperLogLog] approximation algorithm (to estimate cardinality) on the `DeviceInfo.Id` field of each event, which has a standard accuracy rate of 98%. For a list of all available fields, see the [Common Properties] document.

The following platform APIs are used by their respective SDKs to collect and populate `DeviceInfo.Id`: 

Platform       | API              |
---------------|------------------------|
Android		   | `ANDROID_ID` property (`Settings.Secure` class)
iOS 		   | `identifierForVendor` property (`UIDevice` class)
{: .table .table-striped }

> **Note**: The `DeviceInfo.Id` value is not guaranteed to persist across multiple app installs on the same device.

## Analysis

New devices can be examined with the following types of chart.

* A time series chart, which consolidates all supported dimensions into a single line over a given date range.
* Individual charts split by each supported dimension (platform, app version, and so on), displayed by percentage of distribution over a given date range. Each chart is filtered by top N values (indicated in the chart title).

{% img "how-to/user-analytics/new-devices.png" alt:"Category chart" class:"img-responsive" %}

[HyperLogLog]: http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf
