---
title: Ingestion limitations for engagement insights
description: Restrictions for events and workspaces during public preview 
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 11/13/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---
# Workspace and event quotas (public preview)

[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

Engagement insights is a highly scalable application, capable of supporting millions of events per second. During public preview, there are limits to both the ingestion volume in a workspace and the number of workspaces in an organization.

## Engagement insights limits

- Maximum event volume per workspace  = 100 events per second

- Maximum number of workspaces per organization = 100

Events over the volume threshold are dropped. This leads to data loss in the reports based on those events. You can [contact support](https://go.microsoft.com/fwlink/?linkid=2145734) to request a  volume increase before you exceed limits. We'll work with you to determine your need for a volume increase and support your request.
