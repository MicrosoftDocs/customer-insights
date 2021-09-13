---
title: "Important terms and concepts for the consent management capability"
description: "Learn about commonly used terms and concepts in the consent management capability of Customer Insights."
ms.date: 09/30/2021
ms.service: customer-insights
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Terms and concepts

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## Subscription consent

Subscription consent is a type of consent that a person can provide. It usually indicates the interest of a person to get contacted for the reason they subscribed for. For example, a newsletter which informs about updates for a product the person owns.

## Purpose consent

Purpose consent is a type of consent that a person can provide. It indicates the purpose of how data can be used and processed. For example, a person can express consent to a website cookie policy which uses the cookie for targeted advertising. 

## Consent entity

A data table which results from importing consent data to the consent management capability in Dynamics 365 Customer Insights. It contains contact information about the person that gave consent, the type of consent, and more. For more information, see [Data requirements for consent data](import-consent-data.md#data-requirements-for-consent-data).

## Standard actions

As part of the [data mapping step for consent data](map-consent-data.md), admins can define rules that apply to a type of consent. They can choose to include or exclude consent data according to a business logic. These mappings are then used in other applications to apply consent rules in business processes. For example, a mapping can exclude all contacts have set their contact preferences to not receive any information from all segments in audience insights that are used for sending newsletters.

