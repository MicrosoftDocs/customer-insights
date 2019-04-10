---
uid: developers/articles/glossary
title: Glossary of terms
author: vroha
description: Glossary of terms
ms.author: hakrou
ms.date: 03/29/2019
ms.service: dynamics-365-crossapp
ms.topic: conceptual
---
# Glossary of terms

## aggregated data

Product Insights performs calculations as defined by your cubes, then stores the
aggregated results. You can use such calculated aggregation values for
your visualisations.

## aggregated metric

A metric that accumulates over time, such as a count of items.

## cardinality

Number of total realized dimensions in a cube in a specified aggregation
period. If you defined a measure to be dimensioned by OS and
Platform and, for example, you get data for three operating systems
and four platform types in aggregation period T, you'd have a total
cardinality of 12 for T. This number can grow extremely fast depending on
the type of dimension you define. If you use IDs as a dimension property
(_not_ recommended!), then cardinality could hit millions in seconds.
High cardinality usually means poor performance of your cube, and by
extension your visualisations. Especially for distinct counts and
percentiles, we advise that you keep your cardinality low.

## cardinality capping

Cardinality capping is a configuration applied to cubes in the Product Insights
portal, to ensure that they can be served without any degradation in
performance.

## Collector

The Collectors ingest event streams from the SDKs.  If event fields
are tagged in the SDK, the Collectors scrub the PII (personally
identifiable information) in the events. If they are within the Product Insights
compliance boundary, the enterprise apps and services can maintain
their compliance. They provide a compatibility layer to support legacy
events and protocols. They are deployed worldwide in Azure behind a
DNS load-balanced endpoint. They are designed for low latency
(important for mobile devices), high availability, and resiliency
against data loss. They scale horizontally and can absorb spikes in
the data volume.

Product Insights Collectors are a group of Azure VMs that receive data from those
who send Product Insights data, using the Product Insights SDK.

## cube

A cube is a configuration you create to perform aggregate calculations
on streaming data. For example, you define a cube that gets a distinct
count of users. The results are processed and stored by the Real-Time
Aggregation service. Data created by cubes can be visualised in the
portal, and saved as dashboards.

## derived property

A derived property is computed from one or more **signal properties**
using custom functions.  Examples: a URL-normalizing function, or a
string replace function.

## dimensions

A cube defines aggregation operations to be performed by setting up
measures and dimensions. A total number of users (measure) divided
into country of origin (dimension) is an example. You create a
dimension by specifying which event property you would like to use to
divide the data.

When defining dimensions, keep in mind that high cardinality will
impact performance. See [cardinality](#cardinality).

## drill down, drill into 

See [split property](#split-property).

## dynamic

Properties such as App Version contain values that appear and
disappear on a regular cadence.  A **derived property** can be used as
a **split property**.

## e-tag

See [experiment tag](#experiment-tag).

## Event Explorer

The Event Explorer enables you to sample your recent events in
real time as the data flows through the pipeline. You can launch the
event explorer from the Portal in the taskbar on the left.

## event properties

Data sent to Product Insights are essentially a collection of key-value
pairs. These are also referred to event properties. If you sent
country code, action taken, and button pressed, these three are all
event properties over which you can run aggregation operations, such
as total number of events from the UK, or number of certain actions
taken.

## experiment tag

A data field whose contents are a hash of all of your experiments.

## experimentation

Also known as A/B experimentation.  Enables assignment of custom
attributes (such as setting or behavior) based on target parameters to
specific users or devices.  For example, target devices might include
those in the European Union, Android users, or Japanese-speaking users
of Windows 10. During experimentation, only data is sent to remote
devices, not code, but the data can influence which code is running.

## filters

In your visualisation, you can choose to see your data
'filtered'. Number of users filtered by the specified OS type would be
an example.

## flights

Actual experimentation "in flight" (in use), as determined by the
experimentation configuration. With a flight, you can determine why a
client was given certain data.  For example, for one flight, you might
make the title of a page red for a specified group of users.

## funnel

An Product Insights feature that can measure the conversion rate of
users at various steps in a signon or purchase process (for example).
For example, what is the point in a signup process at which many
people quit before converting?

## GDPR

See [NGP](#ngp).

## Geneva

[Geneva](https://aka.ms/geneva) is an Azure service.
See /developers/articles/telemetry/ (link tbd) for more information.

## impression ID

Identifier of the currently running flights, hashed to be more compact
and hide data from the user for security.

## ingestion token

A token used by an app to pass data to the [Collector](#collector).

## Kusto

[Kusto](https://aka.ms/csl) is an Azure service, a Big Data log search
and text analytics cloud service, developed by a team split between
ILDC (Microsoft Israel Development Center) and Redmond.  It is tightly
integrated with Product Insights, and offered as part of Product
Insights. It is a very fast in-memory database and a premium resource.

## measures

Measures are aggregated values that are computed from streaming
data. To transform data from your events into measures, you can define
the measures to be calculated in a cube.  Measures can be arithmetic
which computes average, count, max, sum, standard deviation and
variance. They can also be distinct counts or percentiles. Please note
that with percentiles and distinct counts, cardinality is very
important. This means not defining too many dimensions by
which events' property values will be divided.  Count measures can be
performed on non-numeric values, but no mathematical operations.

## metrics

See [measures](#measures).

## network provider

In the context of Product Insights, this has the usual meaning.  For
example, the network provider for a specified phone might be AT&T or
Verizon.

## NGP

NGP (Next Generation Privacy) is a company-wide effort sponsored by
the SLT to address new world-wide privacy regulations like the EU’s
General Data Protection Regulation (GDPR).

## page action

There are two types of page action: web page actions (for example,
page loads), and physical actions (for example, mouse clicks).

See [event properties](#event-properties).

## PII

Personally Identifiable Information is any data that could potentially
identify a specific individual. If your data to Product Insights
contains any such data, you should use PII tagging to ensure data
privacy.  Find out how you can handle PII data.
Product Insights uses the
nomenclature of _EUII_ and _OII_.  For more information, see /developers/articles/office-compliance/ (link tbd).

## project

A project is typically a team or a single user account that sends a
group of events and owns resources such as dashboards and cubes.

Formerly, **tenant**.

## project ID

A unique identifier for a [project](#project).
Automatically assigned by the Product Insights service upon project creation.
Your project ID is also your Kusto (raw event) database ID.
Formerly, **tenant ID**.

## property functions

Product Insights property functions allow users to interact with incoming data
points (measures or dimensions) to extract and derive new values based
on a pre-defined set of operations or conditions. Data output from
property functions is then aggregated by RTA, and exposed for
visualization and analysis via the real-time cube where it was
configured.
Common scenarios for applying property functions:

- Counting of non-empty values
- Duration/time extraction and conversion

## raw data

Raw data refers to raw events sent by users to Product Insights.
See [event properties](#event-properties).

## resource

Resources are a core concept in ARIA. Resources are used to provide
configuration to the ARIA services that are available. As more
services and data applications are released, the number of resource
types will increase.

Any time you need to configure a specific ARIA service you will either
create or edit an existing resource. By default a new tenant has no
resources. Some resources are generated automatically as you send data
to ARIA but the majority are created by a tenant administrator or
contributor. All resources must belong to a single tenant.

## RTA - Real-Time Aggregation service

The Real-Time Aggregation (RTA) service provides near real-time
cubes. It computes metrics from raw events in near real-time and
powers dashboards and REST APIs for rich query on the metrics. It
enables monitoring KPIs and performing multi-dimensional analysis on
them. Tools such as Power BI and R can be connected to RTA. It stores
the aggregates in a compressed column store in Azure blobs.

RTA is a powerful tool to analyse your data in near real time, as the
data flows in, rather than process raw data in scheduled batch
processing. While there are still plenty of use cases for large scale
map-reduce batch operations on raw data, by leveraging the RTA service
you can get up to date insight into your user population and service
health.

## SDK

"SDK" stands for "Software Development Kit".  Each SDK enables basic
logging and semantic instrumentation. The logging APIs generate an
event with the specified name and event fields. The semantic APIs
prescribe a standard set of fields for common types of events such as
metrics, operations, page views, and user actions. The SDK
auto-populates common fields about the application, user, device, platform, etc. (See
/developers/articles/common-properties/ (link tbd).)
Each SDK also
offers features optimized for the platform. For example, the Client
SDKs support smart transmission of events to reduce power and metered
network usage, as well as a census of device hardware.

## segment

A segment is a set of filters representing a subset of the data.  Examples:

- North American Region: `Country IN (US, CA, MX, ...)`
- All Regions:  <empty filter>
- WA counties excluding Seattle metro area: `County NOT IN (King, Snohomish, Pierce)`

One important difference between a **segment** and a **derived
property** is that segments can represent overlapping subsets of data.
This is because each segment is defined by its own set of filters.

## semantic context

Semantic context is the data or metadata associated with specified
Product Insights data, such as device fields, operating system fields, operating
system name, and so on.

## signal property

See [dimensions](#dimensions).

## split combination

Each distinct set of property values for a metric’s split properties
represents a combination.  For example, if a metric contains split
dimension `OS Platform and Country`, then two examples of combinations
would include `Android, US` and `iOS, UK`.

## split property

A split property is a **signal property** (column or **dimension**),
such as `OS Platform` or `Country`, used to **drill into** (split) a metric
further.  Split property values may be **static** or **dynamic**.

## splits

See [dimensions](#dimensions).

## static

A static property such as `OS Platform` or `Country` consists of a set
of values that are generally unchanging or change very slowly (though
their frequency of occurrence can change).

## tenant

See [project](#project).

## tenant ID

See [project ID](#project-id).

## throttling

Product Insights imposes quota on various aspects of data usage such as incoming
data volume. When usage breaches the imposed limits, throttling occurs
to avoid unexpectedly high costs to users as well as minimizing
disruption to other clients.

Please note that throttling is not triggered by temporary spikes.

## top N query

A top N (or bottom N) query is a query-time filter that first selects
the first N combinations that are aggregated and ordered over the
query time range, and then performs the query using those selected N
combinations.
