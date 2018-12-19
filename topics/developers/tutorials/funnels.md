---
layout: page
title: Funnels introduction
redirect_from: /developers/articles/funnels/
---

The Real-Time Funnels enable product owners to measure the progress of users through important workflows in their application.  Over __15 Office teams__ including Office Word, Excel, PPT, OneNote, Outlook, and Skype are already using RT Funnels, and have created over 300 Funnels.

## Don't know why you need funnels, or what they do? Check the video below.

What are funnels?
{% include video.html src="Funnels.mp4" %}

When do you use funnels?

{% include video.html src="Funnels2.mp4" %}

More videos are available on the [tutorial page](../funnels-tutorial).

## Sample dashboard with funnels

Refer to [this dashboard]({{ site.portal_url }}/dashboard/ZGFzaGJvYXJk4a4c82fe65f749a8beb8c36ad8b93ebf/tab/dGFif393f5807c8f422c8fe079921e2d29f7?projectId=bac7b6a05f514c49a71e4f4f84364572) to see how funnels are visualized.

## How to create your First Funnel?

To use the Real-Time Funnel feature, your product’s telemetry needs to be flowing into Aria, either via a routing layer like Nexus (used by many Office client teams such as Word, Excel and PPT), or using the Aria SDKs (used by teams like OneNote and Outlook Mobile).

- __Learn:__ Please Visit [Funnels Tutorial][1] which Includes 2-minute tutorial videos, to learn about how to create a Real-Time Funnel.
- __Create:__ If you know your way around, you can create funnels from the Applications menu - Funnel manager.


#### Some good examples of funnels:

1.	__Outlook Mobile Sign Up Funnel:__
5-step funnel that measures the success rate of the sign-up process in Outlook mobile apps.

2.	__Skype Phone Number Verification Funnel:__
6-step Funnel that measures the success rate from when a customer submits a phone number, gets the PIN, and submits it successfully in the app to confirm their phone number.

3.	__Office.com Promotion Success Funnel:__
3-step Funnel that measures the rate of customers who react to certain promotions on the office.com website.

{% img "how-to/funnels/funnel1.png" alt:"Funnels" class:"img-responsive" %}

#### OneNote to EverNote Wizard Example:

The Evernote to OneNote Import Wizard Funnel is a great example of this. This feature enables Evernote users to migrate to OneNote using a simple 4 step wizard experience. The steps of this funnel are Welcome Page, Sign in page, Import Progress Page, Success Page. The screen shots below depict the user experience, and the corresponding funnel chart generated in Aria to monitor the funnel.

#### The Import Wizard Screenshots below:

Shows the UI and how funnel conversion rates, are associated with them

{% img "how-to/funnels/funnel2.jpg" alt:"Funnels" class:"img-responsive" %}

#### Aria UI Screenshot of the Funnel steps:

Shows the funnel conversion rate chart, that corresponds with each step of the user flow.


{% img "how-to/funnels/funnel3.jpg" alt:"Funnels" class:"img-responsive" %}

## Stay in Touch

- To file bugs or ask questions, contact [Aria Support][0].

[0]: mailto:ariasupport
[1]: ../funnels-tutorial
[2]: {{ site.portal_url }}/dashboard/ZGFzaGJvYXJk4a4c82fe65f749a8beb8c36ad8b93ebf/tab/dGFif393f5807c8f422c8fe079921e2d29f7?projectId=bac7b6a05f514c49a71e4f4f84364572
[5]: https://aka.ms/whyfunnelsvideotutorialpage
