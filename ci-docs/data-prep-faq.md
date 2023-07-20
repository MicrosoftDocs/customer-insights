---
title: Data prep report (preview) FAQ
description: "Review frequently asked questions about the data prep in Customer Insights."
ms.date: 07/20/2023
ms.reviewer: v-wendysmith
ms.topic: faq
author: radsay01
ms.author: rsayyaparaju 
ms.custom: bap-template
---

# Data prep report (preview) FAQ

[!INCLUDE[public-preview-banner](includes/public-preview-banner.md)]

## Who can access the data prep report?

There are no access restrictions for the data prep report itself, anyone can view it. The ability to turn off the data preparation experience is restricted to Admin only.

## Where can the data prep report be accessed?

The data prep report can be accessed from the Customer Insights **Home** page, the **Data sources** page, and the **Predictions** page.

## Why can’t I see the data prep report?

If you don’t see the data prep report, it probably hasn't been generated because you have not met the prerequisites. Ensure that you have completed ingestion and unification, mapped activities and relationships, and the data prep report consent setting is toggled to “on” in the  **Settings** page.

## Why isn’t the data prep report refreshing?

The data prep report refresh is only triggered when unification is completed. If you have made fixes to your ingested data but have not completed unification again, the report doesn’t refresh.

## How do I address the issues and corresponding recommendations for remediation in the data prep report?

In most cases, the issues and recommendations surfaced in the data prep report must be addressed by performing fixes on the source data outside of Customer Insights, using data clean up tools such as Power Query. The new and improved data must then be re-ingested, and unification must be completed again for the data quality to improve.

[!INCLUDE [footer-include](includes/footer-banner.md)]
