---
title: Data and security roles in Dataverse (preview)
description: Use business units in Dataverse applications to separate data and leverage the Dataverse security model for Customer Insights - Data.
ms.date: 09/01/2023
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: article
author: jodahl
ms.author: jodahl
ms.custom: bap-template
---

# Data and security roles in Dataverse (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Dynamics 365 Customer Insights - Data uses the [security model of Microsoft Dataverse](/power-platform/admin/wp-security-cds).

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Dataverse security roles

To access any data from Customer Insights - Data in Dataverse, a user needs to have the *Customer Insights Data Read Access* and *Customer Insights Data Configuration Viewer* security roles in Dataverse. You can't modify these roles. If different access is needed, for example, access to all profiles irrespectively of business unit, create a custom security role and assign it.

[Learn more about Dataverse security roles.](/power-platform/admin/database-security)

## Next steps

- [Business unit support and role-based access control (preview)](business-units-data-separation.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
