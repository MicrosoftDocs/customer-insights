---
title: Get answers to questions about capabilities from Copilot (preview)
description: Learn how to use Copilot across Customer Insights - Data.
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.reviewer: mhart
ms.topic: how-to
author: jimsonc
ms.author: jimsonc
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# Get answers to questions about capabilities from Copilot (preview)

[!INCLUDE [public-preview-banner](./includes/public-preview-banner.md)]

> [!IMPORTANT]
> Copilot features in Customer Insights - Data are only available in environments in the United States and Switzerland regions. These features may become available in additional regions in future releases.

Copilot in Dynamics 365 Customer Insights - Data can help you achieve your goals by answering your questions about the application and its features. You ask questions in natural language about capabilities and Copilot answers it, using the [official documentation](index.yml), [troubleshooting guides](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights), and blogs from the Microsoft team on how to set up Customer Insights - Data. These sources are organized as a Bing Search index, which is the reason for Copilot showing the disclaimer about Bing Search being used for certain capabilities. To use this capability an admin user needs to provide consent through the [consent experience](copilot-global-consent.md).

Copilot generates responses in accordance with [Microsoft Responsible AI Standards](https://www.microsoft.com/ai/responsible-ai). For more information, see [FAQ for docs-based Q&A capability](faqs-docs-qna.md).

Administrators in Customer Insights - Data can disable all Copilot functionality through the [consent experience](copilot-global-consent.md). Whether Copilot is available in an environment depends on its regions and supported languages.

This Copilot pane is available on all pages of Customer Insights - Data except:

- When create or edit a segment, [Copilot assists you with segment creation](segments-copilot.md) instead.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Get help from Copilot

1. Select the Copilot icon (:::image type="icon" source="media/copilot-icon.png" border="false":::) to expand the **Copilot** pane. The [conversation history](#conversation-history) persists when you close and reopen the side pane.

1. Enter a question about how to use Customer Insights - Data. Alternatively, you can select the suggested prompts that Copilot shows. Once you send your question, Copilot starts generating an answer.

1. The answer appears as a chat message. Each answer contains at least one reference, which is shown as a number in a box. Each reference contains a link to the documentation page that sources the information.

## Conversation history

While you use Copilot, the previous messages remain in the side pane. You can revisit them by scrolling and reference previous answers when asking a follow-up question.

This conversation history is kept temporarily until you close the Customer Insights - Data app.

To clear the conversation history, select the **Reload** button in the header of the side pane.

[!INCLUDE [copilot-availability](includes/copilot-availability.md)]

## Next steps

- [Responsible AI FAQs for Dynamics 365 Customer Insights - Data](responsible-ai-overview.md)
- [FAQ for docs-based Q&A capability](faqs-docs-qna.md)
- [Dialog with data using Copilot](dialog-with-data.md)
