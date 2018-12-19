---
layout: page
title: Using Azure ML Studio with Aria

---

Azure Machine Learning Studio is a GUI-based integrated development environment for constructing and productionizing Machine Learning workflow on Azure. It is available from https://studio.azureml.net/

You can build machine learning models, and use the models to make predictions.

To integrate with Aria,
use Aria to collect data, create metrics, and pull the aggregated data with the Cube API.
Check the video below to see how it's done:

{% include video.html src="AzureML.mp4" %}

Once you export the data, you can import it into Azure ML Studio to create ML models.
There are a couple of ways to create this data inflow:
- Download data as a JSON or CSV file, then import into Azure ML (suitable for R)
- Create a data app that exports data to a designated location, then import it from Azure ML using an import tool
- Execute a Python script that dynamically fetches data from the API, and train a model on fresh data.

## Downloading data as a JSON or CSV file

This method is suggested for initial testing. [You can use developer tools from your browser](#BrowserHack) to manually get a JSON response, which may be simpler for testing purposes.

### For R users

You need authentication to pull data from the Cube API. Unfortunately there is no native AAD support for R ([supported platforms](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-libraries]).

It's suggested that you retrieve data using a supported language, store the JSON result, then load it into R.

## Create a data app that regularly exports data

Create an app in C# or Python based on this [sample project](#SampleProject) that shows you how to connect to the API to get data.

Have the apps export data to Azure-friendly locations.

Set up ML Studio to import data from the locations.

## Execute a Python script that dynamically fetches data

The [Use Python documentation](./use-python) shows you how to connect to the API to get data in Python.

When you make a request, you will get a JSON response. You can convert this into a Pandas dataframe to analyze the data further.

<a name="SampleProject">Sample project with AAD setup</a>

{% include contents/cube-api-get-data-snippet.md %}

<a name="BrowserHack">Use a standard REST client to get data from the API, without AAD setup</a>

{% include contents/cube-api-browser-hack-snippet.md %}
