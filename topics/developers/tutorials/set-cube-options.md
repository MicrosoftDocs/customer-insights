---
layout: page
title: Set cube options

---

## Advanced options for cubes

When you create a new cube, you will see the small switch at the bottom right corner of the screen that says **Show advanced settings**. With this enabled, you will see two settings that you can change: **Timestamp**, and **Base granularity**.

### Timestamp

When you send Aria data, you are probably setting the timestamp which is the `EventInfo.Time` by default. If you are creating a sales event, the timestamp will be when the sales happened. If you're sending a button click event, the timestamp will be when the click happened, not when the data was sent.
Therefore, when you set up a dashboard, you will see correct time reflected on your graph. If you sent the data in a big batch a week after the sales or clicks, the graph will still show the correct time.

However there are times when this behavior is not desirable. Some devices do not have correct times set, and will be sending events that insist on sales from the 1970s. This is very unlikely, unless the user time travels regularly to the 70s. If a lot of your data comes from devices with wrong times, it may make sense to use the ingestion time (when Aria got your data) instead of the event time.
You can select `PipelineInfo.IngestionTime` from the dropdown to use the received time for your data.

{% img "how-to/set-cube-options/timestamp.png" alt:"Timestamp" class:"img-responsive" %}

### Base granularity

Aria's aggregate service does exactly that - aggregate. You specify what data Aria should inspect and aggregate, and it does so. The data is then updated in buckets of 5 minutes. For an hour's data we usually have 12 buckets and will show aggregated values for 10:00 - 10:05, 10:05-10:10 and so on.

For some users, this granularity may be too coarse (or too fine). If that is the case, you may wish to change the granularity.

For high resolution data, select smaller granularity. Note that you may be subject to stricter cardinality limitations.

{% img "how-to/set-cube-options/granularity.png" alt:"Granularity" class:"img-responsive" %}
