---
title: "Custom machine learning models from Azure Synapse"
description: "Work with custom models from Azure Synapse in Dynamics 365 Customer Insights."
ms.date: 11/9/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: tutorial
author: radsay01
ms.author: rsayyaparaju
manager: shellyha
searchScope: 
  - ci-custom-models
  - customerInsights
---

# Custom machine learning models from Azure Synapse

Manage workflows based on Azure Synapse Analytics models. Workflows help you choose the data you want to generate insights from and map the results to your unified customer data. For more information, see [Machine learning in Azure Synapse Analytics](/azure/synapse-analytics/machine-learning/what-is-machine-learning).

## Prerequisites

- Workspace: An [Azure Synapse workspace](/azure/synapse-analytics/get-started-create-workspace). Obtain the Tenant, Workspace, Pipeline, Output Path, and Output Datasource name.
- Subscription: An active Azure subscription.
- Access privileges for Customer Insights environment and Azure Synapse workspace:
  - Admin or Contributor privileges for your Customer Insights environment
  - On the resource group where the Azure Synapse workspace is located, the service principal and the Azure AD user with Admin permissions in Customer Insights must be assigned at least **Reader** [permissions](/azure/role-based-access-control/role-assignments-portal).
  - The Azure AD user with Admin permissions in Customer Insights has **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more about [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).
  - The [Azure Synapse workspace managed identity](/azure/synapse-analytics/security/synapse-workspace-managed-identity) has **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace.
  - On the Azure Synapse workspace, the service principal for Customer Insights has **Synapse Administrator** role assigned.
  - If your Customer Insights environment stores data in your [own Azure Data Lake Storage](own-data-lake-storage.md), the user who sets up the connection to Azure Synapse Analytics has at least the built-in **Reader** role on the Data Lake Storage account. For more information, see [Assign Azure roles using the Azure portal](/azure/role-based-access-control/role-assignments-portal).
- Storage account: An [Azure Data Lake Gen2 storage account](/azure/storage/blobs/data-lake-storage-quickstart-create-account) associated with your Azure Synapse workspace.

> [!NOTE]
> Data is transferred between your Customer Insights instances and the selected Azure web services or pipelines in the workflow. When you transfer data to an Azure service, please ensure that service is configured to process data in the manner and location necessary to comply with any legal or regulatory requirements for that data for your organization.

## Set up a Synapse connection

1. Go to **Admin** > **Connections**.

1. Scroll to **Miscellaneous connections**.

1. Select **Set up** on the **Azure Synapse Analytics** tile.

1. Enter connection information.

   - **Display name**: A unique, recognizable name that describes this connection which starts with a letter and contains only letters, numbers, and underscores.
   - **Choose who can use this connection**: Administrators only or administrators and contributors.
   - **Subscription**: An Azure Synapse subscription.
   - **Workspace**: An Azure Synapse workspace or select [**Create new**](/azure/synapse-analytics/quickstart-create-workspace) to create a new one.
   - **Storage account**: An Azure storage account or select [**Link new**](/azure/storage/common/storage-account-create?bc=%2Fazure%2Fsynapse-analytics%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal) to link to a new one.
   - **Container**: A container within the selected storage account.

   :::image type="content" source="media/synapse-connection.png" alt-text="Screenshot of the Azure Machine Learning connection page.":::
  
1. Review the data privacy and compliance and select **I agree**.

1. Select **Save**.

## Add a new workflow

1. Go to the **Intelligence** page.

1. On the **Create** tab, select **Use model** on the **Custom model (Azure Machine Learning v2)** tile.

1. Select the information about the connection:

   - **Connection**: A connection to your Azure Synapse workspace or select [**Add connection**](#set-up-a-Synapse-connection) to set up a new one.
   - **Pipeline**: A pipeline linked to your Azure Synapse workspace.

1. Select **Get started**.

1. In the **Model name** step, enter the following information:

   - **Name**: A recognizable name for the model.
   - **Output entity name**: An output entity name for the pipeline output results.
   - **Primary key**: The attribute you want as the primary key for your output entity.
   - **Customer ID**: The matching attribute that corresponds to the Customer Insights Customer ID.

   :::image type="content" source="media/custom-model-Synapse-wizard.png" alt-text="Screenshot of the Azure Synapse Model page.":::
  
1. Select **Next**.

1. In the **Required data** step, select **Add data**.

1. Add the data to use for your custom model. Map all the attributes in the data and select **Save**.

   > [!NOTE]
   > You can save and come back to this step but you can't run the model successfully unless all attributes are mapped. Adding optional attributes is not supported. If you want to edit the attributes, change them in your Azure Synapse workspace.

1. Select **Next**.

1. In the **Review and run** step, review the model details and make changes if necessary.

1. Select **Save and run**. The **My predictions** tab displays while the model is being created.

[!INCLUDE [manage-include](includes/custom-models-manage.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
