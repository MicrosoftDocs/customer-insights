Use the Dynamics 365 CX Model Context Protocol (MCP) Server - Customer Insights to connect Customer Insights data and tools to Microsoft Copilot Studio agents, or to any other MCP client that supports HTTP-based MCP connections. Agent 365 Tooling Gateway is the Microsoft-hosted gateway that fronts the Customer Insights MCP server and handles authentication to Dataverse.

This article helps you:

- Understand how Agent 365 Tooling Gateway authentication works for the Dynamics 365 CX MCP Server - Customer Insights
- Configure a Copilot Studio agent to use the server through Agent 365 Tooling Gateway
- Connect supported external MCP clients, such as Visual Studio Code, GitHub Copilot CLI, Cursor, ChatGPT, and Claude Code

> [!IMPORTANT]
> Enabling connections between Dynamics 365 and non-Dynamics 365 services, including Microsoft or external services, allows data to leave the Dynamics 365 FedRAMP High boundary. Data flowing from Dynamics 365 to other services is processed and stored according to the terms, compliance commitments, and data residency and handling requirements of the destination service.
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
- The OAuth scope targets the Agent 365 Tooling Gateway resource. You can request either the `/.default` scope or the named `McpServers.D365CustomerInsights.All` delegated permission.
- The `/.default` scope doesn't support incremental or dynamic user consent, so admin consent must be granted in advance in the customer tenant. The named permission is user-consentable, so each person can consent for themselves if your tenant allows user consent.
- Add `offline_access` to the requested scopes so the client can refresh the token when it expires. Without it, Microsoft Entra doesn't issue a refresh token, and the connection stops working when the access token expires.
- A `/.default` request never fails because a permission is missing. Microsoft Entra quietly issues a token that carries only the permissions the client already holds, so a client can have a valid gateway token and still get `403 Forbidden` from the MCP server. If calls are denied, decode the token and check that the `scp` claim contains `McpServers.D365CustomerInsights.All`.
- The server URL is specific to the environment, so each environment needs its own connector configuration. The delegated permission is the same for every environment, and both the app ID form and the resource URL form of the scope return the same token.
- Discovery-capable clients read the OAuth metadata automatically. If you add the server from the Copilot Studio tools catalog, the connection is configured for you. You only enter OAuth values by hand when you set the server up manually.

## Prerequisites

- The System Administrator role, to configure the MCP server
- The Dataverse environment ID, which the Agent 365 Tooling Gateway server URL requires
- The customer tenant ID, which the authorization, token, and admin-consent URLs require
- Tenant admin or delegated admin-consent permissions, to set up the server manually or to connect an external MCP client

> [!NOTE]
> The environment ID and the tenant ID aren't interchangeable. Use the environment ID only in the MCP server URL and the discovery URL. Use the tenant ID in every `login.microsoftonline.com` URL.

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

## Provision the Agent 365 Tooling Gateway service principal

The Agent 365 Tooling Gateway app is a Microsoft first-party app registration. Before a client app can request a token for it, the gateway service principal must exist in the customer tenant.

As a tenant admin, run one of the following commands.

```azurecli
az ad sp create --id <ATG-app-id>
```

```powershell
New-MgServicePrincipal -AppId "<ATG-app-id>"
```

Microsoft Entra creates the Agent 365 Tooling Gateway service principal under **Enterprise applications** in the customer tenant.

> [!IMPORTANT]
> Don't try to provision the gateway with an admin-consent URL such as `https://login.microsoftonline.com/<customer-tenant-id>/adminconsent?client_id=<ATG-app-id>`. That URL treats the gateway as a *client* and tries to consent every permission the gateway itself declares, including Microsoft-only APIs. Microsoft Entra blocks consent between two Microsoft first-party apps, so the request fails with an error like `AADSTS65002: Consent between first party application 'ea9ffc3e-8a23-4a7d-836d-234d7c7565c1' and first party resource '00000002-0000-0000-c000-000000000000' must be configured via preauthorization`. The error appears whichever tenant ID you use. Run the commands in this section instead. If you set the server up manually, grant admin consent on your own client app, as described later in this article.

## Add the MCP server to a Copilot Studio agent

There are two ways to add the server to an agent. Check the tools catalog first, because it configures the connection for you.

### Add the server from the tools catalog

When you register the Customer Insights MCP server in your tenant, it appears in the Copilot Studio tools catalog. Adding the server from the catalog sets up the server URL and the OAuth configuration for you, so you don't need to register a Microsoft Entra app, create a client secret, or enter any OAuth values.

1. Open [Copilot Studio](https://copilotstudio.microsoft.com), and then open or create an agent.

1. Go to the **Tools** page for your agent, and then select **Add a tool**.

1. Select the **MCP** filter.

1. Search for `Dynamics 365 CX Customer Insights`.

1. Select the Customer Insights MCP server in the results, and then select **Add**.

1. When prompted, create a connection and sign in with an account that has access to the target Customer Insights environment.

1. Publish the agent.

> [!NOTE]
> A tenant admin can check whether the server is available, or block it, in the Microsoft 365 admin center under **Agents** > **Tools** > **Registry**. To learn more, see [Overview of the Tools page](/microsoft-365/admin/manage/agent-tools-overview). If the server isn't in the catalog, add it manually instead.

### Add the server manually

Use this section only if the Customer Insights MCP server doesn't appear in the catalog. Manual setup uses the Copilot Studio MCP onboarding wizard, and it needs your own Microsoft Entra app to hold the gateway permission.

#### Create a client Microsoft Entra app

Create your own confidential client app in Microsoft Entra ID. This app isn't the Dynamics 365 first-party app, and it only needs permission to access the Agent 365 Tooling Gateway resource scope.

In the [Microsoft Entra admin center](https://entra.microsoft.com), do the following:

1. Create an app registration by following the steps in [Register an application](/entra/identity-platform/quickstart-register-app#register-an-application). Make sure you use a single-tenant app registration.

1. Create a client secret for the app registration. Learn more in [Add a client secret](/entra/identity-platform/how-to-add-credentials?tabs=client-secret). Copy the secret value, because you need it when you configure OAuth in Copilot Studio.

1. Go to **API permissions**, and then select **Add a permission**.

1. Select **APIs my organization uses**.

1. Search for the Agent 365 Tooling Gateway app by using the app ID.

1. Add the `McpServers.D365CustomerInsights.All` delegated permission.

1. Select **Grant admin consent**.

Leave the web redirect URI empty until Copilot Studio generates the callback URL during connector setup.

Granting admin consent here is what puts `McpServers.D365CustomerInsights.All` into the tokens your client requests. If you prefer a consent URL to the portal, use the v2.0 admin-consent endpoint and point it at *your* client app, not at the gateway app.

```http
https://login.microsoftonline.com/<customer-tenant-id>/v2.0/adminconsent?client_id=<your-client-app-id>&scope=<ATG-app-id>/.default&redirect_uri=<redirect-uri-registered-on-your-app>
```

> [!TIP]
> `McpServers.D365CustomerInsights.All` is user-consentable. If your client requests that named permission instead of `/.default`, each person can consent for themselves the first time they sign in, as long as your tenant allows user consent for apps. Tenant-wide admin consent is required only for the `/.default` scope.

#### Configure the MCP server in Copilot Studio

1. Open [Copilot Studio](https://copilotstudio.microsoft.com), and then open or create an agent.

1. Go to the **Tools** page for your agent, select **Add a tool**, select **New tool**, and then select **Model Context Protocol**. Learn more in [Connect your agent to an existing MCP server](/microsoft-copilot-studio/mcp-add-existing-server-to-agent).

1. Provide these details:

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
    | Scope | `<ATG-app-id>/.default offline_access`, for example, `ea9ffc3e-8a23-4a7d-836d-234d7c7565c1/.default offline_access`. To skip tenant-wide admin consent, request the named permission instead: `ea9ffc3e-8a23-4a7d-836d-234d7c7565c1/McpServers.D365CustomerInsights.All offline_access`. Separate scopes with a space. |

After you create the OAuth configuration, Copilot Studio shows a callback URL. Copy it and add it as a **Web** redirect URI on the Microsoft Entra app you created for Copilot Studio.

#### Create the connection and add the tool

In your Copilot Studio agent, complete the following steps:

1. In the **Add tool** dialog, select **Create a new connection**.

1. Sign in with an account that has access to the target Customer Insights environment.

1. Add the tool to the agent.

1. Publish the agent.

## Configure discovery-capable MCP clients

Discovery-capable MCP clients, such as Visual Studio Code, GitHub Copilot CLI, Cursor, ChatGPT, and Claude Code, automatically retrieve the tooling gateway OAuth metadata. For these clients, configure the MCP server URL and let the client handle sign-in.

> [!NOTE]
> Clients that support OAuth discovery for MCP servers don't need a manual OAuth endpoint, client ID, scope, or secret.

Each of these clients signs in with its own Microsoft Entra client app, so a tenant admin still needs to allow that client to call the gateway. If sign-in succeeds but tool calls return `403 Forbidden`, the client's app doesn't have the `McpServers.D365CustomerInsights.All` permission. Grant admin consent for that client app, or point the client at a client app you registered yourself.

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
| `400 EndpointInvalid`, with the message `Environment id ... is invalid.` | The `/environments/` segment holds a tenant ID or a malformed GUID | Use the Dataverse environment ID, not the tenant ID. |
| `401 Unauthorized` | The request has no bearer token, or the token audience isn't the Agent 365 Tooling Gateway | Confirm the scope resolves to the gateway app ID. The `WWW-Authenticate` response header points to the discovery metadata for the server. |
| `403 Forbidden`, with the message `Access denied: Scope 'McpServers.D365CustomerInsights.All' is not present in the request.` | The token is valid for the gateway, but it doesn't carry the Customer Insights permission | Add the `McpServers.D365CustomerInsights.All` delegated permission to the client app and grant admin consent. Decode the token and confirm the permission shows up in the `scp` claim. |
| `AADSTS65002: Consent between first party application ... must be configured via preauthorization` | You ran an admin-consent URL against the gateway app ID, or a Microsoft first-party client asked for a gateway permission it isn't preauthorized for | Provision the gateway service principal with `az ad sp create` or `New-MgServicePrincipal`, and request the permission from a client app you registered yourself. |
| Consent prompt fails for a non-admin user | The `/.default` scope doesn't support dynamic user consent | Have a tenant admin grant admin consent in advance, or request the named `McpServers.D365CustomerInsights.All` permission, which users can consent to themselves. |
| The connection works at first, and then stops | The client has no refresh token, so it can't renew the expired access token | Add `offline_access` to the requested scopes, and create the connection again. |
| Tools are missing from the agent | The calling user lacks privileges for the underlying Dataverse tables | Check the user's security role privileges. |
| The server isn't in the Copilot Studio tools catalog | The server isn't registered or is blocked in the tenant tools registry | Ask a tenant admin to check **Agents** > **Tools** > **Registry** in the Microsoft 365 admin center, or add the server manually. |
