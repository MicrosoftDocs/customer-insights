---
title: Provide lead profile summaries to Dynamics 365 Sales (preview)
description: Learn how Customer Insights - Data can provide insights for leads in Dynamics 365 Sales.
author: zacookmsft
ms.author: zacook
ms.reviewer: v-wendysmith
ms.topic: conceptual
ms.date: 12/13/2023
ms.custom: bap-template
---

# Provide lead profile summaries to Dynamics 365 Sales (preview)

Dyanmics 365 Sales users can enrich their lead summary with an insight from Customer Insights - Data. The insight is based on unified activity data ingested by the user, which could include reviews, purchases, appointments, web logs, and more. The insight will be an observation of one of the following:

- Customer's sentiment: their attitudes or feelings toward the business and their products or services
- Customer's behaviour: the cadence of their activities such as time intervals between appointments
- Customer's interest: how likely they are to do something such as book an appointment or purchase a specific type of product or churn if they haven't made a transaction in a while

Leveraging unified activity data from Customer Insights - Data to add an additional insight to the [lead summary in Dynamics 365 Sales](/dynamics365/sales/use-sales-copilot#enrich-leads-with-related-information) helps sellers understand more about their lead, without leaving their workflow. With lead profile summary, sellers can spend less time manually parsing through disparate data sources to find and synthesize information about their leads, and more time having effective conversations with leads.

## Requirements

- [Unified customer profile](data-unification.md)
- [Configured search](search-filter-index.md) includes customer's first name, last name, and email
- [Defined customer activities](activities.md) for the insights you want
- [Enabled Copilot consent](copilot-global-consent.md)

## Next steps

- [Responsible AI FAQs for lead profile summaries in Dynamics 365 Sales (preview)](faqs-profile-summary.md)
- [Responsible AI FAQs for Customer Insights - Data](responsible-ai-overview.md)