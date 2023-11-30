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

The code snippet copied in the previous step serves as a template and needs to be adjusted to the specific use case. You will need to replace all elements marked as `***Please fill***` in the generated template and adjust the logic to your scenario.

Your existing form submission will be sent to Customer Insights - Journeys using a JavaScript API which is defined in the file `FormCapture.bundle.js` and is included in the snippet.
The integration is achieved via a JavaScript API that is defined in the file `FormCapture.bundle.js` and is included in the snippet.

The form capturing setup consists of these steps:
It is accomplished by the following steps:

1. Get the reference to the form element on the page.
1. Define the mapping of form fields on fields (entity attributes) in Customer Insights - Journeys.
1. Define the mapping of Consent fields on Consent model in Customer Insights - Journeys.
1. Send the form submission to Customer Insights - Journeys.

#### 1. Get a reference to the form element

To get a reference to the form element, you can use the `waitForElement` helper function. It also works with dynamically rendered elements and returns a promise that will resolve once the element with the given selector is found on the page. For a reference of CSS selectors, see this [documentation](https://www.w3schools.com/cssref/css_selectors.php).

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

Fields in the form need to be mapped to the respective fields (entity attributes0) in Customer Insights - Journeys. That can be achieved using the function `d365mktformcapture.serializeForm(form, mappings)`.

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

The parameter `form` is retrieved by the `waitForElement` function described in the previous section. The parameter `mappings` is an array with elements of the following structure:

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

Make sure you handle all errors returned by the `FormFieldMappingResults`. You can then send the payload to Customer Insights - Journeys by calling `serializedForm.SerializedForm.build()`.

##### 2.1 Mapping of OptionSet Fields

For `OptionSet` fields, you need to define the mapping to the respective value that should be stored in Customer Insights - Journeys. This can be achieved via the `DataverseFieldValue` property.

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

##### 2.2 Mapping of Lookup Fields

Only static (default) values are supported by the out-of-the-box mapping logic for lookup fields. You need to define the name of the field as well as the value that should be stored on Dynamics 365 side.

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

##### 3. Define the mapping of Consent fields

Consent fields need to be configured in the Form editor in Customer Insights - Journeys. The `DataverseFieldName` and `DataverseFieldValue` mappings will be auto-generated accordingly.

**Example:**

```HTML
<form id="form1">
  <p>Consent: <input type="checkbox" name="consentField"/></p>
</form>

<script>
  ...
  const mappings = [
    {
        FormFieldName: "consentField",
        DataverseFieldName: "msdynmkt_purposeid;channels;optinwhenchecked",
        DataverseFieldValue: "10000000-0000-0000-0000-000000000004;Email;true",
    },
  ];
  ...
</script>
```

#### 4. Send the form submission to Customer Insights - Journeys

Once you get a reference to the form, define the mappings, and serialize the form, you can add an event listener to the `submit` event and send it via the `d365mktformcapture.submitForm(captureConfig, payload)` function. This call returns a promise, and errors can be handled in the `catch` logic.

> [!IMPORTANT]
    > If you have a custom validation in place or a Captcha check, make sure you submit the Form to Customer Insights - Journeys only in case of a successful validation (e.g., check for `isDefaultPrevented` on the `submit` event or explicitly call `submitForm` only after the validation passes)

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

## Troubleshooting

### The call to the submission endpoint fails with a CORS error

This could be a common cause for submissions not to be captured. Please add the domain to be allowed for form hosting. Learn more about [domain authentication](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/domain-authentication).

### Consent values are not updated correctly

Make sure you have setup the respective consent fields in the Form editor (see section "Creating the form capture in Customer Insights - Journeys form editor") and used the correct mappings generated in the publishing process.