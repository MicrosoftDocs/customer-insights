---
title: Data preparation report FAQ
description: "Review frequently asked questions about the Data preparation report in Customer Insights."
ms.date: 04/05/2023
ms.reviewer: v-wendysmith
ms.topic: faq
author: radsay01
ms.author: rsayyaparaju 
ms.custom: bap-template
---

# Data preparation report FAQ

## Who can access the Data prep report?

There are no access restrictions for the Data prep report itself, anyone can view it. The ability to turn off the data prep experience is restricted to Admin only.

## Where can the Data prep report be accessed?

The Data prep report can be accessed from the CI Home page, the Data sources page, and the Predictions page.

## Why can’t I see the Data prep report?

If you don’t see the Data prep report, it has likely not been generated because you have not met the prerequisites. Ensure that you have completed ingestion and unification, mapped activities and relationships, and the data prep experience is toggled to “on” in Settings.

## Why isn’t the Data prep report refreshing

The Data prep report refresh is only triggered when unification is completed. If you have made fixes to your ingested data but have not completed unification again, the report doesn’t refresh. 

## How do I address the issues and corresponding recommendations for remediation in the Data prep report

In most cases, the issues and recommendations surfaced in the Data prep report must be addressed by performing fixes on the source data outside of Customer Insights, using data clean up tools such as Power Query. The new and improved data must then be re-ingested, and unification must be completed again for the data quality to improve.