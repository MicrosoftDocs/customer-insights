
## Manage an existing workflow

1. Go to **Insights** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipsis (&vellip;) next to a model to view available actions.

   - **Edit** a workflow to change the model configuration or the connection.
   - **Refresh** a workflow on demand. The workflow also runs automatically with every [scheduled refresh](../schedule-refresh.md).
   - **Delete** a workflow. The table used to create the workflow is not deleted.

## View the results

Results from a workflow are stored in the **Output table name** you defined. Access this data from the [**Data** > **Tables**](../tables.md) page or with [API access](../apis.md).

### API Access

For the specific OData query to get data from a custom model table, use the following format:

`https://api.ci.ai.dynamics.com/v1/instances/<your instance id>/data/<custom model output table name>%3Ffilter%3DCustomerId%20eq%20'<guid value>'`

1. Replace `<your instance id>` with the ID of your Customer Insights environment, which displays in the address bar of your browser when accessing Customer Insights.

1. Replace `<custom model output table>` with the table name you provided during the **Model name** step.

1. Replace `<guid value>` with the Customer ID of the customer you'd like to access. This ID displays on the [customer profiles](../customer-profiles.md) page in the CustomerID field.
