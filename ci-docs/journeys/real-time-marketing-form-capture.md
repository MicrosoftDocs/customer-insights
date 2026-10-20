---
title: Set up form capture in Customer Insights - Journeys
description: Use form capture in Customer Insights - Journeys to collect submissions from existing website forms. Learn to configure scripts, field mappings, and consent.
ms.date: 10/20/2026
ms.topic: how-to
author: petrjantac
ms.author: udag
ai-usage: ai-assisted
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Set up form capture in Customer Insights - Journeys

Use form capture in Customer Insights - Journeys to collect submissions from existing website forms while preserving their complex logic or connections to other systems. This article explains how to enable form capture, embed the capture script, and map fields and consent. If you can recreate your existing form in the Customer Insights - Journeys form editor, use the editor instead.

Form capture uses the same API as the standard forms to process submissions. The same [security notice](real-time-marketing-form-security-privacy.md) applies for form capture.

> [!IMPORTANT]
>
> - **Form capture requires developer assistance**. It's always easier to create a form by using the Customer Insights - Journeys form editor and embed it into your existing page.
> - **Form capture requires DynamicsMKT_Forms solution version 1.1.35355 or higher**. When provisioning a trial instance, you won't always have the latest version automatically. Ensure you update Customer Insights - Journeys before attempting form capturing.

## Enable form capture feature switch

The form capture feature is disabled by default. You can enable the *Form capture* toggle in **Settings** > **Feature switches** > **Forms**.
:::image type="content" source="media/real-time-marketing-enable-form-capture.png" alt-text="Screenshot of the Form capture toggle in feature switches.":::

## How form capture works

Form capture mimics submission of a standard Customer Insights - Journeys form. To link submissions of your existing form into Customer Insights - Journeys, you need to create a form by using the Customer Insights - Journeys form editor. After you publish that form, you can get a form capture script, which you need to embed into the web page that contains your existing form. The script includes the definition of existing form fields mapping on attributes of the lead or contact entity. You can see all submissions and analytics inside Customer Insights - Journeys. You can also use this form in journey orchestration with the **Marketing Form Submitted** trigger. This form submission can also create or update Contact Point Consent and related Purposes or Topics.

> [!WARNING]
> In form capture scenarios, form visit events aren't collected for analytics, and web tracking isn't available.

## Set up form capture for existing forms

### Create a form capture script in the Customer Insights - Journeys form editor

1. To create a new capture form script, go to **Customer Insights - Journeys** > **Channels** > **Forms** and select **New** on the command bar.
1. Name the form and choose the right audience. The choice of the target audience is important. The form capture script field-to-attribute mapping is available only for attributes of the chosen target audience (entity).
1. Add all fields you want to map to your existing form fields. Although you define **field** to **attribute** mapping in the form capture code, the contact or lead record isn't updated if the field isn't present in the form created by using the form editor. Adding the correct fields into the form generates placeholders for attribute mapping in the form capture script, making the mapping definition easier.
1. Add consent elements like Purpose or Topic to the form and configure them. To learn more, see [manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md).  

    > [!IMPORTANT]
    > You must define the consent in the form editor. The form capture code snippet ignores changes to consent settings. If you change the purpose, topic, channel, or compliance profile of a consent element after you embed the script, copy the script again. To learn more, see [Update the capture script after you change the marketing form](#update-the-capture-script-after-you-change-the-marketing-form).

1. Publish the form by using the **Publish** button in the top right corner of the screen. Copy the form capture code snippet and embed the code snippet in your web page with the existing form, or hand over the code snippet to your developer. The code snippet already includes a link to documentation to guide your developer.
    :::image type="content" source="media/real-time-marketing-form-capture-copy-script.png" alt-text="Screenshot of the form capture code snippet available after publishing a form.":::

    > [!IMPORTANT]
    > You must enable the domain name where you host your existing form for external form hosting. Otherwise, the form submission isn't captured. To learn more, see [domain authentication](domain-authentication.md).

### Embed the capture script and define field and consent mappings

The code snippet you copied in the previous step is a template and must be adjusted to your specific use case. Replace all elements marked as `***Please fill***` in the generated template and adjust the logic to your scenario.

Send your existing form submission to Customer Insights - Journeys by using a JavaScript API defined in the file `FormCapture.bundle.js` and included in the snippet.

The form capturing setup consists of these steps:

1. Get the reference to the form element on the page.
1. Define the mapping of form fields on fields (entity attributes) in Customer Insights - Journeys.
1. Define the mapping of the consent fields on the consent model in Customer Insights - Journeys.
1. Send the form submission to Customer Insights - Journeys.

#### 1. Get a reference to the form element

To get a reference to the form element, use the `waitForElement` helper function. It also works with dynamically rendered elements and returns a promise that resolves once the element with the given selector is found on the page. For a reference of CSS selectors, see this [documentation](https://www.w3schools.com/cssref/css_selectors.php).

**Example:**

```HTML
<form id="form1">
...
</form>

<script>
d365mktformcapture.waitForElement("#form1").then(form => {
  ...
});
</script>
```

#### 2. Define the mapping of form fields

Map fields in the form to the respective fields (entity attributes) in Customer Insights - Journeys. Define the mapping in the function `d365mktformcapture.serializeForm(form, mappings)`.

**Example:**

```HTML
<form id="form1">
  <p>FirstName: <input type="text" name="firstName"/></p>
</form>

<script>
d365mktformcapture.waitForElement("#form1").then(form => {
  const mappings = [
    {
      FormFieldName: "firstName",
      DataverseFieldName: "firstname",
    },
  ];

  ...
  
  const serializedForm = d365mktformcapture.serializeForm(form, mappings);
  // console.log(JSON.stringify(serializedForm)); // NOTE: enable for debugging
  const payload = serializedForm.SerializedForm.build();
});
</script>
```

The `waitForElement` function described in the previous section retrieves the `form` parameter. The `mappings` parameter is an array with elements of the following structure:

```typescript
export interface IFormFieldMapping {
    FormFieldName?: string; // name of form field
    DataverseFieldName: string; // name of field on Dynamics 365 side
    DataverseFieldValue?: string | IFormValueMapping[]; // optional - either a fixed value or a value mapping
}

export interface IFormValueMapping {
    FormValue: string; // form field value
    DataverseValue: string; // mapped value for that form field value that will be sent to Dynamics 365
}
```

The function is synchronous and returns the serialization result with the following contract:

```typescript
export interface IFormSerializationResult {
    FormFieldMappingResults: IFormFieldMappingResult[]; // Status for each of the defined mappings
    SerializedForm: IFormSerializationBuilder; // The serialized form
}

export interface IFormFieldMappingResult {
    Mapping: IFormFieldMapping; // The defined mapping
    FormFieldMappingStatus: FormFieldMappingStatus; // Status of the mapping (see below for status values)
    Message: string; // Optional - an error/warning message for the mapping
}

export enum FormFieldMappingStatus {
    Success = 0,
    NotFound = 1,
    Error = 2
}
```

Ensure you handle all errors returned by the `FormFieldMappingResults`. Create the payload to Customer Insights - Journeys by calling `serializedForm.SerializedForm.build()`.

##### 2.1 Mapping of OptionSet fields

For `OptionSet` fields, define the mapping to the respective value that should be stored in Customer Insights - Journeys. Map your existing form OptionSet fields values in the `DataverseFieldValue` property.

**Example:**

```HTML
<form id="form1">
  <p>Radio: <input type="radio" name="radioInput" value="option1"/><input type="radio" name="radioInput" value="option2"/></p>
</form>

<script>
  ...
  const mappings = [
    {
        FormFieldName: "radioInput",
        DataverseFieldName: "dvradioInput",
        DataverseFieldValue: [ 
            { FormValue: "option1", DataverseValue: "1" }, 
            { FormValue: "option2", DataverseValue: "2" },
        ]
    },
  ];
  ...
</script>
```

##### 2.2 Mapping of lookup fields

###### Set the default value for the lookup field

Use static (default) values in the mapping logic for lookup fields. Define the name of the field and the value that should be stored in Customer Insights - Journeys.

**Example:**

```HTML
<form id="form1">
  ...
</form>

<script>
  ...
  const mappings = [
    {
        DataverseFieldName: "currency",
        DataverseFieldValue: "{\"Id\":\"ffffd6c1-b32d-ee11-bdf3-6045bded6105\",\"LogicalName\":\"transactioncurrency\"}"
    },
  ];
  ...
</script>
```

###### Map the value of the lookup field to a field in your form

You can also map the lookup field value to a respective value in your existing form field.

**Example:**

```HTML
<form id="form1">
  <p>Radio: <input type="radio" name="currency" value="usd"/><input type="radio" name="currency" value="eur"/></p>
</form>

<script>
  ...
  const mappings = [
    {
        FormFieldName: "currency",
        DataverseFieldName: "transactioncurrencyid",
        DataverseFieldValue: [ 
              { FormValue: "usd", DataverseValue: "{\"Id\":\"cd2cff48-08a3-ea11-a813-000d3a0a82b4\",\"LogicalName\":\"transactioncurrency\"}", }, 
              { FormValue: "eur", DataverseValue: "{\"Id\":\"91f1a052-259c-4719-a3ae-3a1d2987a3ed\",\"LogicalName\":\"transactioncurrency\"}", }, 
        ]
    },
  ];
  ...
</script>
```

##### 2.3 Mapping multi-select field values

For `multi-select` fields, define the mapping to the value that Customer Insights - Journeys should store. Map your existing form `multi-select` field values in the `DataverseFieldValue` property.

**Example:**

```HTML
  <form id="form1">
    <p>Fieldset: <fieldset name="multiOptionInput">
      <input type="checkbox" name="multiOptionInput" value="100000000">0</input>
      <input type="checkbox" name="multiOptionInput" value="100000001">1</input>
      <input type="checkbox" name="multiOptionInput" value="100000002">2</input>
    </fieldset></p>
  </form>
 
<script>
...
const mappings = [
  {
    FormFieldName: "multiOptionInput",
    DataverseFieldName: "dvmultiOptionInput",
    DataverseFieldValue: [
      { FormValue: "100000000", DataverseValue: "0" },
      { FormValue: "100000001", DataverseValue: "1" },
      { FormValue: "100000002", DataverseValue: "2" },
    ]
  },
];
...
</script>
```

#### 3. Define consent field mapping

Configure consent fields in the form editor in Customer Insights - Journeys. The `DataverseFieldName`, `DataverseFieldValue`, `LabelText`, and `ComplianceSettingsId` mappings are autogenerated accordingly:

- `DataverseFieldName` is `msdynmkt_purposeid;channels;optinwhenchecked` for a purpose or `msdynmkt_topicid;channels;optinwhenchecked` for a topic.
- `DataverseFieldValue` contains the purpose or topic ID, the channel or channels, and the opt-in setting, separated by semicolons.
- `LabelText` is the consent label from the form editor. Update it to match the label of the checkbox on your page.
- `ComplianceSettingsId` is the ID of the compliance profile.

Set `FormFieldName` to the `name` attribute of the consent checkbox on your page.

**Example:**

```HTML
<form id="form1">
  <p><label><input type="checkbox" name="consentField"/> Marketing emails</label></p>
</form>

<script>
  ...
  const mappings = [
    {
        FormFieldName: "consentField",
        DataverseFieldName: "msdynmkt_purposeid;channels;optinwhenchecked",
        DataverseFieldValue: "10000000-0000-0000-0000-000000000004;Email;true",
        LabelText: "Marketing emails",
        ComplianceSettingsId: "10000000-0000-0000-0000-000000000005",
    },
  ];
  ...
</script>
```

#### 4. Send the form submission to Customer Insights - Journeys

After you get a reference to the form, define the mappings, and serialize the form, add an event listener to the `submit` event. Use the `d365mktformcapture.submitForm(captureConfig, payload)` function to send the form. This call returns a promise, and you can handle errors in the `catch` logic.

> [!IMPORTANT]
> If you use custom validation or a CAPTCHA check, submit the form to Customer Insights - Journeys only if the validation succeeds. For example, check for `isDefaultPrevented` on the `submit` event or explicitly call `submitForm` only after the validation passes.

**Example:**

```HTML
<form id="form1">
  <p>FirstName: <input type="text" name="firstName"/></p>
</form>

<script>
d365mktformcapture.waitForElement("#form1").then(form => {
  const mappings = [
    {
      FormFieldName: "firstName",
      DataverseFieldName: "firstname",
    },
  ];

  form.addEventListener("submit", (e) => {
    const serializedForm = d365mktformcapture.serializeForm(form, mappings);
    // console.log(JSON.stringify(serializedForm)); // NOTE: enable for debugging
    const payload = serializedForm.SerializedForm.build();

    const captureConfig = {
      FormId: "...", // the form id on Dynamics 365 side
      FormApiUrl: "..." // the API url of the Dynamics 365 backend service where the form will be submitted to
    }
    d365mktformcapture.submitForm(captureConfig, payload)
    .catch(e => {
      // error handling
    });
  }, true);
});
</script>
```

### Update the capture script after you change the marketing form

The capture script contains the consent settings of the saved marketing form at the time you copied the script: the purpose and topic IDs, the channels, the consent label text, and the compliance profile ID. The values in the script on your page, such as the purpose, topic, and compliance profile IDs, don't change when you change the marketing form. If you change the compliance profile, a purpose, or a topic, the script on your page keeps sending the old values, and consent might not be captured correctly. Copy the script again and update your page.

To update the capture script:

1. Go to **Customer Insights - Journeys** > **Channels** > **Forms** and open the marketing form.
1. Select **Edit**, and then select **Continue**. Learn more about how to [edit a live form](real-time-marketing-manage-forms.md#edit-a-live-form).
1. Change the consent elements. For example, select a different **Purpose**.
1. Select **Save**. The marketing form stays live.
1. Select **Publish options**, go to the **Form capture** tab, and then select **Copy**.
1. In the script on your page, replace the `DataverseFieldName`, `DataverseFieldValue`, and `ComplianceSettingsId` values of each consent mapping with the new values. Keep `LabelText` matching the label on your page, and keep your `FormFieldName` values and form selector, because the copied script contains `***Please fill***` placeholders again. If you added or removed consent elements, add or remove the matching mappings.

> [!TIP]
> After the marketing form is live, you can copy the capture script again. Select **Publish options**, and then go to the **Form capture** tab.

## Set a logical name for an unmapped field in form capture

Form capture supports [unmapped fields](real-time-marketing-forms-custom-fields.md), allowing you to assign a logical field name even when the form field does not correspond to an existing mapped field. To do this, specify the DataverseFieldName property in the form capture mapping. This value defines the logical name that will be used for the unmapped field during processing, provided it does not conflict with any existing mapped field names.

```HTML
<script>
const mappings = [
  {
    FormFieldName: "customFieldInForm",
    DataverseFieldName: "MyUnmappedField"
  }
];
</script>
```

## Troubleshooting

### The call to the submission endpoint fails with a CORS error

Cross-Origin Resource Sharing (CORS) can cause form submission capture to fail. Enable your domain for external form hosting. Learn more about [domain authentication](domain-authentication.md).

### Consent values aren't updated correctly

Ensure you [set up the respective consent fields in the form editor](#create-a-form-capture-script-in-the-customer-insights---journeys-form-editor) and use the correct mappings generated in the publishing process.

If you change the compliance profile, a purpose, or a topic on the marketing form after you add the script to your page, the consent values in the script on your page become outdated. Copy the script again and update the consent mappings on your page. Learn more in [Update the capture script after you change the marketing form](#update-the-capture-script-after-you-change-the-marketing-form).

When a form submission triggers an immediate page redirect, the browser might cancel pending network requests including the form‑capture call. This behavior results in the submission not being recorded. To avoid this behavior, ensure your code controls the navigation flow. Use `event.preventDefault()` to stop the browser’s default submission behavior so your handler can run. Then, initiate the redirect only after the `d365mktformcapture.submitForm()` promise completes.
