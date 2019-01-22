---
uid: developers/tutorials/use-expressions
title: Use Expressions
---

## Computed datasets using expressions

Product Insights supports creating computed datasets on the results of cube queries, using an expression 
language. You can watch a tutorial video (<8 min) describing the process below.

{% include video.html src="UsingExpressions_short.mp4" %}

A slightly longer tutorial that walks through the whole process follows, including comparisons to transforms.

{% include video.html src="UsingExpressions.mp4" %}

First you must create data layers. After you have at least one layer with one data series, you can create expressions which reference them by adding an Expression query layer.

{% img "how-to/compute-expressions/compute1.png" alt:"Chart types" class:"img-responsive" %}

Next, you can define your expression as shown below:

{% img "how-to/compute-expressions/compute2.png" alt:"Chart types" class:"img-responsive" %}

### In the authoring experience

1. You can refer to the **Layer** label to identify datasets, for example, A and B for Layer(A) and Layer(B). These datasets can be used as variables in the custom expression. The prefix is case-sensitive.
1. Standard arithmetic and precedence operators apply. You can use brackets for precedence and grouping.
1. Invalid expressions will result in error messages from the server.

Visualizations containing dataset expressions can then be saved and viewed in dashboards just like any other chart.

### Examples

1.  The percentage of a specified value. In this scenario, there are two datasets, A (filtered on a dimension that identifies passes) and B (filtered on a dimension that identifies failures).
    ```shell
    100 * A / (A + B)
    ```
1.  The ratio between two datasets.
    ```shell
    A / B
    ```
1.  Scaling with a constant multiple.
    ```shell
    A / 60
    ```
1.  Rating computation using the `SecondsPerGrain` parameter. This is a special variable equal to the number of seconds in a time window. It can convert numbers to rates. Example:
    ```shell
    A / SecondsPerGrain
    ```
1.  Bucketing decision trees.
    ```shell
    A > 75 ? 1 : A > 50 ? 0.5 : 0
    ```

### Technical considerations

* The arithmetic operations are operations on .NET `double` objects.
* The expression is evaluated once per time instance per series.
* Divide by zero operations result in `Double.NaN`, which appears as a missing data point.

### Limitations

* **There can be only one multi-series source dataset**: Only one source dataset may produce multiple series (lines on a chart). This dataset can use features like splits, segments, and multi-operation queries to produce multiple series.
* **The other datasets must produce a single series each**: Each expression produces a single series for every series in the multi-series dataset.
* **Multi-measure dataset queries are not allowed**: Each dataset may only reference a single measure in a cube. You may create multiple datasets, each referencing different measures in the same cube.
* **Mandatory reference**: If there is a multi-series dataset, it must be referenced by the expression.
* **Service limits**:
    * Expressions may reference at most three datasets, total.
	* There may be at most three expression datasets.
