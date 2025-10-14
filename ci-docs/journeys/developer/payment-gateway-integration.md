High level design 

 
For events integrated through Custom solution using events API, following high level components take part in completing the registration for paid event scenario: 

Payment Provider – A service offering capabilities to process online payment. In particular it provides two components: 

Payment Gateway – website allowing to capture the payment information, including product, price, and payee data. Upon submission it initializes processing of payment transaction and typically redirects event participant to a chosen “thank you” page. 

Payment Notification – a service responsible to notify subscribers about payment processing events, including payment completion or payment rejection events. 

In our examples we discuss basic integration with Stripe, but other providers like PayPal, Square, etc can be used. 

EventManagement Power App - Dynamics 365 – Customer Insights Event Management application. Containing core logic and data used by customers to set up and monitor paid events. It also hosts configuration required to integrate with Payment Provider. 

EventManagement API – public endpoint providing API used to register into an event.  

Registration Page- A 3rd party page, which: 

provides user interface for event participants to register to events. 

Integrates with EventManagement system through EventManagement API. 

Note: Implementation of this page is out of scope for current document. To demonstrate how the integration should be implemented, we will use simple http file snippets to issue web requests. 

Registration completion service – A 3rd party service, which 

Integrates with Payment Provider to register payment submission. 

Provides API to receive payment redirect requests from Registration Page and return redirect URL to Payment Gateway. 

Integrates with Payment Notification process payment completion and payment rejection events. Uses Power Apps OData endpoint to register updates for payments through EventManagement Power App custom OData API. 

Note: proposed here split segregation of certain responsibilities into separate components is just for study purposes. Depending on your needs, you can collapse or split certain 3rd components. For example Registration completion service can be split into two parts. One responsible for payment redirect and second responsible for notifications.  

 

Implementation of Registration completion service 

In our samples, we use ASP.NET MVC web application with C#. We use Stripe to illustrate a real-world implementation. However this implementation is very superficial and incomplete. It only demonstrates how to close the payment loop. If you are interested in completing the implementation, please follow official Stripe documentation. 

Part A: Payment redirect logic 

Registration Page receives response with a link to endpoint, that should be accessible by the browser for redirecting the event participant into the Payment Gate. To achieve this the Registration completion service needs to fetch the payment information from EventManagement Power App. Then a call to Payment Gateway service is made to generate a new payment URL. 

Contract 

The link format is described by following OpenAPI specification: 

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

 

We have two input parameters from query string: 

purchaseId – it’s a GUID format identifying a record in msevtmgt_eventpurchase table. The record includes the information about the state of payment and some additional information, in particular the payment amount and currency. 

returnUrl – it’s a URL to which the Payment Gate should return after payment is submitted. Its optional, for example if the customer uses preset Thank You page from Payment Gate. 

The response is a standard HTTP 302 Redirect to the actual payment link on Payment Gateway. 

Fetching Payment Information 

One organization request can be used to fetch the required data. Following C# code snippet demonstrates how to fetch amount and currency code in amount and currencyIsoCode variables: 

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

 
Amount and currency are the absolute basic information that is required by the Payment Gate. If needed, more data can be retrieved based on need. 

Generating redirect link  

This step will differ, depending on what actual Payment Provider is used. In our example we use a simple integration with Stripe. A following code snippet demonstrates how to generate a new link: 

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

 
Part B: Payment finalization logic 

The payment completion receives a notification from Payment Notification service. The notification should include the Purchase ID used in generation of payment link.  
A custom API msevtmgt_finalizeregistrationpayment is available to execute such operation. It takes two parameters: 

msevtmgt_purchaseid – Purchase ID used in generation of payment link. 

msevtmgt_paymentstatus – The value of msevtmgt_paymentstatus 

OptionSet, indicating the status of payment: 

100000000 – cancelled 

100000001 – completed 

Following code snippet demonstrates how to register the payment completion: 

var request = new OrganizationRequest("msevtmgt_finalizeregistrationpayment"); 

request["msevtmgt_purchaseid"] = purchaseId; 

request["msevtmgt_paymentstatus"] = new OptionSetValue(status); 

await cdsServiceClient.ExecuteAsync(request); 

 

An example of Payment Notification from Stripe uses a webhook mechanism to receive notifications about various events, including purchase related.  
 
Following code demonstrates a very simple controller logic for Registration Completion Service: 

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

 

 

Setup 

Enable Payments feature 

Switch on “Enable payments in Real-time Journeys” feature switch in Settings->Feature Switches 
 
 

 

Set up Web application 

Create application set up under Settings->Event management->Web applications 

  

You will receive endpoint that your RegistrationPage uses for initialization of registration process, together with shareable token. 

Set up Payment Provider 

[TODO] where is the link in app module? 

 

Payment page URL points to the URL of payment redirect API from Registration completion service. Please notice that the URL ends with “?” to query string section. Here you can add any additional query string for more advanced implementations of your choice. 

Testing 

Create new Event record. Ensure that: 

“Custom solution using events API” is set as value of  
Where do you want attendees to register for this event? parameter. 

On Passes tab Enable payment gateway is set to Yes. 

On Passes tab Payment provider is selected. 

Add one Pass and set the price on it. Take note of Pass-ID (the primary key of msevtmgt_pass record). 

Set Event record to Live, take note of Readable-Event-ID (the msevtmgt_readableeventid property of msevtmgt_event record) 

Issue a following HTTP request: 

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

The HTTP response body should look like this: 

{ 

"redirectUrl ": "https://localhost:7202/GatewayRedirect/PayWithStripe?purchaseId=a4d9e358-949f-f011-bbd3-6045bd02f64d&returnUrl=https%3A%2F%2Fmicrosoft.com" 

} 

redirectUrl is targeting the endpoint on Registration completion service. In our case it’s pointing to a URL on localhost, as the service is running on local machine for testing purposes. 

Now lets paste the URL in the browser. It should load the payment page, like on the screenshot below: 
 
 

 

Fill up dummy credit card data and submit the payment 

 

You should see that your browser gets redirected to the returnUrl 

 

You can now test the finalization of the payment. If you are logged into PowerApps as administrator, you can open developer tools and execute following Javascript code through console: 

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

 
Alternatively, if you want to use web hook endpoint on your local host with Stripe, you can use stripe Cli to receive webhook notifications. 

You have now completed the payment loop. 
