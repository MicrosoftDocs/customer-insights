---
title: Permissions for out of the box user-custom roles
description: How to manage user accounts and permissions for custom roles in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/02/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Permissions for out of the box user-custom roles

Customer insights - Journeys product is evolving, so roles documented here might not be exact match to current state of product.

This page focuses into the permissions required for the out-of-the-box roles in Customer Insights - Journeys. Whether you're an administrator configuring roles or a user looking to understand the access levels, these roles will serve as a valuable reference.

## Role Event Administrator
**Role identifier**: a31a2242-bf8f-e611-80d7-00155d4b201d
| Table name | Read | Write | Create | Append | AppendTo |
| --- | --- | --- | --- | --- | --- |
| adx_entityform |Global | | | | |
| Adx_website |Global | | | | |
| Adx_websitebinding |Global | | | | |
| AppModule |Global | | | | |
| AsyncOperation |Global | | | | |
| Attribute |Global | | | | |
| AttributeMap |Global | | | | |
| BusinessUnit |Global | | | | |
| Contact |Basic |Basic |Basic |Basic |Basic |
| Customization |Global | | | | |
| Entity |Global | | | | |
| EntityKey |Global | | | | |
| EntityMap |Global | | | | |
| msdyn_PostConfig |Global | | | | |
| msdyn_tour |Global | | | | |
| msdyncrm_customerinsightsinfo |Basic | | | | |
| msdyncrm_defaultmarketingsetting |Global | | | | |
| msdyncrm_digitalassetsconfiguration |Global | | | | |
| msdyncrm_featureconfiguration |Global | | | | |
| msdyncrm_file |Global |Global |Local |Global |Global |
| msdyncrm_leadtoopportunity |Global |Global |Global |Global |Global |
| msdyncrm_marketingconfiguration |Global | | | | |
| msdyncrm_setupdomain |Global |Global |Global |Global |Global |
| msdynmkt_domain |Deep |Deep |Deep |Deep |Deep |
| msdynmkt_marketingfieldsubmission |Global | | | | |
| msdynmkt_marketingform |Global |Global |Global |Global |Global |
| msdynmkt_marketingformfield |Global | | | | |
| msdynmkt_marketingformsubmission |Global | |Global |Global | |
| msdynmkt_marketingformtemplate |Global | | | |Global |
| msdynmkt_matchingstrategy |Global |Global |Global | |Global |
| msdynmkt_matchingstrategyattribute |Global | | | | |
| msdynmkt_trackingcontext |Global | | | | |
| msdynmkt_virtualdomain |Global | | | | |
| msevtmgt_AttendeePass |Global |Global |Global |Global |Global |
| msevtmgt_authenticationsettings |Global | | | | |
| msevtmgt_bpf_9623d46752ae497989f62ac0d11dad99 |Global |Global |Global |Global |Global |
| msevtmgt_Building |Global |Global |Global |Global |Global |
| msevtmgt_CheckIn |Global |Global |Global |Global |Global |
| msevtmgt_customregistrationfield |Global |Global |Global |Global |Global |
| msevtmgt_EntityCounter |Global |Global |Global |Global |Global |
| msevtmgt_Event |Global |Global |Global |Global |Global |
| msevtmgt_eventadministration |Global |Global |Global |Global |Global |
| msevtmgt_eventcustomregistrationfield |Global |Global |Global |Global |Global |
| msevtmgt_eventmanagementconfiguration |Global | | | | |
| msevtmgt_eventpurchase |Global |Global |Global |Global |Global |
| msevtmgt_eventpurchaseattendee |Global |Global |Global |Global |Global |
| msevtmgt_eventpurchasepass |Global |Global |Global |Global |Global |
| msevtmgt_EventRegistration |Global |Global |Global |Global |Global |
| msevtmgt_EventTeamMember |Global |Global |Global |Global |Global |
| msevtmgt_eventvendor |Global |Global |Global |Global |Global |
| msevtmgt_file |Global |Global |Global |Global |Global |
| msevtmgt_Hotel |Global |Global |Global |Global |Global |
| msevtmgt_HotelRoomAllocation |Global |Global |Global |Global |Global |
| msevtmgt_HotelRoomReservation |Global |Global |Global |Global |Global |
| msevtmgt_Layout |Global |Global |Global |Global |Global |
| msevtmgt_pass |Global |Global |Global |Global |Global |
| msevtmgt_registrationresponse |Global |Global |Global |Global |Global |
| msevtmgt_Room |Global |Global |Global |Global |Global |
| msevtmgt_roomreservation |Global |Global |Global |Global |Global |
| msevtmgt_Session |Global |Global |Global |Global |Global |
| msevtmgt_SessionRegistration |Global |Global |Global |Global |Global |
| msevtmgt_SessionTrack |Global |Global |Global |Global |Global |
| msevtmgt_Speaker |Global |Global |Global |Global |Global |
| msevtmgt_speakerengagement |Global |Global |Global |Global |Global |
| msevtmgt_SponsorableArticle |Global |Global |Global |Global |Global |
| msevtmgt_Sponsorship |Global |Global |Global |Global |Global |
| msevtmgt_Venue |Global |Global |Global |Global |Global |
| msevtmgt_waitlistitem |Global |Global |Global |Global |Global |
| msevtmgt_webapplication |Global |Global |Global |Global |Global |
| msevtmgt_webinarconfiguration |Global |Global |Global |Global |Global |
| msevtmgt_webinarconsent |Global |Global |Global |Global |Global |
| msevtmgt_WebinarProvider |Global |Global | |Global |Global |
| msevtmgt_WebinarType |Global | | |Global |Global |
| msevtmgt_websiteentityconfiguration |Global |Global |Global |Global |Global |
| OptionSet |Global | | | | |
| Organization |Global | | | | |
| PluginAssembly |Global | | | | |
| PluginType |Global | | | | |
| Query |Global | | | | |
| Relationship |Global | | | | |
| Role |Global | | | | |
| SdkMessage |Global | | | | |
| SdkMessageProcessingStep |Global | | | | |
| SdkMessageProcessingStepImage |Global | | | | |
| SharePointData |Global |Global |Global | | |
| SharePointDocument |Global | | | | |
| Solution |Global | | | | |
| SystemForm |Global | | | | |
| User |Global | | | |Global |
| UserEntityUISettings |Basic |Basic |Basic | | |
| UserSettings |Global | | | | |
| WebResource |Global | | | | |
| Workflow |Global |Basic |Basic |Basic |Global |