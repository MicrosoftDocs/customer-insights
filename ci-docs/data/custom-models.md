---
title: Use custom models from Azure Machine Learning
description: Learn how to create custom AI models in Azure Machine Learning and use them in your Dynamics 365 Customer Insights workflows.
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.reviewer: alfergus
ms.topic: how-to
author: radsay01
ms.author: rsayyaparaju
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# Use custom models from Azure Machine Learning

Workflows in Dynamics 365 Customer Insights - Data help you choose the data you want to generate insights from and map the results to your unified customer data. Your workflows can include [custom models](azure-machine-learning-experiments.md) enhanced with artificial intelligence (AI) that you create in [Azure Machine Learning](/azure/machine-learning/overview-what-is-azure-machine-learning).

## Prerequisites

> [!NOTE]
> Support for Machine Learning Studio (classic) will end on August 31, 2024. We recommend you [transition to Azure Machine Learning](/azure/machine-learning/migrate-overview) by that date. You can no longer create new Machine Learning Studio (classic) resources, but you can continue to use your existing resources through August 31, 2024.

- Workspace: An [Azure Machine Learning workspace with pipeline](/azure/machine-learning/concept-ml-pipelines)

- Access privileges:

  - Azure Machine Learning workspace with pipeline: [Owner or User Access administrator](/azure/role-based-access-control/rbac-and-directory-admin-roles) privileges

  - Customer Insights - Data environment: Admin or Contributor privileges

- Storage account: An [Azure Data Lake Storage Gen2 account](/azure/storage/blobs/data-lake-storage-quickstart-create-account) that's associated with your Azure Studio instance

Custom models in Customer Insights - Data don't support data sources that are updated with incremental refresh.

Data is transferred between your Customer Insights - Data environment and the selected Azure web services or pipelines in the workflow. When you transfer data to an Azure service, make sure the service is configured to process data in the manner and location necessary to comply with any legal or regulatory requirements.

## Set up an Azure Machine Learning connection

1. In Customer Insights - Data, go to **Settings** > **Connections**.

1. Scroll to **Miscellaneous connections**.

1. Select **Set up** on the **Azure Machine Learning** tile.

1. Enter connection information:

   - **Display name**: Enter a unique, recognizable name that describes the connection. It must start with a letter and contain only letters, numbers, and underscores.
   - **Tenant**: Enter the tenant that's linked to your Azure Machine Learning workspace. Sign in if prompted.
   - **Workspace**: Enter the Azure Machine Learning workspace.

   :::image type="content" source="media/AML-connection.png" alt-text="Screenshot of the Azure Machine Learning connection page.":::

1. Review the data privacy and compliance information and select **I agree**.

1. Select **Save**.

## Add a new workflow

1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use this model** on the **Custom model (Azure Machine Learning v2)** tile.

1. Select the information about the connection:

   - **Connection**: Select a connection to your Azure Machine Learning workspace or select [**Add connection**](#set-up-an-azure-machine-learning-connection) to set up a new one.
   - **Pipeline**: Select a pipeline that's linked to your Azure Machine Learning workspace.
   - **Output Path**: Select the output path that's linked to your pipeline.
   - **Output Datastore**: Select the output datastore that's linked to your pipeline.

1. Select **Get started**.

1. In the **Model name** step, enter or select the following information:

   - **Name**: A recognizable name for the model.
   - **Output table name**: An output table name for the pipeline output results.
   - **Primary key**: The attribute you want as the primary key for your output table.
   - **Customer ID**: The matching attribute that corresponds to the unified customer ID.

   :::image type="content" source="media/custom-model-AML-wizard1.svg" alt-text="Screenshot of the Custom model Azure Machine Learning Model name page.":::

1. Select **Next**.

1. In the **Required data** step, select **Add data**.

1. Add the data to use for your custom model. Map all the attributes in the data and select **Save**.

   You can save and come back to this step, but you can't run the model unless you map all the attributes. You can't add optional attributes. To edit the attributes, change them in your Azure Machine Learning workspace.

1. Select **Next**.

1. In the **Review and run** step, review the model details and make changes if necessary.

1. Select **Save and run**.

[!INCLUDE [manage-include](includes/custom-models-manage.md)]

## Next steps

- [Custom models FAQ](custom-models-faq.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
