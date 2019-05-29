---
uid: developers/downloads/python
title: Get Started with Python
author: vroha
description: Get Started with Python
ms.author: hakrou
ms.date: 04/12/2019
ms.service: product-insights
ms.topic: conceptual
---
# Getting started with Python
 
## Prerequisites
* Python 2.7 or 3.x
* [API token](api-token.md)

## Installing the SDK
There are two primary ways to use the Python SDK:
* Install the SDK to your Python interpreter's `site-packages` folder, or
* Place the [SDK `.egg` file](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSenders/product_insights-2.0.0.egg) 
somewhere and add it to `sys.path`
 
This page describes how to do both.

#### Installing to site-packages
1. Open your terminal and `cd` to the directory containing the file `aria-x.y.z.egg`.
2. Run `python -m easy_install aria-x.y.z.egg`
3. Import the SDK
```python
import aria
from aria import LogManager, EventProperties
```

#### Adding to the Import Path
The SDK can also be used without installation using only the `.egg` file.
In any Python script, add the following code recipe to use the SDK:
```python
import sys
sys.path.append('/path/to/aria-x.y.z.egg')
 
# Import the SDK!
import aria
from aria import LogManager, EventProperties
```
 
## Using the SDK
While a full example can be seen in the SDK's [sample.py file](sample.py), the basic usage pattern is demonstrated here.
 
```python
from aria import LogManager, EventProperties, PiiKind
 
# Initialize the SDK and get a logger
# Use your actual tenant token - it will be longer than this example
logger = LogManager.initialize('0123456789abcdef-01234567-89abcdef')
 
# Create an event
event = EventProperties('some_event_name')
 
# Fill the event values
event.set_property('rpm', 50)
event.set_property('device_name', 'Test Device 9000')
event.set_property('active', True)
 
# Maybe even set a PII (Personally Identifiable Information) value
# This value will be obfuscated on upload, and will be unreadable
event.set_property('username', 'SuperCoolUsername_42', pii_kind=PiiKind.PiiKind_DistinguishedName)
 
# Log the event
logger.log_event(event)
```
 
Keep in mind that the SDK batches events and uploads them periodically rather than immediately (by default, a little over three times per second) when calling `log_event()`.
 
To force all events to be uploaded, call
```python
LogManager.flush()
```
 
Before your program exits, call
```python
LogManager.flush_and_tear_down()
```
 
This convenience method flushes the SDK and ensures it shuts down cleanly. 
 
