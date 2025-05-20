---
title: Find similar customers with AI (preview)
description: Find similar customer segments with artificial intelligence.
ms.date: 09/01/2023
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: v-wendysmith
---

# Find similar customers with AI (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Find similar customers in your customer base using artificial intelligence. You need at least one segment created to use this feature. Expanding the criteria of an existing segment helps find customers that are similar to that segment.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=032665b3-65a7-429e-9a19-2f7871b0e7c0]

> [!NOTE]
> *Find similar customers* uses automated means to evaluate data and make predictions based on that data. Therefore it has the capability to be used as a method of profiling, as that term is defined by various privacy laws and regulations. Customers' use of this feature to process data may be subject to those laws or regulations. You are responsible for ensuring that your use of Dynamics 365 Customer Insights - Data, including predictions, complies with all applicable laws and regulations, including laws related to privacy, personal data, biometric data, data protection, and confidentiality of communications.

## Find similar customers

1. Go to **Insights** > **Segments** and select the segment you want to base your new segment on. That's your *source segment*.

1. Select **Find similar customers**.

1. Review the suggested name for your new segment and change it if necessary.

1. Optionally, add [tags](work-with-tags-columns.md#manage-tags) to the new segment.

1. Review the fields that define your new segment. These fields define the basis on which the system will try to find similar customers to your source segment. The system selects recommended fields by default. If needed, add more fields.
  Fields that can significantly reduce the model performance are automatically excluded:
  
   - Fields with the following data types: StringType, BooleanType, CharType, LongType, IntType, DoubleType, FloatType, ShortType
   - Fields with a cardinality (the number of elements in a field) of less than 2 or more than 30

1. Choose if you want to include **All customers** except the source segment or only customers in a **different segment** in your new segment.

1. By default, the system suggests including only 20% of the target audience size in your output. Edit this threshold as needed. Increasing the threshold will reduce the precision.

1. Include customers in your source segment by selecting the **Include members from source segment in addition to customers with similar attributes** checkbox.

1. Select **Run** at the bottom of the page to start a [binary classification task](#about-similarity-scores) (a method of machine learning) which analyzes the dataset.

## View the similar segment

After processing the similar segment, you'll find the new segment listed on the **Insights** > **Segments** page with the type **Expansion**.

Select **View** to see result distribution across [similarity scores](#about-similarity-scores) and similarity score values under **Segment members preview**.

:::image type="content" source="media/expanded-segment.png" alt-text="Similar customers segment.":::

## Manage a similar segment

[Work with and manage a similar segment](segments.md) as you do with other segments. For example, export the segment or build a measure.

Edit, refresh, rename, download, and delete a similar segment. Editing a similar segment reprocesses your data. The previously created segment gets updated with refreshed data.

## About similarity scores

The binary classification machine learning model assigns a score to customers in the similar segment. The score is based on the similarity to customers in the source segment.

- Similarity scores below 0.55 are customers the system classified as *not similar* to customers in the source segment
- Similarity scores between 0.55 – 0.7 are classified as *somewhat similar*
- Similarity scores between 0.7 – 0.85 are classified as *similar*
- Similarity scores between 0.85 – 1 are customers the system classified as *very similar*

Customers with similarity scores below 0.4 aren't included in the model output. The system doesn't consider them similar enough to the source segment.

[!INCLUDE [footer-include](includes/footer-banner.md)]
