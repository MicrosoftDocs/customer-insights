Use the Dynamics 365 CX Model Context Protocol (MCP) Server - Customer Insights to connect Customer Insights data and tools to Microsoft Copilot Studio agents, or to any other MCP client that supports HTTP-based MCP connections. Agent 365 Tooling Gateway is the Microsoft-hosted gateway that fronts the Customer Insights MCP server and handles authentication to Dataverse.

This article helps you:

- Understand how Agent 365 Tooling Gateway authentication works for the Dynamics 365 CX MCP Server - Customer Insights
- Configure a Copilot Studio agent to use the server through Agent 365 Tooling Gateway
- Connect supported external MCP clients, such as Visual Studio Code, GitHub Copilot CLI, Cursor, ChatGPT, and Claude Code

> [!IMPORTANT]
> Enabling connections between Dynamics 365 and non-Dynamics 365 services, including Microsoft or external services, allows data to egress outside of the Dynamics 365 FedRAMP High boundary. Data flowing from Dynamics 365 to other services is processed and stored according to the terms, compliance commitments, and data residency and handling requirements of the destination service.
>
> This data might include queries and other data that users in your organization submit to agents. Before you enable MCP server connections for your organization, your tenant administrator should confirm that these connections meet your data security, compliance, residency, and governance requirements.

## How Agent 365 Tooling Gateway authentication works

Agent 365 Tooling Gateway is an OAuth 2.0-protected resource. Each MCP server URL that the gateway fronts exposes OAuth discovery metadata through an anonymous discovery endpoint.

```http
GET https://agent365.svc.cloud.microsoft/.well-known/oauth-protected-resource/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights
```

The discovery response tells the MCP client which authorization server, resource audience, and scopes to use.

```json
{
  "resource_name": "mcp_D365CX_CustomerInsights",
  "resource": "https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights",
  "authorization_servers": [
    "https://login.microsoftonline.com/organizations/v2.0"
  ],
  "scopes_supported": [
    "https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights/.default",
    "openid",
    "profile",
    "offline_access"
  ],
  "bearer_methods_supported": [
    "header"
  ]
}
```

The MCP client requests a token for the Agent 365 Tooling Gateway resource. The gateway then performs the on-behalf-of exchange that lets the request reach Dataverse.

### Key considerations

- The token audience is the tooling gateway, not the Dynamics 365 CX MCP Server - Customer Insights directly.
- The OAuth scope uses the Agent 365 Tooling Gateway resource URL and ends with `/.default`.
- The `/.default` scope doesn't support incremental or dynamic user consent, so admin consent must be granted in advance in the customer tenant.
- The scope is specific to the environment and the server, so each environment needs its own connector configuration.
- Discovery-capable clients read the OAuth metadata automatically. Copilot Studio custom connector setup might require you to enter OAuth values manually.

## Prerequisites

- The System Administrator role, to configure the MCP server
- The Dataverse environment ID, which the Agent 365 Tooling Gateway server URL requires
- Tenant admin or delegated admin-consent permissions

## Agent 365 Tooling Gateway app ID

Agent 365 Tooling Gateway uses a Microsoft Entra app ID. Make a note of it.

| Microsoft Entra app ID |
| --- |
| `ea9ffc3e-8a23-4a7d-836d-234d7c7565c1` |

Use this server URL format:

```http
https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights
```

The `/mcp/environments/` path segment is required. If you leave it out, the request returns `404 RouteNotFound`.

## Provision the service principal and grant admin consent

The Agent 365 Tooling Gateway app is a Microsoft first-party app registration. Before a client app can request a token for it, the gateway service principal must exist in the customer tenant, and the delegated permission must have admin consent.

1. As a tenant admin, open the following admin-consent URL. Replace `<customer-tenant-id>` with the customer tenant ID and `<ATG-app-id>` with the app ID.

    ```http
    https://login.microsoftonline.com/<customer-tenant-id>/adminconsent?client_id=<ATG-app-id>
    ```

1. Sign in as a tenant admin and approve the request.

Microsoft Entra creates the Agent 365 Tooling Gateway resource service principal under **Enterprise applications** in the customer tenant.

You can also provision the service principal manually.

```azurecli
az ad sp create --id <ATG-app-id>
```

```powershell
New-MgServicePrincipal -AppId "<ATG-app-id>"
```

## Create a client Microsoft Entra app for Copilot Studio

To configure a custom connector in Copilot Studio, create your own confidential client app in Microsoft Entra ID. This app isn't the Dynamics 365 first-party app, and it only needs permission to access the Agent 365 Tooling Gateway resource scope.

In the [Microsoft Entra admin center](https://entra.microsoft.com), do the following:

1. Create an app registration by following the steps in [Register an application](/entra/identity-platform/quickstart-register-app#register-an-application). Make sure you use a single-tenant app registration.

1. Create a client secret for the app registration. Learn more in [Add a client secret](/entra/identity-platform/how-to-add-credentials?tabs=client-secret). Copy the secret value, because you need it when you configure OAuth in Copilot Studio.

1. Go to **API permissions**, and then select **Add a permission**.

1. Select **APIs my organization uses**.

1. Search for the Agent 365 Tooling Gateway app by using the app ID.

1. Add the `McpServers.D365CustomerInsights.All` delegated permission.

1. Select **Grant admin consent**.

Leave the web redirect URI empty until Copilot Studio generates the callback URL during connector setup.

## Add the MCP server to a Copilot Studio agent

1. Open [Copilot Studio](https://copilotstudio.microsoft.com), and then open or create an agent.

1. Follow the steps in [Add tools and resources from an MCP server to your agent](/microsoft-copilot-studio/mcp-add-components-to-agent) and provide these details:

    | Field | Value |
    | --- | --- |
    | Server name | Enter a clear name, such as `Dynamics 365 CX MCP Server - Customer Insights through ATG`. |
    | Server description | Describe the capabilities so the orchestrator can route requests to this server. For example, `Use Customer Insights tools to resolve unified customer profiles, read segments, measures, and predictions, check consent, and create journeys.` |
    | Server URL | `https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights` |
    | Authentication | Select **OAuth 2.0**. |

1. Enter the OAuth values from the Agent 365 Tooling Gateway discovery metadata. Use manual configuration unless your Copilot Studio environment supports dynamic OAuth discovery for MCP servers.

    | Field | Value |
    | --- | --- |
    | Client ID | The client ID of the Microsoft Entra app you created for Copilot Studio. |
    | Client secret | The client secret value from that app. |
    | Authorization URL | `https://login.microsoftonline.com/<customer-tenant-id>/oauth2/v2.0/authorize` |
    | Token URL | `https://login.microsoftonline.com/<customer-tenant-id>/oauth2/v2.0/token` |
    | Refresh URL | Same as the token URL. |
    | Scope | `<ATG-app-id>/.default`, for example, `ea9ffc3e-8a23-4a7d-836d-234d7c7565c1/.default` |

After you create the OAuth configuration, Copilot Studio shows a callback URL. Copy it and add it as a **Web** redirect URI on the Microsoft Entra app you created for Copilot Studio.

### Create the connection and add the tool

In your Copilot Studio agent, do the following:

1. In the **Add tool** dialog, select **Create a new connection**.

1. Sign in with an account that has access to the target Customer Insights environment.

1. Add the tool to the agent.

1. Publish the agent.

## Configure discovery-capable MCP clients

Discovery-capable MCP clients, such as Visual Studio Code, GitHub Copilot CLI, Cursor, ChatGPT, and Claude Code, retrieve the tooling gateway OAuth metadata automatically. For these clients, configure the MCP server URL and let the client handle sign-in.

> [!NOTE]
> Clients that support OAuth discovery for MCP servers don't need a manual OAuth endpoint, client ID, scope, or secret.

In every example that follows, replace `<environment-id>` with the Dataverse environment ID for the target environment.

### Visual Studio Code

1. In Visual Studio Code, press Ctrl+Shift+P to open the command palette.

1. Enter `MCP: Add Server`.

1. Select **HTTP** or **Server sent events**.

1. Add the Customer Insights MCP server URL.

    ```json
    {
      "servers": {
        "d365-customer-insights": {
          "type": "http",
          "url": "https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights"
        }
      },
      "inputs": []
    }
    ```

### GitHub Copilot CLI

Add the server to `.mcp.json`.

```json
{
  "mcpServers": {
    "d365-customer-insights": {
      "type": "http",
      "url": "https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights"
    }
  }
}
```

### Cursor

1. Open Cursor.

1. Open **Settings**.

1. Go to **Features** > **MCP Servers**.

1. Select **Add MCP Server**.

1. Add the server configuration.

    ```json
    {
      "mcpServers": {
        "d365-customer-insights": {
          "url": "https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights"
        }
      }
    }
    ```

### ChatGPT

1. Go to **Settings** > **Connectors** > **MCP Servers**.

1. Add the Customer Insights MCP server URL.

    ```http
    https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights
    ```

1. Select **Connect**.

1. Sign in when the Microsoft authentication flow opens.

1. Verify that the MCP tools are registered.

### Claude Code

When Claude Code makes its first MCP request, it discovers the Agent 365 Tooling Gateway OAuth metadata, opens Microsoft sign-in, and stores tokens locally after you authenticate.

Configure the MCP server in Claude Code.

```json
{
  "mcpServers": {
    "d365-customer-insights": {
      "transport": {
        "type": "http",
        "url": "https://agent365.svc.cloud.microsoft/mcp/environments/<environment-id>/servers/mcp_D365CX_CustomerInsights"
      }
    }
  }
}
```

## Troubleshoot

| Symptom | Likely cause | What to do |
|---|---|---|
| `404 RouteNotFound` | The server URL is missing the `/mcp/environments/` path segment | Use the full server URL format. |
| `401 Unauthorized` | The token audience is wrong, or admin consent is missing | Confirm the scope ends with `/.default` and that a tenant admin granted consent for the Agent 365 Tooling Gateway app. |
| Consent prompt fails for a non-admin user | The `/.default` scope doesn't support dynamic user consent | Have a tenant admin grant admin consent in advance. |
| Tools are missing from the agent | The calling user lacks privileges for the underlying Dataverse tables | Check the user's security role privileges. |
