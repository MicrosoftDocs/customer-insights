---
title: "Enrich customer profiles with data from Microsoft Office 365 (preview)"
description: "Use proprietary data from Microsoft Office to enrich your customer profiles with engagement data."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: jodahl
ms.author: jodahl
ms.custom: bap-template
---

# Enrich customer profiles with data from Microsoft Office 365 (preview)

[!INCLUDE [public-preview-banner](../includes/public-preview-banner.md)]



[!INCLUDE [azure-ad-to-microsoft-entra-id](../../journeys/includes/azure-ad-to-microsoft-entra-id.md)]

Use data from Microsoft Office 365 to enrich your customer account profiles with insights about engagements through Office 365 apps. The engagement data consists of email and meeting activity, which is aggregated on the account level. For example, the number of emails from a business account or the number of meetings with the account. No data about individual users are made available.

[!INCLUDE [public-preview-note](../includes/public-preview-note.md)]

## Supported countries or regions

We currently support the following regions: UK, Europe, North America.

## Prerequisites

- An active Office 365 cloud license. Content encrypted with [Microsoft Purview Customer Key](/microsoft-365/compliance/customer-key-overview) isn't supported.
- [Unified customer profiles](../customer-profiles.md) based on business accounts.
- [Administrator](../user-roles.md#admin) permissions in Customer Insights - Data.
- Consent from your Office 365 tenant administrator to use Office 365 data to provide **Insights for the Organization** within Dynamics 365 applications.

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Account Engagement** tile.

   :::image type="content" source="media/enrichment-office-tile.png" alt-text="Account engagement tile.":::

1. Review the overview and then select **Next**.

1. Enter email addresses from your organization for which Office data is going to be aggregated. Only data from the listed email addresses gets processed for relevant communication. A best practice is to use email groups, for example, *US Sales team*, which you can manage in Office 365. The number of email addresses in the groups are resolved and shown. The total number of email addresses must be at least 2 and can't exceed 2,500.

1. Review and provide your consent for [Office 365 tenant administrator consent](#office-365-tenant-administrator-consent) by selecting **I agree**.

1. Select **Next**.

1. Select the **Contact data set** and choose the profile you want to enrich. Select **Next**.

1. Map the contact email address field and select **Next**.

1. Provide a **Name** for the enrichment and the **Output table**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Close** to return to the **Enrichments** page.

### Office 365 tenant administrator consent

Consent from an Office 365 tenant administrator is required to activate the enrichment. An email is sent to the Office 365 tenant administrators when the enrichment is saved, which asks them to review and consent to allowing Dynamics 365 applications to use your enterprises’ Office 365 data to provide **Insights for the Organization**. The Office 365 tenant administrator can also consent directly in their Office 365 admin console, by selecting **Insights for the Organization**.

## Running the enrichment for the first time

When the enrichment is started for the first time, after the Office 365 tenant administrator has given consent, the data download from Office 365 begins. This process takes some time. The first enrichment run will be scheduled to happen with a delay of six hours. You can see the number of days that the data covers on the account engagement overview page after the enrichment finishes. With a large data volume, run the enrichment again after a few days. It ensures the data is complete for the entire time window, which is one year.

Depending on the size of your Office data, it may take several hours for an enrichment run to complete.

When you run an enrichment, Microsoft will process the data within the Office 365 compliance boundary to create aggregated insights, which are then added to your environment. No data at an individual level (for example, the body of any e-mail or calendar invite) becomes available to users of Customer Insights - Data.

Select **Run** to start the enrichment process.

[!INCLUDE [progress-details-pane](../includes/progress-details-pane.md)]

## View enrichment results

[!INCLUDE [enrichment-results](../includes/enrichment-results.md)] This is the *Office* table. The *Office_UserTable* contains the Microsoft Entra IDs for the email addresses that were chosen during enrichment configuration.

:::image type="content" source="media/enrichment-office-results-overview.png" alt-text="Preview of results after running the enrichment process.":::

All data is aggregated up to the account level. The system calculates an engagement score, which ranges from 0 to 100, for every account. The engagement score provides a composite measure of the account engagement across emails and meetings relative to your other accounts. The following list contains the aggregated data that the account engagement enrichment provides:

| Data                                                                              | Column name                              |
| :-------------------------------------------------------------------------------- |:---------------------------------------- |
| Engagement score                                                                  |  EngagementScore                         |
| Number of emails to account                                                       |  NoOfEmails_ToAccount                    |
| Number of emails from account                                                     |  NoOfEmails_FromAccount                  |
| Number of meetings initiated by account                                           |  NoOfMeetings_FromAccount                |
| Number of meetings initiated by your organization                                 |  NoOfMeetings_ToAccount                  |
| Number of people from your organization in meetings with account                  |  NoOfContactsInvolved_Meetings           |
| Number of people from your organization in email conversations with account       |  NoOfContactsInvolved_Emails             |
| Number of people from account in meetings with your organization                  |  NoOfAccountContactsInvolved_Meetings    |
| Number of people from account in email conversations with your organization       |  NoOfAccountContactsInvolved_Emails      |
| Engagement start date (first email or meeting in the data)                        |  EngagementStartDate                     |
| Days since last email                                                             |  DaysSinceLastEmail                      |
| Days since last meeting                                                           |  DaysSinceLastMeeting                    |
| Average duration of meetings                                                      |  AverageDuration_Of_Meetings             |
| Average duration of email replies from account                                    |  AverageDuration_Of_AccountEmailReplies  |
| Aggregation start date                                                            |  AggregationStartDate                    |
| Aggregation level (year, month, or week)                                          |  AggregationLevel                        |

## See enrichment data on the customer card

Account engagement can also be viewed on individual customer cards. Go to **Customers** and select a customer profile. In the customer card, you'll find the account's engagement score, the total number of emails, and the total number of meetings aggregated over the last year. You also find charts that show the email and meeting history.

## Next steps

[!INCLUDE [next-steps-enrichment](../includes/next-steps-enrichment.md)]
For example, a segment that contains all the customers that have a value over 60 for *days since last email* and *days since last meeting*. That segment contains stale accounts that you can try to reactivate.

[!INCLUDE [footer-include](../includes/footer-banner.md)]
