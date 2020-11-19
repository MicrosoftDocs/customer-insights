---
title: "Custom machine learning models | Microsoft Docs"
description: "Work with custom models from Azure Machine Learning in Dynamics 365 Customer Insights."
ms.date: 08/19/2020
ms.reviewer: wameng
ms.service: dynamics-365-ai
ms.topic: "article"
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Custom machine learning models

**Intelligence** > **Custom Models** lets you manage workflows based on Azure Machine Learning models. Workflows help you choose the data you want to generate from insights and map the results to your Customer Insights data. [Read the blog about extending Customer Insights with custom models](https://cloudblogs.microsoft.com/dynamics365/it/2019/10/04/extending-dynamics-365-customer-insights-with-azure-ml-based-custom-models/) and the [blog with examples of custom models](https://cloudblogs.microsoft.com/dynamics365/it/2019/10/05/examples-of-extending-dynamics-365-customer-insights-with-azure-ml/).

## Responsible AI

Predictions give substantial capabilities to business to create better customer experiences, improve business capabilities and revenue streams, and define completely new ways of doing business. This value can come at a cost to individuals and society, and we strongly recommend you balance the value of your prediction against the impact it has and biases that may be introduced in an ethical manner. Learn more about how Microsoft is [addressing Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6). You can also learn about [techniques and processes](https://docs.microsoft.com/en-us/azure/machine-learning/concept-responsible-ml) specific to Azure Machine Learning.

## Prerequisites

- Currently, this feature only supports web services published through [Azure Machine Learning Classic](https://studio.azureml.net) and **batch** pipelines deployed through the methods [described here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where?tabs=azcli).

- You need an Azure Data Lake Storage Gen2 storage account associated with your Azure Studio instance to use this feature. For more information, see [Create an Azure Data Lake Storage Gen2 storage account](https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-quickstart-create-account)

## Add a new workflow

1. Go to **Intelligence** > **Custom Models** and select **New Workflow**.

1. Give your custom model a recognizable name in the **Name** field.

   > [!div class="mx-imgBorder"]
   > ![Screenshot of the New workflow pane](media/new-workflow.png "Screenshot of the New workflow pane")

1. Select the organization that contains the web service in **Tenant that contains your web service**.

1. If your Azure Machine Learning subscription is in a different tenant than Customer Insights, select **Sign in** with your credentials for the selected organization.

1. Select the Azure Machine Learning workspace associated with your web service. There are two sections listed, one for AMLv1 (Azure Machine Learning Classic) and AMLv2 (Azure Machine Learning). If you're not sure which workspace is the right one, select "Any".

1. Choose the [web service or pipeline you've published using Azure Machine Learning](https://docs.microsoft.com/azure/machine-learning/studio/deploy-a-machine-learning-web-service#deploy-it-as-a-new-web-service) in the **Web service that contains your model** dropdown. Then, select **Next**.

1. For each **Web service input**, select the matching **Entity** from Customer Insights and select **Next**.

   > [!div class="mx-imgBorder"]
   > ![Configure a workflow](media/intelligence-screen2.png "Configure a workflow")

1. Output mapping
   1. AMLv1
      1. Enter the output **Entity name** you want web service output results to flow into.
   1. AMLv2
      1. Enter the output **Entity name** you want pipeline output results to flow into.
      1. Select the **Output data store parameter name** from your pipeline that aligns to your pipeline output node. You can read more about creating parameters for output nodes [here](custom-model-parameterization.md).
      1. Select the **Output Path parameter name** from your pipeline that aligns to your pipeline output node. You can read more about creating parameters for output nodes [here](custom-model-parameterization.md).

1. Select the matching attribute from the **Customer ID in results** drop-down list that identifies customers in Customer Insights and select **Save**.

1. You'll see the **Workflow Saved** screen with details about the workflow.

1. Select **Done**.

## Edit a workflow

1. On the **Custom Models** page, select the vertical ellipsis in the **Actions** column next to a workflow you've previously created and select **Edit**.

1. You can update your workflow's recognizable name in the **Display name** field, but you can't change the web service. Select **Next**.

1. For each **Web service input**, select the matching **Entity** from Customer Insights.  Then, select **Next**.

1. Output mapping
   1. AMLv1
      1. Enter the output **Entity name** you want web service output results to flow into.
   1. AMLv2
      1. Enter the output **Entity name** you want pipeline output results to flow into.
      1. Select the **Output data store parameter name** from your pipeline that aligns to your pipeline output node. You can read more about creating parameters for output nodes [here](custom-model-parameterization.md).
      1. Select the **Output Path parameter name** from your pipeline that aligns to your pipeline output node. You can read more about creating parameters for output nodes [here](custom-model-parameterization.md).

1. Select the matching attribute from the **Customer ID in results** drop-down list.  When you're done, select **Save**.

## Run a workflow

1. On the **Custom Models** page, select the vertical ellipsis in the **Actions** column next to a workflow you've previously created.

1. Select **Run**.

Your workflow also runs automatically with every scheduled refresh. Learn more about [setting up scheduled refreshes](system.md#schedule-tab).

## Delete a workflow

1. On the **Custom Models** page, select the vertical ellipsis in the **Actions** column next to a workflow you've previously created.

1. Select **Delete** and confirm your deletion.

Your workflow will be deleted. The [entity](entities.md) that was created when you created the workflow persists, and can be viewed from the **Entities** page.

## Creating a Batch Pipeline in Designer and create parameters

### Prerequisites

1. You have an experiment successfully running using the Azure Machine Learning

1. In the experiment screen, select **Create inference pipeline** and select **Batch inference pipeline**
[!NOTE] Realtime inference pipelines are not currently supported
1. Set the [input parameters](#inputparameters)
1. Set the [output parameters](#outputparameters)
1. Click **Submit**
1. Select your existing experiment that you created as a part of the prerequisites
1. Click **Submit**

### Input Parameters

1. Select an input node of your pipeline and look for the **Parameters** section of your node
1. Check the **Set as pipeline parameter** box in the Parameters section.
1. Select a name that you can easily identify with the input requirement. This text will be displayed in the Workflow input creation screen later in your custom workflow.
1. Repeat this step for every input node.

### Output parameters
1. Search for an **Export Data** node in the top left search box, then add it to the end of your pipeline ensuring a link is drawn between your last node and the Export Data node.
1. Select the Export Data node and configure the datastore type to **Azure Blob Storage**
1. Select the horizontal ellipses for the Datastore option and select **Add to pipeline parameter**
  1. Set the **Parameter Name** to something you'll recognize when selecting it in the custom workflow definition.
  1. Click **Save**
1. Select the horizontal ellipses for the Path feature and select **Add to pipeline parameter**
  1. Set the **Parameter Name** to something you'll recognize when selecting it in the custom workflow definition.
  1. Click **Save**