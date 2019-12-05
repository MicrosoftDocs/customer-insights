---
uid:  signal-schema
title: Signal Schema for Product Insights
author: ruthaisabokhae
description: Signal Schema for Product Insights
ms.author: ruthai
ms.date: 11/15/2019
ms.service: product-insights
ms.topic: conceptual
---

# Signal Schema for Product Insights

The following schema is adopted for use by Product Insights signals.

## Signal schema
This contains the minimal set of attributes for Product Insights data, which is also the base class for all signals.

| Property Name        | Description           |
| ------------- |:-------------:|
| timestamp     | This field is required. Value stored as UTC. |
| timeZone      | Contextual timezone as captured from signal during ingestion. Specified by the collector looking at the time zone value of the timestamp field, or via the "device" time zone. No override if specified directly in signal.     |
| name | Name of the signal. This field is required.      |
| version | Version of the signal as defined by the emitter.      |

## Server schema

| Property Name        | Description           |
| ------------- |:-------------:|
| timestamp     | DateTime that the signal was ingested into Product Insights, autopopulated. |
| project | Project ID as defined in Product Insights. This allows for signal routing to the appropriate project.      |

### Notes
* The fields specified above are minimal requirements by any signal.
* All properties will have an object prefix separated by a period. For example, `Signal.timestamp`.
* Custom attributes are optional.

## Product extension
The **Product** extension refers to the *class* of products, such as a specific model. For instance, in the case of vehicles, it can be a specific model, like Star Car Model X.

| Property Name        | Description           |
| ------------- |:-------------:|
| productId     | This field is generally populated by the enrichment service. When available in signal this field enables enrichment service joins. Value is a GUID. |
| partNumber | This field is shown as the value in trasactions like opportunities, orders, cases, etc. This field is generally populated by enrichment service. When available in signal, this field enables enrichment service joins. It is important to note that CDS does not enforce uniqueness on this field, although they typically tend to be unique.     |
| modelNumber     | Manufacturer model number. This field coupled with **manufacturer** can help locate the right product record, although there's no unique index. |

## Asset Extension
The **Asset** extension refers to a single instance of a particular product. For example, in the case of vehicles, it can be an actual specific vehicle with a VIN number, which is equivalent to a serial number.

| Property Name        | Description           |
| ------------- |:-------------:|
| deviceID     | Unique device ID as referred to within IoT and CDS platforms. |
| serialNumber | A unique end-user friendly reference ID generally found within most devices. For a car, it would be a VIN. This field is generally populated by enrichment service. When available in signal, this field enables enrichment service joins.     |
| assetId     | This field is generally populated by enrichment service. When available in signal, this field enables enrichment service joins. |
