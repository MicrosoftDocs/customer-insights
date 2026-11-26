---
title: Monitor your monthly quotas
description: Check monthly quotas and usage for outbound interactions, interacted people, and other services in Dynamics 365 Customer Insights - Journeys. View your limits.
ms.date: 11/13/2026
ms.topic: article
author: udag
ms.author: udag
ai-usage: ai-assisted
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Monitor your monthly quotas

Monitor your monthly quotas in Dynamics 365 Customer Insights - Journeys to see how your outbound interactions and interacted people usage compare with your purchased limits. Check your usage to determine whether you need to upgrade your subscription.  

> [!IMPORTANT]
> Starting December 2026, the *Quota limits* page displays inbound interactions from form and event-registration submissions. This reporting update doesn't change licensing entitlements.

> [!TIP]
> You see in-app notifications as your organization approaches its paid consumption quota and when it exceeds it.

The **Quota limits** page shows the total quota levels you purchased and how much of each quota your organization already used. To see how much of each quota you used, go to **Settings** > **Overview** > **Quota limits**.

:::image type="content" source="media/quota-limits.png" alt-text="Screenshot of the Quota limits page showing purchased quotas and usage.":::

This screen tracks the following usages and limits:

- **Monthly interaction quota**: Shows the total number of outbound interactions (email messages, text messages, and push notifications) that you sent in the current month.
    - The interaction quota resets on the first day of each month.
    - Your interaction quota is equal to ten times your interacted people quota.
- **Interacted people**: Shows the total number of *interacted people* that you can have in your database according to your current Customer Insights - Journeys subscription.
    - Entities that count toward the interacted people quota include leads, contacts, and Customer Insights - Data profiles.
    - Contacts that you never engage in marketing activities don't count as part of this quota.
    - For more information about interacted people and how they're counted, see [How Customer Insights - Journeys is licensed](purchase.md#how-licensed) and the [Administration and setup FAQ](setup-troubleshooting.yml#licensing).
    > [!NOTE]
    > Active interacted people are counted as contact entities in the Dataverse database if they had a marketing interaction within the last 12 months before the current date. Once a contact doesn't receive an interaction in the last 12 months, it's no longer counted as an active contact.
    - Quota entitlement is calculated at the tenant level. If your entitled quota looks higher than the paid SKUs you own, you might have trials on your tenant.
    - Quota usage is shown at the environment (organization) level. Total tenant-level quota is captured in the "Other orgs in your tenant" line item.
- **Litmus email previews**: Shows the total number of Litmus email previews (inbox previews) users at your organization can still use during the current month.
    - The pre-seeded capacity is shown together with your monthly consumption.
    - The pre-seeded capacity automatically resets every month.
- **Free text messages**: For US-based instances, you can send 1,000 free text messages per month by using a toll-free number [created through Azure Communication Services](real-time-marketing-outbound-text-messaging-setup.md#add-a-sender-number-using-the-azure-communication-services-free-trial-preview-us-only).
    > [!NOTE]
    > Effective November 8, 2023, unverified toll-free numbers sending messages to US phone numbers have their traffic blocked. Due to this new restriction, the Azure SMS Preview feature is unavailable. Numbers that were previously verified will continue to send text messages.
- **Paid text messages**: Customer Insights - Journeys offers [native integration with several providers](real-time-marketing-text-messaging-setup.md), enabling you to easily connect with mobile users.
    - You can purchase or reuse an existing SMS provider account.
    - Consumption is recorded and displayed on the quota limits page, but you need to verify the allocated quota with the third-party provider.

The quota limits page also includes charts that show the monthly interaction usage and the annual total interacted people usage.

> [!NOTE]
> Quotas and other limits are different based on whether you're running a trial, preview, or subscribed version of the product.
>
> - For subscribed (paid) versions, download the [Microsoft Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=866544).
> - For trials, see [Dynamics 365 Customer Insights - Journeys limits for trials](trial-preview-limits.md).
> 
> See also the [Readme](./known-issues.md) document for the latest news and updates.
