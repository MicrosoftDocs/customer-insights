---
layout: page
title: Configuring web apps for user analytics

---

To get started using user analytics for web apps, download the latest supported version of User Analytics [Web (React Native) SDK][JavaScript] and start sending data. 
 
### Key considerations with the Web SDK

1. Session Analytics are currently supported for single page applications only.
2. The `DeviceInfo.Id` property is managed automatically by the SDK, and thus should _not_ be set manually (doing so will disrupt or invalidate the device analytics calculations).
3. `DeviceInfo.Id` is populated by the SDK using a UUID, which is stored locally as a cookie. This means that every browser will counted as a separate Device ID, where individual browsers on a single machine are treated as separate devices.

# Managing sessions for web apps

To measure user engagement for web-based apps, the Aria JavaScript SDK currently provides a `logSession` API for programmatically managing session start and end events.  This feature, and autoinstrumentation of session events, are supported with version v1.4.0 and higher of the Web (React-Native) SDK. 

Just as with the Aria Android and iOS SDKs, the `Session.State` field will be emitted by the Web SDK and contains a value of either `Started` or `Ended`. The SDK computes Session Length from the timestamps of the Session Start and End events, and sends this value with the Session End event. The SDK also emits a duration bucket (`Session.DurationBucket` field) along with the session length for histogram visualizations.
Each event logged/sent within an ongoing session also includes the `Session.Id` property, enabling users to associate specific events with a given session. 

### Start Session sample

    var ariaLogger = new microsoft.applications.telemetry.Logger();
    
    ariaLogger.logSession(microsoft.applications.telemetry.SessionState.STARTED)
    
Common session start scenarios include when an application has been loaded for the first time, and/or once a user has been successfully authenticated.

### End Session sample

    ariaLogger.logSession(microsoft.applications.telemetry.SessionState.ENDED)

Common session end scenarios include when a user has signed out of an application, or prior to invoking the `window.onbeforeunload` event.  Under the latter condition, it is also a best practice to invoke `flush()` on the `LogManager` object, as doing so ensures that the SDK will attempt to synchronously send events currently in the queue.
    
    microsoft.applications.telemetry.LogManager.flush();

### Autoinstrumenting sessions

The SDK can send the session events automatically by setting `enableAutoUserSession` to `true` in the `LogConfiguration` object and passing it as the second parameter in the `LogManager.initialize()` method. The session start event will be sent during the `LogManager.initalize()` method and the session end event will be sent in the `window.onbeforeunload` event.

	var configuration = new microsoft.applications.telemetry.LogConfiguration();
	configuration.enableAutoUserSession = true;
	microsoft.applications.telemetry.LogManager.initialize("Your_tenant_token", configuration);

### Analysis

User Analytics now provides all available usage metrics for Web apps that have instrumented session start and session end events using the latest Web SDK.  This includes out-of-the-box 
charts for New Devices, Active Devices, Session Count(s), Session Length and Device Retention, as well as browser-specific splits across each.

#### Active Devices by app version & browser splits

{% img "how-to/user-analytics/active-devices.png" alt:"Category chart" class:"img-responsive" %}

#### Averagew session length by browser splits

{% img "how-to/user-analytics/avg-session-length.png" alt:"Category chart" class:"img-responsive" %}

### Also See:

* [Active Device Metrics]
* [New Device Metrics]
* [Session Metrics]

[JavaScript]: /developers/downloads/release-notes/javascript
[sending and examining events]: /developers/get-started/send-events/

[Active Device Metrics]: /developers/how-to/ua-active-devices
[New Device Metrics]: /developers/how-to/ua-new-devices
[Session Metrics]: /developers/how-to/ua-sessions
[Retention Metrics]: /developers/how-to/ua-retention
