---
title: Troubleshooting Customer Insights - Journeys forms
description: Learn how to troubleshoot forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/06/2024
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

## The form styles seem broken after embedding into my page or I'm having screen reader issues with the form

Some web pages may have a generic style definition for `<table>` elements. This style definition is inherited by the embedded form, which may look different than in the form editor. You can try the new "table-less" form layout, which uses div containers. This helps resolve the style conflict between your page and the form. The table-less layout also improves screen reader performance for better accessibility. The new layout is applied only to the newly created forms; it isn't applied to existing forms.

The "table-less" layout is disabled by default. You can activate it by navigating to **Settings** > **Feature switches** > **Forms** and turning on the **Enable table-less layouts in Form editor** toggle. Don't forget to save the settings once the feature switch is enabled.

:::image type="content" source="media/real-time-marketing-form-enable-div-layout.png" alt-text="Enable div-based layout for forms.":::

## Publishing a form as a standalone page fails

This feature uploads a page with form on CDN. If the operation fails, try to run it again after a few minutes.

## Lead source is missing for newly created leads

The lead source attribute is represented by a form field in the editor. You can add the lead source as a field in the form editor. Set this field as hidden and set the correct default value to enrich your newly created lead's data.

## Form editor removed my custom JavaScript or other custom code from the HTML body

With Customer Insights - Journeys version **1.1.38813.80 or newer**, you can add JavaScript code into the `<body>` section of the HTML. If you add JavaScript into the `<head>` section, it's automatically moved to the top of the `<body>` section.

With Customer Insights - Journeys version **older than 1.1.38813.80**, you can add custom JavaScript code only to the `<head>` section of the HTML source code using the HTML editor. If the code JavaScript code is placed inside the `<body>` section, the form editor automatically removes the code without warning.

To follow security best practices, the form editor can remove unknown code from the body. [Learn more](real-time-marketing-manage-forms.md#add-custom-javascript-to-your-form) about how to customize your form using JavaScript.

## My form submission failed. How do I resubmit the submission?

The form submission may fail because of issues with custom plugins or due to invalid values in the submission.

- If the form submission failed because of the plugin issue, you can resubmit the submission from the list of submissions.
- If the form submission failed because of an invalid value, you can edit the values of submissions from the list of submissions. Select the form submission to see the submitted values. Select the value you need to change and edit the value.

> [!IMPORTANT]
> You can only re-submit failed submissions. Be aware that, by re-submitting, you may create a duplicate contact, such as when the submission fails because of a contact point consent creation error. The replay runs the entire submission process again. To avoid duplicate records, you can change the matching strategy before running the replay feature.

## Investigating failed form submissions

Failed form submissions typically manifest as "Failed to create target entity" or "Failed to update target entity" in the logs and are often related to a customization that creates or updates a contact or lead entity.

:::image type="content" source="media/submission-pipeline.png" alt-text="Chart comparing a successful submission pipeline versus an unsuccessful submission pipeline." lightbox="media/submission-pipeline.png":::

Here's how to troubleshoot a failed form submission issue:

- Temporarily [enable plugin trace logs](/power-apps/developer/data-platform/logging-tracing#enable-trace-logging) Enabling plugin trace logs can impact performance negatively, so make sure to disable them once you're done.
- Resubmit the form.
- Check the logs. If there's a plugin-related error, there should be a plugin name and a reason why the plugin crashed. Follow up with the plugin provider or [disable the plugin](https://community.dynamics.com/blogs/post/?postid=33f947e8-a5f8-4cb2-b2d9-45b444c56060). Don't disable Microsoft plugins (any plugin name that starts with "Microsoft.Dynamics.Cxp.Forms.")
- Check the processes connected to the contact, lead, or other entity you're trying to create through the form submission. Try disabling the process that's interfering with the contact creation.

:::image type="content" source="media/dynamics-processes.png" alt-text="Screenshot of processes list.":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
