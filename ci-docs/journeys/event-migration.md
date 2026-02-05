---
title: Migrate registrations from Outbound event to Real-time marketing event to speed up your transition  
description: Learn how to migrate outbound marketing event registrations to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/05/2026
ms.topic: upgrade-and-migration-article
author: terezakirk
ms.author: alfergus
search.audienceType:
  - admin
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:02/06/2025
---
# Migrate registrations from Outbound event to Real-time marketing event to complete your transition  

## Introduction 

With outbound marketing reaching its end‑of‑life, **organizations still running outbound events** need a reliable way to continue collecting registrations without disruption. Existing live outbound events cannot continue receiving registrations once the module is removed. 

This migration tool enables outbound marketing customers to** move active event registrations and some selected event settings** from a live outbound event into a newly created **real‑time journeys (RTM) event**, allowing a smooth transition before deprecation. 
The context for this transition aligns with Microsoft's official guidance on migrating from outbound to real‑time journeys as described in [transition FAQ](transition-faqs.md).

## What the migration tool does 

The tool is designed to support customers during the outbound deprecation timeline by migrating active registration records from outbound to real-time marketing events. 

### Data the tool can migrate 

- Event registrations
- Session registrations
- Registration QR codes
- Custom registration fields
- Allocated attendee passes
- Basic event settings structure for sessions and passes 

### Data the tool cannot migrate 

- Waitlisted registrations (these must be handled manually)
- Additional setting fields
- Streamed events URL
- Custom attributes added by customers outside supported fields (out of scope for this migration tool) 

## How the tool works  

The migration has to be performed at **one event at a time**. 

### Step 1 — Create the RTM Draft Event 

Before running the script, create a **Draft real‑time event** with the following minimal attributes: 

- Event name
- Start date
- End date 

You _must not_ configure sessions, passes, or other settings manually — the migration tool will populate supported fields, and the rest of the fields should be edited **after** the migration is completed. 

### Step 2 — Register for the Events API 

In the Settings section under** Event management > Web Applications**, create a new web application (if you haven’t created one before). After you create and save a web application, you see a link to the Endpoint you will be using for the migration. To access your API, you must be authorized (provide the **Token** column). [Learn more](ci-docs/journeys/developer/using-rtm-events-api.md#register-for-the-events-api) 

### Step 3 — Run the Migration Script  

Call the **REST API** and run the migration using the event‑to‑event mapping: 

```
POST <endpoint URL retrieved from Web Applications>/obmMigration/start 
{ 
 "fromEventId":"<outbound-event-guid>", 
 "toEventId":"<rtm-event-guid>" 
} 
```

There are additional optional parameters you can use:  

1. If you want to end one migration script that is in progress and start a new one, you can achieve it by adding:  
```
{ 
  "fromEventId": "<outbound-event-guid> ", 
  "toEventId": "<rtm-event-guid>", 
  "stopExistingIfJobRunning": true 
}
```
Check whether the migration is done via: 
```
GET <endpoint URL retrieved from Web Applications> /obmMigration/status 
```
Processing time varies with registration volume. **Expected duration:** ~8 hours for 4,000 registrations. 

### Step 4 — Publish the RTM Event 

Once the migration completes: 

1. Open the new Real‑time event 
1. Review migrated data (registrations, sessions, passes, custom unmapped fields) 
1. Adjust any additional settings for your new event 
1. Publish the event to start receiving new registrations in RTM 

> [!IMPORTANT]
> Make sure to disable any trigger-based journeys that are triggered when the “marketing event registration created” or “session registration created” interactions are fired, this would lead to duplicate registration confirmation communication sent to the migrated attendees. 

## Limitations & Considerations 

- Only one event can be migrated at a time.
- Custom logic or custom fields may not transfer.
- Waitlists must be recreated manually in the real‑time event.
- Ensure the outbound event’s registration migration window aligns with the outbound removal timeline to avoid any disruption to your service.  

## FAQ 

**What if the migration fails?**  
You may re-execute the migration script. If the issue persists, please contact the support team, who can escalate the matter to the engineering team for further investigation of the logs. 

**What if the migration doesn’t transfer all registrations?** 
The process may have failed or encountered exceptions. For a few registrations, add them manually to the RTM event; for many, create a new draft RTM event and rerun the script. 

**What should I do if there are new OBM registrations while the script is running?**  
The OBM event should be in draft state before migrating registrations. Registrations received after the script starts will not be migrated. 

**What will happen to streamed events and the existing Teams URL?**  
The Teams URL from the original OBM event cannot be migrated to the new real-time event. If attendees have already received the initial Teams link, we recommend preparing a segment and distributing an email containing the updated Teams join link from the new RTM event. 
