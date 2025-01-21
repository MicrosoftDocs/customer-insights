---
title: Export Dynamics 365 Customer Voice survey responses to Microsoft Excel in outbound marketing
description: Learn how to map names and emails in outbound marketing to surveys with a custom Power Automate flow.
ms.date: 01/24/2022
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing
---

# Export Dynamics 365 Customer Voice survey responses to Microsoft Excel in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](../transition-overview.md)

The export to Excel feature uses Microsoft Dataverse information to join and pull the contact record information for Customer Insights - Journeys integration customers, making it available in Excel.

To export survey response data to Excel:

1. Enter the following URL into your browser, replacing the value for {surveyidentifier} with the ID of your chosen survey:

    ```https://forms.office.com/FormsPro/Pages/DesignPage.aspx?experienceType=Pro#Analysis=true&FormId={surveyidentifier}```

    > [!NOTE]
    > Do not confuse the survey identifier with the GUID. To find the survey identifier in the Dynamics 365 Customer Voice survey entity, look in the **Source survey identifier** field.
	>
    > The survey identifier will look like the following string: <br>
    ```v4j5cvGGr0GRqy180BHbR8HxyywSGiFAkJ7eG-r1E-9UODI0UzIzUFBOM1FTUENON0pQV1UzV0VTNi4u```

1. After the page loads, select the **Responses** tile.

1. To export the response data, select **Export all**.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
