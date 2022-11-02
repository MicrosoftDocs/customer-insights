---
title: "Custom machine learning models from Azure Machine Learning"
description: "Work with custom models from Azure Machine Learning in Dynamics 365 Customer Insights."
ms.date: 11/8/2022
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

# Custom machine learning models from Azure Machine Learning

> [!NOTE]
> Support for Machine Learning Studio (classic) will end on 31 August 2024. We recommend you transition to [Azure Machine Learning](/azure/machine-learning/overview-what-is-azure-machine-learning) by that date.
>
> You can no longer create new Machine Learning Studio (classic) resources. Through 31 August 2024, you can continue to use the existing Machine Learning Studio (classic) resources. For more information, see [Migrate to Azure Machine Learning](/azure/machine-learning/migrate-overview).  

Azure Machine Learning (AML) v2 lets you manage workflows based on AML models. Workflows help you choose the data you want to generate insights from and map the results to your unified customer data. For more information about building custom ML models, see [Use Azure Machine Learning-based models](azure-machine-learning-experiments.md).

## Prerequisites

- Workspace: An [AML workspace with pipeline](/azure/machine-learning/concept-ml-pipelines). Obtain the Tenant, Workspace, Pipeline, Output Path, and Output Datasource name.

- Access privileges:
  - For your AML workspace with pipeline: Owner or User Access administrator privileges. For more information, see [Azure roles](/azure/role-based-access-control/rbac-and-directory-admin-roles).
  - For your Customer Insights environment: Admin or Contributor privileges.

- Storage account: An [Azure Data Lake Gen2 storage account](/azure/storage/blobs/data-lake-storage-quickstart-create-account) associated with your Azure Studio instance.

  > [!NOTE]
  > Data is transferred between your Customer Insights instances and the selected Azure web services or pipelines in the workflow. When you transfer data to an Azure service, please ensure that service is configured to process data in the manner and location necessary to comply with any legal or regulatory requirements for that data for your organization.

## Set up an AML connection

1. Go to **Admin** > **Connections**.

1. Scroll to **Miscellaneous connections**.

1. Select **Set up** on the **Azure Machine Learning** tile.

1. Enter connection information.

   - **Display name**: A unique, recognizable name that describes this connection. Must start with a letter and contain only letters, numbers, and underscores.
   - **Tenant**: The tenant linked to your AML workspace.
   - **Workspace**: The AML workspace.

   :::image type="content" source="media/AML-connection.png" alt-text="Screenshot of the Azure Machine Learning connection page.":::

1. Review the data privacy and compliance and select **I agree**.

1. Select **Save**.

## Add a new workflow

1. Go to the **Intelligence** page.

1. On the **Create** tab, select **Use model** on the **Custom model (Azure Machine Learning v2)** tile.

1. Select the information about the connection:

   - **Connection**: A connection to your AML workspace. To set up a new connection, select [**Add connection**](#set-up-an-aml-connection).
   - **Pipeline**: A pipeline linked to your AML workspace.
   - **Output Path**: The output path linked to your pipeline.
   - **Output Datastore**: The output datastore linked to your pipeline.

   :::image type="content" source="media/custom-model-AML.png" alt-text="Custom model AML connection input pane.":::

1. Select **Get started**.

1. In the **Model name** step, enter the following information:

   - **Name**: A recognizable name for the model.
   - **Output entity name**: An output entity name for the pipeline output results.
   - **Primary key**: The attribute you want as the primary key for your output entity.
   - **Customer ID**: The matching attribute that corresponds to the Customer Insight Customer ID.

   :::image type="content" source="media/custom-model-AML-wizard1.png" alt-text="Custom model AML Model name page.":::

1. Select **Next**.

1. In the **Required data** step, select **Add data**.

1. Enter the data to use for your custom model and select **Save**.

1. Select **Next**.

1. In the **Review and run** step, review the model details and make changes if necessary.

1. Select **Save and run**. The **My predictions** page displays.

## Manage an existing workflow

1. Go to **Intelligence** and select the **My predictions** tab.

1. Select the vertical ellipsis (&vellip;) next to a model to view available actions.

   - **Edit** a workflow to change the model configuration or the connection.
   - **Refresh** a workflow on demand. The workflow also runs automatically with every [scheduled refresh](schedule-refresh.md).
   - **Delete** a workflow. The entity used to create the workflow is not deleted.

## View the results

Results from a workflow are stored in the entity name defined for **Model Output Parameters**. Access this data from the [**Data** > **Entities** page](entities.md) or with [API access](apis.md).

### API Access

For the specific OData query to get data from a custom model entity, use the following format:

`https://api.ci.ai.dynamics.com/v1/instances/<your instance id>/data/<custom model output entity name>%3Ffilter%3DCustomerId%20eq%20'<guid value>'`

1. Replace `<your instance id>` with the ID of your Customer Insights environment, which displays in the address bar of your browser when accessing Customer Insights.

1. Replace `<custom model output entity>` with the entity name you provided for the **Model Output Parameters**.

1. Replace `<guid value>` with the Customer ID of the customer you'd like to access. This ID displays on the [customer profiles page](customer-profiles.md) in the CustomerID field.

## Frequently Asked Questions

- Why can't I see my pipeline when setting up a custom model workflow?
  This issue is frequently caused by a configuration issue in the pipeline. Ensure the [input parameter is configured](azure-machine-learning-experiments.md#dataset-configuration), and the [output datastore and path parameters](azure-machine-learning-experiments.md#import-pipeline-data-into-customer-insights) are also configured.

- What does the error "Couldn't save intelligence workflow" mean? 
  Users usually see this error message if they don't have Owner or User Access Administrator privileges on the workspace. The user needs a higher level of permissions to enable Customer Insights to process the workflow as a service rather than using the user credentials for subsequent runs of the workflow.

- Is a private endpoint / private link for my custom model workflow supported?
  Customer Insights does not currently support private endpoint for custom models out of the box, but a manual workaround is available. Please contact support for details.

## Responsible AI

Predictions offer capabilities to create better customer experiences, improve business capabilities, and revenue streams. We strongly recommend you balance the value of your prediction against the impact it has and biases that may be introduced in an ethical manner. Learn more about how Microsoft is [addressing Responsible AI](https://www.microsoft.com/ai/responsible-ai?activetab=pivot1%3aprimaryr6). You can also learn about [techniques and processes for responsible machine learning](/azure/machine-learning/concept-responsible-ml) specific to Azure Machine Learning.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWRElk]

[!INCLUDE [footer-include](includes/footer-banner.md)]
