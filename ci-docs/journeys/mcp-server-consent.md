---
title: Use consent tools in the Customer Insights MCP Server (preview)
description: Customer Insights MCP Server consent tools explain consent checks, unsubscribe links, security, prerequisites, and limitations for AI agents.
ms.date: 07/09/2026
ms.update-cycle: 180-days
ms.topic: concept-article
ms.collection: bap-ai-copilot
author: PetrJantac
ms.author: alfergus
ms.reviewer: alfergus
---

# Use consent tools in the Customer Insights MCP Server (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Use the Customer Insights Model Context Protocol (MCP) Server to check consent and generate unsubscribe links for compliant outbound messaging. The server exposes consent capabilities through [MCP](https://modelcontextprotocol.io) tools, enabling AI agents and custom integrations to make privacy-compliant messaging decisions in real time using Customer Insights consent data.

Instead of calling internal APIs directly, your agents interact with a single, secure interface using the same consent rules that are enforced during journey execution.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Why use consent through MCP

Using consent through MCP gives you:

- **Consistent interface**: A single, secure contract between AI experiences and Customer Insights consent data.
- **Real-time compliance**: Agents check consent when a message is about to be sent, ensuring the latest customer preferences are respected.
- **Reduced complexity**: No need to call internal consent APIs or replicate enforcement logic.
- **Consistent enforcement**: The same consent rules used by Customer Insights - Journeys apply to all agents and integrations.

## Who should use these tools

The consent MCP tools are designed for customers building AI agent scenarios that require:

- Compliant outbound communication (email, SMS, custom channels)
- Real-time consent checks before sending messages
- Integration with Dynamics 365 Sales, Customer Insights, or Contact Center workflows that require centralized consent checks

> [!NOTE]
> The Shared Consent service can operate independently of a full Customer Insights installation. Consent tools are available even in environments where only Dynamics 365 Sales or Contact Center is deployed.

## Supported consent tools

The following core consent operations are available for compliant outbound communication.

### Check consent before sending

Check whether you can send a message for a given contact point, channel, and purpose (optionally topic). The tool uses the same consent rules enforced during journey execution.

Use this tool to confirm message eligibility before any outbound communication. The tool returns the consent status and, when applicable, the reason a message would be blocked.

#### Typical use case

An AI agent preparing to send a commercial message calls `check_consent` to verify the recipient opted in for the relevant purpose and channel.

#### Example

Check consent for contact point `+111111111`, compliance profile `7f4a6355-1811-4cde-bde3-fee8c85f56b1`, purpose `Commercial` (`10000000-0000-0000-0000-000000000003`), channel type `SMS`, business unit `c507f51d-8f0c-ee11-8f6e-6045bd6ef763`, and topic `Commercial Topic 001` (`23db4a4d-ba9f-f011-bbd3-6045bd194648`).

**Result**:

| Parameter | Value |
|---|---|
| Contact point | +111111111 |
| Channel type | SMS |
| Compliance profile ID | 7f4a6355-1811-4cde-bde3-fee8c85f56b1 |
| Purpose | Commercial (ID: 10000000-0000-0000-0000-000000000003) |
| Topic | Commercial Topic 001 (ID: 23db4a4d-ba9f-f011-bbd3-6045bd194648) |
| Business unit | c507f51d-8f0c-ee11-8f6e-6045bd6ef763 |
| **Consent** | ✅ Granted |

The contact point **+111111111** has the required opted-in consent for both the **Commercial** purpose and the **Commercial Topic 001** topic. SMS messaging to this contact point is permitted under the current compliance settings.

### Get an unsubscribe link

Generate a personalized unsubscribe link that you can embed directly into outbound messages, ensuring a compliant and user-friendly opt-out experience. Each link is unique to the contact point and message context, providing full traceability and auditability.

When a recipient selects the unsubscribe link in a message, it opens the preference center page associated with the compliance profile. The preference center lets recipients manage their communication preferences, for example, opting out of specific purposes or topics, updating contact points, or unsubscribing from all communications. This gives customers full control over what they receive, rather than simply opting out entirely.

You can customize the look and feel of the preference center to match your brand, including updating text, adding purposes and topics, styling the page with custom CSS, and adding custom JavaScript. For more information, see [Create branded, customized preference centers](real-time-marketing-preference-centers.md).

#### Typical use case

An outreach agent generates a message and calls `get_unsubscribe_link` to include a one-click opt-out link in the message body. When the recipient selects the link, they land on a branded preference center where they can fine-tune which communications they want to continue receiving.

#### Example

Generate an unsubscribe link for contact point `+111111111`, entity type `Contact` (`f56302b0-875e-f111-a826-7ced8d6d1623`), message template `226abb7d-855e-f111-a826-7ced8d6d1e7c`, compliance profile `7f4a6355-1811-4cde-bde3-fee8c85f56b1`, purpose `10000000-0000-0000-0000-000000000003`, topic `23db4a4d-ba9f-f011-bbd3-6045bd194648`, and business unit `c507f51d-8f0c-ee11-8f6e-6045bd6ef763`.

**Result**:

| Parameter | Value |
|---|---|
| Contact point | +111111111 |
| Entity type | Contact |
| Entity ID | f56302b0-875e-f111-a826-7ced8d6d1623 |
| Message template ID | 226abb7d-855e-f111-a826-7ced8d6d1e7c |
| Compliance profile ID | 7f4a6355-1811-4cde-bde3-fee8c85f56b1 |
| Purpose ID | 10000000-0000-0000-0000-000000000003 |
| Topic ID | 23db4a4d-ba9f-f011-bbd3-6045bd194648 |
| Business unit ID | c507f51d-8f0c-ee11-8f6e-6045bd6ef763 |

**Generated unsubscribe link**:

```text
https://public-fra.mkt.dynamics.com/api/v2.0/orgs/7b2fdebc-d216-ee11-a66d-0022483903fc/consent/preferences?contextId=fd436906-0633-42a9-8426-c3a6edca0100
```

## Key scenarios

### Agent-driven outbound communication

An AI agent can check consent before sending a message, retrieve an unsubscribe link, and include it in the outbound message, all through MCP tool calls. This ensures every message is compliant by design.

To send a compliant message:

1. Call `check_consent` to confirm the contact is opted in.
1. Call `get_unsubscribe_link` to get a personalized opt-out link.
1. Compose and send the message with the link embedded.

## How it works

The Customer Insights MCP Server is built on the Dataverse custom API pattern. It uses two custom APIs for tool interaction:

- **List tools**: Enumerates all available MCP tools registered on the server.
- **Call tool**: Executes a specific MCP tool by name, passing the required arguments as JSON.

The consent tools delegate all business logic to the existing Backend Consent Service, which handles consent evaluation, normalization, and resolution. This ensures that the MCP tools are always consistent with the consent behavior in Customer Insights - Journeys.

### Architecture overview

The server follows a layered architecture:

1. **Protocol layer**: Custom APIs and Dataverse plugins handle MCP protocol compliance.
1. **Registry layer**: Automatically discovers available tool providers at runtime using reflection-based auto-discovery.
1. **Tool layer**: MCP wrappers that validate inputs and delegate to services.
1. **Service layer**: Business logic that calls the Backend Consent Service.
1. **Data layer**: Dataverse-based storage for consent records.

The MCP server definition lives in the base solution (CxpClient), which ships to every Dynamics 365 organization. Consent tools are added through the Consent solution as an extension. The same layered model is used for future tool providers from Customer Insights - Data and Customer Insights - Journeys.

### MCP server security layers

The MCP server enforces security at multiple layers:

| Layer | Description |
|---|---|
| **Transport security (mTLS)** | Mutual Transport Layer Security (mTLS) certificate-based authentication between Copilot Studio and Dataverse |
| **Custom API privileges** | The platform validates user privileges before allowing tool discovery or execution |
| **Tool-level authorization** | Each tool checks entity-specific privileges (for example, read access to consent purposes) |
| **Data-level security** | Row-level security ensures users access only data they're authorized to see |

> [!NOTE]
> Authorization is enforced inside the tool logic using the caller's user context. The MCP server doesn't escalate privileges implicitly. Tools act as facades and never perform actions beyond what the calling user is permitted to do.

## Prerequisites

Before using the consent tools, you need:

- A Dynamics 365 Customer Insights - Journeys environment, or a Dynamics 365 environment with Shared Consent deployed (for example, Dynamics 365 Sales with Shared Consent).
- At least one compliance profile configured with purposes and topics. A default compliance profile comes with a **Commercial** purpose (restrictive enforcement) and a **Transactional** purpose (non-restrictive enforcement), so you can start using the consent tools immediately without additional configuration.
- The user or agent identity must have the required Dataverse security role privileges for consent entities.

## Limitations

Keep these limitations in mind:

- The consent tools cover consent checks and unsubscribe link generation. Updating consent, administrative operations (such as creating or deleting purposes and topics), and consent model metadata retrieval aren't exposed through MCP.
- **Performance considerations**: Consent checks through MCP may have higher latency compared to direct service calls during journey execution. Consider this when you're designing high-throughput scenarios.
- **Single MCP server**: The Customer Insights MCP Server is a unified server for both Customer Insights - Journeys and Customer Insights - Data. All tools share the same server-level scope definition. Tool-level authorization controls access to individual tools.

## Next steps

- [Consent management overview](real-time-marketing-compliance-settings.md): Learn how consent works in Customer Insights - Journeys.
- [Model Context Protocol specification](https://modelcontextprotocol.io): Review the MCP open standard.

[!INCLUDE [footer-include](./includes/footer-banner.md)]