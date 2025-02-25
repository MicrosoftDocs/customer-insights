---
title: Create a segment-based journey
description: Create a segment-based journey in Dynamics 365 Customer Insights - Journeys. Learn how to send announcements and nurture campaigns to your most valuable customers.
ms.date: 02/24/2025
ms.topic: article
author: alfergus
ms.author: colinbirkett
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Create a segment-based journey

You can use segment-based journeys to create outbound journeys like sending out announcements or a nurture campaign. To create journeys that can react to customers' actions in real time, see [Create a trigger-based journey](real-time-marketing-trigger-based-journey.md).

## Creating a segment-based journey to send an announcement

To illustrate the capabilities of segment-based journeys, we create a simple journey that sends an announcement to your most valuable customers about an upcoming product. If the customers show interest in the product by clicking the product link, we send them a follow-up message when the product is launched.

## Prerequisites

### Create segments

Create a segment of your *Most valuable customers*. You can [create your own contact or lead-based segment](real-time-marketing-build-segments.md). Segment-based journeys can also [work with segments from outbound marketing and segments from Customer Insights - Data](real-time-marketing-segments.md).
- If you choose to use outbound marketing segments, the email and text content must use **Contact** as the audience data for personalization.
- If you choose to use Customer Insights - Data segments, the email and text content must use **Customer Profile** as the audience data for personalization.

### Create email and text messages

- **Product announcement email**: Initial email announcement that is sent to your *most valuable customers*. This email must contain a link to the new product.
- **Product launched text message**: Follow-up text message that's sent after the product is launched. This follow-up message is sent only to customers who clicked the link in the first email.

You can build the journey while the content is in the **Draft** state. To publish and go live with the journey, the content must be in the **Ready to send** state.

## Set the journey start

:::image type="content" source="media/segment-journey-allow-individuals.png" alt-text="Create a segment-based journey." lightbox="media/segment-journey-allow-individuals.png":::

To create a segment-based journey, go to **Engagement** > **Journeys** and select **+New journey** in the top toolbar. A window opens allowing you to use [Copilot to create a journey](real-time-marketing-use-copilot-create-journey.md). To create a segment-based journey manually, select the **Skip and create from blank** button.

On the "Create a new journey" screen:

- Create a name for the journey
- Select **Segment-based** for the journey type. Customers start a segment-based journey when they qualify to be part of a segment.
- Select one or more segments. Note the following when selecting multiple segments:
  - The total combined member count of all segments can't exceed the limit noted [here](real-time-marketing-known-issues.md#segments) for a journey. You can select at most 15 segments (or fewer if the segment size limit is reached sooner).
  - Outbound marketing segments or mixed audience types (for example, contacts and leads) can't be selected.
  - Environments that use their own [Azure Data Lake storage account](../data/own-data-lake-storage.md#connect-customer-insights---data-with-your-storage-account) aren't supported.
- Choose the **frequency** at which your journey should run:
  - A **one-time** journey with a **static** audience that runs one time. When the journey starts, the current members of the segment start the journey.
  - A **one-time** journey where **newly added members can start at any time**. This journey responds to changes in the segment membership, letting more people start the journey after it starts. When the journey starts, the current members of the segment start the journey. Newly added segment members start the journey when the segment is refreshed. If "Allow audience members who re-join the segment to re-eneter the journey" *isn't* selected, each person goes through the journey only one time even if they're removed and later added back to the segment. If that option *is* selected, a person leaving the segment and then re-joining goes through journey again. 
    - Selecting the "Allow audience members who re-join the segment to re-eneter the journey" option enables advanced scenarios such as this: A business wants to maintain two segments of “Active” and “Inactive” customers and has journeys specific to such segments. Customers who make a purchase are placed in the “Active” segment whose journey promotes other products. After some time, these customers may be moved to the “Inactive” segment where they get different communications (for example, offers to come back). When customers in the "Inactive" segment make a purchase, they are moved back into the “Active” segment. This option allows the business to control whether such "re-joined" people can start the journey for the “Active” segment once again.  
  - A **repeating** journey runs on a schedule that you define. Every time the journey reaches the scheduled run time, all current members of the segment start the journey. Members added to the segment between the scheduled run times are included in the next run of the journey. Every time the journey runs, all segment members start the journey even if they previously entered the journey.

      The repeating schedule is evaluated from the start date and time using 24 hours for days and 7 days for weeks. For months, the same date on the new month is used and if the month doesn't have that date, the last day of the month is used. For example, a journey starting on January 31 and repeating every month will run on January 31, February 28 (or February 29 if it's a leap year), March 30, April 31, and so on.
- Set the **start date and time**: Specify the start date and time when you want the journey to start. You can specify the time zone for the journey's relative start date and time. Once set, the time is converted to UTC to normalize all journey times across different user time zones.

## Other journey configurations

Once you are in the journey editor, you can modify or enhance the journey configurations to exclude members on entry or exit, set goals, or cap the frequency of the journey so that the same person isn't saturated by messages across multiple journeys. You can freely modify these settings before the journey has been published. Once the journey has been published, some of these settings may not be editable due to the fluid state of people in the live journey.

- **Entry**: In the **Entry** settings, you can modify the segments included, change the frequency, add segments to exclude from the journey, change the start or end time, or limit the rate at which people enter the journey.
  - **Exclude segments**: There's no limit to the number of segments you can list to be excluded; however, if the segments are large, it can slow the performance of the journey. For large exclusions, it's best to edit the segment definition and include the excluded segments there for better performance.
  - **Rate limit**: If you choose to limit the rate at which people enter the journey, you can specify how many people per day or per hour should enter. You can also specify which days of the week new audience members should start the journey to spread out the entry flow throughout the week.
- **Exit**: In the **Exit** setting you can specify that people should exit the journey if they engage a trigger or belong to a particular segment.
  - **Exit when a trigger occurs**: Sometimes you want a person to exit a journey if they complete a specific action. For example, if a person views a product detail page on your website but doesn't purchase and the journey sends them a reminder email every day to complete the purchase, you want them to exit the journey if they complete the purchase. In this case, you want the person to exit the journey if they trigger a purchase completion for that item.
  - **Exit by segments**: Sometimes you want a person to exit if they become a member of a segment or multiple segments. For example, you may have a nurture journey for a segment of people who have never purchased from your brand before; however, once they make a purchase they move into the loyalty segment and you want them to exit the journey. As soon as they become a member of the loyalty segment, you want them to exit the first-time buyer journey.
- **Goal** Measuring marketing impact is key to calculating return on investment and justifying ongoing marketing budgets. As such, you may want to set a goal for the journey with a target outcome you're hoping to reach so that you can monitor the success of the journey against your goals. You can choose from a list of pre-defined goals or create custom goal title and associate it with the trigger that indicates when that goal is met. You can specify targets by number or by percentage of people who meet the goal. Once the journey is live, you can watch for the results.
- **Additional settings** You can specify message frequency caps to ensure people don't experience message fatigue from promotional messaging. For example, you may not want to send promotional messages to a person more than once per week to avoid them unsubscribing. In **Settings**, you can set up the frequency caps most relevant to your business and then apply them, avoiding commercial messages such as password reset confirmations, to ensure operational messages are always delivered. You can also choose not to apply frequency caps to the journey.

## Add the announcement messages

Use the plus sign (**+**) on the journey canvas to add the individual steps in your journey.

1. **Send an email**: Because the first step of the journey is to send the product announcement, select the *Product announcement email*. For the **Send to** field, select the attribute that contains the email address you want to send the email to.
1. **Add an if/then branch**: Set the **Branch off this** property to the previous *Product announcement email*. You want to **Wait for** the *Email link clicked* event. For **Which link**, select the link to view the product details. Finally, set the time limit to *1 day* to indicate that customers have up to one day after receiving the email to select the product link.
1. **Add a wait**: If customers select the view product link within one day, they proceed down the **Yes** branch. Under the yes branch, add a Wait and select *Until a specific date and time*. Here, you can specify the exact date and time that the product will launch. This is helpful if, say, the product launches a few days after your email announcement. Customers wait on this step until the specific date and time. If the date and time has already passed, customers will immediately proceed to the next step.  
1. **Send a text message**: After waiting for the product launch, you can send the *Product launched text message*. For the **Send to** field, select the attribute that contains the phone number you want to send the text message to.

## Publish the journey

After adding all the steps to the journey canvas, the journey is ready to go live and message real customers. Before publishing the journey, make sure all related content (email, text messages, and push notifications) is in the **Ready to send** state. The journey can't be modified after it's published, so it's a good idea to verify that all the steps in the journey are exactly how you want them before publishing.

Once the journey is published and live, you can look at the journey [analytics page](real-time-marketing-analytics.md) to understand how it's performing.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
