---
title: Data and security roles in Dataverse
description: Data and security roles in Dataverse let you separate data using business units and apply the Dataverse security model in Customer Insights - Data.
ms.date: 10/12/2026
ms.reviewer: v-wendysmith
ms.topic: concept-article
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Data and security roles in Dataverse

Dynamics 365 Customer Insights - Data uses the [security model of Microsoft Dataverse](/power-platform/admin/wp-security-cds).

## Dataverse security roles

To access any data from Customer Insights - Data in Dataverse, a user needs to have the *Customer Insights Data Read Access* and *Customer Insights Data Configuration Viewer* security roles in Dataverse. You can't modify these roles. If different access is needed, such as access to all profiles regardless of business unit, create a custom security role and assign it.

[Learn more about Dataverse security roles.](/power-platform/admin/database-security)

## Next steps

- [Business unit support and role-based access control](business-units-data-separation.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
