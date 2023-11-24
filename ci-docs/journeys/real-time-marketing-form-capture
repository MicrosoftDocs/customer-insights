---
title: Create Customer Insights - Journeys form capture
description: Create forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/23/2023
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Create Customer Insights - Journeys form capture

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> A preview feature is a feature that is not complete, but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

## What is form capture and when to use it

The form capture is used to get submissions from existing forms that were not created using Customer Insights - Journeys form editor. The form capture is recommended in case your existing form also sends submissions to other systems than D365 or if the existing form contains complex logic that can't be easily recreated in Customer Insights - Journeys form editor. If the existing form can be recreated using Customer Insights - Journeys form editor, it is strongly recommended NOT to use form capture.

> [!IMPORTANT]
> **The form capture requires developer assistance**. It always easier to create the form using Customer Insights - Journeys form editor and embed the form into you existing page.

The form capture mimics submission of a standard Customer Insights - Journeys form. To link submissions of your existing form into Customer Insights - Journeys you need to create a form using Customer Insights - Journeys form editor. Once you publish that form you will be able to obtain a form capture script, which needs to be embedded into your web page containing your existing form. The script includes the definition of existing form fields mapping on attributes of Lead or Contact entity. You can see all submissions and analytics inside Customer Insights - Journeys. You can also use this form in journey orchestration with Marketing Form Submitted trigger. This form submission can also create or update Contact Point Consent and related Purposes or Topics.

## Step by step guide to create form capture

### Creating the form capture in Customer Insights - Journeys form editor

1. To create a new capture form script, go to **Customer Insights - Journeys** > **Channels** > **Forms** and select **New** on the command bar.
1. Name the form and choose the right audience. The choice of target audience is important, the form capture script field->attribute mapping will be available only for attributes of the chosen target audience (entity).
1. Add all fields that will be mapped to your existing form fields. This step is not mandatory, the field->attribute mapping is defined in the form capture code. Adding the right fields into the form will generate placeholder for attribute mapping in the form capture script making the mapping definition easier. 
1. Add Consent elements like Purpose or Topic to form and configure them. Learn more about how to [manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md).
    > [!IMPORTANT]
    > The consent definition must be done in the form editor. Changes made to consent settings done in the form capture code snippet will be ignored.
1. Add Submit button. This is required for successful validation of form before publishing.
1. Publish the form using the **Publish** button in the top right corner of the screen. Copy the form capture code snippet and embed the code snippet to your web page with existing form or hand over the code snippet to your developer. The code snippet already includes link to documentation to provide guidance to your developer.
    > [!div class="mx-imgBorder"]
    > ![Add consent element to the form.](media/real-time-marketing-form-capture-copy-script.png)

    > [!IMPORTANT]
    > The domain name where your existing form is hosted has to be enabled for external form hosting, otherwise the form submission will not be captured. Learn more about [domain authentication](domain-authentication.md).

### Embedding the capture script into your page and mapping definition