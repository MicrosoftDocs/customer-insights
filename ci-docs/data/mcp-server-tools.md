---
title: Use tools in the Customer Insights MCP Server (preview)
description: Customer Insights MCP server tools help Copilot Studio agents unify customer profiles and access predictive insights like CLV and churn risk.
ms.date: 07/10/2026
ms.topic: how-to
ms.service: customer-insights
ms.collection: bap-ai-copilot
ms.update-cycle: 180-days
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Use tools in the Customer Insights MCP Server (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The Customer Insights [Model Context Protocol (MCP) server](https://modelcontextprotocol.io) exposes Dynamics 365 **Customer Insights - Data** and select **Customer Insights - Journeys** capabilities as callable tools for LLM agents.

Use the Customer Insights MCP server to enrich your chat and agent workflows with unified customer data and AI-generated insights. Access extended customer profiles, calculated measures, segment membership, and predictive analytics like Customer Lifetime Value and churn risk - all pulled from your Customer Insights - Data and Customer Insights - Journeys systems.

Quickly get key insights such as:

- Unified customer profiles with extended data from external sources

- Calculated measures and processed insights (purchase activity, rewards points)

- Segment membership and duplicate contact resolution

- Predictive insights such as Customer Lifetime Value (CLV) and churn risk

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Example scenario: unifying a duplicate lead and contact

Sally is a Contoso seller evaluating a new lead for Joe Carmichael who recently attended a product webinar. What Sally doesn't realize is that the lead is a duplicate for a known customer Joseph Carmichael who is an existing VIP customer. Shortly after the lead was created, Customer Insights - Data matched the lead and contact records, creating a unified customer profile joining Dynamics 365 and external contract data.

Francis, a Contoso admin, used Copilot Studio and gave the Contoso Sales and Service chat agent access to the new Customer Insights MCP server. In just a couple of minutes, their chat agent was enhanced with unified customer insights connecting the Joe lead and the Joseph contact.

Sally requests details about the Joe lead using a conversational prompt and in seconds, sees a unified customer view of the Joe lead's webinar interests along with details from Joseph's Dynamics 365 contact, the external contract data, and Joseph's AI-generated Customer Lifetime Value (CLV) score, churn risk, and the segments Joseph is a member of. Armed with solid understanding of the customer, Sally prioritizes and engages Joseph more effectively than if she had simply treated him as yet another unknown lead.

## Add the Customer Insights MCP Server to an agent

1. Access Copilot Studio and create a new agent or open an existing agent.

1. Select **Add tool** and select **Model Context Protocol**.

1. Search for and select **Customer Insights**.

Learn more in [Add tools and resources from an MCP server to your agent](/microsoft-copilot-studio/mcp-add-components-to-agent).

## View tools in the Customer Insights MCP Server

1. Access Copilot Studio and go to the **Tools** tab for your agent.

1. Select the Customer Insights MCP Server to view the available tools. For tool reference, go to [Customer Insights MCP Server tools reference (preview)](mcp-server-tools-reference.md).

## Next steps

- [Customer Insights MCP Server tools reference (preview)](mcp-server-tools-reference.md)
- [Use consent tools in the Customer Insights MCP Server (preview)](../journeys/mcp-server-consent.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
