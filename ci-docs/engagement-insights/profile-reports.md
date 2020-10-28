---
title: Out-of-the box profile reports 
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

# Profile out-of-the-box reports (public preview)

Public preview of Dynamics 365 Customer Insights engagement insights capability has the ability to view audience insights’ unified profile composition. The report includes the number of profiles you have and how they look when grouped by gender, age, and country of origin. 

## Prequisities

Public preview includes self-service enablement of the feature. Only a Microsoft Azure Data Lake Store owned by the customer can be the source of an audience insights profile. 

If you're using a trial version of audience insights capability or an audience insights managed lake, please contact pirequest@microsoft.com for assistance.  

## Enabling the customer profile report

An environment admin must a create a new audience insights connection.  

 :::image type="content" source="media/new-audience-insights.png" alt-text="Real-time usage report":::


As a part of the connection, you will need to specify an Azure Data Lake Store storage account, audience insights environment id and shared access key for EI to access profiles managed by audience insights. 

 :::image type="content" source="media/ai-data-connection.png" alt-text="Real-time usage report":::

 
In the second step of the wizard, optionally grant access to other people in organization (the administrator setting the connection will get access to the profile report automatically). 

 :::image type="content" source="media/manage-access.png" alt-text="Real-time usage report":::

 At the last screen – please review the entered data and click “Done”. This will kick off the process of loading audience insights profiles into engagement insights. Please note that it may take up to 2 hours depending on how many profiles your organization has. 

 :::image type="content" source="media/customer-profiles.png" alt-text="Real-time usage report":::
