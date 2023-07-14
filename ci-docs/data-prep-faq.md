---
title: Data prep report FAQ
description: "Review frequently asked questions about the data preparation report in Customer Insights."
ms.date: 07/14/2023
ms.reviewer: v-wendysmith
ms.topic: faq
author: radsay01
ms.author: rsayyaparaju 
ms.custom: bap-template
---

# Data prep report FAQ

[!INCLUDE[public-preview-banner](includes/public-preview-banner.md)]

## Who can access the data preparation report?

There are no access restrictions for the data preparation report itself, anyone can view it. The ability to turn off the data preparation experience is restricted to Admin only.

## Where can the data preparation report be accessed?

The data preparation report can be accessed from the Customer Insights **Home** page, the **Data sources** page, and the **Predictions** page.

## Why can’t I see the data preparation report?

If you don’t see the data preparation report, it has likely not been generated because you have not met the prerequisites. Ensure that you have completed ingestion and unification, mapped activities and relationships, and the data preparation experience is toggled to “on” in the  **Settings** page.

## Why isn’t the data preparation report refreshing?

The data preparation report refresh is only triggered when unification is completed. If you have made fixes to your ingested data but have not completed unification again, the report doesn’t refresh.

## How do I address the issues and corresponding recommendations for remediation in the data preparation report?

In most cases, the issues and recommendations surfaced in the data preparation report must be addressed by performing fixes on the source data outside of Customer Insights, using data clean up tools such as Power Query. The new and improved data must then be re-ingested, and unification must be completed again for the data quality to improve.

[!INCLUDE [footer-include](includes/footer-banner.md)]
