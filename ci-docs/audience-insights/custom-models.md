---
title: "Custom machine learning models | Microsoft Docs"
description: "Work with custom models from Azure Machine Learning in Dynamics 365 Customer Insights."
ms.date: 11/19/2020
ms.reviewer: zacook
ms.service: dynamics-365-ai
ms.topic: "article"
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Custom machine learning models

**Intelligence** > **Custom models** lets you manage workflows based on Azure Machine Learning models. Workflows help you choose the data you want to generate insights from and map the results to your unified customer data. For more information about building custom ML models, see [Use Azure Machine Learning-based models](azure-machine-learning-experiments.md).

## Responsible AI

Predictions offer capabilities to create better customer experiences, improve business capabilities, and revenue streams. We strongly recommend you balance the value of your prediction against the impact it has and biases that may be introduced in an ethical manner. Learn more about how Microsoft is [addressing Responsible AI](https://www.microsoft.com/ai/responsible-ai?activetab=pivot1%3aprimaryr6). You can also learn about [techniques and processes for responsible machine learning](https://docs.microsoft.com/azure/machine-learning/concept-responsible-ml) specific to Azure Machine Learning.

## Prerequisites

- Currently, this feature only supports web services published through [Azure Machine Learning Classic](https://studio.azureml.net) and batch pipelines deployed through the methods described in [Deploy models with Azure Machine Learning](https://docs.microsoft.com/azure/machine-learning/how-to-deploy-and-where?tabs=azcli).

- You need an Azure Data Lake Gen2 storage account associated with your Azure Studio instance to use this feature. For more information, see [Create an Azure Data Lake Storage Gen2 storage account](https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-quickstart-create-account)

## Add a new workflow

1. Go to **Intelligence** > **Custom models** and select **New workflow**.

1. Give your custom model a recognizable name in the **Name** field.

   > [!div class="mx-imgBorder"]
   > ![Screenshot of the New workflow pane](media/new-workflow.png "Screenshot of the New workflow pane")

1. Select the organization that contains the web service in **Tenant that contains your web service**.

1. If your Azure Machine Learning subscription is in a different tenant than Customer Insights, select **Sign in** with your credentials for the selected organization.

1. Select the **Workspaces** associated with your web service. There are two sections listed, one for Azure Machine Learning v1 (Azure Machine Learning Classic) and Azure Machine Learning v2. If you're not sure which workspace is the right one, select **Any**.

1. Choose the [web service or pipeline you've published using Azure Machine Learning](https://docs.microsoft.com/azure/machine-learning/studio/deploy-a-machine-learning-web-service#deploy-it-as-a-new-web-service) in the **Web service that contains your model** dropdown. Then, select **Next**.

1. For each **Web service input**, select the matching **Entity** from audience insights and select **Next**.

   > [!div class="mx-imgBorder"]
   > ![Configure a workflow](media/intelligence-screen2.png "Configure a workflow")

1. In the **Output mapping** step, set the following properties:
   - Azure Machine Learning v1
      1. Enter the output **Entity name** you want web service output results to flow into.
   - Azure Machine Learning v2
      1. Enter the output **Entity name** you want pipeline output results to flow into.
      1. Select the **Output data store parameter name** from your [pipeline output node](#output-parameters).
      1. Select the **Output Path parameter name** from your [pipeline output node](#output-parameters).

1. Select the matching attribute from the **Customer ID in results** drop-down list that identifies customers and select **Save**.

1. You'll see the **Workflow Saved** screen with details about the workflow.

1. Select **Done**.

## Edit a workflow

1. On the **Custom Models** page, select the vertical ellipsis in the **Actions** column next to a workflow you've previously created and select **Edit**.

1. You can update your workflow's recognizable name in the **Display name** field, but you can't change the web service. Select **Next**.

1. For each **Web service input**, select the matching **Entity** from Customer Insights.  Then, select **Next**.

1. In the **Output mapping** step, set the following properties:
   - Azure Machine Learning v1
      1. Enter the output **Entity name** you want web service output results to flow into.
   - Azure Machine Learning v2
      1. Enter the output **Entity name** you want pipeline output results to flow into.
      1. Select the **Output data store parameter name** from your [pipeline output node](#output-parameters).
      1. Select the **Output Path parameter name** from your [pipeline output node](#output-parameters).

1. Select the matching attribute from the **Customer ID in results** drop-down list.  When you're done, select **Save**.

## Run a workflow

1. On the **Custom Models** page, select the vertical ellipsis in the **Actions** column next to a workflow you've previously created.

1. Select **Run**.

Your workflow also runs automatically with every scheduled refresh. Learn more about [setting up scheduled refreshes](system.md#schedule-tab).

## Delete a workflow

1. On the **Custom Models** page, select the vertical ellipsis in the **Actions** column next to a workflow you've previously created.

1. Select **Delete** and confirm your deletion.

Your workflow will be deleted. The [entity](entities.md) that was created when you created the workflow persists, and can be viewed from the **Entities** page.

## Create a batch pipeline and parameters

If you have an experiment running using Azure Machine Learning, you can create an betach inference pipeline.

1. In Azure Machine Learning, on the experiment page, select **Create inference pipeline** and select **Batch inference pipeline**
   > [!NOTE] 
   > Real-time inference pipelines are currently not supported.

1. Set the [input parameters](#input-parameters)

1. Set the [output parameters](#output-parameters)

1. Select **Submit**.

1. Select your existing experiment that you created as a part of the prerequisites.

1. Select **Submit**.

### Input Parameters

1. Select an input node of your pipeline and look for the **Parameters** section of your node

1. Check the **Set as pipeline parameter** box in the Parameters section.

1. Select a name to recognize the input requirement. This text will be displayed in the Workflow input creation screen later in your custom workflow.

1. Repeat this step for every input node.

### Output parameters

1. Search for an **Export Data** node in the search box and add it to the end of your pipeline. Ensure a link is drawn between your last node and the Export Data node.

1. Select the Export Data node and configure the datastore type to **Azure Blob Storage**

1. Select the horizontal ellipses for the Datastore option and select **Add to pipeline parameter**

1. Set the **Parameter Name** to something you'll recognize when selecting it in the custom workflow definition.

1. Select **Save**

1. Select the horizontal ellipses for the Path feature and select **Add to pipeline parameter**

1. Set the **Parameter Name** to something you'll recognize when selecting it in the custom workflow definition.

1. Select **Save**
1. 