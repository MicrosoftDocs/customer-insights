---
title: Customer Insights - Journeys trial FAQ
description: Solutions to common questions related to Dynamics 365 Customer Insights trial setup and management. Learn how to resolve platform and app-specific issues.
ms.date: 09/09/2025
ms.topic: get-started
ms.custom: template-trial-faq
author: alfergus
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customer Insights - Journeys trial FAQ

[!INCLUDE [azure-ad-to-microsoft-entra-id](./includes/azure-ad-to-microsoft-entra-id.md)]

> [!NOTE]
> For the Customer Insights trial, you need to use an account that is managed by [Microsoft Microsoft Entra ID](https://azure.microsoft.com/services/active-directory/). If you cannot sign up for Customer Insights using a work or school email address, sign up for a [free Office 365 E5 trial](https://www.microsoft.com/microsoft-365/enterprise/office-365-e5), then use the email address associated with your Office 365 E5 trial to sign up for the Customer Insights trial.

## Customer Insights-specific questions

The following are frequently asked questions about Customer Insights - Journeys trials.

### Can I convert the trial to a paid license?

To buy a license directly, go to **admin.microsoft.com** > **Purchase Services** and search for "Customer Insights." Once you have the license, you can convert the trial environment for Customer Insights - Journeys to a paid environment in the Power Platform admin center by selecting the environment and selecting **Convert to Production**. This changes the environment type from "Trial" to "Production."

There are additional steps if you also used Customer Insights - Data and want to preserve your work from that trial. Visit [Customer Insights - Data Trial FAQ](../data/trial-faq.md) for details on how to preserve your configurations from the Customer Insights - Data trial in the production environment.

### How do I start using the trial?

After you sign up for the trial, you'll arrive on the app's main screen. The main screen provides links to user guides and tutorials. To learn more, visit the links in the [Additional resources](trial-signup.md#additional-resources) on the trial setup page.

### What features are available in the trial?

In most ways, Customer Insights trials are fully functional, but time-limited, production instances. The features now include Customer Insights - Journeys *and* Customer Insights - Data apps, allowing you to:

- Trials include real-time journeys features only. All new feature development and product investments are centralized in real-time journeys; therefore, the presales trial showcases the product direction for new customers. 
- Engage customers with trigger-based journeys, dynamic segments, and segments based on profiles from Customer Insights – Data.
- Unify your customer data with Customer Insights - Data.

However, there are a few key differences from the production version:

- Each Customer Insights trial comes preinstalled on a dedicated trial instance included with the trial. You can't install a Customer Insights trial on an existing instance.
- You can't uninstall or reinstall trials using the standard tools provided by the Power Platform admin center. Trials are special and are handled differently than production instances.
- You don't need to use the [installation management area](setup.md#install-uninstall-or-update-customer-insights) when setting up a trial.

### How long does the trial last?

The Customer Insights trial lasts 30 days. As [mentioned below](trial-faq.md#how-do-i-extend-the-trial), you can extend the trial once.

### Is the trial available in all supported geographical regions and languages?

Yes, the trial is available in all regions where the app is supported. To read the latest list of countries/regions where you can use Customer Insights, download the [Microsoft Dynamics 365 International Availability](https://go.microsoft.com/fwlink/p/?linkid=875097) document (PDF). For a list of supported languages, see [Supported languages](/powerapps/maker/portals/configure/enable-multiple-language-support#supported-languages).

### What are the trial limits and quotas?

The following limitations apply for the trial:

- The trial is available to you for 30 days. After that, you can request for an extension for another 30 days, buy a paid license, or sign up for a new trial.
- The trial expires if there’s no activity on the app for 14 consecutive days. Expired trials can't be reactivated. However, you can start a new trial.
- You can have only one active trial per app at any given time. However, you can sign up again after your current trial for the app ends.

Limits and quotas specific to the Customer Insights trial:

- The self-service trial is limited to 1,000 interactions per month. 
- Customer Insights - Data doesn't allow you to bring your own data lake into the trial. 
- Your system is constrained by certain limits and quotas that apply to the number of contacts you can market to, monthly email messages you can send, Litmus previews you can view, and more.
- Familiarize yourself with the terms and limits of the product before you begin to use it. The limits are different based on whether you're running a trial, preview, or subscribed version of the product.
- For subscribed (paid) versions, download the [Microsoft Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=866544) and visit the [Fair use policy](fair-use-policy.md) page.
- For trials, see [Dynamics 365 Customer Insights limits for trials](trial-preview-limits.md).

You can monitor your usage levels by going to  **Settings**  >  **Advanced settings**  >  **Other settings**  >  **Quota limits**  in Customer Insights - Journeys. More information: [Quota limits](quota-management.md).

### What if the trial limits don't meet my needs?

- If you need to test enterprise-scale concepts prior to committing to a long-term agreement, you can directly purchase a month to month subscription and cancel it at the monthly renewal date if you find the application doesn't meet your needs. Visit the [Microsoft Admin Center](https://admin.microsoft.com) and search for **Customer Insights** in the purchase catalog to find the different subscription options.

### I have an existing Dynamics 365 application license for Sales, Customer Service, or another app and existing production, sandbox, and development environments. Can I put a Customer Insights trial on my paid environment?

This isn't possible today. Trial licenses only work on trial-type environments in Power Platform. You can sign-up for a monthly, paid subscription using direct purchase on **admin.microsoft.com** > **Purchase Services** to try Customer Insights on your production, sandbox, or development-type environments and cancel the subscription at the monthly renewal timeframe. You can also upgrade this subscription to your contract pricing and durations should you choose to keep it and update your channel contract.

## Trial platform FAQ

[!INCLUDE [trial-faq-platform](./includes/trial-faq-platform.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
