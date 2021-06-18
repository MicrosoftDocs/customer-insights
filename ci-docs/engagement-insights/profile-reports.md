---
title: Enable out-of-box profile reports
description: How to create out-of-box profile reports grouped by gender, age, and county or region of origin.
author: darrinw-docs
ms.reviewer: mhart
ms.author: darrinw
ms.date: 05/03/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Out-of-box profile reports

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A report is a collection of data visualization to help you understand how users behave. By connecting to Customer Insights audience insights, engagement insights can show a report with information about unified customer profiles. This report includes the number of profiles you have, grouped by gender, age, and geographical location.

## Prerequisites

The audience insights environment must store data in a customer-managed Azure Data Lake Storage account.

If you're using a trial version of audience insights capability or an environment in a Customer Insights managed data lake, [contact us](https://go.microsoft.com/fwlink/?linkid=2145734) for assistance.  


## Enable the customer profile report

An environment admin must [create a connection to audience insights](configure-connections.md).

After specifying the connection details, the admin can grant access to other people in the organization to see the report. The environment admin setting up the connection automatically has access to the report. 

After completing the connection, the **Profiles** feature will be available in the left navigation pane. 

- Go to **Discover** > **Profiles** to see the report.

The **Profiles** report contains visualizations about the gender, age, and geographical location of the connected customer profiles.

:::image type="content" source="media/customer-profiles.png" alt-text="Customer profile report":::

[!INCLUDE[footer-include](../includes/footer-banner.md)]