---
uid: developers/faq/index
title: Product Insights FAQ
---

## When do I use Product Insights?

TK: narrow question down

## What are the service limits?

There is a default ingestion quota of 5,000 events per second and a Kusto database of 1 GiB.

## Why are my events not showing up in the viewer?

See TK (event viewer questions).

## Why are my metrics not working? 

## What is an SDK? 

## How do I send data programmatically? 

You can download an SDK to send data. Or check [here] for alternative ways of sending data. 

## What is a project?

A project is a customer unit within Product Insights. A project sends data, owns its data, and uses its data. Once you create a project, you are the customer of Product Insights, and as that customer (project), you will be using Product Insights services. A project is usually a team, single service, application, or shared library.

## Why do I need a project?

TK

## How do I create a project?

TK: TBD

## How do I send data for a specific project? 

## I can't see my data! 

(Notes: SDK specific data - make sure integration with App Insights and App Center works) 

## How do I see raw events? 

## Why is there a quota on my project? 

Product Insights customers receive 1 million events per month at no additional charge.
After that, events are billed on a linear scale.

## What happens when my project is throttled?

Once the project has exceeded its quota beyond some grace period, the Product Insights Collector will start rejecting events from its clients. Transient spikes in traffic are unlikely to trigger throttling. The SDK on the client will retry the upload until it reaches the maximum queue size or it exceeds the max retry count.

## Which URLs do I need to list for the Aria Collectors?

TK: TBD (table)

## What would happen if a malicious hacker snooped and got my tenant’s ingestion token?

If the hacker knew the Product Insights schema, how to serialize to bond, and also our collector protocol, they could send junk events, thereby increasing event count. This could have an impact on distinct user count, or possibly cause a denial of service attack. We suggest that you replace the compromised token.

## What do I do if my tenant’s ingestion token is compromised?

You can remove the compromised token from your code, and replace it with a new token.

