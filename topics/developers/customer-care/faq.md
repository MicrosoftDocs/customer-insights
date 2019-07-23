---
uid: developers/customer-care/faq
title: FAQ (Frequently Asked Questions)
author: hakrou
description: FAQ (Frequently Asked Questions)
ms.author: hakrou
ms.date: 05/23/2019
ms.service: product-insights
ms.topic: conceptual
---

# FAQ (Frequently Asked Questions)

## Onboarding 


## Concepts 

### What is a project?

A project is a customer unit within Product Insights and belongs to a team. A project sends data, owns its data, and uses its data. Once you create a project, you are the customer of Product Insights, and as that customer (project), you will be using Product Insights services. A project is usually a team, single service, application, or shared library.

### What is a signal?

### What are metrics?

### What are insights?



## Sending Signals 

### What is an SDK?

An SDK is a Software Development Kit. Several SDKs are [available for Product Insights](../dev-resources/index.md), including ones for Android, C#, iOS, and JavaScript. These SDKs will enable you to send data programmatically to Product Insights from their respective platforms.

### Why are some of my signals not showing up in the viewer?

The signals page was designed to provide a quick sample of your signals for you to debug instrumentation and get examples of signals. It was not intended to be a generic query engine. At low volumes, it will capture and return every event. At high volumes, it will capture and return a sample of your recent signals.

### Why can't I see my data?

If you are sending data to Product Insights with an SDK, make sure your application is correctly integrated with App Insights and App Center. You should be receiving a 200 OK confirmation from the Product Insights server when sending data. 

## Exploring Signals 


## Visualizing Signals 



## Security 

### What would happen if a malicious hacker snooped and got my tenant’s ingestion token?

If the hacker knew the Product Insights schema, how to serialize to bond, and also our collector protocol, they could send junk signals, thereby increasing event count. This could have an impact on distinct user count, or possibly cause a denial of service attack. We suggest that you replace the compromised token.

### What do I do if my tenant’s ingestion token is compromised?

You can remove the compromised token from your code, and replace it with a new token.
