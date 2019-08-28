---
uid: developers/tutorials/metrics-use-filters
title: Use filters
author: ruthaisabokhae
description: Use filters
ms.author: ruthai
ms.date: 05/09/2019
ms.service: product-insights
ms.topic: conceptual
---
# Use filters to refine your data 

Filters fine-tune the signals that power your metrics. 

This example uses the metric for the total number of drives completed that was used in the previous two sections ([Create metrics](metrics-create-metrics) and [Add splits](metrics-add-splits)).   

Select **Filter** and then **City**. You will see a new section that shows a filter. 

Click the pencil icon to edit filter options. You can filter the signals so that you only see data for San Francisco, or cities whose names start with "C". There are many other options available. 

Some use cases of filters are as follows: 
- Create a filter that only shows properties starting with "TEST" to only see test data. Use **Does not begin with** or filter out test data. 
- Only show signals from devices whose phone number starts with a specific area code
- Only show feedback from users where the content contains the word "error" 

There are use cases where you can use either a split or a filter. For example, you can see the total number of reported drives in San Francisco using either option. Filters limit the types of signal used for analysis.

> [!VIDEO https://ariamediahost.blob.core.windows.net/media/videos/ProductInsights/UseFilter.mp4] 

## Filter conditions 

Filter offers different conditions you can use on your data. **Is equal to** and **Is not equal to** are used to include or exclude specific strings. Therefore, using this condition you could only see data where city is exactly equal to "San Francisco". Using "Begins with", you could only see cities that start with the word "San", to include San Diego as well. 

The **Contains** condition allows you to filter regardless of where the target string may be. Only showing feedback from users where the content contains the word "error" is a good example. It won't matter where the word 'error' occurs in a possibly long body of text. 

**Has one of** allows you to specify multiple possibilities. You can specify that you want any data that contains one of the following cities: "San Francisco", "Chicago", and "New York".
