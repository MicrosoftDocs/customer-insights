---
layout: page
title: Export data to Cosmos
internal: true
---

Aria has the capability to stream incoming raw data to Cosmos.  This enables teams with existing Cosmos presence to add data from Aria to their existing data sets and also enables large scale batch processing over data sets.

To use the Cosmos data export service, you should already have a virtual cluster (VC) in Cosmos and have approval to land new data in this VC.

**Note**: If you are in SfC, please contact <a href="mailto:skypecosmosreq@microsoft.com">Skype Cosmos Requests</a> to discuss self service, because this is centrally managed at present (November 2016).

## Supported Clusters

We currently support these physical Cosmos clusters:

* cosmos08
* cosmos09
* cosmos11
* cosmos14
* cosmos15 (since 2016-11-02)

If you have a VC on another physical cluster, please contact us for more information to set this up.


## Prerequisites

Before configuring a Cosmos export resource, you should complete these steps:

1. Identify the events that you want to send to Cosmos
1. Create a directory in your Cosmos VC in which to land the data
1. **Share the directory** you created to the ARIA upload cluster with **write access** provided.  This upload cluster will vary depending on where you are located as detailed below.  Please ensure you share to the correct VC.

These are the VCs to which you must share:

* cosmos08: share to **aria.prod.upload08**
* cosmos09: share to **aria.prod.upload**
* cosmos11: share to **skypedata.prod.upload**
* cosmos14: share to **aria.prod.upload14**
* cosmos15: share to **aria.prod.upload15**

 You need to wait at least 30 minutes after your share is created before creating your resource (there is Cosmos latency to create the share).

Here is an example of configuring a Cosmos share and which parameters to use when defining an Aria Cosmos export:

{% img "how-to/exports/Cosmos.png" alt:"Cosmos share settings" class:"img-responsive" %}

## Creating the export

Before you set up export:

* Follow the prerequisite steps.
* Click **Applications** on the sidebar menu, and then **Management** and **Export Manager (Cosmos)**. Alternatively, from Explorer, click **Add**, then **Cosmos export**.

{% img "how-to/exports/CosmosAdd1.png" alt:"Cosmos share settings" class:"img-responsive" %}
{% img "how-to/exports/CosmosAdd2.png" alt:"Cosmos share settings" class:"img-responsive" %}

* Enter a name and description for the export
* Choose the Physical Cosmos cluster name
* Enter the name of the VC in which you previously created the folder
* Enter the name of the share you created on the VC and shared to your upload VC ( __Note: Share names are CaSe SeNsItIvE!__ )
* For the event names you should enter one or more event names that you are sending to Aria
* Set the metadata filter and time settings (see below for more details)
* Click **Update** to commit the changes

Within 5 minutes you should be able to see data landing within Cosmos as long as new data is arriving in Aria.

### Metadata filtering level

By default, when data is sent to Cosmos, we pass the actual data records as well as all metadata about the records (each stage of our pipeline adds additional receipt and timestamp information).  In most cases, this data is not required and you only need the actual record data.  You should choose one of these options:

* Events only: all metadata is filtered out, leaving just the pure data records.  This results in the smallest data size in Cosmos and is the recommended model.
* Events and receipts: all receipts are filtered out, reducing the size of data sent to Cosmos.
* Events, receipts, and metadata: nothing is filtered, and all metadata is sent.

### Data timestamp

There are two options for how data is bucketized when landing in Cosmos.

1. Cosmos upload time: The time the data was processed by the export service.
1. Event time: The actual event time when it was logged on the device/service.

You can choose either model.  In the first model (time the data was uploaded to Cosmos), at the end of a day you know that the daily buckets are complete and will never be written to again.  This is the recommended and default option for exporting data.

In the second model (actual event time) there can be late arriving data written into older buckets.  For example if an event was logged yesterday, but was delayed in transmission and arrived today, it would be written to yesterday's files.  This means that any processing you do on data might need to look back to historic files, as new data could have arrived.

## File Structure

Once your request is processed and your data is streaming to your VC, you will see the data land in your VC on an ongoing basis.  Aria streams data as it arrives throughout the day.  By default, data is split across four files (buckets) per day.  This data is sharded across the files throughout the day to balance out I/O in Cosmos. It is not written sequentially, so you will see all files grow evenly throughout the day, and they will only be completed at the end of the day.

You can control the number of files, file naming, and data retention if required by creating or modifying the `streamset.ini` file in the root directory in which your data lands.  You can read more about [streamsets and controlling the configuration][6].

The default file structure is as follows:

    targetpath/ENV/eventname/YEAR/MONTH/eventname_YEAR_MONTH_DAY.log_bucketN

Where

* ENV is the source ARIA environment the event originated from – currently INT or PRD
* YEAR is the year the data was written to Cosmos
* MONTH is the month the data was written to Cosmos
* DAY is the day the data was written to Cosmos
* N is the bucket number, from 0..3

If "Single Stream For All Events" has been configured, then the eventname above will be `datastream`.

Currently, Aria writes daily streams (sharded across four buckets by default). If you need to process data throughout the day, you can process against the streams but should use the `WITH TIMERANGE` Cosmos option to [scope your processing to a known complete time window][7].


## Data format

Cosmos uses a binary format for data landing in Cosmos. The full data records are sent to Cosmos so you have access to all fields within the records.  This means that the contents of each bucket cannot be directly viewed within the Cosmos web explorer.  Before using the data, you must first extract it to a structured stream or tab-delimited stream.  This is a common first step in processing raw data in Cosmos.  At this stage, you should do any data scrubbing, data deduplication or pre-processing required for raw data to build structured streams as required by your further data pipelines.

## Aria users

### Binaries

In order to extract your data in Cosmos, use the AriaExtractor and its [supporting binaries][5], and are also shared to all VCs via one of the following paths:

* cosmos08: `/shares/aria.prod.upload08/AriaExtractor/latest/`
* cosmos09: `/shares/aria.prod.upload/AriaExtractor/latest/`
* cosmos11, cosmos14, cosmos15: `/shares/skypedata.adhoc/AriaExtractor/latest/`

For more general information about using Cosmos, refer to the [Cosmos][0] or [Scope Studio][4] Sharepoint sites.

### Code sample:

The following is an example of a Scope script for extracting the raw binary event data into a set of columns which can be output to a structured stream (`SSTREAM`) or tab-delimited format.


{% highlight powershell %}

// for cosmos08 use /shares/aria.prod.upload08/AriaExtractor/latest/
// for cosmos09 use /shares/aria.prod.upload/AriaExtractor/latest/
REFERENCE @"/shares/skypedata.adhoc/AriaExtractor/latest/Microsoft.Bond.dll";
REFERENCE @"/shares/skypedata.adhoc/AriaExtractor/latest/Microsoft.Bond.Interfaces.dll";
REFERENCE @"/shares/skypedata.adhoc/AriaExtractor/latest/Microsoft.Bond.Rpc.dll";
REFERENCE @"/shares/skypedata.adhoc/AriaExtractor/latest/protobuf-net.dll";
REFERENCE @"/shares/skypedata.adhoc/AriaExtractor/latest/Skype.Data.Common.IO.Ray.dll";
REFERENCE @"/shares/skypedata.adhoc/AriaExtractor/latest/ASG.Telemetry.Extractor.dll";
REFERENCE @"/shares/skypedata.adhoc/AriaExtractor/latest/ASG.Telemetry.Schemas.dll";
USING Microsoft.Applications.Telemetry.Extractor;

// EVENT_NAME is the event being exported from Aria.  Use 'datastream' if configuring
// all events to export to a single stream.
#DECLARE EVENT_NAME     string = @"datastream";

// EVENT_FOLDER is the VC folder path configured in Aria to receive your event
// streams.
#DECLARE EVENT_FOLDER   string = @"/local/ARIAScratch/androidexp";

// The start date (inclusive) of the streams to extract from.
#DECLARE START_DATE      string = @"2015-07-01";

// The end date (inclusive) of the streams to extract from.
#DECLARE END_DATE        string = @"2015-07-01";

// Do not edit these.  These have a pre-determined format, and are constructed from
// EVENT_NAME & EVENT_FOLDER above.
#DECLARE STREAMSET_PATH     string = string.Format("{0}/prd/{1}/", @EVENT_FOLDER, @EVENT_NAME);
#DECLARE STREAMSET_PATTERN  string = string.Format("%Y/%m/{0}_%Y_%m_%d.log_bucket%n", @EVENT_NAME);

// Extract the events from the streams.  This will extract the following columns:
//   EventInfo_Time        - Client time during event creation, in UTC (DateTime)
//   EventInfo_Name        - Name of the event
//   EventInfo_SdkVersion  - Aria SDK Version used to log the event
//   AppInfo_Id            - Aria tenant id, unless overridden by ISemanticContext.SetAppId()
//   ...
// The first 4 columns are always extracted.  Specify the custom properties to be extracted
// to the AriaExtractor().  For example, specifying:
//   USING AriaExtractor("CustomA", "CustomB")
// will extract the custom properties "CustomA" and "CustomB" as columns 5 and 6 during the
// extraction.  If the property names have '.' in them, they will be replaced with '_' in
// the resulting column names.
EXTRACT *
FROM STREAMSET @STREAMSET_PATH
     PATTERN @STREAMSET_PATTERN
     RANGE __serialnum = ["0", "3"],
           __date = [@START_DATE, @END_DATE]
USING AriaExtractor("UserInfo.Id", "DeviceInfo.Id", "DeviceInfo.OsName");

OUTPUT
TO SSTREAM @"/my/TestOutput.ss";

{% endhighlight %}

Update the following parameters in the sample:

- `EVENT_NAME`: set to the name of the exported event
- `EVENT_FOLDER`: set to the target path of your event streams
- `START_DATE`: set to the start date (inclusive) of the event streams
- `END_DATE`: set to the end date (inclusive) of the event streams
- `AriaExtractor(...)`: update with the properties to be extracted

## ODIN and Vivace Self-Serve Users

The section below details how you can configure a specific Data Export to Cosmos, so that your data is automatically processed to be made available in [ODIN][12]. This section also covers how you can setup [Vivace][15] for your experimentation needs.

### Cosmos Data Export setup for ODIN

Please choose the right Cosmos cluster depending on where you want to consume the data:

* cosmos09 if you consume your data on cosmos09.
* cosmos14 if you consume your data on cosmos11 or cosmos14.

Common settings:

- **Name**: for example, "Aria ODIN Cosmos Export"
- **Description**: for example, "Export Aria events to AriaODIN cooker"
- **Event Types**: enter the Event Type names (comma-delimited) that you want send to ODIN; you can use the wildcard * to send all Event Types defined in your tenant.
- **Event Streams**: Select "Single Stream for All Events"
- **Metadata Filtering Level**: Receipts only
- **Partition Time Setting**: Leave the default values.

cosmos09 settings:

- **Physical Cluster Name**: `cosmos09`
- **Target VC Name**: `searchDM.upload`
- **Share Name**: `Aria`

Cosmos14 settings:

- **Physical Cluster Name**: `cosmos14`
- **Target VC Name**: `OBD.prod`
- **Share Name**: `Aria`

### AriaODIN cooker

Once the Cosmos Data Export is configured following the above guidelines, your data will be automatically processed and available in ODIN within 24 to 48 hours. For a more detailed timeline:

- T1: Cosmos Export resource created (data pumped to Cosmos within 15 mins).
- T2: The AriaODIN cooker will wait until a complete day’s data is available (UTC time zone).
- T3: At 0:00 UTC, cooking will start, and the data will be available in ODIN by 12:00 PM UTC.

The cooker also supports hourly cooking. At the moment, this requires some manual configuration, so please reach out to `asgdtmao@microsoft.com` for more details if you're interested.

### Access data via ODIN

Once your data is ready, you can access it through the [ODIN Event View][13]. If you have onboarded with the Semantic API and are familiar with the Action concept, it's recommended you access your data through [ODIN Action View][14].

### Using Vivace for experimentation

1. Please refer to [ECS instrumentation][9] and [ECS Telemetry][10] to onboard ECS.
2. Please make sure `AppInfo.ETag` is populated for your events.
3. Please check [Get started on Android][11], section 5 for more examples.

Please refer to [Vivace OneNote][16] for details on how to use Vivace.

## Existing Skype Data RV users

### Binaries:

In order to extract your data in Cosmos and use some helper functions, you need the SkypeDataExtractor and supporting binaries.

SkypeDataExtractor is available in NuGet here at `Microsoft.Skype.Data.CosmosExtractor`.

A sample [Scope Studio project][1] is available that contains all the required binaries.  You should start with this project for your first SCOPE scripts.

The latest version of the SkypeDataExtractor is also available in a share from `skypedata.adhoc`.  This is shared to all VCs on cosmos11.  You can access this from your own VC here:

`/shares/skypedata.adhoc/CosmosExtractor/Latest/`

More [details on using the extractor and working with your data in Cosmos][2].

## FAQs

Please see [Help > FAQs > Cosmos](/help/FAQs/cosmos)

[0]: http://aka.ms/Cosmos
[1]: https://microsoft.sharepoint.com/teams/SkypeData/SiteAssets/SkypeData%20Wiki/SkypeDataExtractor%20for%20Cosmos/SkypeDataExtractorExamples-v3.zip "Extractor"
[2]: https://microsoft.sharepoint.com/teams/SkypeData/_layouts/15/start.aspx#/SkypeData%20Wiki/SkypeDataExtractor%20for%20Cosmos.aspx "Wiki"
[4]: http://aka.ms/ScopeStudio
[5]: ./AriaExtractor.zip
[6]: https://www.bingwiki.com/index.php?title=Streams_and_Streamsets
[7]: https://microsoft.sharepoint.com/teams/Cosmos/_layouts/15/start.aspx#/Wiki/WITH%20TIMERANGE.aspx
[8]: /developers/api/aria-sdks/service/action
[9]: /developers/how-to/instrument
[10]: /developer/how-to/telemetry
[11]: /developers/get-started/tutorial-per-platform/android-java-start
[12]: http://odin/
[13]: http://odin/?tab=office-event-view
[14]: http://odin/?tab=office-action-view
[15]: http://vivace/#!/Home
[16]: https://microsoft.sharepoint.com/teams/MetricsAndReporting/_layouts/15/WopiFrame.aspx?sourcedoc=%7b3c0e871e-7484-4df9-b3ec-f7fb6bef6981%7d&action=edit
