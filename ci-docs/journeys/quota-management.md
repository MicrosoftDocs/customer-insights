---
title: Monitor your monthly quotas
description: View your remaining monthly credits for sending marketing email messages and other metered services in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/31/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Monitor your monthly quotas

Dynamics 365 Customer Insights - Journeys is a subscription service that is billed monthly and sets organization-level quotas for the maximum number of interacted people records and monthly outbound interactions that you can send. Other quotas may also apply. You can always upgrade your subscription if you need higher quotas.

The **Quota limits** page shows the total quota levels you have purchased and how much of each quota your organization has already used. To see how much of each quota you've used, go to **Settings** > **Overview** > **Quota limits**.

> [!div class="mx-imgBorder"]
> ![Screenshot of the quota limits area.](media/quota-limits.png)

The following usages and limits are tracked on this screen:

- **Monthly interaction quota**: Shows the total number of outbound interactions (email messages, text messages, and push notifications) that you have sent in the current month.
    - The interaction quota is reset on the first day of each month. 
    - Your interaction quota is equal to ten times your interacted people quota.
- **Interacted people**: Shows the total number of *interacted people* that you can have in your database according to your current Customer Insights - Journeys subscription.
    - Entities that count toward the interacted people quota include leads, contacts, and Customer Insights - Data profiles.
    - Interacted people only include those that you engage with through interactions such as emails, text messages, or push notifications.
    - Contacts that you never engage in marketing activities won't be counted as part of this quota.
    - If you have multiple environments, the contact quota for each environment is shown so that you can tell how much is being used by each environment.
    - For more information about interacted people and how they're counted, see [How Customer Insights - Journeys is licensed](purchase.md#how-licensed) and the [Administration and setup FAQ](setup-troubleshooting.yml#licensing).
    > [!NOTE]
    > Active interacted people are counted as contact entities in the Dataverse database if they've received a marketing interaction within the last 12 months before the current date. Once a contact hasn't received an interaction in the last 12 months, it's no longer counted as an active contact.
    - Quota entitled is calculated at the tenant level. If your entitled quota looks higher than the paid SKUs you own, you probably have trials on your tenant.
    - Quota usage is shown at the environment (organization) level. Total tenant-level quota is captured in the "Other orgs in your tenant" line item.
- **Litmus email previews**: Shows the total number of Litmus email previews (inbox previews) users at your organization can still use during the current month.
    - The pre-seeded capacity is shown together with your monthly consumption.
    - The pre-seeded capacity automatically resets every month.
- **Free text messages**: For US-based instances, 1,000 free text messages per month can be sent using a toll-free number [created through Azure Communication Services](real-time-marketing-outbound-text-messaging-setup.md#add-a-sender-number-using-the-azure-communication-services-free-trial-preview-us-only).
    > [!NOTE]
    > Effective November 8, 2023, unverified toll-free numbers sending messages to US phone numbers will have their traffic blocked. Due to this new restriction, the Azure SMS Preview feature is temporarily unavailable. Numbers that were previously verified will continue to send text messages.
- **Paid text messages**: Customer Insights - Journeys offers [native integration with several providers](real-time-marketing-text-messaging-setup.md), enabling you to easily connect with mobile users.
    - You can purchase or reuse an existing SMS provider account.
    - Consumption is recorded and displayed on the quota limits page, but the allocated quota needs to be verified with the third-party provider.

The quota limits page also includes charts that show the monthly interaction usage and the annual total interacted people usage.

> [!Note]
> Quotas and other limits are different based on whether you are running a trial, preview, or subscribed version of the product.
>
> - For subscribed (paid) versions, please download the [Microsoft Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=866544).
> - For trials, see [Dynamics 365 Customer Insights - Journeys limits for trials](trial-preview-limits.md).
> 
> See also the [Readme](./known-issues.md) document for the latest news and updates.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
