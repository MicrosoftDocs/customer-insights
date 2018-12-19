---
layout: page
title: Use R to work with Aria


---

## Get data

Currently there is no native AAD support for R ([platforms supported](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-libraries)).
It is suggested that you retrieve data using a supported language, store the JSON result, then load it into R. See below on how it can be done, including a
[sample project](#SampleProject) that demonstrates how to connect to the API to get data.
Alternatively, [you can use developer tools from your browser](#BrowserHack) to manually get JSON responses, which may be simpler for testing purposes.

## Processing the JSON response

When you make a request, you will get a JSON response. You can convert this into a Pandas dataframe to analyze the data further.
The code snippet below shows how to load JSON, extract data, create a time series sequence, and then plot the data.

{% highlight r %}
library(jsonlite)
library(ggplot2)
data <- fromJSON("data.json")

# Extract data points
values = data$series$values[[1]]

# Get time interval
time_interval = data$interval[[1]]

# Split the interval, and extract the starting point
start_interval = strsplit(time_interval, "/")[[1]][1]

# Parse starting time and set time zone
start_time <- strptime(start_interval, "%Y-%m-%dT%H:%M:%S", tz = "EST5EDT")

# Create a time series. Note that I know it is by the hour because data$granularity is PT1H
timecol = seq(start_time, by = "hour", length.out = length(values))

# Create a data frame
frame = data.frame(timecol, values)

# Plot time series
ggplot(f, aes(timecol, values)) + geom_line() + xlab("time") + ylab(data$executionInfo$metrics$id)
{% endhighlight %}

<a name="SampleProject">Sample project with AAD setup</a>

{% include contents/cube-api-get-data-snippet.md %}

<a name="BrowserHack">Use a standard REST client to get data from the API, without AAD setup</a>

{% include contents/cube-api-browser-hack-snippet.md %}


