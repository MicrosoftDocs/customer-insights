---
title: Customer Voice FAQs
description: Frequently asked questions about using Dynamics 365 Customer Voice in the outbound marketing area of Dynamics 365 Customer Insights.
ms.date: 09/15/2023
ms.update-cycle: 1095-days
ms.topic: faq
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing, evergreen
---

# Customer Voice FAQs

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

Read this article to find answers to common questions and solutions to known issues associated with using Customer Voice in the outbound marketing area of Dynamics 365 Customer Insights.

## My surveys aren't working; how can I fix my Dynamics 365 Customer Voice installation?

If you don't see the **Survey** tile in the **Toolbox** of your [customer journey designer](customer-journeys-create-automated-campaigns.md), or if it isn't working properly, then the Customer Insights - Journeys setup wizard might have failed to set up the Dynamics 365 Customer Voice app correctly. If this was the only error that occurred during installation, then you might not have received any messages about it. To fix this, do the following:
          
1. [Open the installation management area](setup.md).
1. Go to **Resources** > **Dynamics 365 apps** on the left navigation pane, select any **Dynamics 365 Customer Voice** application in the applications list, and then select the **Install** button on the top ribbon.
          
    > [!div class="mx-imgBorder"]
    > ![Install Dynamics 365 Customer Voice](media/admin-cv-manage.png)
          
1. The **Install Dynamics 365 Customer Voice** pane opens.
          
    > [!div class="mx-imgBorder"]
    > ![Set up your Customer Voice installation](media/admin-cv-setup.png)
          
    Do the following:
    - Choose the instance you are having trouble with from the **Select an environment** drop-down list. 
    - Read the license terms and the privacy policy carefully. If you agree with their terms, select the **I agree to the terms of service** check box.
          
1. Select **Install**. A message at the bottom of the page announces that the installation has successfully started.
1. To track the installation progress, go back to your Power Platform admin center and open the **Environments** list. Select your environment in the list and then select **Resources** > **Dynamics 365 apps** in the top ribbon.
          
    > [!div class="mx-imgBorder"]
    > ![Manage the solutions installed on your environments](media/admin-cv-instances.png)
          
1. The **Dynamics 365 apps** page for your selected environment opens, showing a list of solutions installed on your selected environment and the status of each of them. Find the **Dynamics 365 Customer Voice** solution and then refresh the page periodically until you can see that the solution is shown as **Installed**.
          
    > [!div class="mx-imgBorder"]
    > ![Installation progress](media/admin-cv-solutions4.png)
          
1. Open Customer Insights - Journeys, go to **Settings** > **Advanced settings** > **Marketing settings** > **Marketing data configuration**, and enable syncing of the **Survey (msdyn_survey)** entity. More information: [Choose entities to sync with the marketing-insights service](mkt-settings-sync.md)
1. Confirm that the **Survey** tile is now visible in the customer journey toolbox, and that your surveys are working correctly.
          
If your surveys still aren't working after completing these steps, [contact Microsoft Support](/power-platform/admin/get-help-support) for assistance.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
