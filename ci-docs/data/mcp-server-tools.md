---
title: Use tools in the Customer Insights MCP Server (preview)
description: Discover how Customer Insights MCP server tools help agents unify customer profiles, retrieve segments and measures, and access predictive insights.
ms.date: 07/07/2026
ms.topic: how-to
ms.service: customer-insights
ms.collection: bap-ai-copilot
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

## Scenario

Sally is a seller who is evaluating a lead named Joe who recently attended a webinar for a new product launch event. Sally doesn't know that Joe has several contact records and is a known contact with existing paid licenses for several products, elevating Joe from a simple lead to a VIP customer. Sally's team recently used Copilot Studio and the Customer Insights MCP server to create an insights agent that displays additional customer details from the unified profile and insights created by Customer Insights - Data. Because Customer Insights - Data unifies her company's purchase and rewards system with Dataverse customer data, Sally can see all the extended customer insights from their external systems data like rewards points and product keys Joe purchased. Sally can also see AI-generated insights such as the CLV score, churn risk, and the segments Joe is a member of. Armed with a wealth of customer data, Sally can engage her contacts more effectively than ever.

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
