---
title: Manage Customer Insights - Journeys forms
description: Discover how to manage and style forms in Dynamics 365 Customer Insights - Journeys. Edit, unpublish, and customize forms with ease. Learn more now!
ms.date: 04/11/2025
ms.topic: article
author: petrjantac
ms.author: colinbirkett
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Manage Customer Insights - Journeys forms

This article explains how to edit, unpublish, and manage forms in Customer Insights - Journeys.

## Edit a live form

If your form is already published and you need to update it, select the **Edit** button on the top ribbon. You can continue editing your live form and all changes are automatically published once you select the **Save** button.

> [!IMPORTANT]
> If you choose to create a copy of the form, you will have to publish the newly created copy.

The form is stored on a content delivery network (CDN) where all data is cached to provide the shortest possible loading times to the visitors of your webpage. It can take up to 10 minutes before the cache is refreshed and before you can see the changes on your webpage. You can check the result of the changes in your page if you add this parameter `#d365mkt-nocache` to your webpage URL. Never share the link to your page including this parameter with your customers. The parameter bypasses the CDN cache and slows down the page loading.

## Unpublish a form

To unpublish a live form, select the **Stop** button. The form is removed from the CDN, so your web page visitors are no longer able to submit it. The form may be still visible due to the browser cache, but it can't be submitted. The form status is changed to *Draft*.

## Form field properties

Once you select a field on the canvas, you can see its properties in the right pane.

:::image type="content" source="media/real-time-marketing-form-properties.png" alt-text="Field properties are opened once you add a field to the form." lightbox="media/real-time-marketing-form-properties.png":::

- **Placeholder text**: The placeholder inside the field. The placeholder automatically disappears once the user starts typing into the field.
- **Default value**: Set the default value for this field. The placeholder isn't visible if the default value is set.
- **Required**: If enabled, the user can't submit the form if this field is empty.
- **Validation**: Configure a rule that checks the content of the field. If the validation rule isn't met, the user can't submit the form. It's important to set the correct validation for email and phone number fields.
- **Hide field**: If enabled, the field isn't visible in the form. You can use hidden fields to store extra metadata along with the form submission.

### Custom validation

To create custom validation, enable the **Validation** option and select **Custom**. A pop-up dialog appears where you can enter a Regular Expression (RegExp). You can, for example, use a RegExp to check if the entered value matches a specific phone number format.

## Style your forms using Theme

The **Theme** section can be opened by selecting the brush icon in the right pane. Theme controls the style of all types of fields, buttons, and text. Once you set the theme of a field, it affects all fields of the same type in your form.

The theme feature is a user-friendly interface for editing CSS class definitions in the form HTML. It works only with out-of-the-box form styles. Custom CSS classes aren't visualized, but you can still edit your custom CSS classes using the HTML code editor.

:::image type="content" source="media/real-time-marketing-form-theme.png" alt-text="Edit style of your input field using Theme." lightbox="media/real-time-marketing-form-theme.png":::

**Theme** section allows you to configure:

- **Background**: Define the inner background color and border style for the whole form.
- **Text styles**: Define Heading 1, Heading 2, Heading 3, Paragraph, the Field label. The field label style doesn't affect the checkbox and radio button labels, as these labels can be configured separately. The text style definition includes font family, font size, font color, text style, and line height. You can also set the inner and outer spacing, width, and alignment. On top of these text styles, you can also set the label position (top, left, right) and the required color for your field labels.
- **Input fields** are grouped into 3 categories:
  1. Text input, dropdown, and lookup fields: These three visual styles of fields share the same style definition. You can define font family, size, color, and style for placeholder and input text styles. You can also set the field background color, menu background color, rounded corners, border, size alignment, and inner and outer spacing. The field label can be configured in text styles.
  1. Radio button: The radio button has its own label configuration, allowing you to set the font family and size. You can set the text color, styles, and background color for all options and for the selected option. You can also define rounded corners, width, and inner and outer spacing of your radio buttons.
  1. Checkbox - checkbox field has its own label configuration allowing you to set the font family, size. You can set different text color, styles, and background color for all options and for the selected option. You can also define rounded corners, width, the inner and outer spacing of your checkboxes.
- **Buttons and links**: The button definition allows you to set font family, size, color, text styles, button color, border alignment, and the inner and outer spacing. The hyperlink definition allows you to set the font family, size, color, and text styles.

> [!NOTE]
> The form styles are constantly being improved. Forms created in an older version of real-time journeys form editor have limited options to change the form styling using the theme feature. You can enable more style options by selecting the **Enable** button in the theme section. This updates your form styles to the latest version compatible with the theme feature.

### Custom fonts

There are two ways to use custom fonts in your form:

1. Set the font to "inherit": Recommended for forms **embedded** into your own page. The form inherits the form from your page.
1. Add your own custom font: Recommended for forms **hosted as standalone page**. You can upload your custom font using the theme feature in the custom fonts section. Your uploaded custom fonts can be then used in all text style definitions.

### Preview: Copilot - Forms theme assistant

> [!IMPORTANT]
> A preview feature is a feature that is not complete but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

> [!IMPORTANT]
> You must only use the theme assistant with websites that you own and operate. The theme assistant should not be used to copy third-party websites.

The theme assistant is a Copilot feature in Customer Insights - Journeys. You can use the theme assistant to fetch styles from an existing website that you own and control. To use a theme, enter the website URL and select **Fetch styles**. This process might take a few minutes. You can continue your work and return back later to check the result. Once the assistant fetches the styles from your website, it applies the styles to the theme of your form.

:::image type="content" source="media/real-time-marketing-form-theme-copilot.png" alt-text="Fetch styles from your website using Copilot." lightbox="media/real-time-marketing-form-theme-copilot.png":::

## Parent contact for lead

The **Lead & Contact** audience allows you to update a lead and contact entity with a single form submission. You can change the audience using the picker in the top right corner of the form editor.

To use a combined Lead & Contact audience, it's important to [define how the attributes are mapped to each other](real-time-marketing-form-global-settings.md#lead-contact-mapping). For example, you need to link the contact *First Name* attribute to the lead *First Name* attribute, so the form field *First Name* can update attributes for both entities.

Once you select the *Lead & Contact* audience, you see three sections of fields in the right pane:

:::image type="content" source="media/real-time-marketing-form-lead-contact.png" alt-text="Lead & Contact audience." lightbox="media/real-time-marketing-form-lead-contact.png":::

The fields in the *Contact* section update only the corresponding contact attributes. The fields in the *Lead* section update only the corresponding lead attributes. If you want the field to update both lead and contact attributes, use a field from the *Lead & Contact* section. If the *Lead & Contact* section is empty, you have to [define attribute mapping](real-time-marketing-form-global-settings.md#lead-contact-mapping).

Once the form using the *Lead & Contact* audience is submitted, two interactions are produced: one for a contact and one for a lead. Therefore, you can see the form submission on both the lead timeline and the contact timeline. 

When creating a new journey using the *Marketing form submitted* trigger, you can choose whether the journey is executed for a lead or for a contact. Your journey uses the interaction you choose for the trigger (contact or lead). The journey can only have a single audience: contact *or* lead.

## Form settings

Form settings allow you to configure advanced properties of your form and define what happens after the form submission.

:::image type="content" source="media/real-time-marketing-form-settings.png" alt-text="Form settings." lightbox="media/real-time-marketing-form-settings.png":::

- **Form template**: Select a template for your form. Selecting a template erases all content in your form.
- **Prefill**: Enable [Form Prefill](real-time-marketing-form-prefill.md) for all fields in your form.
- **Web tracking**: Enable [web tracking](interaction-journey-decision.md) of users submitting the form by adding a [tracking cookie](real-time-journeys-cookies.md) containing the form submission ID to their browser. If enabled, the form loader script is automatically enriched with the web tracking script, which produces the tracking cookie. Make sure you inform the users about cookie usage according to your privacy regulations.
- **Audience**: Define [how to handle duplicate records](real-time-marketing-manage-forms.md#how-to-handle-duplicate-records) by selecting the [matching rule](real-time-marketing-matching-rules.md). Configure whether the form submission can create new records or update existing records. If *Update matched contact with submitted data* and *Create a new contact if there was no match to an existing one?* are set to **No**, the form submission doesn't update or create any record. The form submission can be linked to an existing record identified by the matching rule.
- **Post submission action**: Set whether the *Thank you notification* is displayed or the user is redirected to a different page once the form is submitted. The *Thank you notification* is shown for a few seconds even if *Redirect after submission* is selected.
- **Thank you notification**: This message appears if the user successfully submits the form.
- **Error notification**: This message appears if an error occurs when the form is submitted.
- **Double opt-in**: If enabled, the [double opt-in](real-time-marketing-double-opt-in.md) email can be sent after the form submission. To enable double opt-in for your form, a double opt-in-enabled compliance profile is required

## How to handle duplicate records

The default approach to duplicate records is different for contact and lead entities.

- **Contact (default: Update contact using email)**: If the user submits a form with an existing email address, the form submission updates the existing record. There's no new record created.
- **Lead (default: Always create a new record)**: If the user submits a form with an existing email address, a new record with the same email address is created.
- **Lead & Contact (default: Update contact using email and always create a new lead)**: If the user submits a form with an existing email address, the form submission updates the existing contact and creates a new lead.

You can change the default matching rule using the **Duplicate records** drop-down in the **Forms** settings. You can also create a [custom matching rule](real-time-marketing-manage-forms.md#create-a-custom-matching-rule).

### Create a custom matching rule

A custom matching rule allows you to specify criteria for identifying existing leads or contacts. This prevents creating duplicate records. For more information, see [Create custom matching rules](real-time-marketing-matching-rules.md).

## Field types

Field types and formats are defined by the attribute metadata. It isn't possible to change field types and formats. You can, however, change the rendering control for field types where the format isn't defined.

| **Type**  | **Format** | **Rendering control** | **Description**|
|-----------|------------|-----------------------|----------------|
| Single line of text    | Email, Text, URL, Phone, Number         | Automatically set based on the format               | Simple input field. Validation is automatically set based on the format.                                |
| Multiple lines of text    | Text Area     | Text Area             | Text area input field that accepts all types of text values.                                |
| Option set             | n/a           | Radio Buttons         | Field with a limited number of predefined values (as defined in the database). Rendered as a set of radio buttons, with one button for each value.                                  |
| Option set             | n/a           | Drop-down              | Field with a limited number of predefined values (as defined in the database). Rendered as a drop-down list for selecting a value.                                                  |
| Two options            | n/a           | Check box              | Boolean field, which accepts a value of either true or false. It's rendered as a check box, which is selected when true and clear when false.                                              |
| Two options            | n/a           | Radio&nbsp;Buttons         | Field that accepts one of just two possible values (typically true or false). Rendered as a pair of radio buttons, with the display text for each defined in the database.           |
| Date and time          | Date Only     | Date Picker           | Date picker to select a date from a pop-up calendar display. It doesn't accept a time.                                                                           |
| Date and time          | Date and Time | Date-Time Picker      | Date and time picker to select a date from a pop-up calendar and a time from a drop-down list.                                                                   |
| Lookup field          | n/a | Lookup      | A lookup field is linked to a particular entity type, enabling you to add a drop-down list of options that were created in advance to your form. [More information](#lookup-fields). |

The **File** field type isn't supported in forms.

### Phone number field

For the best results with Customer Insight - Journeys, you should only use the international phone number format starting with a "+" sign. This ensures that consent to send text messages can be collected. To improve your customers' experience, we recommend using the phone number label or placeholder to explain the expected format of phone number.

Make sure that the phone number field validation is set to **Phone number**. This out-of-the-box validation checks if the phone number format is compatible with the phone number format requirements for contact point consent creation. The expected phone number format is the international one starting with a "+" sign. If your customer enters a wrong value for the phone number, the default error message generated by the browser is displayed. The forms use the default browser validation to show error messages if the entered field value doesn't match the expected pattern. You can override the default browser validation with custom JavaScript to introduce your own error messages.

If you don't plan to use the phone number for sending text messages, you can collect the phone number in any format. In such a case, you should avoid adding consent for the "Text" channel to the form. Contact point consent strictly requires the international phone number format. If an incompatible format is used, the form submission is processed with a warning about failure when trying to create contact point consent for the entered phone number.

> [!NOTE]
> If the form submission for a form containing a phone number field fails, upgrade your application to the latest version to get the latest fixes and improvements to the phone number format processing.

#### Pre-set phone number country code

If your business is located in a single region with the same phone number country code, you can pre-set the *Country code* parameter of the phone number field.

:::image type="content" source="media/real-time-marketing-form-country-code.png" alt-text="Set the country code for phone number." lightbox="media/real-time-marketing-form-country-code.png":::

If the country code is pre-set, the correct phone number country code is automatically added once the form is submitted. If the customer enters a phone number including the country code, the pre-set phone number country code is ignored.

### Lookup fields

A lookup field is linked to a particular entity type, enabling you to add a drop-down list of options that were created in advance to your form. For example, you could use a lookup field called "Currency" to show a drop-down list of all currencies in your form.

After adding a lookup field, or if your lookup field isn't working, ensure that the service user used has permissions to configure the entities you're using with the lookup field. The Marketing Services User Extensible role used by the form editor needs to have read access to the entity used in the lookup field. You also have to enable **Make lookup data publicly viewable** in the lookup properties. All values within the lookup are available to anyone who sees the form. Ensure that sensitive data isn't exposed to the public. More information: [Adding lookup fields](marketing-fields.md#adding-lookup-fields-and-troubleshooting).

### Custom mapped fields

The form editor allows you to use all attributes of lead or contact entities as form fields. If you create a new custom attribute of a contact or lead entity, it's automatically available as a form field in the editor. Using this approach, you can easily create reusable form fields.

> [!NOTE]
> The custom **unmapped** form fields (form fields not linked to any existing lead or contact attribute) are currently on our roadmap. There's a possible workaround mentioned in this [blog post](https://community.dynamics.com/blogs/post/?postid=3a361b7e-80b0-ee11-92bd-002248527d3d).

## Form validation

The validation process is automatically launched once a *draft* form is published or once a *live, editing* form is saved. The validation checks the form's content and can stop publishing if blocking **errors** are found or it can show **warnings** about potential issues.

You can launch the form validation process manually using the **Check content** button.

### Errors that block form publishing

The following conditions prevent forms from being published and display an error message:

- Is a **Submit** button included?
- Are the form fields linked to an editable attribute?
- Does the form contain duplicated fields?
- Does the form include all attributes required by the matching rule (email field by default)?
- Is the target audience set?

### Warnings that don't stop form publishing

The following conditions don't prevent forms from being published. A warning message is displayed:

- Does the form include all fields linked to attributes of a selected entity that are mandatory to create or update a record?
- Are all required attributes labeled as required="required" in HTML?

## Form submission processing

Once the form is submitted, the submitted values can be found in the **Submissions** section of the form editor. It may take up to a few minutes before the entities targeted by the form are updated and the submission moves from a *Pending* to a *Success* state.

The following contact or lead attributes are automatically updated by the form submission only if a new record is created:

- msdynmkt_emailid
- msdynmkt_customerjourneyid
- msdynmkt_marketingformid
- ownerid
- owningbusinessunit (if the business units feature is enabled)
- subject (only for leads) - the form name is used as the value

The above-listed attributes aren't updated when an existing record is updated with a form submission.

## Advanced form customization

To open the HTML editor and display the source code of a form, select the **HTML button** in the top right corner.

- Customer Insights - Journeys forms can be [rendered using JavaScript API](./developer/realtime-marketing-form-client-side-extensibility.md#rendering-a-marketing-form-using-a-javascript-api), allowing you to load the form dynamically.
- You can [inject a marketing form into a react application](./developer/realtime-marketing-form-client-side-extensibility.md#injecting-a-marketing-form-into-a-react-application).
- It's also possible to [extend form events](./developer/realtime-marketing-form-client-side-extensibility.md#custom-events) like formLoad, formSubmit, etc.
- There are other possibilities to customize your forms. [Learn more](./developer/realtime-marketing-form-client-side-extensibility.md)

### Customize form CSS

You can change the CSS class definitions in the HTML editor. Editing CSS allows you to achieve more advanced design customizations on top of the possibilities in the form editor.

### Add custom JavaScript to your form

> [!IMPORTANT]
> With Customer Insights - Journeys version **1.1.38813.80 or newer**, you can add JavaScript code into the `<body>` section of the HTML. If you add JavaScript into `<head>` section, it's automatically moved to the top of the `<body>` section. The `<script>` tag is automatically renamed `<safe-script>` to prevent script execution in the form editor. The `<safe-script>` tag is then automatically renamed back to `<script>` in the final form HTML served by the formLoader script.

> [!IMPORTANT]
> With Customer Insights - Journeys version **older than 1.1.38813.80**, you can add custom JavaScript code only to the `<head>` section of the HTML source code using the HTML editor. If the code JavaScript code is placed inside the `<body>` section, the form editor automatically removes the code without warning.

All `onEvent` HTML attributes triggering execution of JavaScript code like `onClick` or `onChange` are automatically sanitized (removed from the code).

The following example is **not supported**:

```html
<button onClick="runMyFunction()">
```

As shown in the examples below, you can place the EventListeners inside the JavaScript code to trigger the execution of JavaScript functions.

#### Example 1: Update the value of the form field using values of other form fields

In this example, a script is created that combines the first name and last name field values into the full name.

```js
<script>
    const firstName = document.getElementById("firstname-1679394382894"); // The field ID is unique in each form, make sure you replace it with the correct value.
    const lastName = document.getElementById("lastname-1679335991544"); // The field ID is unique in each form, make sure you replace it with the correct value.
    const fullName = document.getElementById("fullname-1679394390062"); // The field ID is unique in each form, make sure you replace it with the correct value.

    firstName.addEventListener('change', updateFullName);
    lastName.addEventListener('change', updateFullName);

    function updateFullName() {
    fullName.value = firstName.value + ' ' + lastName.value;
    }
</script>
```

#### Example 2: Populate a hidden field with a UTM parameter value from a URL

[UTM sources](real-time-marketing-utm.md) provide important information on where your new leads are coming from. This example script extracts the UTM source parameter from a URL and populates it into the value of a hidden field.

1. Create a new custom attribute of your lead entity called "UTM source" with the logical name `utmsource`.
1. Create a new form with "lead" as the target audience. You can see the custom attribute "UTM source" in the list of fields.
1. Add the UTM source field to the canvas and set it as hidden in the field properties.
1. Open the HTML editor.
1. Put the following script in the body section. Make sure you put the correct field ID into the code.

```js
<script>
    document.addEventListener("d365mkt-afterformload", updateUTMSourceField());
            
    function updateUTMSourceField() {
        const formField = document.getElementById("utmsource-1679335998029"); // The field ID is unique in each form, make sure you replace it with the correct value.        
        const urlParams = new URLSearchParams(window.location.search);
        const utmSource = urlParams.get('utm_source');
        formField.value = utmSource;
        console.log(utmSource); // for debug only, can be removed
    }
</script>
```

You can reuse this example to enrich your leads with more UTM parameters like utm_campaign, utm_medium, utm_term, utm_content.

### Customize the form and form submission entities

You can [add custom attributes to the form or form submission entities](real-time-marketing-customize-forms.md) to enhance your experience with the form editor.

### Integrate a custom captcha into the form

You can [integrate custom captcha](real-time-marketing-form-custom-captcha.md) bot protection services like [Google reCAPTCHA](https://www.google.com/recaptcha/about/) into your form.

### Custom back-end validation of form submission

It's possible to build [custom back-end form submission validation](real-time-marketing-form-customize-submission-validation.md) that prevents or extends form submission processing.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
