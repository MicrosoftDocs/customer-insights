---
layout: page
title: Cube filtering

---

## Why should I use cube filtering? 

Cubes with high cardinality [can cause problems](/developers/how-to/cardinality-tuning). Your cube might slow down, and even stop processing data. 
To avoid this problem, you can fine-tune your cube for maximum performance. Cube filtering is a powerful way of managing your cubes. 

Filters enable you to choose which events contribute to a specific cube. In the past, you could only choose by event name.
Now you can choose by examining the event properties. Examples:
- Only let in events with a property version above 1.5
- Only let in events with an extraordinarily large latency 
- Let in events with a platform of either Linux or macOS
- Conditions can be ANDed and ORed and use the Aria.ms derived properties, like measures and dimensions

How can you define filters? See detailed information on all filter operations [here](/developers/deep-dives/property-filters/). 

{% include video.html src="CardinalityFilteringCapping.mp4" %}

## What are the advantages? 

With cube filtering, you can free up cardinality for the data you really care about, and better organize your data into multiple cubes.
	 
## Any caveats? 

Filters are local to the cube and do not affect the event itself, so other cubes, Kusto, Siphon, and so on are not affected.

