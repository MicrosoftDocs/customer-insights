---
title: "Business acounts overview in Customer Insights - Data"
description: "Learn about business accounts (B2B) in Customer Insights" 
ms.date: 08/11/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author:  sstabbert
ms.custom: bap-template
---

# Business accounts overview in Customer Insights

With Dynamics 365 Customer Insights, business accounts (B2B) aren't supported. However, current customers with B2B data are still supported. This article describes information specific to B2B environments. For all other informtion related to Customer Insights, see [Dynamics 365 Customer Insights documentation.](../index.yml)

B-to-B (business accounts) environments are not supported for:

- Business unit data separation
- Measure templates, use [measure builder](measure-builder-b2b.md).
- Predictions except for [Transactional churn](../predict-transactional-churn.mdpredict-transactional-churn.md): Predicts if a customer account will no longer purchase your products or services in a certain time frame.

## Environment

To create an environment, see [Create a new environment.](../create-environment.md) When creating the environment, select your business type:

- **Choose your business**: Primary audience for the new environment: individual consumers (B2C) or [business accounts](work-with-business-accounts.md) (B2B). If your organization mainly does business with individuals, such as a retailer or a coffee shop, choose individual consumers. If your main audience is other companies, such as a car manufacturer or a paper company, choose business accounts.

## Dataverse storage capacity entitlement

A Customer Insights subscription entitles you to extra capacity for your organization's existing [Dataverse storage capacity](/power-platform/admin/capacity-storage). The added capacity depends on the number of profiles that your subscription uses.

For example, if you have a B2B subscription with 30,000 accounts, your total storage capacity is 45 GB (3 x 15 GB) database storage, and 60-GB file storage (3 x 20 GB).

## Customer profiles

On the **Customers** page, select a customer tile to view details for the selected customer.For business accounts, in addition to the customer profile, **Contacts for this customer** display. Each contact is shown with their fields. Empty fields are hidden. For more information, see [View customer profiles.](../customer-profiles.md)

## Enrichments

Go to **Data** > **Enrichment**. The **Discover** tab shows all supported enrichment options. You can create the following enrichments for B2B:

- [Account engagement data](enrichment-office.md) provided by Microsoft
- [Company data](enrichment-dnb.md) provided by Dun & Bradstreet
- [Company data](enrichment-leadspace.md) provided by Leadspace
- [Enhanced addresses](../enrichment-enhanced-addresses.md) provided by Microsoft
- [Enhanced company data](enrichment-enhanced-company-data.md) provided by Microsoft
- [Location data](../enrichment-azure-maps.md) provided by Microsoft Azure Maps
- [Location data](../enrichment-here.md) provided by HERE Technologies
- [SFTP custom data](../enrichment-SFTP-custom-import.md) through Secure File Transfer Protocol (SFTP)

For more information, see [data enrichment (preview) overview](../enrichment-hub.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]

## Segment exports

You can export segment tables from Customer Insights. Segments are built on the *account* table or the *contact* table. To export account segments as is, the target system needs to support pure account segments. This is the case for [LinkedIn](../export-linkedin-ads.md) when you choose the **company** option while defining the export.

All other target systems require fields from the contact table.

With two segment types (contacts and accounts), Customer Insights automatically identifies which type of segments are eligible for export based on the target system. For example, for a contact-focused target system like Mailchimp, Customer Insights only allows you to choose contact segments to export.

To build segments, see [Create complex segments with segment builder](../segment-builder.md#create-a-new-segment-with-segment-builder). When configuring the export, you select the included data fields, depending on the target system you are exporting data to.

### Limits on segment exports

- Third-party target systems may limit the number of customer profiles that you can export.
- For business accounts, you'll see the number of accounts or contacts depending on the segment. You will get a warning if the segment is too large. Exceeding the limits of the target systems results will skip the export.

## Power Apps

With a [Power Apps connector](../export-power-apps.md), you can choose the **UnifiedContact** table to display the contacts of a customer.

Delegation for **UnifiedContact** only works for the fields **ContactId** and **CustomerId**.

## Segments



[!INCLUDE [footer-include](includes/footer-banner.md)]
