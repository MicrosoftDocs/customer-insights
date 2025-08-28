---
title: Integrate reCAPTCHA service with Customer Insights - Journeys forms
description: Add reCAPTCHA to Customer Insights - Journeys forms to validate submissions and prevent spam. See how to enable and configure reCAPTCHA.
ms.date: 05/23/2025
ms.topic: how-to
author: petrjantac
ms.author: colinbirkett
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:05/23/2025
---

# Integrate reCAPTCHA service with Customer Insights - Journeys forms

Customer Insights - Journeys forms let you use custom captcha bot protection to validate form submissions. This article shows how to integrate [Google reCAPTCHA](https://www.google.com/recaptcha/about/). The flow is similar for other captcha services. The steps in this article apply to marketing and event registration form types.

> [!NOTE]
> In the current app version, only one captcha implementation can be active. If you use your own captcha provider (as outlined in the next sections), existing forms that use the out-of-the-box captcha will stop working. A custom captcha implementation requires at least basic knowledge of writing and debugging [Dataverse plugins](/power-apps/developer/data-platform/plug-ins).

> [!IMPORTANT]
> The default configuration supports reCAPTCHA v2 only.
> To implement reCAPTCHA v3, refer to the guide on [custom back-end validation](real-time-marketing-form-customize-submission-validation.md).

The process consists of these steps:

1. **Add reCAPTCHA to the form**.
1. **Add the captcha text value** to the form submission once the form is submitted.
1. **Activate reCAPTCHA plugin** and safely store the private key.

## Step-by-step example: Integrate Google reCAPTCHA

### 1. Add reCAPTCHA to the form

To add reCAPTCHA to the form:

1. Create a form in the Customer Insights - Journeys form editor.
1. Add a `data-validate-submission="true"` attribute to the `<form>` element, which enables custom validation on the form submission:
    :::image type="content" source="media/real-time-marketing-form-custom-captcha-1.png" alt-text="Add attribute to form element." lightbox="media/real-time-marketing-form-custom-captcha-1.png":::
1. Add a `<div id="g-recaptcha">` in the form as a placeholder for reCAPTCHA. This div ID is used as a reference later. Put the placeholder between the last field and the submit button.
1. Publish the form and embed the form into your website.
1. Edit the page where the form was embedded. Add the script provided by Google into the page header. This script loads the reCAPTCHA with the `onLoad` callback parameter. This callback is called as soon as the captcha is loaded.

    ```javascript
    <script src="https://www.google.com/recaptcha/api.js?onload=onloadCallback" async defer></script>
    ```

1. Add the onLoadCallback function:

    ```javascript
    function onloadCallback() {
        grecaptcha.render('g-recaptcha',
        { 
          sitekey: '{sitekey}',
        });
    }
    ```

    Replace the `{sitekey}` placeholder with the value provided by Google. The callback function renders reCAPTCHA inside the placeholder `<div id="g-recaptcha">` you created earlier.

1. Register the onloadCallback function with the form loader:

    ```document.addE1. Prevent form submission if the reCAPTCHA isn't answered.

    Make the reCAPTCHA challenge required on the client side to avoid form submission without answering the challenge.void form submission without answering the reCAPTCHA challenge.

    ```javascript
    <script>
    document.addEventListener("d365mkt-afterformload", function() {
        var form = document.querySelector("[data-form-id='7305961d-dc04-f011-bae1-0022480c3fab']"); //formId
        form.addEventListener("d365mkt-formsubmit", function(event) {
            if (grecaptcha.getResponse() === '') {                            
               event.preventDefault();
                alert('Please check the reCAPTCHA');
            }
        }, false);
    });
    </script>
    ```

### 2. Add the captcha text value to the form submission

When the form is submitted, the `g-recaptcha-response` parameter is added automatically to the form submission. The reCAPTCHA plugin hides this value and adds it to the `ValidationOnlyFields` list in the response object returned by the plugin code.

:::image type="content" source="media/real-time-marketing-form-custom-captcha-3.png" alt-text="G-recaptcha-response parameter is added." lightbox="media/real-time-marketing-form-custom-captcha-3.png":::

### 3. Activate the reCAPTCHA plugin

To activate the reCAPTCHA plugin:

1. Go to **Settings** > **Form settings** > **reCAPTCHA**.
1. Enter the private key. The private key is saved in a secure storage location.
1. Activate the plugin by switching the **Status** toggle.

:::image type="content" source="media/real-time-marketing-configure-form-recaptcha.png" alt-text="Enter key for reCAPTCHA." lightbox="media/real-time-marketing-configure-form-recaptcha.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
