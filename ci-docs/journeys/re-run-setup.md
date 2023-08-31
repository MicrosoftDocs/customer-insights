---
title: Re-run the Customer Insights - Journeys setup wizard
description: How to run the setup wizard so you can update, uninstall, or modify an existing Dynamics 365 Customer Insights - Journeys environment.
ms.date: 08/22/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Re-run the Customer Insights - Journeys setup wizard

[!INCLUDE[consolidated-sku-rtm-only](../includes/consolidated-sku-rtm-only.md)]

In addition to helping you install Dynamics 365 Customer Insights - Journeys for the first time, the setup wizard can also help you modify, maintain, or update your installation. You can do all of the following by re-running the setup wizard:

- Check for and apply [updates](apply-updates.md)
- Add or remove [portals integration](portal-optional.md)
- Configure an integrated portal
- Fix installation issues
- Connect a disconnected instance to marketing services
- Clean up after a [copy or restore operation](manage-marketing-environments.md)
- [Uninstall](uninstall-marketing.md) Customer Insights - Journeys

To re-run the Customer Insights - Journeys setup wizard:

1. In the Customer Insights - Journeys app, select the **Settings** area in the area switcher. Then, go to **Overview** > **Versions**.
1. To launch the setup wizard, choose the **Manage + update** link.

    > [!div class="mx-imgBorder"]
    > ![Audience configuration settings screenshot.](media/fre-re-run4.png "Audience configuration settings screenshot")

1. The Customer Insights - Journeys setup wizard opens in a new window.

    > [!div class="mx-imgBorder"]
    > ![Setup wizard running on an existing Customer Insights - Journeys instance.](media/fre-re-run3.png "Setup wizard running on an existing Customer Insights - Journeys instance")

    If an update is available, then you'll see a notice and an **Install** button at the top of the page. More information: [Keep Customer Insights - Journeys up to date](apply-updates.md)

    The following links can be available in the **Other actions** panel:

    - **Configure your portal**: This link is only shown if you have a Power Apps portal integrated with your selected Customer Insights - Journeys instance. Select this link to go to the portal configuration where you can, among other things, restart the portal or remove it from your Customer Insights - Journeys instance. More information: [Administer your portal](/powerapps/maker/portals/admin/power-platform-admin-center)
    - **Take me to the app**: Brings you to Customer Insights - Journeys.
    - **Uninstall Customer Insights - Journeys from this org**: Removes Customer Insights - Journeys from the selected instance. More information: [Uninstall Customer Insights - Journeys](uninstall-marketing.md)

    If your selected Customer Insights - Journeys instance isn't currently integrated with a Power Apps portal, then you can set this up by selecting **Use Dynamics 365 Portals or a Power Apps portal** in the main area of the window. More information: [Integrate Customer Insights - Journeys with a CMS system or Power Apps portal](portal-optional.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
