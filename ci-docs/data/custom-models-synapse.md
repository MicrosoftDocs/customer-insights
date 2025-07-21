---
title: Use custom models from Azure Synapse
description: Learn how to create custom AI models in Azure Synapse and use them in your Dynamics 365 Customer Insights workflows.
ms.date: 09/01/2023
ms.update-cycle: 180-days
ms.topic: how-to
author: radsay01
ms.author: rsayyaparaju
ms.reviewer: v-wendysmith
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# Use custom models from Azure Synapse

Workflows in Dynamics 365 Customer Insights - Data help you choose the data you want to generate insights from and map the results to your unified customer data. Your workflows can include custom models enhanced with artificial intelligence (AI) that you create in [Azure Synapse Analytics](/azure/synapse-analytics/machine-learning/what-is-machine-learning).

## Prerequisites

The following table describes the prerequisites for creating a model in Azure Synapse Analytics and using it in a Customer Insights - Data workflow.

| Prerequisite | Requirement | Role | User |
| --- | --- | --- | --- |
| Workspace | An [Azure Synapse workspace](/azure/synapse-analytics/get-started-create-workspace) | | |
| Subscription | An active Azure subscription | | |
| Storage account | An [Azure Data Lake Storage Gen2 account](/azure/storage/blobs/data-lake-storage-quickstart-create-account) that's associated with your Azure Synapse workspace | | |
| Access privileges | Customer Insights - Data environment | [Admin or Contributor](/azure/role-based-access-control/rbac-and-directory-admin-roles) | |
| Access privileges | Resource group where Azure Synapse workspace is located | At least [Reader](/azure/role-based-access-control/role-assignments-portal) | - Service principal<br/> - Azure Active Directory (Azure AD) user with Admin permissions in Customer Insights - Data |
| Access privileges | Azure Data Lake Storage Gen2 account where the data is located and which is linked to the Azure Synapse workspace | [Storage Blob Data Contributor](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) | - Azure AD user with Admin permissions in Customer Insights - Data<br/> - [Azure Synapse workspace managed identity](/azure/synapse-analytics/security/synapse-workspace-managed-identity) |
| Access privileges | Azure Synapse workspace | Synapse Administrator | Service principal for Customer Insights - Data |
| Access privileges if your Customer Insights - Data environment stores data in your [own Azure Data Lake Storage](own-data-lake-storage.md) | Data Lake Storage account | At least Reader | User who sets up the connection to Azure Synapse Analytics |

Learn how to use the Azure portal to [assign Azure roles](/azure/role-based-access-control/role-assignments-portal) and [assign an Azure role for access to blob data](/azure/storage/common/storage-auth-aad-rbac-portal).

Data is transferred between your Customer Insights - Data instances and the selected Azure web services or pipelines in the workflow. When you transfer data to an Azure service, make sure the service is configured to process data in the manner and location necessary to comply with any legal or regulatory requirements.

## Set up a Synapse connection

1. In Customer Insights - Data, go to **Settings** > **Connections**.

1. Scroll to **Miscellaneous connections**.

1. Select **Set up** on the **Azure Synapse Analytics** tile.

1. Enter or select connection information:

   - **Display name**: Enter a unique, recognizable name that describes the connection. It must start with a letter and contain only letters, numbers, and underscores.
   - **Choose who can use this connection**: Select **Administrators only** or **administrators and contributors**.
   - **Subscription**: Select an Azure Synapse subscription for this connection.
   - **Workspace**: Select an Azure Synapse workspace or select [**Create new**](/azure/synapse-analytics/quickstart-create-workspace) to set up a new one.
   - **Storage account**: Select an Azure storage account or select [**Link new**](/azure/storage/common/storage-account-create?bc=%2Fazure%2Fsynapse-analytics%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal) to link to a new one.
   - **Container**: Select a container in the selected storage account.

   :::image type="content" source="media/synapse-connection.png" alt-text="Screenshot of the Azure Synapse Analytics connection page.":::
  
1. Review the data privacy and compliance information and select **I agree**.

1. Select **Save**.

## Add a new workflow

1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Custom model (Azure Machine Learning v2)** tile.

1. Select the information about the connection:

   - **Connection**: Select a connection to your Azure Synapse workspace or select [**Add connection**](#set-up-a-synapse-connection) to set up a new one.
   - **Pipeline**: Select a pipeline that's linked to your Azure Synapse workspace.

1. Select **Get started**.

1. In the **Model name** step, enter or select the following information:

   - **Name**: A recognizable name for the model.
   - **Output table name**: An output table name for the pipeline output results.
   - **Primary key**: The attribute you want as the primary key for your output table.
   - **Customer ID**: The matching attribute that corresponds to the unified customer ID.

   :::image type="content" source="media/custom-model-AML-wizard1.png" alt-text="Screenshot of the Azure Synapse Model page.":::
  
1. Select **Next**.

1. In the **Required data** step, select **Add data**.

1. Add the data to use for your custom model. Map all the attributes in the data and select **Save**.

   You can save and come back to this step, but you can't run the model unless you map all the attributes. You can't add optional attributes. To edit the attributes, change them in your Azure Synapse workspace.

1. Select **Next**.

1. In the **Review and run** step, review the model details and make changes if necessary.

1. Select **Save and run**.

[!INCLUDE [manage-include](includes/custom-models-manage.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
