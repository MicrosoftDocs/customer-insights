---
layout: page
title: Real-time funnels tutorial
---

## Understanding funnels - concepts and examples

{% include video.html src="Funnels_Talkthrough.mp4" %}

For more videos, refer to the [main funnels page](../funnels).

## How to create funnels and how to visualize funnels

{% include video.html src="FunnelsCreation.mp4" %}

---

{% include video.html src="FunnelsVisualization.mp4" %}

For more details, refer to the key concepts below.

### Prerequisites

To use the Real-Time Funnel feature, your product’s telemetry needs to be flowing into Aria, either via a routing layer like Nexus (used by many Office client teams such as Word, Excel and PPT), or using the Aria SDKs (used by teams like OneNote and Outlook Mobile)

## Key concepts

### Funnel steps

Each step of the funnel is defined by an event. The user needs to complete the funnel steps in the exact sequence. If user completes a step out of sequence, it will be ignored.

Examples:<br>
Example 1: **Step 2 then Step 1:** The funnel service will ignore Step 2 and the user is considered to have completed Step 1 only.<br>
Example 2: **Step 2 then Step 1 then Step 2:** Now the user is considered to have completed Step 2.

> **Note**: For a data analyst, the conversion from Step 1 to Step 2 is important as it provides insights on which steps have high dropoff ratios.

### Funnel key

The correlation ID or common property that all steps of the funnel share. As an example, you may define `UserID` as the correlation ID for your funnel to follow an individual user from one step to the next.

> **Note**: The Funnel key needs to be a property of every event that you used to define your funnel.

### Property filters

While creating the funnel, you can filter each step of the funnel using its event properties. This is particularly useful when you are interested in only a subset of users who entered that step of your funnel. Property filters enable you to add multiple filters using any combination of __AND__ or __OR__ logic operators. Additionally, with property filters you have many operators to choose from: Equals, Not Equals, Starts With, Ends With, Contains, Not Starts With, Not Ends With, Is One Of, and Is Not One Of. Please contact us at [Aria Support][1] if there is an operator you would like us to support.

> **Note**: You can also use property filters when multiple events of your funnel have the same name but are distinguished from each other by some parameter.

For example:<br>
**MyFunnel Step 1**: `Event= PageVisit (Property Filter Set -> pagename= SignInPage)`<br>
**MyFunnel Step 2**: `Event= PageVisit (Property Filter Set -> pagename= ViewCart)`

### Conversion Window

The amount of time you wish to give a user to complete the funnel from the time they enter the funnel. You may want to try out different conversion window values to find the optimum one specific to your application. Some scenarios require conversion windows in minutes, and some may allow many days for the users to enter the funnel and complete it.

### Access Control List (ACL)

If you want to create cross-project funnels, it’s important that your project’s Access Control List contains all the projects you wish to share events with. You can manage your project’s ACL by selecting **Settings** > **ACLs** and then adding or removing projects to your authorized projects. Note that you need write access to a project to successfully modify its ACL. Once you successfully add your desired projects and save your ACL, your authorized projects will then be able to access your project and therefore create cross-project funnels using your project’s events. Cross-project funnels are helpful when you want to track a funnel with events from two or more different Aria projects, such as your Prod Environment project and your Dev Environment project.

## Questions?

If you have any questions, please contact us at [Aria Support][1].

[1]: mailto:ariasupport
[4]: http://idwebelements/GroupManagement.aspx?Group=funnelpilots&Operation=join
