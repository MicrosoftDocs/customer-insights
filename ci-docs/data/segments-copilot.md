---
title: Use natural language to create segments with Copilot for Customer Insights
description: Let Copilot in Customer Insights help you in creating segments based on data in your environment.
ms.date: 09/18/2023
ms.reviewer: mhart
ms.topic: how-to
author: 
ms.author: 
---

# Use natural language to create segments with Copilot for Customer Insights

Create segments using everyday words in Dynamics 365 Customer Insights - Data without detailed knowledge about the data schema. Improve the AI model and get more accurate answers by providing feedback about prompts and results.

## Create a segment with Copilot

Copilot provides personalized, suggested prompts based on data in your environment to help you get started. Describe the segment you want and Copilot helps you create it. For example, a simple segment: All customers that live in Seattle, Washington. You can also create segments based on existing measures: All customers that have a lifetime value of at least 500 and also purchased an item within the past 30 days.

1. In Customer Insights - Data, go to **Insights** > **Segments** and select **New** to create a segment.

1. Select the Copilot icon (:::image type="icon" source="media/copilot-icon.png" border="false":::) to open the **Copilot** pane.

1. Enter a description of your segment or choose one of the suggested prompts.

1. Select **Use** to apply the result to a rule.

:::image type="content" source="media/segment-copilot-result.png" alt-text="Screenshot of a segment rule created by Copilot in Customer Insights.":::

If the resulting segment contains multiple [relationship paths](relationships.md), it uses the shortest path by default. **Edit** the segment to change the relationship path.  

## Next steps

- RAI FAQ
- [Responsible AI FAQs for Dynamics 365 Customer Insights - Data](responsible-ai-overview.md)
- [Create and manage segments](segments.md)