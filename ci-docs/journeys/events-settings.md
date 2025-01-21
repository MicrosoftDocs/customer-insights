---
title: Set up event administration options and webinar provider accounts in outbound marketing
description: Set options for event administration and configure connections to your webinar provider accounts in outbound marketing.
ms.date: 01/03/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Set up event administration options and webinar provider accounts in outbound marketing

[!INCLUDE [azure-ad-to-microsoft-entra-id](./includes/azure-ad-to-microsoft-entra-id.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

The **Event management** settings let you set up the connections to your webinar provider accounts and set up a few defaults for event administration. 

To find these settings, open **Settings** and then choose one of the pages under the **Event management** heading in the leftmost column. You can also access these same settings by finding the **Event management** section in the Settings overview.

See the remaining sections of this topic for information about how to work with each page in the **Event management** section.

## Web applications

The **Settings** > **Event management** > **Web applications** settings enable you to register web applications, which is required if you develop custom features that use the events API to interact programmatically with event features. This is mostly of interest to developers rather than administrators. 

For more information about how to use the events API, including how to use the **Web applications** settings, see [Using the Events API](developer/using-events-api.md) and [Register your web application to use Events API](developer/register-web-application-events-api.md).

You also need to register a web application if you decide to host your event website on Azure. More information: [Host your custom event website on Azure](developer/host-custom-event-website-on-azure.md)

<a name="webinar-config"></a>

## Webinar providers

A *webinar provider* is an app or service that hosts webinars. The provider accepts registrations, provides URLs where the presenter and participants can join each webinar, and also provides a server to run the webinar itself. Providers typically also deliver attendance statistics and other webinar features. Customer Insights - Journeys does not provide its own hosting capability, but you can [use Microsoft Teams as a webinar hosting provider](teams-webinar.md). Microsoft Teams is the preferred provider to use for webinars. You can also sign up with a [third-party provider](set-up-webinar.md) and then configure Customer Insights - Journeys with the details needed to connect to that provider.

Each webinar provider that you use must have a record listed on the **Webinar providers** page. For each account that you have with your webinar provider, you must also set up a **Webinar configuration** record as described in the next section.

> [!IMPORTANT]
> In most cases, you should never modify or add any records on the the **Webinar providers** page. Microsoft has partnered with a third-party webinar provider called [On24](https://www.on24.com/). When you open the **Webinar providers** list page, you'll see that a preconfigured **On24** record is already listed here. In nearly all cases, you shouldn't edit or delete this record unless you want to specify an alternative terms-of-service and/or privacy policy URL. Likewise, there is usually no reason to add another provider record here unless you have partnered with a developer who has added a deeply customized solution for your organization. Also, the authorization credentials for your On24 account aren't managed by the webinar provider record, but by a webinar configuration record. See [Webinar configurations](#webinar-config), later in this topic, for details about how to connect to your On24 account.

You can view your webinar providers by going to **Settings** > **Event management** > **Webinar providers**. But as mentioned, you usually shouldn't do anything here. If you do open or create a record here, you'll find the following settings:

- **Name**: Shows the name of the provider.
- **Base service URL**: For On24, this can be blank. If your system has been customized to support another provider, then please contact your development team for instructions on how to use this.
- **Max duration in minutes**: Shows the maximum number of minutes that your provider allows for a single session. Any webinars that are longer than this must be broken down into multiple sessions.
- **Terms of service**: Shows the URL for your webinar provider's terms of service. Select the globe button to open this URL in a new browser tab. This link is provided to Dynamics 365 Customer Insights - Journeys users when they are in the process of enabling webinar functionality, which requires them to agree to these terms. A link to the standard On24 terms of service is provided by default. You might edit this if you prefer to use an alternative URL.
- **Privacy policy**: Shows the URL for your webinar provider's privacy policy. Select the globe button to open this URL in a new browser tab. This link is provided to Dynamics 365 Customer Insights - Journeys users when they are in the process of enabling webinar functionality, which requires them to agree to this policy. A link to the standard On24 privacy policy is provided by default. You might edit this if you prefer to use an alternative URL.
- **Update credentials**: Unless your system has been customized to use a provider other than On24, don't use these settings (and even then, contact your development team for advice). Instead, see [Webinar configurations](#webinar-config), later in this topic, for details about how to connect to your On24 account.

## Webinar configurations for third-party providers

After you have set up an account with your third-party webinar provider (probably On24), you must enter your account details to enable Dynamics 365 Customer Insights - Journeys to authenticate and interact with it. Even if you use just one webinar provider, you might have several accounts with that provider, and can configure each of them as needed.

> [!NOTE]
> Each time you [set up an event or session as a webinar](set-up-webinar.md) (or hybrid), you must choose a webinar configuration. This is how you can control which account you'll be using for that event or session.

To connect to a webinar account or update your account credentials:

1. Go to **Settings** > **Event management** > **Webinar configurations**. Here you'll see a list of existing configurations (if any), and tools for adding new ones.

1. To edit an existing configuration, select it from the list; to create a new configuration, select **New**. (You can also delete or deactivate a record by selecting it in the list and then selecting the appropriate button on the command bar.)

1. Make the following settings:
    - **Name**: Enter a name for the account.
    - **Webinar provider**: Select the name of the webinar provider record (set up as described in the previous section).

1. The following read-only information is also provided here, some of which may be useful for troubleshooting:
    - **Terms of service**: Displays the URL where your provider lists their terms of service. This value comes from the selected **Webinar provider** record. Select the globe button to open this URL in a new browser tab.
    - **Privacy policy**: Displays the URL where your provider details their privacy policy. This value comes from the selected **Webinar provider** record. Select the globe button to open this URL in a new browser tab.
    - **Last metrics update**: Shows the last date and time that your provider returned usage statistics (such as attendance records) to Dynamics 365 Customer Insights - Journeys.
    - **Provider service status**: Shows the current status of the provider service and your connection to it.
    - **Message**: Displays a custom message sent by the provider (typically related to the displayed status).

1. Open the **Credentials** tab. Do one of the following:
    - If you are editing an existing configuration and need to change your credentials, then set **Update credentials?** to **Yes** to expose the credentials settings.
    - If you are creating a new configuration, then the credentials settings are already shown here.

1. Make the following settings:
    - **Client ID**, **Access token key**, and **Access token secret**: These values identify your account and provide authentication (sign-in) credentials for accessing it and communicating with your webinar provider. You should have received these values when you signed up for the account. Please contact your webinar provider if you need help finding these values.

1. Select **Check** on the toolbar to confirm that your credentials are working.

1. Save your work.

<a name="event-admin"></a>

## Event administration

Use the **Event administration** settings to set up a few standard options for your events, including email options, email templates, and default payment gateway. These settings are optional.

To set your event-administration options:

1. Go to **Settings** > **Event management** > **Event administration**. Here you'll see a list of existing event-administration records (if any), and tools for adding new ones. Note the following:
    - You can only have one active event-administration record at a time.
    - If no event-administration records are shown, then select **New** on the command bar to create one.
    - If an event-administration record already exists, then select it to open it.
    - To delete an existing event-administration record, select it and choose **Delete** on the command bar.
    - If you'd like to temporarily disable an existing event-administration record, possibly so you can create a new one to use in the meantime, then select the existing record and choose **Deactivate** from the command bar. To view, edit, and/or reactivate a deactivated record, switch to the **Inactive event administration** view using system view menu (above the list).
1. Make the following settings:
    - **Name**: Enter a name for the current event-administration record.
    - **Match contact based on**: Choose the strategy to use when matching a new event registration to an existing contact record. If a contact record is found that has matching values for *all* of the fields you choose here, then the registration will be linked to that contact record. If no match is found, then a new contact will be created and linked to the new registration record. You can choose to match by email alone; first name and last name; or email, first name, and last name. Learn more: [Set form matching](mkt-settings-matching.md).
    - **Enable demo payment confirmation**: This feature lets you simulate payment on the event website for demo purposes. Set this to **Yes** to enable demo payment. Set it to **No** to disable demo payment. To [enable online payment on a production site](event-payment-gateway.md), you must partner with a third-party payment provider and customize your event site to work with their system. Never enable demo payment on a production system because it can introduce a security vulnerability.

    > [!WARNING]
    > You must only set **Enable demo payment confirmation** to **Yes** when presenting a demo of the event website. You must always set this to **No** before going to production because the simulated-payment feature can introduce a security vulnerability if enabled in a production environment.

    > [!NOTE]
    > To make the name-based contact matching strategy work with [Microsoft Entra ID](/azure/active-directory/fundamentals/whatis), you must provide first name and last name on sign-up. More information [Configuration for Microsoft Entra ID](developer/self-hosted.md#configuration-for-microsoft-entra-id).
    > 
    > To make the name-based contact matching strategy work with **Portal Authentication** it is mandatory to provide first and last name after registering.

    > [!NOTE]
    > It's not possible to deduplicate registrations for the same contact for out-of-the-box marketing events. When duplicate registrations are made for the same contact, a new registration is created for the contact.

    > [!NOTE]
    > The email templates provided for sending confirmations to the event purchaser and/or attendee are hard-coded, so you can't customize or translate their content. If you require custom messaging, then set up a [customer journey](customer-journeys-create-automated-campaigns.md) with event, trigger, and email tiles.

## Website table configurations

The **Settings** > **Event management** > **Website table configurations** settings enable you to expose custom fields through the events API. This can be useful if you develop custom features that use the events API to interact programmatically with event features. This is mostly of interest to developers rather than administrators. 

For more information about how to use the events API, including how to use the **Website table configurations** settings, see [Using the Events API](developer/using-events-api.md) and [Customize the response from Events API](developer/customize-events-api-response.md).

## Privacy notice

[!INCLUDE [cc-privacy-events-webinar](./includes/cc-privacy-events-webinar.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
