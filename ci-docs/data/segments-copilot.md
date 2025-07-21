---
title: Create segments with Copilot for Customer Insights - Data (preview)
description: Let Copilot in Customer Insights - Data help you in creating segments based on data in your environment.
ms.date: 10/23/2024
ms.update-cycle: 180-days
ms.reviewer: mhart
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# Create segments with Copilot for Customer Insights - Data (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Create segments using everyday words in Dynamics 365 Customer Insights - Data without detailed knowledge about the data schema. Improve the AI model and get more accurate answers by providing feedback about prompts and results.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Prerequisites

- [Enable Copilot features powered by Azure OpenAI](copilot-global-consent.md) setting turned **On**. Default is **On**.
- Environment is in a [supported geography and uses a supported language](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport).

## Create a segment with Copilot

Copilot provides personalized, suggested prompts based on data in your environment to help you get started. Describe the segment you want and Copilot helps you create it. For example, a simple segment: All customers that live in Seattle, Washington. You can also create segments based on existing measures: All customers that have a lifetime value of at least 500 and also purchased an item within the past 30 days.

1. In Customer Insights - Data, go to **Insights** > **Segments** and select **New** > **Build your own** to create a segment.

1. Select the Copilot icon (:::image type="icon" source="media/copilot-icon.png" border="false":::) to open the **Copilot** pane.

1. Enter a description of your segment or choose one of the suggested prompts.

1. Select **Use** to apply the result to a rule.

   :::image type="content" source="media/segment-copilot-result.png" alt-text="Screenshot of a segment rule created by Copilot in Customer Insights - Data.":::

1. To create the segment:

   1. Select **Edit details** next to Untitled segment. Provide a name for your segment and update the suggested **Output table name** for the segment. Optionally, add a description and [tags](work-with-tags-columns.md#manage-tags) to the segment.

   1. To save the configuration, select **Save** and then **Close**. The segment is in draft mode or inactive so you can make changes to the configuration before actually creating the segment. Or, select **Run** to save and create the segment.

If the resulting segment contains multiple [relationship paths](relationships.md), it uses the shortest path by default. **Edit** the segment to change the relationship path.  

## Next steps

- [Create and manage segments](segments.md)
- [FAQ for segment creation (preview)](faqs-segment-creation.md)
- [Responsible AI FAQs for Dynamics 365 Customer Insights - Data](responsible-ai-overview.md)