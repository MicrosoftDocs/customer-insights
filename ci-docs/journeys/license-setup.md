---
title: Customer Insights license guidance
description: 'Customer Insights licensing: Learn how to buy, manage, and monitor Dynamics 365 Customer Insights licenses, entitlements, and quotas. Get answers to common questions.'
ms.date: 06/13/2025
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
  - ai-seo-date:06/13/2025
---

# Customer Insights license guidance

This article explains key points about Customer Insights licensing and answers common licensing questions.

## Customer Insights licensing key points

> [!WARNING]
> To use entities, tables, operations, or components associated with a specific app like Sales or Service, you must be licensed for those apps. The license requirement applies regardless of whether you create a custom app to access the data.

### Check current license ownership

As a tenant admin, you can see what licenses are on your tenant by going to the [Microsoft Admin Center](https://admin.microsoft.com) then going to **Billing** > **Your Products**. 

Because Customer Insights licenses aren't seat-based (that is, you don't pay per user), they aren't listed under **Licenses**. Only licenses where you pay per user and assign users appear under **Licenses**.

### Add licenses to your tenant

Depending on how you acquire your license, there are different pathways to get the license on your tenant:

- If you purchase directly through the Microsoft Admin Center, you follow the e-commerce flow and the license is added to **Your Products** as soon as you complete the purchase flow.
- If you purchase through a reseller, partner, or Microsoft volume licensing channels, there are various workflows in place that can take different amounts of time. If you don't see the license in *your products*, contact your reseller, partner, or Microsoft sales representative for help. The product team can't help until the license is on the tenant.
- If you're redeeming internal usage rights (IURs) through the Microsoft Partner Network subscription programs, [follow the instructions](/partner-center/cloud-services#activate-a-subscription-for-the-first-time) to redeem your benefits, choose Dynamics 365 Marketing or Dynamics 365 Customer Insights, and add the licenses to your tenant using the assigned promo codes from the Partner Center.

### Monitoring your usage

As stated in the published Dynamics 365 license guide, Customer Insights - Journeys and Customer Insights - Data are tenant-level licenses, which means that all meters associated with the licenses are summed at the tenant level across any environment of any type (sandbox, production, trial) that's using the application on a given tenant. To monitor your tenant-level usage:
- For Customer Insights - Journeys, go to **Settings** > **Quota Limits** where you can see the total tenant-level entitled interacted people and monthly interactions as well as how much has been used on the environment you are on and all **other** environments on the tenant.
- For Customer Insights - Data, visit each environment on the tenant and sum the total count of **Customers** in each environment. You can visit each environment using the environment switcher in the upper right corner.
- For Dataverse and other platform-related meters, visit **Power Platform Admin Center** > **Capacity**.

### Purchase guidance for Dynamics 365 Customer Insights

- You can find officially published pricing and license details, including the downloadable Power Platform and Dynamics 365 license guide, on the [Customer Insights pricing page](https://www.microsoft.com/dynamics-365/products/customer-insights/pricing). Review the license guide for detailed entitlements.
- The "attach" priced base offer (the price for customers that already have other qualifying Dynamics 365 apps) has the same entitlement definition as the full-priced base offer. It's discounted for customers who already own prequalifying Dynamics 365 application offers.
- Dynamics 365 Customer Insights licenses are tenant-level. If you have more than one tenant, you must purchase licenses for each tenant.
- If you purchased before September 2023, you probably own one or both of the standalone licenses: Dynamics 365 Marketing (standalone) or Dynamics 365 Customer Insights (standalone). The new entitlements given with the currently available Dynamics 365 Customer Insights license don't transfer to the old standalone licenses. To get the new entitlements, you can add the new Dynamics 365 Customer Insights license to your tenant at any time in your contract cycle. Depending on your purchase channel, you can remove the standalone licenses on your renewal date.
- As of September 2023 (when the new licenses and entitlements were launched), licenses are no longer associated with individual application installations as they were prior for the Marketing standalone license model. The applications for Customer Insights - Journeys (formerly called Marketing) and Customer Insights - Data are the same for the old licenses and the new license. **Do not uninstall and reinstall the applications when you change license types**.
- The new entitlements don't apply to subscribers of the old, standalone models. For example, if you own the old standalone Dynamics 365 Marketing license, you don't gain access to install Customer Insights - Data. You must buy the new Dynamics 365 Customer Insights base license to gain the new entitlements.
- If you're a subscriber of the standalone Marketing or Customer Insights offers from before September 2023 and you want to renew on those offers instead of taking advantage of the new, combined Customer Insights offer, you can work with your seller or partner to renew on the legacy, standalone offers.
- If you're on the old Dynamics 365 Marketing standalone license and need to add interacted people (formerly called "active contacts") quota but can't buy the old active contacts add-ons because you previously didn't own the exact SKUs, you can buy the new Interacted People T1-T3 add-ons to increase your quota.
- To scale your needs for the application you're using, you can buy add-ons of interacted people (for the Customer Insights - Journeys app) or unified people (for the Customer Insights - Data app) independently of each other.
    - The meters for interacted people and unified people are independent of each other.
    - Interacted people is the number of Dataverse entities (contacts, leads, profiles, custom, other) that have received an interaction in the last 12 months. 
    - Unified people is the number of unique profiles generated using Customer Insights - Data to merge data records across multiple sources and/or Dataverse entities to result in a single, unified profile for a given person. For example using Dataverse, if you have multiple contact and lead entities with the email address "lamar@contoso.com," all these entities resolve to a single unified profile representing lamar@contoso.com.
- If you plan to use SMS, you must also sign up for an account with an SMS service provider to get a phone number and SMS delivery. [See the list of supported providers](real-time-marketing-text-messaging-setup.md) and sign-up for the provider of your choice. 

### Entitlement details

- The new base Customer Insights license entitles you to:
    - 10,000 interacted people at the tenant level for use with the Customer Insights - Journeys app to engage contacts, leads, profiles, and other Dataverse entities.
    - 100,000 unified people at the tenant level for use with the Customer Insights - Data app to unify, enrich, and know the customer.
- You get 10x interactions per month for the Customer Insights - Journeys app as a [safe use limit](fair-use-policy.md). This means that you can send interactions up to 10 times the total number of interacted people you own at the tenant level. For example, if you own 10,000 interacted people, you can send up to 100,000 interactions per month. Interactions aren't tied to the number of interacted people they're distributed to. In the example, you can choose whether to send all 100,000 interactions to one interacted person or allocate the interactions among many interacted people. Interactions reset monthly and don't roll over. To get more than 10x interactions per month, increase your interacted people entitlement. Interaction usage and performance are subject to environment-level [safe use limits](fair-use-policy.md).
- All quota counts at the tenant level across different environment types (sandbox or production) because the database capacity and services cost Microsoft the same amount of money regardless of the type of environment or application lifecycle development cycle in which it's being used. All quota usage is summed at the tenant level across all environment types.
- By June 30, 2024, if you own paid licenses there are no longer application installation limits for either **Customer Insights - Journeys (real-time only)** or **Customer Insights - Data** on your production and sandbox Dataverse environments. 
- For Customer Insights - Journeys, outbound marketing solution installations are still limited by the prior application licensing constraints. If you own Dynamics 365 Marketing or the add-ons for sandbox or production installations, you get one installation of outbound marketing solutions per license. If you own the Dynamics 365 Customer Insights license available after September 2023, you get four outbound marketing solutions.
- Trial installations are still limited to one environment per trial license. 
- See [detailed documentation about email throughput](real-time-marketing-throughput-guidance.md). Email throughput of 500,000 messages per hour is granted as follows:
    - For customers on the standalone Dynamics 365 Marketing SKU with 10,000,000 or more active contacts.
    - For customers with the new Dynamics 365 Customer Insights SKU with 500,000 or more interacted people.
    - For customers with the new Dynamics 365 Customer Insights SKU who have less than 500,000 interacted people but have purchased the 500,000 sending burst add-on through their seller.
- The Dataverse entitlements on the full price and the attach base offers are the same. In other words, you get the same number of Dataverse entitlements on the full price base offer as you do for the attach priced base offer. You can only get the Dataverse entitlements for the base offer (either full-priced or attached priced) one time, regardless of how many instances of the base offer you buy. You receive incremental Dataverse entitlements for each unit of add-on packs you buy of interacted people and unified people, respectively.

### Licenses vs. applications

As of September 2023, application installation licenses are counted at the tenant level. Prior to this change, with the Dynamics 365 Marketing standalone license and installation model, each license was tightly bound to an environment to enforce the use of one license per environment. As of September 2023, this tight binding has been removed to accommodate both the old Dynamics 365 Marketing standalone license model and the new Dynamics 365 Customer Insights license model. Licenses are counted at the tenant level and displayed in the installation quota at the top of the installation management page. Also with this change, listings of the licenses in the **Power Platform Admin Center** under **Resources** > **Dynamics 365 Apps** are only a means to open the installation management page and always show as nonconfigured.

## Licensing FAQs

### How is Customer Insights - Journeys licensed?

Customer Insights - Journeys is licensed per tenant, and each tenant is priced based on the number of interacted people stored in your database. Customer Insights - Journeys monitors key interaction types to identify contacts. Any contact that performs one or more interactions is flagged as an interacted person and counts against the allotment. Here are answers to some of the most frequently asked questions about licensing:
          
- **What is an interacted person?**  
    An interacted person is any entity (such as a contact, lead, or Customer Insights - Data profile) engaged in an interaction. Entities that are stored, but not marketed to using Customer Insights - Journeys interactions don't count towards the interacted people quota. After an interaction (see below) is logged for a person. It doesn't matter how many interactions occur on that entity, it's counted once. After an interacted person hasn't received or engaged an interaction for 12 months, the entity becomes inactive and is no longer counted.
- **What is an interaction?**  
    An interaction is an outbound message or inbound action (such as a form submission) orchestrated through Customer Insights - Journeys. The interaction can be sent through out-of-box channels available in Customer Insights - Journeys (for example, email, SMS, or push notifications), other Microsoft channels (for example, ACS), or third-party systems integrated with Customer Insights - Journeys (for example, other text message (SMS) providers). Form submissions and other inbound channels are also considered as interactions. Safe use limits allow 10x interactions per interacted person licensed.  
- **Which interacted people count against my quota?**  
    Interacted people are licensed at the tenant level. Any entities across all Dataverse environments on a tenant where Customer Insights - Journeys orchestrates interactions count toward the total interacted people for the tenant. This applies to any environment, including production, sandbox, developer, or trial.
- **Where can I see my quotas and quota usage?**  
    You can calculate your paid quota based on your licenses, visible at **admin.microsoft.com** > **Your Products**. See the [official pricing page](https://www.microsoft.com/dynamics-365/products/customer-insights/pricing) for details about the quota granted with each offer. In Customer Insights - Journeys, see your usage by going to **Settings** > **Advanced settings** > **Other settings** > **Quota limits**. For Customer Insights - Data, your used quota is the total number of **Customers** across all instances on your tenant.
- **What is my monthly interaction quota?**  
    Your monthly interaction quota is 10 times the number of interacted people you buy, per month. For example, if you have 1 interacted person, you can interact with them 10 times per month. If you need more than 10 interactions, increase the number of interacted people you buy to match your monthly volume. Plan for your peak month to make sure you have the right number of interacted people for your needs.
- **How long is a person considered interacted?**  
    When an entity (contact, lead, or Customer Insights - Data profile) is interacted with, it's counted as an interacted person and stays that way until it hasn't been interacted with for 12 months. Interacted person consumption is cumulative throughout the license period and even post license extension, subject to the 12-month rule mentioned above.
- **Why can't I see my licenses in geos other than my home tenant geo?**
    To see your licenses in all geos, your tenant must be set up as a "multi-geo" tenant. Any employee in business applications or support can do this for you. To get help converting your tenant to multi-geo so licenses replicate across all geographies, contact your account manager. After June 14, 2024, this restriction is removed.

### Do I get the base quota for each application install?

No, the quota is at the tenant level. While each environment drives consumption, the total quota is counted and managed at the tenant level across all environments.

### One month of the year I send more than the 10x interactions per month allowed. What should I do?

Buy enough quota to cover the highest usage you expect in any month. The quota gives you the right scale and performance to support your highest volume.

### Why do I see so many listings of Dynamics 365 Marketing in Power Platform Admin Center > Resources > Dynamics 365 apps?

Each time you create a self-service trial, a license is created and isn't removed. As of September 2023, these listings only let you open the installation page through the **Manage** option.

### Where can I learn more about Customer Insights - Journeys licensing?

- For an overview, see [Purchase Dynamics 365 Customer Insights](purchase.md).
- For complete terms that apply to subscribed (paid) versions, download the [Microsoft Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=866544).
- For trials, see [Customer Insights - Journeys limits for trials](trial-preview-limits.md).

### Why does my entitled quota look higher than what I believe my license entitles me to?

- Go to **Microsoft Admin Center** > **Products** to see what licenses you have and when they expire. If you're switching from the old license models to the new one released in September 2023, you can have a period of months where the old licenses are active alongside the new ones. During those months, you see the sum total of both entitlements until the old ones expire.

### What happens when I switch from the old standalone license to the new combined license?

- You get the new license on your tenant and are entitled accordingly.
- Other than being checked for presence at installation and informing quota entitlement amounts, the licenses aren't tied to the application installations in any way. You don't need to do anything related to your existing application installations when you change license types from old to new on your tenant. Your applications continue to work unless your license expires.  

### Why does usage on sandbox environments count against my entitlement?

- The concept of sandbox and production environment types exists to support platform application lifecycle management features and doesn't intersect with any consumption usage metrics. Dynamics 365 Customer Insights, Dataverse add-ons, and other licenses are specified as tenant-level explicitly to capture usage across any and all environments of any and all types. Microsoft accrues the cost of database storage and transactions regardless of the environment type and therefore doesn't make any distinctions about usage by environment type with regard to entitlements. Entitlements are tenant-level, which is the sum of all usage at the tenant level, regardless of environment type.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
