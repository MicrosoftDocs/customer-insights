---
title: Responsible AI FAQs for the journey copilot
description: Discover how to use the journey copilot in Dynamics 365 Customer Insights - Journeys responsibly. These FAQs provide essential guidelines and best practices.
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.topic: faq
author: alfergus
ms.author: alfergus
ms.collection: bap-ai-copilot
ms.custom: 
  - transparency-note
---

# Responsible AI FAQs for the journey copilot

These responsible AI FAQs describe the AI impact of Dynamics 365 Customer Insights - Journeys's journey copilot feature.

## What is the journey copilot?

The journey copilot enables you to use common words and phrases to describe what marketing journey you wish to create. The segment or trigger needs to already exist in your data but can also be in a draft state. Once you type and submit a statement, the service translates it into query using information collected from your segments and triggers and create placeholders for your content. If you're happy with the suggested journey, you can go ahead and select "Create journey" and land in the canvas for further editing such as changing the wait time between messages and adding content to your channels.

## What can I request from the journey copilot?

For the most successful outcome, write prompts that specify your target audience or the trigger that should kick off the journey. Then specify what actions you want the journey to follow.

Some examples:
- Send a personalized message to contacts through email, push, or SMS one hour after they fill out a form.
- When a contact registers for a marketing event, send them reminder emails until they check in for the event.
- Send a promotion email targeting loyalty member and follow up based on whether an email link is clicked.

Here are some examples that won’t work:
- Create a three-step nurture journey with intro, warm up, and call to action for new leads.
    - **Why?**: Because this prompt doesn't include any mention of a trigger or segment that Copilot can search in your database.
    - **A better version**: Create a three-step nurture journey that targets the new lead segment with an intro, warm up, and call to action messages. 

## What are the system’s capabilities?

Journey copilot is built on a machine learning model called GPT-4. Trained on a vast number of text samples from the internet, GPT-4 generates new text in English that looks and sounds like text that was written by a human.

The only time a human reviews the prompts that you have used in the journey copilot is if you report it to Microsoft (using a quick feedback survey built into the feature). This feedback will help improve the suggestions that copilot comes up with in the future.

## What is the system’s intended use?

The journey copilot feature is intended to kick-start the journey creation process without having to learn all the ins and outs of journey orchestration. The simplest way to think about it is that the journey copilot is a mini tutor for journey creation.  

## How was the journey copilot evaluated? What metrics are used to measure performance?

The journey copilot underwent substantial testing before the feature was released. It relies on user feedback to report inappropriate content. If you encounter inappropriate content being generated, report it to Microsoft using this feedback form: [Report abuse](https://msrc.microsoft.com/report/abuse?ThreatType=URL&IncidentType=Responsible%20AI&SourceUrl=https://dynamics.microsoft.com/marketing/overview/). Your feedback helps improve the functionality moving forward.

Microsoft may disable the journey copilot feature for selected customers if abuse of the functionality is detected.

## What are the limitations of the journey copilot? How can users minimize the impact of the journey copilot limitations when using the system?

The journey copilot generates original content, but it isn’t always factual. It supports only the channels and elements available out of the box currently. In addition, because the underlying technology behind the feature uses AI that has been trained on a wide range of internet sources, some suggestions may seem inaccurate to the intended scenario. The journey copilot will also not suggest anything outside of the context of marketing and we block you from using the feature when there's a possibility it might break or corrupt your data. It's your responsibility to edit generated suggestions so that your final journey is accurate.
