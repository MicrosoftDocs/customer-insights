---
layout: page
title: Service limits and quotas
sub_title: Last updated 20 July 2017

---

Having service limits and adjustable quotas are necessary for us to deliver strong isolation between tenants, so one user cannot impact other users if he or she makes a mistake in their usage of Aria or if their event volume increases by 100x. Aria is an extremely scalable service and we have some customers sending over 100,000 events per second today.

In addition to protecting customers by limiting huge unplanned spikes in traffic; pre-defined quotas enable us to avoid running highly over-scaled.  {% if site.internal %} This allows us to keep our COGS lower for Microsoft. 

For a large percentage of our customers the default production quotas provide enough capacity.  However, we can rapidly provision additional capacity as needed based on additional quota requests.

## How to request a quota increase

**To request a quota increase for a production tenant please email [Aria Support][support] providing your team name, tenant ID and details on expected data volume.  We currently support raising quota for ingestion, Cosmos export and Kusto.**

## Service Specific Limits and Quotas

Sandbox and pre-production tenants are designed for low volume testing. **We only adjust quotas for production tenants.**

{% endif %}

We summarize the common service limits and default quotas in the tables below.

### Event ingestion

Resource                      | Resource limit or quota
------------------------------|---------------------------------------------------
Bytes per event               | 2.5 MB (uncompressed)
Event volume per tenant       | 500 events/s for sandbox tenants<br/>1,000 events/s for pre-production tenants<br/>1,000 events/s for GoLocal production tenants\*\*<br/>5,000 events/s for production tenants (adjustable quota)
Event types per tenant        | 100 per tenant in a rolling 24-hour period
Raw data retention            | 90 days
{: .table .table-striped}

{% if site.internal %}
<small>\*\* GoLocal quotas are disabled by default. Please read the [GoLocal Support Page](/developer/deep-dives/go-local-regions).</small>
{% endif %}

Event ingestion is the first point in our service where quotas are applied.  **If you exceed your quota you will receive an email alert indicating that you were throttled.  To ensure the correct distribution list for this mail please ensure you have defined a notification DL in your tenant properties.**

To view the current volume of data you are ingesting, use the Default dashboard created for your tenant.  There is an event count RTA cube created for all tenants and this cube has a measure for event count.

### Real-time cubes

Resource                      | Resource limit or quota
------------------------------|---------------------------------------------------
Dimensional cardinality<br>(distinct dimension<br>value combinations,<br>5 minute base grain cubes)\*\* | 100,000 per day for Arithmetic operations<br>10,000 per day for Fast Distinct Count operations<br>1,000 per day for Percentiles operations<br>250 per day for Accurate Distinct Count operations
Dimensional cardinality<br>(distinct dimension<br>value combinations,<br>1 minute base grain cubes)\*\* | 10,000 per day for Arithmetic operations<br>1,000 per day for Fast Distinct Count operations<br>200 per day for Percentiles operations<br>50 per day for Accurate Distinct Count operations
Allowed event time window     | -7 days and +1 day of the current time
Event filters per cube        | 10
Measures per cube             | 10
Dimensions per cube           | 10
Data retention                | 18 months
{: .table .table-striped}

<small>\*\*The exact limits are dependent on a number of factors, but are typically around the stated dimension value combinations per day. Data with significant time skew can also result in higher processing times. Customers will receive alerts if their cubes approach the limits. Cubes will be disabled if they are over the limits, and above a certain grace period.</small>

{% if site.internal %}
### Data export to Cosmos

Resource                      | Resource limit or quota
------------------------------|---------------------------------------------------
Data volume                   | 1 TB per day (adjustable quota)
{: .table .table-striped}
{% endif %}

### Resources

Resource                      | Resource limit or quota
------------------------------|---------------------------------------------------
Resources per tenant          | 50 per resource type
Tokens per tenant             | 100
AD objects per tenant role    | 50 per role type (e.g., owner)
Tenants per AD user           | 100
{: .table .table-striped}

### Dashboards

Resource                      | Resource limit or quota
------------------------------|---------------------------------------------------
Charts per tab                | 50
Tabs per dashboard            | 50
Dashboards per tenant         | 100
{: .table .table-striped}

{% if site.internal %}
### Kusto Storage

Kusto storage ranges from of 1 GB of compressed data (free of cost) to customized settings of hundreds of Terabytes. Read more in our [Kusto SKU page][1].

### Kusto Queries*

Resource                                       | Resource limit or quota
-----------------------------------------------|---------------------------------------------------
Queries/sec per tenant                         | 3
Queries/hour per tenant                        | 500
Query results/hour per tenant                  | 2 GB
Time spent running queries per hour per tenant | 15 minutes
{: .table .table-striped}

(**\***) These quotas are per tenant in case an Aria read token is used, or per AD user in case federated authentication is used.
{% endif %}

[support]: mailto:ariasupport@service.microsoft.com
[1]: /developers/how-to/kusto-SKUs
