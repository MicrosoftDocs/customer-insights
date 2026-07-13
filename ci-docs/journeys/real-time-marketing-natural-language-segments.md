---
title: Create segments with Query Assist copilot in Customer Insights - Journeys
description: Query Assist copilot in Dynamics 365 Customer Insights - Journeys turns plain-language segment descriptions into segment logic to help you build audience segments.
ms.date: 07/09/2026
ms.update-cycle: 180-days
ms.topic: article
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
  - sfi-image-nochange
---

# Create segments with Query Assist copilot in Customer Insights - Journeys

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=09814d5e-7d78-4bc3-81ed-978d572c80cb]

Query Assist copilot in Customer Insights - Journeys turns plain-language segment descriptions into segment logic. It helps you build segments without needing detailed knowledge of your organization's data model, and you can add the suggested query as a new group or condition anywhere in the segment builder. You can also give feedback on the results to help improve future suggestions.

Let's imagine you want to create a segment that targets people who attended one of your past events. To create a segment with Query Assist, select the **Segments** tab under **Audience**. Enter a segment name, select the target audience (**Contact** or **Lead**), and enter a description for the segment. Query Assist understands both conversational and formal language. In this example, use "People who attended the Contoso Coffee tasting event and recently opened an email." Then select **Create**.

:::image type="content" source="media/real-time-marketing-create-a-new-segment-using-copilot.png" alt-text="Screenshot of the segment creation page with a description entered for Query Assist to build a new segment." lightbox="media/real-time-marketing-create-a-new-segment-using-copilot.png":::

On the right side of the next screen, you'll see a **Query Assist** panel. Query Assist uses the description you entered when creating your segment to suggest a data structure for the segment. If the suggested segment is accurate, select **Use** to apply it to your new segment.

:::image type="content" source="media/real-time-marketing-add-a-suggested-result-using-query-assist.png" alt-text="Screenshot of the Query Assist pane showing a suggested segment query and the Use button." lightbox="media/real-time-marketing-add-a-suggested-result-using-query-assist.png":::

Once you select **Use**, Query Assist builds the relationship on the canvas. 

:::image type="content" source="media/real-time-marketing-provide-additional-details-using-query-assist.png" alt-text="Screenshot of the segment canvas with additional relationship details added by Query Assist." lightbox="media/real-time-marketing-provide-additional-details-using-query-assist.png":::

You can provide feedback on the suggested query by selecting the thumbs up or thumbs down button next to the result in the **Query Assist** pane.

Add more details to your segment by entering additional searches in the Query Assist pane. Select **See more examples** for more suggestions to help you get started.

When you run another search and select **Use**, Query Assist adds the result as a new group at the bottom of the existing canvas. 

:::image type="content" source="media/real-time-marketing-use-canvas-built-by-copilot.png" alt-text="Screenshot of the segment canvas with attributes added after applying a Query Assist result." lightbox="media/real-time-marketing-use-canvas-built-by-copilot.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
