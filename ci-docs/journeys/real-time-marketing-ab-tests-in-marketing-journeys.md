---
title: A/B tests in Customer Insights - Journeys 
description: Test different content and channels in Dynamics 365 Customer Insights - Journeys to gain insights into how best to reach your customers.
ms.date: 02/04/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-desc
  - ai-seo-date:08/15/2023
---

# A/B tests in Dynamics 365 Customer Insights - Journeys

Customer Insights - Journeys uses powerful A/B tests to examine your trigger-based customer journeys, letting you gain insights into how best to reach your customers.

Using A/B tests, you can measure which channel or content messaging strategy leads to higher success. Each test compares a control group of users (version A) against a variant (version B). The control group receives a default experience. The variant group receives a different experience or message. By comparing the results of the groups, you can determine which is the most effective.

A/B testing requires a significantly sized audience to be effective. Running tests on audiences of less than 1,000 can produce unexpected results such as unequal distributions in the variants. Running tests on extremely small groups almost always produces disproportionate distributions. For example, if your audience only has ten members, it's possible that one might go to variant A while nine go to variant B. This is expected behavior when the audience size is so small that the statistical model doesn't have enough data to reach the required distribution.

## Example 1: Creating an A/B test for trigger-based journeys

Imagine you want to test two different emails on a trigger-based journey that activates when someone completes a purchase.

1. Create your initial content in the email editor as usual. Perfect the content and check it for errors to ensure it can go live.
1. When your content is ready, go to **Customer Insights - Journeys** > **Engagement** > **Journeys** and select an existing journey or create a new one.
1. After you select a journey, select the plus sign (**+**) to add an element, and then follow these steps:
    - Select **Test which variation performs better**.
- Select the channels you want to test. In this example, you want to test two emails: select one for version A and one for version B, then select **Create test**.
1. When you select the A/B test tile, the side pane opens.

    > [!div class="mx-imgBorder"]
    > ![A/B test side panel.](media/real-time-marketing-enter-ab-test-details.png "A/B test side panel")

    The pane contains the following parameters:

- **Display name**: To identify your test, enter a name for it. This name is displayed in the A/B test panel and in the customer journey analytics when you look at which tests are running.
- **Versions**: Pick the content for the channel you prepared in step one (in this case, the two emails you want to test). You can do this through a dropdown list by either selecting the child tiles in the journey builder or by making a selection on the side panel.
- **Initial Audience**: This is the audience group you want to hold back from the A/B test before you get the results. This option is only available for segment-based journeys since you already have a total number of customers to help you decide how many you want to hold back. Trigger-based journeys don’t have this option as customers enter when they complete an action. As such, the total number of customers who enter the journey is unknown.
- **Experiment distribution**: Choose the audience distribution you want. The slider is automatically on 50-50, but you can set the slider to your desired distribution. The minimum a version can receive is 10 percent, and the maximum is 90 percent. Remember that, traditionally, version A is your control group and version B is your variant.
- **Winning metric**: Set the winning condition for your test by choosing a winning metric: the version with the most journey goal events hit, the most clicks, or the most opens. For this case, you want to increase your open rates, so you'll choose the open rate option.
- **This test ends**: Choose between ending the test automatically or at a specific date and time. Letting the test determine a winner automatically occurs when the results reach statistical significance. This means that once a clear winner is determined, the system sends the winning version to the rest of your audience. The losing version is discarded. If you choose statistical significance as an option to end the A/B test but there's no clear winner after 30 days, the system automatically sends the default version. If you end the test early, it can take up to four hours to release the control group.
- **Default version**: Lastly, choose a default version in case the test doesn't end successfully. If a winner isn't determined by the deadline specified through the date and time, the default version is automatically sent.
1. The A/B test should look like this when you configure everything and you're ready to publish the journey:

    > [!div class="mx-imgBorder"]
    > ![A/B test side panel is configured and ready for journey creation](media/real-time-marketing-ready-to-publish-journey.png "A/B test side panel is configured and ready for journey creation")

## Example 2: Creating an A/B test for segment-based journeys

Imagine you want to create a journey to welcome new members who joined your loyalty program this month. You want to increase your open rate by testing two different subject lines.

You'll complete steps one through three outlined in the first example, but you'll notice that the side pane looks different. This is because with segment-based journeys, you have a total number of customers to begin with; this allows you to create two types of A/B tests.

1. **A/B test with no control group**: This A/B test behaves similarly to trigger-based journeys where customers funnel through the test as they come until a winner is determined.
 
    > [!div class="mx-imgBorder"]
    > ![A/B test with no control group](media/real-time-marketing-ab-test-with-no-control-group.png "A/B test with no control group")

1. **A/B test with a control group**: This allows you to tell the system exactly how many customers you want to test. For instance, if your segment has 100 loyalty members, you might first test on 20 percent or 20 members where each version receives 10 members. After the A/B test, the remaining 80 members receive the winning version. You can always adjust the initial audience and the distribution to your liking.
 
    > [!div class="mx-imgBorder"]
    > ![A/B test with control group](media/real-time-marketing-ab-test-with-control-group.png "A/B test with control group")

For this example, we're using an A/B test with a control group. All the other settings are the same as in example one.

## Monitor the lifecycle of your A/B tests

After you've published your journey, you can open it to track the lifecycle of your tests.

- **Draft**: These tests haven't run yet, so you can still edit the settings.
- **In progress**: These tests are currently being run. The settings are locked, and you can’t make significant changes.
- **Stopped**: These tests are stopped, and the marketer can choose which version to send.
- **Ended**: These tests were completed by finding a statistically significant winner or by timing out when scheduled to end at a set date and time. Ended tests can't be reused.

## Understand your results

:::image type="content" source="media/real-time-marketing-goal-analytics.png" alt-text="Goal analytics screenshot." lightbox="media/real-time-marketing-goal-analytics.png":::

There are three possible A/B test result outcomes:

- **Test concluded with a clear winner**: The test concluded that one version is performing better than the other. The winning version has a “winner” badge and is distributed to any new customers that funnel through the journey.
- **Test was not conclusive**: The test concluded that recipients are as likely to engage with version A as with version B. In this case, the default version is sent to any new customers that funnel through the journey.
- **The test was stopped**: This means that you or one of your coworkers stopped the test before it could conclude. In this case, the version specified by you or your coworker is sent to any new customers that funnel through the journey.

## FAQ

1. Can I have an A/B test with more than two versions?
    - No, not at the moment.
1. Why am I not seeing the control group option for segment-based journeys?
    - If you put an attribute branch or any tile that changes the total number of the segment, the control group option goes away because the system doesn't know how many customers to hold back until the test is completed.
1. Why is my test ending unexpectedly?
    - If you choose to end the test with statistical significance, the system tries to get a winner within the first 30 days from the time you publish the journey. If no version is declared a winner, the test ends and the default version is sent to the remaining audience.
 
[!INCLUDE [footer-include](./includes/footer-banner.md)]
