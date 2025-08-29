---
title: Set up quiet times to prevent messages from being sent during unwanted hours
description: Learn how to set up quiet times to avoid sending messages during unwanted times.
ms.date: 08/28/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Set up quiet times to prevent messages from being sent during unwanted hours

Quiet times let you set specific periods when messages shouldn't be sent to customers, helping you avoid contacting them at inconvenient or inappropriate times. Customer message restrictions may be based on regulations, company policies, or other considerations. Common quiet times include overnight hours, weekends, and holidays. During these periods, the system holds messages and sends them only after the quiet time ends.

To set up quiet times, go to **Settings** > **Customer engagement** > **Quiet times**. If no quiet time setting exists, select the **New** button in the ribbon to get started.

Quiet times settings let you set detailed rules to respect customer time and meet local regulations. 

## Use time zone for quiet times

To set up quiet times, first choose the type of time zone the quiet times rules use. This choice is important because it determines how the quiet time rules are interpreted. 

:::image type="content" source="media/quiet-time-time-zone.png" alt-text="Set quiet times based on time zone." lightbox="media/quiet-time-time-zone.png":::

### Journey time zone

If you select the **Journey** time zone, the app uses the journey’s time zone to apply quiet times. For example, if you set the journey time zone to **(GMT-5:00) Eastern Time (US & Canada)**, quiet times and days for messages in the journey follow the selected time zone.

You can set the default journey time zone in **Settings** > **Journey Settings**. Individual journeys can have a different time zone that overrides the default.

### Audience time zone

If you choose the **Audience** time zone, quiet times use the time zone of each person in your audience. The system uses the time zone information for each contact, lead, or Customer Insights profile to apply quiet time rules.

Time zone information for each contact point type is set under **Audience configuration** > **Contact point type** > **Time zone field**. If needed, select a different time zone format field for each audience type (like contacts, leads, or Customer Insights profiles) and each contact point type.

> [!NOTE]
> If no time zone field is set under the audience configuration, quiet times use the journey time zone.

## Choose between general or advanced quiet times settings

The following sections outline two options when setting quiet times: *General* and *Advanced* quiet time settings. For advanced quiet time settings, you can create conditions based on specific attributes.

### General quiet times

General quiet times should be used when your audience is in a single geographical area or when you want to apply one simple, broad rule to avoid sending communications during certain hours. For example, you can apply one quiet time rule for the entire United States. General quiet times can also be used as default quiet time rules that apply if none of the advanced quiet time conditions are met.

:::image type="content" source="media/general-quiet-times.png" alt-text="An overview of general quiet times settings." lightbox="media/general-quiet-times.png":::

### Advanced quiet times

The advanced quiet times setting provides more specifications. It allows you to create multiple quiet time rules based on specific conditions, such as country/region, state/province, or phone number. For example, you can create a specific quiet time rule for the state of Texas and another for Alabama. This setting is beneficial for businesses with a diverse customer base spread across geographies. Using advanced settings, you can ensure that communications respect local regulations and time preferences.  

:::image type="content" source="media/advanced-quiet-times.png" alt-text="An overview of advanced quiet times settings." lightbox="media/advanced-quiet-times.png":::

> [!NOTE]
> When several advanced quiet-time rules are created, they're evaluated from top to bottom. The first matching rule is applied. If no rule matches, the app defaults to general quiet times if they were configured.

#### Create conditions for advanced quiet times

To create conditions for advanced quiet times, you need to specify the criteria for when the quiet times should apply. You can base the conditions on the following attributes

-	Country/region
-	State/province
-	Phone number

For example, you might set a specific quiet time to apply if the contact country/region is the United States and the state is Texas, or from a customer's area code within their phone number.

:::image type="content" source="media/quiet-times-set-conditions.png" alt-text="Create conditions for advanced quiet times." lightbox="media/quiet-times-set-conditions.png":::

> [!NOTE]
> When you're setting conditions to match specific values in your data, you need to account for variations in how those values might be recorded based on your database cleanliness. For example, if you're trying to match the state of Texas, your data might have different representations of Texas, such as "TX," "Texas," "tex," or "texas."

You can set conditions to ensure that your customer's situation matches all possible variations. You should add a new row for each variation of the value. For example, for Texas: if state equals Texas, or if state equals TX, or if state equals tex, and so on. Values are case sensitive. By setting multiple conditions, you ensure that your data is matched accurately.

To apply the quiet times, the system checks if each audience member meets the condition (based on the mapped fields) before the journey runs. For contacts and leads, the mapped attribute fields are prepopulated. To update the fields or add the mapping for a Customer Insights - Data profile, go to the **Attribute mapping** tab.

:::image type="content" source="media/quiet-times-attribute-mapping.png" alt-text="An overview of quiet times attribute mapping." lightbox="media/quiet-times-attribute-mapping.png":::

## Create quiet times rules 

Once you select a quiet time setting, you can define several specific rules to tailor your communication strategy.

:::image type="content" source="media/quiet-times-rules.png" alt-text="Screenshot of the quiet time rules configuration page." lightbox="media/quiet-times-rules.png":::

### Set different quiet times for commercial and transactional messages

You can set different rules for commercial and transactional messages. Many organizations prefer not to send commercial messages at odd hours to avoid annoying customers. However, they might want transactional messages (such as order confirmations or password resets) to be sent immediately, regardless of the time.

### Set different quiet times by message channel

You can also differentiate quiet times based on the communication channel. For example, customers might be more sensitive about receiving calls and text messages during off-hours compared to emails. Therefore, you can set stricter quiet times for text messages while allowing emails to be sent during a broader range of hours.

### Define weekly quiet hours

You can set specific days and times during the week when messages shouldn't be sent. Select **Edit** next to "No quiet time" for that channel. You can choose specific times and days for the quiet times. Select **Add** to specify multiple times and days of the week. For example, you could set up quiet times for email to be all day on the weekends and between 9:00 PM and 7:00 AM during the work week. Once you configure the quiet times for the channel, you see the settings reflected directly on the page next to that channel.

### Set up overnight quiet times

To set up quiet times overnight, create a separate evening quiet time and morning quiet time for each day. For example, if you don't want to send messages after 6:00 PM and before 8:00 AM, create two quiet time settings for the channel:
- One time for every day from 6:00 PM to midnight
- One time from midnight to 8:00 AM

> [!NOTE]
> You can set up quiet times for a maximum of three consecutive days, as otherwise it may cause the message queue to back up excessively, and messages aren't delivered. Quiet times only apply to content sent from journeys.

### Set up quiet dates

You can set up specific quiet dates when you don't want any messages to be sent, such as public holidays or company-wide events. To set up quiet dates, choose the channel and then edit the "Quiet date." Choose specific start and end dates when messages shouldn't be sent. You can use this interface to set up holidays or dates to prevent messages from being sent by the channel.

:::image type="content" source="media/quiet-times-dates.png" alt-text="Screenshot of the quiet dates configuration page showing options to select start and end dates." lightbox="media/quiet-times-dates.png":::

## Initial quiet time setting

The first time you create and save a quiet time setting, the system asks if you wish to apply it to all existing journeys and messages. If you select **Apply to all**, the system applies the quiet time setting to all compliance profiles. If you select **Decide later**, you can add the quiet time setting directly to any compliance profiles you want later. Once a quiet time has been added to a compliance profile, all messages designated with that compliance profile respect the quiet times configured.

> [!div class="mx-imgBorder"]
> ![Screenshot of the initial quiet time setting dialog, showing options to apply the setting to all journeys and messages or decide later.](media/real-time-marketing-quiet-times-initial-save.png "Screenshot of the initial quiet time setting dialog, showing options to apply the setting to all journeys and messages or decide later.")

## Quiet times and frequency caps

Quiet times and frequency cap settings are independent. If a message is held for quiet times, the system evaluates the frequency cap when it releases the message from the quiet times hold.

## Quiet times and compliance

Many organizations require quiet times for regulatory reasons. To set quiet times for messages, set the quiet time on the compliance profile that messages use. By setting quiet times on a compliance profile, you can have some compliance profiles that apply quiet times and others that don't. When you set up your first quiet time, the system asks if you want to apply it to existing journeys and messages. If you select **Yes**, the quiet time applies to all existing compliance profiles, journeys, and messages. If you select **No**, you can choose the quiet time you want to enforce later on specific compliance profiles.

## Quiet times and business units

If you use business units, the quiet times you create are available to all compliance profiles, journeys, and messages in your business unit. To set quiet times for different business units, create an individual quiet time setting in each business unit. If Business Unit Scoping for real-time journeys is enabled and you have access to multiple business units, you can choose which business unit the quiet time applies to.

[!INCLUDE[footer-include](./includes/footer-banner.md)]
