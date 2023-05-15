---
title: "Customer Insights data in Dataverse (preview)"
description: "Learn how to use business units in Dataverse applications to separate data."
ms.date: 05/05/2023
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: concept
author: jodahl
ms.author: jodahl
ms.custom: bap-template
---

# Customer Insights data in Dataverse (preview)

Customer Insights belongs to the Microsoft Dynamics 365 ecosystem and it uses the [security model of Microsoft Dataverse](/power-platform/admin/wp-security-cds).

## Dataverse security roles

To access any data from Customer Insights in Dataverse, a user needs to have the *Customer Insights Data Read Access* security role in Dataverse. You can't modify this role. If different access is needed, for example, access to all profiles irrespectively of business unit, create a custom security role and assign it.

[Learn more about Dataverse security roles.](/power-platform/admin/database-security)

[!INCLUDE [footer-include](includes/footer-banner.md)]
