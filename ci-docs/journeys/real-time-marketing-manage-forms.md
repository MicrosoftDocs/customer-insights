---
title: Manage Customer Insights - Journeys forms
description: Discover how to manage and style forms in Dynamics 365 Customer Insights - Journeys. Edit, unpublish, and customize forms with ease. Learn more now!
ms.date: 08/26/2025
ms.update-cycle: 180-days
ms.topic: how-to
author: petrjantac
ms.author: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Manage Customer Insights - Journeys forms

This article explains how to edit, unpublish, and manage forms in Customer Insights - Journeys.

## Edit a live form

If your form is already published and you need to update it, select the **Edit** button on the top ribbon. Continue editing your live form. All changes are automatically published when you select the **Save** button.

> [!IMPORTANT]
> If you choose to create a copy of the form, you must publish the new copy.

The form is stored on a content delivery network (CDN), which caches data to provide the fastest loading times for your webpage visitors. It can take up to 10 minutes for the cache to refresh and for you to see changes on your webpage. To check your changes immediately, add the `#d365mkt-nocache` parameter to your webpage URL. Don't share links with this parameter with your customers, because it bypasses the CDN cache and slows down page loading.

## Unpublish a form

To unpublish a live form, select the **Stop** button. The form is removed from the CDN, so your web page visitors can't submit it. The form might still appear because of the browser cache, but it can't be submitted. The form status changes to *Draft*.

## Form field properties

When you select a field on the canvas, its properties show in the right pane.

:::image type="content" source="media/real-time-marketing-form-properties.png" alt-text="Screenshot of the field properties pane that appears after you add a field to the form." lightbox="media/real-time-marketing-form-properties.png":::

- **Placeholder text**: The placeholder inside the field. The placeholder disappears when the user starts typing in the field.
- **Default value**: Set the default value for this field. The placeholder isn't visible if the default value is set.
- **Required**: If enabled, the user can't submit the form if this field is empty.
- **Validation**: Set a rule that checks the content of the field. If the validation rule isn't met, the user can't submit the form. It's important to set the right validation for email, phone number, and similar fields.
- **Hide field**: If enabled, the field isn't visible in the form. Use hidden fields to store extra metadata with the form submission.

### Custom validation

To create custom validation, turn on the **Validation** option and select **Custom**. A pop-up dialog shows where you enter a regular expression (RegExp). For example, use a RegExp to check if the entered value matches a specific phone number format.

## Style your forms using Theme

Open the **Theme** section by selecting the brush icon in the right pane. Theme controls the style of all types of fields, buttons, and text. When you set the theme of a field, it affects all fields of the same type in your form.

The theme feature lets you edit CSS class definitions in the form HTML through a user-friendly interface. It works only with out-of-the-box form styles. Custom CSS classes aren't visualized, but you can edit your custom CSS classes using the HTML code editor.

:::image type="content" source="media/real-time-marketing-form-theme.png" alt-text="Screenshot of the Theme section where you edit the style of an input field in a form." lightbox="media/real-time-marketing-form-theme.png":::

The **Theme** section lets you configure:

- **Background**: Set the inner background color and border style for the whole form.
- **Text styles**: Set Heading 1, Heading 2, Heading 3, paragraph, and field label styles. The field label style doesn't affect checkbox and radio button labels because you set these labels separately. The text style definition includes font family, font size, font color, text style, and line height. You can also set the inner and outer spacing, width, and alignment. In addition to these text styles, you can set the label position (top, left, right) and the required color for your field labels.
- **Input fields** are grouped into three categories:
  1. Text input, dropdown, and lookup fields: These three field types share the same style definition. Set the font family, size, color, and style for placeholder and input text styles. You can also set the field background color, menu background color, rounded corners, border, size alignment, and inner and outer spacing. Set the field label in text styles.
  1. Radio button: The radio button has its own label configuration, so you set the font family and size. Set the text color, styles, and background color for all options and for the selected option. You can also set rounded corners, width, and inner and outer spacing of your radio buttons.
  1. Checkbox: The checkbox field has its own label configuration, so you set the font family and size. Set different text color, styles, and background color for all options and for the selected option. You can also set rounded corners, width, and inner and outer spacing of your checkboxes.
- **Buttons and links**: Set the font family, size, color, text styles, button color, border alignment, and inner and outer spacing for buttons. Set the font family, size, color, and text styles for hyperlinks.

> [!NOTE]
> Form styles are constantly improving. Forms created in an older version of the real-time journeys form editor have limited options to change form styling using the theme feature. Get more style options by selecting the **Enable** button in the theme section. This updates your form styles to the latest version compatible with the theme feature.

### Custom fonts

Use custom fonts in your form in two ways:

1. Set the font to "inherit": This option is best for forms **embedded** into your own page. The form inherits the font from your page.
1. Add your own custom font: This option is best for forms **hosted as a standalone page**. Upload your custom font using the theme feature in the custom fonts section. You can use your uploaded custom fonts in all text style definitions.

## Parent contact for lead

The **Lead & Contact** audience lets you update a lead and contact entity with a single form submission. Change the audience by using the picker in the top-right corner of the form editor.

To use a combined Lead & Contact audience, [define how the attributes are mapped to each other](real-time-marketing-form-global-settings.md#lead-contact-mapping). For example, link the contact *First Name* attribute to the lead *First Name* attribute, so the form field *First Name* updates attributes for both entities.

After you select the *Lead & Contact* audience, you see three sections of fields in the right pane.

:::image type="content" source="media/real-time-marketing-form-lead-contact.png" alt-text="Lead & Contact audience." lightbox="media/real-time-marketing-form-lead-contact.png":::

Fields in the *Contact* section update only the corresponding contact attributes. Fields in the *Lead* section update only the corresponding lead attributes. To update both lead and contact attributes, use a field from the *Lead & Contact* section. If the *Lead & Contact* section is empty, [define attribute mapping](real-time-marketing-form-global-settings.md#lead-contact-mapping).

When you submit a form using the *Lead & Contact* audience, two interactions are produced: one for a contact and one for a lead. You see the form submission on both the lead timeline and the contact timeline.

When you create a new journey using the *Marketing form submitted* trigger, choose whether the journey runs for a lead or a contact. The journey uses the interaction you choose for the trigger (contact or lead). The journey can have only a single audience: contact or lead.

## Form settings

Form settings let you set advanced properties for your form and define what happens after form submission.

:::image type="content" source="media/real-time-marketing-form-settings.png" alt-text="Screenshot of the form settings page in real-time marketing, showing available configuration options." lightbox="media/real-time-marketing-form-settings.png":::

- **Form template**: Select a template for your form. When you select a template, all content in your form is deleted.
- **Prefill**: [Form Prefill](real-time-marketing-form-prefill.md) fills all fields in your form.
- **Web tracking**: [Web tracking](interaction-journey-decision.md) adds a [tracking cookie](real-time-journeys-cookies.md) with the form submission ID to the user's browser when they submit the form. If enabled, the form loader script automatically includes the web tracking script, which creates the tracking cookie. Tell users about cookie usage according to your privacy regulations.
- **Audience**: Set [how to handle duplicate records](real-time-marketing-manage-forms.md#how-to-handle-duplicate-records) by selecting the [matching rule](real-time-marketing-matching-rules.md). Choose whether form submission creates new records or updates existing records. If *Update matched contact with submitted data* and *Create a new contact if there was no match to an existing one?* are set to **No**, the form submission doesn't update or create any record. The form submission can link to an existing record identified by the matching rule. To make sure that existing values aren't overwritten by submitted empty values, enable the [Ignore empty values toggle](#ignore-empty-values).
- **Post submission action**: Choose whether to show the *Thank you notification* or redirect the user to a different page after form submission. The *Thank you notification* appears for a few seconds, even if *Redirect after submission* is selected.
- **Thank you notification**: This message appears when the user submits the form successfully.
- **Error notification**: This message appears if an error occurs during form submission.
- **Double opt-in**: If enabled, the [double opt-in](real-time-marketing-double-opt-in.md) email is sent after form submission. To use double opt-in for your form, you need a compliance profile with double opt-in turned on.

## How to handle duplicate records

The default approach to duplicate records is different for contact and lead entities.

- **Contact (default: Update contact using email)**: When a user submits a form with an existing email address, the form updates the existing record and doesn't create a new record.
- **Lead (default: Always create a new record)**: When a user submits a form with an existing email address, the form creates a new record with the same email address.
- **Lead & Contact (default: Update contact using email and always create a new lead)**: When a user submits a form with an existing email address, the form updates the existing contact and creates a new lead.

Change the default matching rule by using the **Duplicate records** drop-down in the **Forms** settings. To learn how to create a custom rule, see [custom matching rule](real-time-marketing-manage-forms.md#create-a-custom-matching-rule).

### Create a custom matching rule

A custom matching rule lets you set criteria for identifying existing leads or contacts. This approach helps prevent duplicate records. For more information, see [Create custom matching rules](real-time-marketing-matching-rules.md).

### Ignore empty values

Use the **Ignore empty values** toggle to control whether empty form fields overwrite existing data. If a form is submitted with an empty field (like phone number), this setting determines whether the existing value stays or is cleared.

- **Toggle off (disabled)**: The existing value is overwritten by the empty input.
- **Toggle on (enabled)**: The existing value stays and isn't replaced by the empty input.

**Example**: A contact has a phone number saved. When a form is submitted with the phone number field left blank:

- If the toggle is **disabled**, the phone number is erased.
- If the toggle is **enabled**, the phone number stays the same.

## Field types

Attribute metadata defines field types and formats. You can't change field types or formats, but you can change the rendering control for field types when the format isn't defined.

| **Type**  | **Format** | **Rendering control** | **Description**|
|-----------|------------|-----------------------|----------------|
| Single line of text    | Email, Text, URL, Number         | Automatically set based on the format.               | Simple input field. Validation is automatically set based on the format.                                |
| [Phone number](#phone-number-field)    | Phone number         | Can be extended with the preset country code.               | Simple input field. Validation is set to phone number by default.                                |
| Multiple lines of text    | Text Area     | Text Area             | Text area input field that accepts all types of text values.                                |
| Option set             | n/a           | Radio Buttons         | Field with a limited number of predefined values (as defined in the database). Rendered as a set of radio buttons, with one button for each value.                                  |
| Option set             | n/a           | Drop-down              | Field with a limited number of predefined values (as defined in the database). Rendered as a drop-down list for selecting a value.                                                  |
| Two options            | n/a           | Check box              | Boolean field that accepts a value of either true or false. It's rendered as a check box, which is selected when true and clear when false.                                              |
| Two options            | n/a           | Radio&nbsp;Buttons         | Field that accepts one of two possible values (typically true or false). Rendered as a pair of radio buttons, with the display text for each defined in the database.           |
| Date and time          | Date Only     | Date Picker           | Date picker to select a date from a pop-up calendar display. It doesn't accept a time.                                                                           |
| Date and time          | Date and Time | Date-Time Picker      | Date and time picker to select a date from a pop-up calendar and a time from a drop-down list.                                                                   |
| [Lookup field](#lookup-fields)          | n/a | Lookup      | A lookup field is linked to a particular entity type, enabling you to add a drop-down list of options to your form that were created in advance. |

> [!NOTE]
> **File** and **Customer** field types aren't supported in forms.

### Phone number field

For the best results with Customer Insight - Journeys, use the international phone number format starting with a "+" sign. This format lets you collect consent to send text messages. To improve your customer's experience, use the phone number label or placeholder to explain the expected phone number format.

Set the phone number field validation to **Phone number**. This built-in validation checks if the phone number format meets the requirements for contact point consent creation. The expected format is international, starting with a "+" sign. If your customer enters an invalid phone number, the browser shows the default error message. The forms use the browser's default validation to show error messages if the entered value doesn't match the expected pattern. You can override the default browser validation with custom JavaScript to show your own error messages.

If you don't plan to use the phone number for sending text messages, collect the phone number in any format. In this case, avoid adding consent for the "Text" channel to the form. Contact point consent requires the international phone number format. If the format isn't compatible, the form submission is processed with a warning about the failure to create contact point consent for the entered phone number.

> [!NOTE]
> If the form submission for a form containing a phone number field fails, upgrade your application to the latest version to get the latest fixes and improvements to the phone number format processing.

#### Preset phone number country code

If your business is in a single region with the same phone number country code, preset the *Country code* parameter of the phone number field.

:::image type="content" source="media/real-time-marketing-form-country-code.png" alt-text="Set the country code for phone number." lightbox="media/real-time-marketing-form-country-code.png":::

If the country code is preset, the correct phone number country code is automatically added when the form is submitted. If the customer enters a phone number that includes the country code, the preset country code is ignored.

### Lookup fields

A lookup field links to a particular entity and lets you add a drop-down list of options to your form that you create in advance. For example, use a lookup field called "Currency" to show a drop-down list of all currencies in your form. Set the default value of the lookup field if needed.

> [!IMPORTANT]
> After adding a lookup field, or if your lookup field isn't working, ensure that the **Marketing Services User Extensible** role has **Read** permission to access the entity records and views or filters you're using with the lookup field.

> [!WARNING]
> All values within the lookup are available to anyone who sees the form. The lookup field can display all entity records regardless of the business unit. Ensure that sensitive data isn't exposed to the public. If you're sure that the lookup contains only publicly shareable data, enable **Make lookup data publicly viewable** in the lookup properties.

Improperly configured field-level security can prevent lookup fields from working correctly. Make sure field-level security is set up appropriately.

#### Filter a lookup field values based on an answer in a previous lookup field (cascading lookup fields)

The **Filter value** feature lets you to filter the choices in a lookup field based on the user's selection in a previous lookup field, creating a more intuitive and efficient form experience. This dynamic filtering reduces clutter and confusion by showing only relevant options, helping users complete forms faster and with fewer errors. For example, when selecting a city, users only see cities that match the country they previously selected, eliminating the need to scroll through irrelevant entries. This leads to higher quality submissions and lowers the risk of form abandonment.

##### Set up value filtering for a lookup field

A lookup field represents data from an existing table. Filtering between lookup fields relies on a defined relationship between those tables. If no relationship exists, filtering options aren't available. When multiple relationships are defined between the same tables, the form editor allows you to select the appropriate relationship to use for filtering. This ensures that the dependent field displays only relevant values based on the user's selection in the preceding field.

When your form includes two lookup fields, a **Filter values** button becomes available in the form editor.

:::image type="content" source="media/real-time-marketing-form-filter-values.png" alt-text="Set up value filtering." lightbox="media/real-time-marketing-form-filter-values.png":::

Selecting the **Filter values** button opens a pop-up window where you can configure how the filtering works between lookup fields. In this window, you can specify which lookup field serves as the input for filtering and select the appropriate relationship between the underlying data tables. Once the filtering rule is configured, the field in the form editor changes its highlight from blue to purple, indicating that a filtering relationship has been successfully applied.

The lookup fields for country and city aren't included by default. To add them to your form, refer to this [step-by-step guide that shows how to create a filtered list of cities based on the selected country](real-time-marketing-filter-cities-by-country.md). The guide also offers general guidance on how to define custom lookup fields (entities) and establish relationships between them. This approach can be applied to any scenario where field options need to be dynamically filtered based on prior selections.

Lookup fields also support a JavaScript API, enabling developers to [programmatically set a lookup field value](developer/realtime-marketing-form-client-side-extensibility.md#select-a-lookup-field-value-using-javascript) or apply dynamic filters based on user input. This allows for advanced customization and seamless integration with other form logic.

### Custom mapped fields

The form editor lets you use all attributes of lead or contact entities as form fields. If you create a new custom attribute for a contact or lead entity, it's automatically available as a form field in the editor. This approach lets you easily create reusable form fields.

> [!NOTE]
> The custom **unmapped** form fields (form fields not linked to any existing lead or contact attribute) are currently on our roadmap. There's a possible workaround mentioned in this [blog post](https://community.dynamics.com/blogs/post/?postid=3a361b7e-80b0-ee11-92bd-002248527d3d).

## Form validation

The validation process starts automatically when you publish a *draft* form or save a *live, editing* form. Validation checks the form's content and stops publishing if it finds blocking **errors**, or shows **warnings** for potential issues.

To start validation manually, select **Check content**.

### Errors that block form publishing

These conditions prevent the form from being published and show an error message:

- The form includes a **Submit** button.
- All form fields are linked to an editable attribute.
- The form doesn't have any duplicated fields.
- The form includes all attributes required by the matching rule (email field by default).
- The target audience is set.

### Warnings that don't stop form publishing

These conditions don't prevent the form from being published, but a warning message appears:

- Does the form include all fields linked to attributes of a selected entity that are required to create or update a record?
- Are all required attributes labeled as required="required" in HTML?

## Form submission processing

After you submit the form, you see the submitted values in the **Submissions** section of the form editor. It can take a few minutes for the entities targeted by the form to update, and for the submission to move from a *Pending* to a *Success* state.

The following contact or lead attributes update automatically when the form creates a new record.

- msdynmkt_emailid
- msdynmkt_customerjourneyid
- msdynmkt_marketingformid
- ownerid
- owningbusinessunit (if the business units feature is enabled)
- subject (only for leads)—the form name is used as the value

These attributes don't update when a form submission updates an existing record.

## Advanced form customization

To open the HTML editor and show the source code of a form, select the **HTML button** in the top right corner.

- Customer Insights - Journeys forms can be [rendered using JavaScript API](./developer/realtime-marketing-form-client-side-extensibility.md#rendering-a-marketing-form-using-a-javascript-api), so you can load the form dynamically.
- [Inject a marketing form into a react application](./developer/realtime-marketing-form-client-side-extensibility.md#injecting-a-marketing-form-into-a-react-application).
- [Extend form events](./developer/realtime-marketing-form-client-side-extensibility.md#custom-events) like formLoad, formSubmit, and more.
- Find other ways to customize your forms. [Learn more](./developer/realtime-marketing-form-client-side-extensibility.md)

### Customize form CSS

You can change the CSS class definitions in the HTML editor. Editing CSS allows you to achieve more advanced design customizations on top of the possibilities in the form editor.

### Add custom JavaScript to your form

> [!IMPORTANT]
> With Customer Insights - Journeys version **1.1.38813.80 or newer**, you can add JavaScript code into the `<body>` section of the HTML. If you add JavaScript into `<head>` section, it's automatically moved to the top of the `<body>` section. The `<script>` tag is automatically renamed `<safe-script>` to prevent script execution in the form editor. The `<safe-script>` tag is then automatically renamed back to `<script>` in the final form HTML served by the formLoader script.

> [!IMPORTANT]
> With Customer Insights - Journeys version **older than 1.1.38813.80**, you can add custom JavaScript code only to the `<head>` section of the HTML source code using the HTML editor. If the code JavaScript code is placed inside the `<body>` section, the form editor automatically removes the code without warning.

All `onEvent` HTML attributes that trigger JavaScript code, like `onClick` or `onChange`, are automatically sanitized (removed from the code).

The following example is **not supported**:

```html
<button onClick="runMyFunction()">
```

As shown in the examples below, place the EventListeners inside the JavaScript code to trigger JavaScript functions.

#### Example 1: Update the value of a form field using values from other form fields

This example shows a script that combines the first name and last name field values into the full name.

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

#### Example 2: Populate a hidden field with a UTM parameter value from the URL

[UTM sources](real-time-marketing-utm.md) give important information about where your new leads come from. This example script extracts the UTM source parameter from a URL and puts it in a hidden field.

1. Create a new custom attribute of your lead entity called "UTM source" with the logical name `utmsource`.
1. Create a new form with "lead" as the target audience. The custom attribute "UTM source" appears in the list of fields.
1. Add the UTM source field to the canvas and set it as hidden in the field properties.
1. Open the HTML editor.
1. Add the following script in the body section. Replace the field ID with the correct value for your form.

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

Reuse this example to enrich your leads with more UTM parameters like utm_campaign, utm_medium, utm_term, and utm_content.

### Customize the form and form submission entities

[Add custom attributes to the form or form submission entities](real-time-marketing-customize-forms.md) to enhance your experience with the form editor.

### Integrate a custom captcha into the form

You can [integrate custom captcha](real-time-marketing-form-custom-captcha.md) bot protection services like [Google reCAPTCHA](https://www.google.com/recaptcha/about/) into your form.

### Custom back-end validation of form submission

It's possible to build [custom back-end form submission validation](real-time-marketing-form-customize-submission-validation.md) that prevents or extends form submission processing.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
