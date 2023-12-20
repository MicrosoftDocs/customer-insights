---
title: Troubleshooting Customer Insights - Journeys forms
description: Learn how to troubleshoot forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/20/2023
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Troubleshooting Customer Insights - Journeys forms

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

This article explains how to troubleshoot forms in Customer Insights - Journeys.

## My embedded form isn't visible on my page

Make sure that your domain is allowed for external form hosting. You don't need to finish the domain authentication process to enable external form hosting for your domain. Learn more about [domain authentication](domain-authentication.md).

## Publishing a form as a standalone page fails

This feature uploads a page with form on CDN. If the operation fails, try to run it again after a few minutes.

## Form editor removed my custom JavaScript or other custom code from the HTML body

The form editor can remove unknown code from the body. [Learn more](real-time-marketing-manage-forms.md#add-custom-javascript-to-your-form) about how to customize your form using JavaScript.

## My form submission failed. How do I re-submit the submission?

The form submission may fail because of issues with custom plugins or due to invalid values in the submission.

- If the form submission failed because of the plugin issue, you can re-submit the submission from the list of submissions.
- If the form submission failed because of an invalid value, you can edit the values of submissions from the list of submissions. Select the form submission to see the submitted values. Select the value you need to change and edit the value.

> [!IMPORTANT]
> You can only re-submit failed submissions. Be aware that, by re-submitting, you may create a duplicate contact, such as when the submission fails because of a contact point consent creation error. The replay runs the whole submission process again. You can change the matching strategy before running the replay feature to avoid duplicate records.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
