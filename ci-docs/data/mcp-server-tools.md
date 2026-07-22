---
title: Use tools in the Customer Insights MCP Server (preview)
description: Customer Insights MCP Server tools help Copilot Studio agents unify customer profiles and access predictive insights such as Customer Lifetime Value (CLV) and churn risk.
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

Use the Customer Insights MCP Server to enrich your chat and agent workflows with unified customer data and AI-generated insights. Access extended customer profiles, calculated measures, segment membership, and predictive analytics such as Customer Lifetime Value (CLV) and churn risk, all pulled from your Customer Insights - Data and Customer Insights - Journeys systems.

Quickly get key insights such as:

- Unified customer profiles that combine data from external sources

- Calculated measures that provide processed insights such as purchase activity and reward points

- Segment membership and duplicate contact resolution

- Predictive insights such as CLV and churn risk

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Example scenario: Unifying duplicate lead and contact records

Sally, a Contoso seller, evaluates a new lead for Joe Carmichael, who recently attended a product webinar. 

Sally doesn't realize that the lead is a duplicate of an existing VIP customer, Joseph Carmichael. After the lead is created, Customer Insights - Data matches the lead and contact records and creates a unified customer profile that combines Dynamics 365 data with external contract data.

Francis, a Contoso admin, uses Copilot Studio to give the Contoso Sales and Service agent access to the Customer Insights MCP Server. The agent can access unified customer insights that connect Joe's lead record with Joseph's contact record.

Sally requests details about the lead by using a conversational prompt. The agent returns a unified customer view that includes:

- Webinar interests from the lead record
- Information from Joseph's Dynamics 365 contact record
- Data from external contract systems
- CLV score
- Churn risk
- Segment membership

With this information, Sally can prioritize and engage Joseph more effectively than if she treated the lead as a new customer.

## Add Customer Insights MCP Server to an agent

1. Open Copilot Studio and create a new agent or open an existing agent.

1. Select **Add tool**.
  
1. Select **Model Context Protocol**.

1. Search for **Customer Insights**.

Learn more in [Add tools and resources from an MCP server to your agent](/microsoft-copilot-studio/mcp-add-components-to-agent).

## View tools in the Customer Insights MCP Server

1. Open Copilot Studio and go to the **Tools** tab for your agent.

1. Select the Customer Insights MCP Server to view the available tools. For a tool reference, see [Customer Insights MCP Server tools reference (preview)](mcp-server-tools-reference.md).

## Next steps

- [Customer Insights MCP Server tools reference (preview)](mcp-server-tools-reference.md)
- [Use consent tools in the Customer Insights MCP Server (preview)](../journeys/mcp-server-consent.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
