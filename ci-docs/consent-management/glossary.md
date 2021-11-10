---
title: "Consent management terms and concepts"
description: "Learn about the commonly used terms and concepts in the consent management capability of Dynamics 365 Customer Insights."
ms.date: 09/30/2021
ms.service: customer-insights
ms.subservice: consent-management
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Terms and concepts

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## Subscription consent

Subscription consent is one of the two types of consent that a person can provide. It usually indicates the interest that person has in getting contacted for the reason they subscribed. For example, someone can consent to receive a newsletter that informs them about updates to a product they own.

## Purpose consent

Purpose consent is the second type of consent that a person can provide. It indicates the purpose of how data can be used and processed. For example, a person can consent to a website cookie policy that uses the cookie for targeted advertising. 

## Consent entity

A consent entity is a data table that results from importing consent data to the consent management capability in Dynamics 365 Customer Insights. It contains contact information about the person who gave consent, the type of consent, and more. For more information, go to [Data requirements for consent data](import-consent-data.md#data-requirements-for-consent-data).

## Standard actions

As part of the [data mapping step for setting consent data rules](set-consent-rules.md), admins define rules that apply to a type of consent. They can choose to include or exclude consent data according to a business logic. These are then used in other applications to apply consent rules to business processes. For example, a rule can be set to exclude all contacts that have set their preferences to not receive any information. These contacts are then removed from all segments in audience insights that are used for sending newsletters.

