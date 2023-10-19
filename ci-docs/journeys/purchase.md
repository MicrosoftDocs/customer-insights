---
title: Purchase Customer Insights
description: How to purchase Dynamics 365 Customer Insights.
ms.date: 08/21/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Purchase Dynamics 365 Customer Insights

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

[!INCLUDE [marketing-trial-cta](./includes/marketing-trial-cta.md)]

[!INCLUDE [azure-ad-to-microsoft-entra-id](./includes/azure-ad-to-microsoft-entra-id.md)]

This article explains how to purchase a new Customer Insights environment.

<a name="how-licensed"></a>

## How to purchase Customer Insights

To install Customer Insights, you need to first purchase a base license. How you buy depends on your purchase channel, you might be buying through a Microsoft partner reseller, an enterprise Microsoft sales person, or directly via the Marketplace in [Microsoft Admin Center](https://admin.microsoft.com). In the Marketplace, search for 'Customer Insights' and select the SKU you'd like to buy with a credit card. 

Which base license you choose depends on whether you already have a qualifying Dynamics 365 application. If you have Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Supply Chain Management, Dynamics 365 Finance, or Dynamics 365 Commerce **with 10 or more users**, you can purchase the reduced price "attach" license. Otherwise, you need to purchase a standard Customer Insights license.

Once you have a base license, you can purchase add-ons to increase the number of allowed interacted people you are actively engaging or unified people you are unifying and enriching. Learn more: [Dynamics 365 Customer Insights pricing](https://dynamics.microsoft.com/ai/customer-insights/pricing/)

Be sure to check on the application data center geo availability in case you require the application to run in a specific data center region. See the [geo availabilty map](https://dynamics.microsoft.com/availability-reports/georeport/) to check availability. 

### Customer Insights licensing options

> [!IMPORTANT]
> Customers who purchased before September 2023 may own the legacy, Dynamics 365 Customer Insights and Dynamics 365 Marketing standalone licenses. The standalone licenses have different entitlements from the new Dynamics 365 Customer Insights license sold after September 2023. The differences are as follows:
>
> - Dynamics 365 Marketing (standalone) entitles 10,000 active contacts (renamed "interacted people" after September 2023) and 1 application installation. You can buy add-on subscriptions to entitle additional application installations.
> - Dynamics 365 Customer Insights (standalone) entitles 100,000 customer profiles (renamed "unified people" after September 2023) and 4 installations of the application. You can buy add-ons to unify accounts.
>
> The current Dynamics 365 Customer Insights license entitles 10,000 interacted people (formerly "active contacts"), 100,000 unified people (formerly "unified profiles"), 4 installations of the journeys app, and 4 installations of the data app. You no longer have to pay a higher unit price for add-ons to unify accounts. Learn more: [Dynamics 365 Customer Insights FAQs](ci-faq.md)

## Step 1: Buy the base license

The Dynamics 365 Customer Insights base license includes four application installations of Customer Insights - Journeys and four of Customer Insights - Data. If you own a pre-qualifying Dynamics 365 license, you're entitled to the "attach" pricing. See the [Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/?LinkId=866544&clcid=0x409) for details on pricing and entitlements.

## Step 2: Buy additional capacity

To determine how much capacity you need, consider the following:

-	How many total customers does your business have? You might be able to estimate this by counting the unique email addresses or phone numbers in your database. Buy this number of unified people.
-	For high-volume engagement, how many interactions (email/text message/push notification/custom channel) will you send per month? Divide by 10 to get the number of interacted people you need.
-	For lower-volume engagement, how many leads, contacts, profiles, or custom entities do you think you engage with on an annual basis?

## Next steps

After purchasing, go to [Install and manage Dynamics 365 Customer Insights](setup.md) to install the Customer Insights - Journeys and Customer Insights - Data applications on your existing Dataverse environments and get set up.

## User and portal licensing

Dynamics 365 Customer Insights is a tenant-level application that charges for interacted people in the Customer Insights - Journeys app and unified people in the Customer Insights - Data app. There is no charge for users to access and use the application. For customers with existing Dynamics 365 applications, any [Microsoft Entra ID](/azure/active-directory/fundamentals/whatis) users given the URL to either the Customer Insights - Journeys or Customer Insights - Data applications should be automatically given access. If they are not, there is a $0 user license that can be added to any tenant and used to assign users and force the user sync. The $0 user license can be added to purchase contracts or obtained directly through the Microsoft 365 admin center.

- To add a user license through the Microsoft 365 admin center, go to [https://admin.microsoft.com/#/catalog](https://admin.microsoft.com/#/catalog) and search for "Dynamics 365 Customer Insights User License" under the Dynamics 365 category.

You can choose to run your marketing pages, landing pages, and events website either on an external web server (such as your own CMS system) or on a Dynamics 365 Portal or Power Apps portal running on the same tenant as your Customer Insights environment. Dynamics 365 Portals and Power Apps portals are licensed separately from Customer Insights. For details about portal licensing, see the [Power Apps and Flow licensing FAQ](/power-platform/admin/powerapps-flow-licensing-faq#can-you-share-more-details-regarding-the-new-powerapps-portals-licensing). If you use an external website for your events website and marketing pages, then no portals license is needed. You choose which solution to use when you use the installation management area and can change your mind later by running it again. More information: [Integrate Customer Insights with a CMS system or Power Apps portals](portal-optional.md)

For more information about Customer Insights licensing, see the [Administration and setup FAQ](setup-troubleshooting.yml#licensing). For complete licensing details, including specific quotas and other conditions, see the  [Microsoft Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=866544).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
