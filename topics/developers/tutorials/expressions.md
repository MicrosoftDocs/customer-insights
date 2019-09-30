---
uid: developers/tutorials/expressions
title: Analyze using expressions
author: ruthaisabokhae
description: Analyze using expressions
ms.author: ruthai
ms.date: 09/27/2019
ms.service: product-insights
ms.topic: conceptual
---

# Analyze data using expressions<br>

Expressions enables you perform arithmetic operations on your data. First you must create data layers. After you have at least one layer with one data series, you can create expressions which reference them by adding an **Expression query** layer. Next, you can define your expression as shown in the video below. Visualizations containing dataset expressions can then be saved and viewed in dashboards just like any other chart.

[INSERT VIDEO]

### It is important to note while authoring expressions that:

1. You can refer to the **Layer** label to identify datasets, for example, A and B for Layer(A) and Layer(B). These datasets can be used as variables in the custom expression. The prefix is case-sensitive.
1. Standard arithmetic and precedence operators apply. You can use brackets for precedence and grouping.
1. Invalid expressions will result in error messages from the server.
