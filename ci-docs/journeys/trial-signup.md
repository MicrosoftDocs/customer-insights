---
title: Sign up for a free trial
description: Learn how to quickly sign up for and start a free Dynamics 365 Customer Insights - Journeys trial. Explore the app with tours and videos, and find additional learning resources.
ms.date: 09/09/2025
ms.topic: get-started
ms.custom: template-trial-setup
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Sign up for a free Customer Insights - Journeys trial

[!INCLUDE [azure-ad-to-microsoft-entra-id](./includes/azure-ad-to-microsoft-entra-id.md)]

Customer Insights offers a free 30-day trial. As an enterprise customer, you may also have access to extended trials (called admin trials) for proof of concepts through your salesperson. After a quick sign-up, you'll have access to many of the Customer Insights - Journeys and Customer Insights - Data apps' key features. The trial allows you to test the app with sample data and even try out your own customer data. [Learn more about Dynamics 365 Customer Insights - Journeys features](real-time-marketing-overview.md)

> [!NOTE]
> As of September 2023, the trial includes the Dynamics 365 Customer Insights - Journeys and Dynamics 365 Customer Insights - Data applications installed on the same Dataverse environment. Prior to September 2023, these were two separate trials on two separate environments.

## Sign up for the self-service trial

1. If your tenant admin doesn't block self-service trials on your tenant, go to the [trial overview page](https://dynamics.microsoft.com/ai/customer-insights/) and select the **Try for free** button.
1. To sign up you, need to use a work or school email address, not a personal email address. If you don't have a work or school email address, your tenant admin doesn't allow self-service trials, or if your school or work account isn't [managed by Microsoft Microsoft Entra ID](https://azure.microsoft.com/services/active-directory/), sign up for a [free Office 365 E5 trial](https://www.microsoft.com/microsoft-365/enterprise/office-365-e5), then use the email address associated with your Office 365 E5 trial to sign up for the Customer Insights trial.
1. Choose your starting app: Customer Insights - Journeys or Customer Insights - Data. If you choose Customer Insights - Data, complete the following steps:
    1. For the Customer Insights - Data app, you start in a demo experience. To enable Customer Insights - Data on the same Dataverse environment as Customer Insights - Journeys, select the **Start Trial** button in the upper right corner. This completes the installation of the Customer Insights - Data application.
    1. To sync the segmentation data between Customer Insights - Journeys and Customer Insights - Data, in the Customer Insights - Journeys app area switcher go to **Settings** > **Data Management** > **Customer Insights data connector** and select **Connect**. This may have happened automatically.
1. Customers can have only one concurrent self-service trial on the tenant at a time. They can also have an additional admin (subscription-based trial) on the tenant concurrently if they have an admin trial license. Users on the same tenant who sign-up for the self-service trial are added to the existing self-service trial environment if one is already active. The trial can be converted to a production type environment once a paid license is on the tenant. To start the trial over, delete the trial environment in [Power Platform admin center](https://admin.powerplatform.microsoft.com) and sign-up for a new one. Trials nearing expiration can be [extended one time](/power-platform/admin/trial-environments#extend-a-trial-standard-environment). 

## Set up an admin trial using a subscription-based trial environment

1. If your tenant admin doesn't allow self-service trials, they can get an admin trial license through the [Microsoft Admin Center](https://admin.microsoft.com) or through the Microsoft salesperson.
1. Once the admin trial license is added to the tenant through the Microsoft Admin Center or a promo code URL from a Microsoft salesperson, you can create a new subscription-based trial environment in the Power Platform admin center and install Customer Insights - Journeys and Customer Insights - Data.
    1. On the **Manage** > **Environments** page in [Power Platform admin center](https://admin.powerplatform.microsoft.com), select **New** and fill out the environment details. Select **Subscription-based Trial** as the type of environment. To ensure you can install apps on the environment, toggle **Allow D365 Apps**. 
    1. On the **Manage** > **Dynamics 365 Apps** page, find Dynamics 365 Customer Insights or Dynamics 365 Marketing, select the **...** ellipsis, then select **Manage** to open the installation management page.
    1. To manage installation of trials, select **Trials**. You see the subscription-based trial environment you created and you can then install Customer Insights - Journeys and Customer Insights - Data. Select **Install** next to each application to install them.

## Customer Insights - Data trial

To install *only* a Customer Insights - Data trial on the same environment as the Customer Insights - Journeys trial, go to the **Get Started** page in Customer Insights - Journeys and select the **Launch Customer Insights - Data** button on the top banner. This allows the Customer Insights - Data application to know your environment ID and user ID and add the Customer Insights - Data application to the existing trial environment. Select the **Start Trial** button in the upper right to complete the Customer Insights - Data app installation.

## What if the standard trial doesn't meet your needs?

If you need to test enterprise-scale concepts prior to committing to a long-term agreement, you can directly purchase a month to-month subscription and cancel it at the monthly renewal date if you find the application doesn't meet your needs. Visit the [Microsoft Admin Center](https://admin.microsoft.com) and search for **Customer Insights** in the purchase catalog to find the different subscription options and choose month-to-month.

## What to try

Your trial environment includes many of the same features as the paid version. The links below guide you through some of the key features.

- [Create a marketing email and go live](create-marketing-email.md)
- [Target the right customers using the query assist copilot](real-time-marketing-natural-language-segments.md)
- [Use Copilot to create journeys by describing them in their own words](real-time-marketing-use-copilot-create-journey.md)
- [Create forms](real-time-marketing-form-create.md)
- [Send a targeted email blast](real-time-marketing-email-get-started.md)

## Additional resources

- [Dynamics 365 Customer Insights free trial sign up page](https://dynamics.microsoft.com/ai/customer-insights/)
- [Explore Microsoft Learn training](/training/browse/?products=dynamics-marketing)
- [Watch videos on the product playlist](https://www.youtube.com/playlist?list=PLcakwueIHoT_cV1n1es1YJt_T2A5u-XpR)
- [Trial FAQ](trial-faq.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]