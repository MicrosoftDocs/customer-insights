---
title: Consent management for business units
description: Learn how consent is managed across business units in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/29/2024
ms.topic: reference
author: anubhav-t
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Consent management for business units

> [!IMPORTANT]
> Starting in the December 2023 release, environments that have multiple business units but don't use [business unit scoping](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys) will experience improved handling of consent across business units. This document covers the various scenarios that customers using business units in Dataverse may encounter.

## Key scenario

Customers that have multiple business units but don't use [business unit scoping](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys) expect consent management to work across business units, as the journeys and segments created in such environments can target audience across business units. Let's take a look at an end-to-end flow, from consent collection to journey send to better understand how Customer Insights - Journeys handles consent across business units. We'll also cover the system behavior for the case where the business unit scoping feature is enabled.

## Consent record creation

Consent records can be created through various processes: a form that captures consent, a system user that runs load consent, or a system user that creates a consent record manually. Irrespective of the origin of the consent record, it's always created under the ownership of the user that owns the *purpose* for which the consent was captured.

The owning business unit of the consent record is set to the business unit of the owner. This behavior remains unchanged, even if the business unit scoping feature is enabled.

## Load consent

When business unit scoping is enabled and a user executes load consent, then load consent only considers contacts or leads from the business unit of the user (or the business unit selected in the load consent screen, in case modernized business units are also enabled). Any other contact or lead is ignored and the consent records for them won't be created.  

When business unit scoping is off, load consent doesn't apply any filter on the records that it creates consent records for. It can create consent records based on contacts or leads in any business unit.

## Selecting compliance elements in a form, email, SMS, or custom message  

When business unit scoping is enabled, the user creating a form, email, SMS, or custom message can only select compliance profiles that are in the same business unit as that of the artifact being created.  

When business unit scoping is turned off, the user can select any compliance profile, across any business unit, that they have access to.  
Whether business unit scoping is on or off, any purpose or topic that the user has access to can be selected, irrespective of the business unit it belongs to.

## Journey and segment execution  

When business unit scoping is enabled, journeys and segments only process audience members from the same business unit as the journey or segment.  

## Consent enforcement and lookup for prefilling unsubscribe experiences  

When a journey is executed in an environment where business unit scoping is enabled, the consent checks are performed against consent records found in the business unit of the purpose first. If no corresponding consent record is found, the system falls back to consent records in the business unit of the compliance profile. If no record is found there too, then the system deems the consent as unknown.

When business unit scoping is turned off, in addition to the fallbacks described above, the system performs an additional fallback to look for consent records in any business unit.

This behavior remains consistent even when the system prefills an unsubscribe experience with consent records when an end user selects the unsubscribe link received in an email.  

## Duplicate consent records  

Sometimes, the system may contain duplicate consent records: records that have the same contact point, channel, purpose or topic, and business unit.  
Anytime the system finds duplicate consent records during consent checks or prefills, it always considers the most recently modified record.  

In the case where a consent record has to be updated because the end user modified their consent using the unsubscribe experience, all the duplicate contact point consent records found in the system are updated to reflect the latest consent.  

## Important details for compliance profiles, purposes, and topics  

- A newly created compliance profile is owned by the user creating it and is owned by that user’s business unit (or the business unit they select if the modernized business units feature is enabled).
- A preference center is created as owned by the owner of the compliance profile and the business unit of that compliance profile.
- Newly created purposes are created as owned by the compliance profile’s owning user and assigned the same business unit of the compliance profile.
- There are no restrictions on adding existing purposes from a different business unit into a compliance profile.
- Newly created topics are created as owned by their purpose’s owning user and assigned the business unit of their parent purpose.  

### See also

[Business unit scoping in Customer Insights - Journeys](real-time-marketing-business-units.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]