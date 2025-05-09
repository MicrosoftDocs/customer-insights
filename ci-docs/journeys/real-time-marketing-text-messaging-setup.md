---
title: Set up outbound text messaging
description: Learn how to set up outbound text messaging in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/31/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Set up text messaging

This article explains how to setup and configure providers and phone numbers for text messages.

> [!NOTE]
> Customer Insight - Journeys offers native integration with Azure Communication Services, Infobip, LINK Mobility, Telesign, Twilio, or Vibes (US and Canada). You can bring your own provider by creating up a [custom channel](real-time-marketing-create-custom-channels.md).

## Sign up for and configure your text messaging provider

You can purchase or reuse an existing Azure Communication Services, Infobip, LINK Mobility, Telesign, Twilio, or Vibes SMS account to send text messages in Customer Insights - Journeys. 

The sender types supported vary based on the selected provider. **Customer Insights - Journeys also supports Alphanumeric Sender IDs**.

> [!IMPORTANT]
> To ensure that third-party SMS providers handle STOP commands properly, you must configure your consent settings directly with the provider.

### Sign up for and configure an Azure Communication Services subscription

Azure Communication Services (ACS) integration uses its API to send and receive text messages. You need to sign up for an Azure Communication Services account to enable the Customer Insights - Journeys SMS integration. To create an Azure Communication Services account:

1. Go to [Azure](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) and sign up for a "Pay as you go" account.
1. [Create a Communication Services resource](/azure/communication-services/quickstarts/create-communication-resource?tabs=windows&pivots=platform-azp) and get a [toll-free number](/azure/communication-services/quickstarts/telephony/get-phone-number?tabs=windows&pivots=platform-azcli), a [short code](/azure/communication-services/quickstarts/sms/apply-for-short-code), or an [Alphanumeric Sender ID](/azure/communication-services/quickstarts/sms/enable-alphanumeric-sender-id).
1. Go to your [Azure account homepage](https://ms.portal.azure.com/#home) and navigate to your resource through **Subscriptions** > **Resource groups** > **Resource name**.
1. Go to **Keys** under **Settings** and jot down the Primary and Secondary Connection String values. These values are required to create the integration between Customer Insights - Journeys and Azure Communication Services.
1. Under **Telephony & SMS**, go to **Phone Numbers** to find the toll-free number you want to use as a sender. Go to **Alphanumeric Sender ID** and to **Short Codes** for the respective types of numbers.

### Sign up for and configure an Infobip account

Infobip integration uses its public APIs to send and receive text messages. You need to sign up for an Infobip account to enable the Customer Insights - Journeys SMS integration. To create an Infobip account:

1. Go to [Infobip](https://www.infobip.com/signup?signup_source=MicrosoftDynamicsMarketing) and sign up for a free account that can be upgraded to pay-as-you-go or a monthly subscription later.
1. In your Infobip [Account homepage](https://portal.infobip.com/homepage/), navigate to the **Developers** tab and note the **API key** and **API Base URL** values. These values are required to create the integration between Customer Insights - Journeys and Infobip.
1. [Purchase SMS phone numbers](https://portal.infobip.com/apps/sms) through your Infobip account.

### Sign up for and configure a LINK Mobility account

Like Infobip, LINK Mobility integration uses their public APIs to send and receive text messages. You need to sign up for a LINK Mobility account to enable the Customer Insights - Journeys SMS integration. To create an LINK Mobility account:

1. Go to [LINK Mobility](https://www.linkmobility.com) and sign up for a trial account that can be upgraded later.
1. [Contact the link mobility team](https://www.linkmobility.com/contact-us) to purchase numbers and get all the account integration details required to create the integration between Customer Insights - Journeys and LINK Mobility.

### Sign up for and configure a TeleSign account

TeleSign integration uses TeleSign's public APIs to send and receive text messages. Also, like Twilio, you’ll need to sign up for a TeleSign account to enable TeleSign SMS integration. To create a TeleSign account:  
  
1. Go to [TeleSign](https://portal.telesign.com/signup) and sign up for a trial account. If you expect to send high volumes of SMS traffic (more than 100,000 messages per month), contact TeleSign to request an invoiced enterprise account.
1. In your TeleSign account [Dashboard](https://portal.telesign.com/portal/dashboard), note the **CUSTOMER ID** and **API KEY** values. These values are required to create the integration between Customer Insights - Journeys and TeleSign.
1. Purchase SMS phone numbers through your TeleSign account.
1. On the [TeleSign SMS Settings](https://portal.telesign.com/portal/sms-settings) page, switch the **Status Callback** toggle to **Enabled.** This applies to **Standard accounts**. If you have an **Enterprise account**, you’ll need to contact TeleSign to enable the status callback setting for you.

### Sign up for and configure a Twilio account

Like Telesign, Twilio integration uses Twilio's public APIs to send and receive text messages. You need to sign up for a Twilio account to enable Customer Insights - Journeys SMS integration. To create a Twilio account:  
1. Go to [Twilio](https://www.twilio.com/try-twilio) and sign up for a trial account that can be upgraded to pay-as-you-go. If you expect to send high volumes of SMS traffic (more than 100,000 messages per month), contact Twilio to request an invoiced enterprise account.
1. In your Twilio account [General Settings](https://console.twilio.com/us1/account/manage-account/general-settings), note the **ACCOUNT SID** and **AUTH TOKEN** values. These values are required to create the integration between Customer Insights - Journeys and Twilio.
1. [Purchase SMS phone numbers](https://console.twilio.com/us1/develop/phone-numbers/manage/search?frameUrl=%2Fconsole%2Fphone-numbers%2Fsearch%3Fx-target-region%3Dus1&currentFrameUrl=%2Fconsole%2Fphone-numbers%2Fsearch%3FisoCountry%3DUS%26types%255B%255D%3DLocal%26types%255B%255D%3DTollfree%26capabilities%255B%255D%3DSms%26capabilities%255B%255D%3DMms%26capabilities%255B%255D%3DVoice%26capabilities%255B%255D%3DFax%26searchTerm%3D%26searchFilter%3Dleft%26searchType%3Dnumber%26x-target-region%3Dus1%26__override_layout__%3Dembed%26bifrost%3Dtrue) through your Twilio account.

### Sign up for and configure a Vibes account (US and Canada only)

Vibes integration uses Vibes's public APIs to send and receive text messages. You need to sign up for a Vibes account to enable Vibes SMS integration. To create a Vibes account:  
  
1. Send an email to [dynamics@vibes.com](mailto:dynamics@vibes.com). You'll get a response within a business day.
1. After your account is set up or if you're already a Vibes customer, contact the Vibes customer care team ([live@vibes.com](mailto:live@vibes.com)) or your dedicated customer success manager to request the account integration details required to create the integration between Customer Insights - Journeys and Vibes.

## Set up your provider in the Customer Insights - Journeys app

To set up a new SMS provider for the Customer Insights - Journeys app:

1. Go to **Settings** in the area switcher menu. Then go to **Customer engagement** > **SMS providers** and select **+New** in the top menu.
1. Select the provider you want to set up and then add an internal name and description, along with the business unit it should belong.
1. If you selected Infobip, enter the **API key** and **API Base URL** noted in the steps above. If you selected TeleSign, enter the **Customer ID** and **API key**. If you selected Twilio, enter the **Account SID** and **Auth Token**. If you selected LINK Mobility, contact them first to provide you with the integration credentials. Add them and then select the **Next** button.
1. On the next screen, select **+New phone number** to add one or more numbers that will be used for the integration.
1. On the **Add phone number** pane, add the number, its friendly name to distinguish it, the business unit it belongs, and its type. **Customer Insights - Journeys also supports Alphanumeric Sender IDs**.
    > [!div class="mx-imgBorder"]
    > ![Add SMS number screenshot.](media/real-time-marketing-add-sms-number.png "Add SMS number screenshot")
1. After adding the numbers, select the **Next** button to review the setup details and then select **Done** to complete it. 
1. To receive SMS replies through the providers using the numbers you set up, you also need to specify and set up the **Callback URL**.

    > [!div class="mx-imgBorder"]
    > ![Callback URL screenshot.](media/real-time-marketing-text-message-callback-url.png "Callback URL screenshot")

   For Azure Communication Services, navigate to your resource group through **Subscriptions** > **Resource group name** and create an Event Grid System Topic for your Communication Service resource. Select it and then select **+ Event Subscription**. To set up the **Delivery report Callback URL**, select “**SMS Delivery report received**” in the **Event type** and **Webhook** in the **Endpoint type**, pasting the relevant URL you see in the Customer Insights – Journeys setup wizard. To set up the **Incoming Message Callback URL**, select “**SMS received**” in the **Event type** and **Webhook** in the **Endpoint** type, pasting the relevant URL you see in the Customer Insights – Journeys setup wizard. 

   For Twilio, copy the **Callback URL** from the Customer Insights - Journeys app and paste it into the [numbers' configuration page](https://console.twilio.com/us1/develop/phone-numbers/manage/incoming) in the **"A MESSAGE COMES IN"** field.

    > [!div class="mx-imgBorder"]
    > ![Twilio number config screenshot.](media/real-time-marketing-text-message-twilio-config.png "Twilio number config screenshot")

For Infobip, LINK Mobility, Telesign, and Vibes, you'll need to contact customer support to set this up for you.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
