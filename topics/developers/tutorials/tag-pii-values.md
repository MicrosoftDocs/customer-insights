---
layout: page
title: Tag PII values

---

Your data may contain sensitive user data, or Personally Identifiable Information. To ensure that you comply with data protection regulations, use PII tagging to mask such data.

Aria supports O365 Scrubbing as a service. Tagging a property as PII is as simple as specifying the `PiiType`
of the property (as shown below).

{% highlight csharp %}
var logger = LogManager.Initialize(tenantToken: "YOUR_TENANT_TOKEN");
EventProperties properties = new EventProperties();
properties.SetProperty("SenderIPAddress", "123.23.112.67", PiiType.IPv4AddressLegacy);
properties.SetProperty("UserName", "Joe", PiiType.Identity);

// You can send Pii and Non Pii properties in the same event.
properties.SetProperty("NonPIIValue", 20);
properties.SetProperty("123-456-7890", "Joe", PiiType.PhoneNumber);

// PiiType enum has more options.
// Pick the the appropriate enum value depending on your content.
properties.Name = "EventWithPII";
logger.LogEvent(properties);
{% endhighlight %}

See the **Reference** section on `EventProperties` for more details for platform specific code.
