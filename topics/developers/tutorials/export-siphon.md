---
layout: page
title: Export data to Siphon
internal: true
---

## Siphon Introduction

Siphon is a real-time, highly available and reliable distributed message queue system that offers a pub-sub interface. The Siphon service functions as a Data Bus for ingesting and consuming near real-time data streams for processing and analytics. [Learn more about Siphon][1].

## 1. Create a new resource
1.	Select the Aria tenant.
2.	On the **Settings** page, create a new resource.
3.	Choose the resource type **Data Export (Siphon)**.

{% img "how-to/exports/SiphonAdd1.png" alt:"Add Siphon export" class:"img-responsive" %}

{% img "how-to/exports/SiphonAdd2.png" alt:"Add Siphon export" class:"img-responsive" %}

## 2. Select source events
1.	Select your event types.
2.	Either select event types manually or choose the option **All event types**.
3.	When you select **All event types**, any new event types added to the tenant will be sent to Siphon automatically.

{% img "how-to/exports/SiphonConfig.png" alt:"configure Siphon export" class:"img-responsive" %}

## 3. Destination
1.	Siphon tenant:
Select a Siphon tenant. The list shows all tenants to which you have permissions.
If you know your Siphon tenant and don't see it, [contact][2] the Siphon team. Otherwise, you can use the Siphon public tenant.

2.	Siphon topic:
You can choose an existing topic or create a new one.
This will show the list of all Siphon topics for that tenant.
There will be some topics that are in pending stage that require tenant admin approval.

## 4. Creating a new Siphon topic
1.	Topic name:
Provide a mnemonic and descriptive name for the topic, from
4-255 alphanumeric and symbol characters, including hyphens and underscores.

2.	Quota:
The quota helps Siphon tenant admins estimate the space they show allocate for you.
This value is optional. We will use the tenant default if you don’t know a value.
If you send more data than the allocated quota, you will be throttled.
When you request a new topic, you will be auto-approved if the request is below the tenant’s maximum approval limit. Otherwise, the request will go to a Siphon tenant admin to approve.
You can contact the tenant admin to get the request approved.

## Consuming Aria events in Siphon

Once you have your data in Siphon, you can consume it using [Siphon Connectors][3], or you can use the [Siphon pull SDK][4] to consume the data.

## Help

General questions: [Siphon team][5]

Urgent issues: [Siphon DRI][6]

[1]: http://siphondocs
[2]: mailto:siphon@microsoft.com?subject=Help%20with%20Aria-%3eSiphon%20export
[3]: http://siphondocs/en-us/documentation/Connectors/Available-Connectors
[4]: http://siphondocs/en-us/documentation/Onboarding/Consuming-Data/Consume-with-Siphon-SDK
[5]: mailto:siphon@microsoft.com?subject=Aria-%3eSiphon%20questions
[6]: mailto:siphondri@microsoft.com?subject=Aria-%3eSiphon%20issue
