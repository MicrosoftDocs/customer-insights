---
title: Integrate a reCAPTCHA service with Customer Insights - Journeys forms 
description: Learn how to integrate reCAPTCHA bot protection into forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/12/2024
ms.topic: how-to
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Integrate a reCAPTCHA service with Customer Insights - Journeys forms

Customer Insights - Journeys forms allow you to use custom captcha bot protection to validate form submissions. This article gives an example of how to integrate [Google reCAPTCHA](https://www.google.com/recaptcha/about/). The flow is similar for other captcha services. The steps in this article apply to marketing and event registration form types.

> [!NOTE]
> In the current app version, only one captcha implementation can be active. If you use your own captcha provider (as outlined in the next sections), existing forms that use the out-of-the-box captcha will stop working. A custom captcha implementation requires at least basic knowledge of writing and debugging [dataverse plugins](/power-apps/developer/data-platform/plug-ins).

The process consists of these steps:

1. **Add reCAPTCHA to the form**.
1. **Add the captcha text value** to the form submission once the form is submitted.
1. **Activate reCAPTCHA plugin** and safely store the private key.

## Step-by-step example: Integrate Google reCAPTCHA

### 1. Add reCAPTCHA to the form

1. Create a form in the Customer Insights - Journeys form editor.
1. Add a `data-validate-submission="true"` attribute to the `<form>` element, which enables custom validation on the form submission:
    :::image type="content" source="media/real-time-marketing-form-custom-captcha-1.png" alt-text="Add attribute to form element." lightbox="media/real-time-marketing-form-custom-captcha-1.png":::
1. Add a `<div id="g-recaptcha">` in the form as placeholder for reCAPTCHA. This div ID is used as a reference later. You should put the placeholder between the last field and submit button.
    :::image type="content" source="media/real-time-marketing-form-custom-captcha-2.png" alt-text="Add placeholder for reCAPTCHA." lightbox="media/real-time-marketing-form-custom-captcha-2.png":::
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

    Replace the `{sitekey}` placeholder with the one provided by Google. This callback function renders the reCAPTCHA inside the placeholder `<div id="g-recaptcha">` you created earlier.

1. Register the onloadCallback function to be called by the form loader:

    ```document.addEventListener("d365mkt-afterformload", onloadCallback);```

1. Prevent form submission if reCAPTCHA wasn't answered

    Make reCAPTCHA challenge required on client side to avoid form submission without answering reCAPTCHA challenge.

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

Once the form is submitted, the `g-recaptcha-response` parameter is added automatically to the form submission. The reCAPTCHA plugin hides this value, and adds it to the `ValidationOnlyFields` list in the response object returned by the plugin code.

:::image type="content" source="media/real-time-marketing-form-custom-captcha-3.png" alt-text="G-recaptcha-response parameter is added." lightbox="media/real-time-marketing-form-custom-captcha-3.png":::

### 3. Activate reCAPTCHA plugin

1. Navigate to **Settings** > **Form settings** > **reCAPTCHA**.
1. Enter the private key. Your private key is saved in a secure storage location.
1. Activate the plugin by switching the **Status** toggle.

:::image type="content" source="media/real-time-marketing-configure-form-recaptcha.png" alt-text="Enter key for reCAPTCHA." lightbox="media/real-time-marketing-configure-form-recaptcha.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
