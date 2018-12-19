---
layout: page
title: Use Python to work with Aria


---

This document discusses accessing Aria's Cube API to pull data from Aria's Real-Time Aggregation (RTA) service.

## Related topics

* [Sending data with Python](https://aria.microsoft.com/developer/start-now/using-the-aria-sdk/get-started/python).
* [Connecting to Kusto with Python](/developers/how-to/kusto-python/)

## 1. Get data

You can get data from Aria's Real-Time Aggregation (RTA) service using its API. In this document, we will concentrate on using Python to get data out. You can also access a [sample C# project and information for other platforms](#SampleProject).
Alternatively, [you can use developer tools from your browser](#BrowserHack) to manually get a JSON response, which may be simpler for testing purposes.

From here on, we will be discussing how to work with the API only with Python.
This tutorial consists of two parts. First, we will discuss the shorter method of simply processing the JSON data you have from the API. This assumes that you either used a [browser hack](#BrowserHack) or you retrieved the data already. In the second part, we will examine a [complete Python working example](#PythonExample), including AAD authentication that you will require to get data.

## 2. Processing Aria's data in JSON format

When you make a request, you will get a JSON response. You can convert this into a Pandas dataframe to analyze the data further. (If you don't know how to get data, see above.) The code snippet below shows how to load JSON, extract data, create a time series sequence, and then plot the data.

{% include contents/cube-api-python-json-data-converter.md %}

## 3. Complete working example in Python, including AAD

### <a name="PythonExample">&nbsp;</a>

{% include contents/cube-api-complete-python-example-with-AAD.md %}

## 4. Sample project in C# and other languages

### <a name="SampleProject">Sample project with AAD setup</a>

{% include contents/cube-api-get-data-snippet.md %}

## 5. Browser hack to get data from the API easily

<a name="BrowserHack">Use a standard REST client to get data from the API, without AAD setup</a>

{% include contents/cube-api-browser-hack-snippet.md %}
