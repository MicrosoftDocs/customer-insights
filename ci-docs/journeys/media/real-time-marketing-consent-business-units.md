---
title: Consent management in environments that have more than one business unit
description: Learn how consent is managed across business units in the platform
ms.date: 02/24/2024
ms.topic: reference
author: anubhav-t
ms.author: anubhav-t
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Consent management with business units  

> [!IMPORTANT]
> Starting December 2023 release, environments that have multiple business units but do not use [business unit scoping feature](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys) within the product will experience improved handling of consent across business units. This document covers the various scenarios that customers using business units in dataverse may encounter.

## Key scenario

Customers that have multiple business units but do not use [business unit scoping feature](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys) expect consent management to work across business units as the journeys and segments created in such environments can target audience across business units.  
Let's take a look at an end to end flow, from consent collection to journey send to better understand how the system handles consent across business units.  
We will also cover the system behavior for the case where business unit scoping feature is turned on.

## Consent record creation

Consent record can be created by different processes - a form that captures consent, a system user runs load consent or creates a consent record manually. Irrespective of the origin of the consent record it always gets created under the ownership of the user that owns the Purpose for which the consent was captured. The owning business unit of the consent record is set to the business unit of the owner.  
This behavior remains unchanged even if business unit scoping feature is enabled.

## Load consent

When business unit scoping is turned on and a user executes load consent, then load consent will only consider contacts/leads from the business unit of the user (or the business unit selected in the load consent screen, in case modernized business units are also turned on). Any other contact/lead will be ignored and the consent records for them will not be created.  
When business unit scoping is off, load consent does not apply any filter on the records that it creates consent records for. It can create consent records based on contacts/leads in any business unit.

## Selecting compliance elements in a form, email, SMS or custom message  

When business unit scoping is turned on, the user creating a form, email, SMS or custom message can only select compliance profiles that are in the same business unit as that of the artefact being created.  
When business unit scoping is turned off, the user can select any compliance profile, across any business unit, that they have access to.  
Whether business unit scoping is on or off, any purpose or topic that the user has access to can be selected, irrespective of the business unit it belongs to.

## Journey/Segment execution  

When business unit scoping is turned on, journeys and segments only process audience members from the same business unit as the journey/segment.  

## Consent enforcement and lookup for prefilling unsubscribe experiences  

When a journey is executed in an environment where business unit scoping is turned on, the consent checks are performed against consent records found in the business unit of the purpose first. If no corresponding consent record is found then the system falls back to consent records in the business unit of the compliance profile. If no record is found there too, then the system deems the consent as unknown.  
When business unit scoping is turned off, in addition to the fallbacks described above, the system performs an additional fallback to look for consent records in any business unit.  
This behavior remains consistent even when the system prefills an unsubscribe experience with consent records when an end user clicks on the unsubscribe link received in their emails.  

## Duplicate consent records  

Sometimes, the system may contain duplicate consent records - records that have the same contact point, channel, purpose/topic and business unit.  
Anytime the system finds duplicate consent records during consent checks or prefills, it will always consider the most recently modified record.  
In case where a consent record has to be updated because the end user modified their consent using the unsubscribe experience then we will update all the duplicate contact point consent records found in the system to reflect the latest consent.  

## Important details for compliance profiles, purposes and topics  

1. A newly created compliance profile will be owned by the user creating it and would be owned by that user’s business unit (or the business unit they select if modernized business units feature is enabled).
1. Preference center will be created as owned by the owner of the compliance profile and the business unit of that compliance profile.
1. Newly created purposes are created as owned by the compliance profile’s owning user, and assigned the same business unit of the compliance profile.
1. There are no restrictions on adding existing purposes from a different business unit into a compliance profile.
1. Newly created topics are created as owned by their purpose’s owning user, and assigned the business unit of their parent purpose.  

### See also

[Business unit scoping in Customer Insights - Journeys](real-time-marketing-business-units.md)  