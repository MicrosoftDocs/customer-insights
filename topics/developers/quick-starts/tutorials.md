---
layout: page
title: Aria tutorials
sub_title:

---

## Step by step tutorials

- [Introduction to Aria](../intro-video){: target="_blank" }
- [Starter guide](../written-tutorial){: target="_blank" }
- [More things you can do with Aria](../aria-advanced-tutorial){: target="_blank" }

## Video tutorials

This topic contains the following video tutorials:

- [What is a cube?](#what-is-a-cube?)
- [How to make a good cube](#how-to-make-a-good-cube)
- [Using filters and splits](#using-filters-and-splits)
- [What are segments?](#what-are-segments)
- [You can create a cube with data from a cube!](#you-can-create-a-cube-with-data-from-a-cube)
- [How to calculate percentiles](#how-to-calculate-percentiles)
{% if site.internal %}
- [What is Kusto?](#what-is-kusto)
- [Kusto Cron is your friend](#kusto-cron-is-your-friend)
{% endif %}
- [How to monitor your KPIs](#how-to-monitor-your-kpis)

### What is a cube?

You need to create a cube to aggregate your streaming telemetry data. Watch this video to learn what a cube is, and how to create one. For more information about cubes, see [Real-time cubes](/developers/deep-dives/real-time-cubes/){: target="_blank" }.

{% include video.html src="CubeIntro.mp4" %}

---

{% include video.html src="RTABasics.mp4" %}

### How to make a good cube

You will most likely use cube data to power your dashboards. However, if your cube is poorly designed, then your dashboard might not be as fast as it could be. Watch this video to learn how to build a well-performing cube.

{% include video.html src="CubeDesignTips.mp4" %}

### Using filters and splits

Filters and splits allow you to slice and dice your data. Find out what they are, and how they are different from one another.

{% include video.html src="Filters.mp4" %}

### What are segments?

You found filters and splits that display your data beautifully. If you want to save your configuration, but you don't want to go selecting and deselecting again, then you should create a segment.

{% include video.html src="Segments.mp4" %}

### You can create a cube with data from a cube!

You already have a cube, but then you realize that you could create a new KPI based on the cube data. Well, it's time for composite cubes. Watch this video to find out how to create and use them.

{% include video.html src="CompositeCubes.mp4" %}

### How to calculate percentiles

Averages, minimums, and maximums are great, but sometimes you just need to get percentiles. E.g., find otu what is the worst one percent performer, or what is the best one percent performer. Watch this video to learn out how to calculate percentiles.

{% include video.html src="Percentiles.mp4" %}

{% if site.internal %}
### What is Kusto?

Do you want an ad-hoc, interactive query environment? If the answer is yes, then Kusto is for you.

{% include video.html src="Kusto1.mp4" %}

---

{% include video.html src="Kusto2.mp4" %}

### Kusto Cron is your friend

Kusto is awesome, but if you want to get the output onto your dashboard, then you can do it with KustoCron.

{% include video.html src="KustoCron.mp4" %}
{% endif %}

### How to monitor your KPIs

With health monitoring, you can monitor your KPIs and then have alerts raised automatically when something doesn't look right. Watch this video to learn how.

{% include video.html src="HealthMonitoring.mp4" %}
