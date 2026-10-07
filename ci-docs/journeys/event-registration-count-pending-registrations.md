---
title: Manage your event registrations
description: Manage event registrations with accurate capacity and pending ticket counts. Review failed tickets and retry processing to help attendees complete registration.
ms.date: 10/07/2026
ms.topic: how-to
author: udaykirang
ms.author: udag
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:01/23/2025
---

# Manage your event registrations

Keep your event registrations running smoothly. Event registration doesn't happen in a single step. Depending on your event setup, a registration might involve validating registration details, populating custom registration fields, processing payments, and allocating passes. To ensure an attendee spot is reserved while you complete these steps, the system creates a temporary registration ticket as soon as someone registers through a form or the Event API.  
You can now manage your event registrations with greater confidence and control. Get an accurate view of event capacity with registration counts and pending registration metrics. Stay on top of your event registrations with clear visibility of confirmed registrations, track registrations that are still being processed, and quickly identify registrations that require attention. This information helps you identify issues early and ensure attendees successfully complete their registration journey.

## Event registration count and the Registration tab

The **Registration count** field only reflects successfully created registrations, so you get an accurate view of event capacity at a glance. You can also see the pending registration count, which includes the number of registration tickets that aren't finalized and require your attention.

:::image type="content" source="media/event-registration-capacity.png" alt-text="Screenshot of Dynamics 365 event General tab showing registration count 150 and pending registrations 5.":::

You can check the list of successfully registered attendees in the **Registration and attendance** tab.

:::image type="content" source="media/event-registration-count-pending-registrations/event-registration-attendance-table.png" alt-text="Screenshot of the Registration and attendance tab listing six registered event attendees and their status.":::

| **Status description** | **What it indicates**                           |
|------------------------|-------------------------------------------------|
| Registered             | Registration is finalized and confirmed         |
| Waitlisted             | Registration is pending due to capacity limits. |
| Cancelled              | Registration was cancelled                      |
| Checked-in             | The attendee joined the event                   |

In-progress, failed, or incomplete ticket-based submissions are excluded&mdash; they're tracked separately as **Pending Registrations**.

## Pending registration metric and the Pending registration tab

The **pending registration metric** shows how many registration tickets are still processing or not yet fully converted into confirmed registrations.

:::image type="content" source="media/event-registration-count-pending-registrations/registrations-tab.png" alt-text="Screenshot of the Pending Registrations tab showing six registration tickets and Retry all and Refresh actions.":::

The **pending registration** tab lists every pending and inactive registration with the information you need to review and act on it. Go to **Related** > **pending registration**.

| **Column** | **Description** |
|----|----|
| Created On | The date and time the registration ticket was created. |
| Event Registration | The unique identifier for the registration ticket. |
| Full Name | The registrant’s name, as submitted. |
| Email | The registrant’s email address, as submitted. |
| Counts as pending | Whether the ticket counts toward pending registration. |
| Processing Status | The specific processing state of the ticket. |
| Failure Description | Details about what went wrong when processing didn't complete. |
| Registration Data | The data the registrant submitted — useful for reviewing before a retry. |

## Ticket status and pending registration counts

### Counts toward pending registration 

This ticket doesn't yet have an associated confirmed event registration. It counts toward pending registrations.

| **Status description** | **What it indicates** | **Counts as pending** |
|---|---|---|
| In Progress (validation) | The submission is being validated before the registration is created. | Yes, |
| Payment Pending | The registration is waiting for payment to be completed or confirmed. | Yes |
| Payment Passed | Payment succeeded; the registration is completing its remaining steps. | Yes |
| Failed | Processing stopped due to an error. Review the Failure Description for details. | Yes (except when registration was created but later processing fails, such as custom unmapped fields) |

### Do not count toward pending registration

The ticket was processed, but one or more steps failed. If a registration was created, it counts toward event capacity.

| **Status description** | **What it indicates** | **Counts as pending** |
|----|----|----|
| Registration Created | The registration was created, but one or more custom registration fields couldn't be populated. | No |
| Payment Failed | The payment step wasn't completed, so the registration couldn't be finalized. | No |

## Manage your tickets

Keep your event registrations under control and ensure accurate capacity management by managing your tickets. Refresh the grid to view the latest status or select one or more tickets to perform the following actions.

| **Action** | **What it does** |
|----|----|
| Refresh | Updates the grid to show the latest ticket states. |
| Edit | Open the ticket so you can review or adjust its submitted values before retrying. |
| Retry | Re-triggers registration processing for a failed or stuck ticket. |
| Delete Ticket | Removes the ticket. Deleting a ticket releases any capacity reservation associated with it. |

> [!NOTE]
> For a paid event to be reprocessed successfully, the corresponding event purchase record must be in a consistent state, with **Processed** set to false and **Paid** set to true.
>
> :::image type="content" source="media/event-registration-count-pending-registrations/registrations-grid.png" alt-text="Screenshot of Pending registrations grid showing one failed inactive ticket and Retry all and Refresh commands.":::
