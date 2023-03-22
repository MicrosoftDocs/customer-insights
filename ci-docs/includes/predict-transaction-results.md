- **Training model performance**: Grades A, B, or C indicate the performance of the prediction and can help you make the decision to use the results stored in the output table.

  Grades are determined based on the following rules:
  - **A** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is greater than the baseline rate by at least 10%.
  - **B** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is up to 10% greater than the baseline.
  - **C** when the model accurately predicted less than 50% of the total predictions, or when the percentage of accurate predictions for customers who churned is less than the baseline.
  - **Baseline** takes the prediction time window input for the model (for example, one year), and creates different fractions of time by dividing it by 2 until it reaches one month or less. It uses these fractions to create a business rule for customers who have not purchased in this time frame. These customers are considered as churned. The time-based business rule with the highest ability to predict who is likely to churn is chosen as the baseline model.

- **Likelihood to churn (number of customers)**: Groups of customers based on their predicted risk of churn. Optionally, [create segments of customers](../prediction-based-segment.md) with high churn risk. Such segments help to understand where your cutoff should be for segment membership.

- **Most influential factors**: There are many factors that are taken into account when creating your prediction. Each of the factors has its importance calculated for the aggregated predictions a model creates. Use these factors to help validate your prediction results. Or use this information later to [create segments](../prediction-based-segment.md) that could help influence churn risk for customers.