---
title: "Get answers about Customer Insights - Data from Copilot"
description: "Learn how to use Copilot across Customer Insights - Data"
ms.date:
ms.reviewer: mhart
ms.topic: how-to
author: nikeller
ms.author: nikeller
---

# Copilot in global pane (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 Customer Insights - Data offers a Copilot for all functionalities which helps you achieve your goals by answering your questions about the product. Ask questions in natural language about this product's capabilities. Copilot will provide an answer to each question relying only on the product's public documentation, related [troubleshooting pages](https://learn.microsoft.com/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights) and a blogs by the Microsoft team on how to setup Customer Insights - Data. 

Responses are generated in accordance with [Microsoft Responsible AI Standards](https://www.microsoft.com/ai/responsible-ai). For more information, see [FAQ for docs-based Q&A capability](faqs-docs-qna.md).

# Availability
Administrators in Customer Insights - Data can choose to disable all Copilot functionality for each solution, by using the [consent experience](copilot-global-consent.md).
Whether Copilot is available in a solution depends on the availability of this Copilot, which currently is limited to specific regions and languages. 

This Copilot pane is available on all pages of Customer Insights - Data except the following: 
- When creating or editing a segment, you instead have access to the [Copilot for segment creation](segments-copilot.md).

# How to get help from Copilot

1. Select the Copilot icon (:::image type="icon" source="media/copilot-icon.png" border="false":::) to expand the **Copilot** pane. You can collapse the pane by clicking the **X**. When collapsing and expanding the conversation history will remain. You can learn more about conversation history further below.
1. Ask a question about how to use Customer Insights - Data by typing in the input box. Alternatively you can click the suggested prompts that Copilot shows. Once you send your question, Copilot will start generate an answer.
1. The answer by Copilot will appear as a chat message below your question. Each answer will contain at least one reference, which is shown as a number in a box. Each reference contains a link to the documentation page used.

## Conversation history
While you use Copilot the previous messages will remain as part of the sidecar experience. You can revisit them by scrolling. This allows you to reference previous answers by Copilot when asking a follow-up question.

This conversation history is kept temporarly until you leave the web app. When collapsing and expanding the pane the conversation history will remain.
If you would like to clear the conversation history, you click the **Reload** button in the header of the sidecar. This will clear all of the conversation history.

# Next steps
- [Responsible AI FAQs for Dynamics 365 Customer Insights - Data](responsible-ai-overview.md)
- [FAQ for docs-based Q&A capability](faqs-docs-qna.md)
- [Dialog with data using Copilot](dialog-with-data.md)
