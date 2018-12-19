---
layout: page
title: Creating cubes with data from Kusto
---

## Kusto cubes introduction

Kusto Cubes enable users to build an Aria Cube with a Kusto query based on data in Kusto. The cube can then be used to create charts and dashboards in Aria.

For more background and information, refer to the video below:

{% include video.html src="KustoCron.mp4" %}

## Transforming your query

This page shows you how to transform an existing Kusto query into one that is suitable for Kusto Cubes.

### Step 1: Take a current kusto query

You will use a Kusto query that works on the Aria Calling App Sample tenant. Assume you use this query below to determine the 95th percentile health score for events broken down by the dimension `HealthState_Name`.

{% img "how-to/kusto-cubes/1.png" alt:"Kusto Cubes 1" class:"img-responsive" %}

### Step 2: Parameterize the time dimension to timebox your query

The first thing to examine and remember is the time dimension - `EventInfo_Time`. It's critical that you timebox your query for Kusto. This allows the queries to work well. To that end, you need to parameterize the query as follows. Define two variables - `_starttime_` and `_endtime_` to timebox your query. This is demonstrated below and is the only change made to the query so far. It is very important to filter your events so that they are greater than or equal to `starttime` and less than `endtime`. All events that fall outside this time range will be rejected and will _not_ be sent through to Aria.

{% img "how-to/kusto-cubes/2.png" alt:"Kusto Cubes 2" class:"img-responsive" %}

### Step 3: Think about the summarize and aggregate operations you need to perform in your query

Now you need to transform the query to emit time as a dimension. The original query ran for a time window of two hours, as determined by current time. For Kusto Cubes, you need to remember that Kusto will run your query repeatedly at the frequency you choose and substitute the `_starttime_` and `_endtime_` variables as appropriate. What is also important is the requirement to _emit time as a dimension_  so you can feed the results back into Aria. You must emit the same time dimension that is used for your events. If you are using the Aria SDK, this will usually be `EventInfo_Time`.

In this example, you want to break down the results into five minute intervals. In Kusto Cubes, only five minute, one hour, and one day intervals are supported for bucketing results. Thus, what follows is what the query looks like in Kusto Explorer once you add the time based bucketing, including a new variable called `_bininterval_`, used to project the original results in five minute windows. The dataset you see in Kusto Explorer is the dataset that will be fed back into Aria for Visualization and so on as a new event.

{% img "how-to/kusto-cubes/3.png" alt:"Kusto Cubes 3" class:"img-responsive" %}

### Step 4: Import parts of the query into Aria

In the above example, you will perform the summarize operation as a part of the Aria Kusto Cube definition.

- In your project (previously named "tenant"), select **Application**, and then **Management**, and then **Kusto Cube Manager**.
- Thus, for the query above, with the filter clauses and the transformation highlighted above, the results are as follows. (Notice that the `starttime`, `endtime` and `bininterval` definitions have been dropped.)

{% img "how-to/kusto-cubes/4.png" alt:"Kusto Cubes 4" class:"img-responsive" %}

- Copy and paste the query into the **KUSTO QUERY** text box. If you click outside the text box, your query will run immediately. 

- Upon successful execution, the interface looks like this at the bottom of the screen:

{% img "how-to/kusto-cubes/5.png" alt:"Kusto Cubes 4" class:"img-responsive" %}

- Click **Next** to tweak options related to your Kusto Cube Configuration. Hover over the **?** icon next to each option to see more details about them.

- The "Your query returned X columns" message indicates that you ran the query against Kusto and obtained the column names. From these columns, you need to choose the metrics with which to summarize your results, the column that indicates the timestamp dimension, and finally the columns used to filter or split your data on various dimensions. The screenshot below illustrates the appropriate choices for your sample query. 

{% img "how-to/kusto-cubes/kc_measures_dim.png" alt:"Kusto Cube measures" class:"img-responsive" %}

- Once you have picked your dimensions and columns, here is the exact query you will run against Kusto in the **Review the query** section.

{% img "how-to/kusto-cubes/kc_final.png" alt:"Kusto Cube output" class:"img-responsive" %}

- Hit the **Preview** button to execute the query and see the results that will be available for Visualization. At this point, you can save this resource and start referencing it in a visualization editor.

### Note on joins across databases

In the query above, the `health_state` event belongs to the Aria Calling App Sample tenant. Hence you can directly reference that event. If you wanted to refer to say `EventA` in the database `dbSample`, you would use the following syntax to operate on events within that table.

{% highlight shell %}
database('dbSample').EventA | count
{% endhighlight %}
