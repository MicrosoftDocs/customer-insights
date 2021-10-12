---
title: "Respond to DSR requests under GDPR"
description: "Learn how to remove personal data from the consent management capability of Customer Insights."
ms.date: 10/30/2021
ms.service: customer-insights
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Data subject rights request under GDPR

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

The consent management capability doesn't collect user data directly. It only imports and processes consent data that is provided by users in other applications.

To remove consent data about specific users, remove it in the data sources ingested to the consent management capability. After refreshing the data source, the removed data will be deleted in the Consent Center too. Applications that use the consent entity will also delete data that was removed on the source after a [refresh](../audience-insights/system.md#refresh-policies). We recommend refreshing data sources quickly after responding to a data subject request to remove the user's data from all other processes and applications.

