---
layout: page
title: Session Metrics

---

Aria provides Session Length and Count metrics out of the box, both in aggregate and split by standard dimensions.

## Definitions

Metric       | Description              |
---------------|------------------------|
Session length |Measures session length in eight buckets or duration ranges.
Session count  |Measures the total number of sessions over a given period across all users.
{: .table .table-striped }

## Tracking Sessions

Aria tracks the count and duration of user sessions over a specified time range, and supports two options for collection and reporting:

* **Automatic**: When an app has been configured to use Aria's automatic lifecycle feature, the SDK will automatically detect a session start when an app moves into the foreground, and a session end when the app moves into the background.
* **Manual**: Apps can be explicitly instrumented to manage their own session start/end rules programmatically with the `logSesssion()` API.

Under both configurations, the `Session.State` field will be emitted by the SDK and contain a value of either `Started` or `Ended`.

The Aria SDK computes the session length from the timestamps of the Session Start and End events, and sends this value with the Session End event. The SDK also emits a duration bucket along with the session length for generating histograms.

> **Note**: Automatic session management is _not_ currently supported for web apps.  To take advantage of user analytics for web-based apps, see [Configuring UA for Web apps][2].
 
### Android Sample

	//Manual Mode
	Ilogger ariaLogger = LogManager.getLogger();
	EventProperties eventProps = new EventProperties("sessionStartMetadata");
	eventProps.setProperty("property","value");
	
	ariaLogger.logSession(SessionState.STARTED,eventProps); //can also pass null as 2nd parameter
	ariaLogger.logSession(SessionState.ENDED,null); //EventProperties can be passed as an optional parameter

### iOS Sample

	ACTLogConfiguration* config = [ACTLogConfiguration new];
	[ACTLogManager initForTenant:MYTENANTTOKEN configuration:config];
	id<ACTILogger> ariaLogger = [ACTLogManager logger];
	
	ACTEventProperties* eventProps = [ACTEventProperties new];
	eventProps.eventName = @"sessionStartMetadata";
	[eventProps setValue:@"value" forProperty:@"property"];
	
	[ariaLogger logSessionWithState:SessionStateStarted eventProperties:eventProps];
	// Can also be called without passing the eventProp via: [ariaLogger logSessionWithState:SessionStateStarted];
		
	[ariaLogger logSessionWithState:SessionStateEnded];
	//EventProperties can be passed as an optional parameter via: [ariaLogger logSessionWithState:SessionStateEnded eventProperties:eventProps];

## Session Event Data Model
Aria emits a Session event when the `LogSession()` API is used. See the [Session Data Model][1].
	
## Analysis
Aria offers the following out of the box charts for examining session usage:

#### Session Counts, available both aggregated and split by standard dimensions. 

{% img "how-to/user-analytics/daily-session-count.png" alt:"Category chart" class:"img-responsive" %}

#### Session Length histogram (aggregate only)

{% img "how-to/user-analytics/session-length.png" alt:"Category chart" class:"img-responsive" %}

#### Average Session Length histograms split by standard dimensions.

{% img "how-to/user-analytics/avg-session-length.png" alt:"Category chart" class:"img-responsive" %}

[1]: /developers/how-to/ua-session-data-model
[2]: /developers/how-to/ua-web
 
