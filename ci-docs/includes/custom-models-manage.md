
## Manage an existing workflow

1. Go to **Intelligence** and select the **My predictions** tab.

1. Select the vertical ellipsis (&vellip;) next to a model to view available actions.

   - **Edit** a workflow to change the model configuration or the connection.
   - **Refresh** a workflow on demand. The workflow also runs automatically with every [scheduled refresh](/schedule-refresh.md).
   - **Delete** a workflow. The entity used to create the workflow is not deleted.

## View the results

Results from a workflow are stored in the **Output entity name** you defined. Access this data from the [**Data** > **Entities** page](/entities.md) or with [API access](/apis.md).

### API Access

For the specific OData query to get data from a custom model entity, use the following format:

`https://api.ci.ai.dynamics.com/v1/instances/<your instance id>/data/<custom model output entity name>%3Ffilter%3DCustomerId%20eq%20'<guid value>'`

1. Replace `<your instance id>` with the ID of your Customer Insights environment, which displays in the address bar of your browser when accessing Customer Insights.

1. Replace `<custom model output entity>` with the entity name you provided during the **Model name** step.

1. Replace `<guid value>` with the Customer ID of the customer you'd like to access. This ID displays on the [customer profiles page](/customer-profiles.md) in the CustomerID field.

## Frequently Asked Questions

- Why can't I see my pipeline when setting up a custom model workflow?
  This issue is frequently caused by a configuration issue in the pipeline. Ensure the [input parameter is configured](/azure-machine-learning-experiments.md#dataset-configuration) and the [output datastore and path parameters](/azure-machine-learning-experiments.md#import-pipeline-data-into-customer-insights) are also configured.

- What does the error "Couldn't save intelligence workflow" mean? 

- Can I use a private endpoint with my custom model from Azure Machine Learning?
  Customer Insights does not currently support private endpoints with custom models out of the box. Please contact support for details.

## Responsible AI

Predictions offer capabilities to create better customer experiences, improve business capabilities, and revenue streams. We strongly recommend you balance the value of your prediction against the impact it has and biases that may be introduced in an ethical manner. Learn more about how Microsoft is [addressing Responsible AI](https://www.microsoft.com/ai/responsible-ai?activetab=pivot1%3aprimaryr6). You can also learn about [techniques and processes for responsible machine learning](/azure/machine-learning/concept-responsible-ml) specific to Azure Machine Learning.