---
title: Select the audience source for journeys
description: Learn how to select the audience source for journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/22/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Select the audience source for journeys

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

Audience configuration allows you to manage your audience data sources. Customer Insights - Journeys supports **Contact**, **Lead**, and **Customer profile** entities.

To access the **Audience configuration settings**, go to **Settings** > **Customer engagement** > **Audience configuration**.

> [!div class="mx-imgBorder"]
> ![Audience configuration settings screenshot.](media/real-time-marketing-audience-configuration.png "Audience configuration settings screenshot")

Contacts and leads have default recipient fields set up for emails and phone numbers. The values from these fields are automatically populated in the *Send-to* field. You can modify the default settings by adding more recipient fields or changing the default field content.

Customer profiles have no default fields set. You can choose which fields from a customer profile should be used when sending an email or text message.

## Change your audience configuration

To make changes to the audience configuration, select a data source (**Contact**, **Lead**, or **Customer profile**) and review the information in the right pane.

> [!div class="mx-imgBorder"]
> ![Audience configuration edit pane screenshot.](media/real-time-marketing-audience-edit.png "Audience configuration edit pane screenshot")

You can change the default recipient or add more recipient fields. You can select any of the fields you added when adding an email or text message tile to a customer journey.

A default value is displayed in the *Send-to* field, but you can select any other recipient field from the dropdown menu.

> [!Important]
> Starting from the February 2024 release, it will be possible to configure multiple email addresses for a contact's email channel. However, for any release version before February 2024, you will only be able to select a single email address for a contact's email channel configuration.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
