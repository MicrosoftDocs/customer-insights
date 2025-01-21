---
title: Known issues in outbound marketing and workarounds
description: This article documents known issues in outbound marketing and workarounds.
ms.date: 08/18/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Known issues in outbound marketing and workarounds

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

This document provides important, late-breaking information about known issues and workarounds for Dynamics 365 Customer Insights - Journeys. For information about monthly bug fixes, visit the [What's new in Dynamics 365 Customer Insights - Journeys](whats-new-marketing.md) article.

## Configuration, installation, and first-run experience

- The setup process can take up to two hours. The process might restart automatically during this time, which can result in multiple success (or failure) notifications being sent to you by email.
- Although the licensing agreement doesn't require it, a known technical issue currently prevents you from running the installation management area unless you have a Dynamics 365 license with the _System Administrator_ security role assigned on your target Dynamics 365 instance. <!--- 1183223 -->
- Some language strings in the email designer and customer journey designer aren't available in all languages. <!--- 1912019 --> <!--- 1843911 -->
- When an entitlement is changed, the updated working entitlement will sometimes display as "NotConfigured", and the broken entitlement will display as "Configured" in the Admin UI. You may get this fixed by raising a support request. <!--- 1884488 -->
- When a portal is expired, the **Configure your portal** item under **Other actions** links to the old portal. <!--- 1804106 -->
- When a setting from the Customer Insights - Journeys application settings overview page is selected, users who don't have admin privileges to adjust the setting are redirected to a blank page. <!--- 2157534 -->

## Customer journeys

- Deactivated contacts won't receive any emails from journeys they may be participating in, but they might continue to be included in other actions, such as tasks and workflows. <!--- 852372 -->  
- Insights for journeys, emails, and marketing pages may take up to six hours to display.
- The date scheduler tile in customer journeys doesn't display dates according to the Japanese imperial calendar (including in Japanese localizations). <!--- 1460626 -->
- [Export to Excel](export-journey.md) functionality is limited to 10,000 records. <!--- 1914934 -->
- A journey with too many tiles can overload the Customer Insights - Journeys services. To overcome potential service disruptions, use a [splitter tile](customer-journey-tiles-reference.md#branches).

## Designer feature protection

- Designer feature protection enables admins to limit access to the HTML tab and/or Litmus previews for content designers. However, the protection only applies to users who have read access to the *Designer Feature Access* entity. Users without this read access will always be able to see the HTML and Litmus features, even if you use designer feature protection to block them. To solve this, make sure all security roles provide read access to the *Designer Feature Access* entity. If you're using the out-of-box security roles supplied with the product, then these should automatically update to include this access when you apply the October 2018 (or later) update, but if you use custom security roles you need to add this access explicitly after updating. More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges).

## Event management

- If you disable anonymous registration for the event portal, then customer organizations must create a registerer account using the portal, after which the registerer can register as many attendees from their organization as needed. However, the registerer can't use the portal to create an account using an email address that belongs to a contact already in Dynamics 365. To set up an existing contact as a registerer, create a [portal invitation](/powerapps/maker/portals/configure/invite-contacts) and then send the invitation code to the contact by email.
- There are a few mismatches between the look of a Microsoft Teams webinar created from Customer Insights - Journeys and a webinar created from the Teams calendar. The discrepancies will be minimized in future versions. Until then, note that they don't cause any functional limitations as to how you, as the organizer, can manage the webinar through Customer Insights - Journeys. Refer to this section for more information: [Known issues with Teams webinars](teams-webinar.md#known-issues-with-teams-webinars).
- In the **Registration and attendance** tab of an event, there's an issue with filtering registration responses. Once a custom filter is applied for any column, responses from all events are displayed instead of only the ones relevant to the event. As a workaround, the **Advanced find** functionality can be used to filter registration responses for a particular event. Using **Advanced find**, select “Registration Responses” in the **Look for** dropdown and “Detailed registration responses” in the **Use Saved View** dropdown, then apply the appropriate filters. You can restrict the results to a particular event by filtering by the “Event” attribute of the “Event registration” relationship.
- Session passes aren't cloned in the **Save as** operation of an event. This will be fixed in future releases. Until then, manually add the passes for the sessions.
- For on-premises mailboxes, you cannot create a calendar item for the Teams webinar event organizer or for the speakers. This is a known limitation of Exchange REST APIs for on-premises mailboxes. In this case, you should share the event details (such as the Teams meeting URL) through a standard email to the event speakers.

## General

- The following features from the April 2019 release require that your instance has access to the latest Dynamics 365  infrastructure and services: *manage segment memberships from the contact record*, *session-level event registration*, *event-registration QR codes in email*, *portal-optional operation*, and some *segmentation improvements*. We're rolling out the needed infrastructure updates as quickly as possible, and most customers should have them already. If you're running the April 2019 release and require one or more of these features but don't have them available on your instance, [contact Microsoft Support](/power-platform/admin/get-help-support) to get your infrastructure updated right away.
- If you have different Dynamics 365 sessions open in other browser windows or tabs, and then open the Customer Insights - Journeys app in the same browser, it will authenticate using the same user that you have open in the other sessions. We recommend that you restart the browser each time you need to sign in using a different Dynamics 365 user account.
- Avoid deactivating publishable (go-live) records. Instead, change the publishing state (Status reason), and use the **Stop** buttons to manage records that are no longer required. More information: [Go live with publishable entities and track their status](go-live.md).
- Customer Insights - Journeys is currently supported only on the following browsers: Microsoft Edge, Google Chrome, and Apple Safari on Mac. More information: [Browser and system requirements](browser-requirements.md).
- Right-to-left (RTL) language support currently has the following limitations: the segmentation designer is usable, but shows its user-interface elements in the wrong order; and the supplied content samples (marketing page templates, email templates, form templates, and event website) aren't provided in RTL layouts.
- Diacritics (pronunciation marks placed above or below a letter) aren't supported in dynamic URLs in outbound marketing.

## Insights

- Web interactions registered for an anonymous visitor (on a tracked website, marketing page, marketing form, or redirect URL) don't currently become attributed to a contact record if those visitors later become known contacts. Though these interactions remain anonymous, you can still see them under the related entity (marketing page, website, etc.) and they're leveraged to compute the insights for each record. More information: [Websites](#websites) <!--- 1276305 -->
- Customer journey insights include a count of contacts that stopped their journey midway because the "Contact joined the suppression segment." In the current release,  this count may be unreliable. The suppression segment still works, and the contacts will be stopped correctly on joining it, but some of the contact numbers won't add up due to stopped contacts not getting counted here. <!--- 1348581 -->
- Email insights include a map showing where recipients were when they opened your message. For Gmail addresses, this information will often be inaccurate because of the way that Gmail caches embedded images. Geographical information can also be inaccurate for recipients using a VPN or a widely distributed corporate network.
- Date filtering doesn’t apply to top-10 links or links insights.

## Lead scoring and management

- Lead scoring results might take up to one hour to be calculated.
- When you're creating lead scoring rules, drop-down lists might not be localized for non-English languages.

## Marketing emails

- On some instances, emails that include date fields may fail the error check (with an "unsupported property type" error) and therefore can't go live. If you're affected by this issue, [contact Microsoft Support](/power-platform/admin/get-help-support), and ask them to update your instance with the known fix.
- The default content-settings record must be live before you can send any marketing emails or view heatmaps on **Insights** pages. Usually, the default content-settings record goes live automatically when your setup is complete, but sometimes this isn't the case. To solve this, set up and publish your default content-settings record manually as described in [Use content settings to set up repositories of standard and required values](dynamic-email-content.md#content-settings).
- Selecting **Stop** on a live email will prevent it from being used in future journeys, but it will continue to function in existing live journeys, which will continue to deliver it.
- If you reuse the same email multiple times (within the same journey or in different journeys), you'll see incorrect performance results on its **Insights** pages.
- Many email templates have placeholder images. You should replace these placeholder images with actual images so that marketing emails look professional.
- The email designer requires care when entering code for advanced dynamic content. It's easy to produce non-working code. If you want to use this feature, be sure to review the notes given in [How to enter code in the designer](dynamic-email-content.md#enter-code).
- If you create an email message with dynamic content that attempts to fetch a single value through a one-to-many database relation, then the system won't know which related record to fetch. As a result, the message will end in an error state when published to the sending service and will therefore never get sent (the error checking mechanism currently doesn't catch this error, which is why you can still publish it). An example of a one-to-many relation is the one between contacts and event registrations because each contact can register for multiple events. To prevent this error from occurring, use a for-each loop to enclose any expressions that reference a one-to-many relationship (this will loop through each related record). More information: [Add dynamic content to email messages](dynamic-email-content.md).
- Column padding doesn't always function correctly in new page templates. <!--- 1962146 -->
- Dotted column border styles don't render properly for one column layout in the email designer. <!--- 1942448 -->
- Subscription lists are managed at the *contact* level. If multiple contacts share the same email address, only the specific contact who opted out will stop receiving communications. Other contacts using the same email address will continue to receive communications. If you require opt-outs to be processed at the email level, you'll need to create custom processes. More information: [Manage subscriptions at an email level](set-up-subscription-center.md#manage-subscriptions-at-an-email-level).
- As of March 2021, A/B testing isn't yet available in the new email designer.
- If you have any email editor customizations, your administrator will need to manually recreate them in the new email designer.
- Due to a limitation in Outlook, the maximum divider height is 10 pixels.
- Image placeholders for emails created before the April 2022 release are shown in blue. <!--- 2689328 -->
- Adding a text link with **Add to calendar** functionality generates multiple errors. **Add to calendar** works properly for images and buttons. This error is related to event management only. <!--- 2965667 -->
- Sending emails without building a journey will not stop the user from selecting an email and a segment from different business units.

## Marketing pages and forms

- It's possible for contacts using browsers that don't respect HTML5 form validation (notably iOS devices) to submit marketing forms that don't include values for all required fields.
- When using [form capture](embed-forms.md#use-form-capture-to-integrate-a-form-created-externally), data model changes to mapped fields don't reflect in Customer Insights - Journeys until you manually refresh the marketing form capture page after making the change. <!--- 1798860 -->
- Previews for marketing pages with a single column section larger than 1000 px include a horizontal scrollbar by default. <!--- 1923424 -->
- The form capture tool may not be able to capture all non-Latin script characters correctly. Unrecognized characters are replaced by HTML codes. <!--- 1847623 -->
- Date field values aren't show in the **Insights** tab under **Submissions** for forms. <!--- 2039533 -->

## Reusable content blocks

- Any CSS styles that you include in your reusable content blocks could be overruled by styles in the document where you eventually host the content. If you want to prevent this, design your content blocks with inline styles that include the `!important` attribute.

## Segmentation

- Metadata used for building conditions and drop-downs shown on the designer isn't localized for non-English organizations. <!-- 992449 -->
- When trying to estimate the size of a segment where the query doesn't end in a contact, the system displays a server communication error. To correct this error, make sure your segment definition ends with a clause that links to the contact entity as described in [Design dynamic demographic or firmographic segments](segments-profile.md). <!-- 1226384 -->
- Segments that are created, activated, and exported from Customer Insights - Data, then published in Customer Insights - Journeys won't always display the segment members in Customer Insights - Journeys. <!-- 1874598 -->
- If you create a new static segment and then refresh the page before saving the segment at least once, it will revert to a dynamic segment and you'll need to start over to create a new static one. <!--- 1666195 -->
- In the Members view, you can sort by "Full name" and "Email" columns. Sorting by related entities or custom columns or views isn't supported. <!--- 215415458 -->

## Social posting

- When opening an existing social post, the old UI momentarily displays. <!--- 1927648 -->
- You cannot create a Facebook post that contains a GIF file *and* multiple images.

## Trials

- Trials are subject to the [Dynamics 365 Customer Insights - Journeys trial limits and restrictions](./trial-preview-limits.md).
- You can't use the sign-up process to add more users to a Customer Insights - Journeys trial that is running on a trial tenant without a mailbox set up for the organization admin. Instead, each new user must be added in a specific way. For more information, see [How can I add more users to a trial?](trial-faq.md#how-do-i-add-more-users-to-a-trial).
- You can't sign up using an \@microsoft.com email address. If you're a Microsoft employee and would like to sign up for a trial, start by setting up a Microsoft 365 E3 trial, which will provide you both with a trial tenant (where you can install the Customer Insights - Journeys trial) and a new email address that you can use to sign up for the Customer Insights - Journeys trial. More information: [Sign up for a free trial](trial-signup.md).

## Videos

- When you add a video to a marketing page, the **Designer** tab shows it as a thumbnail image rather than as an embedded video in an iframe. However, the embedded video iframe will still be shown correctly on the live page when you publish it. <!-- Provided as a tip -->

## Websites

- The *websites* feature records all visits to any web page that has a Customer Insights - Journeys tracking script on it. Each log entry includes a timestamp and, if possible, links to a known contact. If the visitor isn't a known contact, then that visit is logged as anonymous. The website tracking script sets a cookie, so the system can group visits into sessions, even for anonymous visits. When a contact submits a landing-page form, the system sets the same cookie (if not present already) and can thereafter match the cookie ID to a contact ID because the landing-page submission will either create or match a contact. Once a visitor is known, all future website visits will be logged with that user's ID. However, previous visits will remain anonymous (the system doesn't back-fill the contact ID to the existing visitor log).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
