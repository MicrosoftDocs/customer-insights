---
title: Use your own Azure Data Lake Storage account for segments
description: Learn about the requirements to use your own Azure Data Lake Storage account for segments in Customer Insights - Journeys.
ms.date: 11/19/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use your own Azure Data Lake Storage account for segments

Customer Insights - Journeys segmentation includes an option to connect to an Azure Data Lake Storage account using a Microsoft Entra service principal.

Automated tools that use Azure services must use restricted permissions. Instead of requiring applications sign in as a fully privileged user, Azure offers service principals. You can use service principals to securely [add or edit a Common Data Model folder as a data source](/dynamics365/customer-insights/data/connect-common-data-model) or [create or update an environment](/dynamics365/customer-insights/data/create-environment).

## Prerequisites

- The Azure Data Lake Storage account must have a [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace).
- If you have to create a new service principal, you must have admin permissions for your Azure tenant.

## Create a Microsoft Entra service principal for segmentation

Before creating a new service principal for segmentation, check whether one already exists in your organization. In most cases, it already exists.

### Look for an existing service principal

1. Go to the [Azure admin portal](https://portal.azure.com/) and sign in to your organization.
1. From **Azure services**, select **Microsoft Entra**.
1. Under **Manage**, select **Microsoft Application**.
1. Add a filter for **Application ID**. Search for the name "Customer Experience Platform Native Segmentation PROD" or `afc9dd19-c23a-4dc8-9fb7-0ad8cec474ff`.
1. If you find a matching record, it means that the service principal already exists. [Grant permissions](/dynamics365/customer-insights/data/connect-service-principal#grant-permissions-to-the-service-principal-to-access-the-storage-account) for the service principal to access the storage account.

    :::image type="content" source="media/byodl-existing-service-principal.png" alt-text="Screenshot showing an existing service principal." lightbox="media/byodl-existing-service-principal.png":::

1. If no results are returned, follow the next steps to create a new service principal.

### Create a new service principal

1. Install the latest version of Microsoft Entra ID PowerShell for Graph. For more information, see [Install Microsoft Entra ID PowerShell for Graph](/powershell/azure/active-directory/install-adv2).
    1. On your PC, press the Windows key on your keyboard and search for **Windows PowerShell**, the select **Run as administrator**.
    1. In the PowerShell window that opens, enter `Install-Module AzureAD`.
1. Create the service principal with the Microsoft Entra ID PowerShell module.
    1. In the PowerShell window, enter `Connect-AzureAD -TenantId "[your Directory ID]" - AzureEnvironmentName Azure`. Replace [your Directory ID] with the actual Directory ID of your Azure subscription where you want to create the service principal. The environment name parameter, "AzureEnvironmentName," is optional.
    1. Enter `New-AzureADServicePrincipal - AppId "afc9dd19-c23a-4dc8-9fb7-0ad8cec474ff " - DisplayName "Customer Experience Platform Native Segmentation PROD"`. This command creates the service principal on the selected Azure subscription.

## Grant permissions to the service principal to access the storage account

To grant permissions to the service principal for the storage account you want to use, one of the following roles must be assigned to the storage account or container:

| Credential | Requirements |
| --- | --- |
| Currently logged in user | When connecting to the Azure Data Lake using the *Azure subscription* option: <br><br> • **Role**: Storage Blob Data Reader, Storage Blob Contributor, or Storage Blob Owner. <br> • **Level**: Permissions granted on the storage account or the container. <br><br> When connecting to the Azure Data Lake using the *Azure resource* option: <br><br> • **Role**: Microsoft.Storage/storageAccounts/read action <br> • **Level**: Permission granted on the storage account. <br><br> AND <br><br> • **Role**: Storage Blob Data Reader, Storage Blob Contributor, or Storage Blob Owner. <br> • **Level**: Permissions granted on the storage account or the container. <br><br> The Storage Blob Data Reader role is sufficient to read and ingest data to Customer Insights - Data. However, the Storage Blob Data Contributor or Owner role is required to edit the manifest files from within the data connection experience. |
| Customer Experience Platform native segmentation service principal - Using Azure Data Lake Storage as a data source | *Option 1* <br><br> • **Role**: Storage Blob Data Reader, Storage Blob Data Contributor, or Storage Blob Owner.<br> • **Level**: Permissions granted on the storage account. <br><br> *Option 2* (*without sharing service principal access to the storage account*)<br><br> • **Role 1**: Storage Blob Data Reader, Storage Blob Data Contributor, or Storage Blob Data Owner. <br> • **Level**: Permissions granted on the container. <br> • **Role 2**: Storage Blob Data Delegator. <br> • **Level**: Permissions granted on the storage account. |
| Customer Experience Platform native segmentation service principal - Using Azure Data Lake Storage as an output or destination | *Option 1* <br><br> • **Role**: Storage Blob Data Contributor or Storage Blob Data Owner.<br> • **Level**: Permissions granted on the storage account. <br><br> *Option 2* (*without sharing service principal access to the storage account*)<br><br> • **Role 1**: Storage Blob Data Contributor or Storage Blob Data Owner. <br> • **Level**: Permissions granted on the container. <br> • **Role 2**: Storage Blob Data Delegator.<br>• **Level**: Permissions granted on the storage account. |

1. Go to the [Azure admin portal](https://portal.azure.com/) and sign in to your organization.
1. Open the storage account you want the service principal to have access to.
1. On the left pane, select **Access control (IAM)** and then select **Add** > **Add role assignment**.

    :::image type="content" source="media/byodl-grant-permissions.png" alt-text="Screenshot showing adding a role assignment." lightbox="media/byodl-grant-permissions.png":::

1. On the **Add role assignment** pane, set the following properties:
    1. **Role**: Storage Blob Data Reader, Storage Blob Contributor, or Storage Blob Owner based on the credentials listed above.
    1. **Assign access to**: User, group, or service principal.
    1. **Select members**: "**Customer Experience Platform Native Segmentation PROD**" (the service principal you looked up earlier in this procedure).
1. Select **Review + assign**.

It can take up to 15 minutes to propagate the changes.

[!INCLUDE [footer-include](./includes/footer-banner.md)]