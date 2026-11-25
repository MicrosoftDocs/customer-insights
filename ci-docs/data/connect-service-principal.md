---
title: Connect to an Azure Data Lake Storage account by using a Microsoft Entra service principal
description: Connect to an Azure Data Lake Storage account using a Microsoft Entra service principal in Customer Insights - Data. Learn how to set up secure, restricted access.
ms.date: 11/23/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: sfi-image-nochange
---

# Connect to an Azure Data Lake Storage account by using a Microsoft Entra service principal

[!INCLUDE [azure-ad-to-microsoft-entra-id](../journeys/includes/azure-ad-to-microsoft-entra-id.md)]

Dynamics 365 Customer Insights - Data provides an option to connect to an Azure Data Lake Storage account by using a Microsoft Entra service principal.

Automated tools that use Azure services must have restricted permissions. Instead of having applications sign in as a fully privileged user, Azure offers service principals. Use service principals to securely [add or edit a Common Data Model folder as a data source](connect-common-data-model.md), [add or edit Delta tables as a data source](connect-delta-lake.md), or [create or update an environment](create-environment.md).

## Prerequisites

- The Data Lake Storage account has [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace).
- Admin permissions for your Azure tenant, if you need to create a new service principal.

## Create Microsoft Entra service principal for Customer Insights

Before creating a new service principal for Customer Insights, check whether it already exists in your organization. In most cases, it already exists.

### Look for an existing service principal

1. Go to the [Azure admin portal](https://portal.azure.com) and sign in to your organization.

1. From **Azure services**, select **Microsoft Entra**.

1. Under **Manage**, select **Microsoft Application**.

1. Add a filter for **Application ID start with** `0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff` or search for the name `Dynamics 365 AI for Customer Insights`.

1. If you find a matching record, the service principal already exists. [Grant permissions](#grant-permissions-to-the-service-principal-to-access-the-storage-account) for the service principal to access the storage account.

   :::image type="content" source="media/ADLS-SP-AlreadyProvisioned.png" alt-text="Screenshot of an existing service principal.":::

1. If no results are returned, [create a new service principal](#create-a-new-service-principal).

### Create a new service principal

1. Install the latest version of Microsoft Entra ID PowerShell for Graph. For more information, see [Install Microsoft Entra ID PowerShell for Graph](/powershell/azure/active-directory/install-adv2).

   1. On your PC, press the Windows key on your keyboard, search for **Windows PowerShell**, and select **Run as administrator**.

   1. In the PowerShell window that opens, enter `Install-Module AzureAD`.

1. Create the service principal with the Microsoft Entra ID PowerShell module.

   1. In the PowerShell window, enter `Connect-AzureAD -TenantId "[your Directory ID]" -AzureEnvironmentName Azure`. Replace *[your Directory ID]* with the actual Directory ID of your Azure subscription where you want to create the service principal. The environment name parameter, `AzureEnvironmentName`, is optional.
  
   1. Enter `New-AzureADServicePrincipal -AppId "0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff" -DisplayName "Dynamics 365 AI for Customer Insights"`. This command creates the service principal on the selected Azure subscription.

## Grant permissions to the service principal to access the storage account

To grant permissions to the service principal for the storage account you want to use in Customer Insights - Data, assign one of the following roles to the storage account or container:

|Credential|Requirements|
|----------|------------|
|Currently logged in user| When connecting to the Azure Data Lake using the *Azure subscription* option: <ul><li>**Role**: Storage Blob Data Reader, Storage Blob Contributor, or Storage Blob Owner.</li><li>**Level**: Permissions granted on the storage account or the container.</li></ul><br>When connecting to the Azure Data Lake using the *Azure resource* option: <ul><li>**Role**: Microsoft.Storage/storageAccounts/read action</li><li>**Level**: Permission granted on the storage account</li></ul><br>AND<br><ul><li>**Role**: Storage Blob Data Reader, Storage Blob Contributor, or Storage Blob Owner.</li><li>**Level**: Permissions granted on the storage account or the container.</li></ul><br>Storage Blob Data Reader role is sufficient to read and ingest data to Customer Insights – Data. However, the Storage Blob Data Contributor or Owner role is required to edit the manifest files from within the data connection experience.|
|Customer Insights Service Principal -<br>Using Azure Data Lake Storage as a data source</br>|Option 1<ul><li>**Role**: Storage Blob Data Contributor or Storage Blob Data Owner.</li><li>**Level**: Permissions granted on the storage account.</li></ul>Option 2 *(without sharing Service Principal access to the storage account)*<ul><li>**Role 1**: Storage Blob Data Contributor or Storage Blob Data Owner.</li><li>**Level**: Permissions granted on the container.</li><li>**Role 2**: Storage Blob Data Delegator.</li><li>**Level**: Permissions granted on the storage account.</li></ul>|
|Customer Insights Service Principal - <br>Using Azure Data Lake Storage as an output or destination</br>|Option 1<ul><li>**Role**: Storage Blob Data Contributor or Storage Blob Owner.</li><li>**Level**: Permissions granted on the storage account.</li></ul>Option 2 *(without sharing Service Principal access to the storage account)*<ul><li>**Role**: Storage Blob Data Contributor or Storage Blob Owner.</li><li>**Level**: Permissions granted on the container.</li><li>**Role 2**: Storage Blob Delegator.</li><li>**Level**: Permissions granted on the storage account.</li></ul>|

1. Go to the [Azure admin portal](https://portal.azure.com) and sign in to your organization.

1. Open the storage account you want the service principal to have access to.

1. On the left pane, select **Access control (IAM)**, and then select **Add** > **Add role assignment**.

   :::image type="content" source="media/ADLS-SP-AddRoleAssignment.png" alt-text="Screenshot of the Azure portal while adding a role assignment.":::

1. On the **Add role assignment** pane, set the following properties:
   - **Role**: Storage Blob Contributor, or Storage Blob Owner based on credentials listed above.
   - **Assign access to**: **User, group, or service principal**
   - **Select** members: **Dynamics 365 AI for Customer Insights** (the [service principal](#create-a-new-service-principal) you looked up earlier in this procedure)

1. Select **Review + assign**.

It can take up to 15 minutes to propagate the changes.

## Enter the Azure resource ID or the Azure subscription details in the storage account attachment to Customer Insights -Data

Attach a Data Lake Storage account in Customer Insights - Data to [store output data](manage-environments.md) or [use it as a data source](connect-dataverse.md). Choose between a [resource-based](#resource-based-storage-account-connection) or a [subscription-based](#subscription-based-storage-account-connection) approach and follow those steps.

### Resource-based storage account connection

1. Go to the [Azure admin portal](https://portal.azure.com), sign in to your subscription, and open the storage account.

1. On the left pane, go to **Settings** > **Endpoints**.

1. Copy the storage account resource ID value.

1. In Customer Insights - Data, insert the resource ID in the resource field displayed on the storage account connection screen.

   :::image type="content" source="media/ADLS-SP-ResourceIdConnection.png" alt-text="Screenshot of entering the storage account resource ID information.":::

1. Continue with the remaining steps to attach the storage account.

### Subscription-based storage account connection

1. Go to the [Azure admin portal](https://portal.azure.com), sign in to your subscription, and open the storage account.

1. On the left pane, go to **Settings** > **Properties**.

1. Review the **Subscription**, **Resource group**, and the **Name** of the storage account to make sure you select the right values in Customer Insights - Data.

1. In Customer Insights - Data, choose the values for the corresponding fields when attaching the storage account.

1. Continue with the remaining steps to attach the storage account.

## Diagnose storage access errors

If Customer Insights - Data shows **Couldn't add resource** with **Storage access forbidden**, Azure Storage might have rejected the request because of permissions or network restrictions. This message alone doesn't confirm that a role assignment is missing.

Check access for both the user who connects the storage account and the Customer Insights service principal. These are separate identities. Access granted to one doesn't establish access for the other.

### Confirm the resource and effective access

Before changing permissions, confirm that you're checking the same storage account, container, and user as the failed operation.

1. In the Azure portal, open the storage account used in the connection. Confirm its full name, subscription, and resource group.

1. Select **Containers**, open the target container, and select **Access control (IAM)**.

1. Use **Check access** to look up the user who performed the failed operation. Review the assigned roles, assignment scopes, conditions, and deny assignments against the requirements in [Grant permissions](#grant-permissions-to-the-service-principal-to-access-the-storage-account). An account-level check doesn't show assignments made only at a child container.

1. If access comes through a group, confirm the user's membership and any nested groups that connect the user to the role assignment. A group name that contains a role name doesn't establish that the group has that role on the target resource.

1. If you use Microsoft Entra Privileged Identity Management (PIM), confirm that the required group membership or role is active, not just eligible.

1. Repeat the access check for the Customer Insights service principal. Use application ID `0bfc4568-a4ba-4c58-bd3e-5d3e76bd7fff` to identify the application, and use its service principal object ID in your tenant to identify role assignments. Check any required account-level role separately from container-level access.

After permission changes propagate, sign out of Customer Insights - Data, sign in again, and retry. Learn more in [List role assignments for a user at a scope](/azure/role-based-access-control/role-assignments-list-portal#list-role-assignments-for-a-user-at-a-scope).

### Capture Blob service diagnostic logs

Use Azure Storage resource logs to investigate the request that fails. The Azure Activity log records management operations, not the Blob data-plane access check.

Ask an Azure administrator with permission to configure diagnostic settings and use the destination Log Analytics workspace to complete these steps.

1. On the target storage account, select **Monitoring** > **Diagnostic settings**, and then select the **Blob** service (`blobServices/default`).

1. If a diagnostic setting already collects the required logs, use its existing destination. Otherwise, select **Add diagnostic setting**.

1. Enable **StorageRead** to capture the read request used for connection validation. Also enable **StorageWrite** or **StorageDelete** if you're investigating a write or delete operation.

1. Select **Send to Log Analytics workspace**, choose an approved workspace, and select **Resource specific** as the destination table mode if offered. Save the setting. The query in the next section uses the resource-specific `StorageBlobLogs` table.

1. Allow logging to start, and then reproduce the failure from **Customer Insights - Data**, using the affected user and the same connection details. Record the UTC time and the Customer Insights request ID shown with the error.

> [!NOTE]
> Logs aren't collected retroactively. If logging wasn't enabled when the original request failed, reproduce the failure after enabling it. Initial delivery can take up to 90 minutes. Log ingestion and retention can incur charges.

Don't disable the storage firewall or grant broader roles just to collect diagnostic logs. Review the [Customer Insights private link requirements](private-link.md) if the account restricts network access. A successful test from the Azure portal or a user's computer doesn't establish that Customer Insights has an allowed network path.

For diagnostic setting configuration, see [Create diagnostic settings in Azure Monitor](/azure/azure-monitor/essentials/create-diagnostic-settings).

### Find the failed request in Log Analytics

Open **Logs** in the destination Log Analytics workspace. Run the following query, replacing `<storage-account-name>` with the account name. Adjust the time range to include the UTC time of your retry.

```kusto
StorageBlobLogs
| where TimeGenerated > ago(1h)
| where AccountName == "<storage-account-name>"
| where StatusCode in ("401", "403")
| project TimeGenerated, OperationName, StatusCode, StatusText,
    AuthenticationType, RequesterObjectId, RequesterAppId,
    RequesterTenantId, CallerIpAddress, Uri, ClientRequestId,
    CorrelationId, AuthorizationDetails
| order by TimeGenerated desc
```

Match records by UTC time, account, requested container or URI, and operation. The Customer Insights request ID isn't necessarily forwarded as the Storage `ClientRequestId`, so don't rely on an exact ID match alone. Account-level operations, such as a delegation-key request, might not include a container in the URI.

Review these fields:

| Field | What to check |
|---|---|
| `StatusText` | The Storage service error code, which is more specific than the generic Customer Insights message. |
| `AuthenticationType`, `RequesterObjectId`, and `RequesterAppId` | How the request authenticated and which identity it used. For OAuth requests, compare the object ID with the affected user's or service principal's object ID. A delegated user request can identify the Customer Insights application in `RequesterAppId`; the application ID alone doesn't mean the request used application-only authentication. Some fields might be empty. |
| `CallerIpAddress` | The source address that Storage observed. Use it with the account's network configuration; it isn't necessarily the user's browser address. |
| `OperationName`, `Uri`, and `AuthorizationDetails` | The operation and resource that failed, and authorization details where available. |

Use the Storage error code to choose the next check:

| Storage error code | Next check |
|---|---|
| `AuthorizationPermissionMismatch` | Verify that the requesting identity has the data permissions required for the operation at the correct scope. Review role conditions and, where applicable, Data Lake Storage ACLs. For SAS authentication, check the permissions on the SAS instead. |
| `AuthorizationFailure` | Review public network access, storage firewall rules, virtual network restrictions, private endpoint configuration, and any network security perimeter rules. This code commonly indicates a network restriction; it doesn't identify the specific rule by itself. |
| `AuthenticationFailed` | Review the authentication details, including token validity, tenant, and audience for OAuth requests, or the signature and expiry for SAS requests. Don't share access tokens, account keys, or SAS signatures. |

For other codes and additional causes, see [Troubleshoot 403 errors in Azure Blob Storage](/troubleshoot/azure/azure-storage/blobs/authentication/storage-troubleshoot-403-errors).

If you don't find a matching row, confirm the Blob service diagnostic setting, workspace, collection mode, and time range. Allow for ingestion delay, and retry if needed. No matching row doesn't establish that access is allowed. Remove the status filter to check for other responses.

[!INCLUDE [footer-include](includes/footer-banner.md)]
