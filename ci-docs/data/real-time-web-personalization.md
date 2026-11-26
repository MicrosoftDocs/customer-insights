---
title: Set up web tracking and personalization
description: Set up web tracking and personalization in Customer Insights - Data to identify visitors, retain browsing history, and tailor their web experience. Get started.
ms.date: 11/24/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: tozahalk
ms.custom:
  - bap-template
  - ci-data-web-tracking
  - ai-gen-docs-bap
  - ai-seo-date: 09/16/2026
ai-usage: ai-assisted
---

# Set up web tracking and personalization

Set up web tracking and personalization in Customer Insights - Data to create unknown profiles for unauthenticated visitors and track their page views and interactions in real time. Merge unknown profiles with known customer profiles when visitors authenticate, and personalize their web experience. Learn more in [Web tracking and personalization overview](real-time-web-personalization-overview.md).

> [!IMPORTANT]
> If you added the tracking script to your website before October 2026, you **must** update your website with the latest script to continue using tracking and personalization. Copy the script from Customer Insights - Data or Customer Insights - Journeys. Scripts are customized for your environment, so it's important to copy and use the production script on your production website. If your script contains `allowIpAddressCollection`, you have the latest script.

## Process overview

Set up web tracking and personalization in three steps. The first step is required and enables anonymous tracking and personalization for returning visitors. Complete the second and third steps to link anonymous browsing activity to customer profiles.

1. **Add the tracking script to your website**: Add the tracking script to see anonymous visitors in Customer Insights - Data and the pages they view.

1. **Tell the system how to recognize your customers**: Specify the table that contains your customer records so the system can identify customers when they sign in.

1. **Call `setUser` when someone signs in**: Add this line of code to merge an anonymous visitor with a known customer and keep their browsing history.

## Prerequisites

- Your website identifies known users and saves their data to a table. For example, a `<WebCustomers>` table. Each customer has a unique identifier, such as a customer ID.

- You ingest your `<WebCustomers>` table into Customer Insights - Data by using one of the [data source connectors](data-sources.md).

- You include your `<WebCustomers>` table in the [data unification process](data-unification.md).

- You have a way to personalize your site, either by using the APIs with your development team or by using the Optimizely integration if you have an Optimizely license.

## Connect your website's consent controls

Connect your website's consent manager before the tracking script initializes. For cookie permission, see [Connect your website's cookie controls](real-time-web-tracking-cookies.md#connect-your-websites-cookie-controls).

Changing a Customer Insights - Journeys **Tracking** purpose setting doesn't automatically disable Customer Insights - Data collection.

## Add the tracking script

1. Sign in to Customer Insights - Data and select **Web tracking & personalization**.

   :::image type="content" source="media/web-tracking-personalization.png" alt-text="Screenshot of Web tracking & personalization in Customer Insights - Data.":::

1. Select your `<WebCustomers>` table. The tracking script uses it to identify your customers when they sign in.

1. Select **Copy** to copy the tracking script, and then paste it in the `<head>` tag of your website.

   > [!IMPORTANT]
   > Copy the script from the same Customer Insights - Data environment where you want to track activity. A script copied from a test environment doesn't report activity to your production environment.

   If you're using a tag manager such as Google Tag Manager, go to the Google Tag Manager portal. Select **Add new tag** > **Tag configuration** > **Custom HTML**, paste the Customer Insights - Data tracking script, and then select **Save**.

   If you're using a content management system (CMS) such as WordPress, use your CMS tools to add the script to your site header. Here's an example from [WordPress](https://wordpress.com/support/adding-code-to-headers/).

Browse your website as an unauthenticated visitor to create an unknown profile in Customer Insights - Data.

To view the unknown profiles, go to the **Customers** page and select **Unknown**. Your visit appears as a profile identified by a cookie ID, and the timeline shows the pages you viewed.

:::image type="content" source="media/customers-unknown.svg" alt-text="Screenshot of the Unknown tab on the Customers page in Customer Insights - Data.":::

To validate the web events in Dataverse, sign in to the [Power Apps maker portal](https://make.powerapps.com/). Select **Tables** > **All**, and then select the `PersonalizationView` and `PersonalizationAction` tables.

## Turn an anonymous visitor into a known customer

When a visitor signs in, Customer Insights - Data can merge their anonymous profile with their known customer profile, including the activity collected while they were anonymous. To identify a signed-in customer, define the `setUser` function on your website.

1. Sign in to Customer Insights - Data and select **Web tracking & personalization**.

1. Select the table that identifies your customers. The list includes only tables used as sources for data unification.

   For example, the source table `LoyaltySignUps` in Customer Insights - Data uses `LoyaltyId` as the primary key, which uniquely identifies a customer in that table.

   Customer Insights - Data identifies the visitor by the primary key of the selected table and uses the same matching logic as data unification.

1. Define the `setUser` function on your website. Typically, you only need to call `setUser` on the page where visitors sign in. Use the visitor's ID from your selected table as the identifier, for example, `jsmith001`.

   ```html
   <script>
     function setUser() {
       window["MSCI"].setUser({ "authId": "<identifier>" });
     }
   </script>
   ```

1. Call the `setUser` function when a visitor authenticates.

   ```html
   <button type="submit" onclick="setUser()">Submit</button>
   ```

The merge happens in real time. The known profile gains the anonymous profile's interactions and its cookie ID, and the anonymous profile expires.

When cookies are allowed, the script saves the customer ID in `msdynci_userauthid`. On later page loads, it restores that ID and automatically sends a `user` event without another `setUser` call. The cookie doesn't prove the visitor is still signed in; handle sign-out and account changes according to your identity and consent requirements.

## Capture query string and IP address (optional)

Page view and click events can also record the page's query string and an anonymized IP address. Both settings are **off by default**. Turn on each setting separately in the `cfg` block of the tracking script.

```javascript
cfg: {
  // ...your existing configuration...

  queryStringAttributes: [ "utm_campaign", "utm_source", "plan", "region" ],
  allowIpAddressCollection: true
}
```

| Setting | Effect |
|---|---|
| `queryStringAttributes` | Specify the query string parameters to capture. Parameter names aren't case-sensitive, and the system records only parameters in the allow list. If you leave it unset or empty, the system captures nothing. |
| `allowIpAddressCollection` | Set to `true` to collect the visitor's IP address with the last octet zeroed. If you omit it or set it to `false`, the system doesn't collect the IP address. |

The query string (`msdynci_querystring`) enables campaign attribution. Tag your campaign links with the parameter names in the allow list. You can then build a segment of people who arrived through a specific campaign. The value isn't stored as it appears in the address bar. The system rebuilds it into a canonical form so that segment rules match consistently:

```text
Address bar   https://example.com/page?Plan=Pro&other=x&utm_campaign=Spring+Sale
Allowlist     [ "utm_campaign", "plan" ]
Stored        &utm_campaign=Spring%20Sale&plan=Pro&
```

The following rules apply:

- The system drops parameters that aren't in the allow list. `other=x` never reaches storage.
- The system converts parameter names to lowercase. Values retain their original case.
- Order follows your allow list, not the address bar.
- Each token is wrapped in `&`, so a rule matching `&plan=Pro&` matches exactly and doesn't match `plan=Promo`.
- If a parameter appears more than once, the system keeps the first occurrence.
- The script doesn't capture content after a `#` in the URL.
- The system caps values at 2,000 characters and trims at a token boundary. The event itself is always recorded even when values are trimmed.

The system collects the **IP address** (`msdynci_ipaddress`) with the last octet zeroed: `203.0.113.0`, not `203.0.113.47`. As a result, it identifies a general network rather than a device.

## Understand real-time web event processing

Real-time web events arrive continuously rather than in scheduled batch loads. The system processes each event as it arrives.

Keep the following points in mind:

- Conflation uses the snapshot of the event data that is available when it runs.
- Segments built directly on personalization view events depend on the real-time data source. As a result, a segment and a conflation run can evaluate different snapshots of the same activity.

This difference can cause slight discrepancies between a segment count and the activity shown on a profile timeline.

## Use captured query-string values in segments

Selected query-string data is stored in the dedicated Dataverse field `msdynci_querystring`, separate from the URL field `msdynci_viewuri`. Use `msdynci_querystring` for query-parameter conditions. Include the `&name=value&` boundaries when matching a complete pair, such as `&campaign=1324&`.

### Match the encoded stored value

Query-string values are URI-encoded in the stored string. For example, a `utm_campaign` parameter uses the stored value shown in the following table. The segment filter condition must use the value stored in the table. A human-readable version with spaces or non-ASCII characters doesn't match the encoded stored value.

| Original parameter value | Stored value |
| --- | --- |
| spring_sale | spring_sale |
| Spring Sale | Spring%20Sale |
| Été | %C3%89t%C3%A9 |
| Buy 1 & Get 1 | Buy%201%20%26%20Get%201 |

Encoding depends on the values you use and how your web application is designed. It's usually sufficient to send a few test parameters and check the **QueryString** column in the **PersonalizationView** table in the Power Apps maker portal to confirm the format.

### Collect only necessary, approved data

Collect only parameters that your organization approves and needs. Avoid adding parameter names that can log sensitive personally identifiable information (PII), tokens, or secrets. Choosing a name doesn't guarantee that its values are safe. Review the values your site stores in each parameter before you enable tracking to help ensure compliance with applicable regulations.

Follow your site's applicable consent and privacy requirements before enabling collection. Handle partially masked IP data responsibly and use it only for the approved purpose.

## Related information

- [Web tracking and personalization overview](real-time-web-personalization-overview.md)
- [Personalize your customer's web experience](optimizely-integration.md)
- [Scenarios for web tracking and personalization](real-time-web-personalization-scenarios.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
