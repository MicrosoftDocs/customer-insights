---
title: Out-of-the box customer profile report
description: How to create unified profile reports grouped by gender, age, and country of origin.
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 10/27/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Customer profile report

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Dynamics 365 Customer Insights engagement insights capability has the ability to view audience insights’ unified profile composition. The report includes the number of profiles you have and how they look when grouped by gender, age, and country of origin. 

## Prequisities

The audience insights environment must store data in a customer-managed Azure Data Lake Storage account.

If you're using a trial version of audience insights capability or an environment in an audience insights managed data lake, please [contact us](https://go.microsoft.com/fwlink/?linkid=2145734) for assistance.  

## Enable the customer profile report

1. An environment admin must a [create a connection to audience insights](configure-connections.md).  

1. After specifying the connection details for th storage account, grant access to other people in the organization. The environment admin setting up the connection automatically has access to the report. 

At the last screen – please review the entered data and click “Done”. This will kick off the process of loading audience insights profiles into engagement insights. Please note that it may take up to 2 hours depending on how many profiles your organization has. 
