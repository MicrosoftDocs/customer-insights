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

## Investigating failed form submissions
Typically manifests as `Failed to create target entity` or `Failed to update target entity` in the logs and is typically related to one of your customizations connected to create or update of contact or lead entity.

![image](https://github.com/MicrosoftDocs/customer-insights/assets/5519592/d1084b39-73ad-4966-9062-a9894e7de294)

Diagnosis:
- Temporarily [enable plugin trace logs](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/logging-tracing#enable-trace-logging) this can be having negative performance consequences so make sure to disable them back once you're done
- Resubmit the form
- Check the logs - in case of error in plugin there should be plugin name and hopefully reason why the plugin crashed
- Check the processes connected to contact / lead or other entity you're trying to create via form submission / try disabling the one intefering with contact creation
![image](https://github.com/MicrosoftDocs/customer-insights/assets/5519592/48f48655-f908-4e62-be96-26c7e8cf3c94)




> [!IMPORTANT]
> You can only re-submit failed submissions. Be aware that, by re-submitting, you may create a duplicate contact, such as when the submission fails because of a contact point consent creation error. The replay runs the whole submission process again. You can change the matching strategy before running the replay feature to avoid duplicate records.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
