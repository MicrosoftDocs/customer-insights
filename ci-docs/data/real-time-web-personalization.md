---
title: Set up real-time web personalization (preview)
description: Learn how to track web interactions and personalize experiences in real time with Customer Insights - Data.
ms.date: 12/20/2024
ms.topic: how-to
author: srivas15
ms.author: shsri
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Set up real-time web personalization (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Let Customer Insights - Data automatically create unknown profiles for unauthenticated visitors to your website and track their page views and interactions in real time. Set up web tracking, merge customers' unknown profiles with their known profiles when they authenticate on your site, and then personalize their web experience. Learn more in [Real-time web personalization overview](real-time-web-personalization-overview.md).

Watch this brief video to learn more about real-time web personalization.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RW1hyhp]

## Prerequisites

- Source data that contains your website customers is ingested and unified.

  Customer Insights - Data uses the primary key from the unified customer profile to identify your website visitors. The primary key should be a field that uniquely identifies a customer, such as email address, phone number, or member ID. For example, in Customer Insights - Data, you might have a source table called `LoyaltySignUps` with `LoyaltyId` as the primary key that uniquely identifies a customer in that table. Learn more in [Data sources overview](data-sources.md) and [Data unification overview](data-unification.md).

## Set up web tracking

1. Sign in to Customer Insights - Data and select **Web tracking & personalization**.

   :::image type="content" source="media/web-tracking-personalization.png" alt-text="Screenshot of Web tracking & personalization in Customer Insights - Data.":::

1. Select the table that the tracking script should use to identify your customers when they [authenticate](#authenticate-unknown-customers-and-merge-them-with-known).

1. Select **Copy** to copy the tracking script, and then paste it in the `<head>` tag of your website.

   If you're using a tag manager such as Google Tag Manager, go to the Google Tag Manager portal. Select **Add new tag** > **Tag configuration** > **Custom HTML**, paste the Customer Insights - Data tracking script, and then **Save**.

   If you're using a Content Management System (CMS) such as Wordpress, your CMS provider should have an easy way to add a script to the site header. Here's an example from Wordpress: [https://wordpress.com/support/adding-code-to-headers/](https://wordpress.com/support/adding-code-to-headers/).

Browse your website as an unauthenticated visitor to create an unknown profile in Customer Insights - Data.

To view the unknown profiles, go to the **Customers** page and select **Unknown**. All unknown profiles have a cookieId as an identifier and the website interactions on the timeline are shown automatically.

  :::image type="content" source="media/customers-unknown.svg" alt-text="Screenshot of the Unknown tab on the Customers page in Customer Insights - Data.":::

To validate the web events in Dataverse, sign in to [https://make.powerapps.com/](https://make.powerapps.com). Select **Tables** > **All**, and then select the `PersonalizationView` and `PersonalizationAction` tables.

## Authenticate unknown customers and merge them with known

To have Customer Insights - Data automatically merge an unknown with a known profile when a visitor authenticates, select the source table that you used to identify your customers when you [set up web tracking](#set-up-web-tracking). To identify and merge the profiles, the system needs to know the authenticated customer's unique ID. It does this by calling the `SetUser` function.

1. Sign in to Customer Insights - Data and select **Web tracking & personalization**.

1. Select the table that identifies your customers.

   For example, the source table `LoyaltySignUps` in Customer Insights - Data uses `LoyaltyId` as the primary key, which uniquely identifies a customer in that table.

   Only tables that were used as a source for data unification appear in the list of tables. Customer Insights - Data automatically identifies the visitor using the primary key of the table that you select. The merge logic is the same as in the data unification process.

1. Define the `setUser` function on your website. Typically, you only define this function on the page that authenticates visitors. The `<identifier>` is the visitor ID; for example, jsmith001.

    ``` javascript
    <script>
       function setUser() {
          window["MSCI"].setUser({ "authId": "<identifier>" });
     }
    </script>
    ```

1. Call the `setUser` function when a visitor authenticates.

   ``` html
   <button type="submit" onclick="setUser()">Submit</button>
   ```

## Personalize your customers' web experience

You can personalize your customers' web experience in either of the following ways:

- Without code, using the Optimizely integration with Customer Insights - data. Learn more in [No-code web personalization using Optimizely](optimizely-integration.md).

- With code, using APIs. Query any of the Customer Insights - Data APIs, which allow you to retrieve rich information about each customer, such as demographic information, web interactions, activities, segments, and measures. Learn more in [Dataverse APIs for Customer Insights - Data](dv-odata.md).

  Since the cookieIds are also used to uniquely identify a known customer or an unknown visitor, you can also use the cookieId to query a profile. Retrieve the Customer Insights - Data web tracking cookie on the server side of your website. Customer Insights - Data cookies are stored as "_msci" in the request.

  For example, using C#, you can find the cookieID of the current visitor like this:

  ```csharp
  string cookieId = Request.Cookies["_msci"]; //CI-D cookie
  ```

  Then, use the cookie as an identifier to query any of the Customer Insights - Data APIs.

The [web tracking and personalization tables](tables.md#real-time-web-personalization-tables-preview) are available in Dataverse.

## Related information

- [Real-time web personalization overview](real-time-web-personalization-overview.md)
- [No-code web personalization using Optimizely](optimizely-integration.md)
- [Known and unknown customers](customer-profiles.md#known-and-unknown-customers)

[!INCLUDE [footer-include](includes/footer-banner.md)]
