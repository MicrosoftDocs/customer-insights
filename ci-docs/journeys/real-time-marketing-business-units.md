---
title: Business unit support in real-time journeys
description: Learn how to use business unit support in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/18/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Business unit support in real-time journeys

Business unit scoping in Customer Insights - Journeys can be enabled at an environment level by an administrator. Once this feature is enabled, all real-time journeys and segments created within the environment will be automatically scoped to the record owner’s business unit.

> [!IMPORTANT]
> If you [enable Business Unit scoping in Customer Insights - Journeys](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys), any newly created journeys and segments and only process audience members from the owning business unit of the journey/segment.
>
> Audience members that belong to any child unit of the business unit in which the journey or segment was created will not be processed.  

## Segment scopes, membership, and member lists

Business units affect Customer Insights - Journeys segments as follows:

- When [scoping is enabled](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys) for your instance, each [segment](real-time-marketing-build-segments.md) is automatically scoped to the segment owner’s business unit. In addition:
  - Business unit scoped segments only include audience members from the same business unit as the segment owner, even if the selection criteria would otherwise identify contacts from all business units.

## Journey scopes, design, processing, and content settings

Business units affect customer journeys as follows:

- When [scoping is enabled](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys) for your instance, each [journey](real-time-marketing-trigger-based-journey.md) is automatically be scoped to the journey owner’s business unit. In addition:
  - Business unit scoped journeys only process audience members that belong to the same business unit as the journey owner.
  - If the environment's business unit scoping is enabled, all journeys automatically filter the segments, emails, text messages, and push notifications that can be used in a journey to those that are in the same business unit as the journey.

> [!NOTE]
> The scoping business unit on a **Live** journey does not change even if the owner of the journey changes or if the business unit of the owner changes. If you edit a **Live** journey and publish a new version, the *new* journey version will take the current value of the business unit of the journey owner at the time of publication for scoping purposes. The previous version of the journey, however, retains the original business unit scoping.

## Message (email, text message, push notification) and template design

Business units affect messages (emails, text messages, and push notifications) and templates as follows:

- When [scoping is enabled](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys) for your instance, each message or template is automatically scoped to the email owner’s business unit.
  - A message or template can only include elements from the same business unit as that of its owner.

## Forms

Business units affect forms as follows:

- When [scoping is enabled](real-time-marketing-business-units.md#enabling-business-unit-scopes-in-customer-insights---journeys) for your instance, each [form](real-time-marketing-form-overview.md) is automatically scoped to the form owner’s business unit. In addition:
  - Business unit scoped forms, when submitted, create records in the form owner’s business unit.

## Enabling business unit scopes in Customer Insights - Journeys

> [!NOTE]
> While the business unit scoping feature can be turned on or off in outbound marketing, it behaves differently for Customer Insights - Journeys. Business unit scoping for Customer Insights - Journeys is an irreversible feature switch; once it's enabled, it can't be disabled. To enable this feature:

1. Go to **Settings** > **Other settings** > **Feature switches**.
1. Set the **Business Unit Scoping (Customer Insights - Journeys)** toggle to **On**.
1. Read the customer agreement displayed in the prompt and select on **I Agree** to turn on the feature.
1. Select **Save** in the upper right.

### See also

[Domain authentication for modernized business units](domain-authentication.md#domain-authentication-for-modernized-business-units)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
