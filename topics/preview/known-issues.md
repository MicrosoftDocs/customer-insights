---
title: Known issues 
author: ruthaisabokhae
description: Learn about issues you may experience during private preview and how to work around them
ms.author: ruthai
ms.date: 08/13/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Known issues

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

As we continue to work on Dynamics 365 Product Insights private preview and refine the experience, we've become aware of some outstanding issues for you to bear in mind. These issues are summarized in the following table.

|  | Issue and impact | Workaround | 
|------------------|------------------------|------------------------|
| 1 | Product Insights is working on changing a schema of events by the end of August 2020. | After the new schema is rolled out, you'll need to create a new project, get new code (copied from the snippet), and update it on your site. |
| 2 | The first project you create after you sign in may take up to two minutes to create, and it might fail. | Retry a few times, and if takes longer, please contact us at [pirequest@microsoft.com](mailto:pirequest@microsoft.com). |
| 3 | You might experience errors in one tile or real time usage when data hasn't been sent for some time. | Instrument your website, and send data. After you start sending data again, you should no longer see this error. | 
| 4 | During your quickstart run (after you've signed in as a new user for the first time, accepted terms, and created your project), the code snippet might not contain the ingestion key. | Give it some time and try again later. |
| 5 | We're renaming **signals** to **events**, and **derived signals** to **refined events**, so you might see may still see all four references in the product. | Please consider these terms as equivalent while we work to complete our updates. |
