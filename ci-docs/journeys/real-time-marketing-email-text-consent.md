---
title: Manage consent for email and text messages in Customer Insights - Journeys
description: Learn how to manage consent for messages in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/22/2023
ms.topic: reference
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Manage consent for email, SMS (text) and custom channel messages in Customer Insights - Journeys

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

> [!NOTE]
> Customer Insights - Journeys consent is contact-point based and works for messages sent to contacts, leads, and Customer Insights - Data profiles. Customer consent is stored per email address or phone number, as opposed to being stored per contact record. Outbound marketing consent processes that you have already defined are not influenced by the Customer Insights - Journeys settings.

> [!IMPORTANT]
> As of December 2022, consent enforcement for real-time journeys for **contacts** was changed to require opt-in for emails sent using the **restrictive** consent enforcement model. If you would like to revert to the previous behavior, you can change your consent enforcement model to **non-restrictive**. Alternatively, if you have previously captured consent on **contact** records in outbound marketing, you can **load consent** to populate the contact-point consent records used to enforce consent in Customer Insights - Journeys. Learn more: [Migrate consent records to Customer Insights - Journeys](real-time-marketing-migrate-consent.md)

> [!IMPORTANT]
> Real-time journeys may check the contact's `DoNotEmail`, `DoNotBulkEmail` and `DoNotTrack` fields to match outbound's consent enforcement behavior and aid in the transition from outbound marketing to real-time journeys. To learn more, visit [Manage user compliance settings in Customer Insights - Journeys](real-time-marketing-compliance-settings.md)

> [!CAUTION]
> In July 2023 Customer Insights - Journeys introduced new Dataverse tables to support business units and multi-brand consent compliance profiles. All customers have been migrated the new tables. Customers who have custom workflows (such as Power Automate Flows) that read or write **msdynmkt_contactpointconsent2** or **msdynmkt_contactpointconsent3** consent tables need to take action to ensure they do not lose functionality.
>
> If your custom workflows *read* from the **msdynmkt_contactpointconsent2** or **msdynmkt_contactpointconsent3** consent tables, you must update custom workflows to read from the latest **msdynmkt_contactpointconsent4** table to ensure continued functionality.
>
> If your custom workflows *write* to the **msdynmkt_contactpointconsent2** or **msdynmkt_contactpointconsent3** consent tables, any writes to these tables automatically have data synced to the **msdynmkt_contactpointconsent4** table after a delay (potentially 24 hours or longer). The data sync will continue until **June 1, 2024**. After that date, you will need to have moved all workflows that write contact point consent records to target the **msdynmkt_contactpointconsent4** table.

## How consent is respected for emails

When creating a new email message, you choose a **Compliance Profile**, a **Purpose**, and, optionally, a **Topic** from that profile in the **Compliance** section of the **Email header** settings. To set up message designation, select the gear icon ![The Settings menu icon.](media/settings-icon.png "The Settings menu icon") in the email header. This opens the **Email header** settings pane on the right side of the page. Navigate to the **Email settings** section.

> [!div class="mx-imgBorder"]
> ![Compliance profile and purpose screenshot.](media/real-time-marketing-email-compliance-settings.png " Compliance profile and purpose screenshot ")

An email message is only sent if it passes the consent checks configured by the **Purpose** and (optional) **Topic**. The decision to send or block sending a message is done right before sending the message. This ensures that the app never mistakenly sends a message to someone who has opted out, even if they're mistakenly included in a journey segment. The enforcement rules for consent are governed by the **Enforcement model** setting on the purpose. If the purpose has a "Restrictive" enforcement model, the email is sent only if the email address has explicitly opted into receiving this message. If the purpose has a "Non-restrictive" enforcement model, the email is sent as long as the email address hasn't opted out. The "Disabled" enforcement model disables consent checks on the email address and lets all messages be delivered. The default "Commercial" purposes have a "Non-restrictive" enforcement model. The default "Transactional" purpose has a "Disabled" enforcement model. The enforcement models of the purposes can be changed in the compliance profile. To learn more about the **Purpose**, **Topic**, and **Enforcement model** concepts, visit [Manage user compliance settings in Customer Insights - Journeys](real-time-marketing-compliance-settings.md)

As required for commercial email, a **Company Address** placeholder and an **Preference Center** placeholder link are added to the email footer automatically. The company address reflects the value set on the **Compliance profile** and can be edited directly from the email editor if needed. The **Preference center** link leads to the preference management page configured by the **Compliance Profile**, where customers can review and change communication preferences.

The presence of a company address and unsubscribe link is checked when you select **Ready to send**. The app warns you if one of these parameters is missing if you're sending a message to a commercial consent purpose.

> [!NOTE]
> The app will display warnings if, for example, you accidentally delete either the company address or link to the preference center. However, it does not block you from sending such an email. Thus, you are able to replace the given company address field with another one of your choice or add a link to a custom preference center if you like.

## How consent is respected for SMS (text) and custom channel messages

The Customer Insights - Journeys rules for sending SMS and custom channel messages are slightly different than the rules for sending emails. A user must always opt in to consent to receive commercial SMS or commercial custom channel messages, irrespective of the consent enforcement model. Transactional SMS and custom channel messages are always sent and don't have consent checked or enforced.

## Consent to track user behavior

Each compliance profile has its own purpose specifically for tracking user interactions, such as message opens and link clicks. Like the commercial and transactional purposes, the enforcement model for tracking consent can be restrictive, non-restrictive, or disabled. If the tracking purpose is set to a disabled enforcement model, no tracking consent checks are made for messages sent as part of that compliance profile, meaning all interactions are tracked.

If you would like to collect tracking consent, you can add the tracking purpose to forms and preference centers.  

> [!IMPORTANT]
> With the July 2023 release, customer consent data began to utilize the new multi-brand consent features. For some Customer Insights - Journeys users, the migration changed the settings that control whether tracking links are included in messages. The changes may prevent tracking in messages if the customers have not given explicit consent. After the migration, if you want to enable tracking links in messages for customers who have not provided consent, update the Tracking purpose enforcement model of your Compliance Profile(s) to "Non-restrictive." This enables tracking links to be substituted in emails as long as the receiver has not explicitly opted out of tracking. 

## Consent enforcement diagram

The following diagram provides a visual representation of how consent is enforced in Customer Insights - Journeys.

<table>
  <tr>
    <th>Restrictive enforcement model</th>
  </tr>
  <tr>
  	<td></td>
    <td><b>Opted out</b></td>
    <td><b>None/Not-set</b></td>
    <td><b>Opted in</b></td>
  </tr>
  <tr>
  	<td><b>Email channel</b></td>
    <td>Blocked</td>
    <td>Blocked</td>
    <td>Sent</td>
  </tr>
  <tr>
  	<td><b>SMS/Custom channel</b></td>
    <td>Blocked</td>
    <td>Blocked</td>
    <td>Sent</td>
  </tr>
  <tr>
  	<td><b>Tracking purpose<b></td>
    <td>Not tracked</td>
    <td>Not tracked</td>
    <td>Tracked</td>
  </tr>
</table>

<table>
  <tr>
    <th>Non-restrictive enforcement model</th>
  </tr>
  <tr>
  	<td></td>
    <td><b>Opted out</b></td>
    <td><b>None/Not-set</b></td>
    <td><b>Opted in</b></td>
  </tr>
  <tr>
  	<td><b>Email channel</b></td>
    <td>Blocked</td>
    <td>Sent</td>
    <td>Sent</td>
  </tr>
  <tr>
  	<td><b>SMS/Custom channel</b></td>
    <td>Blocked</td>
    <td>Blocked</td>
    <td>Sent</td>
  </tr>
  <tr>
  	<td><b>Tracking purpose<b></td>
    <td>Not tracked</td>
    <td>Tracked</td>
    <td>Tracked</td>
  </tr>
</table>

<table>
  <tr>
    <th>Disabled enforcement model</th>
  </tr>
  <tr>
  	<td></td>
    <td><b>Opted out</b></td>
    <td><b>None/Not-set</b></td>
    <td><b>Opted in</b></td>
  </tr>
  <tr>
  	<td><b>Email channel</b></td>
    <td>Sent</td>
    <td>Sent</td>
    <td>Sent</td>
  </tr>
  <tr>
  	<td><b>SMS/Custom channel</b></td>
    <td>Sent</td>
    <td>Sent</td>
    <td>Sent</td>
  </tr>
  <tr>
  	<td><b>Tracking purpose<b></td>
    <td>Tracked</td>
    <td>Tracked</td>
    <td>Tracked</td>
  </tr>
</table>

> [!IMPORTANT]
> Real-time journeys may check the contact's `DoNotEmail`, `DoNotBulkEmail` and `DoNotTrack` fields to match outbound's consent enforcement behavior and aid in the transition from outbound marketing to real-time journeys. To learn more, visit [Manage user compliance settings in Customer Insights - Journeys](real-time-marketing-compliance-settings.md)

## View consent records

In the consent center, you can view a list of all contact-point consents and their related attributes (type, status, source of consent data, and date modified).

To see a compact view for a single consent record or make changes to it, select the contact-point name from the list of records.

## Audit consent records

You can keep track of all consent-related changes on a per contact record basis (who made the changes and when). The **Audit history** is available under a consent record's **Related** tab.

### See also

[Grow your business with multi-brand, custom preference centers](real-time-marketing-compliance-settings.md)
[Customer Insights - Journeys preference centers](real-time-marketing-preference-centers.md)
[Outbound marketing compliance settings](privacy-use-features.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
