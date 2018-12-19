---
layout: page
title: Cube APIs


---

You can use Aria's Cube API to extract data directly from the cubes.

[This sample project](#SampleProject) shows you how to connect to the API to get data.

[This Python sample](#PythonExample) is complete with AAD authentication to retrieve data from the API, manipulate the data and then plot the results.

Alternatively, [you can use developer tools from your browser](#BrowserHack) to manually get json response which may be simpler for testing purposes.

## 1. Sample project in C#, and other languages

### <a name="SampleProject">Sample project with AAD setup</a>

{% include contents/cube-api-get-data-snippet.md %}

## 2. Complete working example in Python, including AAD

### <a name="PythonExample">Complete Python example</a>

{% include contents/cube-api-complete-python-example-with-AAD.md %}

## 3. Browser hack to get data from the API easily

<a name="BrowserHack">Use a standard REST client to get data from the API, without AAD setup</a>

### {% include contents/cube-api-browser-hack-snippet.md %}
