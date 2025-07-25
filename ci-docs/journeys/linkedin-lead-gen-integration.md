---
title: LinkedIn Lead Gen integration in outbound marketing
description: How to use the connector to LinkedIn Lead Gen Forms, which imports leads from LinkedIn to the outbound marketing area of Dynamics 365 Customer Insights - Journeys.
ms.date: 12/09/2024
ms.update-cycle: 1095-days
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing, evergreen
---

# LinkedIn Lead Gen integration in outbound marketing

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

> [!WARNING]
> Social posting and LinkedIn lead generation capabilities have been removed from Customer Insights - Journeys.

 Dynamics 365 Customer Insights - Journeys includes a connector for LinkedIn Lead Gen. Use this feature to see how people are interacting with your marketing initiatives on LinkedIn and to bring leads and lead information generated by using the [LinkedIn Lead Gen](https://business.linkedin.com/marketing-solutions/native-advertising/lead-gen-ads) tools into Dynamics 365.

[!INCLUDE [cc-linkedin-disclaimer](./includes/cc-linkedin-disclaimer.md)]

## Enable lead sync from LinkedIn to Customer Insights - Journeys

To enable leads to be synced from LinkedIn to Dynamics 365:

- A system admin must [assign security roles to users and set up the matching strategy](linkedin-configuration.md) for new leads from LinkedIn. In Dynamics 365, this user must have the **LinkedIn Lead Gen Forms Connector Administrator** security role.

- At least one LinkedIn member with access to LinkedIn Campaign Manager must [Authorize Dynamics 365 to sync data from LinkedIn Campaign Manager](#authorize-dynamics-365-to-sync-data-from-linkedin-campaign-manager), as described in the following section. In Dynamics 365, this user requires at least a **LinkedIn Lead Gen Forms Connector Salesperson** security role.

For more information about assigning security roles to users, see [Create users and assign security roles](/power-platform/admin/create-users-assign-online-security-roles)

<a name="authorize-sync"></a>

### Authorize Dynamics 365 to sync data from LinkedIn Campaign Manager

To use this feature, you must authorize Customer Insights - Journeys to connect to LinkedIn using an existing LinkedIn account that has access to [LinkedIn Campaign Manager](https://www.linkedin.com/help/lms/answer/56969). To do this: 

1. Go to **Outbound marketing** > **LinkedIn Lead Gen** > **User Profiles**. A list of existing profiles opens (if any).

1. Select **Authorize** on the command bar.

1. A browser pop-up window opens with a LinkedIn sign-in form. (If your browser is set to block pop-up windows, then you must configure it to allow pop-ups from your Customer Insights - Journeys domain then select the **Authorize** button again.)  Enter the credentials for your LinkedIn profile and then select **Sign In**. (If you are already signed into LinkedIn on this browser, then you might skip this step.)

1. A LinkedIn permissions dialog opens, providing details about the connection you are setting up. Read the text and, provided you agree with the terms, select **Allow** to continue. (If you previously accepted these conditions for your LinkedIn account, then you might skip this step.)

1. A Dynamics 365 authorization dialog opens, providing additional privacy information. Read the text and, provided you agree with the terms, select **Yes** to continue.

1. On success, the system creates a new LinkedIn user profile and syncs it with LinkedIn. Your new profile opens immediately after this, so you should now see details from your LinkedIn account, including associated accounts, campaigns, and Lead Gen forms. This new profile is also now listed on the **User Profiles** page, where you can select it to return to these details at any time.

Usually it's not required, but you can trigger an optional, on-demand sync of LinkedIn form submissions after authorizing a profile by selecting **Reset synchronization**.

## Analyze leads and lead performance

When a new lead is synced from LinkedIn, Dynamics 365 can either update an existing lead record if the person is already known, or create a new lead if it's the first contact with this person. New LinkedIn leads appear as **LinkedIn Form Submissions** in Dynamics 365. The information in LinkedIn form submissions consists of the answers given by LinkedIn members when they submitted the forms.

When a LinkedIn lead matches a lead record in Dynamics 365, the lead record is updated with additional information. In addition to the updates of individual lead records, charts on dashboards can represent the performance of a marketing campaign on LinkedIn.

### See the details of a lead

To see the details of a lead record in Customer Insights - Journeys, go to **Outbound marketing** > **Lead management** > **Leads**, and then select the lead record from the list. If the lead was created by Dynamics 365 Connector for LinkedIn Lead Gen Forms, the lead source is **LinkedIn Sponsored Content**. If an existing lead record was updated, Dynamics 365 updates the lead field values by using the information submitted by the lead on LinkedIn. More information: [Create or edit a lead (Sales and Sales Hub)](/dynamics365/sales-enterprise/create-edit-lead-sales)

To see the information collected by LinkedIn Lead Gen for any lead, regardless of how it was created, open the lead and go to its **LinkedIn Lead Info** tab.

### Review the aggregated lead performance

Work with a dashboard containing charts about the source of new leads or create new dashboards by using the charts that matter the most to get your reporting completed.

When you create your own dashboard, consider adding a chart for the record type **LinkedIn Form Submissions** to see how your campaigns perform compared to each other. Or, you can create a **Leads by Source** chart for the lead record. 

### Analyze individual LinkedIn Lead Gen forms and submissions

To see all form submissions in Customer Insights - Journeys, go to **Outbound marketing** > **LinkedIn Lead Gen** > **Form Submissions**. You can drill down to individual submissions to see the details of the lead and the information provided by the LinkedIn members when they answered the underlying LinkedIn Lead Gen form. LinkedIn Lead Gen forms refer to the ad campaigns on LinkedIn that generate leads. Every campaign creates a new Lead Gen form, and answers to the campaigns are captured as LinkedIn form submissions.

## See the sync status for LinkedIn data 

Go to **Outbound marketing** > **LinkedIn Lead Gen** > **Sync Status**, to find an aggregated overview about the data that was pulled from all LinkedIn user profiles to Customer Insights - Journeys. At a glance, you can see when the most recent synchronization took place and find out how many leads were created or updated.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
