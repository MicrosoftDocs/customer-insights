---
layout: page
title: Active device metrics

---

Aria offers daily, weekly and monthly active device metrics out of the box, both in aggregate and split by standard dimensions.  Aria counts any device from which a session event is generated in the selected time range as an active device.

## Definitions

Metric       | Description              |
---------------|------------------------|
Daily Active Devices (DAD)		   | Measures the number of unique devices with at least one app session for the specified day.
Monthly Active Devices (MAD)	| Measures the number of unique devices with at least one app session for the specified calendar month.
Weekly Active Devices (WAD) | Measures the number of unique devices with at least one app session for the current fiscal week (from Saturday to Friday).
{: .table .table-striped }

## Identifying devices

A device identifier is automatically collected from a given platform and always reported by the Aria telemetry library; no code is required to generate out of the box metrics on new devices. 

To calculate distinct devices, Aria applies the [HyperLogLog] approximation algorithm (to estimate cardinality) on the `DeviceInfo.Id` field of each event, which has a standard accuracy rate of 98%. For a list of all available fields, see the [Common Properties] document.

The following platform APIs are used by their respective SDKs to collect and populate `DeviceInfo.Id`: 

Platform       | API              |
---------------|------------------------|
Android		   | `ANDROID_ID` property (`Settings.Secure` class)
iOS 		   | `identifierForVendor` property (`UIDevice` class)
{: .table .table-striped }

> **Note**: The `DeviceInfo.Id` value is not guaranteed to persist across multiple app installs on the same device.

## Analysis

Active devices can be examined with the following types of chart:

* A time series chart, which consolidates all supported dimensions into a single line over a given date range.
* Individual charts split by each supported dimension (platform, app version, and so on), displayed by percentage of distribution over a given date range.  Each chart is filtered by top N values (indicated in the chart title).

{% img "how-to/user-analytics/active-devices.png" alt:"Category chart" class:"img-responsive" %}

[HyperLogLog]: http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf
[Common Properties]: /developer/do-more/working-with-data/common-properties
