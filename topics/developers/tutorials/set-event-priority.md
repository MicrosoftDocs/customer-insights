---
layout: page
title: Set event priority

---

When you send data, you can set priority for events. High priority events are likely to be sent first, and given preference in local storage.

## Batching and priority

Aria client SDKs optimize for network usage, through efficient use of batching. A single HTTPS POST request from the SDK to the collector is allowed to be a maximum of about 2.8 MB in payload. The SDK tries to pack as many events as it can, in order to fit into this 2.8 MB limit.

But there is also a time limit. For example, if there are only a few events to send, and the timer has fired (meaning, that the events need to be sent now), then the SDK will batch those few events itself, and send it in a POST request. In this case, the payload might very well be far less than 2.8MB.

**Events of each priority are in their own batches. Thus there will be a batch for high priority, another for normal priority, and another for low (assuming there are events of each type of priority).**

## Local storage and priority

For all priorities, in iOS, macOS, and Android SDKs, the events are stored as soon as they come in. In the C++ SDK, it's a bit different: only the high priority events get stored right away; the events with other priorities get stored only when you call `Flush()` or when the in-memory queue gets filled up.

The events are removed in a first-in, first-out manner, as well as based on priority. When the transmission thread needs to send events over the wire, for every timer interval, it will pick up events from the storage by order of priority, and send them over.

In case the storage is full, the events are dropped. The logic used to select the events to drop is as follows: Select a set of events from the earlier time and lowest priority, and remove them to make way for new events. If more space is needed (for example, when new telemetry events are coming in at high pace), then continue to drop events of lowest priority. Once those are over, then move on to next highest priority, and so on.

The size of local storage is configurable. The default is 3 MB.

## Custom transmission profiles and priority

You can set a different transmission profile to cater for your scenario. This means you can give your own timer values for each of the combinations of event priority, network state, and power state. See more on [how to specify the values and pass them to the SDK, and so on](/developers/deep-dives/client-sdk).

Note that timer values have to be in seconds (a positive integer value) and each must be a multiple of the higher priority. That is, whatever value of the timer you specify for high priority events, the timers for normal priority must be a multiple of the high priority timer, and the low priority events timer must be a multiple of normal priority timer. If the numbers passed in are not multiples, the SDK will automatically take it to be the ceiling of the closest multiple.

A [more comprehensive discussion of the client SDK and transmission options](/developers/deep-dives/client-sdk) is available.
