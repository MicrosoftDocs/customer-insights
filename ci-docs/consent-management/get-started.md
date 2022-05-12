---
title: "Quickstart guide to consent management"
description: "Follow these four steps to quickly set up consent management, import consent data, and configure consent data rules in Dynamics 365 Customer Insights."
ms.date: 04/28/2022

ms.subservice: consent-management
ms.topic: how-to
author: anubhav-t
ms.author: antando
ms.reviewer: mhart
manager: shellyha
ms.custom: intro-internal
searchScope: 
  - ci-system-consent
  - customerInsights
---

# Get started with consent management

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

The consent management capability of Dynamics 365 Customer Insights enables organizations to manage consent data.

## Step 1: Set up consent management

You have to be an [administrator in Customer Insights](../permissions.md) to work with the consent management capability.

Select **Go to Consent Center** from the **Home** page of Customer Insights. It might take a moment to get the Consent Center ready if it's the first time you visit. Review the terms of service before you continue. You'll start on the home page of the Consent Center. This page gives an overview of the key features and provides links to related documentation.

:::image type="content" source="media/consent-center-cta.png" alt-text="Launch the Consent Center from the Customer Insights home page.":::

## Step 2: Import consent data

In the Consent Center, [import the consent data](import-consent-data.md) your organization collected through a broad set of available connectors.

## Step 3: Configure consent data rules and define default rules

After successfully importing consent data, [configure consent data rules](set-consent-rules.md) and define rules to apply by default.

## Step 4: Apply consent rules to segments in Customer Insights

The rules you created automatically sync with Customer Insights. [Activate default consent rules](../activate-consent.md) for segments in Customer Insights. You can now [export segments](../export-destinations.md) in Customer Insights with applied consent data rules.

## Step 5: Review consent metrics on the home page

The imported consent data and related rules are visualized on the **Home** page of the Consent Center. Charts inform you about the recent data imports and rules.

- **Communication preferences breakdown** helps you analyze your customers' consent across the different communication channels like email and text message to help you quickly identify the channel that has the best reach. It shows the total number of data subject identifiers like emails and phone numbers that have provided consent and the data subject identifiers that haven't provided consent for each communication channel.
- **Consent rules breakdown** gives you a quick summary view of the total number of data subject identifiers that have provided consent and the data subject identifiers that haven't provided consent to help you quickly identify the number of contactable customers in your customer base.
- **Data use purpose breakdown** helps you quickly visualize the top data use purposes for which your customer base has provided consent and breaks it down to highlight the total number of data subject identifiers that have provided consent and the data subject identifiers that haven't provided consent.
- **Subscription breakdown** helps you quickly visualize the top subscriptions for which your customer base has provided consent and breaks it down to highlight the total number of data subject identifiers that have provided consent and the data subject identifiers that haven't provided consent. 

The home page also provides a set of helpful links that point to relevant articles in the documentation.
