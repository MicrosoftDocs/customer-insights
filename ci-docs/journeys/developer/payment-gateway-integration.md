---
title: Set up payment gateway integration
ms.reviewer: alfergus
description: Set up payment gateway integration for your events. Discover how to configure payment providers and streamline attendee payments on your event website.
ms.date: 01/26/2026
ms.topic: how-to
author: pawelkruk
ms.author: alfergus
search.audienceType: 
  - developer
---

# Payment integration for events in real-time journeys

If you have one or more events where contacts must purchase a pass, then you can enable attendees to pay for their passes online while they're registering for the event on your event website.

To enable online payment, you must make an agreement with a third-party payment provider who can authenticate and capture payment details. Your payment provider supplies you with details about how to implement their system, which you'll usually do by adding code supplied by your provider to a web page on your event website. You typically also must tell your provider the URL to request from Dynamics 365 Customer Insights - Journeys to indicate a successful payment.

Once your new payment gateway is in place on your event website, you can configure events to use it, or assign it as the default for all new events. To learn more about setting up event passes, see [Set up event passes](../real-time-journeys-event-passes.md).

To turn on payment integration, go to **Settings** > **Feature switches**, and under **Event management**, turn on the **Enable payments in real-time journeys** toggle.

## Overview of payment integration components

For event registrations created using the [events API](using-rtm-events-api.md), the following components are used to complete the registration for a paid event scenario:

1. **Payment provider**: A service that processes online payments. The payment provider contributes two components:
    - *Payment gateway*: A website that captures payment information, including product, price, and payee data. Upon submission, the payment gateway initializes payment transaction processing and typically redirects the event participant to a “thank you” page.
    - *Payment notification*: A service that notifies subscribers about payment processing events, including payment completion or payment rejection events.

    > [!NOTE]
    > The examples in this article discuss basic integration with Stripe, but other providers like PayPal or Square can be used.

1. **EventManagement Power App**: The Dynamics 365 – Customer Insights event management application. Contains core logic and data used by customers to set up and monitor paid events. It also hosts the configuration required to integrate with the payment provider.
1. **EventManagement API**: Public endpoint providing the API used to register for an event.
1. **Registration page**: A third-party page, which:
    - Provides the user interface for event participants to register for events.
    - Integrates with the EventManagement system through the EventManagement API.

    > [!NOTE]
    > Implementation of the registration page is out of scope this article. To demonstrate how the integration should be implemented, this article uses simple _http_ file snippets to issue web requests.

1. **Registration completion service**: A third-party service, which:
    - Integrates with the payment provider to register payment submission.
    - Provides an API to receive payment redirect requests from the registration page and returns a redirect URL to the payment gateway.
    - Integrates with the payment notification to process payment completion and payment rejection events. Uses a Power Apps OData endpoint to register updates for payments through the EventManagement Power App custom OData API.

    > [!NOTE]
    > The breakdown of payment integration responsibilities into separate components is for illustrative purposes. Depending on your needs, you can collapse or split certain third-party components. For example, the registration completion service can be split into two parts: one responsible for payment redirect and a second responsible for notifications.  

## Implementing a registration completion service

This article uses an ASP.NET Model-View-Controller (MVC) web application with C# for the implementation examples. The examples use Stripe to show a real-world implementation. This implementation is high level and incomplete. It only shows how to close the payment loop. If you want to finish the implementation, follow the official Stripe documentation.

### Part A: Payment redirect logic

The registration page gets a response with a link to the endpoint that the browser uses to redirect the event participant to the payment gateway. To do this, the registration completion service fetches the payment information from the EventManagement Power App. Then, it calls the payment gateway service to generate a new payment URL.

#### Contract

The link format is described by the following OpenAPI specification:

```
{ 
    "openapi": "3.0.1", 
    "info": { 
        "title": "PaymentGatewaySample", 
        "version": "1.0" 
    }, 
    "paths": { 
        "/GatewayRedirect/PayWithStripe": { 
            "get": { 
                "tags": [ 
                    "GatewayRedirect" 
                ], 
                "parameters": [ 
                    { 
                        "name": "purchaseId", 
                        "in": "query", 
                        "schema": { 
                            "type": "string", 
                            "format": "uuid" 
                        } 
                    }, 
                    { 
                        "name": "returnUrl", 
                        "in": "query", 
                        "schema": { 
                            "type": "string" 
                        } 
                    } 
                ], 
                "responses": { 
                    "302": { 
                        "description": "Redirect" 
                    } 
                } 
            } 
        } 
    }, 
    "components": {} 
} 
```

The query string has two input parameters:

- `purchaseId`: A GUID that identifies a record in the `msevtmgt_eventpurchase` table. The record has information about the payment state and other details, including the payment amount and currency.
- `returnUrl`: A URL where the payment gateway returns after the payment is submitted. The return URL is optional. Use the return URL if, for example, you use a preset thank you page from the payment gateway.

The response is a standard HTTP 302 redirect to the payment link on the payment gateway.

#### Fetching the payment information

Use an organization request to get the required data. The following C# code snippet shows how to get the amount and currency code in the `amount` and `currencyIsoCode` variables:

```
var request = new RetrieveRequest 
{ 
    Target = new EntityReference("msevtmgt_eventpurchase", purchaseId), 
    ColumnSet = new ColumnSet( "msevtmgt_totalprice"), 
    RelatedEntitiesQuery = new RelationshipQueryCollection 
    { 
        { 
            new Relationship("TransactionCurrency_msevtmgt_eventpurchase"), 
            new QueryExpression 
            { 
                EntityName = "transactioncurrency", 
                ColumnSet = new ColumnSet("isocurrencycode") 
            } 
        } 
    }, 
}; 
var response = await cdsServiceClient.ExecuteAsync(request) as RetrieveResponse; 
var entity = response?.Entity; 
var amount = entity?.GetAttributeValue<Money>("msevtmgt_totalprice") ??  
             throw new InvalidOperationException("Total price on purchase record is not set"); 
var currencyEntity = entity?.RelatedEntities.FirstOrDefault().Value.Entities.FirstOrDefault(); 
var currencyIsoCode = currencyEntity?.GetAttributeValue<string>("isocurrencycode") ?? "USD"; 
```

The amount and currency are the minimum information required by the payment gateway. If needed, more data can be retrieved.

#### Generating a redirect link  

This step is different for each payment provider. In this example, the article uses a simple integration with Stripe. The following code snippet shows how to generate a new link:

```
public static string GetRedirectUrl(string purchaseId, long priceInCents, string currency, string? redirectUrl) 
{ 
    var priceOptions = new PriceCreateOptions 
    { 
        UnitAmount = priceInCents, 
        Currency = currency, 
        ProductData = new PriceProductDataOptions 
        { 
            Name = $"Payment {purchaseId}", 
        }, 
    }; 
    var priceService = new PriceService(); 
    var price = priceService.Create(priceOptions); 
    var options = new PaymentLinkCreateOptions 
    { 
        LineItems = new List<PaymentLinkLineItemOptions> 
        { 
            new PaymentLinkLineItemOptions 
            { 
                Price = price.Id, 
                Quantity = 1, 
            }, 
        }, 
        Metadata = new Dictionary<string, string> 
        { 
            { "order_id", purchaseId }, 
            { "time", DateTime.UtcNow.ToString("o") }, // ISO 8601 format  
        } 
    }; 
    if (!string.IsNullOrEmpty(redirectUrl)) 
    { 
        options.AfterCompletion = new PaymentLinkAfterCompletionOptions 
        { 
            Type = "redirect", 
            Redirect = new PaymentLinkAfterCompletionRedirectOptions 
            { 
                Url = redirectUrl, 
            }, 
        }; 
    } 
    var service = new PaymentLinkService(); 
    PaymentLink paymentLink = service.Create(options); 
    return paymentLink.Url; 
} 
```

### Part B: Payment finalization logic

The payment completion gets a notification from the payment notification service. The notification includes the purchase ID used to generate the payment link. Use the custom API, `msevtmgt_finalizeregistrationpayment`, to run this operation. The API takes two parameters:

- `msevtmgt_purchaseid`: The purchase ID used to generate the payment link.
- `msevtmgt_paymentstatus`: The value of the `msevtmgt_paymentstatus` OptionSet, indicating the status of payment:
    - `100000000` = Cancelled
    - `100000001` = Completed

The following code snippet demonstrates how to register the payment completion:

```
var request = new OrganizationRequest("msevtmgt_finalizeregistrationpayment"); 
request["msevtmgt_purchaseid"] = purchaseId; 
request["msevtmgt_paymentstatus"] = new OptionSetValue(status); 
await cdsServiceClient.ExecuteAsync(request); 
```

An example payment notification from Stripe uses a webhook to receive notifications about various events, including purchase-related events.  

The following code shows simple controller logic for the registration completion service:

```
using Microsoft.AspNetCore.Mvc; 
using PaymentGatewaySample.Dataverse; 
using Stripe; 
using Stripe.Checkout; 
namespace PaymentGatewaySample.Controllers 
{ 
    [ApiController] 
    [Route("GatewayEvents")] 
    public class GatewayEventsController(IDataverseClientService dataverseUtil) : ControllerBase 
    { 
        private readonly IDataverseClientService dataverseUtil = dataverseUtil; 
        [HttpPost("HandleStripeEvent")] 
        public async Task<IActionResult> HandleStripeEvent() 
        { 
            try 
            { 
                var body = await new StreamReader(HttpContext.Request.Body).ReadToEndAsync(); 
                var stripeEvent = EventUtility.ParseEvent(body); 
                if (stripeEvent.Type != EventTypes.CheckoutSessionCompleted) 
                { 
                    return Ok(); 
                } 
                var session = stripeEvent.Data.RawJObject["object"].ToObject<Session>(); 
                var status = session.PaymentStatus; 
                var purchaseId = session.Metadata.TryGetValue("order_id", out var orderId) ? Guid.Parse(orderId) : Guid.Empty; 
                if (status == "paid" && purchaseId != Guid.Empty) 
                { 
                    // Update purchase with Paid status 
                    await dataverseUtil.UpdatePurchaseStatus(purchaseId, 100000001, CancellationToken.None); 
                } 
                return Ok(); 
            } 
            catch (StripeException e) 
            { 
                return BadRequest(); 
            } 
        } 
    } 
} 
```

## Complete the setup of payment gateway in Customer Insights - Journeys

1. **Set up the web application**: Create the application set up under **Settings** > **Event management** > **Web applications**, as described in [events API documentation](using-rtm-events-api.md). You receive an endpoint that your registration page uses to initialize the registration process, together with a shareable token.

1. **Set up a payment provider**: Navigate to **Settings** > **Event management** > **Payment providers** and add a new payment provider configuration by selecting **+New**. You're asked to provide:
    - **Provider name**: The internal name that helps your users understand which integration they should use for their events.
    - **Payment page URL**: The payment page URL points to the URL of the payment redirect API from the registration completion service. Notice that the URL ends with a “?” and a query string section. Here, you can add any additional query string for more advanced implementations of your choice.
    - **Payment timeout (minutes)**: This is the maximum amount of time the registration reservation should wait for successful payment confirmation before releasing the spot and canceling the transaction.

## Testing

1. Create a new event record. Ensure that:
    - **Custom solution using events API** is set as the value for the **Where do you want attendees to register for this event?** parameter.
    - On the **Passes** tab, **Enable payment gateway** is set to **Yes**.
    - On the **Passes** tab, **Payment provider** is selected.
1. Add one pass and set the price on it. Make note of the **Pass-ID** (the primary key of the `msevtmgt_pass` record).
1. Set the event record to **Live**. Make note of the **Readable-Event-ID** (the `msevtmgt_readableeventid` property of the `msevtmgt_event` record).
1. Issue the following HTTP request:

    ```
    POST <Replace with Web Application Endpoint>/events/<Replace with Readable-Event-ID>/registrations?emApplicationtoken=<Replace with Web Application Token> 
    Accept: */* 
    Content-Type: application/json 
    { 
        "attendees": [ 
            { 
                "lastName": "Jane", 
                "firstName": "Doe", 
                "email": "Jane@contoso.com", 
                "passId": "<Replace with Pass ID>" 
            } 
        ] 
    }
    ```

    The HTTP response body should look like this:

    ```
    { 
    "redirectUrl ": "https://localhost:7202/GatewayRedirect/PayWithStripe?purchaseId=a4d9e358-949f-f011-bbd3-6045bd02f64d&returnUrl=https%3A%2F%2Fmicrosoft.com" 
    }
    ```

    `redirectUrl` targets the endpoint on the registration completion service. In this example, it points to a URL on the `localhost`, as the service is running on a local machine for testing purposes.

1. Now, paste the URL in the browser. It should load the payment page from your selected payment provider.
1. Fill in dummy credit card data and submit the payment.
1. You should see that your browser is redirected to the **returnUrl**.

Now, test the payment finalization. If you're signed in to PowerApps as an admin, open the developer tools and run the following JavaScript code in the console:

```
x ={ 
"msevtmgt_purchaseid": "<replace>", // <--- your purchase ID 
"msevtmgt_paymentstatus": 100000001 
}; 
var xhr = new XMLHttpRequest(); 
xhr.open("POST", window.location.origin + "/api/data/v9.1/msevtmgt_finalizeregistrationpayment", true); 
xhr.setRequestHeader("Accept", "application/json"); 
xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8"); 
xhr.setRequestHeader("OData-MaxVersion", "4.0"); 
xhr.setRequestHeader("OData-Version", "4.0"); 
xhr.send(JSON.stringify(x)); 
```

You've completed the payment loop.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
