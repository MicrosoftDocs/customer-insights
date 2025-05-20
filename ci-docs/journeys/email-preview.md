---
title: Check your work using previews and test sends
description: Test and preview your email designs in Dynamics 365 Customer Insights - Journeys to ensure they look great across devices and email clients.
ms.date: 04/16/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:04/16/2025
---

# Check your work using previews and test sends

Your marketing email messages are seen by many potential customers, so make sure they look right when opened, regardless of the device and email software each recipient uses. Dynamics 365 Customer Insights - Journeys provides several tools to help you test and evaluate your design before you use it in an email campaign.

> [!IMPORTANT]
> Previews and test sends let you quickly test your design. However, not all features work with them. The following limitations apply:
>
> - [For-each loops](dynamic-email-content.md#for-each) don't render.
> - [Subscription center links](set-up-subscription-center.md#test-sub-center) open the subscription center page, but the page won't function.
> - You can test send the [double opt-in email](real-time-marketing-double-opt-in.md#double-opt-in-confirmation-email) layout but you can't test the actual logic behind it. This is because the logic depends on the compliance profile assigned to each audience and varies depending on how dynamic placeholders are resolved.
> - To test an email that contains placeholders that point to Dataverse tables, the user running the test must have [read permissions](role-permissions.md) for the tables.
> - To ensure [QR codes](email-qr-code.md) display correctly across different email clients, test them using a journey instead of the standard email test send or preview. Journey functionality uses a public link for the QR code image rather than embedding it with base64, which maintains consistent display quality across various email clients. 
>
> To test these features, create a simple customer journey that targets a small segment (such as one that includes a single contact with your email address) and sends the message you want to test.

## Preview your message in the designer

The email designer offers two types of previews when you're designing a marketing email message:

- **Standard preview**: Go to the **Email designer**, then select the **Preview and test** tab to see the standard designer preview. Choose between various form factors, contacts, and content settings. If your message contains personalization, enter sample data. Learn more in [Preview personalized content](real-time-marketing-preview-personalized-content.md).
- **Inbox preview**: Go to the **Email designer** > **Preview and test** > **Email clients** tab to see real-world inbox previews. These previews show your design as it appears in various target email clients and platforms.

See the next sections for details about each of these types of previews.

> [!NOTE]
> Microsoft Outlook supports local customizations and plugins, which can affect how messages are rendered. In some cases, recipients using customized Outlook installations may see odd layouts or repeated page elements when viewing pages designed in Dynamics 365 Customer Insights - Journeys. The standard or inbox preview displays can't simulate these effects. If necessary, you can use test sends to see how your designs look in specific Outlook configurations.

## Use the basic preview feature

Go to the **Email designer**, and then select the **Preview and test** tab to see an in-browser preview that simulates how your message is typically rendered on various form factors (desktop, tablet, or phone) and orientations (portrait or landscape).

Use the form factor icons in the right pane to switch between the available form factors for the preview. If your message contains personalization, you can enter sample data. Learn more: [Preview personalized content](real-time-marketing-preview-personalized-content.md)

<a name="inbox-preview"></a>

## Use the advanced inbox preview feature

Go to the **Email designer** > **Preview and test** > **Email clients** tab to see real-world inbox previews that show your design exactly as it will appear in a wide variety of target email clients and platforms. This feature renders your message by using native code from each of the listed target platforms and then delivers your preview as an image file showing the precise results.

The inbox preview is provided by a Microsoft partner called Litmus Software, Inc. ([litmus.com](https://litmus.com/)). Your Dynamics 365 Customer Insights - Journeys license includes 100 inbox previews per month. This quota is shared by your entire organization. After your organization uses all the available previews for the month, each user must set up their own Litmus account to create additional previews. Personal Litmus quotas apply to individual users, not to the entire organization. When you've used all your free previews, you are given the option to sign in to Litmus directly from the **Inbox Preview** tab in Dynamics 365 Customer Insights - Journeys. After you're signed in, the integration is seamless.

The **Email clients** tab displays a grid of icons, each labeled with the name of a different destination platform or email client. Initially, each preview is dimmed and shows a key (locked) icon, meaning you haven't generated that preview with your current design and settings. Select one of these icons to generate that preview and unlock its icon. Each time you unlock a preview, you'll use one preview from either your organization's or your personal quota. The unlocked preview remains available for viewing until you change the design or the **Properties** (dynamic text) settings, at which time all existing previews will no longer be valid and will be shown as locked again.

> [!NOTE]
> You must enable Litmus for your instance before using it. 
> - To enable Litmus in real-time journeys orgs only, go to **Feature switches** > **Email editor** > **Litmus integration**. 
> - To enable Litmus in outbound marketing *and* real-time journeys orgs, go to **Default settings** > **Marketing emails** > **Enable Litmus integration**.

## Send a test message

Select **Test Send** on the command bar to send your current design to one or more email addresses. This command initiates an [error check](email-check-golive.md#error-check). If your message passes the error check, a flyout panel opens asking you to specify the following:

- **Email address**: Enter one or more target email addresses (comma-separated). You'll typically just use your own email address here.
- **Test contact**: Select a contact record to supply values for dynamic content (such as a first name in the salutation). For a live message, these values come from the contact record for each individual recipient.
- **Test content settings**: Select a content-settings record to supply values for dynamic content (such as a subscription-center URL or the sender's postal address). For a live message, the content-settings record is specified by the customer journey that sends the message.

Select the **Save** button at the bottom of the flyout panel to send the message to your specified email addresses.

> [!NOTE]
> - You can test-send draft *and* live email messages, so you don't need to go live to do a test send. In a live email message, select the three dots on the right of the command bar to see the **Test send** button.
> - Email analytics aren't affected by the test-send feature.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
