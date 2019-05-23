---
uid: developers/articles/glossary
title: Glossary of terms
author: vroha
description: Glossary of terms
ms.author: hakrou
ms.date: 04/12/2019
ms.service: product-insights
ms.topic: conceptual
---
# Glossary of terms

## aggregated data

Product Insights performs calculations as defined by your cubes, then stores the
aggregated results. You can use such calculated aggregation values for
your visualisations.

## aggregated metric

A metric that accumulates over time, such as a count of items.

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

## signal properties

Data sent to Product Insights are essentially a collection of key-value
pairs. These are also referred to signal properties. If you sent
country code, action taken, and button pressed, these three are all
signal properties over which you can run aggregation operations, such
as total number of events from the UK, or number of certain actions
taken.

## filters

In your visualisation, you can choose to see your data
'filtered'. Number of users filtered by the specified OS type would be
an example.

## ingestion token

A token used by an app to pass data to Product Insights.

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

## PII

Personally Identifiable Information is any data that could potentially
identify a specific individual. If your data to Product Insights
contains any such data, you should use PII tagging to ensure data
privacy.  Find out how you can handle PII data.
Product Insights uses the
nomenclature of _EUII_ and _OII_.  

## project

A project is typically a team or a single user account that sends a
group of events and owns resources such as dashboards and cubes.

Formerly, **tenant**.

## project ID

A unique identifier for a [project](#project).
Automatically assigned by the Product Insights service upon project creation.
Your project ID is also your Kusto (raw event) database ID.
Formerly, **tenant ID**.

## raw data

Raw data refers to raw signals sent by users to Product Insights.

## SDK

"SDK" stands for "Software Development Kit".  Each SDK enables basic
logging and semantic instrumentation. The logging APIs generate an
event with the specified name and event fields. The semantic APIs
prescribe a standard set of fields for common types of events such as
metrics, operations, page views, and user actions. The SDK
auto-populates common fields about the application, user, device, platform, etc. 

## signal property

See [dimensions](#dimensions).

## split property

A split property is a **signal property** (column or **dimension**),
such as `OS Platform` or `Country`, used to **drill into** (split) a metric
further.  Split property values may be **static** or **dynamic**.

## splits

See [dimensions](#dimensions).

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


