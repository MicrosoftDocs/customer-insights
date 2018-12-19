---
layout: page
title: Set transmit profiles

---

## Choose a transmit profile to customize your telemetry event transmission

Every time the Aria client library sends data to the Aria collector service, it consumes power and network bandwidth,
both scarce resources, especially on mobile devices. In addition, it might incur charges if a user is on a
metered network or roaming. The Aria client library exposes mechanisms to improve the utilization
of such resources. For example, certain types of event should not be sent (or sent a lower frequency)
depending on the state of the device, such as on a metered network. Another example is to batch events for
transmission instead of waking the device every time an event is logged, so as to conserve the battery.

However, client application doesn't have to think about all these device conditions and try to figure out
the optimal way to utilize them. Instead, it should focus on identifying the business value of an event
and decide on what the overall data transmission latency and throughput of the application would need.
For the former, an event could be specified as High, Normal or Low priority. For the latter it is what the
Transmit Profile setting client application could set to achieve its data latency and throughput goals
while utilizing resources in an optimal way.

The Aria client library supports three transmit profiles, namely `RealTime`, `NearRealTime`, and `BestEffort`. This setting
combined with the priority of an event determines how and how frequently the event will be transmitted to the Aria
collector service based on the device conditions. If none is specified, the `RealTime` transmit profile is used
by default.

### RealTime transmit profile

The `RealTime` transmit profile is intended for client applications to achieve real-time telemetry data availability.
It favors low data transmission latency, which might incur more power and/or bandwidth consumption even on a metered network.
This setting could also be used to service the need of testing during application development phase for quick verification
of the Aria client library and Aria pipeline.

### NearRealTime Transmit Profile

The `NearRealTime` transmit profile is intended for client application to achieve near-real-time telemetry data availability.
Client applications can choose this setting for a balance of conservation of device resources and having a data latency longer
than real-time but still achieving nearly real-time results.

### BestEffort Transmit Profile

The `BestEffort` transmit profile favors conserving device resources bearing longer telemetry data latency than that of
the `RealTime` and `NearRealTime` transmit profiles. This setting is intended for client applications whose telemetry data is less
time-sensitive and whose device resource conservation is a more important requirement.

With these profiles, it's expected that telemetry data will be submitted to the Aria collector service by the Aria client library
within a minute for the `RealTime` profile, 10 minutes for the `NearRealTime`, and 15 minutes for the `BestEffort` transmit profile settings.
Also note that Low priority events will not be transmitted, except for the `RealTime` transmit profile, unless it will not incur
additional cost to the client application in terms of resource consumption, which mostly means when device is on plug-in power
and on a non-metered network.

For more information, please refer to the [TransmitProfile](/developer/api/aria-sdks/ios/logmanager/settransmitprofile)
reference documentation.
