---
title: "Get started with the consent management capability"
description: "Quickstart guide to configure and use consent data in Customer Insights."
ms.date: 09/30/2021
ms.service: customer-insights
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
ms.custom: intro-internal
---

# Get started with consent management

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

The consent management capability of Dynamics 365 Customer Insights enables organizations to manage how they use the data they gathered about their customers.

## Step 1: Set up consent management

You have to be an [administrator in audience insights](../audience-insights/permissions.md) to work with the consent management capability.

Select **Go to Consent Center** from the **Home** page of audience insights. It might take a moment to provision the consent center if it's the first time you visit. 

:::image type="content" source="media/consent-center-cta.png" alt-text="Lunch the Consent Center from th audience insights home page.":::

## Step 2: Import consent data

In Consent Center, [import the consent data](import-consent-data.md) your organization collected through a broad set of available connectors.

## Step 3: Configure default rules for consent data

After successfully importing consent data, [configure consent data rules](set-consent-rules.md) and set rules to apply by default.

## Step 4: Apply consent rules to segments in audience insights

The rules you created automatically sync with audience insights. [Activate default consent rules](../audience-insights/activate-consent.md) for segments in audience insights. You can now [export segments](../audience-insights/export-destinations.md) in audience insights with applied consent data rules.