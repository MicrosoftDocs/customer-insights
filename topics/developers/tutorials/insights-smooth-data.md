---
uid: developers/tutorials/insights-smooth-data
title: Smooth data
author: vroha
description: Smooth data
ms.author: v-roha
ms.date: 05/22/2019
ms.service: product-insights
ms.topic: conceptual
---
# Smooth data

Explanation

Exponential rolling average: give more weight to the latest data and react faster to recent changes; this is the preferred smoothing transform

Some signals are noisy. To reduce fluctuations and noise, you can use rolling averages to smooth out variability and outliers. It also makes trends much easier to spot. Choose automatic time grain to let the system find the optimal window size.

## Example

Step by step instructions

> [!VIDEO https://ariamediahost.blob.core.windows.net/media/videos/ProductInsights/insights-smoothing.mp4]
