---
title: Copilot - Use AI to kickstart email creation
description: Content ideas Copilot in Dynamics 365 Customer Insights - Journeys generates email draft ideas from key points. Learn how to enable it and use your organization's emails.
ms.date: 07/09/2026
ms.update-cycle: 180-days
ms.topic: article
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Copilot - Use AI to kickstart email creation

> [!NOTE]
> The content ideas copilot is currently available worldwide in the following languages:
> - **cs**: Czech
> - **da**: Danish
> - **de**: German
> - **el**: Greek
> - **en**: English
> - **es**: Spanish
> - **fi**: Finnish
> - **fr**: French
> - **it**: Italian
> - **ja**: Japanese
> - **ko**: Korean
> - **nb**: Norwegian Bokmål
> - **nl**: Dutch
> - **pl**: Polish
> - **pt-br**: Brazilian Portuguese
> - **ru**: Russian
> - **sv**: Swedish
> - **th**: Thai
> - **tr**: Turkish
> - **zh-Hans**: Simplified Chinese

> [!Tip]
> Learn about using Copilot to create inspiring email content ideas in our latest blog: [Make email creation fun and more efficient with AI-powered content ideas in Dynamics 365 Customer Insights - Journeys](https://cloudblogs.microsoft.com/dynamics365/it/2022/11/30/engage-your-customers-faster-with-ai-powered-marketing-email-content/).

Content ideas Copilot is an AI-assisted feature in Dynamics 365 Customer Insights - Journeys that generates email draft ideas from your key points. This article explains how content ideas Copilot works and how to use it when creating emails.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=3bd21ca7-e598-4d73-895a-37dbf678f7fc]

## What is the content ideas copilot?

The content ideas copilot acts like a brainstorming partner while you write an email. You provide a short list of initial thoughts (key points) and select a tone of voice, and Copilot generates longer content suggestions that you can build on. You can add these suggestions to your draft, use them as inspiration for a new draft, or go in a different direction altogether.

:::image type="content" source="media/real-time-marketing-copilot-content-ideas.png" alt-text="Screenshot of the content ideas Copilot pane in the email editor, showing key points, tone of voice, and generated suggestions." lightbox="media/real-time-marketing-copilot-content-ideas.png":::

## Enable the content ideas copilot

> [!NOTE]
> In the North America (NAM) region, the content ideas copilot and other Copilot features are enabled by default and visible in the email editor toolbox. In other regions, you need to turn them on in the app settings.

### Turn on or off the content ideas copilot feature switch

1. Go to **Settings** > **Overview** > **Feature switches**.
1. Enable or disable the **Global Opt-in consent** toggle.
1. Enable or disable the **Copilot data movement across geographies** toggle.

## How to use Copilot to generate content ideas

1. Select the **Copilot** button in the email editor toolbox or above the text on the canvas to open the Copilot pane.
1. If your email contains at least 10 words, Copilot uses your email content to fill in recommended **key points** for new ideas. You can then refine them. If your email is empty or contains fewer than 10 words, choose **Topic of your email** from the list of suggested topics or select **Custom**.
    1. If you select one of the suggested topics, Copilot automatically fills in sample key points for you, which you can modify according to your needs.
    1. If you select a custom topic, add up to five key points that you want to get across in your email (a minimum of three words per key point is recommended). You can also use premade examples (select the **See examples** link and then **Use this example** for a selected set of key points).
1. Select the **Tone of voice**.
1. Select **Get ideas**.
1. Copilot generates a set of text suggestions. Generating content can take up to 15 seconds, depending on usage.
1. Browse the generated ideas using the scrollbar in the content ideas pane.
1. Select **Get more ideas** to generate more ideas for the same key points.

    > [!NOTE]
    > Content ideas are suggestions. Review and edit generated suggestions so your final copy is accurate and appropriate.

:::image type="content" source="media/real-time-marketing-copilot-content-ideas-1.png" alt-text="Screenshot of the content ideas Copilot pane with multiple generated email suggestions for selected key points." lightbox="media/real-time-marketing-copilot-content-ideas-1.png":::

## Generate ideas using your organization's emails

You can provide personalized context to the content ideas copilot feature. The content ideas copilot analyzes your organization's existing ready-to-send or live marketing emails (minimum 20), along with a wide range of internet sources, to increase the relevance of generated ideas. The analysis is a one-time process that can take up to a few hours.

To begin the Copilot analysis:

1. Select the **Copilot** button in the email editor toolbox to display the content ideas pane.
1. If there are enough ready-to-send/live marketing emails in your organization to start the analysis process (minimum 20) and you have read permission to access all the emails, select the **Enable** button.
1. A pop-up window lets you know it's ready to analyze your emails. This one-time process can take up to a few hours. Select **Enable** to proceed.
    > [!NOTE]
    > You can start the analysis process only if you have read permission for all the emails in your organization.
1. After the existing email analysis is complete, you'll be able to generate ideas using your organization's emails.

    To generate ideas, add up to five key points in the content ideas pane. Select the **Generate ideas using your organization's emails** checkbox, and then select **Get ideas**.

## How does the Copilot technology work?

The content ideas copilot assistant is built on a machine learning model called GPT-3.5. Trained on a vast number of text samples from the internet, GPT-3.5 generates new text in English that looks and sounds similar to text that was written by a human. Copilot uses GPT-3.5 as a foundation, then considers your organization's recent (English) ready-to-send emails and the key messaging points that you share for each new email draft. Copilot masks any personal data in generated ideas and shows only the results that are long enough and unique enough to be useful.

## What data does Copilot collect?

If you grant permission, Copilot automatically reviews your organization's recent English ready-to-send emails without human review. The only time a human reviews generated ideas is if you report them to Microsoft by using the quick feedback survey built into the content ideas feature.

## What if I'm not satisfied with the generated content?

Copilot uses the key points you add to generate suggestions for your email. Make sure to provide good key points that touch on the top themes you want to get across to your audience. Include two to five key points. Use a group of words or a full sentence for each key point.
 
If you aren't satisfied with the generated ideas, try one or more of the following:

1. Continue browsing through generated ideas to make sure you've reviewed all of them.
1. Get more ideas based on the already provided key points.
1. Rephrase or add more key points to get new ideas.

Copilot generates original content, but it isn't always factual. In addition, because the underlying technology behind content ideas uses AI trained on a wide range of internet sources, some text suggestions might include questionable or inappropriate content. Review and edit generated suggestions so your final copy is accurate and appropriate.

> [!IMPORTANT]
> If you encounter inappropriate content being generated, report it to Microsoft using this feedback form: [Report abuse](https://msrc.microsoft.com/report/abuse?ThreatType=URL&IncidentType=Responsible%20AI&SourceUrl=https://dynamics.microsoft.com/marketing/overview/). It will help improve the functionality moving forward.
>
> Microsoft may disable the content ideas feature for selected customers if abuse of the functionality is detected.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
