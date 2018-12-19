---
layout: page
title: Explore Raw Events


---

# How do I access my raw events?

You can access your raw events using ARIA's deep integration with kusto, provided the source event is enabled in your kusto database (by default all events are, unless explicitly disabled by you) and it has enough retention, by simply heading to [kusto web explorer]({{ site.portal_url }}/kusto-explorer) and author a releveant query for your ad-hoc analyses.

# How do I easily access raw events that are contributing to a given chart?

If you are, though, looking at a chart powered by an RTA cube we offer an easy way to access the exact events that are contributing to the series you are seeing. Just click on "Explore Raw Events" available at the top of any chart and you will be brought to our own kusto web explorer with a query prepopulated for you that will exactly match the raw events that build up yout chart.

# What can I do with it?

You know your data best than anyone, that's why we left the query generated quite generic and easy to extend, but we left some pointers for you to explore.
By default the query we generate will show you juat 100 raw events matched so you can quickly remember the schema of the event(s) itself.

## Explore your raw events in full

You are not limited by just the dimensions you chose at cube creation time, here you will have access to the all properties your event is bringing in (provided you haven't explictly disabled them in kusto manager in order to save space). Maybe you had a high cardinality property (say a guid) that can't be used as a dimension, but here you will be able to explore that data and aggregate/split by it as need be.

Kusto offers a few ML tools to find insights (e.g. clusters) automatically for you, we left an easy way for you to use, as an example, [autocluster](https://kusto.azurewebsites.net/docs/queryLanguage/query_language_autoclusterplugin.html?q=autocluster) but there are you can explore such [reduce](https://kusto.azurewebsites.net/docs/queryLanguage/query_language_reduceoperator.html?q=reduce), consider reading more [here](https://kusto.azurewebsites.net/docs/queryLanguage/query_language_machine_learning_and_tsa.html?q=machine learning).

## Compare data with RTA cube

You will find commented out a summarize clause that, if you wished so, you can re-enable and you will be able to see a tabular view of the exact chart you were seeing in RTA. They should always match, if they don't it will likely be a case of your data being throttled inobund to kusto (and you might want to consider [upgrading to an higher SKU](/developers/how-to/kusto-SKUs/) or tackle your [ingestion rate]({{ site.portal_url }}/ingestion) if you want to have a better data quality in kusto).

# Upcoming features

* **Single time series drill down** we will soon allow you to find the raw events contributing to a single time series.

# Current limitations

* **Transforms** are currently ignored
* **Segments** are currently not supported
* **System cubes (such as Event Counts)** are currently not supported
* **Non migratable cubes** wont be supported for this feature
