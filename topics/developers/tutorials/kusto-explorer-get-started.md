---
layout: page
title: Getting started with Kusto Explorer
---

## Overview

Kusto Explorer enables searching and queries over your raw Aria event data. Below is a short video on Kusto Explorer.

{% include video.html src="KustoExplorer.mp4" %}

### Demo

Let's query the Aria Calling App Sample data to get a summary of the device and OS types for sessions in the last 24 hours.

[Open]({{ site.portal_url }}/kusto-explorer?projectId=dac04b4cb8ae466d8dcf842682c3a264&tabIndex=0){:target="_blank"} the Kusto Explorer within the context of the Aria Mobile Analytics Demo. Once it is open, you can paste in the following query, which processes the data and displays the results in a grid.

{% highlight shell %}
session
    | where EventInfo_Time > ago(24h)
    | summarize count() by DeviceInfo_Make, DeviceInfo_Model, DeviceInfo_OsName, DeviceInfo_OsVersion
{% endhighlight %}

Your browser should display something similar to the following.

{% img "how-to/kusto-explorer/demo.png" alt:"Kusto Explorer demo" class:"img-responsive" %}

Once you are done with your query, you can save it, link to it, and perform all the common actions on that you can with other Aria documents.

[Learn more about the Kusto language syntax](https://kusto.azurewebsites.net/docs/queryLanguage/query_language.html){:target="_blank"}.

## Features
- Users can access the Aria/Kusto Explorer as a standalone app.
- Within the app, users can browse their Kusto source tables and events.
- Users can write and execute their queries against events ingested via Aria.
- Users can view query results in a tabular format (with chart support coming soon).
- Users can save and load query files as they do with other Aria documents.
- Users can leverage integrated Kusto language support (that is, Intellisense) when authoring queries.
- Users have autocomplete support available thanks to the integration with the [Monaco editor](https://microsoft.github.io/monaco-editor/index.html){:target="_blank"}.

## How to

### To start a new query

1. Click the query selector to display a list of saved queries.
2. Click the **New query** option at the top of the list.

### To add an element from the side panel

1. Hover over the schema's elements to display the **Insert** button.
2. Click the icon to insert the item into the Kusto editor.

### To save

The **Save** button has a red background when there are unsaved changes. To save, just click the **Save** icon. The first time you save, a dialog will request a name and description for your document.

### To create a clone (duplicate)

Click the duplicate icon to the right of the **Save** button. This feature is similar to the **Save as** option.
