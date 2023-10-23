---
title: Create outbound text messages 
description: Learn how to create outbound text messages for Dynamics 365 Customer Insights - Journeys
ms.date: 10/23/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create outbound text messages

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

Text messages (SMS) allow you to reach customers directly on their mobile devices. You can send text messages from Dynamics 365 Customer Insights - Journeys by generating a phone number to use within the app. This article explains how to add a phone number generated in the Azure Communication Services preview, Infobip, LINK Mobility, Telesign, Twilio, or Vibes and how to create and send text messages in Customer Insights - Journeys.

> [!NOTE]
> Text messaging using a toll-free number generated in the Azure Communication Services preview is only supported in the countries/regions listed below.
>
>| Supported countries/regions | Supported type | Legal designation | Range    |
>|---------------------|----------------|-------------------|----------|
>| United States                 | Toll-free      | Transactional     | Domestic |


As [discussed below](real-time-marketing-outbound-text-messaging.md#track-your-text-message-metrics-from-channel-insights), the Customer Insights - Journeys app tracks text messaging metrics for channel insights purposes, including incoming SMS responses.

## Add a sender number using the Azure Communication Services free trial preview (US only)

To generate an Azure Communication Services free trial preview phone number to use in Customer Insights - Journeys, go to **Settings** in the area switcher menu. Then go to **Customer engagement** > **Azure SMS preview** and select **+New text message sender** on the top ribbon.

Once you agree to the *Voice and text message terms* and select your country or region, you’ll be provided with a toll-free United States phone number.

> [!div class="mx-imgBorder"]
> ![Generate phone number screenshot.](media/real-time-marketing-text-number.png "Generate phone number screenshot")

Toll-free numbers are a good option for transactional A2P messaging, which means sending automated messages to large groups. Toll-free numbers don’t require template registration, so once you get a number you can immediately start sending messages.

> [!NOTE]
> During the Azure Communication Services free trial preview, the text message service is limited to a single toll-free phone number with a limited number of outbound messages per month (1,000 per organization). The phone number you receive will be your dedicated number for the duration of the preview.
> 
> If you want to integrate an already active Azure Communication Services subscription, refer to the section below instead.

> [!TIP]
> Carriers, just like email providers, have ways of filtering spam messages. This results in the phone number being blocked and becoming unusable. Due to carrier filtering, you should only use toll-free numbers for transactional messages (as opposed to promotional messages). You should avoid sending promotional content or misleading information. Promotional content includes free products or discount offers.
>
>**UPDATE:** With carriers becoming even more strict with filtering, to ensure the maximum deliverability for your text messages, the toll-free number now needs to be verified. To verify your number, fill in the form [here](https://forms.office.com/r/x3LCH1gS7b). You can learn more about Azure Communication Services toll-free number verification [here](/azure/communication-services/concepts/sms/sms-faq#toll-free-verification).

## Add a sender number from an active Azure Communication Services subscription (worldwide)

You can purchase or reuse an existing Azure Communication Services subscription to send text messages in Customer Insights - Journeys. The integration works for all countries in which a phone number can be purchased. Customer Insights - Journeys also supports Alphanumeric Sender IDs.

### Sign up for and configure an Azure Communication Services subscription

Azure Communication Services (ACS) integration uses its API to send and receive text messages. You need to sign up for an Azure Communication Services account to enable the Customer Insights - Journeys SMS integration. To create an Azure Communication Services account:

1. Go to [Azure](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) and sign up for a "Pay as you go" account.
1. [Create a Communication Services resource](/azure/communication-services/quickstarts/create-communication-resource?tabs=windows&pivots=platform-azp) and get a [toll-free number](/azure/communication-services/quickstarts/telephony/get-phone-number?tabs=windows&pivots=platform-azcli), a [short code](/azure/communication-services/quickstarts/sms/apply-for-short-code), or an [Alphanumeric Sender ID](/azure/communication-services/quickstarts/sms/enable-alphanumeric-sender-id).
1. Go to your [Azure account homepage](https://ms.portal.azure.com/#home) and navigate to your resource through **Subscriptions** > **Resource groups** > **Resource name**.
1. Go to **Keys** under **Settings** and jot down the Primary and Secondary Connection String values. These values are required to create the integration between Customer Insights - Journeys and Azure Communication Services.
1. Under **Telephony & SMS**, go to **Phone Numbers** to find the toll-free number you want to use as a sender. Go to **Alphanumeric Sender ID** and to **Short Codes** for the respective types of numbers.

## Add a sender number from an Infobip, LINK Mobility, Telesign, Twilio, or Vibes account (worldwide)

You can purchase or reuse an existing Infobip, LINK Mobility, Telesign, Twilio, or Vibes SMS account to send text messages in Customer Insights - Journeys. **The integration works for all countries** in which a phone number can be purchased from the relevant SMS provider. 

The sender types supported vary based on the selected provider. **Customer Insights - Journeys also supports Alphanumeric Sender IDs**.

> [!IMPORTANT]
> To ensure that third-party SMS providers handle STOP commands properly, you must configure your consent settings directly with the provider.

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

### Sign up for and configure a Vibes account

Vibes integration uses Vibes's public APIs to send and receive text messages. You need to sign up for a Vibes account to enable Vibes SMS integration. To create a Vibes account:  
  
1. Send an email to [dynamics@vibes.com](mailto:dynamics@vibes.com). You will get a response within a business day.
1. After your account is set up or if you are already a Vibes customer, contact the Vibes customer care team ([live@vibes.com](mailto:live@vibes.com)) or your dedicated customer success manager to request the account integration details required to create the integration between Customer Insights - Journeys and Vibes.

### Set up your Azure Communication Services, Infobip, LINK Mobility, Telesign, Twilio, or Vibes sender numbers in the Customer Insights - Journeys app

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

You can view all active provider integrations in the **SMS providers** tab. You can also edit, update, delete, or add more numbers to an existing integration.

## Create text messages

After you add your phone number, you can start authoring text messages by going to **Customer Insights - Journeys** > **Channels** > **Text messages** and selecting **+New text message** in the top ribbon. This will take you to the text messaging editor.

> [!div class="mx-imgBorder"]
> ![Text editor screenshot.](media/real-time-marketing-text-editor4.png "Text editor screenshot")

To create a message:

1. Select the message sender. The **Text message sender** dropdown lets you choose from the sender phone numbers (Azure Communication Services preview, Twilio, or TeleSign) you’ve added.
1. Enter your message content. You can enter text, emojis, and [personalized content](real-time-marketing-outbound-text-messaging.md#personalize-text-messages).
1. Choose whether your message designation is **Commercial** or **Transactional**. A commercial message is one that is sent to recipients who have opted-in to receive messages. An example is a coupon sent to a group of customers who opted-in to receive promotional offers from your company. A transactional message is one that is sent in response to a transaction the recipient previously started with you. An example is a response to an email inquiry.

> [!IMPORTANT]
> In the text messaging editor, the message designation is preselected as transactional for numbers that might be prone to carrier filtering if used for promotional or marketing messaging. To make sure your number isn't blocked by carriers, it's highly recommended to use this number for transactional messaging only.

Before sending your message, select the **Check content** button in the upper right. This will run an error check on the message, much like the error check functionality in the email designer.

Next, test your message by selecting the **Test send** button in the upper right. If you’re using an Azure Communication Services preview toll-free sender number, you can test send the message to any United States mobile number. If you’re using a Twilio or TeleSign sender number, you can send the message to a mobile device in any supported country. You can also add the message to a journey to see how it can be triggered by events.

## Personalize text messages

Personalizing text messages allows you to insert dynamic data that is unique to each message recipient. You might want to dynamically populate a name, an appointment time, a location, or any other unique data.

To personalize a text message:

1. Select the **Personalization** ![The Personalization button.](media/real-time-marketing-personalization2.png "The Personalization button") button in the **Message** field.
1. Select **Select a data field** to choose a data source. Your data source can be based on an **Audience**, a **Trigger**, or **Compliance**.
1. After choosing the data source, you can search for the specific attribute or trigger you want.
1. Add a **Label** to quickly identify your token in the message content.

When you send the text message from a journey, it will automatically populate the token according to the attribute you selected.

## Add a Customer Voice survey to a text message

Adding a Customer Voice survey link to a text message or [push notification](real-time-marketing-push-notifications.md#add-a-customer-voice-survey-to-a-push-notification) allows you to seek feedback from customers on the channels they use the most.

To add a Customer Voice survey to a text message:

1. Select the **Customer Voice survey** button ![The Customer Voice survey button.](media/real-time-marketing-customer-voice.png "The Customer Voice survey button") in the **Message** field.
1. Choose a Customer Voice survey in the lookup field.
1. Select whether you want the survey to be anonymous and whether you want to track the survey link after customers click on it. If you select the **Survey is anonymous** option, no user data will be saved with the answers.
    > [!div class="mx-imgBorder"]
    > ![Customer Voice survey options screenshot.](media/real-time-marketing-survey-options.png "Customer Voice survey options screenshot")
1. Select **Save**.

When you send the text message from a journey, it will automatically populate the token with the survey and options you selected.

## Add SMS keywords to a text message

Adding SMS keywords in your text message allows you to use them in your customer journey to branch it based on your customer’s response to your text messages.  
 
To add a keyword to a text message:
 
1. Select the keyword icon.
2. Type the keyword that you’d like to add.
3. Select it from the list if it has been used previously in the journey or select the **New keyword** button to create it.

The following screenshot shows how to add SMS keywords in your text message.

> ![Add SMS keywords screenshot](media/add-sms-keywords.png "[Add SMS keywords screenshot")
 
All keywords created through the SMS editor are also added to the [SMS keywords page](manage-sms-keywords.md ).
 
## Track your text message metrics from channel insights

You can see how customers react to your text messages by checking the text message analytics in the message itself and within journeys.

> [!NOTE]
> Delivery reports for text messages are received from different carriers in every country or region. This might result in false positives or negatives at times, depending on the carrier. Consider this when you check the delivery reports of your text messages.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
