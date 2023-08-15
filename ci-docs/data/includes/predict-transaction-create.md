1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Customer churn model** tile.

1. Select **Transaction** for the type of churn and then **Get started**.

1. **Name this model** and the **Output table name** to distinguish them from other models or tables.

1. Select **Next**.

### Define customer churn

Select **Save draft** at any time to save the prediction as a draft. The draft prediction displays in the **My predictions** tab.

1. Set the **Prediction window**. For example, predict the risk of churn for your customers over the next 90 days to align to your marketing retention efforts. Predicting churn risk for a longer or shorter period of time can make it more difficult to address the factors in your churn risk profile, but it depends on your specific business requirements.

1. Enter the number of days to define churn in the **Churn definition** field. For example, if a customer hasn't made a purchase in the last 30 days, they might be considered as churned for your business.

1. Select **Next**.

### Add purchase history

1. Select **Add data** for **Customer transaction history**.

1. Select the semantic activity type, **SalesOrder** or **SalesOrderLine**, that contains the transaction history information. If the activity has not been set up, select **here** and create it.

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or table you'd like the calculation to focus on. If semantic mapping did not occur, select **Edit** and map your data.

   :::image type="content" source="../media/transaction-churn-select-activity.PNG" alt-text="Side pane showing choosing specific activities under the semantic type.":::

1. Select **Next** and review the attributes required for this model.

1. Select **Save**.

1. Add more activities or select **Next**.