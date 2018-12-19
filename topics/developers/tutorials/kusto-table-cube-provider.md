---
layout: page
title: Instant charts from raw data (Kusto Table Cube Provider)

---

This feature enables you to create charts from raw events that are streaming in. It uses Kusto for data input, and the Aria portal for visualization.

Aria's workhorse RTA processes incoming data and stores the results. Visualisations powered by RTA run on the smaller pre-processed data sets, which allow for highly responsive charts.

Kusto complements RTA by enabling you to access and query raw streaming data, not the processed data. Until now, there was not an easy and fast way of visualizing raw data from the Aria portal. 

Enter the Kusto Table Cube Provider. It enables you to create a "view" on the raw data. While cubes for RTA are instructions to RTA to process and aggregate data, Kusto Table Cube is a view that processes data on the fly, and enables you to create charts and dashboards with the same operations that RTA cubes use, but without the time delay. 

## Why is this useful? 

If you know exactly which KPIs you want, RTA is the perfect tool for you. However, if you are still exploring your data, and want to try out various aggregation methods to fine-tune your KPIs, the RTA feedback loop can be cumbersome, since changing your data processing definition will only affect future data. The Kusto Table Cube Provider enables you to explore your data freely and see results instantaneously. 

## What's the catch? 

After data exploration, you probably want a productionized data processing system that continuously and reliably extracts key insights from the data. You would want to build up a history that you can easily look up and compare to current data. For this purpose, RTA offers outstanding performance and stability for extremely low cost. Retention period in Kusto can differ by orders of magnitude, especially if your data volume is high. RTA also offers more ways to manipulate data with property functions. 

Note that charts having data sourced from this provider are not auto-refreshed. Additionally, the amount of data we can use to in the cube is limited by the amount of data present in the Kusto Table. Compared to RTA cubes, the performance of these cubes can be slow, especially for large data sets, since we need to query Kusto at run time. For longer term retention of cube results, faster performance, and getting alerts from your charts, Aria has provided a very simple process to convert your Kusto Table data source into an RTA cube. Once a user takes this action, Aria switches from having that chart powered by a Kusto Table Cube data source to an RTA data source. RTA cubes can only provide results after they have been created and new events are sent to the project.
