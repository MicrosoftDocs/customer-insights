---
title: Extend Customer Insights - Journeys marketing forms using code
description: Extend Customer Insights - Journeys marketing forms with JavaScript to apply custom business logic in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/12/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType:
- developer
---

# Extend Customer Insights - Journeys marketing forms using code

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

This article explains how to extend Customer Insights - Journeys marketing forms for advanced customization.

## JavaScript API
  
Customer Insights - Journeys marketing forms consist of two parts:

1. A form placeholder, which looks similar to this:

```HTML
<div>
  data-form-id='{msdynmkt_marketingformid}'
  data-form-api-url='https://{server}.dynamics.com/api/v1.0/orgs/{organizationid}/landingpageforms/forms/{msdynmkt_marketingformid}'
  data-cached-form-url='https://{server}.dynamics.com/{organizationid}/digitalassets/forms/{msdynmkt_marketingformid}'
</div>
```

2. And a form loader, which lights up the form placeholders once page the is loaded (a`DOMContentLoaded` event is triggered):

```
<script src='https://cxppusa1formui01cdnsa01-endpoint.azureedge.net/global/FormLoader/FormLoader.bundle.js'></script>
```

### Custom events

| Custom event | Description |
|------|-------|
|`d365mkt-beforeformload`|Triggered when the form placeholder is recognized before the actual form content is fetched. This event is triggered before the page is loaded, so it isn't visible in the developer console. |
|`d365mkt-formrender`|Triggered after the form content is fetched and right before it is injected into the form placeholder. This event is triggered before the page is loaded, so it isn't visible in the developer console. |
|`d365mkt-afterformload`|Triggered after the form is injected into the placeholder. |
|`d365mkt-formsubmit`| Triggered when the form is submitted, cancellable. |
|`d365mkt-afterformsubmit`| Triggered after form is submitted |

#### Form submit - d365mkt-formsubmit detail object properties

| Name | Type | Desription |
| ----- | ---- | ---- |
| Payload | Object | Dictionary with form properties to be sent to the server |

#### After form submit - d365mkt-afterformsubmit detail object properties

| Name | Type | Desription |
| ----- | ---- | ---- |
| Success | Boolean | Indicates whether the server accepted the submission or if the submission was rejected |
| Payload | Object | Dictionary with form properties as they were sent to the server |
  
You can attach custom events using the standard event attach mechanics:

##### Sample code
  ```HTML
  <script>
document.addEventListener("d365mkt-beforeformload", function() { console.log("d365mkt-beforeformload") });
document.addEventListener("d365mkt-afterformload", function() { console.log("d365mkt-afterformload") });
document.addEventListener("d365mkt-formrender", function() { console.log("d365mkt-formrender") });
document.addEventListener("d365mkt-formsubmit", function(event) {
    // example of validation using form submit event - cancelling form submission unless first name is John 
    if (document.forms[0]["firstname"].value !== "John") { 
      event.preventDefault(); 
      console.log("blocked mkt-formsubmit"); 
      return;
    }
    console.log("mkt-formsubmit" + JSON.stringify(event.detail.payload)); 
});
document.addEventListener("d365mkt-afterformsubmit", function(event) {
    console.log("success - " + event.detail.successful);
    console.log("payload - " + JSON.stringify(event.detail.payload));
});
</script>
```

### Form behavior customization

You can customize the form behavior by including a configuration script before the loader script is injected into a page.

 ```HTML
 <script>
 var d365mkt = {
   // disables showing of progress bar during form loading
   hideProgressBar: true
 };
 </script>
``` 

### Rendering a marketing form using a JavaScript API

Waiting for `DOMContentLoaded` can be inconvenient, especially for scenarios like dynamic content loading. For these situations, you can use the `createForm` helper function. `createForm` immediately returns a `div` DOM element, which triggers fetching form content in the background (the form is injected into a placeholder the moment it is fetched). 

```HTML
<html>
  <body>
    <script src="https://cxpiusa1formui01cdnsa01-endpoint.azureedge.net/global/FormLoader/FormLoader.bundle.js"></script>
    <div id="root"></div>
    <script>
      const root = document.getElementById('root');
      root.appendChild(d365mktforms.createForm(
        'formId',
        'formApiBaseUrl',
        'formUrl'));
    </script>
  </body>
</html>
```

You must also pass the readable event ID for the event registration forms. The modified syntax is as follows:
```JS
d365mktforms.createForm(
  'formId',
  'https://{server-api}/api/v1.0/orgs/{organizationid}/eventmanagement',
  'https://{server-load}/{organizationid}/digitalassets/forms/{msdynmkt_marketingformid}',
  { 'data-readable-event-id': 'My_Test_Event_123_replace_with_actual_readable_event_id' })
```

### Injecting a marketing form into a React application

You can use marketing forms within React applications. The form loader exposes the `d365mktforms.FormPlaceholder` React component, which you can inject into your application.

```HTML
<html>
  <head>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://cxppusa1formui01cdnsa01-endpoint.azureedge.net/global/FormLoader/FormLoader.bundle.js"></script>
  </head>
  <body>
    <div id="root"></div>
    <script>
      const root = ReactDOM.createRoot(document.getElementById('root'));
      root.render(React.createElement(d365mktforms.FormPlaceholder, {
        formId:'{msdynmkt_marketingformid}',
        formApiBaseUrl:'https://{server-api}/api/v1.0/orgs/{organizationid}/landingpageforms',
        formUrl:'https://{server-load}/{organizationid}/digitalassets/forms/{msdynmkt_marketingformid}'
      }, null));
    </script>
  </body>
</html>
```

You must also pass the readable event ID for the event registration forms. The modified syntax (introduced in Marketing version 6.1) is as follows:
```JS
      root.render(React.createElement(d365mktforms.FormPlaceholder, {
        formId:'{msdynmkt_marketingformid}',
        formApiBaseUrl:'https://{server-api}/api/v1.0/orgs/{organizationid}/eventmanagement',
        formUrl:'https://{server-load}/{organizationid}/digitalassets/forms/{msdynmkt_marketingformid}',
        readableEventId:'My_Test_Event_123_replace_with_actual_readable_event_id'
      }, null));
```

> [!NOTE]
> You have to replace `{msdynmkt_marketingformid}` with the actual identifier of the marketing form entity and `{organizationid}` with the actual identifier of your organization. `{server-}` should point to the server endpoints for your organization. The easiest way to grab the information you need is with the "Get Javascript Code" command from the form publish options.
>
> | Widget attribute | React component property |
> |---------------------|---------------------------------|
> | data-form-id | formId |
> | data-form-api-url | formApiBaseUrl |
> | data-cached-form-url | formUrl |

> [!NOTE]
> The Javascript API is available only for forms hosted as a script. It is not supported for the iFrame hosting option.  

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
