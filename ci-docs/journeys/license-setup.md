---
title: Customer Insights license guidance
description: Learn about licensing information in Dynamics 365 Customer Insights.
ms.date: 04/02/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customer Insights license guidance

This article covers important key points about Customer Insights licensing and provides answers to frequently asked questions about licensing.

## Customer Insights licensing key points

> [!WARNING]
> To use entities, tables, operations, or components associated with a specific app like Sales or Service, you must be licensed for those apps. The license requirement applies regardless of whether you create a custom app to access the data.

### Check current license ownership

As a tenant admin, you can see what licenses are on your tenant by going to the [Microsoft Admin Center](https://admin.microsoft.com) then going to **Billing** > **Your Products**.

Because Customer Insights licenses aren't seat-based (that is, you don't pay per user), they aren't listed under **Licenses**. Only licenses where you pay per user and assign users show up under **Licenses**.

### Purchase guidance for Dynamics 365 Customer Insights

- You can find officially published pricing and license details, including the downloadable Power Platform and Dynamics 365 license guide, on the [Customer Insights pricing page](https://dynamics.microsoft.com/ai/customer-insights/pricing/). Review the license guide for detailed entitlements.
- The "attach" priced base offer (the price for customers that already have other qualifying Dynamics 365 apps) has the same entitlement definition as the full-priced base offer. It's simply discounted for customers who already own pre-qualifying Dynamics 365 application offers. 
- You can find officially published pricing and license details, including the downloadable Power Platform and Dynamics 365 license guide, on the [Customer Insights pricing page](https://dynamics.microsoft.com/ai/customer-insights/pricing/). Review the license guide for detailed entitlements.
- If you purchased before September 2023, you probably own one or both of the standalone licenses: Dynamics 365 Marketing (standalone) or Dynamics 365 Customer Insights (standalone). The new entitlements given with the currently available Dynamics 365 Customer Insights license don't transfer to the old standalone licenses. To get the new entitlements, you can add the new Dynamics 365 Customer Insights license to your tenant at any time in your contract cycle. Depending on your purchase channel, you can remove the standalone licenses on your renewal date.
- As of September 2023 (when the new licenses and entitlements were launched), licenses are no longer associated with individual application installations as they were prior for the Marketing standalone license model. The applications for Customer Insights - Journeys (formerly called Marketing) and Customer Insights - Data are the same for the old licenses and the new license. **Do not uninstall and reinstall the applications when you change license types**.
- The new entitlements don't apply to subscribers of the old, standalone models. For example, if you own the old standalone Dynamics 365 Marketing license, you don't gain access to install Customer Insights - Data. You must buy the new Dynamics 365 Customer Insights base license to gain the new entitlements.
- If you're a subscriber of the standalone Marketing or Customer Insights offers prior to September 2023 and you want to renew on those offers instead of taking advantage of the new, combined Customer Insights offer, you can work with your seller or partner to renew on the legacy, standalone offers.
- If you're on the old Dynamics 365 Marketing standalone license and need to add interacted people (formerly called "active contacts") quota but can't buy the old active contacts add-ons because you previously didn't own the exact SKUs, you can buy the new Interacted People T1-T3 add-ons to increase your quota.
- To scale your needs for the application you're using, you can buy add-ons of interacted people (for the Customer Insights - Journeys app) or unified people (for the Customer Insights - Data app) independently of each other.
    - The meters for interacted people and unified people are independent of each other.
    - Interacted people is the number of Dataverse entities (contacts, leads, accounts, profiles, custom, other) that have received an interaction in the last 12 months. 
    - Unified people is the number of unique profiles generated using Customer Insights - Data to merge data records across multiple sources and/or Dataverse entities to result in a single, unified profile for a given person. For example using Dataverse, if you have multiple contact and lead entities with the email address "lamar@contoso.com," all these entities resolve to a single unified profile representing lamar@contoso.com.
- If you plan to use SMS, you must also sign up for an account with an SMS service provider to get a phone number and SMS delivery. [See the list of supported providers](real-time-marketing-text-messaging-setup.md) and sign-up for the provider of your choice. 

### Entitlement details

- The new base Customer Insights license entitles you to:
    - 10,000 interacted people at the tenant level for use with the Customer Insights - Journeys app to engage contacts, leads, profiles, accounts, and other Dataverse entities.
    - 100,000 unified people at the tenant level for use with the Customer Insights - Data app to unify, enrich, and know the customer.
- You get 10x interactions per month for the Customer Insights - Journeys app as a [safe use limit](fair-use-policy.md). This means that you can send interactions up to 10 times the total number of interacted people you own at the tenant level. For example, if you own 10,000 interacted people, you can send up to 100,000 interactions per month. Interactions aren't tied to the number of interacted people they're distributed to. In the example, you can choose whether to send all 100,000 interactions to one interacted person or allocate the interactions among interacted people. Interactions reset monthly and don't roll over. To get more than 100,000 interactions per month, increase the number of interacted people you own. Interaction usage and performance is subject to environment level [safe use limits](fair-use-policy.md).
- All quota counts at the tenant level across different environment types (sandbox or production) because the database capacity and services cost Microsoft the same amount of money regardless of the type of environment or application lifecycle development cycle in which it's being used. All quota usage is summed at the tenant level across all environment types.
- With the new Customer Insights license sold after September 2023, you can install the **Customer Insights - Journeys** app up to four times on any of your Dataverse environments.
- With the new Customer Insights license sold after September  2023, you can install the **Customer Insights - Data** app up to four times on any of your Dataverse environments.
- To accommodate migration scenarios, the installation management page allows you to install two times more than you're entitled. If you need to install either application more than four times, you can buy an additional instance of the base license to get four more application installation entitlements per app.
- Email throughput of 500,000 messages per hour is granted as follows:
    - For customers on the standalone Dynamics 365 Marketing SKU with 10,000,000 or more active contacts.
    - For customers with the new Dynamics 365 Customer Insights SKU with 500,000 or more interacted people.
    - For customers with the new Dynamics 365 Customer Insights SKU who have less than 500,000 interacted people but have purchased the 500,000 sending burst add-on through their seller.
- The Dataverse entitlements on both the full price and attach base offers are the same. In other words, you get the same amount of Dataverse entitlements on the full price base offer as you do for the attach priced base offer. You can only get the Dataverse entitlements for the base offer (either full-priced or attached priced) one time, regardless of how many instances of the base offer you buy. You receive incremental Dataverse entitlements for each unit of add-on packs you buy of interacted people and unified people, respectively.

### Licenses vs. applications

- As of September 2023, application installation licenses are counted at the tenant level. Prior to this change, with the Dynamics 365 Marketing standalone license and installation model, each license was tightly bound to an environment to enforce the use of one license per environment. As of September 2023, this tight binding has been removed to accommodate both the old Dynamics 365 Marketing standalone license model and the new Dynamics 365 Customer Insights license model. Licenses are counted at the tenant level and displayed in the installation quota at the top of the installation management page. Also with this change, listings of the licenses in the **Power Platform Admin Center** under **Resources** > **Dynamics 365 Apps** are only a means to open the installation management page and always show as non-configured.

## Licensing FAQs

### How is Customer Insights - Journeys licensed?

Customer Insights - Journeys is licensed per tenant, with each tenant priced according to the number of interacted persons stored in your database. To identify contacts, Customer Insights - Journeys monitors key interaction types. Any contact that performs one or more interactions is flagged as an interacted person and count against the allotment. Here are answers to several of the most frequently asked questions about licensing:
          
- **What is an interacted person?**  
    An interacted person is any entity (such as a contact, lead, account, or Customer Insights - Data profile) engaged in an interaction. Entities that are stored, but not marketed to using Customer Insights - Journeys interactions don't count towards the interacted people quota. After an interaction (see below) is logged for a person. It doesn't matter how many interactions occur on that entity, it's counted once. After an interacted person hasn't received or engaged an interaction for 12 months, the entity becomes inactive and is no longer counted.
- **What is an interaction?**  
    An interaction is an outbound message or inbound action (such as a form submission) orchestrated through Customer Insights - Journeys. The interaction can be sent through out-of-box channels available in Customer Insights - Journeys (for example, email, SMS, or push notifications), other Microsoft channels (for example, ACS), or third-party systems integrated with Customer Insights - Journeys (for example, other text message (SMS) providers). Form submissions and other inbound channels are also considered as interactions. Safe use limits allow 10x interactions per interacted person licensed.  
- **Which interacted people count against my quota?**  
    Interacted people are licensed at the tenant level. Therefore, any entities across all Dataverse environments on a tenant where the Customer Insights - Journeys application is orchestrating interactions count toward the total interacted people for the tenant. This is true for any type of environment including production, sandbox, developer, or trial.
- **Where can I see my quotas and quota usage?**  
    To see how many of each quota you've purchased and used, go to **Settings** > **Advanced settings** > **Other settings** > **Quota limits**.
- **What is my monthly interaction quota?**  
    Your monthly interaction quota is equal to 10 times the number of interacted people you have purchased, per month. For example, if you own 1 interacted person, you can interact with them 10 times per month. If you need more than 10 interactions, you should increase the number of interacted people you own to allow for the volume of monthly interactions you need to send. Consider the peak month of the year you need to optimize for and ensure that you have the right number of interacted people to allow for that volume and corresponding performance.
- **How long is a person considered interacted?**  
    When an entity is interacted with, it's counted as an interacted person and stays that way until it hasn't been interacted with for 12 months. Interacted person consumption is cumulative throughout the license period and even post-license extension, subject to the 12-month rule mentioned above.

### Do I have to install the four Customer Insights - Journeys and Customer Insights - Data app installs on the same four environments?

No. You can install each app four times. You can choose the same four environments or four different environments for a total of eight independent installations.

### Do I get the base quota for each install?

No, the quota is at a tenant level and while each environment drives consumption, total quota is counted and managed at the tenant level across all environments.

### One month of the year I send more than the 10x interactions per month allowed. What should I do?

You should own quota for the highest, peak amount of usage you expect to need for any given month. The quota ensures that you get the right scale and performance needed to support executing the highest volume for your audience.

### Why do I see so many listings of Dynamics 365 Marketing in Power Platform Admin Center > Resources > Dynamics 365 apps?

Every time you’ve done a self-service trial, a license is created and never removed. As of September 2023, these listings are now a means to open the installation page and mean nothing more.

### Where can I learn more about Customer Insights - Journeys licensing?
- For an overview, see [Purchase Dynamics 365 Customer Insights](purchase.md) 
- For complete terms that apply to subscribed (paid) versions, download the [Microsoft Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=866544)
- For trials, see [Customer Insights - Journeys limits for trials](trial-preview-limits.md)
