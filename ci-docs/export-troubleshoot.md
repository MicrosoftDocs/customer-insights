---
title: "Segment not eligible for export"
description: "Troubleshooting segment exports in Customer Insights"
author: pkieffer
ms.author: philk
manager: shellyha
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights

ms.date: 01/05/2023
ms.topic: troubleshoot
ms.custom: bap-template
---

# Segment not eligible for export

## Symptoms

Within an environment of business accounts your exports fail with the error message:
"The following segment is not eligible for this export destination: '{name of segment}'. Please choose only segments of type ContactProfile and try again."

## Resolution

Customer Insights environments for business accounts was updated to support contact segments in addition to account segments. Due to that change, exports needing contact details only work with segments based on contacts.

1. [Create a segment based on contacts](segment-builder.md) which matches your previously used segment.

1. Once that contact segment is run, edit the respective export and select the new segment.

1. Select **Save** to save the configuration or **Save and run** to test this export right away.

[!INCLUDE [footer-include](includes/footer-banner.md)]
