---
author: radsay01
ms.author: sstabbert
ms.reviewer: mharts
ms.date: 08/16/2023
ms.topic: include
ms.service: customer-insights
---

## Manage a workflow

1. Go to **Insights** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipsis (**&vellip;**) next to a model to view the actions you can take.

   - **Edit** a workflow to change the model configuration or the connection.
   - **Refresh** a workflow on demand. The workflow also runs automatically with every [scheduled refresh](../schedule-refresh.md).
   - **Delete** a workflow. The table that was used to create the workflow isn't deleted.

## View the results

Results from a workflow are stored in the **Output table name** you defined. View it from the [**Data** > **Tables** > **Output**](../tables.md) page or with [API access](../apis.md).

### API Access

To get data from a custom model table, use the following OData query:

`https://api.ci.ai.dynamics.com/v1/instances/<your instance id>/data/<custom model output table name>%3Ffilter%3DCustomerId%20eq%20'<guid value>'`

1. Replace `<your instance id>` with the ID of your Customer Insights environment, as shown in your browser's address bar.

1. Replace `<custom model output table>` with the table name you provided during the **Model name** step.

1. Replace `<guid value>` with the Customer ID of the customer you want to see, as shown in the `CustomerID` field on the [customer profiles](../customer-profiles.md) page.
