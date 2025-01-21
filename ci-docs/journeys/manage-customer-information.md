---
title: Manage information about your current and prospective customers
description: How to find, create and use contact, account, and lead records in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/21/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Manage information about your current and prospective customers

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Three of the most important and common types of database records are contacts, accounts, and leads. These fundamental business entities are shared by most model-driven apps in Dynamics 365, including Dynamics 365 Customer Insights - Journeys. Read this article to learn how these basic entities are used and affected by the Customer Insights - Journeys app.

<a name="contacts"></a>

## Use contacts to manage customers

Contacts represent individual people. They're the primary customer entity in Customer Insights - Journeys. When you run a customer journey, your target segment includes only contact records. And when you create a lead, you'll also set a parent contact for that lead (or set a parent account, which itself relates to contacts). Other Dynamics 365 apps might treat these entities differently, instead focusing more on accounts or using leads that aren't related to any contact.

Most of your contacts represent customers or potential customers, but you might also include partners or suppliers among your contacts, especially for events where you'll also typically include speakers, vendors, and sponsors in your contacts database.

To view, create, or edit a contact, go to **Outbound marketing** > **Customers** > **Contacts**. This brings to you a standard list view, which you can use to search, sort, filter, create, and delete your contacts. Open any contact to view its details.

The contacts entity is common for and shared by most model-driven apps in Dynamics 365, but Customer Insights - Journeys adds several enhancements to it, including:

- **Marketing source information**: The contact **Details** tab includes a section called **Marketing**, where you can see which marketing initiatives were responsible for generating that contact.
- **Contact preferences**: The contact **Details** tab includes a section called **Contact preferences**, where you can see information about how that contact prefers to be contacted (or not contacted) by your organization. Important settings for Customer Insights - Journeys here include:
  - **Bulk email**: Controls whether Customer Insights - Journeys is permitted to send marketing email messages from customer journeys to this contact. When set to **Do not allow**, no marketing email messages are sent to this contact. Contacts can adjust this setting themselves using a subscription center. More information: [Set up subscription lists and subscription centers](set-up-subscription-center.md)
  - **Email**: This setting is part of the standard contact entity (it isn't added specifically for Customer Insights - Journeys). It controls whether any Dynamics 365 app (including Customer Insights - Journeys) can send any type of email to this contact, including both commercial and transactional messages.
  - **Prefill marketing form**: Controls whether Customer Insights - Journeys is permitted to prefill form information (like name and email) on marketing pages for this contact.  When set to **Do not allow**, all marketing pages (other than subscription centers) will present an empty form to this contact, even when the contact is recognized by the system. Contacts can set this option for themselves by setting a "remember me" check box on any marketing page that is set up to include the prefill feature.
  - **Follow email**: This field is often present, but isn't* added by Customer Insights - Journeys. It has no effect of the functionality of the Customer Insights - Journeys app, including its ability to track email interactions. You can still use it in segmentation criteria, just like any other contact field. (This field is used by the email engagement feature of Dynamics 365 Sales. More information:
 [Use email engagement to view message interactions](/dynamics365/ai/sales/email-engagement).)

- **Subscription lists**: The contact **Details** tab includes a section called **Subscription lists**, where you can see a list of each email subscription the contact has signed up for in Customer Insights - Journeys. More information: [Set up subscription lists and subscription centers](set-up-subscription-center.md)
- **Data protection**: The contact **Details** tab includes a section called **Data protection**, where you can see and set the data-privacy consent level granted by this contact, and also see whether the contact is a child and, if so, who their parent or guardian is. For more information about these features, see [Data protection and privacy](privacy.md).
- **Event information**: Each contact record provides the following information about events the contact has registered for or attended:
    - The contact **Details** tab includes a section called **Event information**, where you can see basic information that was collected from the contact when they registered for an event.
    - The contact **Events attended** tab provides complete details of all event registrations and check-ins associated with this contact.
- **Marketing insights**: Detailed KPIs and analytics about how this contact has interacted with your various marketing initiatives are provided on the **Contact: Insights** form view for the contact entity (available from the drop-down list above the contact name in the page heading). More information: [Analyze results to gain insights from your marketing activities](insights.md)

## Use accounts to manage customer companies

Accounts are companies that you market and sell to. They can also be partner companies or suppliers. If you use accounts, you'll also set up at least one contact for each of them&mdash;these contacts usually represent employees at the company.

> [!IMPORTANT]
> Customer journeys can only target contacts, not accounts or leads, so be sure to create contact records for everyone you want to include in your customer journeys, and then associate each of them with any relevant accounts or leads.

To view, create, or edit an account, go to **Outbound marketing** > **Customers** > **Accounts**. This brings to you a standard list view, which you can use to search, sort, filter, create, and delete your accounts. Open any account to view its details.

<a name="leads-in-marketing"></a>

## Use leads to register and track expressions of interest

A primary goal of Customer Insights - Journeys is to generate interest and then find, nurture, and qualify leads for salespeople. As mentioned, Customer Insights - Journeys is centered around contacts, which is the only type of customer entity that you can target by using a customer journey. When a contact shows interest in one of your products or services, you'll either generate a lead record that relates to that contact or allow a landing page to generate the lead automatically. The lead represents an expressed interest by the related contact in some specific product. A given contact might have several leads associated with it, each representing a different level of interest in a different product or offer.

You can associate each lead with either a parent contact or a parent account. If you choose to create account-based leads, then each account must be associated with one or more contact records because your segments and customer journeys still need to include and target contacts, not accounts. In this regard, accounts are treated as collections of one or more contacts. More information: [Account-based marketing](account-based-marketing.md).

Salespeople sometimes use leads differently and might therefore create leads that don't have parent contacts assigned, but you can easily customize your system to work with both types of leads. For details about how to integrate sales-driven (lead-centered) and marketing-driven (contact-centered) workflows, see [Market to leads](market-to-leads.md).

Customer Insights - Journeys keeps an eye on your leads and can automatically score each of them based on how their parent contacts interact with your marketing initiatives. For example, the lead score might increase each time the parent contact opens a relevant email, signs up for a download, or attends a sales event. After a lead reaches a "sales-ready" score threshold, it's considered marketing-qualified and is ready to be taken over by a salesperson. The salesperson might eventually promote the lead to an opportunity and then go on to close the sale. Or the salesperson might decide to send it back to marketing for further nurturing.

Customer Insights - Journeys collects detailed interaction records for each contact. These records include information such as email opens, email clicks, website visits, and more. Interaction records relate to contacts, not to leads or accounts, so when you're reviewing marketing insights for a lead or account, you're actually viewing interaction records for the contact(s) associated with that lead or account. Leads that don't have a parent contact or account associated with them won't show many insights and also can't be scored automatically by Customer Insights - Journeys.

To view, create, or edit a lead, go to **Outbound marketing** > **Customers** > **Leads**. This brings you to a standard list view, which you can use to search, sort, filter, create, and delete your leads. Open any lead to view its details. Select **New** in the command bar to create a new lead.

More information: [The lead lifecycle](lead-lifecycle.md)

## Gain insights into how contacts, accounts, and leads are interacting with your marketing initiatives

Once you have Customer Insights - Journeys installed, your instance begins to collect information about how each of these entities interacts with your marketing activities. The system provides a wealth of information, including analytics, KPIs, graphs, and more, to help you gain insights from your marketing results. More information: [Analyze results to gain insights from your marketing activities](insights.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
