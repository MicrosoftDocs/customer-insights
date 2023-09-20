---
title: Manage user compliance settings in Customer Insights - Journeys using the web API
description: Learn how to manage user compliance settings in Dynamics 365 Customer Insights - Journeys using the web API
ms.date: 10/01/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - developer
  - enduser
---

# Manage user compliance settings in Customer Insights - Journeys using the web API

[!INCLUDE[consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

You can and update Customer Insights - Journeys contact point consent records using the Web API following the same approach you would to [create any entity in a Power App](/power-apps/developer/data-platform/webapi/create-entity-web-api#basic-create). It is important to familiarize yourself with the consent and compliance concepts before building API integrations. For a comprehensive overview visit the [Manage user compliance settings in Customer Insights - Journeys](/ci-docs/journeys/real-time-marketing-compliance-settings.md) to learn more.

# Creating a contact point consent record

> [!IMPORTANT]
> There are three different contact point consent tables available. The proper one to use is `msdynmkt_contactpointconsent4`. Tables `msdynmkt_contactpointconsent2` and `msdynmkt_contactpointconsent3` are no longer in use for nearly all customers.

By default every organization will have at least one Compliance profile with at least one Commercial, Transactional, and Tracking purpose. Many customers will modify these defaults or create additional records. In addition, each Purpose can zero or more child Topics associated with it. To create a contact point consent record, you need to provide the following information:

* Contact point (`msdynmkt_contactpointvalue`): This is the email or phone number associated with the consent record
* Channel (`msdynmkt_contactpointtype`): Email, phone
* Consent status (`msdynmkt_value`): Opted-in, Opted-out, Not set
* Purpose (`msdynmkt_purposeId`): The identifier of the purpose
* Reason (`msdynmkt_logicalreason`): The reason for the update
* Source  (`msdynmkt_source`): Internal, preference center, etc.
* Status (`statuscode`): Active, inactive
* Owner (`ownerid`): Identifier of the owner of the record
