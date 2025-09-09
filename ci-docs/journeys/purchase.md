---
title: Purchase Dynamics 365 Customer Insights
description: Learn how to purchase Dynamics 365 Customer Insights, including licensing options and installation steps.
ms.date: 09/09/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:12/16/2024
---

# Purchase Dynamics 365 Customer Insights

[!INCLUDE [marketing-trial-cta](./includes/marketing-trial-cta.md)]

[!INCLUDE [azure-ad-to-microsoft-entra-id](./includes/azure-ad-to-microsoft-entra-id.md)]

This article explains how to purchase a new Customer Insights environment.

<a name="how-licensed"></a>

## How to purchase Customer Insights

To install Customer Insights, you need to first purchase a base license. How you buy depends on your purchase channel. You might be buying through a Microsoft partner reseller, an enterprise Microsoft salesperson, or directly using the Marketplace in [Microsoft Admin Center](https://admin.microsoft.com). In the Marketplace, search for "Customer Insights" and select the SKU you'd like to buy with a credit card. 

Which base license you choose depends on whether you already have a qualifying Dynamics 365 application. If you have Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Supply Chain Management, Dynamics 365 Finance, or Dynamics 365 Commerce **with 10 or more users**, you can purchase the reduced price "attach" license. Otherwise, you need to purchase a standard Customer Insights license.

Once you have a base license, you can purchase add-ons to increase the number of allowed interacted people you're actively engaging or unified people you're unifying and enriching. Learn more: [Dynamics 365 Customer Insights pricing](https://www.microsoft.com/dynamics-365/products/customer-insights/pricing)

If you need the application to run in a specific data center region, be sure to check the application data center geo availability. See the [geo availability map](https://dynamics.microsoft.com/availability-reports/georeport/) to check availability. 

### Customer Insights licensing options

> [!IMPORTANT]
> Customers who purchased before September 2023 may own the legacy, Dynamics 365 Customer Insights and Dynamics 365 Marketing standalone licenses. The standalone licenses have different entitlements from the new Dynamics 365 Customer Insights license sold after September 2023. The differences are as follows:
>
> - Dynamics 365 Marketing (standalone) entitles 10,000 active contacts (renamed "interacted people" after September 2023) and 1 application installation. You can buy add-on subscriptions to entitle additional application installations.
> - Dynamics 365 Customer Insights (standalone) entitles 100,000 customer profiles (renamed "unified people" after September 2023) and unlimited application installations. You can buy add-ons to unify accounts.
>
> The current Customer Insights license entitles 10,000 interacted people (formerly "active contacts"), 100,000 unified people (formerly "unified profiles"), unlimited installations of Customer Insights - Journeys and Customer Insights - Data. You no longer have to pay a higher unit price for add-ons to unify accounts. Learn more: [Dynamics 365 Customer Insights FAQs](ci-faq.md)

### Step 1: Buy the base license

The Dynamics 365 Customer Insights base license includes four application installations of Customer Insights - Journeys and four of Customer Insights - Data. If you own a pre-qualifying Dynamics 365 license, you're entitled to the "attach" pricing. See the [Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/?LinkId=866544&clcid=0x409) for details on pricing and entitlements.

### Step 2: Buy additional capacity

To determine how much capacity you need, consider the following:

-	How many total customers does your business have? You might be able to estimate this by counting the unique email addresses or phone numbers in your database. Buy this number of unified people.
-	For high-volume engagement, how many interactions (email/text message/push notification/custom channel) will you send per month? Divide by 10 to get the number of interacted people you need.
-	For lower-volume engagement, how many leads, contacts, profiles, or custom entities do you think you engage with on an annual basis?

### Step 3: Sign up for an SMS provider of your choice

If you plan to use SMS, you must select a provider (such as Azure Communication Services) and create a separate account with that provider. The Customer Insights license doesn't provide phone numbers and SMS delivery services for production use. [See the list of supported providers](real-time-marketing-text-messaging-setup.md) and sign-up for the provider of your choice.

### Step 4: Add Customer Insights to your Microsoft 365 tenant

There are several ways to acquire a Customer Insights license. You can purchase a license from the [Dynamics 365 Customer Insights overview page](https://dynamics.microsoft.com/marketing/overview/). Or, you can go to **Billing** > **Purchase services** in your Microsoft 365 admin center. You can also purchase a license by contacting your Microsoft sales representative or channel partner. After you've purchased a license and it's added to your tenant, you’ll find it in the Power Platform admin center under **Manage** > **Dynamics 365 apps**.

You can have any number of Customer Insights licenses available on your tenant. Licenses translate to "apps" listed in the Power Platform admin center. Even old, expired trial licenses have records listed in the Power Platform admin center. You can access the installation management experience for any of these apps in the Power Platform admin center under **Manage** > **Dynamics 365 apps**. The app listing under **Dynamics 365 apps** is just a means to access the management page; it doesn't represent anything else.

Once a paid license has been applied to your tenant, it can take up to 24 hours to sync with the Dynamics 365 licensing system and be available for installation. To see your licenses in the Microsoft admin center, go to **Your products**. They won't show up under **Licenses** because they're tenant-level application licenses, not assignable seat-based licenses where you pay per user. Only pay-per-user, seat-based licenses are shown on the "Licenses" page.

To see your license in the Power Platform admin center, if you don't have a global tenant, you must select the geography that matches the home tenant geography on which the license was installed. For example, if the tenant home geo is Canada, you'll only see the license in the Power Platform admin center when you select Canada. To see the license in all geographies regardless of the tenant's home geography, Microsoft support or a Microsoft product manager must convert your tenant to a multi-geo tenant.

## Next steps

After purchasing, go to [Install and manage Dynamics 365 Customer Insights](setup.md) to install the Customer Insights - Journeys and Customer Insights - Data applications on your existing Dataverse environments and get set up.

> [!IMPORTANT]
> Your system is constrained by certain limits and quotas that apply to the number of contacts you can market to, monthly email messages you can send, Litmus previews you can view, and more. Familiarize yourself with the terms and limits of the product before you use it. The limits are different based on whether you're running a trial or subscribed version of the product.
> - For subscribed (paid) versions, download the [Microsoft Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=866544) and visit the [Fair use policy](fair-use-policy.md) page.
> - For trials, see [Dynamics 365 Customer Insights limits for trials](trial-preview-limits.md).
> 
> You can monitor your usage levels by going to  **Settings**  >  **Advanced settings**  >  **Other settings**  >  **Quota limits**. More information: [Quota limits](quota-management.md)

## User and portal licensing

Dynamics 365 Customer Insights is a tenant-level application that charges for interacted people in the Customer Insights - Journeys app and unified people in the Customer Insights - Data app. There's no charge for users to access and use the application. For customers with existing Dynamics 365 applications, any [Microsoft Entra ID](/azure/active-directory/fundamentals/whatis) users given the URL to either the Customer Insights - Journeys or Customer Insights - Data applications should be automatically given access. If they aren't, there's a $0 user license that can be added to any tenant and used to assign users and force the user sync. The $0 user license can be added to purchase contracts or obtained directly through the Microsoft 365 admin center.

- To add a user license through the Microsoft 365 admin center, go to [https://admin.microsoft.com/#/catalog](https://admin.microsoft.com/#/catalog) and search for "Dynamics 365 Customer Insights User License" under the Dynamics 365 category.

You can choose to run your marketing pages, landing pages, and events website either on an external web server (such as your own CMS system) or on a Dynamics 365 Portal or Power Apps portal running on the same tenant as your Customer Insights environment. Dynamics 365 Portals and Power Apps portals are licensed separately from Customer Insights. For details about portal licensing, see the [Power Apps and Flow licensing FAQ](/power-platform/admin/powerapps-flow-licensing-faq#can-you-share-more-details-regarding-the-new-powerapps-portals-licensing). If you use an external website for your events website and marketing pages, then no portals license is needed. You choose which solution to use when you use the installation management area and can change your mind later by running it again. More information: [Integrate Customer Insights with a CMS system or Power Apps portals](portal-optional.md)

For more information about Customer Insights licensing, see the [Administration and setup FAQ](setup-troubleshooting.yml#licensing). For complete licensing details, including specific quotas and other conditions, see the  [Microsoft Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=866544).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
