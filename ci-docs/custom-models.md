---
title: "Custom machine learning models from Azure Machine Learning"
description: "Work with custom models from Azure Machine Learning in Dynamics 365 Customer Insights."
ms.date: 05/30/2023
ms.reviewer: mhart
ms.topic: how-to
author: radsay01
ms.author: rsayyaparaju
ms.custom: bap-template
searchScope: 
  - ci-custom-models
  - customerInsights
---

# Custom machine learning models from Azure Machine Learning

> [!NOTE]
> Support for Machine Learning Studio (classic) will end on August 31, 2024. We recommend you transition to [Azure Machine Learning](/azure/machine-learning/overview-what-is-azure-machine-learning) by that date.
>
> You can no longer create new Machine Learning Studio (classic) resources. Through August 31, 2024, you can continue to use the existing Machine Learning Studio (classic) resources. For more information, see [Migrate to Azure Machine Learning](/azure/machine-learning/migrate-overview).  

 Manage workflows based on Azure Machine Learning v2 models. Workflows help you choose the data you want to generate insights from and map the results to your unified customer data. For more information, see [Use Azure Machine Learning-based models](azure-machine-learning-experiments.md).

## Prerequisites

- Workspace: An [Azure Machine Learning workspace with pipeline](/azure/machine-learning/concept-ml-pipelines). Obtain the Tenant, Workspace, Pipeline, Output Path, and Output Datasource name.
- Access privileges:
  - Azure Machine Learning workspace with pipeline: Owner or User Access administrator privileges. For more information, see [Azure roles](/azure/role-based-access-control/rbac-and-directory-admin-roles).
  - Customer Insights environment: Admin or Contributor privileges.
- Storage account: An [Azure Data Lake Gen2 storage account](/azure/storage/blobs/data-lake-storage-quickstart-create-account) associated with your Azure Studio instance.
- Custom models in Customer Insights don't support data sources that are updated with incremental refresh.

  > [!NOTE]
  > Data is transferred between your Customer Insights instances and the selected Azure web services or pipelines in the workflow. When you transfer data to an Azure service, please ensure that service is configured to process data in the manner and location necessary to comply with any legal or regulatory requirements for that data for your organization.

## Set up an Azure Machine Learning connection

1. Go to **Settings** > **Connections**.

1. Scroll to **Miscellaneous connections**.

1. Select **Set up** on the **Azure Machine Learning** tile.

1. Enter connection information.

   - **Display name**: A unique, recognizable name that describes this connection. It must start with a letter and contain only letters, numbers, and underscores.
   - **Tenant**: The tenant linked to your Azure Machine Learning workspace. Sign in if prompted.
   - **Workspace**: The Azure Machine Learning workspace.

   :::image type="content" source="media/AML-connection.png" alt-text="Screenshot of the Azure Machine Learning connection page.":::

1. Review the data privacy and compliance and select **I agree**.

1. Select **Save**.

## Add a new workflow

1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use this model** on the **Custom model (Azure Machine Learning v2)** tile.

1. Select the information about the connection:

   - **Connection**: A connection to your Azure Machine Learning workspace or select [**Add connection**](#set-up-an-azure-machine-learning-connection) to set up a new one.
   - **Pipeline**: A pipeline linked to your Azure Machine Learning workspace.
   - **Output Path**: The output path linked to your pipeline.
   - **Output Datastore**: The output datastore linked to your pipeline.

   :::image type="content" source="media/custom-model-AML.png" alt-text="Custom model Azure Machine Learning connection input pane.":::

1. Select **Get started**.

1. In the **Model name** step, enter the following information:

   - **Name**: A recognizable name for the model.
   - **Output table name**: An output table name for the pipeline output results.
   - **Primary key**: The attribute you want as the primary key for your output table.
   - **Customer ID**: The matching attribute that corresponds to the Customer Insights Customer ID.

   :::image type="content" source="media/custom-model-AML-wizard1.svg" alt-text="Custom model Azure Machine Learning Model name page.":::

1. Select **Next**.

1. In the **Required data** step, select **Add data**.

1. Add the data to use for your custom model. Map all the attributes in the data and select **Save**.

   > [!NOTE]
   > You can save and come back to this step but you can't run the model successfully unless all attributes are mapped. Adding optional attributes is not supported. If you want to edit the attributes, change them in your Azure Machine Learning workspace.

1. Select **Next**.

1. In the **Review and run** step, review the model details and make changes if necessary.

1. Select **Save and run**. The **My predictions** tab displays while the model is being created.

[!INCLUDE [manage-include](includes/custom-models-manage.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
