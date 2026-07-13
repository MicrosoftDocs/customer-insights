---
title: 'Copilot - Refresh and perfect your message (preview)'
description: Content rewrite Copilot in Dynamics 365 Customer Insights - Journeys rephrases email, form, SMS, and push notification text. Learn how to enable it and refine content.
ms.date: 07/09/2026
ms.update-cycle: 180-days
ms.topic: how-to
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Copilot - Refresh and perfect your message (preview)

[!INCLUDE [Preview banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Content rewrite Copilot is an AI-assisted editing feature in Dynamics 365 Customer Insights - Journeys. It helps you rephrase, shorten, lengthen, and adjust the tone of email, form, text message, and push notification content.

> [!NOTE]
> Editing text with the content rewrite copilot is available for the following types of content:
> - Emails, email templates
> - Forms
> - Text messages
> - Push notifications

> [!NOTE]
> The content rewrite copilot is currently available only in English in the United States.

> [!Tip]
> Learn about using the content ideas copilot to create inspiring email copy: [Make email creation fun and more efficient with AI-powered content ideas in Dynamics 365 Customer Insights - Journeys](https://cloudblogs.microsoft.com/dynamics365/it/2022/11/30/engage-your-customers-faster-with-ai-powered-marketing-email-content/)

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## What is the content rewrite copilot?

The content rewrite copilot helps you rapidly iterate on your content to optimize your messaging. Whether you're creating content for email, text messages, push notifications, or forms, using Copilot, you can easily rephrase messages, adjust the tone of voice, and shorten or lengthen copy.

Select any text and use the content rewrite copilot to:
- Rewrite the text and choose from different variations
- Change tone of voice to be more engaging, formal, casual, luxurious, or adventurous  
- Shorten or lengthen copy

## Enable the content rewrite copilot

> [!NOTE]
> The content rewrite copilot and other Copilot features are enabled by default and visible in the email, push notification, SMS, and form editors in the United States.

To turn on or off the content rewrite copilot feature switch:
1. Go to **Settings** > **Overview** > **Feature switches**.
1. Enable or disable the **Global Opt-in consent** toggle.

## How to use Copilot to refresh or perfect your content

:::image type="content" source="media/tone-selection-for-copilot.png" alt-text="Screenshot of the content rewrite Copilot dialog in the email editor, showing tone options and generated text suggestions." lightbox="media/tone-selection-for-copilot.png":::

1. Select a **text element** in your email, form, SMS, or push notification message.
1. Select **Rewrite** from the text element contextual menu.
1. To generate different variants of your text, select **Get ideas**. Copilot generates a set of text suggestions. It might take a short while to generate the content (up to 15 seconds, depending on the usage).
1. Browse the generated ideas using the navigation buttons in the content rewrite dialog.
1. To update your text with generated content, select **Insert text**.
1. Select **Tone** and then **Choose one tone** for your content from the dropdown.
1. To shorten your text, select **Shorten**.
1. To lengthen your text, select **Lengthen**.
1. To generate more ideas for the same key points, select **Get more ideas**.

> [!NOTE]
> AI-generated content might be incorrect. Review and edit generated content so your final copy is accurate and appropriate.

> [!NOTE]
> The content rewrite copilot is available only for text with at least 10 words. If the text snippet is shorter or empty, the content rewrite copilot feature is unavailable.

> [!Tip]
> You can refresh only part of a paragraph instead of changing the entire paragraph:
> 1. Select the text you want to update.
> 1. To update the selected text, use any of the Copilot options: "Get ideas," "Tone," "Shorten," or "Lengthen."

:::image type="content" source="media/selected-editable-text-facility.png" alt-text="Screenshot of selected text in the email editor with content rewrite Copilot options available from the contextual menu." lightbox="media/selected-editable-text-facility.png":::

## How does the Copilot technology work?

The content rewrite copilot assistant is built on a machine learning model called GPT-3.5. Trained on a vast number of text samples from the internet, GPT-3.5 generates new text that looks and sounds similar to text that was written by a human. Copilot masks any personal data in generated ideas and shows only the results that are long enough and unique enough to be useful.

## What data does Copilot collect?

The only time a human reviews the content of generated ideas is if you report it to Microsoft (using a quick feedback survey built into the content rewrite copilot feature).

## What if I'm not satisfied with the generated content?

Copilot uses your text as the basis for new suggestions for your email. Include the information you want to get across to your audience in the source text.
 
If you aren't satisfied with the generated content, try one or more of the following:
1. Continue browsing through generated ideas to make sure you've reviewed all of them.
1. Get more ideas using the **Regenerate** button in the content rewrite dialog.
1. Rephrase your text to get new ideas.

Copilot generates original content, but it isn't always factual. In addition, because the underlying technology behind content rewrite uses AI trained on a wide range of internet sources, some text suggestions might include questionable or inappropriate content. Review and edit generated suggestions so your final copy is accurate and appropriate.

> [!IMPORTANT]
> If you encounter inappropriate content being generated, report it to Microsoft using this feedback form: [Report abuse](https://msrc.microsoft.com/report/abuse?ThreatType=URL&IncidentType=Responsible%20AI&SourceUrl=https://dynamics.microsoft.com/marketing/overview/). It will help improve the functionality moving forward.
>
> Microsoft may disable the content rewrite copilot feature for selected customers if abuse of the functionality is detected.

[!INCLUDE [footer-include](./includes/footer-banner.md)]